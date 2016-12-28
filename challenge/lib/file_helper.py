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
        file_handler = open(file_path)
        data = file_handler.read()
        file_handler.close()
        return data
