# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from cStringIO import StringIO
from PIL import Image


class T22(Challenge):
    def do_compute(self):
        # step 1, get prompt information from web source
        gif_prompt = TextHelper.find_text_between_tag(self.web_source, '<!-- or maybe ', ' would be more')
        gif_url = WebHelper.join_url(self.url, gif_prompt)
        print "Get gif url: %s" % gif_url

        url_ignore, img_data = WebHelper.get_auth_url_content(gif_url, self.user, self.password)
        img = Image.open(StringIO(img_data))
        print img.size
        im2 = img.point(lambda p: p * 0.5)
        im2.save("angelababy.jpg")


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/copper.html'
    print "start with url: " + current_url

    challenge = T22(current_url, True, 'butter', 'fly')
    challenge.do_compute()
    # print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: