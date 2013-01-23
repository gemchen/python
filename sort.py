import random
import datetime
import copy

def QuickSort(data, low = 0, high = None):
	if high == None:
		high = len(data) - 1
	if low < high:
		sign, i, j = data[low], low, high
		while i < j:
			while i < j and data[j] >= sign:
				j = j - 1
			if i < j:
				data[i] = data[j]
				i = i + 1
			while i < j and data[i] <= sign:
				i = i + 1
			if i < j:
				data[j] = data[i]
				j = j - 1
		data[i] = sign
		QuickSort(data, low, i - 1)
		QuickSort(data, i + 1, high)

def qsort(L):
	if L == []: return []
	return qsort([x for x in L[1:] if x <= L[0]]) + L[0:1] + qsort([x for x in L[1:] if x > L[0]])

def sort_perform(sortfunc, data):
    sort_data = copy.deepcopy(data)
    t1 = datetime.datetime.now()
    sortfunc(sort_data)
    t2 = datetime.datetime.now()
    print sortfunc.__name__, t2 - t1
    #print sort_data

data = [random.randint(0, 65536) for i in range(2000)]
#print data
sort_perform(QuickSort, data)
sort_perform(qsort, data)
# sort_perform(bubblesort, data)