#Ambata, Jo Simon V.
#OL158 - 2018100711


import os
from prettytable import PrettyTable


def FirstComeFirstServe(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time):

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
	print(process_dict)
	#check on what algorithm thereas
	algorithm_count = algorithm_count + 1
		
	#update parameters
	updated_b = []
	updated_p = []
	updated_w = []
	updated_ta = []

	z = 0
	while(z < len(a)):
		updated_b.append(process_dict[z][1])
		updated_p.append(process_dict[z][2])
		updated_w.append(process_dict[z][3])
		updated_ta.append(process_dict[z][4])
		z = z + 1


	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)

	
	
def ShortestJobFirstP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time):
	#SJF-P
	
	sum_b = sum(b)
	process_list = []
	size = len(a)
	process_dict = dict()
	i = 0
	is_process_executed = 0

	while (i < size):
		process_dict[i] = [a[i], b[i], p[i], w[i], ta[i], 0]
		i = i + 1

	remaining_process = 0
	for process_unfinished in range(len(a)):
		if(process_dict[process_unfinished][1] > 0):
			remaining_process = remaining_process + 1

	while(is_process_executed < remaining_process):
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

			condition = False

			for w in range(len(available_dict)):
				if(process_dict[w][1] == 0):
					process_dict[w][5] = 1

			for v in range(len(available_dict)):		
				if(process_dict[v][5] == 1):
					condition = True
				else:
					condition = False
					break

			if(condition == True):
				break


			
	print("SJF-P:",process_list)
	#check on what algorithm thereas
	algorithm_count = algorithm_count + 1
		
	#update parameters
	updated_b = []
	updated_p = []
	updated_w = []
	updated_ta = []

	z = 0
	while(z < len(a)):
		updated_b.append(process_dict[z][1])
		updated_p.append(process_dict[z][2])
		updated_w.append(process_dict[z][3])
		updated_ta.append(process_dict[z][4])
		z = z + 1


	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)

	
	
def ShortestJobFirstNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time):
	#SJF-NP
	sum_b = sum(b)
	process_list = []
	size = len(a)
	process_dict = dict()
	i = 0
	next_process = 0
	lowest_burst_time = 999
	while (i< size):
		process_dict[i] = [a[i], b[i], p[i], w[i], ta[i], 0]
		i = i + 1

	if(len(process_list) == time):
		for j in range(size):
			if(process_dict[j][0] == time):
				next_process = j
				next_process_value = process_dict[j][1]
	else:
		for h in range(size):
			if(process_dict[h][1] > 0 and process_dict[h][1] < lowest_burst_time):
				lowest_burst_time = process_dict[h][1]
				next_process = h
	while(time < completion_time):

		available_dict = []

		for i in range(size):
			if(process_dict[i][0] <= time and process_dict[i][1] > 0 and process_dict[i][5] == 0):
				available_dict.append(i)

		
		
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
	#check on what algorithm thereas
	algorithm_count = algorithm_count + 1

	#update parameters
	updated_b = []
	updated_p = []
	updated_w = []
	updated_ta = []

	z = 0
	while(z < len(a)):
		updated_b.append(process_dict[z][1])
		updated_p.append(process_dict[z][2])
		updated_w.append(process_dict[z][3])
		updated_ta.append(process_dict[z][4])
		z = z + 1


	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)

	
	
def PriorityP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time):
	#Priority Preemptive

	sum_b = sum(b)
	process_list = []
	size = len(a)
	process_dict = dict()
	i = 0

	while (i<len(a)):
		process_dict[i] = [a[i], b[i], p[i], w[i], ta[i], 0]
		i = i + 1

	is_process_executed = 0

	remaining_process = 0
	for process_unfinished in range(len(a)):
		if(process_dict[process_unfinished][1] > 0):
			remaining_process = remaining_process + 1

	while(is_process_executed < remaining_process):
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

			condition = False

			for w in range(len(available_dict)):
				if(process_dict[w][1] == 0):
					process_dict[w][5] = 1

			for v in range(len(available_dict)):		
				if(process_dict[v][5] == 1):
					condition = True
				else:
					condition = False
					break

			if(condition == True):
				break

	print("P-P:",process_list)
	#check on what algorithm thereas
	algorithm_count = algorithm_count + 1
		
	#update parameters
	updated_b = []
	updated_p = []
	updated_w = []
	updated_ta = []

	z = 0
	while(z < len(a)):
		updated_b.append(process_dict[z][1])
		updated_p.append(process_dict[z][2])
		updated_w.append(process_dict[z][3])
		updated_ta.append(process_dict[z][4])
		z = z + 1


	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)

	
	

def PriorityNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time):
	#Priority Non Preemptive

	sum_b = sum(b)
	process_list = []
	size = len(a)
	process_dict = dict()
	i = 0

	while (i<len(a)):
		process_dict[i] = [a[i], b[i], p[i], w[i], ta[i], 0]
		i = i + 1
	while(time < completion_time):
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
			process_dict[smallest_index][2] = 0
			process_dict[smallest_index][1] = process_dict[smallest_index][1] - 1
			time = time + 1

			


	print("P-NP:",process_list)
	#check on what algorithm thereas
	algorithm_count = algorithm_count + 1

	#update parameters
	updated_b = []
	updated_p = []
	updated_w = []
	updated_ta = []

	z = 0
	while(z < len(a)):
		updated_b.append(process_dict[z][1])
		updated_p.append(process_dict[z][2])
		updated_w.append(process_dict[z][3])
		updated_ta.append(process_dict[z][4])
		z = z + 1


	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)

	
	
