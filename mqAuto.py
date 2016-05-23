import re, csv, os, os.path
import numpy as np
import glob
import shutil


#REGEX to find PID
CurrDir = os.getcwd()
print "You're in " + CurrDir

print "__________________"
folders = glob.glob('[0-9][0-9][0-9]')

for participant in folders:
    path = CurrDir + "\\" + participant
    os.chdir(path)
    print "Changing to: " + os.getcwd()

    print "STARTED"
    fn = glob.glob('[0-9][0-9]_*.csv')
    filenames = fn + glob.glob('[0-9]_*.csv')
    for name in filenames:
        # print "NAME:"
        # print name
        # size = os.stat(name).st_size
        # print "SIZE:"
        # print size
        #
        # if size < 2250:
        #     continue
        reader = csv.reader(open(name, 'rU'))  # open reader
        pid = re.findall('[0-9]+_([a-zA-Z0-9]+)---', name)  # find PID
        session = re.findall('([0-9]+)_[a-zA-Z0-9]+---', name) #find Session number
        print "Doing Session: " + str(session)
        if len(pid) < 1:
            break
        outputName = pid[0] + "_" + "clean.csv"

        reaction = {1:{1:[], 4:[], 5:[], 6:[], 13:[]}, 2:{1:[], 4:[], 5:[], 6:[], 13:[]},
        3:{1:[], 4:[], 5:[], 6:[], 13:[]}, 4:{1:[], 4:[], 5:[], 6:[], 13:[]},
         5:{1:[], 4:[], 5:[], 6:[], 13:[]}, 6:{1:[], 4:[], 5:[], 6:[], 13:[]},
          7:{1:[], 4:[], 5:[], 6:[], 13:[]}, 8:{1:[], 4:[], 5:[], 6:[], 13:[]},
           9:{1:[], 4:[], 5:[], 6:[], 13:[]} , 10:{1:[], 4:[], 5:[], 6:[], 13:[]}}
        acc = {1:{1:[], 4:[], 5:[], 6:[], 13:[]}, 2:{1:[], 4:[], 5:[], 6:[], 13:[]},
        3:{1:[], 4:[], 5:[], 6:[], 13:[]}, 4:{1:[], 4:[], 5:[], 6:[], 13:[]},
         5:{1:[], 4:[], 5:[], 6:[], 13:[]}, 6:{1:[], 4:[], 5:[], 6:[], 13:[]},
          7:{1:[], 4:[], 5:[], 6:[], 13:[]}, 8:{1:[], 4:[], 5:[], 6:[], 13:[]},
           9:{1:[], 4:[], 5:[], 6:[], 13:[]} , 10:{1:[], 4:[], 5:[], 6:[], 13:[]}}
        counts = {
        1:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []},
        2:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []},
        3:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []},
        4:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []},
        5:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []},
        6:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []},
        7:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []},
        8:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []},
        9:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []},
        10:{'eoo': 0, 'eoc': 0, 'tresp': 0, 'level': [], 'tacc': [], 'trt': []}
        }

        if os.path.exists(outputName):
            writer = csv.writer(open(outputName, 'ab'))  # open filewriter
        else:
            writer = csv.writer(open(outputName, 'wb'))
            writer.writerow(
                ['PID', 'Session', 'Round', 'Avg ACC', 'Avg RT', 'Avg Lvl', 'Total Responses', '#EOO', '#EOC', 'ACC Lure',
                 'ACC NLure', 'RT Lure', 'RT NLure'])  # write headers


        for row in reader:
            if row[0] == 'Participant ID' or len([t for t in row if len(t) > 0]) < 10: #Check if header or if row is short (practice or Qs)
                continue
            # print row[5]

            rnd = int(row[1])
            lvl = int(row[3])
            # print lvl
            luretype = int(row[5])
            # print luretype
            # print row[9]
            if row[7]!= '':
                rt = int(row[7])
            accuracy = int(row[8])
            pr = row[6]
            # nbacktype = row[17]
            if row[7]!= '':
                reaction[rnd][luretype].append(rt)  # {0: [0,0,0,1,0,1,1,0]}
            acc[rnd][luretype].append(accuracy) # {0: [0,0,0,1,0,1,1,0]}

            if accuracy == 0:
                if pr == 'tapped screen':
                    counts[rnd]['eoc'] += 1
                elif pr == 'no tap':
                    counts[rnd]['eoo'] += 1

            if pr == 'tapped screen':
                counts[rnd]['tresp'] += 1

            counts[rnd]['level'].append(lvl)
            counts[rnd]['tacc'].append(accuracy)
            if row[7]!= '':
                counts[rnd]['trt'].append(rt)

        for x in range(1,8):
            if x == 0:
                print "OH NO"
    #-------------------------------------------------------------------------------
            fullListNLacc1 = list(item for item in acc[x][1])
            fullListNLacc2 = list(item for item in acc[x][4])

            fullListNLacc = fullListNLacc1 + fullListNLacc2

            fullListLacc1 = list(item for item in acc[x][5])
            fullListLacc2 = list(item for item in acc[x][6])

            fullListLacc = fullListLacc1 + fullListLacc2

            # print x
            # print "FULL LIST L"
            # print fullListLacc
            # print "FULL LIST NL"
            # print fullListNLacc
            accl = np.mean(fullListLacc)
            accnl = np.mean(fullListNLacc)

    #-------------------------------------------------------------------------------

            fullListNLrt1 = list(item for item in reaction[x][4])
            fullListNLrt2 = list(item for item in reaction[x][1])

            fullListNLrt = fullListNLrt1 + fullListNLrt2

            fullListLrt1 = list(item for item in reaction[x][5])
            fullListLrt2 = list(item for item in reaction[x][6])

            fullListLrt = fullListLrt1 + fullListLrt2

            rtl = np.mean(fullListLrt)
            rtnl = np.mean(fullListNLrt)

            # print "ACC"
            # print acc
            # print "/n REACTION"
            # print reaction
            writer.writerow([pid[0], session[0], x, np.mean(counts[x]['tacc']), np.mean(counts[x]['trt']),
            np.mean(counts[x]['level']),counts[x]['tresp'], counts[x]['eoo'], counts[x]['eoc'],
            accl, accnl, rtl, rtnl,])

    # moveFolder = CurrDir + '\\Clean'
    # if os.path.exists(moveFolder):
    #     if os.path.exists(moveFolder+outputName):
    #         continue
    #     shutil.copy(outputName,moveFolder)
    # else:
    #     os.mkdir(moveFolder)
    #     shutil.copy(outputName,moveFolder)
