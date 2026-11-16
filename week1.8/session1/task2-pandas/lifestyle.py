import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
# a dataframe, a type of tabular data.
# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
size = data.size
print("Number of Students = {}".format(size))
# Find the mean average GPA of the students
mn = data.mean(axis=0, skipna=True, numeric_only=True)
print(f"Mean GPA = {mn._get_value("GPA",0)}")

# Find the standard deviation of how much sleep students get per day
sd = data.std(axis =0, skipna = True, numeric_only =True)
print(f"Standard Deviation of Sleep = {sd._get_value("Sleep_Hours_Per_Day",0)}")
# Find the maximum amount of study hours per day

# Sort the students by social hours per day ascending (lowest -> highest)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
