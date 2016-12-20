# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.web_helper import WebHelper
from lib.text_helper import TextHelper
from lib.file_helper import FileHelper
from PIL import Image


class T11(Challenge):

    def do_compute(self):
        # step 1. get picture from web
        prompt_img_url = TextHelper.find_text_between_tag(self.web_source, "<img src=\"", "\" width=\"640\" height")
        img_url = WebHelper.join_url(self.url, prompt_img_url)
        local_img = WebHelper.get_url_page(img_url)
        WebHelper.download_with_auth(img_url, local_img)

        # step 2. get odd picture
        img = Image.open(local_img)
        odd = Image.new(img.mode, (img.size[0], img.size[1]))
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if (x + y) % 2 == 0:
                    odd.putpixel((x, y), img.getpixel((x,y)))
        odd.show()  # shows: 11 evil
        odd.close()

        # step 3. set prompt
        self.set_prompt("evil")

        # step 4. clear the files
        FileHelper.remove_file(local_img)




if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/5808.html'
    print "start with url: " + current_url

    challenge = T11(current_url, True)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/return/evil.html
