def insertionSort(anArray):
    n = len(anArray)
    for i in range(1, n):
        ins = anArray[i]
        x = i - 1
        while x >= 0 and ins < anArray[x]:
            anArray[x + 1] = anArray[x]
            x = x - 1
        anArray[x + 1] = ins
        
        
key = "IBSN"

def bubbleSort(anArray):
  for i in range(len(anArray)):
    for j in range(i+1, len(anArray)):
        if anArray[i][key] > anArray[j][key]:
            anArray[i], anArray[j] = anArray[j], anArray[i]

