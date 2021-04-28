import json
a=input("Enter the name of the team : ")
myjsonFile=open('IntelegenciaData.json',)
obj = json.load(myjsonFile)
list=obj['teamDetails']  
for i in obj["teamDetails"]:
    if(i['teamName']==a):
        print(i)

    
