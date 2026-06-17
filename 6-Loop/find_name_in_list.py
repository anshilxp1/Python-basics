name_list = ["ram","anshil", "harsh","ansh", "ram"]
name = input("enter the name : ")
for ch in name_list :
    if name in name_list :
     print("name exist")
     break
else:
    print("name not exist")