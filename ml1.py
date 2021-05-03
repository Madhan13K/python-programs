import pandas as pf
xlsx_file="1000 Records.csv"
df=pf.read_csv(xlsx_file)
df.head()
# print(df)
l=df.loc[0,"Region"]
print(l)
i=2
x=lambda i:i*2
print(x(5))
a=df.ix[0,1]
print(a)
