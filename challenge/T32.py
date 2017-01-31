# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# This challenge want us to draw the image according to the digital in the left of the row and in the
# top of the column.
# The digital's meaning represent the continue filled block's number.
# For example: if the number is 433, that means four continue filled block, some unfilled block, 3 continue
# filled block, then some unfilled block, then 3 filled block
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.etch_a_scetch import Sketch
from PIL import Image
from cStringIO import StringIO


class T32(Challenge):
    def do_compute(self):
        # step 1, get information from web source
        print TextHelper.find_text_between_tag(self.web_source, '	<!-- ', '-->')
        print TextHelper.find_text_between_tag(self.web_source, '<font color="gold">\n', '\n        </font>')
        warm_up_url = TextHelper.find_text_between_tag(self.web_source, 'blanks <!-- for ', ' -->')
        warm_up_url = WebHelper.join_url(self.url, warm_up_url)

        # step 2, solve first etch-a-scetch
        file_content = WebHelper.get_auth_url_content(warm_up_url, self.user, self.password)[1]
        # print "Words in warmup.txt:\n%s" % file_content
        sketch = Sketch(file_content)
        # sketch.play_game()
        prompt = 'up'
        print "It shows an %s tag" % prompt
        second_file = WebHelper.join_url(warm_up_url, prompt)

        # step 3, solve the second etch-a-scetch
        file_content = WebHelper.get_auth_url_content(second_file, self.user, self.password)[1]
        sketch = Sketch(file_content)
        # sketch.play_game()
        python = 'python'
        print "It shows a picture of %s" % python

        # step 4, search the wiki get prompt information
        python_url = WebHelper.join_url(self.url, python)
        print "Python url: %s" % python_url
        file_content = WebHelper.get_auth_web_source(python_url, self.user, self.password)
        print TextHelper.find_text_between_tag(file_content, '<font color="gold">', '</font>')
        prompt = 'beer'
        print "Search on the wiki %s is the words next to Free" % prompt

        # step 5, set prompt for next url
        self.set_prompt(prompt)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/rock/arecibo.html'
    print "start with url: " + current_url

    challenge = T32(current_url, True, "kohsamui", "thailand")
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/rock/beer.html
