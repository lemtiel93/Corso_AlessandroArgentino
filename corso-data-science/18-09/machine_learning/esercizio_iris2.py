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
    def __init__(self):
            iris = load_iris()
            self.X = iris.data  
            self.y = iris.target 
            self.model = DecisionTreeClassifier()
            self.scaler = StandardScaler()

    def split_dataset(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

    def scala_dati(self):
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)

    def create_model(self):
        self.model.fit(self.X_train, self.y_train)
    
    def evaluate_model(self):
        self.y_pred = model.predict(X_test)
        accuracy = accuracy_score(self.y_test, self.y_pred)
        report = classification_report(self.y_test, self.y_pred, target_names=self.iris.target_names)
        print(f"Accuratezza del modello: {accuracy:.2f}")
        print("Classification Report:\n", report)
    
    def matrice_confusione(self):
        self.cm = confusion_matrix(y_test, y_pred)

        sns.heatmap(self.cm, annot=True, fmt='d', cmap='Blues', xticklabels=self.iris.target_names, yticklabels=self.iris.target_names)
        plt.show()
    

    
   

