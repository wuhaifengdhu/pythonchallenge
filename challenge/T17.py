# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
from urllib import quote_plus
import bz2
import xmlrpclib
import urllib2


class T17(Challenge):

    def do_compute(self):
        # step 1, get picture from web source
        prompt_url = TextHelper.find_text_between_tag(self.web_source, "<img src=\"", "\" border=\"0\"/>")
        cookie_img_url = WebHelper.join_url(self.url, prompt_url)
        ImageHelper.show_image_from_web(cookie_img_url)  # Do you feel familiar with the embed picture? Yes, the level 4
        level_4_start_url, ignore_content = WebHelper.get_final_url_content("http://www.pythonchallenge.com/pc/def/linkedlist.html")
        print "python challenge level 4 start url: " + level_4_start_url

        # step 2, get traverse start url
        cookies, level_4_web_source = WebHelper.get_cookie_content_from_url(level_4_start_url)
        cookie_prompt = ''.join(cookies)  # you+should+have+followed+busynothing...
        print "prompt from start web cookie: " + cookie_prompt
        new_para = TextHelper.find_text_between_tag(cookie_prompt, "have followed ", "...")
        print "get new para from cookie prompt: " + new_para
        origin_start_url = TextHelper.find_text_between_tag(level_4_web_source, "<center>\n<a href=\"", "\">")
        print "get origin start url: " + origin_start_url
        start_url = WebHelper.join_url(level_4_start_url, origin_start_url.replace("nothing", new_para))
        print "replace with new para, get final start url: " + start_url

        # step 3, get traverse start url
        cookies_collect = WebHelper.get_traverse_cookie(start_url, "and the next busynothing is ")
        compressed_message =  ''.join(cookies_collect)
        print "Get compressed message from cookies: " + compressed_message

        # step 4, uncompress message
        message = bz2.decompress(compressed_message)
        print "decompressed messsage: %s" % message
        # decompressed messsage: is it the 26th already? call his father and inform him that "the flowers are \
        # on their way". he'll understand.
        his_father = "Leopold"
        message = TextHelper.find_text_between_tag(message, "call his father and inform him that \"", "\". he'll ")

        # step 5, call his father
        his_father = "Leopold"
        phone_book_url = "http://www.pythonchallenge.com/pc/phonebook.php"
        phone = xmlrpclib.ServerProxy(phone_book_url)
        number = phone.phone(his_father)
        print "%s number is %s" % (his_father, number)  # Leopold number is 555-VIOLIN
        ignore_url, violin_content = WebHelper.get_auth_url_content(WebHelper.join_url(self.url, "violin"))
        print violin_content
        violin_url = TextHelper.find_pattern_in_content(violin_content, "no! i mean yes! but (.*php)")[0]
        print "violin url is %s" % violin_url
        leopold_url = WebHelper.join_url(self.url, violin_url)

        # step 6, send the message
        opener = urllib2.build_opener()
        message = "the flowers are on their way"
        opener.addheaders.append(('Cookie', 'info=' + quote_plus(message)))
        response = opener.open(leopold_url)
        leopold_prompt = response.read()

        # step 7, set next level prompt
        final_prompt = TextHelper.find_text_between_tag(leopold_prompt, "t you dare to forget the ", ".</font>")
        self.set_prompt(final_prompt)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/return/romance.html'
    print "start with url: " + current_url

    challenge = T17(current_url, True)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/return/balloons.html

