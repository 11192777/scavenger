import argparse
import os
import re
from urllib.parse import unquote

import requests
from lxml import etree
from requests.cookies import RequestsCookieJar


class HeliosGit:

    def __init__(self, path=None, project_name=None, branch_name=None, user_name=None, remote_name=None, remote_branch_name=None, title=None):
        self.cookies = RequestsCookieJar()
        self.info = {}
        self.path = "huilianyi"
        self.push_info()
        self.title = title
        self.titleFormat = title and [title] or []
        if project_name is not None:
            self.info["project_name"] = project_name
        if branch_name is not None:
            self.info["branch_name"] = branch_name
        if user_name is not None:
            self.info["user_name"] = user_name
        if remote_name is not None:
            self.info["remote_name"] = remote_name
        if remote_branch_name is not None:
            self.info["remote_branch_name"] = remote_branch_name
        if path is not None:
            self.path = path
        if title is not None:
            self.title = title

    def access(self):
        url = "https://code.huilianyi.com/user/login"
        response = requests.get(url=url)
        self.cookies.update(response.cookies)

    def login(self):
        url = "https://code.huilianyi.com/user/login"
        response = requests.post(url=url, data={"user_name": "qingyu.meng@huilianyi.com", "password": "Qingyu981117"},
                                 cookies=self.cookies, headers={"Content-Type": "application/x-www-form-urlencoded"})
        self.cookies.update(response.cookies)
        url = "https://code.huilianyi.com/"
        response = requests.get(url=url, cookies=self.cookies)
        self.cookies.update(response.cookies)

    def compare(self):
        url = "https://code.huilianyi.com/{}/{}/compare/{}...{}:{}".format(self.path, self.info["project_name"], self.info["branch_name"], self.info["user_name"], self.info["remote_branch_name"])
        print("===> Compare url is:\n{}".format(url))
        response = requests.get(url=url, cookies=self.cookies)
        html = etree.HTML(response.text)
        commits = html.xpath("/html/body/div[@class='full height']/div[@class='repository compare pull diff']/div[@class='ui container']/div[@class='sixteen wide column page grid']/div[@class='ui unstackable attached table segment']/table[@id='commits-table']/tbody/tr")
        commit_content = []
        for commit in commits:
            user = commit.xpath("./td[@class='author']/text()")
            comment = commit.xpath("./td[@class='message collapsing']/span/text()")
            if str.strip(user[1]) == self.info["commit_username"]:
                commit_content.append(str.strip(comment[0]))
        return commit_content

    def merge(self, title):
        url = "https://code.huilianyi.com/{}/{}/compare/{}...{}:{}".format(self.path, self.info["project_name"], self.info["branch_name"], self.info["user_name"], self.info["remote_branch_name"])
        print("===> Merge url is:\n{} \nTitle is:{}".format(url, title))
        title = len(title) < 240 and title or (title[:240] + " ...")
        response = requests.post(url=url, data={"title": title, "_csrf": unquote(self.cookies.get("_csrf"))}, cookies=self.cookies, headers={"Content-Type": "application/x-www-form-urlencoded"}, allow_redirects=False)
        print("===> Pull address url is: \nhttps://code.huilianyi.com{}".format(response.headers["location"]))

    def run(self):
        self.access()
        self.login()
        commits = self.compare()
        if len(commits) == 0:
            print("Already synced. The operation has been canceled.")
            return
        if self.title is None:
            merge_info = ""
            for i in range(len(commits)):
                info = commits[i][:5] == "Merge" and "Merge remote-tracking." or commits[i]
                merge_info = merge_info + "{}.{}  ".format(str(i + 1), info)
                self.titleFormat.append(merge_info)
            merge_info = "[{}] {}".format(self.info["branch_name"], merge_info)
            self.merge(merge_info)
        else:
            self.merge(self.title)

    def push_info(self):
        branch_vv = ""
        for line in os.popen("git branch -vv").read().split("\n"):
            if line.startswith("*"):
                branch_vv = line.split()[3]
        remote_name = branch_vv[branch_vv.index("[") + 1:branch_vv.index("/")]
        self.info["remote_name"] = remote_name
        branch_name = ""
        for line in os.popen("git branch").read().split("\n"):
            if line.startswith("*"):
                branch_name = line.split()[1]
        self.info["branch_name"] = branch_name
        remove_v = os.popen("git remote -v")
        line = remove_v.readline()
        while line != "":
            items = line.split()
            if items[0] == remote_name:
                remote_url = items[1]
                target = remote_url.startswith("http") and re.findall(r'https:\/\/code.huilianyi.com\/(.+?)\.git', items[1])[0] or re.findall(r'gogsio@code.huilianyi.com:(.+?)\.git', items[1])[0]
                self.info["user_name"] = target.split("/")[0]
                self.info["project_name"] = target.split("/")[1]
                break
            line = remove_v.readline()
        self.info["commit_username"] = os.popen("git config user.name").read().split()[0]
        self.info["remote_branch_name"] = self.info["branch_name"]


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', type=str, default=None, help="指定域名")
        parser.add_argument('--branch', type=str, default=None, help="指定远程分支")
        parser.add_argument('--project', type=str, default=None, help="指定项目名称")
        parser.add_argument('--username', type=str, default=None, help="指定提交人名称")
        parser.add_argument('--cbranch', type=str, default=None, help="指定本地分支")
        parser.add_argument('--title', type=str, default=None, help="自定义标题")
        args = parser.parse_args()
        git = HeliosGit(path=args.path, project_name=args.project, branch_name=args.cbranch, user_name=args.username, remote_branch_name=args.branch, title=args.title)
        git.run()
    except Exception as e:
        print(repr(e))
