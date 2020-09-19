#Ambata, Jo Simon V.
#OL157 - 2018100711


import os
from prettytable import PrettyTable

#initialization
a = [0,2,4,5]
b = [7,4,1,4]
p = [4,3,2,1]
w = [0, 0, 0, 0]
ta = [0, 0, 0, 0]
time = 0

process_list = []
process_features = dict()
process_dict = dict()
sum_b = sum(b)
size = len(a)
i = 0
while (i<len(a)):
	process_dict[i] = [a[i], b[i],p[i], w[i], ta[i], 0]
	i = i + 1

#First Come First Serve



while(time < sum_b):
	available_dict = []

	for i in range(len(a)):
		if(process_dict[i][0] <= time and process_dict[i][1] > 0):
			available_dict.append(i)

	smallest = 999
	smallest_index = 999
	for j in available_dict:
		if(process_dict[j][0] <= smallest and process_dict[j][1] > 0 ):
			smallest = process_dict[j][0]
			smallest_index = j

	while(process_dict[smallest_index][1] > 0):

		if(process_dict[smallest_index][0] <= time and process_dict[smallest_index][1] > 0):
			process_list.append(smallest_index+1)
			process_dict[smallest_index][1] = process_dict[smallest_index][1] - 1
			time = time + 1
			
			m = 0
			while(m < len(a)):

				#WT
				if(m != smallest_index and process_dict[m][1] > 0 and process_dict[m][0] < time):
					process_dict[m][3] = process_dict[m][3] + 1

				#TAT
				if(process_dict[m][0] <= time and process_dict[m][1] > 0):
					process_dict[m][4] = process_dict[m][4] + 1

				m = m + 1

	o = 0
	while(o < size):
		if(process_dict[o][0] == 0):
			process_dict[o][4] = process_dict[o][4] + 1
		o = o + 1

print("FCFS:",process_list)

#SJF-P

a = [0,2,4,5]
b = [7,4,1,4]
p = [4,3,2,1]
w = [0,0,0,0]
ta = [0,0,0,0]

sum_b = sum(b)
time = 0
process_list = []
size = len(a)
process_dict = dict()
i = 0
is_process_executed = 0

while (i < size):
	process_dict[i] = [a[i], b[i], p[i], w[i], ta[i], 0]
	i = i + 1

while(is_process_executed < size):

	available_dict = []
	
	for i in range(size):	
		if(process_dict[i][0] <= time and process_dict[i][1] > 0 and process_dict[i][5] == 0): 
			available_dict.append(i)
	smallest = 999

	for j in available_dict:
		if(process_dict[j][1] < smallest and process_dict[j][1] > 0 ):
			smallest = process_dict[j][1]
			smallest_index = j

	if(process_dict[smallest_index][0] <= time and process_dict[smallest_index][1] > 0):
	
		m = 0
		while(m < size):

			#WT
			if(m != smallest_index and process_dict[m][1] > 0 and process_dict[m][0] <= time):
				process_dict[m][3] = process_dict[m][3] + 1

			#TAT
			if(process_dict[m][0] <= time and process_dict[m][1] > 0):
				process_dict[m][4] = process_dict[m][4] + 1

			m = m + 1

		process_list.append(smallest_index+1)
		process_dict[smallest_index][1] = process_dict[smallest_index][1] - 1
		time = time + 1

		if(len(available_dict) == 1 and process_dict[smallest_index][1] == 0):
			process_dict[smallest_index][5] = 1
			is_process_executed = is_process_executed + 1
			
		elif(len(process_list) > 1):
			if(process_list[-2] != process_list[-1]):
				process_dict[process_list[-2]-1][5] = 1
				is_process_executed = is_process_executed + 1

		
print("SJF-P:",process_list)

#SJF-NP

a = [0,2,4,5]
b = [7,4,1,4]
p = [4,3,2,1]
w = [0,0,0,0,0]
ta = [0,0,0,0,0]

sum_b = sum(b)
time = 0
process_list = []
size = len(a)
process_dict = dict()
i = 0
next_process = 0

while (i< size):
	process_dict[i] = [a[i], b[i], p[i], w[i], ta[i], 0]
	i = i + 1

while(time < sum_b):

	available_dict = []

	for i in range(size):
		if(process_dict[i][0] <= time and process_dict[i][1] > 0 and process_dict[i][5] == 0):
			available_dict.append(i)

	if(len(process_list) == time):
		for j in range(size):
			if(process_dict[j][0] == 0):
				next_process = j
				next_process_value = process_dict[j][1]

	if(process_dict[next_process][1] > 0):
		
		m = 0
		while(m < size):

			#WT
			if(m != next_process and process_dict[m][1] > 0 and process_dict[m][0] <= time):
				process_dict[m][3] = process_dict[m][3] + 1

			#TAT
			if(process_dict[m][0] <= time and process_dict[m][1] > 0):
				process_dict[m][4] = process_dict[m][4] + 1

			m = m + 1

		process_list.append(next_process+1)
		process_dict[next_process][1] = process_dict[next_process][1] - 1
		time = time + 1


	else:
		if(process_dict[next_process][1] == 0):
			next_process_value = 999

		for o in available_dict:
			if(process_dict[o][1] < next_process_value):
				next_process_value = process_dict[o][1]
				next_process = o

		m = 0
		while(m < size):

			#WT
			if(m != next_process and process_dict[m][1] > 0 and process_dict[m][0] <= time):
				process_dict[m][3] = process_dict[m][3] + 1

			#TAT
			if(process_dict[m][0] <= time and process_dict[m][1] > 0):
				process_dict[m][4] = process_dict[m][4] + 1

			m = m + 1

		process_list.append(next_process+1)
		process_dict[next_process][1] = process_dict[next_process][1] - 1
		time = time + 1
		
