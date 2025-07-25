lst = [["6:29" , "12:01" , 2000 , "Dell"] , ["6:30" , "12:02" , 1050 , "Oracle"] , ["12:01" , "12:40" , 600 , "Cerone"], ["12:35" , "12:45" , 3000,"HCL"]]
while True:
    startTime = input("Enter the start time : ")
    endTime = input("Enter the end time : ")
    amount = int(input("Enter the amount : "))
    print("Enter 1 to continue ")
    print("Enter 2 to end ")
    userInput = int(input())

    if(userInput == 2):
        break

sorted_lst = []

for i in lst:
    hour,minutes = i[0].split(":")
    hour = int(hour)
    for index,j in enumerate(sorted_lst):
        tempHour,tempMinutes = j[0].split(":")
        tempHour = int(tempHour)
        if(tempHour == hour):
            sorted_lst.insert(index+1,i)
            break
        elif(tempHour > hour):
            sorted_lst.insert(index,i)
            break
    else:
        sorted_lst.append(i)

start_time_hour, start_time_minutes = sorted_lst[0][0].split(":")
end_time_hour, end_time_minutes = sorted_lst[0][1].split(":")

start_time_hour = int(start_time_hour)
start_time_minutes = int(start_time_minutes)
end_time_hour = int(end_time_hour)
end_time_minutes = int(end_time_minutes)

amount = sorted_lst[0][2]

result = []

def calculate_max_revenue(index , sorted_lst , start_time_hour , start_time_minutes ,end_time_hour , end_time_minutes , amount , result):
    if(index >= len(sorted_lst)):
        return amount,result
    hour,minutes = sorted_lst[index][0].split(":")
    hour = int(hour)
    minutes = int(minutes)
    ended_hour,ended_minutes = sorted_lst[index][1].split(":")
    ended_hour = int(ended_hour)
    ended_minutes = int(ended_minutes)
    current_revene = sorted_lst[index][2]

    if(end_time_hour < hour or (end_time_hour == hour and end_time_minutes <= minutes)):
        new_list = result
        new_list.append(sorted_lst[index][3])
        return calculate_max_revenue(index+1 ,  sorted_lst ,  hour , minutes , ended_hour , ended_minutes , amount+current_revene , new_list)
    else:
        new_list = result.copy()
        differentRevenue , result2 = calculate_max_revenue(index+1 ,  sorted_lst , start_time_hour , start_time_minutes , end_time_hour , end_time_minutes , amount , result)
        new_list.pop()
        new_list.append(sorted_lst[index][3])
        currentRevenue , result1 = calculate_max_revenue(index+1 ,  sorted_lst , hour , minutes , ended_hour , ended_minutes , (amount - sorted_lst[index-1][2]) + current_revene , new_list)
        if currentRevenue == differentRevenue:
            minimumTimeDifference1 = ((start_time_hour*60) + start_time_minutes) - ((end_time_hour*60) + end_time_minutes)
            minimumTimeDifference2 = ((hour*60) + minutes) - ((ended_hour*60) + ended_minutes)
            if minimumTimeDifference1 <= minimumTimeDifference2:
                return differentRevenue , result2
            else:
                return current_revene , result1
        elif currentRevenue > differentRevenue:
            return currentRevenue , result1
        elif currentRevenue < differentRevenue:
            return differentRevenue , result2
    
result.append(sorted_lst[0][3])
print(calculate_max_revenue(1 , sorted_lst , start_time_hour , start_time_minutes , end_time_hour , end_time_minutes , amount , result))