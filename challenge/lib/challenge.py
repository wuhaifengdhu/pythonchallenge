from web_helper import WebHelper


class Challenge(object):

    def __init__(self, url, need_authentication=False, user_name='huge', pass_word='file'):
        if need_authentication:
            self.url, self.web_source = WebHelper.get_auth_url_content(url, user_name, pass_word)
        else:
            self.url, self.web_source = WebHelper.get_final_url_content(url)
        self._prompt = None
        self._next_level_url = None

    def get_next_level_url(self):
        # compute next level url, set prompt or next_level_url
        self.do_compute()
        # get next level url
        if self._next_level_url is not None:
            return self._next_level_url
        if self._prompt is not None:
            self._next_level_url = WebHelper.join_url(self.url, self._prompt)
            return self._next_level_url
        else:
            print "do_compute should set at least one value of [prompt, next_level_url]"
            return

    def do_compute(self):
        # get value for self._next_html
        pass

    def set_prompt(self, prompt):
        self._prompt = prompt

    def set_next_level_url(self, url):
        self._next_level_url = url


