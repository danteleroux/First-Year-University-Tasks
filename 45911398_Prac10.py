# 45911398
# Importing sqlite3
import sqlite3

def main():
    # Connect to the studentdatabase
    conn = sqlite3.connect("CMPG111.db")
    # Create Cursor
    cur = conn.cursor()
    # DROP statement for if table already exists
    drop_table = '''DROP TABLE IF EXISTS CMPG111'''
    # Create statement, to create table if it does not exist
    create_table_sql = ''' CREATE TABLE IF NOT EXISTS CMPG111 ( StudentNumber INTEGER PRIMARY KEY,
                       StudentName TEXT,
                       ParticipationMark REAL)'''
    # Inserting the data into the database
    insert_data_sql = '''INSERT INTO CMPG111(StudentNumber, StudentName, ParticipationMark)VALUES
                        (31592834, "John Doe", 76),
                        (42748191, "Jane Austen", 38),
                        (32774344, "Alex Carter", 85),
                        (33693821, "Avery Jordan", 92),
                        (45829162, "John Smith", 28)'''

    # Select students above 74%
    select_above_74 = '''SELECT StudentNumber, StudentName FROM CMPG111 WHERE ParticipationMark> 74'''

    # Execute statements
    cur.execute(drop_table)
    cur.execute(create_table_sql)
    cur.execute(insert_data_sql)
    cur.execute(select_above_74)

    # Print values, using fetchall()
    rows = cur.fetchall()
    
    for row in rows:
        print(f"{row[0]:8} {row[1]:50}")

    # Commit everything
    conn.commit()

    # Close Connections
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
