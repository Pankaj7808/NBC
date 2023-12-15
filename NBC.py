import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import * #classification_report
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

df = pd.read_csv('disease.csv')
#df.head()

le = LabelEncoder()
df['Sore Throat'] = le.fit_transform(df['Sore Throat'])
df['Fever'] = le.fit_transform(df['Fever'])
df['Swollen Glands'] = le.fit_transform(df['Swollen Glands'])
df['Congestion'] = le.fit_transform(df['Congestion'])
df['Headache'] = le.fit_transform(df['Headache'])
df['Diagnosis'] = le.fit_transform(df['Diagnosis'])

x = df.drop('Diagnosis', axis = 1)
y = df['Diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

classifier = MultinomialNB()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

print('Confusion Matrix : ')
print(confusion_matrix(y_test, y_pred))

print('Classification Report :')
print(classification_report(y_test, y_pred))
