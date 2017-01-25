# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
import bz2


class T29(Challenge):
    def do_compute(self):
        # step 1, get information from web source
        data = ''.join(map(chr, [len(i) for i in self.web_source.splitlines()[12:]]))
        message = bz2.decompress(data)
        print "Get message from blank: %s" % message

        # step 2, set prompt information
        prompt = TextHelper.find_text_between_tag(message, 'I am ', '!')
        self.set_prompt(prompt)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/ring/guido.html'
    print "start with url: " + current_url

    challenge = T29(current_url, True, 'repeat', 'switch')
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
