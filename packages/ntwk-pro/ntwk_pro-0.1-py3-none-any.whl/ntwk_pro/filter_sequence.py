class Filter_sequence():
    def __init__(self, file):
        self.file = file

    def SQ_LS(self):
        sq_ls = []
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
            sq_ls.append(aList)
        return sq_ls
