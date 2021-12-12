import matplotlib.pyplot as plt
from varible import cur, list_x, list_y, matplot_chinese, WORKAREA_SORT

cur.execute(query=WORKAREA_SORT)
workarea_big = cur.fetchall()
for i in workarea_big:
    list_x.append(i[0])
    list_y.append(i[1])
matplot_chinese()
plt.barh(y=list_x, width=list_y)
plt.legend()
plt.show()
