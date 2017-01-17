# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
from lib.file_helper import FileHelper
from PIL import Image
import os
import wave


class T25(Challenge):
    def do_compute(self):
        # step 1, get prompt information from web source
        print TextHelper.find_text_between_tag(self.web_source, '<!-- ', '-->')
        wav_suffix = 'wav'
        print "Above prompt words ask us to replace the suffix of jpg to %s" % wav_suffix
        wave_img_url = WebHelper.join_url(self.url, TextHelper.find_text_between_tag(self.web_source, '<img src="', '">'))
        print "wave image web url is %s" % wave_img_url
        ImageHelper.show_image_from_web(WebHelper.join_url(self.url, wave_img_url), self.user, self.password)
        print "This picture prompt us: there is 25 block, we need to combine them"

        # step 2, download waves
        wave_url = WebHelper.change_suffix_url(wave_img_url, wav_suffix)
        print "After change suffix: %s" % wave_url
        local_directory = 't25'
        FileHelper.mkdir(local_directory)
        waves = []
        for i in range(25):
            store_path = FileHelper.join_path(local_directory, WebHelper.get_url_page(wave_url))
            WebHelper.download_with_auth(wave_url, store_path, self.user, self.password)
            waves.append(wave.open(store_path))
            wave_url = WebHelper.url_add(wave_url)

        # step 3, Create combine image from waves
        img = Image.new('RGB', (300, 300), 'black')
        frames = waves[0].getnframes()
        print "Totally waves: %d" % len(waves)
        for i in range(len(waves)):
            tmp_img = Image.frombytes('RGB', (60, 60), waves[i].readframes(frames))
            current_pos = (60 * (i % 5), 60 * (i // 5))
            print "Put image to position%s" % str(current_pos)
            img.paste(tmp_img, current_pos)
        img.show()  # It shows a words 'decent'

        # step 4, set prompt words
        prompt_word = 'decent'
        print "Get prompt words from combined picture: %s" % prompt_word
        self.set_prompt(prompt_word)

        # step 5, clean unused file
        FileHelper.remove_folder(local_directory)

if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/lake.html'
    print "start with url: " + current_url

    challenge = T25(current_url, True, 'butter', 'fly')
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: 
