### 1.执行顺序
1.get_data_preprocess/single_thread_spider.py
2.write_to_mysql.py
3.analysis_data/*(不分前后)

### 2.注意事项

- 执行过程中需要修改根目录下的[variable.py](./variable.py)文件夹中的数据库信息
- 当然header中的信息也可能过期需要重新输入
- 尽量用pycharm打开整个项目,直接运行是不可以的,因为有些文件是引用了其他文件夹下面的python文件.

