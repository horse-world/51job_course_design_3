import time
from varible import CREATE_TABLE_51JOB, CLEAR_TABLE, format_insert, cur, SAVEFILE_PATH

start_time = time.localtime()
file = open(SAVEFILE_PATH + "51job_data.csv", mode="r", encoding="utf-8")
cur.execute(query=CREATE_TABLE_51JOB)
cur.execute(query=CLEAR_TABLE)
for item in file.readlines():
    i = item.split("\t")
    insert_values = format_insert(i=i)
    cur.execute(query="insert into 51job_table values {}".format(insert_values))
    cur.connection.commit()
print(cur.fetchall())
print(start_time, "\n", time.localtime())
