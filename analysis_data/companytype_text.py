import matplotlib.pyplot as plt
from varible import cur, list_x, list_y, matplot_chinese, COMPANYTYPE_TEXT

cur.execute(query=COMPANYTYPE_TEXT)
companytype = cur.fetchall()

for i in companytype:
    list_x.append(i[0])
    list_y.append(i[1])

list_x[5] = "其他"
list_y[5] = sum(list_y[5:])
matplot_chinese()
plt.pie(x=list_y[:6], labels=list_x[:6])
plt.legend(loc="lower left", bbox_to_anchor=(-0.3, 0.9))
plt.show()
