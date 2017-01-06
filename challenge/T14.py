# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from cStringIO import StringIO
from PIL import Image


class T14(Challenge):
    def do_compute(self):
        # step 1. get prompt information from web source
        words_prompt = TextHelper.find_text_between_tag(self.web_source, "<!-- ", "-->")
        print words_prompt  # remember: 100*100 = (100+99+99+98) + (...

        url_prompt = TextHelper.find_text_between_tag(self.web_source, "<img src=\"", "\" width=\"100\" height=\"100\">")
        img_url = WebHelper.join_url(self.url, url_prompt)
        print "get image url: " + img_url
        url_ignore, img_data = WebHelper.get_auth_url_content(img_url)

        # step 2. try to get information from img
        wire_img = Image.open(StringIO(img_data))
        (width, height) = wire_img.size
        print width, height   # The picture size is '10000, 1' ===> 10000 = 100 * 100

        # step 3. draw picture in square
        T14.draw_circle(wire_img)  # We can see the picture is cat

        # step 4. cat url
        cat_url = WebHelper.join_url(self.url, "cat")
        url_ignore, cat_content = WebHelper.get_auth_url_content(cat_url)
        cat_prompt = TextHelper.find_text_between_tag(cat_content, "and its name is <b>", "</b>. you'll hear from him ")

        # step 5. set prompt for the next level
        self.set_prompt(cat_prompt)

    @staticmethod
    def draw_circle(wire_img):
        img = Image.new('RGB', (100, 100), 'black')
        wire_img_current_pox = (-1, 0)
        new_img_current_pos = (-1, 0)

        for border in range(100, 0, -2):
            # Move from left to right on the top     ====> steps as prompt: 100
            for i in range(border):
                new_img_current_pos = new_img_current_pos[0] + 1, new_img_current_pos[1]
                wire_img_current_pox = wire_img_current_pox[0] + 1, wire_img_current_pox[1]
                img.putpixel(new_img_current_pos, wire_img.getpixel(wire_img_current_pox))
            # Move from top to bottom on the right   ====> steps as prompt: 99
            for i in range(border - 1):
                new_img_current_pos = new_img_current_pos[0], new_img_current_pos[1] + 1
                wire_img_current_pox = wire_img_current_pox[0] + 1, wire_img_current_pox[1]
                img.putpixel(new_img_current_pos, wire_img.getpixel(wire_img_current_pox))
            # Move from right to left on the bottom   ====> steps as prompt: 99
            for i in range(border - 1):
                new_img_current_pos = new_img_current_pos[0] - 1, new_img_current_pos[1]
                wire_img_current_pox = wire_img_current_pox[0] + 1, wire_img_current_pox[1]
                img.putpixel(new_img_current_pos, wire_img.getpixel(wire_img_current_pox))
            # Move from bottom to top on the left     ====> steps as prompt: 98
            for i in range(border - 2):
                new_img_current_pos = new_img_current_pos[0], new_img_current_pos[1] - 1
                wire_img_current_pox = wire_img_current_pox[0] + 1, wire_img_current_pox[1]
                img.putpixel(new_img_current_pos, wire_img.getpixel(wire_img_current_pox))
        img.show()


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/italy.html'
    print "start with url: " + current_url

    challenge = T14(current_url, True)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/return/uzi.html
