# Challenge URL: http://www.pythonchallenge.com/pc/def/ocr.html
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------
from lib.challenge import Challenge
from lib.text_helper import TextHelper


class T(Challenge):

    def do_compute(self):

        # step 1. Get text from web source
        text = TextHelper.find_text_between_tag(self.web_source)

        # step 2. Calculate the rare characters
        text_dict = {}
        for char in text:
            if char in text_dict.keys():
                text_dict[char] += 1
            else:
                text_dict[char] = 1
        rare_characters = ''.join([char for char, count in text_dict.items() if count < 10])

        # step 3. Get next url
        ans = ''.join([char for char in text if char in rare_characters])
        self.set_prompt(ans)  # Get word 'equality'


if __name__ == '__main__':
    current_url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    print "start with url: " + current_url

    challenge = T(current_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/def/equality.html
