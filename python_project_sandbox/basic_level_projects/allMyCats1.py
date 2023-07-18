catNames = []
while True:
    print("Enter cat number " +str(len(catNames) +1) + "or 4 to stop.")
    catName = input()
    if catName == "4":
        break
    else:
        catNames = catNames + [catName]

print("Here are all the cats:")
for name in catNames:
    print(name)

