# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
from lib.file_helper import FileHelper
from PIL import Image, ImageDraw


class T22(Challenge):
    def do_compute(self):
        # step 1, get prompt information from web source
        gif_prompt = TextHelper.find_text_between_tag(self.web_source, '<!-- or maybe ', ' would be more')
        gif_url = WebHelper.join_url(self.url, gif_prompt)
        print "Get gif url: %s" % gif_url

        ImageHelper.show_image_from_web(gif_url, self.user, self.password)
        local_image = WebHelper.get_url_page(gif_url)
        WebHelper.download_with_auth(gif_url, local_image, self.user, self.password)
        ImageHelper.show_from_file(local_image)

        # step 2, get Image draw
        img = Image.open(local_image)
        prompt_img = Image.new("RGB", (500, 200))
        draw = ImageDraw.Draw(prompt_img)
        cx, cy = 0, 100
        for frame in range(img.n_frames):
            img.seek(frame)
            left, upper, right, lower = img.getbbox()
            dx = left - 100
            dy = upper - 100

            if dx == dy == 0:
                cx += 50
                cy = 100

            cx += dx
            cy += dy

            draw.point([cx, cy])
        prompt_img.show()  # shows 'bonus'

        # step 3, set prompt
        prompt_words = 'bonus'
        print "get prompt words from image %s" % prompt_words
        self.set_prompt(prompt_words)

        # step 4, clean unused files
        FileHelper.remove_file(local_image)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/copper.html'
    print "start with url: " + current_url

    challenge = T22(current_url, True, 'butter', 'fly')
    challenge.do_compute()
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/hex/bonus.html
