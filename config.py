import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Text'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'/home/phoenista/Desktop/ghubby/cobot/err-you-cobot/data'
BOT_EXTRA_PLUGIN_DIR = '/home/phoenista/Desktop/ghubby/cobot/err-you-cobot/plugins'

BOT_LOG_FILE = r'/home/phoenista/Desktop/ghubby/cobot/err-you-cobot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('CHANGE ME', )  # !! Don't leave that to "CHANGE ME" if you connect your errbot to a chat system !!