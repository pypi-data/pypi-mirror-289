import re

class Find_community_byhost():
    def __init__(self, genotype, A_csv, B_csv):
        self.genotype = genotype
        self.A_csv = A_csv
        self.B_csv = B_csv

    # Example function
    def AIVChina(self, nWlist, Zidian):
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
            if 2013 <= date < 2023 and subtyp.search(geno) and Host not in ["Human", "swine", "unknown", "unknow"] and location == "China":
                print(aKey, end="|")
                print("完整索引号:", aVal)
                eptList.append(Host)
                NumofCommu = i[1]
                eptList.append(NumofCommu)
                EMPTYlist.append(eptList)
        print("符合筛选条件的毒株宿主类型及所占社团数量:", EMPTYlist)
        # Further processing and saving to CSV can be done here...
