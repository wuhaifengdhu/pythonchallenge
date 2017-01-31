# Challenge URL:
# -----------------------------------------------------------------------------------------------------
# Process to solve the problem
# -----------------------------------------------------------------------------------------------------

from lib.challenge import Challenge
from lib.text_helper import TextHelper
from lib.web_helper import WebHelper
from lib.image_helper import ImageHelper
from lib.file_helper import FileHelper
import sys
import os


class T24(Challenge):
    def do_compute(self):
        # step 1, get information from web source
        print TextHelper.find_text_between_tag(self.web_source, '<title>', '</title>')
        print "words above indicate us to explore the maze from top to bottom"

        maze_prompt = TextHelper.find_text_between_tag(self.web_source, '<img src="', '">')
        maze_img = ImageHelper.create_image_from_web(WebHelper.join_url(self.url, maze_prompt), self.user, self.password)
        width, height = maze_img.size

        print "Find entrance in the top"
        for i in range(width):
            if maze_img.getpixel((i, 0))[2] == 0:
                entrance = (i, 0)
                print "(width=%d, height=0), pixel=(%s)" % (i, maze_img.getpixel(entrance))
                break

        print "Find export at the bottom"
        for i in range(width):
            if maze_img.getpixel((i, height - 1))[2] == 0:
                export = (i, height - 1)
                print "(width=%d, height=%d), pixel=(%s)" % (i, height - 1, maze_img.getpixel(export))

        # step 2, get out of the maze
        queue = T24.go_maze(maze_img, entrance, export)

        # step 3, get information from path
        zip_file = 'maze.zip'
        open('maze.zip', 'wb').write(''.join([chr(maze_img.getpixel(pos[0])[0]) for pos in queue[1::2]]))
        FileHelper.unzip_to_directory(zip_file, '.')

        # step 4, get prompt information from picture
        maze_jpg = 'maze.jpg'
        ImageHelper.show_from_file(maze_jpg)
        prompt_words = 'lake'
        print "Get %s in the picture" % prompt_words
        self.set_prompt(prompt_words)

        # step 5, clean unused files
        FileHelper.remove_file(maze_jpg)
        FileHelper.remove_file(zip_file)

    @staticmethod
    def print_maze(maze_img, block_char='#', empty_char=' '):
        maze_string = ''
        for i in range(maze_img.size[0]):
            for j in range(maze_img.size[1]):
                maze_string += block_char if maze_img.getpixel((j, i))[2] != 0 else empty_char
            maze_string += '\n'
        print maze_string

    @staticmethod
    def go_maze(maze_img, entrance, export):
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
        maze_data = {}
        for i in range(maze_img.size[0]):
            for j in range(maze_img.size[1]):
                maze_data[str((i, j))] = maze_img.getpixel((i, j))[2]
        maze = {'zone': maze_data, 'entrance': entrance, 'export': export, 'direction': direction}
        current_pos = [entrance, 0]
        queue = [current_pos]

        print "Starting go maze with maze%s, queue%s" % (str(maze), str(queue))
        T24.run_next_by_next(maze, queue)
        print "Get out of maze"
        return queue

    @staticmethod
    def run_next_by_next(maze, queue):
        count = 0
        while True:
            count += 1
            if len(queue) == 0:
                # This means get out of from the entrance
                print "Can not find the path from entrance%s to export%s" % (str(maze['entrance']), str(maze['export']))
                return
            current_pos = queue[len(queue) - 1]
            if current_pos[0] == maze['export']:
                # This means get out of maze from export
                print "Success get out of maze from export%s after %i iterations" % (str(maze['export']), count)
                return
            if current_pos[1] == 4:
                # This means tried all direction 0, 1, 2, 3, so this way is not right
                print "Block position%s set value to %d" % (str(current_pos[0]), maze['zone'][str(current_pos[0])])
                queue.pop()  # pop out this node
                queue[len(queue) - 1][1] += 1  # try next direction in parent node
                continue
            # check for this direction
            direction = maze['direction'][current_pos[1]]
            new_pos = (current_pos[0][0] + direction[0], current_pos[0][1] + direction[1])
            if maze['zone'][str(new_pos)] == 0:
                # Good direction, add this node into queue
                print "Added node position%s" % str(new_pos)
                maze['zone'][str(new_pos)] = 255  # block this road as it is already tried
                queue.append([new_pos, 0])
            else:
                # Bad direction, try another direction
                queue[len(queue) - 1][1] += 1


if __name__ == '__main__':
    current_url = 'http://www.pythonchallenge.com/pc/hex/ambiguity.html'
    print "start with url: " + current_url

    challenge = T24(current_url, True, 'butter', 'fly')
    print "Next Challenge URL: " + challenge.get_next_level_url()
    # Next Challenge URL: http://www.pythonchallenge.com/pc/hex/lake.html
