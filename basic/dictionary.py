#3.dictionary
a = {"a":1,"b":2}
print(a)
print(type(a))
b = {"class":"sce","block":"srix"}
print(b["class"])
#get method
print(a.get("class"))
#updation
b["class"] = "it"
print(b)
#2nd method of updation
b.update({"block":"8th block"})
print(b)
#pop operation
b.pop("class")
print(b)
#pop item
b.update({"sec":"7201"})
print(b)
b.popitem()
#clear
print(b)
b.clear()
print(b)
#applying membership operator
print("block"in b)
print("cse"in b)
#these below gives the output in a tuple format
d={"class":"cse","block":"srix"}
print(d.keys())#(['class', 'block'])
print(d.values())#(['cse','srix'])
print(d.items())#([('class','cse'),('block','srix')])
#dictionary looping
# #looping through values
for i in d.values():
    print(i)
#looping through keys
for i in d.keys():
    print(i)
#looping for items
for i,j in d.items():
    print(i,j)
    
d={
    "123":{"name":"a","age":20,"branch":"cse"},
    "124":{"name":"b","age":21,"branch":"ece"},
    "125":{"name":"c","age":19,"branch":"mech"},
    "126":{"name":"d","age":24,"branch":"cse"}
}