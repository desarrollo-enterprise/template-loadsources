import selenium
from setting import setting_web

class WebScrap:
    urls = ''
    credential = ''

    def __init__(self, urls, credential):
        self.urls = urls
        self.credential = credential

    def give_credential(self):
        user = self.credential["user"]
        password = self.credential["password"]

        print(f"""USUARIO:\t\t{user}
CONTRASEÑA:\t\t{password}""")

        # Here you could write the code selenium to enter to the web.


a = WebScrap(setting_web['url'], setting_web['credential'])
a.give_credential()
