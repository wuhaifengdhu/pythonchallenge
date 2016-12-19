# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
import pickle


class T5(Challenge):

    def do_compute(self):
        # step 1. Get banner dump data
        banner_prompt = TextHelper.find_text_between_tag(self.web_source, "peakhell src=\"", "\"/>")
        banner_url = WebHelper.join_url(self.url, banner_prompt)
        banner_data = WebHelper.get_web_source(banner_url)

        # step 2. show the banner
        banner = ''
        for line in pickle.loads(banner_data):
            for char, count in line:
                banner += char * count
            banner += '\n'
        print banner   # Get word channel

        # step 3. Set prompt
        self.set_prompt("channel")


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/def/peak.html'
    print "start with url: " + current_url

    challenge = T5(current_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/def/channel.html
