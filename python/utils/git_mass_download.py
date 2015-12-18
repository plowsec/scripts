#!/usr/bin/python

import argparse,sys
import os
import subprocess
import shutil
import requests
import re
import traceback
class Main:

    def __init__(self, username="hackedteam"):

        self.USERNAME = username
        self.CLONE_COMMAND = "git --git-dir=/dev/null clone --depth=1 https://github.com{repo}.git"
        self.CLONE_COMMAND = "git archive --format=tar --remote=https://github.com{repo}.git HEAD | tar xf - "
        self.REPOSITORIES_URL = "https://github.com/{username}?tab=repositories".format(username = self.USERNAME) 
        self.PATTERN = '<h3 class="repo-list-name">.*\n?.*<a href="(.*)">.*\n?.*<\/a>.*\n?.*<\/h3>'
        self.repos = []

    def execute(self):
        """Here, we parse the commandline options and react according to them"""

        self.getRepos()
        for repo in self.repos:
            if repo.split("/")[-1] == "rcs-db":
                continue
            print("[*] Downloading : " + repo)
            #print("Cloning : " + repo)
            #command = self.CLONE_COMMAND.format(username=self.USERNAME, repo=repo)
            #res_process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            #print("".join(map(str, res_process.communicate())))
            self.download_file("https://github.com{repo}/archive/master.zip".format(repo=repo), repo.split("/")[-1] + ".zip")

    def download_file(self, url, filename):
        r = requests.get(url, stream=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: 
                    f.write(chunk)

    def getRepos(self):
        try:
            data = requests.get(self.REPOSITORIES_URL).text
            self.repos = re.findall(self.PATTERN, data)
        except:
            print("Error while fetching repos list")
            traceback.print_exc()
            sys.exit()


if __name__ == "__main__":
    main = Main()
    main.execute()
