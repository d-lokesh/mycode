def sortbubble(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list




nums=[2,8,1,5,7,5,500,588,0]
print(sortbubble(nums))
