#psycopg2- library used to connect to the DB i.e., postgresql
import psycopg2

#connect to the db
con = psycopg2.connect(
    host = "localhost",
    database = "university_students",
    user = "postgres",
    password = "Postgres123"
)

#cursors- vessels to communicate with the DB; read-only pointer that allows a program to access the result set of a query
cur = con.cursor()

#CRUD:CREATE A ENTRY INTO THE TABLE
cur.execute("insert into undergrads (std_id, std_name, std_course, std_stream) values (%s, %s, %s, %s)", (6, "Mary", "B.Pharma", "English"))

#CRUD: UPDATE EXISTING ENTRY
cur.execute("Update undergrads set std_course= %s where std_id= %s", ("B.C.A Hons", "2"))

#execute the query; CRUD:READ FROM THE TABLE
cur.execute("select * from undergrads")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} name {r[1]} pursuing {r[2]} in {r[3]}")

#CRUD: DELETE FROM THE TABLE
cur.execute("Delete from undergrads where std_id = %s", ("4"))

#commit the changes to the DB
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()