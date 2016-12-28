# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from calendar import isleap, weekday
from PIL import Image
from cStringIO import StringIO


class T15(Challenge):
    def do_compute(self):
        # step 1, get question from web source
        words_prompt = TextHelper.find_text_between_tag(self.web_source, "<title>", "</title>")
        print words_prompt  # ask us who is this person?

        # step 2, get image from web
        prompt_url = TextHelper.find_text_between_tag(self.web_source, "<img src=\"", "\"><br>")
        img_url = WebHelper.join_url(self.url, prompt_url)
        url_ignore, img_data = WebHelper.get_auth_url_content(img_url)
        img = Image.open(StringIO(img_data))
        img.show()  # a calendar shows a date January, 26, 1XX6
        img.close()
        month = 1
        day = 26

        # step 3, calculate possible date
        possible_year = filter(lambda y: isleap(y) and 0 == weekday(y, 1, 26), range(1006, 2000, 10))
        print possible_year

        # step 4, get the date with more prompt information
        words_prompt = TextHelper.find_text_between_tag(self.web_source, "<!-- todo: ", " -->")
        print words_prompt  # prompt us the date after January, 26 is some day special for memory
        day += 1

        words_prompt = TextHelper.find_text_between_tag(self.web_source, "<center>\n<!-- ", " -->")
        print words_prompt  # prompt us choose the second youngest
        year = possible_year[-2]

        print "The day special for flower is " + str(year) + "/" + str(month) + "/" + str(day)
        # some body may know but I don't know this day is the birthday of mozart
        # https://en.wikipedia.org/wiki/January_27#Births

        # step 5, set prompt for the next leve
        self.set_prompt("mozart")


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/uzi.html'
    print "start with url: " + current_url

    challenge = T15(current_url, True)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/return/mozart.html
