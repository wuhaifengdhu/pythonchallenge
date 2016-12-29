from web_helper import WebHelper
from cStringIO import StringIO
from PIL import Image


class ImageHelper(object):

    @staticmethod
    def show_image(img_url):
        img_data = WebHelper.get_auth_web_source(img_url)
        img = Image.open(StringIO(img_data))
        img.show()
        img.close()
