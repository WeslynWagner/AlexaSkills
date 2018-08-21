"""
This lambda code is the backend for an Alexa Skill that simulates an automated butler named 'Olaf the snowman'
Developer: Weslyn Wagner, 2018

Skeleton code borrowed from http://amzn.to/1LGWsLG
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome!"
    speech_output = "Hey guys, what's up? Need anything? " \
                    "Try asking me for the wifi password, or a tour, or a list of things I can help with. "
    #speech_output = "Welcome! "
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please let me know how I can help out. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
def get_hello_response(intent, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Hello!"
    should_end_session = True
    if 'visitors' in intent['slots']:
        visitors = intent['slots']['visitors']['value']
        speech_output = "Hello "+visitors+ "! Welcome to the snow globe, " \
                    "please make yourself at home. " \
                    "My name is Olaf and I will be your personal home assistant, " \
                    "so let me know if you need anything. " 
        reprompt_text = "What can I help with?"
    else:
        speech_output = "I'm sorry, no strangers allowed. Try asking me to welcome your friends. "
        reprompt_text = "Who would you like to welcome? "
        
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def give_wifi_secret():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Wifi password"
    speech_output = "Sure, I can give you the wifi password. " \
                    "The network is called Mi Casa Es Su Casa. " \
                    "And the password is..." \
                    "three six one, eight seven seven, five seven one eight"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Do you need me to repeat that?"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def give_capabilities_list():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "What Olaf can do:"
    speech_output = "I can do lots of things! " \
                    "Try saying, Alexa, turn off the kitchen lights, or Alexa, " \
                    "turn on the living room TV. " \
                    "I can also be your tour guide, so you can ask me things like, where is the restroom? "

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "What can I help you with? "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

        
#def set_room_attribute(room):
#    return {"Room": room}

def give_direction(intent, session):
    """ Replies to the user based on the directional input.
    """
    card_title = intent['name']
    session_attributes = {}
    should_end_session = True

    if 'Room' in intent['slots']:
        room = intent['slots']['Room']['value']
        #session_attributes = create_room_attribute(room)
        #room = session_attributes["Room"]
        speech_output = "Oh, you'd like to know where the " + room + " is? "
        reprompt_text = "Anything else I can help you find? "
        if room == "kitchen":
            speech_output = speech_output + "You're already in the kitchen!"
        elif room == "bathroom" or room == "guest bathroom":
            speech_output = speech_output + "Go to the hallway, first door on your left. "
        elif room == "bedroom" or room == "guest bedroom":
            speech_output = speech_output + "Go to the end of the hallway on your right. " \
                            "One room is on the left, and the other is on the right. "
        elif room =="study":
            speech_output = speech_output + "It's by the front door."
        else:
            speech_output = "I'm not sure where that room is. Sorry."
            reprompt_text = "Try asking me to find a different room. "
    else:
        speech_output = "I'm sorry, that room isn't available.  "
        reprompt_text = "Can I help you find another room? "
        should_end_session = True
        
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def living_room_light_off():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Living Room Light"
    speech_output = "The controller for the living room light is in the middle of the couch. " \
                    "You can use it to turn the light/fan on and off. "
    reprompt_text = None
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def watch_tv(intent, session):
    session_attributes = {}
    card_title = "Living Room TV"
    if 'television' in intent['slots']:
        speech_output = "Say Alexa, turn on the living room tv. " \
                        "Then use the Sony remote, press the home button, and choose Youtube TV, Hulu, or Netflix. "
        reprompt_text = None
        should_end_session = True
    else:
        speech_output = "I'm not sure what you mean. " \
                        "Try saying, I want to watch tv, or how do I watch Netflix?  "
        reprompt_text = None
        should_end_session = True  
        
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "It has been my pleasure to serve you. " \
                    "See ya later! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

###########################     EXAMPLES     ###########################
'''			"slots": {
				"visitors": {
					"name": "visitors",
					"value": "guests",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.9b34e7ee-6824-4c3f-bcd2-0cb33011c856.visitors",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								    "code": "ER_SUCCESS_NO_MATCH"
								    passOrFail = intent['slots']['TYPE']['resolutions']['resolutionsPerAuthority'][0]['status']['code']
'''


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}

def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Weslyn's favorite color is " + favorite_color  + \
                        ", that's cool right? Also, he loves Annat. That's cool right?"
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
###########################     EXAMPLES     ###########################


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "HelloIntent":
        return get_hello_response(intent, session)
    elif intent_name == "WifiIntent":  
        return give_wifi_secret()
    elif intent_name == "CapabilityIntent":  
        return give_capabilities_list()
    elif intent_name == "DirectionIntent":  
        return give_direction(intent, session)
    elif intent_name == "LivingRoomLightIntent":  
        return living_room_light_off()
    elif intent_name == "LivingRoomTVIntent":  
        return watch_tv(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
