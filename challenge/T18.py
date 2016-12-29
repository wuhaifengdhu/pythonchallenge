# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from PIL import Image
from cStringIO import StringIO


class T18(Challenge):
    def do_compute(self):
        pass


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/balloons.html'
    print "start with url: " + current_url

    challenge = T18(current_url)
    challenge.do_compute()
    # print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: 
