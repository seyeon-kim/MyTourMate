#-*- coding:utf-8 -*-
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./My Project-1c08bc363ad2.json"
import io
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import instaloader
from datetime import datetime
import six
import csv
import re


APIResults = []

def instaCrawler(hashtag):
    # Get instance
    L = instaloader.Instaloader()

    # get_location_posts
    cnt = 0
    for post in L.get_hashtag_posts(hashtag):
        # post is an instance of instaloader.Post
        if cnt == 300:
            break
        targetTag = '#'+hashtag
        L.download_post(post, target=targetTag)
        cnt += 1
    return


def googleVisionAPI(filelists, hashtag):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    result = []
    for file in filelists:
        filename = '#'+hashtag+'/'+file+'.jpg'
        
        file_name = os.path.join(
            os.path.dirname(__file__),
            filename)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations

        labellist = []
        for label in labels:
            #print(label)
            labellist.append(label.description)
        APIResults.append(labellist)
        return


def filterFile(fileList,keywrd):
    returnlst = []
    for f in fileList:
        if keywrd in f:
            returnlst.append(f)
    return returnlst
            
def convertHashtag(line):
    return line.split('#')

def checkLines(lines):
    returnLines = []
    for line in lines:
        if line != '':
            line = line.replace('\n', '')
            returnLines.append(line)
    return returnLines

def fileConverting(hashtag, filename):
    fullName = "./#"+hashtag+"/"+filename
    f = open(fullName, 'r', encoding='utf-8')
    lines = f.readlines()
    convertLines = []
    for line in lines:
        if "#"in line:
            convertLines = convertLines + convertHashtag(line)
        else:
            convertLines.append(line)
    convertLinse = checkLines(convertLines)
    f.close()
    return convertLines

def convertFile(hashtag, tag):
    path_dir = "./#" + hashtag
    file_list = os.listdir(path_dir)
    file_list = filterFile(file_list, tag)
    fileConvertList = []
    for file in file_list:
        fileConvertList.append(fileConverting(hashtag, file))
    return fileConvertList
    
def findName(name, postID):
    for i in range(len(APIResults)):
        if name != '':
            if APIResults[i][0] == name and postID not in APIResults[i][4]:
                APIResults[i][3] += 1
                APIResults[i][4].append(postID)
                return True
    return False

def korFiltering(words):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+$')
    result = hangul.sub('', words)
    if result == '' : return None
    return result
    
def googleAPI(lines, postID):
    for text in lines:
        client = language.LanguageServiceClient()
        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')
        document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)
        entities = client.analyze_entities(document).entities
        for entity in entities:
            entity_type = enums.Entity.Type(entity.type)
            name = korFiltering(entity.name)
            if name == None: pass
            entityType = entity_type.name
            salience = entity.salience
            if entityType != 'NUMBER' and salience > 0.2 and name != '' or name != None:
                if not findName(name, postID):
                    APIResults.append([name, entityType, salience, 1, [postID]])
    return 


def makeCSV(filename, triples):
    f = open(filename + '.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    for tag in triples:
        wr.writerow(tag)
    f.close()

def main(location) :
    instaCrawler(location) 
    files = convertFile(location, '.txt')
    picfiles = convertFile(location, '.png')
    postID = 0
    for file in files:
        googleAPI(file, postID)
        googleVisionAPI(picfiles, postID)
        postID += 1
    makeCSV(location, APIResults)
    return
