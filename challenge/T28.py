# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper


class T28(Challenge):
    def do_compute(self):
        # step 1, get information from web source
        png_url = TextHelper.find_text_between_tag(self.web_source, '<img src="', '" border="')
        png_url = WebHelper.join_url(self.url, png_url)
        print "Get png from web url: %s" % png_url
        bell_png = ImageHelper.create_image_from_web(png_url, self.user, self.password)
        green = bell_png.split()[1]
        message = ""
        for a, b in T28.paired(green.getdata()):
            diff = abs(a - b)
            if diff != 42:
                message += chr(diff)
        print 'Prompt Message: %s' % message   # whodunnit().split()[0] ?

        # step 2, set prompt
        prompt = self.whodunnit().split()[0]
        self.set_prompt(prompt.lower())

    @staticmethod
    def paired(data):
        data = iter(data)
        while True:
            yield data.next(), data.next()

    @staticmethod
    def whodunnit():
        python_creator = 'Guido van Rossum'
        return python_creator


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/ring/bell.html'
    print "start with url: " + current_url

    challenge = T28(current_url, True, 'repeat', 'switch')
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/ring/guido.html
