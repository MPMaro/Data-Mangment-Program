


def bubbleSort(anArray, key):
  for i in range(len(anArray)):
    for j in range(i+1, len(anArray)):
        if anArray[i][key] > anArray[j][key]:
            anArray[i], anArray[j] = anArray[j], anArray[i]






def binary_search(list, key, value):
  low = 0
  high = len(list) - 1
  while low <= high:
    mid = (low + high) // 2
    if list[mid][key] == value:
      return mid
    elif list[mid][key] < value:
      low = mid + 1
    else:
      high = mid - 1
  return -1