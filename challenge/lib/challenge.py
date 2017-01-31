from web_helper import WebHelper


class Result(object):
    def __init__(self):
        self.file = None
        self.url = None
        self.user = None
        self.password = None

    def set_url(self, url):
        self.url = url

    def set_file(self, file_name):
        self.file = file_name

    def set_user_password(self, user, password):
        self.user = user
        self.password = password


class Challenge(object):
    user = ''
    password = ''

    def __init__(self, url_or_result, need_authentication=False, user_name='huge', pass_word='file'):
        if type(url_or_result) is Result:
            self.url = url_or_result.url
            self.user = url_or_result.user
            self.password = url_or_result.password
            self.file_name = url_or_result.file
            if self.user is not None and self.password is not None:
                need_authentication = True
            self.result = url_or_result
        else:
            self.url = url_or_result
            self.user = user_name
            self.password = pass_word
            self.result = Result()

        if need_authentication:
            self.url, self.web_source = WebHelper.get_auth_url_content(self.url, self.user, self.password)
        else:
            self.url, self.web_source = WebHelper.get_final_url_content(self.url)
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
            return self.url

    def set_user_password(self, user, password):
        self.result.user = user
        self.result.password = password

    def get_result(self):
        self.result.url = self.get_next_level_url()
        return self.result

    def do_compute(self):
        # get value for self._next_html
        pass

    def set_prompt(self, prompt):
        self._prompt = prompt

    def set_next_level_url(self, url):
        self._next_level_url = url