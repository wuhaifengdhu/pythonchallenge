# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from PIL import Image
from cStringIO import StringIO


class T30(Challenge):
    def do_compute(self):
        # step 1, get information from the web
        prompt_jpg = TextHelper.find_text_between_tag(self.web_source, '<img src="', '" border="0"')
        print "Get img short url %s, which yankee doodle is a informal America national song!" % prompt_jpg
        prompt_jpg = WebHelper.join_url(self.url, prompt_jpg)
        print "Get prompt img url: %s" % prompt_jpg
        prompt_message = TextHelper.find_text_between_tag(self.web_source, '	<br>', '\n')
        print "Prompt Message: %s" % prompt_message
        prompt_message = TextHelper.find_text_between_tag(self.web_source, '<!-- ', ' -->')
        print "Prompt Message: %s" % prompt_message
        prompt_suffix = TextHelper.find_text_between_tag(prompt_message, 'look at the ', ' file')
        print "Prompt new suffix for the url: %s" % prompt_suffix
        prompt_url = WebHelper.change_suffix_url(prompt_jpg, prompt_suffix)
        print "Get prompt url: %s" % prompt_url

        # step 2, get prompt message



if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/ring/yankeedoodle.html'
    print "start with url: " + current_url

    challenge = T30(current_url, True, 'repeat', 'switch')
    challenge.do_compute()
    # print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL:
