numList = [1,2,3,4,5]
specificNum = 3


def binary_search(list,find):
  i=0
  while i != find and i <= len(list):
    i+=1
  if i == find:
    print(f"{find} is found at the index of {i-1}")
  else:
    print(f"{find} is not found")


binary_search(numList,specificNum)