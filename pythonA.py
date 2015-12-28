#!/usr/bin/python
def BullleSort(list):
	n = len(list)
	for i in range(0,n):y
		print list[i]
		for j in range(i,n):
			if list[i] >=list[j]:
				list[i],list[j] = list[j],list[i]
				print list
	return list
def InsertionSort (list):
	if len(list) > 1:
		for i in range(1,len(list)):
			while i > 0 and list[i] > list[i-1]:
				tmp = list[i]
				list[i] = list[i-1]
				list[i-1] = tmp
				i = i-1
				print list
def SelectSort(list):
	for i in range(len(list)):
		position = i
		for j in range(len(list)):
			if list[position] > list[j]:
				partition = j
		if position != i:
	 		tmp = list[position]
			list[position] = list[i]
			list[i] = tmp
	return  list

def getprim(n):
        p = 3
        x = 0
        while(x<n):
            result = True
            for i in range(2,p-1):
                    if (p % i == 0):
                        result = False
            if result == True:
                    x = x+1
                    rst = p
            p = p+2
        print rst
if __name__ == '__main__':
	#print InsertionSort(list)
	#print SelectSort(list)
    getprim(1000)