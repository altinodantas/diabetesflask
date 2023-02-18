import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import joblib

dados = pd.read_csv("../data/diabetes.csv")

feature_cols = ['pregnant', 'glucose','bp', 'skin',  'insulin', 'bmi', 'pedigree', 'age']
X = dados[feature_cols]
y = dados.label

#scaler = StandardScaler()
#X=scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=1)

clf = SVC(probability=True)
clf = clf.fit(X_train, y_train)

filename = 'modelo_salvo.sav'
joblib.dump(clf, filename)
