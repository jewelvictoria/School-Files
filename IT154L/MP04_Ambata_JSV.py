#Ambata, Jo Simon V.
#OL158 - 2018100711


import os
from prettytable import PrettyTable


def FirstComeFirstServe(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):

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

	#print("FCFS:",process_list)
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

	final_process_list = final_process_list + process_list
	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 3):
		Finalization(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	
	
def ShortestJobFirstP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):
	#SJF-P
	
	sum_b = sum(b)
	process_list = []
	size = len(a)
	process_dict = dict()
	past_process = []
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
				past_process.append(smallest_index)
				is_process_executed = is_process_executed + 1
				
			elif(len(process_list) > 1):
				if(process_list[-2] != process_list[-1]):
					process_dict[process_list[-2]-1][5] = 1
					is_process_executed = is_process_executed + 1

		condition = False

		for u in range(len(past_process)):
			if(process_dict[u][1] == 0):
				process_dict[u][5] = 1

		for v in range(len(past_process)):		
			if(process_dict[v][5] == 1):
				condition = True
			else:
				condition = False
				break

		if(condition == True):
			break
			
	#print("SJF-P:",process_list)
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

	final_process_list = final_process_list + process_list
	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 3):
		Finalization(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	
	
def ShortestJobFirstNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):
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

	#print(sum_b)
	#print(len(final_process_list))
	#print("HELLLOOOOOOOOO")
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
	#print(process_dict)		
	#print("SJF-NP:",process_list)
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

	final_process_list = final_process_list + process_list

	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 3):
		Finalization(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	
	
def PriorityP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):
	#Priority Preemptive

	sum_b = sum(b)
	process_list = []
	size = len(a)
	process_dict = dict()
	i = 0
	past_process = []

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
				past_process.append(smallest_index)
				
			elif(len(process_list) > 1):
				if(process_list[-2] != process_list[-1]):
					process_dict[process_list[-2]-1][5] = 1
					is_process_executed = is_process_executed + 1


			
		condition = False

		for u in range(len(past_process)):
			if(process_dict[u][1] == 0):
				process_dict[u][5] = 1

		for v in range(len(past_process)):		
			if(process_dict[v][5] == 1):
				condition = True
			else:
				condition = False
				break

		if(condition == True):
			break

			

	#print("P-P:",process_list)
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

	final_process_list = final_process_list + process_list

	

	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 3):
		Finalization(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	
	
def PriorityNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):
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

			


	#print("P-NP:",process_list)

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

	final_process_list = final_process_list + process_list

	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 3):
		Finalization(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	
	
def RoundRobin(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):
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
	smallest_index = 0

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

		for u in range(size):
			if(process_dict[u][1] == 0):
				process_dict[u][5] = 1

		for v in range(size):		
			if(process_dict[v][5] == 1):
				condition = True
			else:
				condition = False
				break

		if(condition == True):
			break

	#print("RR:",process_list)
	
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


	final_process_list = final_process_list + process_list

	if(algorithm_count == 1):
		SecondAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 2):
		ThirdAlgorithm(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_count == 3):
		Finalization(a, updated_b, updated_p, updated_w, updated_ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	

def FirstAlgorithm(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):

	#First Queue
	if(algorithm_first == 1):
		FirstComeFirstServe(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_first == 2):
		ShortestJobFirstP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_first == 3):
		ShortestJobFirstNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_first == 4):
		PriorityP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_first == 5):
		PriorityNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_first == 6):
		quantum_time = QT_FirstAlgorithm
		RoundRobin(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)

def SecondAlgorithm(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):
	#Second Queue
	if(algorithm_second == 1):
		FirstComeFirstServe(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_second == 2):
		ShortestJobFirstP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_second == 3):
		ShortestJobFirstNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_second == 4):
		PriorityP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_second == 5):
		PriorityNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_second == 6):
		quantum_time = QT_SecondAlgorithm
		RoundRobin(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)

def ThirdAlgorithm(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):
	#Third Queue
	if(algorithm_third == 1):
		FirstComeFirstServe(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_third == 2):
		ShortestJobFirstP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_third == 3):
		ShortestJobFirstNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_third == 4):
		PriorityP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_third == 5):
		PriorityNP(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)
	if(algorithm_third == 6):
		quantum_time = QT_ThirdAlgorithm
		RoundRobin(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)


