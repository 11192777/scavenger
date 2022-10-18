from urllib.parse import urlencode, unquote
from urllib.parse import urlunparse

import requests
from requests.cookies import RequestsCookieJar


if __name__ == '__main__':
    csrf = "6K3CaQO5936TJgXTipfy36khn106MTY2NTk5NDg0NDAwMDc5MDI0Mg=="
    cookies = RequestsCookieJar()
    cookies.set("lang", "zh-CN")
    cookies.set("Hm_lvt_3c193caea742eb1d364949dfa96cea20", "1661486186,1661525852,1661737666,1663341034")
    cookies.set("Hm_lvt_343b9b8fc424627f20938ba2a6d10b47", "1661486186,1661525852,1661737666,1663341035")
    cookies.set("Qs_lvt_337518", "1661418127%2C1661477446%2C1661525853%2C1661737666%2C166334103")
    cookies.set("Qs_pv_337518", "2299340530736051200%2C865690689348363800%2C442714974431105600%2C978892390697045200%2C169423104547499300")
    cookies.set("helios_git_lucky", "3c9a8d466d502197")
    cookies.set("_csrf", "6K3CaQO5936TJgXTipfy36khn106MTY2NTk5NDg0NDAwMDc5MDI0Mg%3D%3D")
    cookies.set("redirect_to", "%252F")

    data = {
        "_csrf": csrf,
        "user_name": "qingyu.meng@huilianyi.com",
        "password": "Qingyu981117",
        "remember": "on"
    }
    response1 = requests.get("https://code.huilianyi.com/user/login", data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
    cookies.update(response1.cookies)

    response2 = requests.get("https://code.huilianyi.com")
    cookies.update(response2.cookies)

    csrf = "QZQw5K_vNhGyo38USdlR0SB38r06MTY2NjAwMDMxNTgzNjIzMTgzOQ=="

    data = {
        "_csrf": csrf,
        "title": "66666"
    }
    print(cookies)
    response3 = requests.post("https://code.huilianyi.com/yali.liu/scavenger/compare/master...yali.liu:dev", data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
    print(response3.text)
