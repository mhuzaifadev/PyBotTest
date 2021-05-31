import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 80
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")