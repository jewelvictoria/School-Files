//Ambata, Jo Simon V.
//OL158 - 2018100711

#include <iostream>
#include <time.h>
#include <cstdlib>
#include <fstream>
#include <sstream>

using namespace std;


int need[100][100], allot[100][100],maximum[100][100],available[100],allotA[100][100];
bool isFinished[100];
int sequence[100];
void isSafe(int N, int M);
void student_information();
void askUser();
void mainProcess();

ofstream efe;

	
void student_information(){
    cout << "Programmed by: Jo Simon V. Ambata" << endl;
    cout << "MP05 - BANKER'S ALGORITHM" << endl << endl;
}


void isSafe(int N, int M){
        int i,j,work[100],count=0;
        for(i=0;i<M;i++)
            work[i]=available[i];
        for(i=0;i<100;i++)
            isFinished[i]=false;

        while(count<N)
        {
                bool canAllot=false;
                for(i=0;i<N;i++)
                {
                   if(isFinished[i]==false)
                   {

                        for(j=0;j<M;j++)
                        {
                            if(work[j]<need[i][j])
                            {
                                break;
                            }
                        }
                        if(j==M)
                        {
                            for(j=0;j<M;j++)
                            {
                                work[j]+=allot[i][j];
                            }

                            sequence[count++]=i;
                            isFinished[i]=true;
                            canAllot=true;
                        }
                   }
                }
                if(canAllot==false)
                {
                    cout << endl << "System is not safe\n";
                    efe << endl << "System is not safe\n";
                    askUser();
                    return ;
                }
        }

        cout << endl << "System is in safe state\n";
        cout << "Safe sequence: ";
        efe << endl << "System is in safe state\n";
        efe << "Safe sequence: ";
        for(i=0;i<N;i++){
        	cout << "P" << sequence[i] << " " ;
            efe << "P" << sequence[i] << " " ;
		}
            
        cout << endl << endl;
        efe << endl << endl;
}

