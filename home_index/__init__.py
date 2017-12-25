"""
由于Django内部连接MySQL时使用的是MySQLdb模块，而python3中还无此模块，所以需要使用pymysql来代替
"""

import pymysql
pymysql.install_as_MySQLdb()