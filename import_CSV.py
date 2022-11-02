import pandas as pd
from pandasql import sqldf
import sys
import csv


data=pd.read_csv("C:\\Users\\hisham\\Desktop\\convertcsv.csv")
df = pd.DataFrame(data,columns=['Id','Area','Name','Quantity','Brand'])
orders_count=df.count('index')
product=df.value_counts(subset=["Name","Quantity"])
df.Name.unique()
size=df.index.size
output1 = sqldf(" select Name,Brand from (SELECT count(*) as x, Name, Brand FROM df GROUP BY  Name, Brand  order by count(*) desc ) group by Name,Brand ")

query0="SELECT p.Name,SUM(b.Quantity)/"+str(size)+" as sumof_Quantity FROM  df p INNER JOIN df b ON p.Id=b.Id GROUP BY  p.Name"
output0 = sqldf(query0)
z=df.describe(include='all')
output1.to_csv('C:\\Users\\hisham\\Desktop\\1_input_example.csv',index=False,header=False)
output0.to_csv('C:\\Users\\hisham\\Desktop\\0_input_example.csv',index=False,header=False)
print(df)
print(product)
print("\n")
print(df.index.size)
print("\n")
print(output0)
print("\n")
print(output1)

