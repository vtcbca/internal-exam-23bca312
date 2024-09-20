import sqlite3 as sq
con=sq.connect("D:/23BCA312/sqlite-tools-win-x64-3460000/python_internal_7.db")
cur=con.cursor()

#creating table contact
cur.execute("""create table if not exists contact(fname,lname,contact int primary key,email,city) """)

#inserting records
cur.execute("""insert into contact values("neha","shrivastav",9755653435,"nehashriv@gmail.com","valod"),
                ("kavita","poddar",9876543456,"kavita@gmail.com","vyara"),
                ("varsha","singh",8976553345,"varsha@gmail.com","bardoli"),
                ("priya","singh",8123456788,"priya@gmail.com","surat"),
                ("rani","gupta",9354236747,"rani@gmail.com","surat"),
                ("puja","teli",8746574564,"pooja@gmail.com","vyara"),
                ("trisha","yadav",9754466456,"@gmail.com","surat")""")

#creating log table for newely inserted records
cur.execute("""create table if not exists contact_log( operation_name ,
    operation_datetime TIMESTAMP,
    new_fname,
    new_lname ,
    new_contact) """)
# creating trigger after insert on contact
cur.execute(""" create trigger if not exists insert_log 
                after insert on contact
                 for each row
                 BEGIN
                 insert into contact_log 
                 values('INSERT',datetime('now'), new.fname, new.lname, new.contact);
                 end;""")
# inserting new record in contact to check whether the trigger is created properly or not
cur.execute("""insert into contact values("shreya","poddar",2276543456,"kavita@gmail.com","vyara") """)
cur.execute("select * from contact_log")
record=cur.fetchall()
print(record)

# creating new log table for deleted records
cur.execute("""create table if not exists contact2_log( operation_name ,
    operation_datetime TIMESTAMP,
    old_fname,
    old_lname ,
    old_contact) """)
# creating trigger after delete on contact
cur.execute(""" create trigger if not exists delete_log 
                after delete on contact
                 for each row
                 BEGIN
                  insert into contact_log 
                 values('DELETE', datetime('now'), old.fname, old.lname, old.contact);
                 end;""")
# deleting record from contact to check whether the trigger is created properly or not
cur.execute("delete from contact where fname='neha'")
cur.execute("select * from contact2_log")
record=cur.fetchall()
print(record)

cur.execute("select * from contact")
record=cur.fetchall()
print(record)
con.commit()