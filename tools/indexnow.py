#!/usr/bin/env python3
"""Submit all URLs from docs/sitemap.xml to IndexNow. Usage: python3 tools/indexnow.py"""
import json,os,re,urllib.request
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
F=json.load(open(f'{R}/facts.json'));K=F['indexnow_key']
urls=re.findall(r'<loc>([^<]+)</loc>',open(f'{R}/docs/sitemap.xml').read())
host=urls[0].split('/')[2]
body=json.dumps({"host":host,"key":K,"keyLocation":f"https://{host}/{K}.txt","urlList":urls}).encode()
req=urllib.request.Request('https://api.indexnow.org/indexnow',body,{'Content-Type':'application/json; charset=utf-8'})
try: r=urllib.request.urlopen(req,timeout=30); print(r.status,len(urls),'urls')
except urllib.error.HTTPError as e: print(e.code,e.read()[:300])
