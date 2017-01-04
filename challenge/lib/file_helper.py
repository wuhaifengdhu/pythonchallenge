import shutil
import os
import gzip
from zipfile import ZipFile


class FileHelper(object):

    @staticmethod
    def remove_file(file_path):
        print "Removed file: " + file_path
        os.remove(file_path)

    @staticmethod
    def remove_folder(folder_path):
        print "Removed folder: " + folder_path
        shutil.rmtree(folder_path)

    @staticmethod
    def get_file_content(file_path):
        file_handler = open(file_path)
        data = file_handler.read()
        file_handler.close()
        return data

    @staticmethod
    def read_gzip_file(file_path):
        zip_file = gzip.open(file_path, 'r')
        content = zip_file.read()
        zip_file.close()
        return content

    @staticmethod
    def save_to_zip_file(content, local_name):
        file_opener = open(local_name, 'wb')
        file_opener.write(content)
        file_opener.close()

    @staticmethod
    def unzip_file_with_password(zip_file, password):
        zip = ZipFile(zip_file)
        zip.extractall(pwd=password)
        zip.close()
