file=open("default of credit card clients.csv", "r")
out=open("dataset.csv", "w")

firstline=file.readline()
args=firstline.strip().split(";")
string=""
for i in range(0, 6):
    string+=args[i]+";"
for i in range(12, 24):
    string+=args[i]+";"
string+=args[24]
out.write(string+"\n")

for line in file:
    args=line.strip().split(";")
    #args will contain 25 elements
    insert=True;
    for i in range(0, 25):
        if i in range(12, 24) and int(args[i])==0:
            insert=False;

    if (insert):
        string=""
        for i in range(0, 6):
            string+=args[i]+";"
        for i in range(12, 24):
            string+=args[i]+";"
        string+=args[24]
        out.write(string+"\n")

file.close()
out.close()
