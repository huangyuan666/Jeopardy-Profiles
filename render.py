#!/usr/bin/env python
# -*- coding: utf-8 -*-

from challenges import challenges


def get_challenge_by_name(challenge_name):
    for i in challenges:
        if i[1] == challenge_name:
            return i

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
            challenge = get_challenge_by_name(i.encode("utf-8"))
            challenge_type = challenge[5].upper()
            template += "  * [[%s] %s](https://github.com/SniperOJ/Challenges/blob/master/web/%s.json)  \n" % (
                challenge_type,
                i.encode("utf-8"),
                i.encode("utf-8"),
            )
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