int main(){
	efe.open ("MP05_Output_Ambata.txt");
	mainProcess();
}
void mainProcess(){
	efe << "\nProgrammed by: Jo Simon V. Ambata" << endl;
    efe << "MP05 - BANKER'S ALGORITHM" << endl << endl;
	
    student_information();

    srand(time(0));
    int i,j,N,M;
    char letter = 64;
    int index = 0;
    
    //File Input
    ifstream file_linecount("MP05_check.txt"); //variable for line count
	ifstream input("MP05_check.txt"); //variable for getting the data
    //Line Count
    int number_of_lines = 0;
    string line;
    while (getline(file_linecount, line)){
    	++number_of_lines;
	}
    //Reference: https://stackoverflow.com/questions/3482064/counting-the-number-of-lines-in-a-text-file
    
    int data_array [number_of_lines];
	if(input.is_open()){
	    while(!input.eof()){
	          string number;
	          int data;
	           getline(input,number); //read number
	           data = atoi(number.c_str()); //convert to integer
	           data_array[index] = data;
	           index = index + 1;
	    }
	}
	int len = *(&data_array + 1) - data_array;
	//Reference: https://www.cplusplus.com/forum/beginner/73470/
	//cout<<inFile;
    
    //User Input
    cout << "Input (1)" << endl << "Enter the following:(From the file: MP05_check.txt)"<<endl;
    cout << "No. Processes: "<<data_array[0];
    efe << "Input (1)" << endl << "Enter the following:(From the file: MP05_check.txt)"<<endl;
    efe << "No. Processes: "<<data_array[0];
    N = data_array[0];
	cout<<endl;
    efe<<endl;
    
    cout << "No. Resources: "<<data_array[1];
    efe << "No. Resources: "<<data_array[1];
    M = data_array[1];
	cout<<endl;
	efe<<endl;
    int indx,arr[100];
    
    cout << "No. of Instances: \n";
    efe << "No. of Instances: \n";
    for (i = 0; i < M; i++){
        letter = letter + 1;
        cout << (char)letter << " - "<<data_array[i+2]<<endl;
        efe << (char)letter << " - "<<data_array[i+2]<<endl;
        arr[i] = data_array[i+2];
    }


    //Process
   
    //cout << endl;
    for (i = 0; i < N; i++){
        //cout << "P" << i << " ";
        for(j = 0; j < M; j++){
            //cin >> maximum[i][j];
            maximum[i][j] = rand() % arr[j]+1;
            //cout << maximum[i][j] << " ";
        }
        //cout << endl;
    }
    //cout << endl;
    //Allocation
    int sum;
    int temp;

    //N = process
    //M = resource
    //cout <<"Allocation:";
    for (i = 0; i < M; i++){   
        sum = 0;
        for(j = 0; j < N; j++){
            if (maximum[j][i] == 0 || sum >= arr[i])
                allot[j][i] = 0;
        else{
            do{
                temp = rand() % (arr[i] - sum);
            }while (temp>maximum[j][i]);
            allot[j][i] = temp;
            sum += temp;
        }
        sum += allot[j][i];
        }
    }
    

    for (i = 0; i <= M; i++){
        available[i] = arr[i];
        for(j = 0; j < N; j++){
            available[i] = available[i] - allot[j][i];
        }
    }   


    //Output
    //Need matrix
    letter = 64;
    cout << "\nOutput (1):"<<endl;
    cout << "NEED MATRIX: " << endl;
    cout << "   ";
    efe << "\nOutput (1):"<<endl;
    efe << "NEED MATRIX: " << endl;
    efe << "   ";
    for (i=0;i<M;i++){
        letter = letter + 1;
        cout << (char)letter << " ";      
        efe << (char)letter << " ";
    }

    cout << endl;
    efe << endl;
    
    for(i=0;i<N;i++){
        cout << "P" << i << " ";
        efe << "P" << i << " ";
        for(j=0;j<M;j++){
            need[i][j]=maximum[i][j]-allot[i][j];
            cout << need[i][j] << " ";
            efe << need[i][j] << " ";
        }
        cout << endl;
        efe << endl;
    }
    isSafe(N,M);



    //input 2
    cout << "Input (2)" << endl;
    cout << "Request" << endl;
    cout << "Process ID: P";
    cin >> indx;
    efe << "Input (2)" << endl;
    efe << "Request" << endl;
    efe << "Process ID: P";
    efe << indx << endl;

    cout << "No. of Instances: "<<endl;
    efe << "No. of Instances: "<<endl;
    letter = 64;
    for(i=0;i<M;i++){
        letter = letter + 1;
        cout << (char)letter << " - ";
        efe << (char)letter << " - ";
        cin >> arr[i];
        efe << arr[i]<<endl;
    }
    
    //output 2
    for(i=0;i<M;i++){
            if( need[indx][i]<arr[i] || arr[i]>available[i] )
            {
               cout << "Cannot request" << endl;
               efe << "Cannot request" << endl;
                break;
            }
    }


    if(i==M){
        for(i=0;i<M;i++){
            allot[indx][i]+=arr[i];
            available[i]-=arr[i];
            need[indx][i]-=arr[i];
        }

        cout << endl;
        efe << endl;

        letter = 64;
        cout << "NEED MATRIX: " << endl;
        cout << "   ";
        efe << "NEED MATRIX: " << endl;
        efe << "   ";
        for (i=0;i<M;i++){
            letter = letter + 1;
            cout << (char)letter << " ";      
            efe << (char)letter << " ";   
        }

        cout << endl;
        efe << endl;
        for(i=0;i<N;i++){
            cout << "P" << i << " ";
            efe << "P" << i << " ";
            for(j=0;j<M;j++){
                need[i][j]=maximum[i][j]-allot[i][j];
                cout << need[i][j] << " ";
                efe << need[i][j] << " ";
            }
            cout << endl;
            efe << endl;
        }
        isSafe(N,M);
    }
    

askUser();

}

void askUser(){
    
    char answer;
    string question = "Do you want to exit[y/n]?:";
    cout << question;
    efe << question;
    cin >> answer;
    efe << answer;
    answer = tolower(answer);

    if (answer == 'n'){
        cout << endl << endl;
        mainProcess();
    }

    else if (answer == 'y'){
        system("pause");
        exit('0');
    }

    else{
        cout << "Choose only between 'y' and 'n'!" << endl;
        efe << "Choose only between 'y' and 'n'!" << endl;
        askUser();
    }
}

