import sqlite3 as st
conn=st.connect("Database_Banking_system.db")
conn.execute("""
insert into Balance(Card_ID,balance)VALUES
             (1234,500000)
""")
conn.commit()
conn.close()
