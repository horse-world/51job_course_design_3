from varible import cur, DEGREEFROM_WORKYEAR_COMPANYSIZE_TEXT
from varible import ANALYSIS_COMPANYTYPE_TEXT
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

dict_companysize_text = {
    "少于50人": 1,
    "50-150人": 2,
    "150-500人": 3,
    "500-1000人": 4,
    "1000-5000人": 5,
    "5000-10000人": 6,
    "10000人以上": 7
}

dict_companytype_text = {
    "上市公司": 1,
    "民营公司": 2,
    "外资（非欧美）": 3,
    "合资": 4,
    "国企": 5,
    "创业公司": 6,
    "政府机关": 7,
    "外资（欧美）": 8,
    "外企代表处": 9,
    "非营利组织": 10,
    "事业单位": 11
}

clf = GaussianNB()

cur.execute(DEGREEFROM_WORKYEAR_COMPANYSIZE_TEXT)
x_data = cur.fetchall()
x_line = len(x_data)
X = np.zeros([x_line, 3])
for i in range(x_line):
    X[i][0] = int(x_data[i][0])
    X[i][1] = int(x_data[i][1])
    X[i][2] = dict_companysize_text[x_data[i][2]]
# print(X)
cur.execute(ANALYSIS_COMPANYTYPE_TEXT)
y_data = cur.fetchall()
y_line = len(y_data)
y = np.zeros(y_line)
for i in range(y_line):
    y[i] = dict_companytype_text[y_data[i][0]]

# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf.fit(X_train, y_train)
print(clf.predict(X_test))
print(y_test.T)
print(clf.score(X_test, y_test))
