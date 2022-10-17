from urllib.parse import urlencode, unquote
from urllib.parse import urlunparse

import requests
from requests.cookies import RequestsCookieJar


class HeliosGit:

    def __init__(self):
        self.cookies = RequestsCookieJar()
        self.cookies.set("lang", "lang")
        self.cookies.set("hy_data_2020_id", "18339f5d0343e-075464d74af03f-1a525635-3686400-18339f5d035155")
        self.cookies.set("hy_data_2020_js_sdk", "%7B%22distinct_id%22%3A%2218339f5d0343e-075464d74af03f-1a525635-3686400-18339f5d0351556%22%2C%22site_id%22%3A357%2C%22user_company%22%3A266%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218339f5d0343e-075464d74af03f-1a525635-3686400-18339f5d0351556%22%7D")
        self.cookies.set("Hm_lvt_343b9b8fc424627f20938ba2a6d10b47", "Hm_lvt_343b9b8fc424627f20938ba2a6d10b47")
        self.cookies.set("Qs_lvt_337518", "1660876247%2C1662743027%2C1663124754%2C1665546985%2C1665645018")
        self.cookies.set("Qs_pv_337518", "2362588262057168000%2C3127977143522190000%2C338456138017873860%2C1394974043157306600%2C3274612798727682600")
        self.cookies.set("helios_git_lucky", "03e636fb2557330a")
        self.cookies.set("_csrf", "CFYLvv64iMx9nD2iP_n2Lk9kNlU6MTY2NTk4OTU2NjI3NTMzOTk3MA%3D%3D")
        self.cookies.set("redirect_to", "%252F")



    def response_text(self, method, url, **kwargs):
        """请求函数"""
        response = requests.request(method, url, cookies=self.cookies, **kwargs)  # 发送请求带入cookies
        result = response.text
        self.cookies.update(response.cookies)  # 更新cookies
        return result

    def cookires(self):
        return self.cookies


if __name__ == '__main__':
    git = HeliosGit()
    login_url = "https://code.huilianyi.com/user/login" + urlencode({"_csrf": "spzech8jcVLTarWDez2sUp1YOTA6MTY2NTk4ODEzMjA5NzM0NDMzOA==", "user_name": "qingyu.meng@huilianyi.com", "password": "Qingyu981117", "remember": "on"})
    git.response_text("POST", login_url)

    code_huilianyi = "https://code.huilianyi.com"
    print(git.response_text("GET", code_huilianyi))

    print(git.cookies)

    print(unquote(git.cookies.get("_csrf")))
    merge_url = "https://code.huilianyi.com/yali.liu/scavenger/compare/master...yali.liu:dev" + urlencode({"_csrf": unquote(git.cookies.get("_csrf")), "title": "66666"})
    print(git.response_text("POST", merge_url))