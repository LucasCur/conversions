import json, re
arr = json.load(open("conv.data","r"))
def gettype(x,ac):
  x = (re.sub("([0-9.+])([A-Za-z+])","\\1|\\2",x)).split("|")
  y = x[0]
  z = x[1]
  if z != "cm":
    for iter in range(0,len(arr)):
      if z == arr[iter][1]:
        y = float(y) * float(arr[iter][0])
  for iter in range(0,len(arr)):
    if z != arr[iter][1]:
      a = round(float(y) / float(arr[iter][0]),ac)
      if len(str(str(a).split(".")[1])) < ac:
        a = str(a) + (ac-len(str(str(a).split(".")[1])))*"0"
      print(str(x[0] + x[1]),"=",str(a)+str(arr[iter][1]))
gettype(input("Input: "),int(input("Accuracy (dp): ")))
