# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.web_helper import WebHelper
from lib.text_helper import TextHelper
import xmlrpclib


class T13(Challenge):
    def do_compute(self):
        # step 1. get hint from web source
        prompt_url = TextHelper.find_text_between_tag(self.web_source, "coords=\"326,177,45\" href=\"", "\" />")
        phone_book_url = WebHelper.join_url(self.url, prompt_url)

        # step 2. use xmlrpclib
        server = xmlrpclib.Server(phone_book_url)
        print server.phone('Bert')   # print 555-ITALY

        # step 3. set prompt
        self.set_prompt('italy')


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/disproportional.html'
    print "start with url: " + current_url

    challenge = T13(current_url, True)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/return/italy.html
