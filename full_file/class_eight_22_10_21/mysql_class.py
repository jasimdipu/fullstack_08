import mysql.connector as conn


class MySQLdb:

    def connect_mysql(self, host="localhost", user='root', password='', database=''):
        try:
            if database != '':
                mydb = conn.connect(
                    host=host,  # 127.0.0.1
                    user=user,
                    password=password,
                    database=database
                )
            else:
                mydb = conn.connect(
                    host=host,  # 127.0.0.1
                    user=user,
                    password=password,
                )
            print(mydb)
            return mydb
        except Exception as e:
            print(e)

    def create_database(self, dbname):
        try:
            connection = self.connect_mysql()
            cursor = connection.cursor()
            sql = "CREATE DATABASE " + dbname
            cursor.execute(sql)
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def create_table(self, table_name):
        try:
            connection = self.connect_mysql(database='university')
            cursor = connection.cursor()
            sql = "CREATE TABLE " + table_name + " (id integer, name varchar(255), dept varchar(255))"
            cursor.execute(sql)
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def insert_data(self, table_name):
        try:
            connection = self.connect_mysql(database='university')
            cursor = connection.cursor()
            sql = "INSERT INTO " + table_name + "(id, name, dept) VALUES(1, 'Shumon', 'CSE')"
            sql2 = "INSERT INTO " + table_name + "(id, name, dept) VALUES(2,'Alim', 'BBA')"
            sql3 = "INSERT INTO " + table_name + "(id, name, dept) VALUES(3, 'Tarek', 'MBA')"
            # val = (id, name, dept)
            for i in [sql, sql2, sql3]:
                cursor.execute(i)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def show_data(self, table_name):
        try:
            connection = self.connect_mysql(database='university')
            cursor = connection.cursor()
            sql = "SELECT * FROM " + table_name
            cursor.execute(sql)
            resutl = cursor.fetchall()
            for i in resutl:
                print(i)
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)


mysql_handl = MySQLdb()
mysql_handl.create_database('university')
mysql_handl.create_table('student')
mysql_handl.insert_data('student')
mysql_handl.show_data('student')
