import importlib
from challenge.lib.challenge import Result
from challenge.lib.web_helper import WebHelper
from challenge.lib.text_helper import TextHelper

if __name__ == '__main__':
    # step 1. Set start parameters
    start = Result()
    start.set_url('http://www.pythonchallenge.com/pc/def/0.html')

    # step 2. Run iterator to solve these challenge
    for i in range(0, 34):
        print "Level %i" % i
        print "start with url: " + start.url
        Challenger = getattr(importlib.import_module("challenge.T%i" % i), "T%i" % i)
        challenger = Challenger(start)
        start = challenger.get_result()
        print "Next Challenge URL: %s" % start.url

    # The last web page
    final_url = start.url
    web_source = WebHelper.get_auth_web_source(final_url, start.user, start.password)
    print TextHelper.find_text_between_tag(web_source, '<title>', '</title>')
    print TextHelper.find_text_between_tag(web_source, '</font>\n\n', '<br><br>')
