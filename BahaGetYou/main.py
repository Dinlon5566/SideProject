#make by dinlon-OwO
import minterm.SandL as SL
import bs4
import urllib.request

#這個def原本放minterm裡面，不過感覺有點多餘就單獨出來
def GetWeb(urls,head):
    request = urllib.request.Request(urls, headers={"User-Agent":head})
    with urllib.request.urlopen(request) as data:
        file = data.read().decode("utf-8")
    return file

project=input("你想查誰的廢文?\n")
urls = "https://home.gamer.com.tw/creation.php?v=1&owner="+project+"&t=0"
heads= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45"
print("廢文捕捉對象:"+project)
SL.Save(project,GetWeb(urls,heads))
#SL.SLtest(project,"Project name:")
data=bs4.BeautifulSoup(SL.Load(project),"html.parser")
maindata=data.find_all("td",align="left")
con=1
#逃避考試是不是可以激發人類淺力阿
for line in maindata:
    SL.Output(project,line.a.string,con)
    print(str(con)+". "+line.a.string)
    con+=1
SL.Output(project,"---End---\n"+whatever,0)
print("---End---\n"+whatever)