def RoundRobin(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time):
	#Round Robin
	process_list = []
	process_dict = dict()
	sum_b = sum(b)
	size = len(a)
	i = 0
	is_process_executed = 0
	remaining_process = 0
	past_process = []
	sum_executed = 0
	exception_handling_list = []

	while (i<len(a)):
		process_dict[i] = [a[i], b[i],p[i], w[i], ta[i], 0]
		i = i + 1
	
	while(is_process_executed <= remaining_process):

		
		available_dict = []

		i = 0
		while(i < size):
			if(process_dict[i][0] <= time and process_dict[i][1] > 0 and process_dict[i][5] == 0):
				available_dict.append(i)
				past_process.append(i)
			i = i + 1


		smallest = 999
		for j in available_dict:
			if(process_dict[j][2] < smallest and process_dict[j][1] > 0 and process_dict[j][5] == 0):
				smallest = process_dict[j][2]
				smallest_index = j

		l = 0
		#exception_handling_list = process_list
		while (l < quantum_time):
			if(process_dict[smallest_index][0] <= time and process_dict[smallest_index][1] > 0 and process_dict[smallest_index][5] == 0):
				m = 0
				while(m < size):

					#WT
					if(m != smallest_index and process_dict[m][1] > 0 and process_dict[m][0] <= time):
						process_dict[m][3] = process_dict[m][3] + 1

					#TAT
					if(process_dict[m][0] <= time and process_dict[m][1] > 0):
						process_dict[m][4] = process_dict[m][4] + 1

					m = m + 1

				
				#print("EX:",exception_handling_list)

				process_list.append(smallest_index+1)
				process_dict[smallest_index][1] = process_dict[smallest_index][1] - 1
				time = time + 1
				#print("PL:",process_list)
				if(l == (quantum_time-1)):
					process_dict[smallest_index][5] = 1
					is_process_executed = is_process_executed + 1

				if(process_dict[smallest_index][1] == 0):
					process_dict[smallest_index][5] = 1
					is_process_executed = is_process_executed + 1 

			l = l + 1
	
		i=0
		while(i < size):
			if(process_dict[i][0] <= time and process_dict[i][1] > 0 and process_dict[i][5] == 0):
				available_dict.append(i)
			i = i + 1

		if(len(available_dict) > 1):
			if (available_dict[-1]+1 not in past_process ): #and available_dict[-1] + 1 not in process_list
				for x in available_dict:
					if(process_dict[x][5] == 0 and process_dict[x][0] <= time):
						remaining_process = remaining_process + 1

		condition = False

		for w in range(size):
			if(process_dict[w][1] == 0):
				process_dict[w][5] = 1

		for v in range(size):		
			if(process_dict[v][5] == 1):
				condition = True
			else:
				condition = False
				break

		if(condition == True):
			break

	print("RR:",process_list)

	#check on what algorithm thereas
	algorithm_count = algorithm_count + 1

	#update parameters
	updated_b = []
	updated_p = []
	updated_w = []
	updated_ta = []

	z = 0
	while(z < len(a)):
		updated_b.append(process_dict[z][1])
		updated_p.append(process_dict[z][2])
		updated_w.append(process_dict[z][3])
		updated_ta.append(process_dict[z][4])
		z = z + 1


	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time)
	
	
def FirstAlgorithm(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time):

	#First Queue
	if(algorithm_first == 1):
		FirstComeFirstServe(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_first == 2):
		ShortestJobFirstP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_first == 3):
		ShortestJobFirstNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_first == 4):
		PriorityP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_first == 5):
		PriorityNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_first == 6):
		quantum_time = 2
		RoundRobin(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)

def SecondAlgorithm(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time):
	#Second Queue
	if(algorithm_second == 1):
		FirstComeFirstServe(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_second == 2):
		ShortestJobFirstP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_second == 3):
		ShortestJobFirstNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_second == 4):
		PriorityP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_second == 5):
		PriorityNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_second == 6):
		quantum_time = 1
		RoundRobin(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)

def ThirdAlgorithm(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time):
	#Third Queue
	if(algorithm_third == 1):
		FirstComeFirstServe(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_third == 2):
		ShortestJobFirstP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_third == 3):
		ShortestJobFirstNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_third == 4):
		PriorityP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_third == 5):
		PriorityNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)
	if(algorithm_third == 6):
		RoundRobin(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)

#initialization
a = [0,2,4,5]
b = [7,4,1,4]
p = [4,3,2,1]
w = [0,0,0,0]
ta = [0,0,0,0]
quantum_time = 2
time = 0

completion_time = sum(b)
algorithm_first = 6
	#quantum_time = 1
algorithm_second = 6
	#quantum_time = 2
algorithm_third = 3

algorithm_count = 0




FirstAlgorithm(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time)