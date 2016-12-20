# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.file_helper import FileHelper
from lib.web_helper import WebHelper
from cStringIO import StringIO
from PIL import Image


class T12(Challenge):

    def do_compute(self):
        # step 1. get prompt information
        prompt_img_url = TextHelper.find_text_between_tag(self.web_source, "<img src=\"", "\"><br>")
        img_url = T12.evil_add_url(WebHelper.join_url(self.url, prompt_img_url))
        print "get new image url: " + img_url
        local_img = WebHelper.get_url_page(img_url)
        WebHelper.download_with_auth(img_url, local_img)
        img = Image.open(local_img)
        img.show()  # shows: we should use suffix .gfx not .jpg
        img.close()

        # step 2. get gfx file
        gfx_url = WebHelper.change_suffix_url(img_url, ".gfx")
        local_gfx = WebHelper.get_url_page(gfx_url)
        WebHelper.download_with_auth(gfx_url, local_gfx)

        # step 3. play data cards
        T12.play_cards(local_gfx)

        # step 3. clean the files
        FileHelper.remove_file(local_img)
        FileHelper.remove_file(local_gfx)
        for i in range(5):
            Image.open(str(i) + ".jpg").show()
            FileHelper.remove_file(str(i) + ".jpg")

    @staticmethod
    def evil_add_url(img_url):
        page = WebHelper.get_url_page(img_url)
        page_add = page[:4] + str(int(page[4: page.index(".")]) + 1) + page[page.index("."):]
        return WebHelper.join_url(img_url, page_add)

    @staticmethod
    def play_cards(local_file):
        data = open(local_file, 'rb').read()
        for i in range(5):
            open("%d.jpg" % i, "wb").write(data[i::5])


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/evil.html'
    print "start with url: " + current_url

    challenge = T12(current_url, True)
    challenge.do_compute()
    # print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: 
