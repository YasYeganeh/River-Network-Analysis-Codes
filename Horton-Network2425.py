import pandas as pd

df=pd.read_excel('Network 2425.xlsx')
# print(df)

######## baraye yek order
df1=df[df['Order']==1]
df2=df[df['Order']==2]
df3=df[df['Order']==3]
df4=df[df['Order']==4]
df5=df[df['Order']==5]
# print(df1)
# print(df1['from_node'].tolist())
max_order=max(df['Order'])
min_order=min(df['Order'])
#############################################
# order1
fromnode_list=df1['from_node'].tolist()
tonode_list=list(df1['to_node'])
# print(tonode_list)
# print(fromnode_list)

a1=[]
for i in tonode_list:
    count=0
    if i not in fromnode_list:
        count+=1
        a1.append(i)
    # print(i,count)
# print('a1:',a1)
# print(len(a1))
#############################################
# order2
fromnode_list=df2['from_node'].tolist()
tonode_list=df2['to_node'].tolist()

a2=[]
for i in tonode_list:
    count=0
    if i not in fromnode_list:
        count+=1
        a2.append(i)
    # print(i,count)
# print('a2:',a2)
# print(len(a2))
# #############################################
# order3
fromnode_list=df3['from_node'].tolist()
tonode_list=df3['to_node'].tolist()

a3=[]
for i in tonode_list:
    count=0
    if i not in fromnode_list:
        count+=1
        a3.append(i)
    # print(i,count)
# print('a3:',a3)
# print(len(a3))
#############################################
# order4
fromnode_list=df4['from_node'].tolist()
tonode_list=df4['to_node'].tolist()

a4=[]
for i in tonode_list:
    count=0
    if i not in fromnode_list:
        count+=1
        a4.append(i)
    # print(i,count)
# print('a4:',a4)
# print(len(a4))
#############################################
# order5
fromnode_list=df5['from_node'].tolist()
tonode_list=list(df5['to_node'])
# print(tonode_list)
# print(fromnode_list)

a5=[]
for i in tonode_list:
    count=0
    if i not in fromnode_list:
        count+=1
        a5.append(i)
    # print(i,count)
# print('a5:',a5)
# print(len(a5))

## dataframe linkhaye complete order az har martabe
df1_complete=df.loc[(df['to_node'].isin(a1)) & (df['Order']==1)]
df2_complete=df.loc[(df['to_node'].isin(a2)) & (df['Order']==2)]
df3_complete=df.loc[(df['to_node'].isin(a3)) & (df['Order']==3)]
df4_complete=df.loc[(df['to_node'].isin(a4)) & (df['Order']==4)]
df5_complete=df.loc[(df['to_node'].isin(a5)) & (df['Order']==5)]
# print(df1_complete)
# print(df2_complete)
# print(df3_complete)
# print(df4_complete)
##########################################
# NESBATE TEDAD
# rasme nemoodare nesbate tedade horton
import matplotlib.pyplot as plt
import numpy as np
import math

plt.figure()
x=np.array(list(range(min_order,max_order+1,1)))
y=np.array([len(a1),len(a2),len(a3),len(a4),len(a5)])
log_y = np.log(y)
coefficients = np.polyfit(x, log_y, 1)
# print(coefficients)
Rb=math.exp(-coefficients[0])
print('Rb:',Rb)
# print(coefficients[0],coefficients[1])
c = np.exp(coefficients[1]) * np.exp((coefficients[0])*x)
plt.text(1.5, 100, f'Ln(y)={coefficients[0]}*x + {coefficients[1]}',c='g')
plt.title("Rb")
plt.plot(x, c,c='g')
plt.scatter(x, y)
plt.xlabel("Order", fontsize=15)
plt.ylabel("Number of branches", fontsize=15)
plt.yscale('log')
plt.grid()
correlation_matrix = np.corrcoef(c, y)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print(f'Ln(y)={coefficients[0]}*x + {coefficients[1]}')
print('R^2:',r_squared)
# plt.show()
##########################################
# NESBATE TOOL HA

alllinks_List=list(df['arcid'])
alltonodes_List=list(df['to_node'])
allfromnodes_List=list(df['from_node'])
# print(allfromnodes_List)
# print(alltonodes_List)
# print(alllinks_List)
branch1_List=list(df1_complete['arcid'])
tonodes_branch1_List=list(df1_complete['to_node'])
fromnodes_branch1_List=list(df1_complete['from_node'])
branch2_List=list(df2_complete['arcid'])
tonodes_branch2_List=list(df2_complete['to_node'])
fromnodes_branch2_List=list(df2_complete['from_node'])
branch3_List=list(df3_complete['arcid'])
tonodes_branch3_List=list(df3_complete['to_node'])
fromnodes_branch3_List=list(df3_complete['from_node'])
branch4_List=list(df4_complete['arcid'])
tonodes_branch4_List=list(df4_complete['to_node'])
fromnodes_branch4_List=list(df4_complete['from_node'])
branch5_List=list(df5_complete['arcid'])
tonodes_branch5_List=list(df5_complete['to_node'])
fromnodes_branch5_List=list(df5_complete['from_node'])
# print(completelink1_List)
# print(tonodes_complete1_List)
allbranches_List=branch1_List+branch2_List+branch3_List+branch4_List+branch5_List
# print(allbrancheslink_List)
# print(len(allbranches_List))

startnodes_List=[]
for element in allfromnodes_List:
    if element not in alltonodes_List:
        startnodes_List.append(element)
# print(startnodes_List)
Outlet=list(set(df['to_node'])-set(df['from_node']))
outlet=Outlet[0]
# print(outlet)

branch_startnodes={}
for branch in allbranches_List:
    # print(branch)
    fromnode=int(df[df['arcid']==branch]['from_node'])
    if fromnode in startnodes_List:
        branch_startnodes[branch]=[fromnode]
    else:
        branch_startnodes_List=[]
        for node in startnodes_List:
            to_node=int(df[df['from_node']==node]['to_node'])
            while to_node!=outlet:
                from_node=to_node
                if from_node==fromnode:
                    branch_startnodes_List.append(node)
                    break
                to_node=int(df[df['from_node']==from_node]['to_node'])
        branch_startnodes[branch]=branch_startnodes_List
# print(branch_startnodes)


def distance(start,end):
    tonode=int(df[df['from_node']==start]['to_node'])
    Distance=float(df[df['from_node']==start]['Length'])
    while tonode != end:
        start = tonode
        Distance+=float(df[df['from_node']==start]['Length'])
        tonode = int(df[df['from_node'] == start]['to_node'])
    return Distance
branch_riverlength={}
for branch in branch_startnodes.keys():
    allstartnodes=branch_startnodes[branch]
    to_node = int(df[df['arcid'] == branch]['to_node'])
    DIRECTIONS=[]
    for startnode in allstartnodes:
        L=distance(startnode,to_node)
        DIRECTIONS.append(L)
    max_riverlength=max(DIRECTIONS)
    # print(branch,max_riverlength)
    branch_riverlength[branch]=max_riverlength
# print(branch_riverlength)

l=[]
for branch in branch1_List:
    L_list=branch_riverlength[branch]
    l.append(L_list)
    L_avg1=sum(l)/len(l)
# print('L_avg1:',L_avg1)
# print(len(l))
l=[]
for branch in branch2_List:
    L_list=branch_riverlength[branch]
    l.append(L_list)
    L_avg2=sum(l)/len(l)
# print('L_avg2:',L_avg2)
l=[]
for branch in branch3_List:
    L_list=branch_riverlength[branch]
    l.append(L_list)
    L_avg3=sum(l)/len(l)
# print('L_avg3:',L_avg3)
l=[]
for branch in branch4_List:
    L_list=branch_riverlength[branch]
    l.append(L_list)
    L_avg4=sum(l)/len(l)
# print('L_avg4:',L_avg4)
l=[]
for branch in branch5_List:
    L_list=branch_riverlength[branch]
    l.append(L_list)
    L_avg5=sum(l)/len(l)
# print('L_avg5:',L_avg5)

