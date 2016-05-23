import re, csv,os, os.path
import glob
import shutil
#this will pull their responses from the files and put them in one place--CP
CurrDir = os.getcwd()
print "You're in " + CurrDir

print "__________________"
folders = glob.glob('[0-9][0-9][0-9]')

for participant in folders:
    path = CurrDir + "\\" + participant
    os.chdir(path)
    print "Changing to: " + os.getcwd()

    filenames = glob.glob('[0-9]_*.csv')
    print filenames

    for f in filenames:
        print f#for checking purposes, prints file it's processing into terminal
        reader = csv.reader(open(f, 'rb'))
        pid = re.findall('[0-9]_([0-9][0-9][0-9])---', f)
        if len(pid)>0:
            name = pid[0] + '_'+ 'questions.csv'
        else:
            break
        if os.path.exists(name):
            writer = csv.writer(open(name,'ab'),delimiter = ',')
        else:
            writer = csv.writer(open( name ,'wb'))
            writer.writerow(['PID', 'Question', 'Score','Date','Session'])
        for row in reader:
            getRidofSpaces = list(r for r in row if r != '')
            if len(getRidofSpaces)<6 and row[1]!= "Practice round for level: ":

                writer.writerow(getRidofSpaces)#the last 4 rows, just put them back
    # moveFolder = CurrDir + '\\Questions'
    # if os.path.exists(moveFolder):
    #     if os.path.exists(moveFolder+name):
    #         continue
    #     shutil.copy(name,moveFolder)
    # else:
    #     os.mkdir(moveFolder)
    #     shutil.copy(name,moveFolder)
