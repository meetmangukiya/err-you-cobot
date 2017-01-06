import re
import random

from errbot import BotPlugin, re_botcmd

class Coala(BotPlugin):

    def callback_message(self, msg):
        """
        Shout at the user for using an upercased c in coala.
        """
        emots = [":(", ":angry:", ":anger:", ":confounded:",
                 ":disappointed:", ":triumph:"]
        
        match = re.search(r'C+[Oo]+[Aa]+[Ll]+[Aa]+', msg.body)
        if match:
            self.send(msg.frm,
                      "@{} coala is always written in lowercase c. {}".format(
                                                        str(msg.frm).split('@')[0],
                                                        emots[random.randint(0,
                                                              len(emots) - 1)]))
