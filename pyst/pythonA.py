#!/usr/bin/python
def BullleSort(list):
	n = len(list)
	for i in range(0,n):
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

if __name__ == '__main__':
	list = [6,7,5,2,3,4,1]
	print InsertionSort(list)
	print SelectSort(list)
	print 'test'
