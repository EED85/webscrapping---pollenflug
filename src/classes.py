import requests
import glob
import bs4
import os
import pandas as pd
import datetime


class DonnerwetterPollenflugScrapper(object):
    def __init__(self, url_root, liste_plz, location_html):
        self.url_root = url_root
        self.liste_plz = liste_plz
        self.location_html = location_html
        self._execution_time = None

    def download_html(self):
        self._execution_time = datetime.datetime.now()
        for plz in self.liste_plz:
            url = self.url_root + plz
            r = requests.get(url)
            c = r.content
            # soup = bs4.BeautifulSoup(c,"html.parser")
            html = self.location_html + os.path.sep+plz+'.html'
            with open(html, 'w', encoding="utf-8") as f:
                f.write(str(c))

    def extract_pollination(self):
        html_files = glob.glob(self.location_html + os.path.sep + "*.html")
        for url in html_files:
            soup = bs4.BeautifulSoup(open(url), "html.parser")
            tr = soup.find("tr", {"bgcolor": "#FFFBD6"})
            table = tr.find_parent()
            all_tr = table.find_all("tr")
            csv = os.path.basename(url).replace("html", "csv")
            df = pd.DataFrame()
            i = -1
            d = dict()
            for tr in all_tr:
                i += 1
                d_tmp = dict()
                all_td = tr.find_all("td")
                if all_td[1].text:
                    d_tmp["plant"] = all_td[1].text
                    d_tmp["staerke_txt"] = all_td[2].find("img")["alt"]
                    verlauf_href = all_td[3].find("a")["href"]
                    if verlauf_href.find("Staerke") == -1:
                        d_tmp["staerke_num"] = 0
                    else:
                        d_tmp["staerke_num"] = int(all_td[3].find("a")["href"][all_td[3].find("a")["href"].find("Staerke=")+8:])
                    d[i] = d_tmp
            df = pd.DataFrame(d).transpose()
            df["execution_time"] = self._execution_time
            df.index.name = "index"
            csv_full_path = self.location_html + os.path.sep + csv
            if os.path.isfile(csv_full_path):
                df_csv = pd.read_csv(csv_full_path)
                df_csv = df_csv.set_index('index')
                df = df.append(df_csv)
                df.index.name = "index"
            df.to_csv(csv_full_path)
