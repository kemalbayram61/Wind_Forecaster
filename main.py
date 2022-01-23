from data_converter          import DataConverter
from time_series             import TimeSeries
from artifical_neural_network import ANN
import pandas                as pd

dataConverter = DataConverter()
timeSeries    = None

def withTimeSeries():
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
    print(len(averageWindSpeed))

    #filtreleneck indexlerin keşfi
    filterIndexes  = dataConverter.getFilterIndexes(averageWindSpeed, None)

    #verilei indexlere göre filtreleme
    dateColumn       = dataConverter.filterData(dateColumn       , filterIndexes)
    averageWindSpeed = dataConverter.filterData(averageWindSpeed , filterIndexes, dataType = float)

    #boyut kontrolü
    print("#### -> Filtrelemeden Sonra")
    print(len(dateColumn))
    print(len(averageWindSpeed))

    #time series sınıfı
    timeSeries = TimeSeries(averageWindSpeed, dateColumn, yLabel="Ortalama Rüzgar Hızı")
    timeSeries.predictWithSARIMAX()
    timeSeries.predictWithARIMA()

def withANN():
    averageTemperature   = dataConverter.getData("daily", "ortalamaSicaklik")
    averageHumidity      = dataConverter.getData("daily", "ortalamaNem")
    averagePressure      = dataConverter.getData("daily", "aktuelBasinc")
    maxWindDirection     = dataConverter.splitData(dataConverter.getData("daily", "maxRuzgarYonveHiz")      , " ", 0)
    maxWindSpeed         = dataConverter.splitData(dataConverter.getData("daily", "maxRuzgarYonveHiz")      , " ", 1)
    averageWindDirection = dataConverter.splitData(dataConverter.getData("daily", "ortalamaRuzgarYonveHiz") , " ", 0)
    averageWindSpeed     = dataConverter.splitData(dataConverter.getData("daily", "ortalamaRuzgarYonveHiz") , " ", 1)

    #boyut kontrolü
    print("#### -> Filtrelemeden Önce")
    print(len(averageTemperature))
    print(len(averageHumidity))
    print(len(averagePressure))
    print(len(averageWindSpeed))

    #filtreleneck indexlerin keşfi  tahmin kolonu ortalama rüzgar hızı seçilmiştir
    filterIndexes  = dataConverter.getFilterIndexes(averageWindSpeed, None)

    #verilei indexlere göre filtreleme
    averageWindSpeed   = dataConverter.filterData(averageWindSpeed  , filterIndexes, dataType = float)
    averageTemperature = dataConverter.filterData(averageTemperature, filterIndexes, dataType = float)
    averageHumidity    = dataConverter.filterData(averageHumidity   , filterIndexes, dataType = float)
    averagePressure    = dataConverter.filterData(averagePressure   , filterIndexes, dataType = float)

    filterIndexes  = dataConverter.getFilterIndexes(averageTemperature, None)

    #verilei indexlere göre filtreleme
    averageWindSpeed   = dataConverter.filterData(averageWindSpeed  , filterIndexes, dataType = float)
    averageTemperature = dataConverter.filterData(averageTemperature, filterIndexes, dataType = float)
    averageHumidity    = dataConverter.filterData(averageHumidity   , filterIndexes, dataType = float)
    averagePressure    = dataConverter.filterData(averagePressure   , filterIndexes, dataType = float)

    filterIndexes  = dataConverter.getFilterIndexes(averageHumidity, None)

    #verilei indexlere göre filtreleme
    averageWindSpeed   = dataConverter.filterData(averageWindSpeed  , filterIndexes, dataType = float)
    averageTemperature = dataConverter.filterData(averageTemperature, filterIndexes, dataType = float)
    averageHumidity    = dataConverter.filterData(averageHumidity   , filterIndexes, dataType = float)
    averagePressure    = dataConverter.filterData(averagePressure   , filterIndexes, dataType = float)

    filterIndexes  = dataConverter.getFilterIndexes(averagePressure, None)

    #verilei indexlere göre filtreleme
    averageWindSpeed   = dataConverter.filterData(averageWindSpeed  , filterIndexes, dataType = float)
    averageTemperature = dataConverter.filterData(averageTemperature, filterIndexes, dataType = float)
    averageHumidity    = dataConverter.filterData(averageHumidity   , filterIndexes, dataType = float)
    averagePressure    = dataConverter.filterData(averagePressure   , filterIndexes, dataType = float)


    #boyut kontrolü
    print("#### -> Filtrelemeden Sonra")
    print(len(averageTemperature))
    print(len(averageHumidity))
    print(len(averagePressure))
    print(len(averageWindSpeed))

    #Sinir ağının kurulması
    ann = ANN(averageTemperature, "Ortalama Sicaklik", averageWindSpeed, "Ortalama Ruzgar Hizi")
    ann.addColumn(averageHumidity, "Ortalama Nem")
    ann.addColumn(averagePressure, "Ortalama Basinc")

    ann.predict()

if __name__ == '__main__':
    #withTimeSeries()
    withANN()
