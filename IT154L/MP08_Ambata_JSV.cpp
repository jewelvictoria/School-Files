#include<iostream>
#include<vector>
#include<bits/stdc++.h>
#include<cstdlib> 
using namespace std;

int main(){
	//File Input
    ifstream linecount("MP08_check.txt"); //variable for line count
	ifstream input("MP08_check.txt"); //variable for getting the data
	
    //Line Count
    int num_lines = 0;
    string line;
    while (getline(linecount, line)){
    	++num_lines;
	}
    
    string data_array [num_lines];
    int index = 0;
    string in_line;
	while(getline(input, in_line)){
	    data_array[index] = in_line;
	    index = index + 1;
	}
	
	string ref_num = data_array[0];
	int length; 
	length = atoi(ref_num.c_str());
	

  	istringstream iss(data_array[2]);
  	string s;
  	int queue [length];
  	int in = 0;
  	int queue_size = 0;
  	while ( getline( iss, s, ' ' ) ) {
		if(atoi(s.c_str()) >= 0){
			queue [in] = atoi(s.c_str());
			queue_size = queue_size + 1;
		}
		else{
			break;
		}
		in = in + 1;
  	}
  	
	int cylinder_size = stoi(data_array[0]);
	int head_queue = stoi(data_array[1]);
	string queue_remove_negative = data_array[2].substr(0, data_array[2].find("-", 0));
	cout<<"Programmed by: Jo Simon V. Ambata"<<endl;
	cout<<"MP08 - Disk Scheduling"<<endl<<endl;
	cout<<"Inputs:(MP08_check.txt)"<<endl;
    cout<<"Max Cylinder Size: "<<cylinder_size<<endl;
    cout<<"Head Pointer Position: "<<head_queue<<endl;
    cout<<"Queue: "<<queue_remove_negative<<endl<<endl;
	
	//FIFO ===================================================================================================================================
	vector <int> FIFO_queue;
	FIFO_queue.push_back(head_queue);
	for (int i=0; i<queue_size; i++){
    	FIFO_queue.push_back(queue[i]);
	}
	cout<< "FIFO: ";
	for(int i=0; i < FIFO_queue.size(); i++){	
   		cout <<FIFO_queue.at(i) << " ";
	}
	cout<<endl;
	
	//SSTF ===================================================================================================================================
	//Based on the open-source code: https://japp.io/algorithms/shortest-seek-time-first-disk-scheduling-algorithm-in-c-c/
	int i,j,k,n,m,sum=0,x,y,h;
	n = queue_size;
	m = cylinder_size;
	
	vector <int> a(n),b;
	
    map <int,int> mp;
	for(i=0;i<n;i++){
        a[i] = queue[i];
        mp[a[i]]++;
    }
    
    for(i=0;i<n;i++){
        if(a[i]>m){
            cout<<"Error, Unknown position "<<a[i]<<"\n";
            return 0;
        }
    }
    h = head_queue;
    int temp=h;
    int ele;
    b.push_back(h);
    int count=0;
    while(count<n){
        //initially taking diff to be very large.
        int diff=999999;
        //traversing in map to find the least difference
        for(auto q:mp){
            if(abs(q.first-temp)<diff){
                ele=q.first;
                diff=abs(q.first-temp);
            }
        }
        //deleting the element that has the least
        //difference from the map
        mp[ele]--;
        if(mp[ele]==0){
            mp.erase(ele);
        }
        //adding that element to our output array.
        b.push_back(ele);
        temp=ele;
        count++;
    }
    //printing the output array
    
	vector<int> SSTF_queue;
    cout<<"SSTF: ";
    for(i=0;i<b.size();i++){
        SSTF_queue.push_back(b[i]);
        sum+=abs(b[i]-temp);
        temp=b[i];
    }
    for(i=0;i<SSTF_queue.size();i++){
        cout<<SSTF_queue[i]<<" ";
    }
    cout<<endl;

	//SCAN ===================================================================================================================================
	vector <int> L_scanqueue;
	vector <int> R_scanqueue;
	L_scanqueue.push_back(head_queue);
	for (int j=0; j<queue_size;j++){
		if(queue[j]<head_queue){
			L_scanqueue.push_back(queue[j]);
		}
		if(queue[j]>head_queue){
			R_scanqueue.push_back(queue[j]);
		}
	}
	
	//end of disk
	L_scanqueue.push_back(0);
	R_scanqueue.push_back(cylinder_size-1);
	
	//sort(R_scanqueue, R_scanqueue - queue_size);
	sort(R_scanqueue.begin(),R_scanqueue.end());
	sort(begin(L_scanqueue), end(L_scanqueue), greater<int>());
	
	//concatenating
	vector<int> SCAN_queue(L_scanqueue);
	SCAN_queue.insert(SCAN_queue.end(), R_scanqueue.begin(), R_scanqueue.end());
	
	cout<< "SCAN: ";
	for(int i=0; i < SCAN_queue.size(); i++){	
   		cout << SCAN_queue.at(i) << " ";
	}
	cout<< endl;
	
	//LOOK ===================================================================================================================================
	vector <int> L_lookqueue;
	vector <int> R_lookqueue;
	L_lookqueue.push_back(head_queue);
	for (int j=0; j<queue_size;j++){
		if(queue[j]<head_queue){
			L_lookqueue.push_back(queue[j]);
		}
		if(queue[j]>head_queue){
			R_lookqueue.push_back(queue[j]);
		}
	}
	
	//end of disk
	//L_lookqueue.push_back(0);
	//R_lookqueue.push_back(cylinder_size-1);
	
	//sort(R_scanqueue, R_scanqueue - queue_size);
	sort(R_lookqueue.begin(),R_lookqueue.end());
	sort(begin(L_lookqueue), end(L_lookqueue), greater<int>());
	
	//concatenating
	vector<int> LOOK_queue(L_lookqueue);
	LOOK_queue.insert(LOOK_queue.end(), R_lookqueue.begin(), R_lookqueue.end());
	cout<< "LOOK: ";
	for(int i=0; i < LOOK_queue.size(); i++){	
   		cout << LOOK_queue.at(i) << " ";
	}
	cout<< endl;
	
	//C-SCAN ===================================================================================================================================
	vector <int> L_cscanqueue;
	vector <int> R_cscanqueue;
	R_cscanqueue.push_back(head_queue);
	L_cscanqueue.push_back(0);
	for (int j=0; j<queue_size;j++){
		if(queue[j]<head_queue){
			L_cscanqueue.push_back(queue[j]);
		}
		if(queue[j]>head_queue){
			R_cscanqueue.push_back(queue[j]);
		}
	}
	
	//end of disk
	R_cscanqueue.push_back(cylinder_size-1);
	
	//sort(R_scanqueue, R_scanqueue - queue_size);
	sort(R_cscanqueue.begin(),R_cscanqueue.end());
	sort(L_cscanqueue.begin(),L_cscanqueue.end());
	
	//concatenating
	vector<int> CSCAN_queue(R_cscanqueue);
	CSCAN_queue.insert(CSCAN_queue.end(), L_cscanqueue.begin(), L_cscanqueue.end());
	cout<< "C-SCAN: ";
	for(int i=0; i < CSCAN_queue.size(); i++){	
   		cout << CSCAN_queue.at(i) << " ";
	}
	cout<< endl;
	
	//C-LOOK ===================================================================================================================================
	vector <int> L_clookqueue;
	vector <int> R_clookqueue;
	R_clookqueue.push_back(head_queue);
	//L_clookqueue.push_back(0);
	for (int j=0; j<queue_size;j++){
		if(queue[j]<head_queue){
			L_clookqueue.push_back(queue[j]);
		}
		if(queue[j]>head_queue){
			R_clookqueue.push_back(queue[j]);
		}
	}
	
	//end of disk
	//R_cscanqueue.push_back(cylinder_size-1);
	
	//sort(R_scanqueue, R_scanqueue - queue_size);
	sort(R_clookqueue.begin(),R_clookqueue.end());
	sort(L_clookqueue.begin(),L_clookqueue.end());
	
	//concatenating
	vector<int> CLOOK_queue(R_clookqueue);
	CLOOK_queue.insert(CLOOK_queue.end(), L_clookqueue.begin(), L_clookqueue.end());
	cout<< "C-LOOK: ";
	for(int i=0; i < CLOOK_queue.size(); i++){	
   		cout << CLOOK_queue.at(i) << " ";
	}
	cout<< endl;
	
	//TABLE ==================================================================================================================================
	//FIFO
	vector<int> FIFO_traversed;
	FIFO_traversed.push_back(0);
	
	int total_FIFO = 0;
	int size_FIFO = 0;
	for(int l=1; l<FIFO_queue.size(); l++){
		FIFO_traversed.push_back( abs(FIFO_queue[l] - FIFO_queue[l-1]));
	}
	
	cout<<endl<<endl<<"   FIFO"<<endl;
    cout<<"|--------------------------------------------|";
	cout <<"\n Next Track Accessed \t"<< "Next Track Traversed "<< endl;
	cout<<"|--------------------------------------------|\n";
    cout << "\t" << FIFO_queue[0]<< "\t\t\t"<<"-" <<endl;
	for (int k = 1; k < FIFO_queue.size(); k++) {
        cout << "\t" << FIFO_queue[k]<< "\t\t\t" <<FIFO_traversed[k]  << endl;
        total_FIFO = total_FIFO + FIFO_traversed[k];
		size_FIFO = size_FIFO + 1;
    }
    double FIFO_average = total_FIFO/(size_FIFO * 1.0);
    cout<<"|--------------------------------------------|"<<endl;
    cout << " Total" << "\t\t\t\t" << total_FIFO << "\t\t"<<endl;
    cout << " Average" << "\t\t\t" << FIFO_average << "\t\t"<<endl;
    cout<<"|--------------------------------------------|\n\n";
    
    //SSTF
    vector<int> SSTF_traversed;
	SSTF_traversed.push_back(0);
	
	int total_SSTF = 0;
	int size_SSTF = 0;
	for(int l=1; l<SSTF_queue.size(); l++){
		SSTF_traversed.push_back( abs(SSTF_queue[l] - SSTF_queue[l-1]));
	}
	cout<<endl<<endl<<"   SSTF"<<endl;
    cout<<"|--------------------------------------------|";
	cout <<"\n Next Track Accessed \t"<< "Next Track Traversed "<< endl;
	cout<<"|--------------------------------------------|\n";
    cout << "\t" << SSTF_queue[0]<< "\t\t\t"<<"-" <<endl;
	for (int k = 1; k < SSTF_queue.size(); k++) {
        cout << "\t" << SSTF_queue[k]<< "\t\t\t" <<SSTF_traversed[k]  << endl;
        total_SSTF = total_SSTF + SSTF_traversed[k];
		size_SSTF = size_SSTF + 1;
    }
    double SSTF_average = total_SSTF/(size_SSTF * 1.0);
    cout<<"|--------------------------------------------|"<<endl;
    cout << " Total" << "\t\t\t\t" << total_SSTF << "\t\t"<<endl;
    cout << " Average" << "\t\t\t" << SSTF_average << "\t\t"<<endl;
    cout<<"|--------------------------------------------|\n\n";
    
    //SCAN
    vector<int> SCAN_traversed;
	SCAN_traversed.push_back(0);
	
	int total_SCAN = 0;
	int size_SCAN = 0;
	for(int l=1; l<LOOK_queue.size(); l++){
		SCAN_traversed.push_back( abs(LOOK_queue[l] - LOOK_queue[l-1]));
	}
	cout<<endl<<endl<<"   SCAN"<<endl;
    cout<<"|--------------------------------------------|";
	cout <<"\n Next Track Accessed \t"<< "Next Track Traversed "<< endl;
	cout<<"|--------------------------------------------|\n";
    cout << "\t" << LOOK_queue[0]<< "\t\t\t"<<"-" <<endl;
	for (int k = 1; k < LOOK_queue.size(); k++) {
        cout << "\t" << LOOK_queue[k]<< "\t\t\t" <<SCAN_traversed[k]  << endl;
        total_SCAN = total_SCAN + SCAN_traversed[k];
		size_SCAN = size_SCAN + 1;
    }
    double SCAN_average = total_SCAN/(size_SCAN * 1.0);
    cout<<"|--------------------------------------------|"<<endl;
    cout << " Total" << "\t\t\t\t" << total_SCAN << "\t\t"<<endl;
    cout << " Average" << "\t\t\t" << SCAN_average << "\t\t"<<endl;
    cout<<"|--------------------------------------------|\n\n";
    
    //LOOK
    vector<int> LOOK_traversed;
	LOOK_traversed.push_back(0);
	
	int total_LOOK = 0;
	int size_LOOK = 0;
	for(int l=1; l<LOOK_queue.size(); l++){
		LOOK_traversed.push_back( abs(LOOK_queue[l] - LOOK_queue[l-1]));
	}
	cout<<endl<<endl<<"   LOOK"<<endl;
    cout<<"|--------------------------------------------|";
	cout <<"\n Next Track Accessed \t"<< "Next Track Traversed "<< endl;
	cout<<"|--------------------------------------------|\n";
    cout << "\t" << LOOK_queue[0]<< "\t\t\t"<<"-" <<endl;
	for (int k = 1; k < LOOK_queue.size(); k++) {
        cout << "\t" << LOOK_queue[k]<< "\t\t\t" <<LOOK_traversed[k]  << endl;
        total_LOOK = total_LOOK + LOOK_traversed[k];
		size_LOOK = size_LOOK + 1;
    }
    double LOOK_average = total_LOOK/(size_LOOK * 1.0);
    cout<<"|--------------------------------------------|"<<endl;
    cout << " Total" << "\t\t\t\t" << total_LOOK << "\t\t"<<endl;
    cout << " Average" << "\t\t\t" << LOOK_average << "\t\t"<<endl;
    cout<<"|--------------------------------------------|\n\n";
    
    //C-SCAN
    vector<int> CSCAN_traversed;
	CSCAN_traversed.push_back(0);
	
	int total_CSCAN = 0;
	int size_CSCAN = 0;
	for(int l=1; l<CLOOK_queue.size(); l++){
		CSCAN_traversed.push_back( abs(CLOOK_queue[l] - CLOOK_queue[l-1]));
	}
	cout<<endl<<endl<<"   C-SCAN"<<endl;
    cout<<"|--------------------------------------------|";
	cout <<"\n Next Track Accessed \t"<< "Next Track Traversed "<< endl;
	cout<<"|--------------------------------------------|\n";
    cout << "\t" << CLOOK_queue[0]<< "\t\t\t"<<"-" <<endl;
	for (int k = 1; k < CLOOK_queue.size(); k++) {
        cout << "\t" << CLOOK_queue[k]<< "\t\t\t" <<CSCAN_traversed[k]  << endl;
        total_CSCAN = total_CSCAN + CSCAN_traversed[k];
		size_CSCAN = size_CSCAN + 1;
    }
    double CSCAN_average = total_CSCAN/(size_CSCAN * 1.0);
    cout<<"|--------------------------------------------|"<<endl;
    cout << " Total" << "\t\t\t\t" << total_CSCAN << "\t\t"<<endl;
    cout << " Average" << "\t\t\t" << CSCAN_average << "\t\t"<<endl;
    cout<<"|--------------------------------------------|\n\n";
    
    //C-LOOK
    vector<int> CLOOK_traversed;
	CLOOK_traversed.push_back(0);
	
	int total_CLOOK = 0;
	int size_CLOOK = 0;
	for(int l=1; l<LOOK_queue.size(); l++){
		CLOOK_traversed.push_back( abs(CLOOK_queue[l] - CLOOK_queue[l-1]));
	}
	cout<<endl<<endl<<"   C-LOOK"<<endl;
    cout<<"|--------------------------------------------|";
	cout <<"\n Next Track Accessed \t"<< "Next Track Traversed "<< endl;
	cout<<"|--------------------------------------------|\n";
    cout << "\t" << CLOOK_queue[0]<< "\t\t\t"<<"-" <<endl;
	for (int k = 1; k < CLOOK_queue.size(); k++) {
        cout << "\t" << CLOOK_queue[k]<< "\t\t\t" <<CLOOK_traversed[k]  << endl;
        total_CLOOK = total_CLOOK + CLOOK_traversed[k];
		size_CLOOK = size_CLOOK + 1;
    }
    double CLOOK_average = total_CLOOK/(size_CLOOK * 1.0);
    cout<<"|--------------------------------------------|"<<endl;
    cout << " Total" << "\t\t\t\t" << total_CLOOK << "\t\t"<<endl;
    cout << " Average" << "\t\t\t" << CLOOK_average << "\t\t"<<endl;
    cout<<"|--------------------------------------------|\n\n";
    
    
    
    
    
}