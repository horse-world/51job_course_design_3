import pymysql
import matplotlib.pyplot as plt

HOST = "localhost"
USER = "root"
PASSWORD = "123456"
DATABASE = "51job"
PORT = 3306,
CHARSET = "utf8"
SAVEFILE_PATH = "../data/"
list_x = []
list_y = []

cur = pymysql.Connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE, port=3306,
                      charset=CHARSET).cursor()


def matplot_chinese():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False


HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "guid=4062bb2a161e1a5164dc5c36edcbf762; slife=lowbrowser%3Dnot%26%7C%26; "
              "adv=adsnew%3D0%26%7C%26adsnum%3D2004282%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F"
              "%252Fwww.baidu.com%252Fother.php%253Fsc.000000KjabwzhFuJe6WiJFtEr4VnTNNmokhFAKvAV4yNFKdxMLd"
              "-5Ss3O7ZiGJ9Y-lBL06"
              "-Wm3hxJ88AancByBOPZdj3pqv8FNSr_2VenITm54XRQMKRxNkO3zNI9G_YOj6mh8Crz5ZVnz3ApEWNKHD6BDOLOm4Es7Do5Kq9NG53FnIsdLzD4TOXU3hEnwg16Em_gPzfNS4_U9_GNY3WsAkaNgF3.DR_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_uQQr1F_zIyT8P9MqOOgujSOODlxdlPqKMWSxKSgqjlSzOFqtZOmzUlZlS5S8QqxZtVAOtIOtHOuS81wODSgL35SKsSXKMqOOgfESyOHjGLY51xVOeNH5exS88Zqq1ZgVm9udSnQr1__oodvgvnehUrPL72xZgjX1IIYJN9h9merzEuY60.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqPH7JUvc0IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqPH7JUvc0ThPv5HD0IgF_gv-b5HDdnWc1rjb3njf0UgNxpyfqnHn3PjfdP1D0UNqGujYknjT4nWcdnsKVIZK_gv-b5HDkPHnY0ZKvgv-b5H00pywW5R9rffKWThnqPjndPjD%2526ck%253D3804.1.101.347.217.357.212.270%2526dt%253D1608977107%2526wd%253D51job%2526tpl%253Dtpl_11534_23295_19442%2526l%253D1522389804%2526us%253DlinkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E3%25252580%25252590%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A751Job%252525E3%25252580%25252591-%25252520%252525E5%252525A5%252525BD%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%2521%252526linkType%25253D%26%7C%26; partner=www_baidu_com; 51job=cenglish%3D0%26%7C%26; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA26%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA26%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B7%BF%B2%FA%BE%AD%BC%CD%C8%CB%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60151100%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA26%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B7%BF%B2%FA%BE%AD%BC%CD%C8%CB%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%600%7C%21",
    "Host": "search.51job.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 "
                  "Safari/537.36 "
}


def format_url(page):
    URL_STYLE = "https://search.51job.com/list/000000,000000,0000,26,9,99,+,2,{}.html".format(page)
    return URL_STYLE


def format_write(i):
    format_string = "" \
                    "{job_name}\t{company_name}\t{providesalary_text}\t{workarea_text}\t" \
                    "{updatedate}\t{companytype_text}\t{degreefrom}\t{workyear}\t" \
                    "{issuedate}\t{jobwelf}\t{attribute_text}\t" \
                    "{companysize_text}\t{companyind_text}{newline}" \
        .format(
        job_name=i["job_name"], company_name=i["company_name"],
        providesalary_text=i["providesalary_text"],
        workarea_text=i["workarea_text"], updatedate=i["updatedate"],
        companytype_text=i["companytype_text"],
        degreefrom=i["degreefrom"], workyear=i["workyear"],
        issuedate=i["issuedate"], jobwelf=i["jobwelf"],
        attribute_text=" ".join(i["attribute_text"]),
        companysize_text=i["companysize_text"],
        companyind_text=i["companyind_text"],
        newline="\n")
    return format_string


CREATE_TABLE_51JOB = """
            create table if not exists 51job_table(
                  job_name varchar(100), company_name varchar(100), 
                  providesalary_text varchar(100), workarea_text varchar(100), 
                  updatedate varchar(100), companytype_text varchar(100), 
                  degreefrom varchar(50), workyear varchar(50), 
                  issuedate varchar(50), jobwelf varchar(100), 
                  attribute_text varchar(100), companysize_text varchar(50), 
                  companyind_text varchar(50)
                  )
"""

CLEAR_TABLE = """
truncate table 51job_table
"""

COMPANYTYPE_TEXT = """
            select substring_index(companytype_text, '-', 1) companytype, count(*) companytype_count
            from 51job_table a
            group by companytype
            order by companytype_count desc
"""

HEAD_TOP_COMPANY = """
        select distinct company_name, count(company_name) company_count 
            from 51job_table 
            group by company_name 
            order by company_count desc 
            limit 10;
"""

JOBWELF_COUNT = """
            select count(*) from 51job_table where jobwelf != ''
"""

WORKAREA_SORT = """
        select substring_index(workarea_text, '-', 1) workarea_province, count(*) workarea_count
            from 51job_table a
            group by workarea_province
            order by workarea_count desc
            limit 20;
"""


def format_insert(i):
    INSERT_VALUES = "" \
                    "('{job_name}', '{company_name}', '{providesalary_text}', '{workarea_text}', " \
                    "'{updatedate}', '{companytype_text}', '{degreefrom}', '{workyear}', " \
                    "'{issuedate}', '{jobwelf}', '{attribute_text}', " \
                    "'{companysize_text}', '{companyind_text}') " \
                    "".format(
        job_name=i[0].strip("\\"), company_name=i[1],
        providesalary_text=i[2],
        workarea_text=i[3], updatedate=i[4],
        companytype_text=i[5],
        degreefrom=i[6], workyear=i[7],
        issuedate=i[8], jobwelf=i[9],
        attribute_text=" ".join(i[10]),
        companysize_text=i[11],
        companyind_text=i[12].strip()
    )
    return INSERT_VALUES


DEGREEFROM_WORKYEAR_COMPANYSIZE_TEXT = """
select degreefrom, workyear, companysize_text
from 51job_table
where degreefrom !="" and workyear != "" and companysize_text != "" and companytype_text != "";
"""

ANALYSIS_COMPANYTYPE_TEXT = """
select companytype_text
from 51job_table
where degreefrom !="" and workyear != "" and companysize_text != "" and companytype_text != "";
"""

