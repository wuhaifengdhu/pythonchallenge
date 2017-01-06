# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from cStringIO import StringIO
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


class T12(Challenge):

    def do_compute(self):
        # step 1. get prompt information
        prompt_img_url = TextHelper.find_text_between_tag(self.web_source, "<img src=\"", "\"><br>")
        img_url = T12.evil_add_url(WebHelper.join_url(self.url, prompt_img_url))
        print "get new image url: " + img_url
        url_ignore, img_data = WebHelper.get_auth_url_content(img_url)
        img = Image.open(StringIO(img_data))
        img.show()  # shows: we should use suffix .gfx not .jpg

        # step 2. get gfx file
        gfx_url = WebHelper.change_suffix_url(img_url, ".gfx")
        url_ignore, gfx_data = WebHelper.get_auth_url_content(gfx_url)

        # step 3. play data cards
        T12.play_cards(gfx_data)  # There were five picture shows : 'dis', 'pro', 'port', 'ional', 'ity' (strikeout)

        # step 3. set prompt for next level
        self.set_prompt('disproportional')

    @staticmethod
    def evil_add_url(img_url):
        page = WebHelper.get_url_page(img_url)
        page_add = page[:4] + str(int(page[4: page.index(".")]) + 1) + page[page.index("."):]
        return WebHelper.join_url(img_url, page_add)

    @staticmethod
    def play_cards(data):
        for i in range(5):
            img = Image.open(StringIO(data[i::5]))
            img.show()
            img.close()


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/evil.html'
    print "start with url: " + current_url

    challenge = T12(current_url, True)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/return/disproportional.html
