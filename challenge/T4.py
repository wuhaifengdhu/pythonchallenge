# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.web_helper import WebHelper
from lib.text_helper import TextHelper


class T4(Challenge):

    def do_compute(self):
        # step 1. Get traverse start url
        start_url_prompt = TextHelper.find_text_between_tag(self.web_source, "<center>\n<a href=\"", "\">")
        start_url = WebHelper.join_url(self.url, start_url_prompt)
        print "Get start traverse url" + start_url
        # start url is http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

        # step 2. Traverse in url, util the end url
        end_url, end_content = WebHelper.get_traverse_url_content(start_url, "and the next nothing is ")
        # end url is http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831

        # step 3. Get the next level url
        final_url, final_content = WebHelper.get_final_url_content(end_url, end_content)
        self.set_next_level_url(final_url)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.html'
    print "start with url: " + current_url

    challenge = T4(current_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/def/peak.html
