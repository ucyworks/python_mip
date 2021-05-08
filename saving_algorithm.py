"""
' --- Saving Algorithm for ATSP --- ' 
#distances
1-1: 0
1-2: 10
1-3: 22
1-4: 8
2-1: 7
2-2: 0
2-3: 17
2-4: 9
3-1: 24
3-2: 4
3-3: 0
3-4: 11
4-1: 9
4-2: 12
4-3: 10
4-4: 0

#order savings
S_12 = C_01 + C_02 - C_12
S_13 = C_01 + C_03 - C_13
S_14 = C_01 + C_04 - C_14
...
S_43 = C_04 + C_03 - C43

#routing
0 - S12 - S23 ... 

"""

distances = [[0,10,22,8],
             [7,0,17,9],
             [24,4,0,11],
             [9,12,10,0]]

 
nodes = [["C00",0,0],
         ["C01",0,1],
         ["C02",0,2],
         ["C03",0,3],
         ["C10",1,0],
         ["C11",1,1],
         ["C12",1,2],
         ["C13",1,3],
         ["C20",2,0],
         ["C21",2,1],
         ["C22",2,2],
         ["C23",2,3],
         ["C30",3,0],
         ["C31",3,1],
         ["C32",3,2],
         ["C33",3,3]]
 
#transpose for distance matrix
for i in distances:
    row_index = distances.index(i)
    for j in i:
        column_index = i.index(j)
        for z in nodes:
            if z[1] == row_index and z[2] == column_index:
                z.append(j)
#print(nodes)
 
    
#order savings and sorting   
order = []           
for i in nodes:
    if i[1] >0 and i[2] > 0 and i[1] != i[2]:
        first_node = distances[0][i[1]]
        second_node = distances[0][i[2]]
        depot = distances[i[1]][i[2]]
        result = first_node + second_node - depot
        i.append(result)
    
    #sorting    
    if len(i) == 5:
        order.append(i)
    order= sorted(order,key=lambda l:l[4],reverse=True)
#print(order)

#routing
route = [0]
for i in order:
    if i[2] in route and i[1] not in route:
        route.insert(route.index(i[2]),i[1]) 
    elif i[1] not in route:
        route.append(i[1])
        route.append(i[2])
 
route.append(0) 
    
#cost calculation
cost = 0       
i=0
while i < len(route)-1:
    for j in nodes:
        if j[1] == route[i] and j[2] == route[i+1]:
            cost = cost + j[3]
    i += 1
   
print("Route: ",route)
print("Cost: ",cost)


 
