import csv
f1=open("C:\\Users\\91976\\Desktop\\523eds\\stud_info.csv","r")
info_dataset=[]
while True:
 data=f1.readline()
 if data:
 info_dataset.append(data.replace("\n",",").split(","))
 else:
 break;
print(info_dataset)
f2=open("C:\\Users\\91976\\Desktop\\523eds\\stud_placement.csv","r")
f3=open("C:\\Users\\91976\\Desktop\\523eds\\student_marks.csv","r")
RollNo=[]
name=[]
Gender=[]
DOB=[]
for row in info_dataset[1:]:
 RollNo.append(row[0])
 name.append(row[1])
 Gender.append(row[2])
 DOB.append(row[3])
print(RollNo)
print(name)
print(Gender)
print(DOB)
f2=open("C:\\Users\\91976\\Desktop\\523eds\\stud_placement.csv","r")
placement_dataset=[]
while True:
 data=f2.readline()
 if data:
 placement_dataset.append(data.replace("\n",",").split(","))
 else:
 break;
print(placement_dataset)
RollNo=[]
Company=[]
JobRole=[]
Package=[]
for row in placement_dataset[1:]:
 RollNo.append(row[0])
 Company.append(row[1])
 JobRole.append(row[2])
 Package.append(row[3])
print(RollNo)
print(Company)
print(JobRole)
print(Package)
f3=open("C:\\Users\\91976\\Desktop\\523eds\\student_marks.csv","r")
marks_dataset=[]
while True:
 data=f3.readline()
 if data:
 marks_dataset.append(data.replace("\n",",").split(","))
 else:
 break;
print(marks_dataset)
Roll=[]
Maths=[]
Physics=[]
Chemistry=[]
Total=[]
Percentage=[]
for row in marks_dataset[1:]:
 Roll.append(row[0])
 Maths.append(row[1])
 Physics.append(row[2])
 Chemistry.append(row[3])
 Total.append(row[4])
 Percentage.append(row[5])
print(Roll)
print(Maths)
print(Physics)
print(Chemistry)
print(Total)
print(Percentage)
student_data=[]
for i in range(len(marks_dataset)):
 student_data.append(info_dataset[i]+placement_dataset[i]
+marks_dataset[i])
print(student_data)
studentdata=[]
studentdata.append(RollNo)
studentdata.append(name)
studentdata.append(Gender)
studentdata.append(DOB)
studentdata.append(RollNo)
studentdata.append(Company)
studentdata.append(JobRole)
studentdata.append(Package)
studentdata.append(Roll)
studentdata.append(Maths)
studentdata.append(Physics)
studentdata.append(Chemistry)
studentdata.append(Total)
studentdata.append(Percentage)
print(studentdata)
# stastical Operations
print("Math Marks=",Maths)
print("Physics marks=",Physics)
print("Chemistry marks=",Chemistry)
Math=[int(i) for i in Maths]
Physics=[int(i) for i in Physics]
Chemistry=[int(i) for i in Chemistry]
sum_of_marks=[]
average=[]
for i in range(len(Math)):
 sum_of_marks.append(Math[i]+Physics[i]+Chemistry[i])
 average.append(round(sum_of_marks[i],2))

print("Sum of marks=",sum_of_marks)
print("Average of marks=",average)
print("maximum marks=",max(sum_of_marks))
print("minimum marks=",min(sum_of_marks))
print("total no of students=",len(studentdata[0]))
print("total no company=",len(studentdata[5]))
print("jobrole=",len(studentdata[6]))
per=[]
for i in range(len(sum_of_marks)):
 per.append(round((100*sum_of_marks[i]/270),2))
print("Percentage=",per)
