import pandas as pd

df=pd.read_excel('Network 2142.xlsx')
# print(df)
df1=df.query('Order==1')
df2=df.query('Order==2')
df3=df.query('Order==3')
df4=df.query('Order==4')

order1_indexlist=[]
fromnodesdf1=[]
for index, row in df1.iterrows():
    # print(index, row['from_node'])
    order1_indexlist.append(index)
    fromnodesdf1.append(row['from_node'])
# print(fromnodesdf1)
# print(order1_indexlist)

tonodesdf1=[]
for index, row in df1.iterrows():
    # print(index, row['from_node'])
    tonodesdf1.append(row['to_node'])
# print(tonodesdf1)

# for i in order1_indexlist:
#     from_node = df1.loc[i]['from_node']
#     # print(from_node)
#     to_node=df1.loc[i]['to_node']
#     # print(to_node)
# count=df1['to_node'].value_counts()

pd.options.mode.chained_assignment = None  # default='warn'
df1['freq_count'] = df1.groupby('to_node')['to_node'].transform('count')
# print(df1)

oneone=[]
for index, row in df1.iterrows():
    # print(index, row['from_node'])
    if row['freq_count']==2:
        oneone.append(index)
# print(oneone)
N11=len(oneone)
##############################################
tonodesdf2=[]
for index, row in df2.iterrows():
    # print(index, row['from_node'])
    tonodesdf2.append(row['to_node'])
# print(tonodesdf2)

df12=df1.loc[(df1['to_node'].isin(tonodesdf2))]
N12=len(df12)
##############################################
tonodesdf3=[]
for index, row in df3.iterrows():
    # print(index, row['from_node'])
    tonodesdf3.append(row['to_node'])
# print(tonodesdf3)

df13=df1.loc[(df1['to_node'].isin(tonodesdf3))]
N13=len(df13)
##############################################
tonodesdf4=[]
for index, row in df4.iterrows():
    # print(index, row['from_node'])
    tonodesdf4.append(row['to_node'])
# print(tonodesdf4)

df14=df1.loc[(df1['to_node'].isin(tonodesdf4))]
N14=len(df14)
########################################################
order2_indexlist=[]
fromnodesdf2=[]
for index, row in df2.iterrows():
    # print(index, row['from_node'])
    order2_indexlist.append(index)
    fromnodesdf2.append(row['from_node'])
# print(fromnodesdf2)
# print(order2_indexlist)

tonodesdf2=[]
for index, row in df2.iterrows():
    # print(index, row['from_node'])
    tonodesdf2.append(row['to_node'])
# print(tonodesdf2)

pd.options.mode.chained_assignment = None  # default='warn'
df2['freq_count'] = df2.groupby('to_node')['to_node'].transform('count')
# print(df2)

twotwo=[]
for index, row in df2.iterrows():
    # print(index, row['from_node'])
    if row['freq_count']==2:
        twotwo.append(index)
# print(twotwo)
N22=len(twotwo)
##############################################
tonodesdf3=[]
for index, row in df3.iterrows():
    # print(index, row['from_node'])
    tonodesdf3.append(row['to_node'])
# print(tonodesdf3)

df23=df2.loc[(df2['to_node'].isin(tonodesdf3))]
N23=len(df23)
##############################################
tonodesdf4=[]
for index, row in df4.iterrows():
    # print(index, row['from_node'])
    tonodesdf4.append(row['to_node'])
# print(tonodesdf4)

df24=df2.loc[(df2['to_node'].isin(tonodesdf4))]
N24=len(df24)
##############################################
order3_indexlist=[]
fromnodesdf3=[]
for index, row in df3.iterrows():
    # print(index, row['from_node'])
    order3_indexlist.append(index)
    fromnodesdf3.append(row['from_node'])
# print(fromnodesdf3)
# print(order3_indexlist)

tonodesdf3=[]
for index, row in df3.iterrows():
    # print(index, row['from_node'])
    tonodesdf3.append(row['to_node'])
# print(tonodesdf3)

pd.options.mode.chained_assignment = None  # default='warn'
df3['freq_count'] = df3.groupby('to_node')['to_node'].transform('count')
# print(df3)

thrthr=[]
for index, row in df3.iterrows():
    # print(index, row['from_node'])
    if row['freq_count']==2:
        thrthr.append(index)
# print(thrthr)
N33=len(thrthr)
##############################################
tonodesdf4=[]
for index, row in df4.iterrows():
    # print(index, row['from_node'])
    tonodesdf4.append(row['to_node'])
# print(tonodesdf4)

df34=df3.loc[(df3['to_node'].isin(tonodesdf4))]
N34=len(df34)
##############################################
order4_indexlist=[]
fromnodesdf4=[]
for index, row in df4.iterrows():
    # print(index, row['from_node'])
    order4_indexlist.append(index)
    fromnodesdf4.append(row['from_node'])
# print(fromnodesdf3)
# print(order4_indexlist)

tonodesdf4=[]
for index, row in df4.iterrows():
    # print(index, row['from_node'])
    tonodesdf4.append(row['to_node'])
# print(tonodesdf4)
N44=1
print('N11=',N11,'N12=',N12,'N13=',N13,'N14=',N14,'N22=',N22,'N23=',N23,'N24=',N24,'N33=',N33,'N34=',N34,'N44=',N44)
N1=N11+N12+N13+N14
N2=N22+N23+N24
N3=N33+N34
N4=N44
print('N1=',N1,'N2=',N2,'N3=',N3,'N4=',N4)
T12=N12/N2
T13=N13/N3
T14=N14/N4
T23=N23/N3
T24=N24/N4
T34=N34/N4
print('T12=',T12,'T13=',T13,'T14=',T14,'T23=',T23,'T24=',T24,'T34=',T34)
T1=(T12+T23+T34)/3
T2=(T13+T24)/2
T3=T14
print('T1=',T1,'T2=',T2,'T3=',T3)
T=[T1,T2,T3]
K=[1,2,3]
import matplotlib.pyplot as plt
import numpy as np
import math

plt.figure()
x=np.array(K)
y=np.array(T)
log_y = np.log(y)
coefficients = np.polyfit(x, log_y, 1)
# print(coefficients)
# print(coefficients[0],coefficients[1])
Y = np.exp(coefficients[1]) * np.exp((coefficients[0])*x)
plt.text(1, 27, f'Ln(y)={coefficients[0]}*x - {-coefficients[1]}',c='rebeccapurple')
plt.title("Tokunaga parameters")
plt.plot(x, Y,c='rebeccapurple')
plt.scatter(x, y)
plt.xlabel("Side Branching Order, k", fontsize=15)
plt.ylabel("Tk", fontsize=15)
plt.yscale('log')
plt.grid()
# plt.text(-5, 60, f'Log(Tk)={coefficients[0]}*x + {coefficients}', fontsize = 22)
correlation_matrix = np.corrcoef(Y, y)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
c=math.exp(coefficients[0])
a=math.exp(math.log(c)+coefficients[1])
print(f'Ln(y)={coefficients[0]}*x - {-coefficients[1]}')
print('c=',c,'a=',a)
print('r_squared=',r_squared)
plt.show()





