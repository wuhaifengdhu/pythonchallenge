# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------
import zlib
import bz2
from lib.web_helper import WebHelper


class T21(object):
    def __init__(self, local_file, web_url):
        self.file_name = local_file
        self.url = web_url
        self._next_level_url = ''
        self.unwrap()

    def unwrap(self):
        result = ""
        with open(self.file_name, "rb") as f:
            data = f.read()
            while True:
                if data.startswith(b'x\x9c'):
                    data = zlib.decompress(data)
                    result += ' '
                elif data.startswith(b'BZh'):
                    data = bz2.decompress(data)
                    result += '#'
                elif data.endswith(b'\x9cx'):
                    data = data[::-1]
                    result += '\n'
                else:
                    break
            print(result)  # COPPER
            self._next_level_url = WebHelper.join_url(self.url, 'copper')

    def get_next_level_url(self):
        return self._next_level_url


if __name__ == '__main__':
    last_level_url = 'http://www.pythonchallenge.com/pc/hex/idiot2.html'
    local_file = 'package.pack'
    challenge = T21(local_file, last_level_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/hex/copper.html
