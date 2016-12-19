# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
import re


class T3(Challenge):
    def do_compute(self):
        # step 1. Get text from web source
        text = TextHelper.find_text_between_tag(self.web_source)

        # step 2. Get target characters
        characters = TextHelper.find_pattern_in_content(self.web_source, '[^A-Z][A-Z]{3}(?P<Boss>[a-z])[A-Z]{3}[^A-Z]')

        # step 3. Get prompt of next level challange url
        self.set_prompt(''.join(characters))


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    print "start with url: " + current_url

    challenge = T3(current_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/def/linkedlist.html
