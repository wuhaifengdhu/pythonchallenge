# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
import requests
from PIL import Image
from cStringIO import StringIO


class T31(Challenge):
    def do_compute(self):
        # step 1, get information from web source
        question = TextHelper.find_text_between_tag(self.web_source, '<title>', '</title>')
        print "The title asked us: %s" % question
        answer = ("kohsamui", "thailand")
        self.result.set_user_password(answer[0], answer[1])
        print "Set next level user, password = (%s, %s)" % answer
        print "Search google by this photograph, you can find the place: %s, %s" % answer
        prompt = TextHelper.find_text_between_tag(self.web_source, '<a href="', '"><img src')
        new_url = WebHelper.join_url(self.url, prompt)
        print "Get prompt jpg url: %s" % new_url
        new_web_content = WebHelper.get_auth_web_source2(new_url, answer)
        print TextHelper.find_text_between_tag(new_web_content, '<font color="gold">', '</font>')
        mandelbrot_gif = TextHelper.find_text_between_tag(new_web_content, '<img src="', '" border="0">')
        mandelbrot_gif = WebHelper.join_url(new_url, mandelbrot_gif)
        print "Get new gif picture: %s" % mandelbrot_gif
        print TextHelper.find_text_between_tag(new_web_content, 'border="0">\n', '\n	</img>')

        # step 2, parse mandelbrot gif
        left, top, width, height, iteration = 0.34, 0.57, 0.036, 0.027, 128
        img = ImageHelper.create_image_from_web(mandelbrot_gif, answer[0], answer[1])
        print "Get image size: %s, %s" % img.size
        w, h = img.size
        x_step, y_step = width/w, height/h
        result = []
        for y in range(h - 1, -1, -1):
            for x in range(w):
                c = complex(left + x * x_step, top + y * y_step)
                z = 0 + 0j
                for i in range(iteration):
                    z = z * z + c
                    if abs(z) > 2:
                        break
                result.append(i)
        new_img = img.copy()
        new_img.putdata(result)
        new_img.show()

        # step 3, show diff about these two picture
        diff = [(a - b) for a, b in zip(img.getdata(), new_img.getdata()) if a != b]
        print len(diff)
        print set(diff)

        plot = Image.new('L', (23, 73))
        plot.putdata([(i < 16) and 255 or 0 for i in diff])
        plot.resize((230, 730)).show()
        prompt = 'arecibo'
        print "Oh, God dammit! Who knows this is a message humanity send to the starts from %s telescope" % prompt

        # step 4, set next challenge url
        next_level_url = WebHelper.join_url(mandelbrot_gif, prompt)
        next_level_url = WebHelper.change_suffix_url(next_level_url, 'html')
        self.set_next_level_url(next_level_url)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/ring/grandpa.html'
    print "start with url: " + current_url

    challenge = T31(current_url, True, 'repeat', 'switch')
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/rock/arecibo.html
