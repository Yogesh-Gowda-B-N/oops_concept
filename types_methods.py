########### 1 object method ########
""" WAP to create a class for company and write two object methods for it """
# class Company:
#     Cname = 'ABC'
#     Loc = 'bangalore'
#     CEO = 'XYZ'
#
#     def __init__(self, ename, eid, email, esal, phno, desig):
#         self.ename = ename
#         self.eid = eid
#         self.email = email
#         self.esal = esal
#         self.phno = phno
#         self.desig = desig
#
#     def disp(self):
#         print(self.ename, self.eid, self.email, self.esal, self.phno, self.desig)
#
#     def ch_phno(self, new):
#         self.phno = new
#
#     def ch_desig(self,new):
#         self.desig = new
#
#     def ch_email(self,new):
#         self.email = new
#
# e1 = Company('abc', 'ty01', 'abc@xyz.com', 12000, 9123456780, 'se')
# e2 = Company('xyz', 'ty02', 'xyz@abc.com', 15000, 8912345670, 'ae')
# Company.disp(e1)
# Company.disp(e2)
#
# e2.disp()
# e1.ch_email("pqr@lmn.com")
# e1.disp()

#Program 2
# WAP to create a class for student and write four object methods for it.
class Student:
    Sschool = 'ABC'
    Ssloc = 'bengaluru'
    Sprinc = 'xyz'

    def __init__(self, sname, sid, sphno, dob):
        self.sname = sname
        self.sid = sid
        self.sphno = sphno
        self. dob = dob

    def disp(self):
        print(self.sname, self.sid, self.sphno, self.dob)

s1 = Student('lmn', 'S01', 7890123456, "11.01.1901")
s2 = Student('pqr', 's02', 6789012345, "11.02.1901")
s3 = Student('abc', 's03', 5678901234, '11.03.1901')
s4 = Student('xyz', 's04', 4567890123, "11.04.1901")

s3.disp()
s4.disp()
Student.disp(s1)
Student.disp(s2)


