plt.figure()
x=np.array(list(range(min_order,max_order+1,1)))
y=np.array([L_avg1,L_avg2,L_avg3,L_avg4,L_avg5])
log_y = np.log(y)
coefficients = np.polyfit(x, log_y, 1)
# print(coefficients)
Rl=math.exp(coefficients[0])
print('Rl:',Rl)
# print(coefficients[0],coefficients[1])
c = np.exp(coefficients[1]) * np.exp((coefficients[0])*x)
plt.text(1, 50000, f'Ln(y)={coefficients[0]}*x + {coefficients[1]}',c='b')
plt.title("Rl")
plt.plot(x, c,c='b')
plt.scatter(x, y)
plt.xlabel("Order", fontsize=15)
plt.ylabel("Average Branch Length", fontsize=15)
plt.yscale('log')
plt.grid()
correlation_matrix = np.corrcoef(c, y)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print(f'Ln(y)={coefficients[0]}*x + {coefficients[1]}')
print('R^2:',r_squared)
# plt.show()
# #########################################################
# NESBATE MASAHAT
# all_area_list=list(df['Area'])
# all_area_list1=set(list(df['Area']))
# print(len(all_area_list))
# print(len(all_area_list1))


branch_nodes={}
for branch in allbranches_List:
    fromnode=int(df[df['arcid']==branch]['from_node'])
    id1=int(df[df['arcid']==branch]['arcid'])
    # print(branch_startnodes[branch])
    if fromnode in startnodes_List:
        branch_nodes[branch]=[fromnode]
    else:
        branch_nodes_list=[]
        for node in branch_startnodes[branch]:
            to_node=int(df[df['from_node']==node]['to_node'])
            # print(node)
            while to_node!=Outlet:
                from_node=to_node
                # print(from_node)
                branch_nodes_list.append(from_node)
                if from_node==fromnode:
                    branch_nodes_list.append(node)
                    break
                to_node=int(df[df['from_node']==from_node]['to_node'])
        branch_nodes[branch]=list(set(branch_nodes_list))
# print(branch_nodes)

branch_area={}
for branch in allbranches_List:
    A = []
    for link in branch_nodes[branch]:
        area=int(df[df['from_node']==link]['Area'])
        A.append(area)
    branch_area[branch]=A
# print(branch_area)

a1=[]
for branch in branch1_List:
    a1+=(branch_area[branch])
Area1_avg=sum(a1)/len(branch1_List)
# print('Area1_avg:',Area1_avg)

a2=[]
for branch in branch2_List:
    a2+=(branch_area[branch])
Area2_avg=sum(a2)/len(branch2_List)
# print('Area2_avg:',Area2_avg)

a3=[]
for branch in branch3_List:
    a3+=(branch_area[branch])
Area3_avg=sum(a3)/len(branch3_List)
# print('Area3_avg:',Area3_avg)

a4=[]
for branch in branch4_List:
    a4+=(branch_area[branch])
Area4_avg=sum(a4)/len(branch4_List)
# print('Area4_avg:',Area4_avg)

a5=[]
for branch in branch5_List:
    a5+=(branch_area[branch])
Area5_avg=sum(a5)/len(branch5_List)
# print('Area5_avg:',Area5_avg)

plt.figure()
x=np.array(list(range(min_order,max_order+1,1)))
y=np.array([Area1_avg,Area2_avg,Area3_avg,Area4_avg,Area5_avg])
log_y = np.log(y)
coefficients = np.polyfit(x, log_y, 1)
# print(coefficients)
Ra=math.exp(coefficients[0])
print('Ra:',Ra)
# print(coefficients[0],coefficients[1])
c = np.exp(coefficients[1]) * np.exp((coefficients[0])*x)
plt.text(1, 1000000000, f'Ln(y)={coefficients[0]}*x + {coefficients[1]}',c='coral')
plt.title("Ra")
plt.plot(x, c,c='coral')
plt.scatter(x, y)
plt.xlabel("Order", fontsize=15)
plt.ylabel("Average Branch Area", fontsize=15)
plt.yscale('log')
plt.grid()
correlation_matrix = np.corrcoef(c, y)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print(f'Ln(y)={coefficients[0]}*x + {coefficients[1]}')
print('R^2:',r_squared)
plt.show()

