import os
import git
from classes import DonnerwetterPollenflugScrapper as Scrapper

repo = git.Repo(os.getcwd()) 

os.chdir(os.getcwd()+os.path.sep + 'src')
l_plz = ["51427"]

url_root = "https://www.donnerwetter.de/region/ortrubrik.mv?Rubrik=%2Fpollenflug%2Fregion.hts&search="

scrapper = Scrapper(url_root=url_root, liste_plz=l_plz, location_html=os.getcwd() + os.path.sep + "data")
scrapper.download_html()
scrapper.extract_pollination()
repo_dir = os.path.join(rw_dir, 'my-new-repo')
file_name = os.path.join(repo_dir, 'new-file')


repo.index.add(r"C:\DEV\git\scrapping-pollination\src\data\51427.csv")
repo.index.commit("adding csv")
repo.remotes.origin.push()