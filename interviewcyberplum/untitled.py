f=open("uszips.csv","r")
# 1
cvd={}
for data in f:
    zipcode=data[0]
    cvd[zipcode]={}
    cvd[zipcode]["name"]=zipcode
