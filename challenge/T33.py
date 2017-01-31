# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
from lib.file_helper import FileHelper
import math
import os
from PIL import Image
from cStringIO import StringIO
import numpy as np
from scipy.stats import itemfreq
from pprint import pprint


class T33(Challenge):
    def do_compute(self):
        # step 1. get information from web source
        print TextHelper.find_text_between_tag(self.web_source, '<!--\n', '\n-->')
        beer_url = TextHelper.find_text_between_tag(self.web_source, '<img src="', '" border="0"')
        beer_url = WebHelper.join_url(self.url, beer_url)
        print beer_url
        beer_url = WebHelper.url_add(beer_url)
        beer_url = WebHelper.change_suffix_url(beer_url, 'png')

        # step 2. try out this picture
        beer_img = ImageHelper.create_image_from_web(beer_url, self.user, self.password)
        data = list(beer_img.getdata())
        local_dir = 'img_data'
        FileHelper.mkdir(local_dir)
        print len(data)
        count = 0
        while len(data) > 0:
            if self.is_int_sqrt(len(data)) and len(data) > 0:
                count += 1
                size = int(math.sqrt(len(data)))
                print "data length = %i, sqrt value = %i" % (len(data), size)
                new_img = Image.new('RGB', (size, size))
                new_img.putdata(data)
                new_img.save(os.path.join(local_dir, 'img_%i.png' % count))
            max_value = max(data)
            data = [x for x in data if x != max_value]

        # step 3, Get hint from these pictures
        print "check png under %s, you will find many characters!" % local_dir
        prompt = 'gremlins'
        print "but only characters %s are in square" % str(list(prompt))
        self.set_prompt(prompt)
        FileHelper.remove_folder(local_dir)

    @staticmethod
    def is_int_sqrt(number):
        return int(math.sqrt(number)) ** 2 == number

if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/rock/beer.html'
    print "start with url: " + current_url

    challenge = T33(current_url, True, "kohsamui", "thailand")
    final_url = challenge.get_next_level_url()
    print "Next Challenge URL: " + final_url
    # Next Challenge URL: http://www.pythonchallenge.com/pc/rock/arecibo.html

    web_source = WebHelper.get_auth_web_source(final_url, "kohsamui", "thailand")
    print TextHelper.find_text_between_tag(web_source, '<title>', '</title>')
    print TextHelper.find_text_between_tag(web_source, '</font>\n\n', '<br><br>')
