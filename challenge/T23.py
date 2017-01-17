# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
from PIL import Image
from cStringIO import StringIO
import this
import string
import re


class T23(Challenge):
    def do_compute(self):
        # step 1, get information from web
        module_prompt = TextHelper.find_text_between_tag(self.web_source, "<!-- 	it can't find it. ", '-->')
        print "First prompt to use module: %s" % module_prompt
        words_prompt = TextHelper.find_text_between_tag(self.web_source, "<!--\n'", "?'\n-->")
        print "Second prompt: %s" % words_prompt

        # step 2, translate prompt words with prompt module
        table = string.maketrans(''.join(this.d.keys()), ''.join(this.d.values()))
        message = string.translate(words_prompt, table)
        print "Message after translate: %s" % message
        pattern = string.replace(message, 'what', '(\w+)')
        text = string.translate(this.s, table)

        # step 3, get prompt
        prompt_word = re.search(pattern, text, re.I).group(1)
        print prompt_word
        self.set_prompt(prompt_word)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/bonus.html'
    print "start with url: " + current_url

    challenge = T23(current_url, True, 'butter', 'fly')
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/hex/ambiguity.html
