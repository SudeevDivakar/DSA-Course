def power_sum(array,power=1):
    #write code here
    sum = 0
    for i in array:
        if type(i) == list:
            sum += power_sum(i, power + 1)
        elif type(i) == int:
            sum += i
    return sum ** power

print(power_sum([1,2,[2,3,5]]))