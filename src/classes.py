import requests
import glob
import bs4
import os
import pandas as pd


class DonnerwetterPollenflugScrapper(object):
    def __init__(self, url_root, liste_plz, location_html):
        self.url_root = url_root
        self.liste_plz = liste_plz
        self.location_html = location_html

    def download_html(self):

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
            # <tr bgcolor="#FFFBD6" valign="middle" align="left">
            # <td><img src="//static.donnerwetter.de/images/pollgb.gif" align="middle" width="30" height="30" data-pagespeed-url-hash="3210090727" onload="pagespeed.CriticalImages.checkImageForCriticality(this);"></td>
            # <td><font size="3"><b><font size="2">Erle</font></b></font></td>
            # <td><img src="//static.donnerwetter.de/images/poll0.gif" width="90" height="30" alt="keine" data-pagespeed-url-hash="3218762444" onload="pagespeed.CriticalImages.checkImageForCriticality(this);"> </td>
            # <td><font size="1">Verlauf<br>
            # <a href="/pollenflug/region.hts?lid=DE14331&amp;Ort=BERGISCH GLADBACH&amp;PTag=LF&amp;Allergen=1">Langfrist</a></font>
            # </td>
            # </tr>
            tr = soup.find("tr", {"bgcolor": "#FFFBD6"})
            table = tr.find_parent()
            all_tr = table.find_all("tr")
            csv = os.path.basename(url).replace("html", "csv")
            df = pd.DataFrame()
            i = -1
            d = dict()
            for tr in all_tr:
                i+=1
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
            df.to_csv(self.location_html + os.path.sep + csv)