# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------
import zlib
import bz2
from lib.web_helper import WebHelper
from lib.file_helper import FileHelper
from lib.challenge import Challenge
from lib.challenge import Result


class T21(Challenge):
    def do_compute(self):
        # step 1. Get information from file
        output = ""
        with open(self.file_name, "rb") as f:
            data = f.read()
            while True:
                if data.startswith(b'x\x9c'):
                    data = zlib.decompress(data)
                    output += ' '
                elif data.startswith(b'BZh'):
                    data = bz2.decompress(data)
                    output += '#'
                elif data.endswith(b'\x9cx'):
                    data = data[::-1]
                    output += '\n'
                else:
                    break
            print(output)  # COPPER
            prompt = 'copper'
            print "From the print image we can see word %s" % prompt

        # step 2. set prompt
        self.set_prompt(prompt)

        # step 3. clean unused file
        FileHelper.remove_file(self.file_name)


if __name__ == '__main__':
    last_level_url = 'http://www.pythonchallenge.com/pc/hex/idiot2.html'
    local_file = 'package.pack'
    result = Result()
    result.set_url(last_level_url)
    result.set_file(local_file)
    result.set_user_password('butter', 'fly')
    challenge = T21(result)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/hex/copper.html
