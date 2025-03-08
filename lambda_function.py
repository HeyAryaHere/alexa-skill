import logging
import json
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    """Handles skill launch"""
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speak_output = "Welcome! I can help plan your day. Just say 'Plan my day'."
        return handler_input.response_builder.speak(speak_output).ask(speak_output).response

class PlanMyDayIntentHandler(AbstractRequestHandler):
    """Handles the PlanMyDayIntent"""
    def can_handle(self, handler_input):
        return is_intent_name("PlanMyDayIntent")(handler_input)

    def handle(self, handler_input):
        # Placeholder: We will integrate Google Calendar and Gmail scraping here
        speak_output = "I'm gathering your schedule and to-do list. Please wait..."
        return handler_input.response_builder.speak(speak_output).response

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(PlanMyDayIntentHandler())

lambda_handler = sb.lambda_handler()
