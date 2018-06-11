#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import glob
import time


def render():
    users = glob.glob("data/*.json")

    for user in users:
        email = user.split("/")[1].replace(".json","")
        data = json.loads(open(user).read())
        template = "#### %s  \n\n" % (data['username'].encode("utf-8"))
        template += "* Email: %s  \n" % (email)    
        template += "* University: %s  \n" % (data['university'].encode("utf-8"))    
        template += "* Register Time: %s  \n" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['register_time'])))    
        template += "* Register IP: %s  \n" % (data['register_ip'].encode("utf-8"))    
        template += "* Score: %s  \n" % (data['score'])    
        template += "* Solved challenges: \n"
        for i in data['solved_challenges']:
            template += "  * %s  \n" % (i.encode("utf-8"))
        # print template
        with open("data/%s.md" % (email), "w") as f:
            f.write(template)


'''
| Nickname | University | Score |
| -------- | ---------- | ----- |
'''

def get_score(element):
    return element['score']

def render_root():
    users = glob.glob("data/*.json")
    template = ""
    headers = [
        'Nickname',
        'University',
        'Score',
    ]
    template += '| %s |  \n' % (" | ".join(headers))
    template += '| %s  \n' % (":-: |" * len(headers))
    sorted_users = []

    for user in users:
        data = json.loads(open(user).read())
        sorted_users.append(data)

    sorted_users.sort(key=get_score, reverse=True)

    for data in sorted_users:
        template += '|%s|%s|%s|  \n' % (
            data['username'].encode("utf-8"),
            data['university'].encode("utf-8"),
            data['score'],
        )
    print template
    with open("README.md", "w") as f:
        f.write(template)


def main():
    render_root()
    render()

if __name__ == '__main__':
    main()