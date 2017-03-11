import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

from ask import alexa

def lambda_handler(request_obj, context=None):
    return alexa.route_request(request_obj)

@alexa.default
def default_handler(request):
    logger.info('default_handler')
    return alexa.respond('There were 42 accidents in 2016.')

@alexa.request("LaunchRequest")
def launch_request_handler(request):
    logger.info('launch_request_handler')
    return alexa.respond('You can ask me about car accidents.')

@alexa.request("SessionEndedRequest")
def session_ended_request_handler(request):
    logger.info('session_ended_request_handler')
    return alexa.respond('Goodbye.')

@alexa.intent('AMAZON.CancelIntent')
def cancel_intent_handler(request):
    logger.info('cancel_intent_handler')
    return alexa.respond('Okay.', end_session=True)

@alexa.intent('AMAZON.HelpIntent')
def help_intent_handler(request):
    logger.info('help_intent_handler')
    return alexa.respond('You can ask me about car accidents.')

@alexa.intent('AMAZON.StopIntent')
def stop_intent_handler(request):
    logger.info('stop_intent_handler')
    return alexa.respond('Okay.', end_session=True)
