# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
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
        raw_data = WebHelper.get_auth_web_source(prompt_url, self.user, self.password)
        data = [x.strip() for x in raw_data.split(",")]
        length = len(data)
        print "Length of data: %s" % length
        factors = [x for x in range(2, length) if length % x == 0]

        img = Image.new('F', (factors[0], factors[1]))
        img.putdata([float(x) for x in data], 256)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img = img.transpose(Image.ROTATE_90)
        # img.show()

        # step 3, set prompt
        res = ''.join(map(chr, [int(x[0][5] + x[1][5] + x[2][6]) for x in zip(data[0::3], data[1::3], data[2::3])]))
        print res
        prompt = TextHelper.find_text_between_tag(res, 'look at ', '",')
        self.set_prompt(prompt)

if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/ring/yankeedoodle.html'
    print "start with url: " + current_url

    challenge = T30(current_url, True, 'repeat', 'switch')
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/ring/grandpa.html
