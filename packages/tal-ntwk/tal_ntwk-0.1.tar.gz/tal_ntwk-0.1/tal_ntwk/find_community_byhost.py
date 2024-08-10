import re
class Find_community_byhost():
    def __init__(self,genotype,A_csv,B_csv):
        self.genotype=genotype
        self.A_csv = A_csv
        self.B_csv = B_csv
    def AIVChina(self,nWlist,Zidian):
        EMPTYlist=[]
        for i in nWlist:
            eptList = []
            aKey = i[0]
            aVal = Zidian.get(aKey,0)  
            dat = aVal.strip().split(",")[8]
            date = float(dat)
            Host = aVal.strip().split(",")[9]
            geno = aVal.strip().split(",")[11]
            subtyp = re.compile(self.genotype)  
            location = aVal.strip().split(",")[12]  
            if 2013 <= date < 2023 and subtyp.search(geno) and Host != "Human" and Host != "swine" and Host != "unknown" and Host != "unknow" and location == "China":
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
        
        # ------------------------------------------------------------------------
        fopl = open(self.A_csv, 'w')
        flpr = open(self.B_csv, 'w')
        TotalCommu_Domans = 0
        TotalDomans = 0
        TotalCommu_Human = 0
        TotalHuman = 0
        TotalCommu_wildans = 0
        Totalwildans = 0
        TotalCommu_Domgal = 0
        TotalDomgal = 0
        TotalCommu_wildother = 0
        Totalwildother = 0
        TotalCommu_swine = 0
        Totalswine = 0
        TotalCommu_Domother = 0
        TotalDomother = 0
        TotalCommu_unknown = 0
        Totalunknown = 0
        TotalCommu_wildunknown = 0
        Totalwildunknown = 0
        TotalCommu_Domunknown = 0
        TotalDomunknown = 0
        TotalCommu_wildgal = 0
        Totalwildgal = 0
        for i in EMPTYlist:
            if i[0] == "Dom.ans":
                TotalCommu_Domans += i[1]
                TotalDomans += 1
            elif i[0] == "Human":
                TotalCommu_Human += i[1]
                TotalHuman += 1
            elif i[0] == "wild.ans":
                TotalCommu_wildans += i[1]
                Totalwildans += 1
            elif i[0] == "Dom.gal":
                TotalCommu_Domgal += i[1]
                TotalDomgal += 1
            elif i[0] == "wild.other":
                TotalCommu_wildother += i[1]
                Totalwildother += 1
            elif i[0] == "swine":
                TotalCommu_swine += i[1]
                Totalswine += 1
            elif i[0] == "Dom.other":
                TotalCommu_Domother += i[1]
                TotalDomother += 1
            elif i[0] == "unknown":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "unknow":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "Dom.unknown":
                TotalCommu_Domunknown += i[1]
                TotalDomunknown += 1
            elif i[0] == "wild.gal":
                TotalCommu_wildgal += i[1]
                Totalwildgal += 1
            elif i[0] == "wild.unknown":
                TotalCommu_wildunknown += i[1]
                Totalwildunknown += 1
        #g,DA,Hu,wa,dg,wo,sw,do,un,wn,du,wg

        if TotalCommu_Domans != 0:
            print("Dom.ans", TotalCommu_Domans, sep=",", file=fopl)
            print("Dom.ans", TotalDomans, sep=",", file=flpr)
        if TotalCommu_Human != 0:
            print("Human", TotalCommu_Human, sep=",", file=fopl)
            print("Human", TotalHuman, sep=",", file=flpr)
        if TotalCommu_wildans != 0:
            print("wild.ans", TotalCommu_wildans, sep=",", file=fopl)
            print("wild.ans", Totalwildans, sep=",", file=flpr)
        if TotalCommu_Domgal != 0:
            print("Dom.gal", TotalCommu_Domgal, sep=",", file=fopl)
            print("Dom.gal", TotalDomgal, sep=",", file=flpr)
        if TotalCommu_wildother != 0:
            print("wild.other", TotalCommu_wildother, sep=",", file=fopl)
            print("wild.other", Totalwildother, sep=",", file=flpr)
        if TotalCommu_swine != 0:
            print("swine", TotalCommu_swine, sep=",", file=fopl)
            print("swine", Totalswine, sep=",", file=flpr)
        if TotalCommu_Domother != 0:
            print("Dom.other", TotalCommu_Domother, sep=",", file=fopl)
            print("Dom.other", TotalDomother, sep=",", file=flpr)
        if TotalCommu_unknown != 0:
            print("unknown", TotalCommu_unknown, sep=",", file=fopl)
            print("unknown", Totalunknown, sep=",", file=flpr)
        if TotalCommu_wildunknown != 0:
            print("wild.unknown", TotalCommu_wildunknown, sep=",", file=fopl)
            print("wild.unknown", Totalwildunknown, sep=",", file=flpr)
        if TotalCommu_Domunknown != 0:
            print("Dom.unknown", TotalCommu_Domunknown, sep=",", file=fopl)
            print("Dom.unknown", TotalDomunknown, sep=",", file=flpr)
        if TotalCommu_wildgal != 0:
            print("wild.gal", TotalCommu_wildgal, sep=",", file=fopl)
            print("wild.gal", Totalwildgal, sep=",", file=flpr)
        fopl.close()
        flpr.close()

    def HIVChina(self, nWlist, Zidian):
        EMPTYlist = []
        for i in nWlist:
            eptList = []
            aKey = i[0] 
            aVal = Zidian.get(aKey, 0) 
            dat = aVal.strip().split(",")[8]
            date = float(dat)
            Host = aVal.strip().split(",")[9]
            geno = aVal.strip().split(",")[11]
            subtyp = re.compile(self.genotype)  
            location = aVal.strip().split(",")[12]  
            if 2013 <= date < 2023 and subtyp.search(
                    geno) and Host != "unknown" and Host != "unknow" and location == "China":
                
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)

        fopl = open(self.A_csv, 'w')
        flpr = open(self.B_csv, 'w')
        TotalCommu_Domans = 0
        TotalDomans = 0
        TotalCommu_Human = 0
        TotalHuman = 0
        TotalCommu_wildans = 0
        Totalwildans = 0
        TotalCommu_Domgal = 0
        TotalDomgal = 0
        TotalCommu_wildother = 0
        Totalwildother = 0
        TotalCommu_swine = 0
        Totalswine = 0
        TotalCommu_Domother = 0
        TotalDomother = 0
        TotalCommu_unknown = 0
        Totalunknown = 0
        TotalCommu_wildunknown = 0
        Totalwildunknown = 0
        TotalCommu_Domunknown = 0
        TotalDomunknown = 0
        TotalCommu_wildgal = 0
        Totalwildgal = 0
        for i in EMPTYlist:
            if i[0] == "Dom.ans":
                TotalCommu_Domans += i[1]
                TotalDomans += 1
            elif i[0] == "Human":
                TotalCommu_Human += i[1]
                TotalHuman += 1
            elif i[0] == "wild.ans":
                TotalCommu_wildans += i[1]
                Totalwildans += 1
            elif i[0] == "Dom.gal":
                TotalCommu_Domgal += i[1]
                TotalDomgal += 1
            elif i[0] == "wild.other":
                TotalCommu_wildother += i[1]
                Totalwildother += 1
            elif i[0] == "swine":
                TotalCommu_swine += i[1]
                Totalswine += 1
            elif i[0] == "Dom.other":
                TotalCommu_Domother += i[1]
                TotalDomother += 1
            elif i[0] == "unknown":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "unknow":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "Dom.unknown":
                TotalCommu_Domunknown += i[1]
                TotalDomunknown += 1
            elif i[0] == "wild.gal":
                TotalCommu_wildgal += i[1]
                Totalwildgal += 1
            elif i[0] == "wild.unknown":
                TotalCommu_wildunknown += i[1]
                Totalwildunknown += 1
        # g,DA,Hu,wa,dg,wo,sw,do,un,wn,du,wg

        if TotalCommu_Domans != 0:
            print("Dom.ans", TotalCommu_Domans, sep=",", file=fopl)
            print("Dom.ans", TotalDomans, sep=",", file=flpr)
        if TotalCommu_Human != 0:
            print("Human", TotalCommu_Human, sep=",", file=fopl)
            print("Human", TotalHuman, sep=",", file=flpr)
        if TotalCommu_wildans != 0:
            print("wild.ans", TotalCommu_wildans, sep=",", file=fopl)
            print("wild.ans", Totalwildans, sep=",", file=flpr)
        if TotalCommu_Domgal != 0:
            print("Dom.gal", TotalCommu_Domgal, sep=",", file=fopl)
            print("Dom.gal", TotalDomgal, sep=",", file=flpr)
        if TotalCommu_wildother != 0:
            print("wild.other", TotalCommu_wildother, sep=",", file=fopl)
            print("wild.other", Totalwildother, sep=",", file=flpr)
        if TotalCommu_swine != 0:
            print("swine", TotalCommu_swine, sep=",", file=fopl)
            print("swine", Totalswine, sep=",", file=flpr)
        if TotalCommu_Domother != 0:
            print("Dom.other", TotalCommu_Domother, sep=",", file=fopl)
            print("Dom.other", TotalDomother, sep=",", file=flpr)
        if TotalCommu_unknown != 0:
            print("unknown", TotalCommu_unknown, sep=",", file=fopl)
            print("unknown", Totalunknown, sep=",", file=flpr)
        if TotalCommu_wildunknown != 0:
            print("wild.unknown", TotalCommu_wildunknown, sep=",", file=fopl)
            print("wild.unknown", Totalwildunknown, sep=",", file=flpr)
        if TotalCommu_Domunknown != 0:
            print("Dom.unknown", TotalCommu_Domunknown, sep=",", file=fopl)
            print("Dom.unknown", TotalDomunknown, sep=",", file=flpr)
        if TotalCommu_wildgal != 0:
            print("wild.gal", TotalCommu_wildgal, sep=",", file=fopl)
            print("wild.gal", Totalwildgal, sep=",", file=flpr)
        fopl.close()
        flpr.close()

    def AIVNorthAmerica(self, nWlist, Zidian):
        EMPTYlist = []
        for i in nWlist:
            eptList = []
            aKey = i[0]  
            aVal = Zidian.get(aKey, 0) 
            dat = aVal.strip().split(",")[8]
            date = float(dat)
            Host = aVal.strip().split(",")[9]
            geno = aVal.strip().split(",")[11]
            subtyp = re.compile(self.genotype)  
            Loc = aVal.strip().split(",")[10] 
            if 2013 <= date < 2023 and subtyp.search(
                    geno) and Host != "unknown" and Host != "Human" and Host != "swine" and Host != "unknow" and Loc == "NorthAmerica":
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
        # ------------------------------------------------------------------------
        fopl = open(self.A_csv, 'w')
        flpr = open(self.B_csv, 'w')
        TotalCommu_Domans = 0
        TotalDomans = 0
        TotalCommu_Human = 0
        TotalHuman = 0
        TotalCommu_wildans = 0
        Totalwildans = 0
        TotalCommu_Domgal = 0
        TotalDomgal = 0
        TotalCommu_wildother = 0
        Totalwildother = 0
        TotalCommu_swine = 0
        Totalswine = 0
        TotalCommu_Domother = 0
        TotalDomother = 0
        TotalCommu_unknown = 0
        Totalunknown = 0
        TotalCommu_wildunknown = 0
        Totalwildunknown = 0
        TotalCommu_Domunknown = 0
        TotalDomunknown = 0
        TotalCommu_wildgal = 0
        Totalwildgal = 0
        for i in EMPTYlist:
            if i[0] == "Dom.ans":
                TotalCommu_Domans += i[1]
                TotalDomans += 1
            elif i[0] == "Human":
                TotalCommu_Human += i[1]
                TotalHuman += 1
            elif i[0] == "wild.ans":
                TotalCommu_wildans += i[1]
                Totalwildans += 1
            elif i[0] == "Dom.gal":
                TotalCommu_Domgal += i[1]
                TotalDomgal += 1
            elif i[0] == "wild.other":
                TotalCommu_wildother += i[1]
                Totalwildother += 1
            elif i[0] == "swine":
                TotalCommu_swine += i[1]
                Totalswine += 1
            elif i[0] == "Dom.other":
                TotalCommu_Domother += i[1]
                TotalDomother += 1
            elif i[0] == "unknown":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "unknow":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "Dom.unknown":
                TotalCommu_Domunknown += i[1]
                TotalDomunknown += 1
            elif i[0] == "wild.gal":
                TotalCommu_wildgal += i[1]
                Totalwildgal += 1
            elif i[0] == "wild.unknown":
                TotalCommu_wildunknown += i[1]
                Totalwildunknown += 1
        # g,DA,Hu,wa,dg,wo,sw,do,un,wn,du,wg

        if TotalCommu_Domans != 0:
            print("Dom.ans", TotalCommu_Domans, sep=",", file=fopl)
            print("Dom.ans", TotalDomans, sep=",", file=flpr)
        if TotalCommu_Human != 0:
            print("Human", TotalCommu_Human, sep=",", file=fopl)
            print("Human", TotalHuman, sep=",", file=flpr)
        if TotalCommu_wildans != 0:
            print("wild.ans", TotalCommu_wildans, sep=",", file=fopl)
            print("wild.ans", Totalwildans, sep=",", file=flpr)
        if TotalCommu_Domgal != 0:
            print("Dom.gal", TotalCommu_Domgal, sep=",", file=fopl)
            print("Dom.gal", TotalDomgal, sep=",", file=flpr)
        if TotalCommu_wildother != 0:
            print("wild.other", TotalCommu_wildother, sep=",", file=fopl)
            print("wild.other", Totalwildother, sep=",", file=flpr)
        if TotalCommu_swine != 0:
            print("swine", TotalCommu_swine, sep=",", file=fopl)
            print("swine", Totalswine, sep=",", file=flpr)
        if TotalCommu_Domother != 0:
            print("Dom.other", TotalCommu_Domother, sep=",", file=fopl)
            print("Dom.other", TotalDomother, sep=",", file=flpr)
        if TotalCommu_unknown != 0:
            print("unknown", TotalCommu_unknown, sep=",", file=fopl)
            print("unknown", Totalunknown, sep=",", file=flpr)
        if TotalCommu_wildunknown != 0:
            print("wild.unknown", TotalCommu_wildunknown, sep=",", file=fopl)
            print("wild.unknown", Totalwildunknown, sep=",", file=flpr)
        if TotalCommu_Domunknown != 0:
            print("Dom.unknown", TotalCommu_Domunknown, sep=",", file=fopl)
            print("Dom.unknown", TotalDomunknown, sep=",", file=flpr)
        if TotalCommu_wildgal != 0:
            print("wild.gal", TotalCommu_wildgal, sep=",", file=fopl)
            print("wild.gal", Totalwildgal, sep=",", file=flpr)
        fopl.close()
        flpr.close()

    def HIVNorthAmerica(self, nWlist, Zidian):
        EMPTYlist = []
        for i in nWlist:
            eptList = []
            aKey = i[0]  
            aVal = Zidian.get(aKey, 0) 
            dat = aVal.strip().split(",")[8]
            date = float(dat)
            Host = aVal.strip().split(",")[9]
            geno = aVal.strip().split(",")[11]
            subtyp = re.compile(self.genotype)  
            Loc = aVal.strip().split(",")[10]
            if 2013 <= date < 2023 and subtyp.search(
                    geno) and Host != "unknown" and Host != "unknow" and Loc == "NorthAmerica":
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
        # ------------------------------------------------------------------------
        fopl = open(self.A_csv, 'w')
        flpr = open(self.B_csv, 'w')
        TotalCommu_Domans = 0
        TotalDomans = 0
        TotalCommu_Human = 0
        TotalHuman = 0
        TotalCommu_wildans = 0
        Totalwildans = 0
        TotalCommu_Domgal = 0
        TotalDomgal = 0
        TotalCommu_wildother = 0
        Totalwildother = 0
        TotalCommu_swine = 0
        Totalswine = 0
        TotalCommu_Domother = 0
        TotalDomother = 0
        TotalCommu_unknown = 0
        Totalunknown = 0
        TotalCommu_wildunknown = 0
        Totalwildunknown = 0
        TotalCommu_Domunknown = 0
        TotalDomunknown = 0
        TotalCommu_wildgal = 0
        Totalwildgal = 0
        for i in EMPTYlist:
            if i[0] == "Dom.ans":
                TotalCommu_Domans += i[1]
                TotalDomans += 1
            elif i[0] == "Human":
                TotalCommu_Human += i[1]
                TotalHuman += 1
            elif i[0] == "wild.ans":
                TotalCommu_wildans += i[1]
                Totalwildans += 1
            elif i[0] == "Dom.gal":
                TotalCommu_Domgal += i[1]
                TotalDomgal += 1
            elif i[0] == "wild.other":
                TotalCommu_wildother += i[1]
                Totalwildother += 1
            elif i[0] == "swine":
                TotalCommu_swine += i[1]
                Totalswine += 1
            elif i[0] == "Dom.other":
                TotalCommu_Domother += i[1]
                TotalDomother += 1
            elif i[0] == "unknown":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "unknow":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "Dom.unknown":
                TotalCommu_Domunknown += i[1]
                TotalDomunknown += 1
            elif i[0] == "wild.gal":
                TotalCommu_wildgal += i[1]
                Totalwildgal += 1
            elif i[0] == "wild.unknown":
                TotalCommu_wildunknown += i[1]
                Totalwildunknown += 1
        # g,DA,Hu,wa,dg,wo,sw,do,un,wn,du,wg

        if TotalCommu_Domans != 0:
            print("Dom.ans", TotalCommu_Domans, sep=",", file=fopl)
            print("Dom.ans", TotalDomans, sep=",", file=flpr)
        if TotalCommu_Human != 0:
            print("Human", TotalCommu_Human, sep=",", file=fopl)
            print("Human", TotalHuman, sep=",", file=flpr)
        if TotalCommu_wildans != 0:
            print("wild.ans", TotalCommu_wildans, sep=",", file=fopl)
            print("wild.ans", Totalwildans, sep=",", file=flpr)
        if TotalCommu_Domgal != 0:
            print("Dom.gal", TotalCommu_Domgal, sep=",", file=fopl)
            print("Dom.gal", TotalDomgal, sep=",", file=flpr)
        if TotalCommu_wildother != 0:
            print("wild.other", TotalCommu_wildother, sep=",", file=fopl)
            print("wild.other", Totalwildother, sep=",", file=flpr)
        if TotalCommu_swine != 0:
            print("swine", TotalCommu_swine, sep=",", file=fopl)
            print("swine", Totalswine, sep=",", file=flpr)
        if TotalCommu_Domother != 0:
            print("Dom.other", TotalCommu_Domother, sep=",", file=fopl)
            print("Dom.other", TotalDomother, sep=",", file=flpr)
        if TotalCommu_unknown != 0:
            print("unknown", TotalCommu_unknown, sep=",", file=fopl)
            print("unknown", Totalunknown, sep=",", file=flpr)
        if TotalCommu_wildunknown != 0:
            print("wild.unknown", TotalCommu_wildunknown, sep=",", file=fopl)
            print("wild.unknown", Totalwildunknown, sep=",", file=flpr)
        if TotalCommu_Domunknown != 0:
            print("Dom.unknown", TotalCommu_Domunknown, sep=",", file=fopl)
            print("Dom.unknown", TotalDomunknown, sep=",", file=flpr)
        if TotalCommu_wildgal != 0:
            print("wild.gal", TotalCommu_wildgal, sep=",", file=fopl)
            print("wild.gal", Totalwildgal, sep=",", file=flpr)
        fopl.close()
        flpr.close()

    def AIVEurope(self, nWlist, Zidian):
        EMPTYlist = []
        for i in nWlist:
            eptList = []
            aKey = i[0] 
            aVal = Zidian.get(aKey, 0) 
            dat = aVal.strip().split(",")[8]
            date = float(dat)
            Host = aVal.strip().split(",")[9]
            geno = aVal.strip().split(",")[11]
            subtyp = re.compile(self.genotype)
            Loc = aVal.strip().split(",")[10] 
            if date > 2013 and subtyp.search(geno) and Host != "Human" and Host != "swine" and Host != "unknown" and Host != "unknow" and Loc == "WesternEurope":
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
            elif date > 2013 and subtyp.search(geno) and Host != "Human" and Host != "swine" and Host != "unknown" and Host != "unknow" and Loc == "EasternEurope":
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
            elif date > 2013 and subtyp.search(geno) and Host != "Human" and Host != "swine" and Host != "unknown" and Host != "unknow" and Loc == "SouthernEurope":
                
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
            elif date > 2013 and subtyp.search(geno) and Host != "Human" and Host != "swine" and Host != "unknown" and Host != "unknow" and Loc == "CentralEurope":
               
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
            elif date > 2013 and subtyp.search(geno) and Host != "Human" and Host != "swine" and Host != "unknown" and Host != "unknow" and Loc == "NorthernEurope":
                
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
        
        fopl = open(self.A_csv, 'w')
        flpr = open(self.B_csv, 'w')
        TotalCommu_Domans = 0
        TotalDomans = 0
        TotalCommu_Human = 0
        TotalHuman = 0
        TotalCommu_wildans = 0
        Totalwildans = 0
        TotalCommu_Domgal = 0
        TotalDomgal = 0
        TotalCommu_wildother = 0
        Totalwildother = 0
        TotalCommu_swine = 0
        Totalswine = 0
        TotalCommu_Domother = 0
        TotalDomother = 0
        TotalCommu_unknown = 0
        Totalunknown = 0
        TotalCommu_wildunknown = 0
        Totalwildunknown = 0
        TotalCommu_Domunknown = 0
        TotalDomunknown = 0
        TotalCommu_wildgal = 0
        Totalwildgal = 0
        for i in EMPTYlist:
            if i[0] == "Dom.ans":
                TotalCommu_Domans += i[1]
                TotalDomans += 1
            elif i[0] == "Human":
                TotalCommu_Human += i[1]
                TotalHuman += 1
            elif i[0] == "wild.ans":
                TotalCommu_wildans += i[1]
                Totalwildans += 1
            elif i[0] == "Dom.gal":
                TotalCommu_Domgal += i[1]
                TotalDomgal += 1
            elif i[0] == "wild.other":
                TotalCommu_wildother += i[1]
                Totalwildother += 1
            elif i[0] == "swine":
                TotalCommu_swine += i[1]
                Totalswine += 1
            elif i[0] == "Dom.other":
                TotalCommu_Domother += i[1]
                TotalDomother += 1
            elif i[0] == "unknown":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "unknow":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "Dom.unknown":
                TotalCommu_Domunknown += i[1]
                TotalDomunknown += 1
            elif i[0] == "wild.gal":
                TotalCommu_wildgal += i[1]
                Totalwildgal += 1
            elif i[0] == "wild.unknown":
                TotalCommu_wildunknown += i[1]
                Totalwildunknown += 1
        # g,DA,Hu,wa,dg,wo,sw,do,un,wn,du,wg

        if TotalCommu_Domans != 0:
            print("Dom.ans", TotalCommu_Domans, sep=",", file=fopl)
            print("Dom.ans", TotalDomans, sep=",", file=flpr)
        if TotalCommu_Human != 0:
            print("Human", TotalCommu_Human, sep=",", file=fopl)
            print("Human", TotalHuman, sep=",", file=flpr)
        if TotalCommu_wildans != 0:
            print("wild.ans", TotalCommu_wildans, sep=",", file=fopl)
            print("wild.ans", Totalwildans, sep=",", file=flpr)
        if TotalCommu_Domgal != 0:
            print("Dom.gal", TotalCommu_Domgal, sep=",", file=fopl)
            print("Dom.gal", TotalDomgal, sep=",", file=flpr)
        if TotalCommu_wildother != 0:
            print("wild.other", TotalCommu_wildother, sep=",", file=fopl)
            print("wild.other", Totalwildother, sep=",", file=flpr)
        if TotalCommu_swine != 0:
            print("swine", TotalCommu_swine, sep=",", file=fopl)
            print("swine", Totalswine, sep=",", file=flpr)
        if TotalCommu_Domother != 0:
            print("Dom.other", TotalCommu_Domother, sep=",", file=fopl)
            print("Dom.other", TotalDomother, sep=",", file=flpr)
        if TotalCommu_unknown != 0:
            print("unknown", TotalCommu_unknown, sep=",", file=fopl)
            print("unknown", Totalunknown, sep=",", file=flpr)
        if TotalCommu_wildunknown != 0:
            print("wild.unknown", TotalCommu_wildunknown, sep=",", file=fopl)
            print("wild.unknown", Totalwildunknown, sep=",", file=flpr)
        if TotalCommu_Domunknown != 0:
            print("Dom.unknown", TotalCommu_Domunknown, sep=",", file=fopl)
            print("Dom.unknown", TotalDomunknown, sep=",", file=flpr)
        if TotalCommu_wildgal != 0:
            print("wild.gal", TotalCommu_wildgal, sep=",", file=fopl)
            print("wild.gal", Totalwildgal, sep=",", file=flpr)
        fopl.close()
        flpr.close()

    def HIVEurope(self, nWlist, Zidian):
        EMPTYlist = []
        for i in nWlist:
            eptList = []
            aKey = i[0] 
            aVal = Zidian.get(aKey, 0) 
            dat = aVal.strip().split(",")[8]
            date = float(dat)
            Host = aVal.strip().split(",")[9]
            geno = aVal.strip().split(",")[11]
            subtyp = re.compile(self.genotype)  
            Loc = aVal.strip().split(",")[10] 
            if date > 2013 and subtyp.search(geno) and Host != "unknown" and Host != "unknow" and Loc == "WesternEurope":
                
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
            elif date > 2013 and subtyp.search(geno) and Host != "unknown" and Host != "unknow" and Loc == "EasternEurope":
                
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
            elif date > 2013 and subtyp.search(geno) and Host != "unknown" and Host != "unknow" and Loc == "SouthernEurope":
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
            elif date > 2013 and subtyp.search(geno) and Host != "unknown" and Host != "unknow" and Loc == "CentralEurope":
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
            elif date > 2013 and subtyp.search(geno) and Host != "unknown" and Host != "unknow" and Loc == "NorthernEurope":
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
        # ------------------------------------------------------------------------
        fopl = open(self.A_csv, 'w')
        flpr = open(self.B_csv, 'w')
        TotalCommu_Domans = 0
        TotalDomans = 0
        TotalCommu_Human = 0
        TotalHuman = 0
        TotalCommu_wildans = 0
        Totalwildans = 0
        TotalCommu_Domgal = 0
        TotalDomgal = 0
        TotalCommu_wildother = 0
        Totalwildother = 0
        TotalCommu_swine = 0
        Totalswine = 0
        TotalCommu_Domother = 0
        TotalDomother = 0
        TotalCommu_unknown = 0
        Totalunknown = 0
        TotalCommu_wildunknown = 0
        Totalwildunknown = 0
        TotalCommu_Domunknown = 0
        TotalDomunknown = 0
        TotalCommu_wildgal = 0
        Totalwildgal = 0
        for i in EMPTYlist:
            if i[0] == "Dom.ans":
                TotalCommu_Domans += i[1]
                TotalDomans += 1
            elif i[0] == "Human":
                TotalCommu_Human += i[1]
                TotalHuman += 1
            elif i[0] == "wild.ans":
                TotalCommu_wildans += i[1]
                Totalwildans += 1
            elif i[0] == "Dom.gal":
                TotalCommu_Domgal += i[1]
                TotalDomgal += 1
            elif i[0] == "wild.other":
                TotalCommu_wildother += i[1]
                Totalwildother += 1
            elif i[0] == "swine":
                TotalCommu_swine += i[1]
                Totalswine += 1
            elif i[0] == "Dom.other":
                TotalCommu_Domother += i[1]
                TotalDomother += 1
            elif i[0] == "unknown":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "unknow":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "Dom.unknown":
                TotalCommu_Domunknown += i[1]
                TotalDomunknown += 1
            elif i[0] == "wild.gal":
                TotalCommu_wildgal += i[1]
                Totalwildgal += 1
            elif i[0] == "wild.unknown":
                TotalCommu_wildunknown += i[1]
                Totalwildunknown += 1
        # g,DA,Hu,wa,dg,wo,sw,do,un,wn,du,wg

        if TotalCommu_Domans != 0:
            print("Dom.ans", TotalCommu_Domans, sep=",", file=fopl)
            print("Dom.ans", TotalDomans, sep=",", file=flpr)
        if TotalCommu_Human != 0:
            print("Human", TotalCommu_Human, sep=",", file=fopl)
            print("Human", TotalHuman, sep=",", file=flpr)
        if TotalCommu_wildans != 0:
            print("wild.ans", TotalCommu_wildans, sep=",", file=fopl)
            print("wild.ans", Totalwildans, sep=",", file=flpr)
        if TotalCommu_Domgal != 0:
            print("Dom.gal", TotalCommu_Domgal, sep=",", file=fopl)
            print("Dom.gal", TotalDomgal, sep=",", file=flpr)
        if TotalCommu_wildother != 0:
            print("wild.other", TotalCommu_wildother, sep=",", file=fopl)
            print("wild.other", Totalwildother, sep=",", file=flpr)
        if TotalCommu_swine != 0:
            print("swine", TotalCommu_swine, sep=",", file=fopl)
            print("swine", Totalswine, sep=",", file=flpr)
        if TotalCommu_Domother != 0:
            print("Dom.other", TotalCommu_Domother, sep=",", file=fopl)
            print("Dom.other", TotalDomother, sep=",", file=flpr)
        if TotalCommu_unknown != 0:
            print("unknown", TotalCommu_unknown, sep=",", file=fopl)
            print("unknown", Totalunknown, sep=",", file=flpr)
        if TotalCommu_wildunknown != 0:
            print("wild.unknown", TotalCommu_wildunknown, sep=",", file=fopl)
            print("wild.unknown", Totalwildunknown, sep=",", file=flpr)
        if TotalCommu_Domunknown != 0:
            print("Dom.unknown", TotalCommu_Domunknown, sep=",", file=fopl)
            print("Dom.unknown", TotalDomunknown, sep=",", file=flpr)
        if TotalCommu_wildgal != 0:
            print("wild.gal", TotalCommu_wildgal, sep=",", file=fopl)
            print("wild.gal", Totalwildgal, sep=",", file=flpr)
        fopl.close()
        flpr.close()

    def AIVGlobal(self, nWlist, Zidian):
        EMPTYlist = []
        for i in nWlist:
            eptList = []
            aKey = i[0]  
            aVal = Zidian.get(aKey, 0)  
            dat = aVal.strip().split(",")[8]
            date = float(dat)
            Host = aVal.strip().split(",")[9]
            geno = aVal.strip().split(",")[11]
            subtyp = re.compile(self.genotype)  
            if 2013 <= date < 2023 and subtyp.search(
                    geno) and Host != "Human" and Host != "swine" and Host != "unknown" and Host != "unknow" :
                
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
        fopl = open(self.A_csv, 'w')
        flpr = open(self.B_csv, 'w')
        TotalCommu_Domans = 0
        TotalDomans = 0
        TotalCommu_Human = 0
        TotalHuman = 0
        TotalCommu_wildans = 0
        Totalwildans = 0
        TotalCommu_Domgal = 0
        TotalDomgal = 0
        TotalCommu_wildother = 0
        Totalwildother = 0
        TotalCommu_swine = 0
        Totalswine = 0
        TotalCommu_Domother = 0
        TotalDomother = 0
        TotalCommu_unknown = 0
        Totalunknown = 0
        TotalCommu_wildunknown = 0
        Totalwildunknown = 0
        TotalCommu_Domunknown = 0
        TotalDomunknown = 0
        TotalCommu_wildgal = 0
        Totalwildgal = 0
        for i in EMPTYlist:
            if i[0] == "Dom.ans":
                TotalCommu_Domans += i[1]
                TotalDomans += 1
            elif i[0] == "Human":
                TotalCommu_Human += i[1]
                TotalHuman += 1
            elif i[0] == "wild.ans":
                TotalCommu_wildans += i[1]
                Totalwildans += 1
            elif i[0] == "Dom.gal":
                TotalCommu_Domgal += i[1]
                TotalDomgal += 1
            elif i[0] == "wild.other":
                TotalCommu_wildother += i[1]
                Totalwildother += 1
            elif i[0] == "swine":
                TotalCommu_swine += i[1]
                Totalswine += 1
            elif i[0] == "Dom.other":
                TotalCommu_Domother += i[1]
                TotalDomother += 1
            elif i[0] == "unknown":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "unknow":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "Dom.unknown":
                TotalCommu_Domunknown += i[1]
                TotalDomunknown += 1
            elif i[0] == "wild.gal":
                TotalCommu_wildgal += i[1]
                Totalwildgal += 1
            elif i[0] == "wild.unknown":
                TotalCommu_wildunknown += i[1]
                Totalwildunknown += 1
        # g,DA,Hu,wa,dg,wo,sw,do,un,wn,du,wg

        if TotalCommu_Domans != 0:
            print("Dom.ans", TotalCommu_Domans, sep=",", file=fopl)
            print("Dom.ans", TotalDomans, sep=",", file=flpr)
        if TotalCommu_Human != 0:
            print("Human", TotalCommu_Human, sep=",", file=fopl)
            print("Human", TotalHuman, sep=",", file=flpr)
        if TotalCommu_wildans != 0:
            print("wild.ans", TotalCommu_wildans, sep=",", file=fopl)
            print("wild.ans", Totalwildans, sep=",", file=flpr)
        if TotalCommu_Domgal != 0:
            print("Dom.gal", TotalCommu_Domgal, sep=",", file=fopl)
            print("Dom.gal", TotalDomgal, sep=",", file=flpr)
        if TotalCommu_wildother != 0:
            print("wild.other", TotalCommu_wildother, sep=",", file=fopl)
            print("wild.other", Totalwildother, sep=",", file=flpr)
        if TotalCommu_swine != 0:
            print("swine", TotalCommu_swine, sep=",", file=fopl)
            print("swine", Totalswine, sep=",", file=flpr)
        if TotalCommu_Domother != 0:
            print("Dom.other", TotalCommu_Domother, sep=",", file=fopl)
            print("Dom.other", TotalDomother, sep=",", file=flpr)
        if TotalCommu_unknown != 0:
            print("unknown", TotalCommu_unknown, sep=",", file=fopl)
            print("unknown", Totalunknown, sep=",", file=flpr)
        if TotalCommu_wildunknown != 0:
            print("wild.unknown", TotalCommu_wildunknown, sep=",", file=fopl)
            print("wild.unknown", Totalwildunknown, sep=",", file=flpr)
        if TotalCommu_Domunknown != 0:
            print("Dom.unknown", TotalCommu_Domunknown, sep=",", file=fopl)
            print("Dom.unknown", TotalDomunknown, sep=",", file=flpr)
        if TotalCommu_wildgal != 0:
            print("wild.gal", TotalCommu_wildgal, sep=",", file=fopl)
            print("wild.gal", Totalwildgal, sep=",", file=flpr)
        fopl.close()
        flpr.close()

    def HIVGlobal(self, nWlist, Zidian):
        EMPTYlist = []
        for i in nWlist:
            eptList = []
            aKey = i[0]  
            aVal = Zidian.get(aKey, 0) 
            dat = aVal.strip().split(",")[8]
            date = float(dat)
            Host = aVal.strip().split(",")[9]
            geno = aVal.strip().split(",")[11]
            subtyp = re.compile(self.genotype)  
            if 2013 <= date < 2023 and subtyp.search(
                    geno) and Host != "unknown" and Host != "unknow" :
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
        
        fopl = open(self.A_csv, 'w')
        flpr = open(self.B_csv, 'w')
        TotalCommu_Domans = 0
        TotalDomans = 0
        TotalCommu_Human = 0
        TotalHuman = 0
        TotalCommu_wildans = 0
        Totalwildans = 0
        TotalCommu_Domgal = 0
        TotalDomgal = 0
        TotalCommu_wildother = 0
        Totalwildother = 0
        TotalCommu_swine = 0
        Totalswine = 0
        TotalCommu_Domother = 0
        TotalDomother = 0
        TotalCommu_unknown = 0
        Totalunknown = 0
        TotalCommu_wildunknown = 0
        Totalwildunknown = 0
        TotalCommu_Domunknown = 0
        TotalDomunknown = 0
        TotalCommu_wildgal = 0
        Totalwildgal = 0
        for i in EMPTYlist:
            if i[0] == "Dom.ans":
                TotalCommu_Domans += i[1]
                TotalDomans += 1
            elif i[0] == "Human":
                TotalCommu_Human += i[1]
                TotalHuman += 1
            elif i[0] == "wild.ans":
                TotalCommu_wildans += i[1]
                Totalwildans += 1
            elif i[0] == "Dom.gal":
                TotalCommu_Domgal += i[1]
                TotalDomgal += 1
            elif i[0] == "wild.other":
                TotalCommu_wildother += i[1]
                Totalwildother += 1
            elif i[0] == "swine":
                TotalCommu_swine += i[1]
                Totalswine += 1
            elif i[0] == "Dom.other":
                TotalCommu_Domother += i[1]
                TotalDomother += 1
            elif i[0] == "unknown":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "unknow":
                TotalCommu_unknown += i[1]
                Totalunknown += 1
            elif i[0] == "Dom.unknown":
                TotalCommu_Domunknown += i[1]
                TotalDomunknown += 1
            elif i[0] == "wild.gal":
                TotalCommu_wildgal += i[1]
                Totalwildgal += 1
            elif i[0] == "wild.unknown":
                TotalCommu_wildunknown += i[1]
                Totalwildunknown += 1
        # g,DA,Hu,wa,dg,wo,sw,do,un,wn,du,wg

        if TotalCommu_Domans != 0:
            print("Dom.ans", TotalCommu_Domans, sep=",", file=fopl)
            print("Dom.ans", TotalDomans, sep=",", file=flpr)
        if TotalCommu_Human != 0:
            print("Human", TotalCommu_Human, sep=",", file=fopl)
            print("Human", TotalHuman, sep=",", file=flpr)
        if TotalCommu_wildans != 0:
            print("wild.ans", TotalCommu_wildans, sep=",", file=fopl)
            print("wild.ans", Totalwildans, sep=",", file=flpr)
        if TotalCommu_Domgal != 0:
            print("Dom.gal", TotalCommu_Domgal, sep=",", file=fopl)
            print("Dom.gal", TotalDomgal, sep=",", file=flpr)
        if TotalCommu_wildother != 0:
            print("wild.other", TotalCommu_wildother, sep=",", file=fopl)
            print("wild.other", Totalwildother, sep=",", file=flpr)
        if TotalCommu_swine != 0:
            print("swine", TotalCommu_swine, sep=",", file=fopl)
            print("swine", Totalswine, sep=",", file=flpr)
        if TotalCommu_Domother != 0:
            print("Dom.other", TotalCommu_Domother, sep=",", file=fopl)
            print("Dom.other", TotalDomother, sep=",", file=flpr)
        if TotalCommu_unknown != 0:
            print("unknown", TotalCommu_unknown, sep=",", file=fopl)
            print("unknown", Totalunknown, sep=",", file=flpr)
        if TotalCommu_wildunknown != 0:
            print("wild.unknown", TotalCommu_wildunknown, sep=",", file=fopl)
            print("wild.unknown", Totalwildunknown, sep=",", file=flpr)
        if TotalCommu_Domunknown != 0:
            print("Dom.unknown", TotalCommu_Domunknown, sep=",", file=fopl)
            print("Dom.unknown", TotalDomunknown, sep=",", file=flpr)
        if TotalCommu_wildgal != 0:
            print("wild.gal", TotalCommu_wildgal, sep=",", file=fopl)
            print("wild.gal", Totalwildgal, sep=",", file=flpr)
        fopl.close()
        flpr.close()