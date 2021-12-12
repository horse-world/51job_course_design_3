from wordcloud import WordCloud
import matplotlib.pyplot as plt
from varible import cur, matplot_chinese, JOBWELF_COUNT
# 画饼图
cur.execute(query=JOBWELF_COUNT)
has_jobwelf = cur.fetchall()
matplot_chinese()
plt.pie(x=[has_jobwelf[0][0], 100000 - has_jobwelf[0][0]], labels=["有福利", "无福利"], colors=["blue", "red"])
plt.show()

# 画词云
cur.execute("select jobwelf from 51job_table")
all_jobwelf = cur.fetchall()
text_all = ""
for i in all_jobwelf:
    text_all = text_all + i[0]

wc = WordCloud(background_color='white', font_path="../word_type/simhei.ttf")
wc.generate(text_all)
wc.to_file("../data/1.png")
