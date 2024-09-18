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

class ModelloIris:
    def __init__(self,funct):
            self.iris = funct
            self.X = self.iris.data  
            self.y = self.iris.target 
            self.model = DecisionTreeClassifier()
            self.scaler = StandardScaler()

    def split_dataset(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)
        
        
    def scala_dati(self):
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print("Valori non scalati",self.X_train[0])
        print("Valori scalati ",self.X_train_scaled[0])

    def create_evaluate_model(self):
        self.model.fit(self.X_train, self.y_train)
        self.y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, self.y_pred)
        report = classification_report(self.y_test, self.y_pred, target_names=self.iris.target_names)
        print(f"Accuratezza del modello: {accuracy:.2f}")
        print("Classification Report:\n", report)
    
    def matrice_confusione(self):
        
        print("La matrice di confusione è uno strumento utilizzato per valutare le prestazioni di un modello di classificazione.")
        print("Essa confronta le etichette vere con le etichette previste dal modello, mostrando:")
        print("- True Positives (TP): Predizioni corrette della classe positiva.")
        print("- True Negatives (TN): Predizioni corrette della classe negativa.")
        print("- False Positives (FP): Predizioni errate della classe positiva.")
        print("- False Negatives (FN): Predizioni errate della classe negativa.")
        print("Dalla matrice, è possibile calcolare metriche come accuratezza, precisione e richiamo.")
        self.cm = confusion_matrix(self.y_test, self.y_pred)

        sns.heatmap(self.cm, annot=True, fmt='d', cmap='Blues', xticklabels=self.iris.target_names, yticklabels=self.iris.target_names)
        plt.show()
