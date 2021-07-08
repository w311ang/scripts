import requests
from bs4 import BeautifulSoup

site_url='https://www.hkisl.net/'
tolerance=30

s=requests.Session()
ua='Mozilla/5.0 (Linux; Android 9; ONEPLUS A3010 Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36'
s.headers.update({'user-agent':ua})
s.get(site_url,params={'language':'chinese_cn'})
exists=[]
invalid=0
count=0
for i in range(1,1000):
  if invalid>tolerance:
    break
  order_url=site_url+'cart.php?a=add&pid=%s'%i
  with s.get(order_url) as resp:
    history=resp.history
    try:
      code=history[0].status_code
    #溢出是因为history不会记录最终code
    except IndexError:
      code=resp.status_code
    text=resp.text
    url=resp.url
    if code==302:
      try:
        loc=history[0].headers['location']
      #溢出是因为history不会记录最终url
      except IndexError:
        loc=url
      #print(loc)
      #判断是有效
      if '/cart.php?a=confproduct' in loc:
        invalid=0
        #判断是需配置商品
        if '/cart.php?a=confproduct' in url:
          soup = BeautifulSoup(text,'lxml')
          title = soup.find('p', attrs={'class' : 'product-title'}).string
        #判断是无需配置商品
        elif '/cart.php' in url:
          with s.get(site_url+'/cart.php?a=confproduct&i=%s'%count) as resp:
            text=resp.text
            soup = BeautifulSoup(text,'lxml')
            title = soup.find('p', attrs={'class' : 'product-title'}).string
            count+=1
        print('%s - %s'%(title,order_url))
      #判断是无效
      elif loc=='/cart.php':
        invalid+=1
    #判断是缺货
    elif code==200:
      invalid=0
