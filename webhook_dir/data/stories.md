## fallback
- utter_default

## reset
* reset
    - utter_reset
* affirmation
    - utter_end
    - action_restart

## reset_deny
* reset
    - utter_reset
* deny
    - action_back

## Story 1
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_rest{"needs": "rest"}
    - slot{"needs": "rest"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "east"}
    - action_set_location
    - slot{"location": "east"}
    - utter_get_intimacy
* inform_intimacy{"intimacy": "friend"}
    - action_set_intimacy
    - slot{"intimacy": "friend"}
    - utter_get_time
* inform_time{"time": "dinner"}
    - action_set_time
    - slot{"time": "dinner"}
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart


## Story 2
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_anything_intimacy{"intimacy":"alone"}
    - slot{"intimacy": "alone"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - action_set_location
    - slot{"location": "west"}
- action_set_intimacy
    - utter_get_time
* inform_time{"time": "dinner"}
    - action_set_time
    - slot{"time": "dinner"}
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart

## Story 3
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_rest{"needs": "rest"}
    - slot{"needs": "rest"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - action_set_location
    - slot{"location": "west"}
    - utter_get_intimacy
* inform_intimacy{"intimacy": "parents"}
    - action_set_intimacy
    - slot{"intimacy": "parents"}
    - utter_get_time
* well
    - action_recom_place
* affirmation
    - utter_feedback
* deny
    - utter_sorry
    - utter_end
    - action_restart


## Story 4
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_anything
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "east"}
    - action_set_location
    - slot{"location": "east"}
    - utter_get_intimacy
* inform_intimacy{"intimacy": "pet"}
    - action_set_intimacy
    - slot{"intimacy": "pet"}
    - utter_get_time
* inform_time{"time": "noon"}
    - action_set_time
    - slot{"time": "noon"}
    - action_recom_place
* deny
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart


## Story 5
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_play{"needs": "play"}
    - slot{"needs": "play"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "north"}
    - action_set_location
    - slot{"location": "north"}
    - utter_get_intimacy
* inform_intimacy{"intimacy": "brother"}
    - action_set_intimacy
    - slot{"intimacy": "brother"}
    - utter_get_time
* inform_time{"time": "dinner"}
    - action_set_time
    - slot{"time": "dinner"}
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart


## Story 6
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_sightsee{"needs": "sightsee"}
    - slot{"needs": "sightsee"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "east"}
    - action_set_location
    - slot{"location": "east"}
    - utter_get_intimacy
* inform_intimacy{"intimacy": "alone"}
    - action_set_intimacy
    - slot{"intimacy": "alone"}
    - utter_get_time
* inform_time{"time": "morning"}
    - action_set_time
    - slot{"time": "morning"}
    - action_recom_place
* deny
    - action_recom_place
* affirmation
    - utter_feedback
* deny
    - utter_sorry
    - utter_end
    - action_restart


## Story 7
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_rest_all{"needs": "rest", "time": "dinner", "intimacy": "brother"}
    - action_set_time
    - action_set_intimacy
    - slot{"needs": "rest"}
    - slot{"time": "dinner"}
    - slot{"intimacy": "brother"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "north"}
    - action_set_location
    - slot{"location": "north"}
    - action_recom_place
* deny
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart
    

## Story 8
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_sightsee{"needs": "sightsee"}
    - slot{"needs": "sightsee"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "east"}
    - action_set_location
    - slot{"location": "east"}
    - utter_get_intimacy
* inform_intimacy{"intimacy": "alone"}
    - action_set_intimacy
    - slot{"intimacy": "alone"}
    - utter_get_time
* inform_time{"time": "morning"}
    - action_set_time
    - slot{"time": "morning"}
    - action_recom_place
* deny
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart


## Story 9
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_special{"special": "insta", "activity":"cafe"}
    - action_set_activity
    - action_set_special
    - slot{"special": "insta"}
    - slot{"activity": "cafe"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "east"}
    - action_set_location
    - slot{"location": "east"}
    - utter_get_time
* inform_time{"time": "noon"}
    - action_set_time
    - slot{"time": "noon"}
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart

## Story 10
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_special{"special": "photo"}
    - action_set_special
    - slot{"special": "photo"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - action_set_location
    - slot{"location": "west"}
    - utter_get_time
* inform_time{"time": "now"}
    - action_set_time
    - slot{"time": "now"}
    - action_recom_place
* deny
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart


## Story 11
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_anything_all{"time": "noon", "intimacy":"lover"}
    - slot{"time": "noon"}
    - slot{"intimacy": "lover"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - action_set_location
    - slot{"location": "west"}
    - action_set_time
    - action_set_intimacy
    - action_recom_place
* deny
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart

## Story 12
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_sightsee{"needs": "sightsee"}
    - slot{"needs": "sightsee"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "east"}
    - action_set_location
    - slot{"location": "east"}
    - utter_get_intimacy
* reset
    - utter_reset
* affirmation
    - utter_end
    - action_restart

## interactive_story_1
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_play{"intimacy": "friend", "needs": "play"}
    - slot{"intimacy": "friend"}
    - slot{"needs": "play"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "east"}
    - action_set_location
    - action_set_intimacy
    - slot{"location": "east"}
    - utter_get_time
* inform_time{"time": "night"}
    - action_set_time
    - slot{"time": "night"}
    - action_recom_place
* deny
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart

## interactive_story_2
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_rest_intimacy{"intimacy": "parents", "needs": "rest"}
    - slot{"intimacy": "parents"}
    - slot{"needs": "rest"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - action_set_location
    - action_set_intimacy
    - slot{"location": "west"}
    - utter_get_time
* inform_time{"time": "afternoon"}
    - action_set_time
    - slot{"time": "afternoon"}
    - action_recom_place
* affirmation
    - utter_feedback
* deny
    - utter_sorry
    - utter_end
    - action_restart

## interactive_story_3
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_rest_time{"needs": "rest", "time": "night"}
    - slot{"needs": "rest"}
    - slot{"time": "night"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "north"}
    - action_set_location
    - action_set_time
    - slot{"location": "north"}
    - utter_get_intimacy
* inform_intimacy{"intimacy": "pet"}
    - action_set_intimacy
    - slot{"intimacy": "pet"}
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart

## interactive_story_4
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_rest{"needs": "eat"}
    - slot{"needs": "eat"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - action_set_location
    - slot{"location": "west"}
    - utter_get_intimacy
* inform_intimacy{"intimacy": "children"}
    - action_set_intimacy
    - slot{"intimacy": "children"}
    - utter_get_time
* well
    - action_recom_place
* affirmation
    - utter_feedback
* deny
    - utter_sorry
    - utter_end
    - action_restart

## interactive_story_5
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_play{"time": "night", "intimacy": "friend", "needs": "play"}
    - slot{"intimacy": "friend"}
    - slot{"needs": "play"}
    - slot{"time": "night"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "east"}
    - action_set_location
    - action_set_time
    - action_set_intimacy
    - slot{"location": "east"}
    - action_recom_place
* deny
    - action_recom_place
* affirmation
    - utter_feedback
* deny
    - utter_sorry
    - utter_end
    - action_restart

## interactive_story_6
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_rest_intimacy{"intimacy": "parents", "needs": "rest"}
    - slot{"intimacy": "parents"}
    - slot{"needs": "rest"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - action_set_location
    - action_set_intimacy
    - slot{"location": "west"}
    - utter_get_time
* inform_time{"time": "dinner"}
    - action_set_time
    - slot{"time": "dinner"}
    - utter_get_time
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart

## interactive_story_7
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_rest{"needs": "rest"}
    - slot{"needs": "rest"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - action_set_location
    - slot{"location": "west"}
    - utter_get_intimacy
* inform_intimacy{"intimacy": "alone"}
    - action_set_intimacy
    - slot{"intimacy": "alone"}
    - utter_get_time
* well
    - action_recom_place
* deny
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart

## interactive_story_8
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* recommend_play{"needs": "play"}
    - slot{"needs": "play"}
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - slot{"location": "west"}
    - action_set_location
    - utter_get_intimacy
* inform_intimacy{"intimacy": "parents"}
    - slot{"intimacy": "parents"}
    - action_set_intimacy
    - utter_get_time
* reset
    - utter_reset
* deny
    - action_back
* inform_time{"time": "night"}
    - slot{"time": "night"}
    - action_set_time
    - action_recom_place
* affirmation
    - utter_feedback
* deny
    - utter_sorry
    - utter_end
    - action_restart

## interactive_story_9
* hello
    - utter_greeting
    - utter_inform
    - utter_get_needs
* reset
    - utter_reset
* deny
    - action_back
* recommend_special{"special": "photo"}
    - slot{"special": "photo"}
    - action_set_special
    - utter_ask_location
    - utter_select_location
* inform_location{"location": "west"}
    - slot{"location": "west"}
    - action_set_location
    - utter_get_time
* inform_time{"time": "dawn"}
    - slot{"time": "dawn"}
    - action_set_time
    - action_recom_place
* affirmation
    - utter_feedback
* affirmation
    - utter_thanks
    - utter_end
    - action_restart

