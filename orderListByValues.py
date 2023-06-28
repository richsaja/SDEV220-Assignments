numList = [0,2,1,2,0]
orderedNum = []

def order_numbers(numbers):
  orderedNum.append(numbers[0])
  for i in range(1,len(numList)):
    smaller_check(i,numbers)
  print(orderedNum)

def smaller_check(index, num):
  for count in range(len(orderedNum)):
    if num[index] < orderedNum[count]:
      orderedNum.insert(count, num[index])
      return
  orderedNum.append(num[index])

order_numbers(numList)