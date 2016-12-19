# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.file_helper import FileHelper
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from PIL import Image


class T7(Challenge):

    def do_compute(self):
        # step 1. get png url and download
        png_prompt = TextHelper.find_text_between_tag(self.web_source, "<img src=\"", "\"/>")
        png_url = WebHelper.join_url(self.url, png_prompt)
        png_local = WebHelper.get_url_page(png_url)
        WebHelper.download(png_url, png_local)

        # step 2. get prompt information
        png = Image.open(png_local)
        row = [png.getpixel((x, png.size[1]/2)) for x in range(0, png.size[0], 7)]
        print ''.join([chr(r) for r, g, b, d in row if r == g and g == b])
        # get hint: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

        # step 3. set prompt for next url
        self.set_prompt(''.join([chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]]))

        # step . clean file
        FileHelper.remove_file(png_local)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
    print "start with url: " + current_url

    challenge = T7(current_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/def/integrity.html
