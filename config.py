import logging
import os

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Gitter'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = os.path.join(os.getcwd(), 'data')
BOT_EXTRA_BACKEND_DIR = os.path.join(os.getcwd(), 'err-backend-gitter')

BOT_EXTRA_PLUGIN_DIR = os.path.join(os.getcwd(), 'plugins')

BOT_LOG_FILE = os.path.join(os.getcwd(), 'errbot.log')
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('meetmangukiya', )  # !! Don't leave that to "CHANGE ME" if you connect your errbot to a chat system !!

BOT_IDENTITY = {
    'token' : '<token>'
}
