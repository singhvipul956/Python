from tkinter import *
import pyodbc


def insertData():
    '''conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                          'Server=IN142P-GSS-062;'
                          'Database=PyTest;'
                          #'uid=sa;pwd=Password@1;'
                          'Trusted_Connection=yes;')'''

    conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};SERVER=IN142P-GSS-062; database=PyTest;uid=sa;pwd=Password@1;")
                            

    cursor = conn.cursor()
    cursor.execute("insert into Pytesttbl values('%s','%s','%s','%s')"%(fname.get(), lname.get(),Position.get(),Salary.get()))
    cursor.close()
    conn.commit()
    conn.close()
    status.set('Data saved successfully')
    fetchdata()


def fetchdata():
    conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};SERVER=IN142P-GSS-062; database=PyTest;uid=sa;pwd=Password@1;")

    cursor = conn.cursor()
    cursor.execute("select * from Pytesttbl")
    rows = cursor.fetchall()
    for row in rows:
        Label(text=row[1], values=row[2])

    cursor.close()
    conn.commit()
    conn.close()


root = Tk()

fname = StringVar()
lname = StringVar()
Position = StringVar()
Salary = StringVar()
status = StringVar()

Label(root, text='First Name: ').grid(row=0, column=0)
Label(root, text='Last Name: ').grid(row=1, column=0)
Label(root, text='Position: ').grid(row=2, column=0)
Label(root, text='Salary: ').grid(row=3, column=0)
Label(root, text='', textvariable=status).grid(row=5, columnspan=2)

Entry(root, textvariable=fname).grid(row=0, column=1)
Entry(root, textvariable=lname).grid(row=1, column=1)
Entry(root, textvariable=Position).grid(row=2, column=1)
Entry(root, textvariable=Salary).grid(row=3, column=1)

Button(root, text='Submit', command=insertData).grid(row=4, columnspan=2)


root.mainloop()
