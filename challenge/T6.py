# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.file_helper import FileHelper
import zipfile


class T6(Challenge):

    def do_compute(self):
        # step 1. Get hint from page source
        hint = TextHelper.find_text_between_tag(self.web_source, "<html> <!-- <-- ", " -->\n<head>")
        zip_url = WebHelper.change_suffix_url(self.url, hint)

        # step 2. Download zip to local and extract
        tmp_zip = zip_url[zip_url.rindex("/") + 1:]
        tmp_folder = tmp_zip[: tmp_zip.index(".")]
        WebHelper.download(zip_url, tmp_zip)
        zip_ref = zipfile.ZipFile(tmp_zip, 'r')
        zip_ref.extractall(tmp_folder)
        zip_ref.close()

        # step 3. Get next hint
        readme_txt = open(tmp_folder + "/readme.txt", 'r').read()
        start_txt = TextHelper.find_text_between_tag(readme_txt, "hint1: start from ", "\n")
        next_hint = T6.read_traverse(start_txt)
        print next_hint  # Hint: Collect the comments.

        # step 4. Get comments
        print T6.collect_comments(tmp_zip, start_txt)  # Comments: HOCKEY  (Small letter oxygen)

        # step 5. Wrong way
        wrong_url = WebHelper.join_url(self.url, "hockey")
        print WebHelper.get_web_source(wrong_url)   # it's in the air. look at the letters.

        # step 6. Get next url hint
        self.set_prompt(WebHelper.join_url(self.url, "oxygen"))

        # step 7. Clean folder
        FileHelper.remove_folder(tmp_folder)
        FileHelper.remove_file(tmp_zip)

    @staticmethod
    def read_traverse(txt_name):
        txt_file = "channel/" + txt_name + ".txt"
        readme_txt = open(txt_file, 'r').read()
        print readme_txt
        if "Next nothing is " in readme_txt:
            next_name = TextHelper.find_text_between_tag(readme_txt, "Next nothing is ", "")
            print "Get next file name: " + next_name
            return T6.read_traverse(next_name)
        else:
            return readme_txt

    @staticmethod
    def collect_comments(zip_path, txt_name):
        zip_ref = zipfile.ZipFile(zip_path, 'r')
        collect = ''
        while True:
            txt_file = "channel/" + txt_name + ".txt"
            readme_txt = open(txt_file, 'r').read()
            if "Next nothing is " in readme_txt:
                collect += zip_ref.getinfo(txt_name + ".txt").comment
                txt_name = TextHelper.find_text_between_tag(readme_txt, "Next nothing is ", "")
            else:
                break
        zip_ref.close()
        return collect


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/def/channel.html'
    print "start with url: " + current_url

    challenge = T6(current_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/def/oxygen.html
