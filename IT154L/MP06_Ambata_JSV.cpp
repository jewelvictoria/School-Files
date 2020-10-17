//Ambata, Jo Simon V.
//OL158 - 2018100711

#include <iostream>
#include <string> 
#include <iomanip>
#include <sstream>
#include <vector>
#include <string>
#include <bits/stdc++.h> 
#include <fstream>
#include <cstdlib>

using namespace std;
void initializeTableVector(vector<string> &table, int frameSize);
void addEmptyFrameTableVector(vector<string> &table, int frameSize);
void addFrameTableVector(vector<string> &table, int frameSize, int frameArray []);
void printTable(vector<string> &table, string topString, int referenceStringSize, int frameSize);
void mainProcess();

ofstream efe;
int main(){
	//File Input
    ifstream linecount("MP06_check.txt"); //variable for line count
	ifstream input("MP06_check.txt"); //variable for getting the data
	
    //Line Count
    /*
    Notes:
    string_size
    frame_size
    ref_array[0-string_size]
    */
    
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
	

  	istringstream iss(data_array[1]);
  	string s;
  	int ref_array [length];
  	int in = 0;
  	while ( getline( iss, s, ' ' ) ) {
		ref_array[in] = atoi(s.c_str());
		in = in + 1;
  	}
  	
	int string_size = stoi(data_array[0]);
	int frame_size = stoi(data_array[2]);
	efe.open ("MP06_check.txt");
	efe << string_size<<endl;
	efe << data_array[1]<<endl;
	efe << frame_size<<endl<<endl; 
	mainProcess();
}
void mainProcess()
{	
			cout << "Programmed by: Jo Simon V. Ambata" << endl
	    	<< "MP06 - OPTIMAL Page Replacement" << endl<< endl << endl;
	    	
    		bool tryAgain;
			do
			{
				
		tryAgain = true;
		int reference_stringsize;
		int frameSize;
		int* frameArray;
		int* reference_nums;
		int* arrivalTime;
		int pageFaults = 0;
		string referenceString;
		string *reference_stringarray;
		string topString = "";
		
		//File Input
	    ifstream linecount("MP06_check.txt"); //variable for line count
		ifstream input("MP06_check.txt"); //variable for getting the data
		
	    //Line Count
	    /*
	    Notes:
	    string_size
	    frame_size
	    ref_array[0-string_size]
	    */
	    
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
		
	
	  	istringstream iss(data_array[1]);
	  	string s;
	  	int ref_array [length];
	  	int in = 0;
	  	while ( getline( iss, s, ' ' ) ) {
			ref_array[in] = atoi(s.c_str());
			in = in + 1;
	  	}
	  	
		int string_size = stoi(data_array[0]);
		int frame_size = stoi(data_array[2]);
		try
		{
			reference_stringsize = string_size;
			cout << "enter reference string size: "<<reference_stringsize<<endl;
			
			if(reference_stringsize <= 0)
			{
				throw reference_stringsize;
			}
			cout << "enter reference string:  ";
		
			referenceString = data_array[1];
			
			
			if(referenceString.length() != reference_stringsize + (reference_stringsize-1))
			{
				throw reference_stringsize;
			}
			cout << referenceString << endl;
			
			cout << "frame Size: "<<frame_size<<endl<<endl;
			frameSize = frame_size;
			if(frameSize <= 0)
			{
				throw frameSize;
			}
			efe << "Programmed by: Jo Simon V. Ambata" << endl;
		    efe << "MP06 - OPTIMAL Page Replacement" << endl << endl;
		    efe << "enter reference string size: "<<reference_stringsize<<endl;
			efe << "enter reference string:  "<<referenceString<<endl;
			efe << "frame Size: "<<frame_size<<endl<<endl;
		}
		
		
	    
		catch(int e)
		{
			cout <<  endl << "Something went wrong with the input process please try again " << endl;
			efe << endl << "Something went wrong with the input process please try again " << endl;
			cin.clear();
			fflush(stdin);
			system("PAUSE");
		}

		frameArray = new int[frameSize];
		arrivalTime = new int[frameSize];
		reference_nums = new int[reference_stringsize];
		reference_stringarray = new string[reference_stringsize];
		for(int i =0;i<frameSize;i++)
		{
			frameArray[i] = -1;
		}
		int currentNum=0;
		for(int i=0;i < reference_stringsize*2-1;i+=2)
		{
			reference_stringarray[currentNum] = referenceString[i];
			currentNum++;
			if(currentNum == reference_stringsize)
			{
				break;
			}
		}
		for(int i=0;i<reference_stringsize;i++)
		{
			topString += reference_stringarray[i];
			topString += "   ";
		}
		
		for(int i =0;i <reference_stringsize;i++)
		{
			stringstream ss(reference_stringarray[i]);
			ss >> reference_nums[i];
			ss.clear();
		}
		
		vector<string> table;
		vector<int> notInReferenceAnymore;
		vector<int> notInReferenceAnymoreArrivalTime;
		
		initializeTableVector(table, frameSize);

		int runtime =-1;
		bool emptySpotFound;
		bool same;
		bool stillInTheReference;
		for(int i =0;i < reference_stringsize;i++)
		{
			runtime++;
			same = false;
			emptySpotFound= false;
			for(int j =0;j <frameSize;j++)
			{
				if(reference_nums[i] == frameArray[j])
				{
					same = true;
				}
			}
			if(!same)
			{
				for(int j=0;j<frameSize;j++)
				{
					if(frameArray[j]==-1)
					{
						emptySpotFound = true;
						break;
					}
				}
				if(!emptySpotFound)
				{
					if(i < reference_stringsize-1)
					{
						for(int k=0;k<frameSize;k++)
						{
							stillInTheReference = false;
							for(int l = i;l<reference_stringsize;l++)
							{
								if(frameArray[k] == reference_nums[l])
								{
									stillInTheReference=true;
									break;
								}
							}
							if(!stillInTheReference)
							{
								 notInReferenceAnymore.push_back(frameArray[k]);
								 notInReferenceAnymoreArrivalTime.push_back(arrivalTime[k]);
							}
						}
						if(notInReferenceAnymore.size() > 0)
						{
							int lowestArrivalTime = 10000000;
							for(int o = 0;o<notInReferenceAnymore.size();o++)
							{
								if(notInReferenceAnymoreArrivalTime[o] < lowestArrivalTime)
								{
									lowestArrivalTime = notInReferenceAnymoreArrivalTime[o];
								}
							}
							for(int j = 0;j<frameSize;j++)
							{
								if(arrivalTime[j] == lowestArrivalTime)
								{
									frameArray[j] = reference_nums[i];
									arrivalTime[j] = runtime;
								}
							}
							pageFaults++;
							addFrameTableVector(table, frameSize, frameArray);
						}
						else 
						{
							int largestDistance = -10000;
							int largestDistanceNumber;
							for(int k=0;k<frameSize;k++)
							{
								for(int l=i+1;l < reference_stringsize;l++)
								{
									if(frameArray[k] == reference_nums[l])
									{
										if(l > largestDistance)
										{
											largestDistance = l;
											largestDistanceNumber = frameArray[k];
										}
										break;
									}
								}
							}
							
							for(int k =0; k<frameSize;k++)
							{
								if(frameArray[k] == largestDistanceNumber)
								{
									frameArray[k] = reference_nums[i];
									arrivalTime[k] = runtime;
								}
							}
							pageFaults++;
							addFrameTableVector(table, frameSize, frameArray);
						}
					} 
					else
					{
						int lowestArrivalTime = 10000000;
						
						for(int p=0;p<frameSize;p++)
						{
							if(arrivalTime[p] < lowestArrivalTime)
							{
								lowestArrivalTime = arrivalTime[p];
							}
						}
						
						for(int j = 0;j<frameSize;j++)
						{
							if(arrivalTime[j] == lowestArrivalTime)
							{
								frameArray[j] = reference_nums[i];
								arrivalTime[j] = runtime;
							}
						}
						pageFaults++;
						addFrameTableVector(table, frameSize, frameArray);
					}
				}
				else if(emptySpotFound)
				{
					for(int j=0;j<frameSize;j++)
					{
						if(frameArray[j]==-1)
						{
							frameArray[j]=reference_nums[i];
							arrivalTime[j]=runtime;
							break;
						}
					}
					addFrameTableVector(table, frameSize, frameArray);
					pageFaults++;
				}
			}
			else if(same)
			{
				addEmptyFrameTableVector(table, frameSize);
			}
			notInReferenceAnymore.clear();
			notInReferenceAnymoreArrivalTime.clear();
		}
		printTable(table, topString, reference_stringsize, frameSize);
		string answer;
		cout << endl << endl << endl << "Page Faults: " << pageFaults << endl;
		efe << endl << endl << endl << "Page Faults: " << pageFaults << endl;
		//Resets and delete dynamic arrays to prevent memory leaks
		delete [] frameArray;
		delete [] reference_nums;
		delete [] arrivalTime;
		delete [] reference_stringarray;
		table.clear();
		notInReferenceAnymore.clear();
		notInReferenceAnymoreArrivalTime.clear();
		do
			{
			cin.clear();
			fflush(stdin);
			cout << "Do you want to run again? [y/n]: ";
			cin >> answer;
			efe << "Do you want to run again? [y/n]: "<<answer<<endl<<endl;
			if(answer == "N" || answer == "n")
			{
				tryAgain = false;
			}
		}while(answer!="N" && answer!= "n" && answer!="y" && answer !="Y");
		

	}while(tryAgain);
}

