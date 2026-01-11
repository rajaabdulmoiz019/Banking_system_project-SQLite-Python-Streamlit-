import sqlite3 as st
conn=st.connect("Database_Banking_system.db")
conn.execute("""create table if not exists Customer_data(
             Card_ID INT,
             "Name" VARCHAR(50),
             "Date" VARCHAR(50)
             )""")
conn.commit()
conn.close()