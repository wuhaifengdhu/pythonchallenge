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


class T28(Challenge):
    def do_compute(self):
        # step 1, get information from web source
        png_url = TextHelper.find_text_between_tag(self.web_source, '<img src="', '" border="')
        png_url = WebHelper.join_url(self.url, png_url)
        print "Get png from web url: %s" % png_url
        bell_png = ImageHelper.create_image_from_web(png_url, self.user, self.password)
        green = list(bell_png.split()[1].getdata())

        diff = [abs(a - b) for a, b in zip(green[0::2], green[1::2])]
        filtered = list(filter(lambda x: x != 42, diff))
        decoded = bytes(filtered).decode()
        print str(decoded)



if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/ring/bell.html'
    print "start with url: " + current_url

    challenge = T28(current_url, True, 'repeat', 'switch')
    challenge.do_compute()
    # print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: 
