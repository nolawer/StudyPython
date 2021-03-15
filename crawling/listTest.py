dic = {}

list2 = ['a',1,'b',2,'c',3,'d',4]

count = 0

oddlist=list2[0::2]
evenlist=list2[1::2]


print(oddlist)
print(evenlist)

max = int(len(oddlist))

i = 0
print(max)

for i in range(0, max):
    dic[oddlist[i]] = evenlist[i]
    print(i)

print (dic)

# for i in list2:
#
#     dic[list2[count]] = list2[count+1]
#     count += 1
#     if count == max-1:
#         break
#
#
#
# print(dic)



#print(max)

# for i in list2:
#     if count == 0:
#         list.append([list2[count], list2[count + 1]])
#         count += 1
#         print(count)
#     elif count % 2 == 1:
#         list.append([list2[count],list2[count+1]])
#         count += 1
#         print(count)
#     elif count % 2 == 0:
#         continue
#     elif count == max-1:
#         break

#print(list)