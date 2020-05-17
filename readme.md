# Webscrapping

## Used Techniques

### Preliminary remarks

package Beuatifulsoup is used to scrape particular web pages

### requirements.txt

``` conda prompt
pip freeze > requirements.txt
```

### Running Python Scripts with Github

Introduction:
<https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions>

<https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow#filtering-for-specific-branches-tags-and-paths>

### upload to Github Repository

#### Authentification

Authentification via Github Secrets. Password is passed as parameter to an py script started with the shell

not tested yet

### Upload to sharepoint

#### Authentification SP

see above

#### Implementation

not testet yet

<https://pypi.org/project/SharePlum/>

```python
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

authcookie = Office365('https://abc.sharepoint.com', username='username@abc.com', password='password').GetCookies()
site = Site('https://abc.sharepoint.com/sites/MySharePointSite/', version=Version.v2016, authcookie=authcookie)
folder = site.Folder('Shared Documents/This Folder')
folder.upload_file('Hello', 'new.txt')
folder.read_txt_file('new.txt')
folder.check_out('new.txt')
folder.check_in('new.txt', "My check-in comment")
folder.delete_file('new.txt')
```

or

<https://www.pythonbite.tech/11-blog/python-advanced/4-uploading-files-to-sharepoint>
