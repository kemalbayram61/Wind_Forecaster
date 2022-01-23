from data_converter import DataConverter
import pandas       as pd

dataConverter = DataConverter()

if __name__ == '__main__':
    dateColumn           = dataConverter.getData("daily", "maxRuzgarYonveHiz", isDayColumn=True)
    averageTemperature   = dataConverter.getData("daily", "ortalamaSicaklik")
    averageHumidity      = dataConverter.getData("daily", "ortalamaNem")
    averagePressure      = dataConverter.getData("daily", "aktuelBasinc")
    maxWindDirection     = dataConverter.splitData(dataConverter.getData("daily", "maxRuzgarYonveHiz")      , " ", 0)
    maxWindSpeed         = dataConverter.splitData(dataConverter.getData("daily", "maxRuzgarYonveHiz")      , " ", 1)
    averageWindDirection = dataConverter.splitData(dataConverter.getData("daily", "ortalamaRuzgarYonveHiz") , " ", 0)
    averageWindSpeed     = dataConverter.splitData(dataConverter.getData("daily", "ortalamaRuzgarYonveHiz") , " ", 1)

    #boyut kontrolü
    print("#### -> Filtrelemeden Önce")
    print(len(dateColumn))
    print(len(maxWindDirection))

    #filtreleneck indexlerin keşfi
    filterIndexes  = dataConverter.getFilterIndexes(maxWindDirection, None)

    #verilei indexlere göre filtreleme
    dateColumn       = dataConverter.filterData(dateColumn      , filterIndexes)
    maxWindDirection = dataConverter.filterData(maxWindDirection, filterIndexes)

    #boyut kontrolü
    print("#### -> Filtrelemeden Sonra")
    print(len(dateColumn))
    print(len(maxWindDirection))

