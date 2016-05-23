import re, csv,os, os.path
import glob

#This program will pull all the files from a folder that are .csv and it just sorts them and then adds a session number--CP
CurrDir = os.getcwd()
print "You're in " + CurrDir

print "__________________"
folders = glob.glob('[0-9][0-9][0-9]')

for participant in folders:
    path = CurrDir + "\\" + participant
    os.chdir(path)
    print "Changing to: " + os.getcwd()

    filenames = glob.glob('[0-9][0-9][0-9]---*.csv')
    new = sorted(filenames)#will sort
    i=1
    for f in new:
        print f#for checking purposes, prints file it's processing into terminal
        print i
        reader = csv.reader(open(f, 'rU'))
        name = str(i)+ '_' + f
        writer = csv.writer(open( name ,'wb'))
        for row in reader:
            if len(row)<29:
                writer.writerow([row[0],row[1],row[2],row[3],str(i)])#the last 4 rows, just put them back
            else:
                if row[0]=="Participant ID":
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],
                    row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],
                    row[14],row[15],row[16],row[17],row[18],row[19],row[20],
                    row[21],row[22],row[23],row[24],row[25],row[26], row[27],
                    row[28], "Session"])#header Row
                else:
                    writer.writerow([row[0],row[1], row[2],row[3],row[4],row[5],
                    row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],
                    row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],
                    row[22],row[23],row[24],row[25],row[26],row[27],row[28],str(i)])#add session number
        i += 1 #next session
