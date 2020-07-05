'''
	There are two sorted arrays nums1 and nums2 of size m and n respectively.
	Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
	Example 1:
	nums1 = [1, 3]
	nums2 = [2]
	The median is 2.0
	Example 2:
	nums1 = [1, 2]
	nums2 = [3, 4]
	The median is (2 + 3)/2 = 2.5
'''
def finding_position(result_list, number):
	low, high = 0, 
def merge_median(list1, list2):
	#first we will consider all the edhe cases
	l1 = len(list1)
	l2 = len(list2)
	maximum = l1 if l1>l2 else l2
	minimum = l2 if l1>l2 else l1
	if minimum==1:
		if maximum==1:
			return (list1[0]+list2[0])/2
		elif maximum==2:
			if l2==2:
				if list1[0]<list2[0]:
					return list2[0]
				elif list1[0]>list2[1]:
					return list2[1]
				else:
					return list1[0]
			else:
				if list2[0]<list1[0]:
					return list1[0]
				elif list2[0]>list1[1]:
					return list1[1]
				else:
					return list2[0]
		else:
			if l2==maximum:
				if (l2)%2==0:
					mid = int(l2/2)
					if list1[0]<list2[mid-1]:
						return list2[mid-1]
					elif list1[0]>list2[mid]:
						return list2[mid]
					else:
						return list1[0]
				else:
					mid = int(l2/2)
					if list1[0]<list2[mid-1]:
						return (list2[mid]+list2[mid-1])/2
					elif list1[0]>list2[mid+1]:
						return (list2[mid]+list2[mid+1])/2
					else:
						return (list1[0]+list2[mid])/2

			else:#just swaping 1 and 2
				if (l1)%2==0:
					mid = int(l1/2)
					if list2[0]<list1[mid-1]:
						return list1[mid-1]
					elif list2[0]>list1[mid]:
						return list1[mid]
					else:
						return list2[0]
				else:
					mid = int(l1/2)
					if list2[0]<list1[mid-1]:
						return (list1[mid]+list1[mid-1])/2
					elif list2[0]>list1[mid+1]:
						return (list1[mid]+list1[mid+1])/2
					else:
						return (list2[0]+list1[mid])/2
	elif minimum==2:
		if maximum==2:
			if list1[0]<list1[1]<list2[0]<list2[1]:
				return (list1[1]+list2[0])/2
			elif list1[0]<list2[0]<list2[1]<list1[1]:
				return (list2[0]+list2[1])/2
			elif list1[0]<list2[0]<list1[1]<list2[1]:
				return (list2[0]+list1[1])/2
			elif list2[0]<list2[1]<list1[0]<list1[1]:
				return (list2[1]+list1[0])/2
			elif list2[0]<list1[0]<list1[1]<list2[1]:
				return (list1[0]+list1[1])/2
			else:
				return (list1[0]+list2[1])/2
		else:
			if maximum%
	else:
		mid = int(l2/2)
		med1 = list1[mid]
		med2 = list2[mid]
		if med1<med2:
			return merge_median(list1[mid:],list2[:mid+1])
		elif med1>med2:
			return merge_median(list1[:mid+1],list2[mid:])
		else:
			return med1
