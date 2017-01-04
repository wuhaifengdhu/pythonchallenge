# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.file_helper import FileHelper
from PIL import Image
from cStringIO import StringIO
import re
import requests
from requests.auth import HTTPBasicAuth


class T20(Challenge):
    def do_compute(self):
        # step 1, get prompt information from web source
        unreal_img_url = WebHelper.join_url(self.url, TextHelper.find_text_between_tag(self.web_source, "<img src=\"",
                                                                                       "\" border="))
        print "Get image url: %s" % unreal_img_url
        response = requests.get(unreal_img_url, auth=HTTPBasicAuth(self.user, self.password))
        print "Headers: %s" % response.headers

        # step 2, loop to get more information
        response = self.loop_next_range(unreal_img_url, response.headers)
        # Information: Why don't you respect my privacy?
        response = self.loop_next_range(unreal_img_url, response.headers)
        # Information: we can go on in this way for really long time.
        response = self.loop_next_range(unreal_img_url, response.headers)
        # Information: stop this!
        response = self.loop_next_range(unreal_img_url, response.headers)
        # Information: invader! invader!
        response = self.loop_next_range(unreal_img_url, response.headers)
        # Information: ok, invader. you are inside now.
        (start, end, length) = self.get_content_range(response.headers['content-range'])
        invader_prompt = TextHelper.find_text_between_tag(response.content, 'ok, ', '. you are inside now.')
        invader_url = WebHelper.join_url(self.url, invader_prompt)
        print "Get invader url : %s" % invader_url
        response = self.loop_next_range(invader_url)
        # Information: Yes! that's you!

        # step 3, try cross the border
        response = requests.get(unreal_img_url, headers={'Range': 'bytes=%i-' % (int(length) + 1)}, auth=(
            self.user, self.password))
        (start, end, length) = self.get_content_range(response.headers['content-range'])
        print "Headers: %s" % response.headers
        print "Information: %s" % response.content  # esrever ni emankcin wen ruoy si drowssap eht

        content_reverse = response.content.strip()[::-1]
        print "reverse content: %s" % content_reverse  # the password is your new nickname in reverse
        invader_password = invader_prompt[::-1]
        print "invader password is %s" % invader_password

        response = requests.get(unreal_img_url, headers={'Range': 'bytes=%i-' % (int(start) - 1)}, auth=(
            self.user, self.password))
        print "Headers: %s" % response.headers
        print "Information: %s" % response.content  # 'and it is hiding at 1152983631.\n'

        prompt_start = TextHelper.find_text_between_tag(response.content, 'it is hiding at ', '.\n')
        response = requests.get(unreal_img_url, headers={'Range': 'bytes=%i-' % (int(prompt_start))}, auth=(
            self.user, self.password))
        local_zip_file = 'invader.zip'
        FileHelper.save_to_zip_file(response.content, local_zip_file)

        # step 4, unzip local zip file
        FileHelper.unzip_file_with_password(local_zip_file, invader_password)

    @staticmethod
    def get_content_range(content_range):
        pattern = re.compile('bytes (\d+)-(\d+)/(\d+)')
        return pattern.search(content_range).groups()

    def loop_next_range(self, web_url, last_headers=None):
        if last_headers is not None:
            (start, end, length) = self.get_content_range(last_headers['content-range'])
            print "%s-%s/%s" %(start, end, length)
            response = requests.get(web_url, headers={'Range': 'bytes=%i-' % (int(end) + 1)}, auth=(self.user,
                                                                                                    self.password))
        else:
            response = requests.get(web_url, auth=(self.user, self.password))
        print "Headers: %s" % response.headers
        print "Information: %s" % response.content
        return response


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/idiot2.html'
    print "start with url: " + current_url

    challenge = T20(current_url, True, 'butter', 'fly')
    challenge.do_compute()
    # print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: 
