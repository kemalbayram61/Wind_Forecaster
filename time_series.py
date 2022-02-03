from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model        import ARIMA
import  pandas                          as pd
import matplotlib.pyplot                as plt
import seaborn                          as sns
import numpy                            as np

class TimeSeries:
    dataColumn = None
    dateColumn = None
    yLabel     = None
    test       = None
    train      = None

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

    def prepareTestAndTrain(self):
        splitCount       = int(len(self.dataColumn)*0.98)
        self.train       = pd.DataFrame(np.reshape(self.dataColumn[0:splitCount], (splitCount, 1)), columns=[self.yLabel])
        self.train.index = self.dateColumn[0:splitCount]
        self.test        = pd.DataFrame(np.reshape(self.dataColumn[splitCount:], (len(self.dateColumn) - splitCount, 1)), columns=[self.yLabel])
        self.test.index  = self.dateColumn[splitCount:]

        plt.plot(self.train, color="blue")
        plt.plot(self.test  , color="red")
        plt.ylabel(self.yLabel)
        plt.xlabel('Tarih')
        plt.xticks(rotation=45)
        #plt.show()

    def predictWithSARIMAX(self):
        self.prepareTestAndTrain()
        #seasonal_order = (Mevsimsel AR(Accounts Receivable) özelliği, Mevsimsel Entegrasyon sırası, Mevsimsel MA(Moving Average), Mevsimsel periyodiklik)
        #model    = SARIMAX(self.train, order=(5,1,0), seasonal_order=(5,1,1,12))
        model = SARIMAX(self.train, order=(1,1,1), sesional_order=(1,1,1,1))
        model = model.fit()

        #modelin içeriğne ait özet bilgisi
        model.summary()

        prediction        = model.get_forecast(len(self.test.index))
        results           = prediction.conf_int(alpha=0.05)
        results["Tahmin"] = model.predict(start=results.index[0], end=results.index[-1])
        results.index     = self.test.index
        plt.plot(results["Tahmin"], color='green', label='Tahminler')
        plt.legend()
        plt.show()

    def predictWithARIMA(self):
        self.prepareTestAndTrain()
        #order = (P = otoregresif model parametresi, D = fark alma , Q = hareketli ortalama gecikmeleri)
        model    = ARIMA(self.train, order=(1,1,1))
        model = model.fit()

        #modelin içeriğne ait özet bilgisi
        model.summary()

        prediction        = model.get_forecast(len(self.test.index))
        results           = prediction.conf_int(alpha=0.05)
        results["Tahmin"] = model.predict(start=results.index[0], end=results.index[-1])
        results.index     = self.test.index
        plt.plot(results["Tahmin"], color='green', label='Tahminler')
        plt.legend()
        plt.show()
