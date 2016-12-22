import re


class TextHelper(object):

    @staticmethod
    def find_text_between_tag(content, start_tag="<!--\n", end_tag="\n-->"):
        try:
            start_index = content.rindex(start_tag) + len(start_tag)
        except ValueError as TAG_NOT_FOUND_ERROR:
            print "start tag: " + start_tag + " not found in :" + content
            return
        content = content[start_index:]

        if len(end_tag) == 0:
            return content
        try:
            end_index = content.index(end_tag)
        except ValueError as TAG_NOT_FOUND_ERROR:
            print "end tag: " + end_tag + " not found in :" + content
            return
        return content[:end_index]

    @staticmethod
    def find_pattern_in_content(content, pattern_str):
        pattern = re.compile(pattern_str)
        return re.findall(pattern, content)