name = "Name"
print(name.upper())
print(name.lower())
print(name.strip())
kt = "123123pl"
print(kt.startswith("4"))
print(kt.endswith("s"))
print(kt.count("a"))
print(kt.find("s"))
print("Ten toi la {} va toi {} tuoi.".format("Name, 17"))
print(len(name))
print(kt[4:])
print(kt[:-5])
name2 = "name,title,age"
print(name2.split(","))
for i in name2.split(","):
    print(i)
print("-".join(name2.split(",")))