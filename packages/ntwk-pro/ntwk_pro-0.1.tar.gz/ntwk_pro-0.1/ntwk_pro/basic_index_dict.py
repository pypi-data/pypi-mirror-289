class Basic_index_Dict(): 
    def __init__(self, file):
        self.file = file

    def basic_dict_index(self):
        fDict = {}
        for line in open(self.file):  
            lis = line.strip().split("=")[1]
            LiS = "[" + lis + "]"
            vAl = line.strip().split("=")[0]
            valu = vAl[8:]
            fDict[LiS] = valu
        return fDict

    def clifin_Exclusive_dict_index(self):
        mkDict = {}
        for line in open(self.file):  
            lis = line.strip().split("=")[1]
            vAl = line.strip().split("=")[0]
            valu = vAl[8:]  
            mkDict[valu] = lis
        return mkDict

    def read_basic_index(self):
        LIs = []
        for line in open(self.file):
            lis = line.strip().split("=")[1]
            aList = []
            i = 0
            while i < 8:  
                fst = lis.split(",")[i]
                fst = int(fst)
                aList.append(fst)
                i += 1
            dt = lis.split(",")[8]
            dt = float(dt)
            aList.append(dt)  
            j = 9  
            while j < 13:  
                apd = lis.split(",")[j]
                aList.append(apd)
                j += 1
            LIs.append(aList)
        return LIs
