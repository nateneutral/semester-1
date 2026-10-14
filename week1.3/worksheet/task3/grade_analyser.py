# Worksheet 1.3: Task 3

# Your code for the overall grade classification
#    >= 70 : 1
#    >=60 : 2:1
#    >=50 : 2:2
#    >=40 : 3
#    <40 : F
# ask for filename of the student file
fileName = input("please enter the student file. ")
# open the file
with open(fileName, "r") as f:
# read in the data, and for each student calculate their average grade and classification
    data = f.readlines()
# this is a good use for list comprehensions:
data = [ line.strip().split(",") for line in data ]
# turns data into a 2D array
data.pop(0)
length = len(data)
newData =[]
i = 0
#print(data)
for line in data:
    if i >= (length-1):
        break
    else:
        newArr =[]
        j = 0
        gradeSum = 0
        gradeNum = 0
        gradeAvg = 0
        for val in line:
            if j == 0:
                newArr.append(val)
            elif val == "":
                break
            else:
                gradeSum = gradeSum+int(val)
                gradeNum = gradeNum +1
            j = j+1
        gradeAvg = float(gradeSum/gradeNum)
        gradeAvg = round(gradeAvg,2)  
        newArr.append(str(gradeAvg))

        if gradeAvg >= 70:
            finalGrade = "1"
        elif gradeAvg >= 60:
            finalGrade = "2.1"
        elif gradeAvg >= 50:
            finalGrade = "2.2"
        elif gradeAvg >= 40:
            finalGrade = "3"
        else:
            finalGrade = "F"
        newArr.append(finalGrade)
  
    newData.append(newArr)  
    i = i+1





# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}
print(newData)

# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'
newFileName = fileName + "_out.csv"

try:
    with open(newFileName, "w") as f:
        for l in newData:
            print(l)
            for v in l:
                if l.index(v) < 2:
                    f.write(v)
                    f.write(",")
                else:
                    f.write(v)
                    f.write("\n")
                
except FileExistsError:
    print("file already exists, exclusive creation aborted.")
#This tries to create file.txt only if it doesn’t exist, otherwise prints an informative message.
# You can compare your output files with the 4 example files in example_outfiles folder