from sklearn.preprocessing   import LabelEncoder
from sklearn.preprocessing   import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models  import Sequential
from tensorflow.keras.layers  import Dense
import matplotlib.pyplot     as plt
import  pandas               as pd
import  numpy                as np

class ANN:
    dataFrame    = None
    resultColumn = None
    yLabel       = None
    inputSize    = 0

    def __init__(self, dataColumn, columnName, resultColumn, yLabel):
        self.dataFrame    = pd.DataFrame(dataColumn, columns=[columnName])
        self.resultColumn = resultColumn
        self.yLabel       = yLabel
        self.inputSize    = 1

    def addColumn(self, newColumn, newColumnName):
        self.dataFrame[newColumnName] = newColumn
        self.inputSize                = self.inputSize + 1

    def removeColumn(self, columnName):
        self.dataFrame.drop(columnName, axis=1)
        self.inputSize = self.inputSize - 1


    def predict(self):
        #sonuç koloonunun kategorize edilmesi
        labelEncoder = LabelEncoder().fit(self.resultColumn)
        labels       = labelEncoder.transform(self.resultColumn)
        classes      = list(labelEncoder.classes_)

        #eğitim verilerinin optimize edilerek dönüştürülmesi
        standardScaler                   = StandardScaler()
        X                                = standardScaler.fit_transform(self.dataFrame.to_numpy())
        X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)

        #modelin oluşturulması
        model = Sequential()
        model.add(Dense(16, input_dim=self.inputSize, activation="relu"))
        model.add(Dense(16, activation="relu"))
        model.add(Dense(1, activation="softmax"))
        model.summary()

        #modelin derlenmesi ve veri ile eğitilmesi
        model.compile(loss="categorical_crossentropy", metrics=["accuracy"])
        y_train = np.reshape(y_train, (len(y_train), 1))
        y_test  = np.reshape(y_test , (len(y_test), 1))
        model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=300, batch_size=10)

        plt.plot(model.history.history["accuracy"])
        plt.plot(model.history.history["val_accuracy"])
        plt.title("Model Başarımları")
        plt.ylabel("Başarım")
        plt.xlabel("Epok Sayısı")
        plt.legend(["Epok sayısı"], loc="upper left")
        plt.show()

        plt.plot(model.history.history["loss"])
        plt.plot(model.history.history["val_loss"])
        plt.title("Model Kayıpları")
        plt.ylabel("Kayıp")
        plt.xlabel("Epok sayısı")
        plt.legend(["Eğitim","Test"], loc="upper left")
        plt.show()
