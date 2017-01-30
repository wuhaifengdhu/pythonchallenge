from web_helper import WebHelper


class Sketch(object):
    def __init__(self, file_content):
        self.filled = '#'
        self.unfilled = ' '
        self.table = []
        self.__basic_init(file_content)
        self.__extended_init()

    def __basic_init(self, file_content):
        lines = [line.strip() for line in file_content.split('\n') if not line.startswith('#')]
        lines = filter(lambda x: len(x) > 0, lines)
        self.dimensions = map(int, lines[0].split())  # width, height
        self.width, self.height = self.dimensions
        print "Get dimension from init file: %s" % self.dimensions
        assert len(lines) == 1 + sum(self.dimensions)
        # tags for each column
        self.column_bar = [map(int, lines[i].split()) for i in range(1, 1 + self.dimensions[0])]
        print "Get horizontal from init file: %s" % str(self.column_bar)
        # tags for each row
        self.row_bar = [map(int, lines[i].split()) for i in range(1 + self.dimensions[0], len(lines))]
        print "Get vertical from init file: %s" % str(self.row_bar)

    def __extended_init(self):
        # 1. Calculate the empty block can take for each column
        self.column_empty_blocks = [self.height - sum(r) - (len(r) - 1) for r in self.row_bar]
        print "Get max empty block for each column: %s" % str(self.column_empty_blocks)

        # 2. Calculate the max step for each column
        self.column_max_steps = [(len(r) + 1) ** (self.height - sum(r) - (len(r) - 1)) for r in self.row_bar]
        print "Get max steps for each column: %s" % str(self.column_max_steps)

        # 3. Init current step for each column
        self.column_current_steps = [0 for i in range(self.width)]
        print "Init column steps for each column: %s" % str(self.column_current_steps)

    def play_game(self):
        current = end = self.width - 1
        while not self.meet_requirement():
            print "Current column: %i, steps for each column: %s" % (current, str(self.column_current_steps))
            while self.column_current_steps[current] + 1 == self.column_max_steps[current]:
                current -= 1
                if current == -1:
                    print "There is no solution for this table, exit!"
                    return
            self.column_current_steps[current] += 1
            self.clean_after(current)
            current = end
        self.print_result()

    # After a update on current column, set all the following column adopt method from 0
    def clean_after(self, current):
        for i in range(current + 1, self.width):
            self.column_current_steps[i] = 0

    def meet_requirement(self):
        # 1. Build the current table according to self.horizontal_current_steps
        self.table = []
        for i in range(self.width):
            self.table.append(self.build_column(i))  # one column by one column

        # 2. Check requirement on vertical
        for i in range(self.height):
            if not self.meet_row_requirement(i):
                return False
        return True

    def build_column(self, c):
        place_holder = len(self.row_bar[c]) + 1
        empty_blocks = self.column_empty_blocks[c]
        digital = methods = self.column_current_steps[c]  # Max value equal (place_holder ** empty_blocks)
        empty = [0 for i in range(place_holder)]  # init empty blocks in each place holder
        for i in range(empty_blocks):
            position = digital % place_holder
            empty[position] += 1
            digital //= place_holder
        column = [0 for j in range(empty[0])]
        for i in range(len(self.row_bar[c])):
            column.extend([1 for j in range(self.row_bar[c][i])])
            column.extend([0 for j in range(empty[i + 1] + 1)])
        column.pop()  # remove the last 0
        # print "For method: %i, empty blocks: %i, place holder: %i, filled block required: %s, empty:%s, get row: %s" % \
        #       (methods, empty_blocks, place_holder, str(self.horizontal[c]), str(empty), str(column))
        return column

    def meet_row_requirement(self, r):
        row = [self.table[i][r] for i in range(self.width)]
        row_filled = []
        total = 0
        for i in range(self.width):
            if row[i] == 1:
                total += 1
            elif total != 0:
                row_filled.append(total)
                total = 0
        if total != 0:
            row_filled.append(total)
        if row_filled == self.column_bar[r]:
            return True
        else:
            # print "Row %i from table: %s" % (r, str(row))
            # print "Required: %s, Get: %s" % (str(self.vertical[r]), row_filled)
            return False

    def print_result(self):
        for i in range(self.height):
            print ''.join(map(lambda x: self.filled if x == 1 else self.unfilled,
                              [self.table[j][i] for j in range(self.width)]))


if __name__ == '__main__':
    file_web_url = 'http://www.pythonchallenge.com/pc/rock/warmup.txt'
    content = WebHelper.get_auth_web_source(file_web_url, 'kohsamui', 'thailand')
    sketch = Sketch(content)
    sketch.play_game()
