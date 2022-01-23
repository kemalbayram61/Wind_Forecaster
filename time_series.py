import  pandas           as pd
import matplotlib.pyplot as plt
import seaborn           as sns

class TimeSeries:
    dataColumn = None
    dateColumn = None
    yLabel     = None

    def __init__(self, dataColumn, dateColumn, yLabel):
        self.dataColumn = dataColumn
        self.dateColumn = pd.to_datetime(dateColumn, format="%Y-%m-%d")
        self.yLabel     = yLabel

    def visualizeData(self):
        sns.set()
        plt.ylabel(self.yLabel)
        plt.xlabel('Tarih')
        plt.xticks(rotation=45)
        plt.plot(self.dateColumn, self.dataColumn)
        plt.show()

    def trainTestVisualization(self):
        train = self.dataColumn[0 : 650]
        test  = self.dataColumn[650 : ]

        plt.plot(train, color="black")
        plt.plot(test, color="red")
        plt.ylabel(self.yLabel)
        plt.xlabel('Tarih')
        plt.xticks(rotation=45)
        plt.show()
