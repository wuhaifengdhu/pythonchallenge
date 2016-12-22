import shutil
import os


class FileHelper(object):

    @staticmethod
    def remove_file(file_path):
        print "Removed file:" + file_path
        os.remove(file_path)

    @staticmethod
    def remove_folder(folder_path):
        print "Removed folder:" + folder_path
        shutil.rmtree(folder_path)

    @staticmethod
    def get_file_content(file_path):
        return open(file_path).read()
