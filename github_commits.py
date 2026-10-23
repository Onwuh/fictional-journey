from main import count_by
import requests


if __name__ == "__main__":


    r = requests.get("https://api.github.com/repos/odoo/odoo/commits")
    r.raise_for_status()
    committer_list = []
    for entrie in r.json():
        committer_list.append(entrie["committer"])
    print(committer_list)
    print(count_by(committer_list,"login"))

