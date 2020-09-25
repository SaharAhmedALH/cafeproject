import os 

x = 3
print(x)

y=5
print(y)


#Dictionary
myDic={ "name":"Sahar","age":29,
"skills":["reading","songing","playing"],"eduction":"master"}
print(myDic.keys())
print(myDic.values())
print(myDic["name"])
print(myDic["skills"])
print("#"*40)
print("#"*40)
#Two deminational Dictionary
languges= {
    "one":{
        "name":"HTML",
        "progress":"80%"}, 
    "Two":{
        "name":"css",
        "progress":"90%"},
     "Three":{
        "name":"js",
        "progress":"90%" }}
print(languges)
print(languges["one"])
print(languges["one"]["name"])
print("#"*40)
print("#"*40)
#Dictionary Length
print(len(languges))
print(len(languges["one"]))
print("#"*40)
print("#"*40)
#Dictionary from varibles 
first={"name":"Sahar",
       "Age":"29"}
second={"name":"Rema",
       "Age":"30"}
third={"name":"Sja",
       "Age":"28"}
allnames={"one":first,
    "two":second,
    "three":third }
print(allnames)
print("#"*40)
print("#"*40)
#Dictionary Methods
member={"name":"Arjoan"}
print(member)
print(member.clear())
print("*"*40)
user={"name":"Rena"}
print(user)
b=user.copy()
print(b)
print("*"*40)
user.update({"age":"30"})
print(user)
print("*"*40)
print("#"*40)
print("#"*40)
