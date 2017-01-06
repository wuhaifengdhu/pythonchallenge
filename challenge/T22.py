# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
from cStringIO import StringIO
from PIL import Image


class T22(Challenge):
    def do_compute(self):
        # step 1, get prompt information from web source
        gif_prompt = TextHelper.find_text_between_tag(self.web_source, '<!-- or maybe ', ' would be more')
        gif_url = WebHelper.join_url(self.url, gif_prompt)
        print "Get gif url: %s" % gif_url

        ImageHelper.show_image_from_web(gif_url, self.user, self.password)
        # local_image = WebHelper.get_url_page(gif_url)
        # WebHelper.download_with_auth(gif_url, local_image, self.user, self.password)
        # ImageHelper.show_in_windows(local_image)

if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/copper.html'
    print "start with url: " + current_url

    challenge = T22(current_url, True, 'butter', 'fly')
    challenge.do_compute()
    # print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: