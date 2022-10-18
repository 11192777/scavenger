import os
import re
from urllib.parse import urlencode, unquote
from urllib.parse import urlunparse

import requests
from lxml import etree
from requests.cookies import RequestsCookieJar


class HeliosGit:

    def __init__(self, path="huilianyi"):
        self.cookies = RequestsCookieJar()
        self.info = {}
        self.path = path

    def access(self):
        url = "https://code.huilianyi.com/user/login"
        response = requests.get(url=url)
        self.cookies.update(response.cookies)

    def login(self):
        url = "https://code.huilianyi.com/user/login"
        response = requests.post(url=url, data={"user_name": "qingyu.meng@huilianyi.com", "password": "Qingyu981117"}, cookies=self.cookies, headers={"Content-Type": "application/x-www-form-urlencoded"})
        self.cookies.update(response.cookies)
        url = "https://code.huilianyi.com/"
        response = requests.get(url=url, cookies=self.cookies)
        self.cookies.update(response.cookies)

    def compare(self):
        url = "https://code.huilianyi.com/{}/{}/compare/{}...{}:{}".format(self.path, self.info["project_name"], self.info["branch_name"], self.info["user_name"], self.info["branch_name"])
        print(url)
        response = requests.get(url=url, cookies=self.cookies)
        html = etree.HTML(response.text)
        commits = html.xpath("/html/body/div[@class='full height']/div[@class='repository compare pull diff']/div[@class='ui container']/div[@class='sixteen wide column page grid']/div[@class='ui unstackable attached table segment']/table[@id='commits-table']/tbody/tr")
        print(commits)
        for commit in commits:
            user = commit.xpath("./tr/td[@class='author']")
            comment = commit.xpath("./tr/td[@class='message collapsing']/span")
            print("user:{} comment:{}".format(user, comment))
        return "None"

    def merge(self, title):
        url = "https://code.huilianyi.com/{}/{}/compare/{}...{}:{}".format(self.path, self.info["project_name"], self.info["branch_name"], self.info["user_name"], self.info["branch_name"])
        response = requests.post(url=url, data={"title": title, "_csrf": unquote(self.cookies.get("_csrf"))}, cookies=self.cookies, headers={"Content-Type": "application/x-www-form-urlencoded"})

    def run(self):
        self.access()
        self.login()
        self.push_info()
        self.compare()
        # self.merge()

    def push_info(self):
        branch_vv = os.popen("git branch -vv").read().split()[3]
        remote_name = branch_vv[branch_vv.index("[") + 1:branch_vv.index("/")]
        self.info["remote_name"] = remote_name
        branch_name = branch_vv[branch_vv.index("/") + 1:branch_vv.index("]")]
        self.info["branch_name"] = branch_name
        remove_v = os.popen("git remote -v")
        line = remove_v.readline()
        while line != "":
            items = line.split()
            if items[0] == remote_name:
                target = items[1]
                project_name = target[target.index("/") + 1:target.rindex(".")]
                self.info["project_name"] = project_name
                user_name = target[target.index(":") + 1:target.index("/")]
                self.info["user_name"] = user_name

                break
            line = remove_v.readline()


if __name__ == '__main__':
    git = HeliosGit("yali.liu")
    git.run()
