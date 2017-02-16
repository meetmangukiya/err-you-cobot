import random

from errbot import BotPlugin, botcmd


class ShipIt(BotPlugin):
    """
    Displays the Ship It squirel!
    """

    squirrels = [
      "http://shipitsquirrel.github.io/images/ship%20it%20squirrel.png",
      "http://dougbelshaw.com/blog/wp-content/uploads/2013/10/ship-it-squirrel.jpg",
      "http://i.imgur.com/ApTAkDm.gif",
      "http://i.imgur.com/DPVM1.png",
      "http://d2f8dzk2mhcqts.cloudfront.net/0772_PEW_Roundup/09_Squirrel.jpg",
      "http://www.cybersalt.org/images/funnypictures/s/supersquirrel.jpg",
      "http://www.zmescience.com/wp-content/uploads/2010/09/squirrel.jpg",
      "https://dl.dropboxusercontent.com/u/602885/github/sniper-squirrel.jpg",
      "http://1.bp.blogspot.com/_v0neUj-VDa4/TFBEbqFQcII/AAAAAAAAFBU/E8kPNmF1h1E/s640/squirrelbacca-thumb.jpg",
      "https://dl.dropboxusercontent.com/u/602885/github/soldier-squirrel.jpg",
      "https://dl.dropboxusercontent.com/u/602885/github/squirrelmobster.jpeg",
    ]

    @botcmd  # flags a command
    def ship_it(self, msg, args):  # a command callable with !tryme

        return random.choice(self.squirrels)  # This string format is markdown.
