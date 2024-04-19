import pandas as pd
from tube.model import DTreeForIMA
from sklearn.model_selection import train_test_split

test_ex = DTreeForIMA('learn_model_dtree')

df = pd.read_csv('vostok_tube.csv', sep=';')
cols = df.columns
cols = list(cols)
cols.remove('L')
for col in cols:
    df[col] = df[col].apply(lambda x: float(x.split()[0].replace(',','.')))
df = df.astype(float)
X = df.drop(['BHP', 'D', 'L', 'R', 'dH'], axis=1)
y = df.BHP
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

predict_values = test_ex.predict(X_test)
print(predict_values)