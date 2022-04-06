from flask import Flask, render_template, request
import sqlite3

data = sqlite3.connect("studentdata.db",check_same_thread=False)
table = data.execute("select name from sqlite_master where type='table' and name= 'student' ").fetchall()
if table!=[]:
    print("Table already exists")

else:
    data.execute('''create table student(
                                    id integer primary key autoincrement,
                                    Name text,
                                    branch text,
                                    rollno integer,
                                    admno integer,
                                    DOB text,
                                    pass text,
                                    Semester text
                                ); ''')
    print("Table created")

student = Flask(__name__)

@student.route('/')
def Login():
    return render_template("login.html")

@student.route('/register',methods=['GET','POST'])
def Register_new():
    if request.method == "POST":
        getName = request.form["name"]
        getBranch = request.form["branch"]
        getRollno = request.form["rollno"]
        getAdmno = request.form["admno"]
        getDob = request.form["dob"]
        getPass = request.form["pass"]
        getConpass = request.form["cpass"]
        getSemester = request.form["sem"]
        print(getName)
        print(getBranch)
        print(getRollno)
        print(getAdmno)
        print(getDob)
        print(getPass)
        print(getConpass)
        print(getSemester)
        try:
            query = "insert into student(Name,branch,rollno,admno,DOB,pass,Semester) \
            values('"+getName+"','"+getBranch+"',"+getRollno+","+getAdmno+",'"+getDob+"','"+getPass+"','"+getSemester+"')"
            print(query)
            data.execute(query)
            data.commit()
            data.close()
            print("Data added successfully")
        except Exception as err:
            print("Error occured",err)

    return render_template("register.html")

@student.route('/search')
def Search_student():
    return render_template("search.html")

@student.route('/delete')
def Delete_student():
    return render_template("delete.html")

if __name__=="__main__":
    student.run()

