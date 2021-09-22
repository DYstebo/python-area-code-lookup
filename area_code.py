import csv

with open('npa_report.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = list(reader)
    aCode = input("Enter an area code to lookup: ")
    for i in range(0,len(mydict)):
        if aCode == mydict[i][0]:
            print("Area code " + aCode + " belongs to " + mydict[i][1] + ", " + mydict[i][2] + ".")
            infile.close()
            exit()
    print("No match for that area code.")
    infile.close()