def Finalization(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm):
	#Finalization
	print("\nFinal Process List:",final_process_list)

	print("\n\nTable: ")
	size = len(a)
	from prettytable import PrettyTable

	table = PrettyTable(['PROCESS', 'TURNAROUND TIME', 'WAITING TIME'])
	o = 0
	total_waiting = 0
	total_turnaround = 0
	while (o < size):
		table.add_row(['P{}'.format(o+1), ta[o], w[o]])
		total_waiting = total_waiting + w[o]
		total_turnaround = total_turnaround + ta[o]
		o = o + 1

	total_TAT =  total_turnaround
	total_WT = total_waiting
	ave_TAT = total_turnaround/size
	ave_WT = total_waiting/size

	total_TAT = round(total_TAT,3)
	total_WT = round(total_WT,3)
	ave_TAT = round(ave_TAT,3)
	ave_WT = round(ave_WT,3)

	table.add_row(['TOTAL:', total_TAT, total_WT])
	table.add_row(['AVERAGE', ave_TAT, ave_WT])
	print(table)


#Global Declaration
a = []
b = []
p = []
w = []
ta = []

algorithm_first = 0
algorithm_second = 0
algorithm_third = 0
algorithm_count = 0
final_process_list = []

def main():
	#read data file
	check = open("MP04_check.txt","r")
	readValues = check.read()
	values = []
	for y in readValues.split('\n'):
		if y.isdigit():
			values.append(int(y))
	size = values[0]


	#declare list
	a = []
	b = []
	p = []
	w = []
	ta = []
	time = 0
	quantum_time = 0	
	completion_time = 0
	algo = [0,0,0]
	QT = [0,0,0]
	i = 0

	#other declarations
	#Global Declaration
	a = []
	b = []
	p = []
	w = []
	ta = []

	algorithm_first = 0
	algorithm_second = 0
	algorithm_third = 0
	algorithm_count = 0
	final_process_list = []

	#Quantum Time
	QT_FirstAlgorithm = 0
	QT_SecondAlgorithm = 0
	QT_ThirdAlgorithm = 0

	#Adjusting List Size
	while (i < size):
		a.append(0)
		b.append(0)
		p.append(0)
		w.append(0)
		ta.append(0)
		#qNum.append(0)
		i = i + 1

	i = 0
	while (i < size):
		a[i] = values[i + 1]
		i = i + 1

	j = 0
	for i in range(size):
		b[j]= values[i+size+1]
		i = i+1
		j = j+1

	j = 0
	for i in range(size):
		p[j] = values[i+size+size+1]
		i = i + 1
		j = j + 1
	
	j = 0
	h = 0
	for i in range(3):
		algo[i] = values [(size*3) + 1 + j]
		if (algo[i] == 6):
			QT[h] = values [(size*3) + 1 + j + 1]
			j = j + 1
			h = h + 1
		j = j + 1
	completion_time = sum(b)
	#START OUTPUT
	print ("Programmed by: Jo Simon Ambata \nMP04 - MULTILEVEL FEEDBACK QUEUE ALGORITHM \n")
	print ("Enter No. of Processes: ", size)
	print ("Arrival Time:")
	i = 0
	for i in range(size):
		print("P{}: {}".format(i+1,a[i]))
		i = i+1

	i = 0
	print ("Burst Time:")
	for i in range(size):
		print("P{}: {}".format(i+1,b[i]))
		i = i+1

	i = 0
	print ("Priority Number:")
	for i in range(size):
		print("P{}: {}".format(i+1,p[i]))
		i = i+1

	print("\nAlgorithm: ")
	print(" 1. FCFS\n 2. SJF-P\n 3. SJF-NP\n 4. P-P\n 5. P-NP\n 6. RR")
	
	i = 0
	print("\nQueue Algorithm: ")
	for i in range(3):
		print("Queue {}: {}".format(i+1,algo[i]))
		if (algo[i] == 6):
			print("\t  Q:", QT[i])
		i = i+1

	algorithm_first = algo[0]
	algorithm_second = algo[1]
	algorithm_third = algo[2]

	QT_FirstAlgorithm = QT[0]
	QT_SecondAlgorithm = QT[1]
	QT_ThirdAlgorithm = QT[2]
	

	FirstAlgorithm(a, b, p, w, ta, quantum_time, time, algorithm_count, completion_time, final_process_list, algorithm_first, algorithm_second, algorithm_third, QT_FirstAlgorithm, QT_SecondAlgorithm, QT_ThirdAlgorithm)



main()
