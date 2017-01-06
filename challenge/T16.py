# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from PIL import Image
from cStringIO import StringIO


class T16(Challenge):
    def do_compute(self):
        # step 1, get image link from web source
        img_prompt = TextHelper.find_text_between_tag(self.web_source, "<img src=\"", "\"><br>")
        img_url = WebHelper.join_url(self.url, img_prompt)
        url_ignore, img_data = WebHelper.get_auth_url_content(img_url)
        img = Image.open(StringIO(img_data))
        img.show()
        width, height = img.size
        print width, height

        # step 2, strength the line
        new_img = Image.new('RGB', (width, height), 'black')
        for h in range(height):
            line = [img.getpixel((w, h)) for w in range(width)]
            pink = line.index(195)
            line = line[pink:] + line[:pink]
            for w, pixel in enumerate(line):
                new_img.putpixel((w, h), pixel)
        new_img.show()  # picture with words: romance

        # step 3, set prompt
        self.set_prompt("romance")


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/mozart.html'
    print "start with url: " + current_url

    challenge = T16(current_url, True)
    # challenge.do_compute()
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/return/romance.html
