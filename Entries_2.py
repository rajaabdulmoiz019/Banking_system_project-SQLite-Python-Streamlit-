import sqlite3 as st
conn=st.connect("Database_Banking_system.db")
conn.execute("""
INSERT into Customer_data(Card_ID,Name,Date)VALUES
             (1234,"Abdul moiz","3 July 2026")
""")
conn.commit()
conn.close()
