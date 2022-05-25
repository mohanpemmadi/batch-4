'''
SQL Server
Oracle
PostgreSQL
MySQL

-----


sql

'''

"""

python <-psycopg2->  database(postgresql)
python <-mysqldb->  database(mysql)


"""

'''

install progresql server:

	https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
	
guide :

	https://www.guru99.com/download-install-postgresql.html

	
install psycopg2:

	pip install psycopg2

postgresql tutorial:

	https://www.w3schools.blog/postgresql-tutorial
		
'''

import psycopg2

conn = psycopg2.connect(host='127.0.0.1',user='postgres',password='root',database='pythondb', port=5432)

cur = conn.cursor()

''' Table creation '''
# cur.execute("create table employee(name varchar(100),age int, city varchar(100), salary int)")
# conn.commit()
# print('table created')

''' insert '''
# insert_query = "insert into employee values('krishana',33,'vijayawada',13000)"
# cur.execute(insert_query)
# conn.commit()
# print('inserted')

''' select '''

# cur.execute('select * from employee')
# data = cur.fetchall()
# data = cur.fetchone()
# print(data)
# for row in data:
#     print(row)

# cur.execute("select * from employee where city='vijayawada'")
# result = cur.fetchall()
# print(result)


''' update '''

# cur.execute("update employee set age=35 where name='phani'")
# conn.commit()
# print('updated')

''' delete '''

cur.execute("delete from employee where city='guntur'")
conn.commit()
print('deleted')

