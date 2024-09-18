from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , classification_report
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

class ModelloTree:
    def __init__(self,funct):
            self.iris = funct
            self.X = self.iris.data  
            self.y = self.iris.target 
            self.model = DecisionTreeClassifier()
            self.scaler = StandardScaler()

    def split_dataset(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)
        print("Forma dataset train",self.X_train.shape, "Forma dataset test", self.X_test.shape)
        
        
    def scala_dati(self):
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print("Valori non scalati",self.X_train[0])
        print("Valori scalati ",self.X_train_scaled[0])
        
        plt.plot(self.X_train[0],label="Non scalati")
        plt.plot(self.X_train_scaled[0],label = 'Scalati')
        plt.legend()
        plt.show()
        
    def create_evaluate_model(self):
        self.model.fit(self.X_train, self.y_train)
        self.y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, self.y_pred)
        report = classification_report(self.y_test, self.y_pred, target_names=self.iris.target_names)
        print(f"Accuratezza del modello: {accuracy:.2f}")
        print("Classification Report:\n", report)
    
    def matrice_confusione(self):
        
        print("\nInterpretazione:")
        print("La matrice di confusione mostra il numero di predizioni corrette e errate per ciascuna classe.")
        print("Righe = Classi Vere, Colonne = Classi Predette.")
        print("Esempio di matrice (3 classi):")
        print("              Predetto")
        print("            |  0   |  1   |  2   |")
        print("          -----------------------")
        print("       0  |  TP0  |  FP01 |  FP02 |  <- Classe vera 0")
        print("       1  |  FN10 |  TP1  |  FP12 |  <- Classe vera 1")
        print("       2  |  FN20 |  FN21 |  TP2  |  <- Classe vera 2")
        print("TP = True Positives, FP = False Positives, FN = False Negatives.")
        self.cm = confusion_matrix(self.y_test, self.y_pred)

        sns.heatmap(self.cm, annot=True, fmt='d', cmap='Blues', xticklabels=self.iris.target_names, yticklabels=self.iris.target_names)
        plt.show()
