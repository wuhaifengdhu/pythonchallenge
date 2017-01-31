# Challenge URL: http://www.pythonchallenge.com/pc/def/0.html
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------
from lib.challenge import Challenge


class T0(Challenge):

    def do_compute(self):

        # Get result: 274877906944, update the url to 274877906944.html get next challenge url
        self.set_prompt(str(2 ** 38))


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/def/0.html'
    print "start with url: " + current_url

    challenge = T0(current_url)
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/def/274877906944.html

