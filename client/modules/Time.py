# -*- coding: utf-8-*-
import datetime
import re
from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = ["TIME"]


def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    tz = getTimezone(profile)
    now = datetime.datetime.now(tz=tz)
    service = DateService()
    response = service.convertTime(now)

    comment = ''
    if now.hour > 19:
        comment = ' It is time to be sleeping.'
    mic.say("It is {0} right now. {1}".format(response, comment) )


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\btime\b', text, re.IGNORECASE))
