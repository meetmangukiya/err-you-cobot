import requests
import re
import os

import github3

from errbot import BotPlugin, botcmd

GH = github3.login(token=os.environ.get("GITHUB_TOKEN"))
if not GH:
    raise ValueError("Environment variable GITHUB_TOKEN not set")

class GitHub(BotPlugin):

    @botcmd(split_args_with=" ")
    def gh_assign(self, msg, args):
        """
        Assign a given issue to the user who issues the cmd.
        """
        
        issue_link = args[0]
        
        # https://github.com/:user/:repo/issues/:number
        self.log.info("Issue link", issue_link)
        issue_re = re.compile(r'https://github.com/coala/([^/]+)/issues/(\d+)')
        match = issue_re.match(issue_link)
        iss = GH.issue('coala',
                        match.group(1), # repo
                        match.group(2))  # issue number
        
        if not iss.assignee:
            self.log.info("Issue has no assignees, assigning")
            user = str(msg.frm).split('@')[0]
            iss.assign(user)
            self.send(msg.frm,
                      ":tada: You have been assigned to {}".format(issue_link))
        else:
            self.log.info("Issue has assigness", iss.assignee)
            self.send(msg.frm,
                      "Issue is already assigned, please check [other]({}) issues".format(
                      "https://github.com/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+user%3Acoala+"
                      ))
