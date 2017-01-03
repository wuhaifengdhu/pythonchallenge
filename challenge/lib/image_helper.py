from web_helper import WebHelper
from cStringIO import StringIO
from PIL import Image


class ImageHelper(object):

    @staticmethod
    def show_image_from_web(img_url):
        img_data = WebHelper.get_auth_web_source(img_url)
        ImageHelper.show_image_from_data(img_data)

    @staticmethod
    def show_image_from_data(data):
        img = Image.open(StringIO(data))
        img.show()
        img.close()
