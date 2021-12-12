from varible import cur, list_x, list_y, matplot_chinese, HEAD_TOP_COMPANY
import matplotlib.pyplot as plt

cur.execute(query=HEAD_TOP_COMPANY)
company_count = cur.fetchall()
for i in company_count:
    list_x.append(i[0])
    list_y.append(i[1])

matplot_chinese()
colors = ['gray', 'pink', 'purple', 'red', 'green', 'blue', 'yellow', 'orange']
plt.barh(y=list_x, width=list_y, color=colors)
plt.legend(loc="lower left", bbox_to_anchor=(-0.3, 0.9))
plt.grid()
plt.show()
