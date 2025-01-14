import sqlite3
def create_db():
    con=sqlite3.connect(database="rms_db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text,description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS student(rollno INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,addmision text,course text,state text,city text,pin text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,rollno text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()

    con.close()


create_db()