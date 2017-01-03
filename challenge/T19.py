# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.wave_helper import WaveHelper
from lib.file_helper import FileHelper
import email
from PIL import Image
from cStringIO import StringIO


class T19(Challenge):

    def do_compute(self):
        # step 1, get prompt form web source
        email_string = TextHelper.find_text_between_tag(self.web_source, "<!--\n", "\n-->")
        message = email.message_from_string(email_string)
        audio = message.get_payload(0).get_payload(decode=True)
        local_wav = "mainland.wav"
        WaveHelper.save_base64_file(audio, local_wav)
        WaveHelper.play(local_wav)  # pronounce 'sorry'
        pronounce_word = "sorry"
        print "pronounce word: %s" % pronounce_word

        # step 2, wrong try
        sorry_url = WebHelper.join_url(self.url, pronounce_word)
        url_ignore, sorry_content = WebHelper.get_auth_url_content(sorry_url, self.user, self.password)
        print sorry_content

        # step 3, reverse the wav data
        reverse_wave = "sea.wav"
        WaveHelper.reverse_wave(local_wav, reverse_wave)
        WaveHelper.play(reverse_wave)  # pronounce "you are idiot, a.a.a.a..."
        print "pronounce word: %s" % "you are idiot, a.a.a.a..."
        prompt_url = WebHelper.join_url(self.url, "idiot")
        print "prompt url: %s" % prompt_url

        # step 4, get next level url
        next_url = WebHelper.get_prompt_url_from_web(prompt_url, '<br><a href="', '">Continue to the', self.user, self.password)
        self.set_next_level_url(next_url)

        # step 5, clean resources
        FileHelper.remove_file(local_wav)
        FileHelper.remove_file(reverse_wave)


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/bin.html'
    print "start with url: " + current_url

    challenge = T19(current_url, True, "butter", "fly")
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/hex/idiot2.html
