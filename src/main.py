# Init
import pkg_resources
import os
import git
import json
from utils.classes import DonnerwetterPollenflugScrapper as Scrapper
repo_path = os.getcwd()
repo = git.Repo(repo_path)
os.chdir(os.path.join(repo_path, 'src'))
places = os.path.join("utils", "places.json")
with open(places, "r", encoding="utf-8") as read_file:
    d_places = json.load(read_file)
l_plz = list(d_places.values())

url_root = "https://www.donnerwetter.de/region/ortrubrik.mv?Rubrik=%2Fpollenflug%2Fregion.hts&search="

scrapper = Scrapper(url_root=url_root,
                    liste_plz=l_plz,
                    location_html=os.getcwd() + os.path.sep + "data",
                    )
scrapper.download_html()
scrapper.extract_pollination()


# commit and push csv to github
add_path = os.path.join(repo_path, 'src', 'data', '*.csv')
repo.index.add(add_path)
repo.index.commit("#15 adding csv")
repo.remotes.origin.push()

[print(d.project_name + "==" + d.version) for d in pkg_resources.working_set]
