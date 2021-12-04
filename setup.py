import sys

import requests


def main(day):
    with open("session_cookie.txt", 'r') as f:
        cookie = f.readline()

    headers = {'session': cookie}
    url = "https://adventofcode.com/2021/day/" + day + "/input"

    session = requests.Session()
    resp = session.get(url, cookies=headers)

    in_file = open("day" + day + "/input.txt", 'w')
    in_file.write(resp.text)
    in_file.close()


if __name__ == "__main__":
    main(sys.argv[1])