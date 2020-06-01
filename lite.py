puid=''#填puid
token=''#填token
from cmd2 import Cmd
class cx(Cmd):
  data=[]
  def __init__(self):
    Cmd.__init__(self)
    self.do_cd()
  def getdata(self,puid,token,fldid=''):
    from requests import get
    from json import loads
    data,pagedata,page=[],[],0
    while pagedata!=[] or page==0:
      page=page+1
      pagedata=loads(get('https://pan-yz.chaoxing.com/api/getDirAndFiles?puid=%s&_token=%s&fldid=%s&page=%s'%(puid,token,fldid,page)).text)['data']
      for dict in pagedata:
        data.append(dict)
    return data
  def do_cd(self,args=''):
    fldid='' if args=='' else self.data[int(args)]['resid']
    self.data=self.getdata(puid,token,fldid)
    for i in range(len(self.data)):
      print([i],self.data[i]['name'])
      print('\033[1;34mhttps://pan-yz.chaoxing.com/external/m/file/%s\033[0m'%self.data[i]['resid'])
if __name__=='__main__':
  cx().cmdloop()