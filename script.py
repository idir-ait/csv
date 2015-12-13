import time
import re



class VarType(object):
    def __init__(self, name, regex):
        self.regex=re.compile(regex)
        self.name=name
    def isPattern(self, str):
      return bool(self.regex.match(str))

#Renvoie le nombre de separateur 
def nbrSeparater(line, delimiter, separater):
    cpt = 1;
    inSentence = False
    for c in line:
        if(c == delimiter and inSentence == False):
         inSentence = True
        else :
         if(c == delimiter and inSentence == True):
          inSentence = False
        if(c == separater and inSentence == False):
         cpt = cpt + 1;
    return cpt

#Renvoie le nombre de column d'un fichier csv
def nbrColumn(path, delimiter, separater):
	file = open(path, 'r')
	return nbrSeparater(file.readline(), delimiter, separater)


def isInteger(str):
    return (str(int(str)) == str)

#Parametres d'entree
path = "/home/iah/csv_file_analysis/test.csv"
delimiter = '"'
separater = ","
#nbrCol = nbrColumn(path, delimiter, separater)

#Parametres de sortie
listWrongLines =[]

#------------------------------------------------Main---------------------------------------------------
start_time = time.time() #Tmp
"""
file = open(path, 'r')
i = 1;
while 1:
    line = file.readline()
    if (line == '') :
        break
    print(i)
    i = i+1
    nbrSep = nbrSeparater(line, delimiter, separater)
    if(nbrSep != nbrCol) :
     listWrongLines.append(i)

"""
print "coucou"
print("--- %s seconds ---" % (time.time() - start_time))#Tmp
#print nbrColumn(path, delimiter, separater)
#print listWrongLines



var=VarType('nombre','^[0-9]*$')


print var.isPattern("llg51545")

listVarType = []
listVarType.append(var)
listVarType.append(var)
listVarType.append(var)


countVect= [0] * len(listVarType)

class analyse(object):
    def __init__(self, nbrColumn, listVarType):
        self.mat = [] 
        for i in range(1, nbrColumn+1):
          self.mat.append([0] * len(listVarType))
        print self.mat
    def isPattern(self, str):
      return bool(self.regex.match(str))

t = analyse(5, listVarType)


