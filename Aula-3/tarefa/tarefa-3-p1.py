import pandas as pd
database = pd.read_csv('credit-data.csv')
database

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')

database[['age', 'income', 'loan']] = imputer.fit_transform(database[['age', 'income', 'loan']])

imputer = SimpleImputer(missing_values=-1, strategy='mean')

database['age'] = imputer.fit_transform(database[['age']])

database

from sklearn.model_selection import train_test_split

x_base = database.iloc[:, 1:4].values
y_base = database.iloc[:, 4].values

x_base
y_base

x_treino, x_teste, y_treino, y_teste = train_test_split(x_base, y_base, test_size=0.1, random_state=0)

from sklearn.naive_bayes import GaussianNB

naive_risco = GaussianNB()
naive_risco.fit(x_treino, y_treino)

from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import metrics
import matplotlib.pyplot as plt

predict = naive_risco.predict(x_teste)

matrix = confusion_matrix(y_teste, predict)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = matrix, display_labels = [0, 1])

cm_display.plot()
plt.show()


accuracy_score(y_teste, predict)

