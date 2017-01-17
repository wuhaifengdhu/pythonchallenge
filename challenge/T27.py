# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
from PIL import Image
import bz2
import keyword
import string


class T27(Challenge):
    def do_compute(self):
        # step 1, get information from web source
        bell_url = TextHelper.find_text_between_tag(self.web_source, '<a href="', '">')
        bell_url = WebHelper.join_url(self.url, bell_url)
        print "Find some url: %s" % bell_url
        zigzag_jpg = TextHelper.find_text_between_tag(self.web_source, '<img src="', '"> <!--')
        zigzag_jpg = WebHelper.join_url(self.url, zigzag_jpg)
        print "Find a picture: %s" % zigzag_jpg
        gif_prompt = TextHelper.find_text_between_tag(self.web_source, 'did you say ', '? -->')
        gif_url = WebHelper.change_suffix_url(zigzag_jpg, gif_prompt)
        print "Get a gif picture: %s" % gif_url

        # step 2, deal with gif
        img = ImageHelper.create_image_from_web(gif_url, self.user, self.password)
        img_content = img.tobytes()
        img_plt = img.palette.getdata()[1][::3]
        trans = string.maketrans("".join([chr(i) for i in range(256)]), img_plt)
        img_tran = img_content.translate(trans)
        diff = ["", ""]
        img = Image.new("1", img.size, 0)
        for i in range(1, len(img_content)):
            if img_content[i] != img_tran[i - 1]:
                diff[0] += img_content[i]
                diff[1] += img_tran[i - 1]
                img.putpixel(((i - 1) % img.size[0], (i - 1) / img.size[0]), 1)
        img.show()  # two words shows in picture: 'not', 'word', between is an key
        text = bz2.decompress(diff[0])
        auth = set()
        for i in text.split():
            if not keyword.iskeyword(i):
                auth.add(i)
        # print repeat, switch, ../ring/bell
        print auth

        # step 3, set next level url
        for key in auth:
            if 'html' in key:
                self.set_prompt(key)
                auth.remove(key)
                print auth
                break


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/speedboat.html'
    print "start with url: " + current_url

    challenge = T27(current_url, True, 'butter', 'fly')
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/ring/bell.html
