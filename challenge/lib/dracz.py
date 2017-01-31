from web_helper import WebHelper


# This solution is copied from https://github.com/dracz/pythonchallenge/blob/master/level32.py
# My own solution is in below, but it takes too much time.
# https://github.com/wuhaifengdhu/pythonchallenge/blob/master/challenge/lib/etch_a_scetch.py
class Sketch(object):
    SPACE = " "
    MARK = "#"
    UNKNOWN = "?"

    @staticmethod
    def load_file(file_content):
        lines = [line.strip() for line in file_content.split('\n') if not line.startswith('#')]
        lines = filter(lambda x: len(x) > 0, lines)
        dimensions = map(int, lines[0].split())  # width, height
        print "Get dimension from init file: %s" % dimensions
        assert len(lines) == 1 + sum(dimensions)
        # tags for each column
        hor = [map(int, lines[i].split()) for i in range(1, 1 + dimensions[0])]
        print "Get horizontal from init file: %s" % str(hor)
        # tags for each row
        ver = [map(int, lines[i].split()) for i in range(1 + dimensions[0], len(lines))]
        print "Get vertical from init file: %s" % str(ver)
        return hor, ver

    @staticmethod
    def print_solution(res):
        """ print the solution to console """
        print("\n".join(["".join(r) for r in res]))

    @staticmethod
    def prune(cs, i, val):
        """ prune the list of list in cs to contain only those that have the specified val at index i """
        return [c for c in cs if c[i] == val]

    @staticmethod
    def iterate(hc, vc, res, col=False):
        """ iterate through one pass of the puzzles rows and columns
        :param hc: list of current possible solutions for first dimension
        :param vc: list of current possible solutions for second dimension
        :param res: the list of rows of the current solution
        :param col: whether iterating over columns or rows
        """
        for i in range(len(hc)):
            cs = hc[i]  # candidates for this row/col
            for j in [j for j in range(len(vc))]:
                r = res[i][j] if not col else res[j][i]
                if not r == Sketch.UNKNOWN:
                    continue
                if [c[j] for c in cs].count(cs[0][j]) == len(cs):
                    if not col:
                        res[i][j] = cs[0][j]  # fill in the row
                    else:
                        res[j][i] = cs[0][j]  # fill in the col
                    vc[j] = Sketch.prune(vc[j], i, cs[0][j])  # prune cols/rows

    @staticmethod
    def runs(l, w, space=SPACE, mark=MARK):
        """
        Generate list of possible runs
        :param l: list of ints specifying run lengths
        :param w: the width of the puzzle
        :param space: character to use for spaces
        :param mark: character to use for marks
        :return: list of list of bool specified whether box is marked
        """
        res = []
        for i in range(w - sum(l) - len(l) + 2):
            head = space * i + mark * l[0]
            if len(l) == 1:
                res.append(head + space * (w - len(head)))
            else:
                tails = [space + tail for tail in Sketch.runs(l[1:], w - len(head) - 1, space, mark)]
                res.extend([head + tail for tail in tails])
        return res

    @staticmethod
    def solve(hor, ver, max_iters=1000):
        """ solve a puzzle specified by the horizontal and vertical clues
        :param hor: list of list of integer clues for each row of the puzzle
        :param ver: list of list of integer clues for each column of the puzzle
        :return: a list of the rows of the puzzle solution as characters
        """
        w, h = len(ver), len(hor)
        total = w * h

        # generate all possible runs for row and column clues
        hc = [Sketch.runs(r, w) for r in hor]
        vc = [Sketch.runs(r, h) for r in ver]

        res = [[Sketch.UNKNOWN for i in range(w)] for j in range(h)]
        iters, filled = 0, 0

        # iterate until all boxes are filled in or we reach max number of iterations
        print("\nsolving...\n")
        while total - filled > 0:
            iters += 1
            Sketch.iterate(hc, vc, res, col=False)
            Sketch.iterate(vc, hc, res, col=True)
            filled = len([x for row in res for x in row if x != Sketch.UNKNOWN])
            print("filled", filled, "after", iters, "iterations")

        print("\nsolved:\n")
        Sketch.print_solution(res)
        return res

    @staticmethod
    def play_game(file_content):
        horizontal, vertical = Sketch.load_file(file_content)
        Sketch.solve(horizontal, vertical)

if __name__ == '__main__':
    file_web_url = 'http://www.pythonchallenge.com/pc/rock/up.txt'
    content = WebHelper.get_auth_web_source(file_web_url, 'kohsamui', 'thailand')
    h, v = Sketch.load_file(content)
    Sketch.solve(h, v)