void initializeTableVector(vector<string> &table, int frameSize)
{
	table.push_back(" ");
	table.push_back(" ");
	table.push_back(" ");
	for(int i =0;i<frameSize-1;i++)
	{
		table.push_back(" ");
		table.push_back(" ");
	}
}

void addFrameTableVector(vector<string> &table, int frameSize, int frameArray [])
{
	stringstream ss;
	table[0]+="--- ";
	table[1]+="|";
	ss << frameArray[0];
	table[1]+=ss.str();
	table[1]+="| ";
	ss.str("");
	table[2]+="--- ";
	int currentFrame = 1;
	for(int i =3;i<=frameSize*2;i++)
	{
		if(i%2==0)
		{
			table[i]+="--- ";
		}
		else
		{
			if(frameArray[currentFrame]!=-1)
			{
				table[i]+="|";
				ss << frameArray[currentFrame];
				table[i]+=ss.str();
				table[i]+="| ";
				ss.str("");
				currentFrame++;
			}
			else
			{
				table[i]+="| | ";
			}
		}
	}
}

void addEmptyFrameTableVector(vector<string> &table, int frameSize)
{
	table[0]+="--- ";
	table[1]+="| | ";
	table[2]+="--- ";
	for(int i =3;i<=frameSize*2;i++)
	{
		if(i%2==0)
		{
			table[i]+="--- ";
		}
		else
		{
			table[i]+="| | ";
		}
	}
}

void printTable(vector<string> &table, string topString, int reference_stringsize, int frameSize)
{
	if(reference_stringsize <= 20)
	{
		cout << topString << endl;
		efe << topString << endl;
		for(int i=0;i<table.size();i++)
		{
			cout << table[i] << endl;
			efe <<table[i] << endl;
		}
	}
	else
	{
		bool complete = false;
		int topStringProcess = 0;
		int tableProcess = 0;
		while(!complete)
		{
			for(int i =0;i < 80;i++)
			{
				cout << topString[topStringProcess];
				efe << topString[topStringProcess];
				topStringProcess++;
				if(topStringProcess>=reference_stringsize*4)
				{
					complete = true;
					break;
				}
			}
			cout << endl;
			efe << endl;
			for(int i =0;i<table.size();i++)
			{
				for(int j=tableProcess;j<tableProcess+80;j++)
				{
					cout << table[i][j];
					efe << table[i][j];
					if(j >= reference_stringsize*4)
					{
						complete = true;
						break;
					}
				}
				cout << endl;
				efe << endl;
			}
			tableProcess +=80;
		}
	}

}
