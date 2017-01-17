# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.email_helper import EmailHelper, Email
from lib.text_helper import TextHelper
from lib.file_helper import FileHelper
from lib.image_helper import ImageHelper
import hashlib
import string
import array


class T26(Challenge):
    def do_compute(self):
        # step 1, get information from web source
        web_message = TextHelper.find_text_between_tag(self.web_source, '"gold"/>\n', '\n')
        print web_message
        print TextHelper.find_text_between_tag(self.web_source, '"> <!-- ', '-->')
        print 'Prompt us to send email to leopold!\n'
        leopold_email_address = 'leopold.moz@pythonchallenge.com'
        leo_mail = Email(None, leopold_email_address, 'Apology', 'Sorry!')
        EmailHelper.send_mail(leo_mail)
        leo_response = EmailHelper.get_latest_email(leopold_email_address)
        if leo_response is not None:
            print "Response email content: %s" % leo_response.get_payload()
        # Never mind that.
        #
        # Have you found my broken zip?
        #
        # md5: bbb8b499a0eef99b52c7f13f4e78c24b
        #
        # Can you believe what one mistake can lead to?

        # step 2, decode mybroken.zip
        zip_file = 'mybroken.zip'
        repair_file = 'repair.zip'
        local_dir = 'repair'
        md5 = 'bbb8b499a0eef99b52c7f13f4e78c24b'
        data = array.array('c', open(zip_file, 'rb').read())
        if not T26.fix(data, md5):
            print "Can not fix %s!" % zip_file
        FileHelper.save_to_zip_file(data, repair_file)
        FileHelper.unzip_to_directory(repair_file, local_dir)

        # step 3, set prompt words
        ImageHelper.show_from_file(local_dir + "/mybroken.gif")
        prompt_words = 'speed' + string.split(web_message, ' ')[-1]
        print "Get words %s from picture!" % prompt_words
        self.set_prompt(prompt_words)

        # step 4, clean unused file
        FileHelper.remove_file(repair_file)
        FileHelper.remove_folder(local_dir)

    @staticmethod
    def fix(data, good_md5):
        all_chars = map(chr, range(256))
        for i, old_char in enumerate(data):
            for new_char in all_chars:
                data[i] = new_char
                if hashlib.md5(data).hexdigest() == good_md5:
                    return True
            data[i] = old_char
        return False


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/decent.html'
    print "start with url: " + current_url

    challenge = T26(current_url, True, 'butter', 'fly')
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/hex/speedboat.html
