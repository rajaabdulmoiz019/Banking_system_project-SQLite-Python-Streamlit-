import sqlite3 as st
conn=st.connect("Database_Banking_system.db")
conn.execute("""create table if not exists Balance(
             Card_ID INT,
             balance INT
             )""")
conn.commit()
conn.close()