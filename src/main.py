# Init
import os
import git
import json
from classes import DonnerwetterPollenflugScrapper as Scrapper
repo_path = os.getcwd()
repo = git.Repo(repo_path)
os.chdir(os.path.join(repo_path, 'src'))

with open("places.json", "r") as read_file:
    d_places = json.load(read_file)
l_plz = list(d_places.values())

url_root = "https://www.donnerwetter.de/region/ortrubrik.mv?Rubrik=%2Fpollenflug%2Fregion.hts&search="

scrapper = Scrapper(url_root=url_root, liste_plz=l_plz, location_html=os.getcwd() + os.path.sep + "data")
scrapper.download_html()
scrapper.extract_pollination()


# commit and push csv to github
add_path = os.path.join(repo_path, 'src', 'data', '*.csv')
repo.index.add(add_path)
repo.index.commit("#15 adding csv")
repo.remotes.origin.push()

import pkg_resources
[print(d.project_name + "==" + d.version) for d in pkg_resources.working_set]