#ques 3 - Ascending order
#sample input                               Sample output
#4                                          [10,20,45,87]
#20
#87
#45
#10

n = int(input())
temp_list=[]
final_list=[]
count=0
for i in range(n):
    temp=int(input())
    temp_list=[temp]
    final_list= final_list + temp_list

for i in range(n):
    for j in range(i+1,n):
        if final_list[i] > final_list[j]:
            a=final_list[i]
            final_list[i] = final_list[j]
            final_list[j] = a
            
                
print(final_list)