print("SJF-NP:",process_list)



#Priority Preemptive

a = [0,2,5,4]
b = [7,4,5,4]
p = [4,3,1,2]
w = [0,0,0,0,0]
ta = [0,0,0,0,0]

sum_b = sum(b)
time = 0
process_list = []
size = len(a)
process_dict = dict()
i = 0

while (i<len(a)):
	process_dict[i] = [a[i], b[i], p[i], w[i], ta[i], 0]
	i = i + 1

is_process_executed = 0
while(is_process_executed < size):
	available_dict = []

	for i in range(len(a)):
		if(process_dict[i][0] <= time and process_dict[i][1] > 0 and process_dict[i][5] == 0):
			available_dict.append(i)
	
	smallest = 999
	for j in available_dict:
		if(process_dict[j][2] < smallest and process_dict[j][1] > 0 ):
			smallest = process_dict[j][2]
			smallest_index = j

	if(process_dict[smallest_index][0] <= time and process_dict[smallest_index][1] > 0):
		
		
		m = 0
		while(m < len(a)):

			#WT
			if(m != smallest_index and process_dict[m][1] > 0 and process_dict[m][0] <= time):
				process_dict[m][3] = process_dict[m][3] + 1

			#TAT
			if(process_dict[m][0] <= time and process_dict[m][1] > 0):
				process_dict[m][4] = process_dict[m][4] + 1

			m = m + 1

		process_list.append(smallest_index+1)
		process_dict[smallest_index][1] = process_dict[smallest_index][1] - 1
		time = time + 1

		if(len(available_dict) == 1 and process_dict[smallest_index][1] == 0):
			process_dict[smallest_index][5] = 1
			is_process_executed = is_process_executed + 1
			
		elif(len(process_list) > 1):
			if(process_list[-2] != process_list[-1]):
				process_dict[process_list[-2]-1][5] = 1
				is_process_executed = is_process_executed + 1

print("P-P:",process_list)

#Priority Non Preemptive

a = [0,2,4,5]
b = [7,4,1,4]
p = [4,3,2,1]
w = [0,0,0,0,0]
ta = [0,0,0,0,0]

sum_b = sum(b)
time = 0
process_list = []
size = len(a)
process_dict = dict()
i = 0

while (i<len(a)):
	process_dict[i] = [a[i], b[i], p[i], w[i], ta[i], 0]
	i = i + 1
while(time < sum_b):
	available_dict = []

	for i in range(len(a)):
		if(process_dict[i][0] <= time and process_dict[i][1] > 0):
			available_dict.append(i)
	
	smallest = 999
	for j in available_dict:
		if(process_dict[j][2] < smallest and process_dict[j][1] > 0 ):
			smallest = process_dict[j][2]
			smallest_index = j

	if(process_dict[smallest_index][0] <= time and process_dict[smallest_index][1] > 0):
		
		m 
		while(m < len(a)):

			#WT
			if(m != smallest_index and process_dict[m][1] > 0 and process_dict[m][0] <= time):
				process_dict[m][3] = process_dict[m][3] + 1

			#TAT
			if(process_dict[m][0] <= time and process_dict[m][1] > 0):
				process_dict[m][4] = process_dict[m][4] + 1

			m = m + 1

		process_list.append(smallest_index+1)
		process_dict[smallest_index][2] = 0
		process_dict[smallest_index][1] = process_dict[smallest_index][1] - 1
		time = time + 1

		


print("P-NP:",process_list)

#Round Robin
a = [0,2,4,5]
b = [7,4,1,4]
p = [4,3,2,1]
w = [0, 0, 0, 0]
ta = [0, 0, 0, 0]
time = 0

process_list = []
process_dict = dict()
sum_b = sum(b)
size = len(a)

i = 0
while (i<len(a)):
	process_dict[i] = [a[i], b[i],p[i], w[i], ta[i], 0]
	i = i + 1

time = 0
quantum_time = 3
is_process_executed = 0

while(is_process_executed != size):
	available_dict = []
	for i in range(size):
		if(process_dict[i][0] <= time and process_dict[i][1] > 0 and process_dict[i][5] == 0):
			available_dict.append(i)

	smallest = 999
	for j in available_dict:
		if(process_dict[j][2] < smallest and process_dict[j][1] > 0 ):
			smallest = process_dict[j][2]
			smallest_index = j

	l = 0
	while (l < quantum_time):
		if(process_dict[smallest_index][0] <= time and process_dict[smallest_index][1] > 0):
			m = 0
			while(m < size-1):

				#WT
				if(m != smallest_index and process_dict[m][1] > 0 and process_dict[m][0] <= time):
					process_dict[m][3] = process_dict[m][3] + 1

				#TAT
				if(process_dict[m][0] <= time and process_dict[m][1] > 0):
					process_dict[m][4] = process_dict[m][4] + 1

				m = m + 1

			process_list.append(smallest_index+1)
			process_dict[smallest_index][1] = process_dict[smallest_index][1] - 1
			time = time + 1

			if(l == quantum_time-1):
				process_dict[smallest_index][5] = 1
				is_process_executed = is_process_executed + 1

			if(process_dict[smallest_index][1] == 0):
				process_dict[smallest_index][5] = 1
				is_process_executed = is_process_executed + 1

		l = l + 1

print("RR:",process_list)

