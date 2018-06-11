#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import glob
import time

data_folder = 'profiles'

def render():
    users = glob.glob("%s/*.json" % (data_folder))

    for user in users:
        email = user.split("/")[1].replace(".json", "")
        data = json.loads(open(user).read())
        template = "#### %s  \n\n" % (data['username'].encode("utf-8"))
        template += "* Email: %s  \n" % (email)
        template += "* University: %s  \n" % (
            data['university'].encode("utf-8"))
        template += "* Register Time: %s  \n" % (time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(data['register_time'])))
        template += "* Register IP: %s  \n" % (
            data['register_ip'].encode("utf-8"))
        template += "* Score: %s  \n" % (data['score'])
        template += "* Solved challenges: \n"
        for i in data['solved_challenges']:
            template += "  * %s  \n" % (i.encode("utf-8"))
        # print template
        with open("%s/%s.md" % (data_folder, email), "w") as f:
            f.write(template)


def get_score(element):
    return element['score']


def render_root():
    users = glob.glob("%s/*.json" % (data_folder))
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
        data['email'] = user.split("/")[1].replace(".json", "")
        sorted_users.append(data)

    sorted_users.sort(key=get_score, reverse=True)

    for data in sorted_users:
        template += '|[%s](%s)|%s|%s|  \n' % (
            data['username'].encode("utf-8"),
            "%s/%s.md" % (data_folder, data['email'].encode("utf-8")),
            data['university'].encode("utf-8"),
            data['score'],
        )
    with open("README.md", "w") as f:
        f.write(template)


def main():
    render_root()
    render()


if __name__ == '__main__':
    main()
