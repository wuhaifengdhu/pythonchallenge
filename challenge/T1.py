# Challenge URL: http://www.pythonchallenge.com/pc/def/274877906944.html
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------
from lib.challenge import Challenge
from lib.text_helper import TextHelper
f


class T(Challenge):

    def do_compute(self):

        # Step 1. Get string from source code
        encode_text = TextHelper.find_text_between_tag(self.web_source, "f000f0\">\n", "\n</tr")

        # Step 2. Translate encode_text
        from_str = string.lowercase
        to_str = from_str[2:] + from_str[:2]
        table = string.maketrans(from_str, to_str)
        print string.translate(encode_text, table)
        # Get promote to translate the url with the same table

        # Step 3. Translate url
        # Current url is http://www.pythonchallenge.com/pc/def/map.html
        self.set_prompt(string.translate("map", table))
        # Get translate message: ocr


if __name__ == '__main__':
    current_url = "http://www.pythonchallenge.com/pc/def/274877906944.html"
    print "start with url: " + current_url

    challenge = T(current_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/def/ocr.html
