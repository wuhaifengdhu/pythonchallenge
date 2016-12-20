# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper


class T10(Challenge):
    def do_compute(self):
        # step 1. get prompt from web source       hint: len(a[30]) = ?
        prompt_url = TextHelper.find_text_between_tag(self.web_source, "href=\"", "\" />")
        sequence = WebHelper.get_auth_web_source(WebHelper.join_url(self.url, prompt_url))
        print sequence  # a = [1, 11, 21, 1211, 111221,

        # step 2. compute len(a[30])
        a_str = '1'
        for i in range(30):
            a_str = T10.read_string(a_str)

        # step 3. set prompt
        self.set_prompt(str(len(a_str)))

    @staticmethod
    def read_string(str_to_read):
        read_str = ''
        cur_char = str_to_read[0]
        cnt = 1
        for i in range(1, len(str_to_read)):
            if str_to_read[i] == cur_char:
                cnt += 1
            else:
                read_str += str(cnt) + cur_char
                cur_char = str_to_read[i]
                cnt = 1
        read_str += str(cnt) + cur_char
        return read_str


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/bull.html'
    print "start with url: " + current_url

    challenge = T10(current_url, True)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/return/5808.html
