import sqlite3 as sq
con=sq.connect("C:/sqlite3/sqlite3/python_int1.db")
cur=con.cursor()
#creating contact table
cur.execute("""create table if not exists contact_s(fname,lname,contacts,email,city) """)
#creating log table
cur.execute("""create table if not exists contacts_log( operation_name ,
    operation_datetime default(datetime('now')),
    old_fname ,
    old_lname ,
    old_contacts,
    new_fname,
    new_lname ,
    new_contacts) """)

cur.execute(""" create trigger if not exists insert_log 
                after insert on contact_s
                 for each row
                 BEGIN
                 insert into contacts_log (operation_name, operation_datetime, new_fname, new_lname, new_contact)
                 values('INSERT',datetime('now'), new.fname, new.lname, new.contact);
                 end;""")

cur.execute(""" create trigger if not exists delete_log
                after delete on contact_s
                for each row
                BEGIN
                 insert into contacts_log (operation_name, operation_datetime, old_fname, old_lname, old_contact)
                 values('DELETE',datetime('now'), old.fname, old.lname, old.contact);
                 end;""")

cur.execute("""insert into contact_s values('neha','shrivastav',8755673430,'nehashriv@gmail.com','valod'),
                 ("kavita","poddar",8876543356,"kavita@gmail.com","vyara"),
                ("varsha","singh",8876555345,"varsha@gmail.com","bardoli"),
                ("priya","singh",9123456088,"priya@gmail.com","surat"),
                ("rani","gupta",9554236847,"rani@gmail.com","surat"),
                ("puja","teli",8646570564,"pooja@gmail.com","vyara"),
                ("trisha","yadav",9674466456,"@gmail.com","surat")""")
con.commit()
#cur.execute(""" select * from contact_s""")
#record=cur.fetchall()
#print(record)
#cur.execute("select * from contacts_log")
#recor=cur.fetchall()
#print(recor)
cur.execute("""insert into contact_s values('priyansi','singh',8975634764,'priya@gmail.com','valod') """)
con.commit()
cur.execute(""" delete from contact_s where city='valod'and fname='neha'""")
cur.execute("select * from contacts_log")
rec=cur.fetchone()
print(rec)
con.commit()