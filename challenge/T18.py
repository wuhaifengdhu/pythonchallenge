# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.file_helper import FileHelper
from lib.image_helper import ImageHelper
from PIL import Image
from cStringIO import StringIO
import gzip, difflib


class T18(Challenge):
    def do_compute(self):
        # step 1, get prompt information from web source
        words_hint = TextHelper.find_text_between_tag(self.web_source, "<!-- ", " -->")
        print words_hint
        img_url_short = TextHelper.find_text_between_tag(self.web_source, "<img src=\"", "\" border=")
        ImageHelper.show_image_from_web(WebHelper.join_url(self.url, img_url_short))
        # It shows a same picture with different brightness
        print "brightness"
        prompt_url = WebHelper.join_url(self.url, "brightness")
        print "get new prompt url: %s" % prompt_url

        # step 2, download gz file from web
        prompt_url = WebHelper.get_prompt_url_from_web(prompt_url, "<!-- maybe consider ", " -->")
        local_gz = WebHelper.get_url_page(prompt_url)
        WebHelper.download_with_auth(prompt_url, local_gz)

        # step 3, get png data and show the image
        gz_content = FileHelper.read_gzip_file(local_gz)
        png = T18.get_png_data_from_diff_data(gz_content)

        for i in range(3):
            ImageHelper.show_image_from_data(png[i])

        # from image, we can see "../hex/bin.html", "butter", "fly"  ==> These last two words will be used in next level
        prompt_url = "../hex/bin.html"
        print 'we can see "../hex/bin.html", "butter", "fly" in these image, set new user, password for next level'
        self.result.set_user_password("butter", "fly")

        # step 4, set prompt
        self.set_prompt(prompt_url)

        # step 5, clean zip file
        FileHelper.remove_file(local_gz)

    @staticmethod
    def get_png_data_from_diff_data(gz_data):
        deltas = gz_data.splitlines()
        left, right = [], []
        for row in deltas:
            left.append(row[:53])
            right.append(row[56:])
        diff = list(difflib.ndiff(left, right))
        png = ['', '', '']
        for row in diff:
            chars = [chr(int(byte, 16)) for byte in row[2:].split()]
            if row[0] == '-':
                png[0] += ''.join(chars)
            elif row[0] == '+':
                png[1] += ''.join(chars)
            elif row[0] == ' ':
                png[2] += ''.join(chars)
        return png

if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/balloons.html'
    print "start with url: " + current_url

    challenge = T18(current_url, True)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    print "with user: %s, password: %s" % ("butter", "fly")
    # Next Challenge URL: http://www.pythonchallenge.com/pc/hex/bin.html
