
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import json
import os
wd = os.getcwd()
json_path = os.path.join(wd, "src", "authentification", "sharepoint_authentification.json")


with open(json_path, "r") as read_file:
    sp_auth = json.load(read_file)


authcookie = Office365(sp_auth["url"]
    , username=sp_auth["username"]
    , password=sp_auth['password']).GetCookies()
site = Site(sp_auth["url_site"], version=Version.v2016, authcookie=authcookie)
folder = site.Folder('Github_upload')


csv_path = os.path.join(wd, "src", "data", "51427.csv")
with open(csv_path, 'r', encoding="Latin-1") as file:
    data = file.read()

folder.upload_file(data, "51427.csv")
