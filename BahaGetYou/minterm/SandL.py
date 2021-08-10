def Load(local):
    with open("./" + local + ".txt", mode="w", encoding="utf-8") as temp:
        temp.write("廢文捕捉對象:"+local+"\n")
    with open("./DataBase/"+local+".txt",mode="r",encoding="utf-8") as file:
        data=file.read()
        return data
def Save(local,data):
    with open("./DataBase/"+local+".txt", mode = "w", encoding="utf-8") as file:
        file.write(data)
        return 1
def SLtest(local,data):
    #useless
    Save(local,data)
    print(Load(local))
    return 1
def Output(project,file,con):
    with open("./"+str(project)+".txt", mode="a", encoding="utf-8") as data:
        if con==0:
            data.write(file)
        else:
            data.write(str(con)+". "+file+"\n")
    return 1