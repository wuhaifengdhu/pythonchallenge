# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
import bz2


class T8(Challenge):
    def do_compute(self):
        # step 1. get information from url
        login_url_prompt = TextHelper.find_text_between_tag(self.web_source, "href=\"", "\" />")
        login_url = WebHelper.join_url(self.url, login_url_prompt)
        user_encode = TextHelper.find_text_between_tag(self.web_source, "un: '", "'")
        user = bz2.decompress(user_encode.decode('string_escape'))
        print "user = " + user   # huge
        password_encode = TextHelper.find_text_between_tag(self.web_source, "pw: '", "'")
        password = bz2.decompress(password_encode.decode('string_escape'))
        print "password = " + password   # file
        self.result.set_user_password(user, password)

        # step 2. Login with user, password
        self.set_next_level_url(login_url)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
    print "start with url: " + current_url

    challenge = T8(current_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: 
