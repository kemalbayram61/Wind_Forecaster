import pandas as pd

class DataVariables:
    @staticmethod
    def getDailyFilesPath():
        return {"maxRuzgarYonveHiz"      : "data/20220105GunlukMaxRuzgarYonuveHizi.xlsx",
                "ortalamaSicaklik"       : "data/20220105GunlukOrtalamaSicaklik.xlsx",
                "ortalamaRuzgarYonveHiz" : "data/20220105GunlukOrtalamaRuzgarYonuveHizi.xlsx",
                "ortalamaNem"            : "data/20220105GunlukOrtalamaNispiNem.xlsx",
                "aktuelBasinc"           : "data/20220105GunlukOrtalamaAktuelBasinc.xlsx"}

    @staticmethod
    def getHourlyFilesPath():
        return {"aktuelBasinc"   : "data/20220106SaatlikAktuelBasinc.xlsx",
                "nem"            : "data/20220106SaatlikNispiNem.xlsx",
                "ruzgarYonveHiz" : "data/20220106SaatlikRuzgarYonuveHizi.xlsx",
                "sicaklik"       : "data/20220106SaatlikSicaklik.xlsx"}

    @staticmethod
    def getDailyFilesDataFrame():
        #[baslangic satiri, bitiş satiri + 1, başlangıç kolonu, bitiş kolonu + 1]
        return {"maxRuzgarYonveHiz"      : [[5, 36, 2, 14],[44, 75, 2, 14]],
                "ortalamaSicaklik"       : [[5, 36, 2, 14],[44, 75, 2, 14]],
                "ortalamaRuzgarYonveHiz" : [[5, 36, 2, 14],[44, 75, 2, 14]],
                "ortalamaNem"            : [[5, 36, 2, 14],[44, 75, 2, 14]],
                "aktuelBasinc"           : [[5, 36, 2, 14],[44, 75, 2, 14]]}

    @staticmethod
    def getHourlyFilesDataFrame():
        #TODO Hesaplamaları ekle
        return {"aktuelBasinc"   : [[5, 26, 2, 25],[33, 43, 2, 25]],
                "nem"            : [[5, 36, 2, 25],[44, 75, 2, 25]],
                "ruzgarYonveHiz" : [[5, 36, 2, 25],[44, 75, 2, 25]],
                "sicaklik"       : [[5, 36, 2, 25],[44, 75, 2, 25]]}

class DataConverter:

    def getData(self, type, key, isDayColumn = False):
        if(type == "daily"):
            currentYear  = None
            shape        = None
            dataColumn   = []
            data         = pd.read_excel(DataVariables.getDailyFilesPath()[key], engine = "openpyxl")
            dataFrames   = DataVariables.getDailyFilesDataFrame()[key]

            #dataFramelerin her biri bir yıllık veriyi gösterir
            for year in range(len(dataFrames)):
                currentYear = data.iloc[dataFrames[year][0] : dataFrames[year][1], dataFrames[year][2] : dataFrames[year][3]]
                shape       = currentYear.shape
                #her bir kolon için bütün satırlar gezinilerek ver oluşturulur
                for col in range(shape[1]):
                    for row in range(shape[0]):
                        #eğitim için günlük bütün veriler peş peşe eklenir
                        if(isDayColumn == False):
                            dataColumn.append(currentYear.iloc[row, col])
                        else:
                            dataColumn.append(str(2020 + year) + "-" + str(col + 1) + "-" + str(row + 1))
            return dataColumn

        elif(type == "hourly"):
            #TODO Saatlik biçimde çalışacak hale getir
            pass
    def splitData(self, dataColumn, splitChar, selectedRow):
        response = []
        for i in range(len(dataColumn)):
            if(str(dataColumn[i]) != 'nan'):
                response.append(dataColumn[i].split(splitChar)[selectedRow])
            else:
                response.append(None)
        return  response

    #parametre olaerak aldığı kolonu belirlenen filtreye göre filtreleyip filtrenin bulunduğu indexleri döndürür
    def getFilterIndexes(self, dataColumn, filterData):
        response = []
        for i in range(len(dataColumn)):
            if(dataColumn[i] == filterData):
                response.append(i)
        return  response

    #parametre olarak adığı filtreleme indexlerini kolondki verilerden çıkartmaktadır.
    def filterData(self, dataColumn, filterIndexes, dataType = None):
        response = []

        for i in range(len(dataColumn)):
            if(i not in filterIndexes):
                if(dataType == None):
                    response.append(dataColumn[i])
                else:
                    if(dataColumn[i] != None):
                        if(type(dataColumn[i]) == type("k") and dataColumn[i].strip()[-1].isnumeric() == False):
                            response.append(dataType(dataColumn[i].strip()[0: len(dataColumn[i].strip()) - 1]))
                        elif(type(dataColumn[i]) == type("k")):
                            response.append(dataType(dataColumn[i].strip()))
                        else:
                            response.append(dataColumn[i])
                    else:
                        response.append(None)

        return response