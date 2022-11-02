import pandas as pd
from pandasql import sqldf
import sys
import csv

print("This file take inputs with specific format check attached sample")
filename = input("Please input file name  :")
data = pd.read_csv(filename)
df = pd.DataFrame(data, columns=['Id', 'Area', 'Name', 'Quantity', 'Brand'])
# product = df.value_counts(subset=["Name", "Quantity"])
df.Name.unique()
size = df.index.size
output1 = sqldf(
    " select Name,Brand from (SELECT count(*) as x, Name, Brand FROM df GROUP BY  Name, Brand  order by count(*) desc ) group by Name,Brand ")

query0 = f"SELECT p.Name,SUM(b.Quantity)/{size} as sumof_Quantity FROM  df p INNER JOIN df b ON p.Id=b.Id GROUP BY  p.Name"

output0 = sqldf(query0)
z = df.describe(include='all')
output1.to_csv('1_input_' + filename, index=False, header=False)
output0.to_csv('0_input_' + filename, index=False, header=False)
print(df)
# print(product)
print("\n")
print(df.index.size)
print("\n")
print(output0)
print("\n")
print(output1)
