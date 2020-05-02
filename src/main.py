# Init
import os
import git
from classes import DonnerwetterPollenflugScrapper as Scrapper
repo_path = os.getcwd()
repo = git.Repo(repo_path)
os.chdir(os.path.join(repo_path, 'src'))
l_plz = ["51427", "Welling"]


url_root = "https://www.donnerwetter.de/region/ortrubrik.mv?Rubrik=%2Fpollenflug%2Fregion.hts&search="

scrapper = Scrapper(url_root=url_root, liste_plz=l_plz, location_html=os.getcwd() + os.path.sep + "data")
scrapper.download_html()
scrapper.extract_pollination()


# commit and push csv to github
add_path = os.path.join(repo_path, 'src', 'data', '*.csv')
repo.index.add(add_path)
repo.index.commit("adding csv")
repo.remotes.origin.push()
