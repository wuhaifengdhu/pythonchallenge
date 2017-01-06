# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.image_helper import ImageHelper
from PIL import Image, ImageDraw


class T9(Challenge):

    def do_compute(self):
        # step 1. get information from web
        first = TextHelper.find_text_between_tag(self.web_source, "first:\n", "second:").strip()
        first = [int(x) for x in first.split(',')]
        second = TextHelper.find_text_between_tag(self.web_source, "second:", "-->").strip()
        second = [int(x) for x in second.split(',')]

        # step 2. draw prompt
        img = Image.new('RGB', (500, 500))
        draw = ImageDraw.Draw(img)
        for i in range(0, len(first), 2):
            draw.line(first[i: i + 4], fill='white')
        for i in range(0, len(second), 2):
            draw.line(second[i: i + 4], fill='white')
        img.show("prompt")  # it shows a bull

        # step 3. set the prompt
        self.set_prompt("bull")


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/good.html'
    user = 'huge'
    password = 'file'
    print "start with url: " + current_url

    challenge = T9(current_url, True, user, password)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/return/bull.html
