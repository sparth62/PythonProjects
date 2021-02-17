#include<iostream>
#include<stdio.h>
#include<conio.h>
#include<iomanip>
#include<stdlib.h>
#include<windows.h>
#include<ctype.h>
#include<time.h>
using namespace std;

long winning=0;
int cnt=0;
int new_time=0;
int lifeline[4]={0,0,0,0};

class question
{
	private:
	string que;
	string o1,o2,o3,o4;
	char answer;
	long value;
	char user_ans;
	int dd;
	public:
	question(string,string,string,string,string,char,long);
	void show_question();
	void get_answer();
	void check_answer();
};

question::question(string q,string O1,string O2,string O3,string O4,char ans,long val)
{
	que=q;
	o1=O1;
	o2=O2;
	o3=O3;
	o4=O4;
	answer=ans;
	value=val;
}

void question::show_question()
{
	system("cls");
	cout<<endl<<que<<endl;
	cout<<"A."<<setw(15)<<left<<o1<<"B."<<setw(15)<<left<<o2<<endl<<"C."<<setw(15)<<left<<o3<<"D."<<setw(15)<<left<<o4;
	cout<<"\n------------------------------------------------------------------------------\n";

    cout<<"A|B|C|D for answer\n";
    if(lifeline[0]==0)
    {
        cout<<"1 for Message a friend\t";
    }
    if(lifeline[1]==0)
    {
        cout<<"2 for Fifty-Fifty";
    }
    cout<<endl;
    if(lifeline[2]==0)
    {
        cout<<"3 for Double Dip\t";
    }
    if(lifeline[3]==0)
    {
        cout<<"4 for Audience Poll ";
    }
    get_answer();
    check_answer();
}

void question::get_answer()
{
	cout<<"\nPlease enter your answer";  
	if(cnt<5)
	{ 
		DWORD start_time, check_time;
		start_time=GetTickCount();
        if(new_time==1)
        {
            cout<<"(Time_Limit: 180 seconds):";
            check_time=start_time+180000;
        }
        else 
        {
            cout<<"(Time_Limit: 60 seconds):";
        	check_time=start_time+60000;
        }
        while((check_time>GetTickCount()))
        {
        	if (kbhit())
            {
            	user_ans=getche();
                break;
            }
            user_ans='\0';
        }	    	
        new_time=0;
	}  
	else
	{
    	cout<<":";
	   	user_ans=getche();
    }
    user_ans=toupper(user_ans);
    cnt++;
}

void question::check_answer()
{
	if(user_ans==answer)
	{
		winning=value;
		cout<<"\nCongratulations, You win "<<winning<<" INR.";
		int k=0;
		dd=0;
		while(k!=15)
		{
			if(k%2==0)
				system("color 1E");
			else
				system("color E1");
			Sleep(100);
			k++;
		}
	}
    else if(user_ans=='1' && lifeline[0]==0 && dd==0)
    {
    	lifeline[0]=1;
      	cout<<"\nWait for few seconds";
      	system("python friend.py");
      	new_time=1;
      	show_question();
    }
    else if(user_ans=='2' && lifeline[1]==0 && dd==0)
    {
      	lifeline[1]=1;
      	srand(time(0));
      	char n1,n2;
      	int upper=68;
      	int lower=65;
       	do
       	{
        	n1= (rand() % (upper - lower + 1)) + lower;
         	n2= (rand() % (upper - lower + 1)) + lower;
         	if(n1==answer)
         	{
           		n1= (rand() % (upper - lower + 1)) + lower;
         	}
         	if(n2==answer)
         	{
          		n2= (rand() % (upper - lower + 1)) + lower;
         	}  
       }while(n1==n2 || n1==answer || n2==answer);
       
       printf("\n%c and %c are not answer",n1,n2);
       printf("\nPress any key to continue...");
       getch();
       show_question();
    }
    else if(user_ans=='3' && lifeline[2]==0 && dd==0)
    {
    	lifeline[2]=1;
    	dd=0;
    	get_answer();
    	if(user_ans==answer)
    	{
    		dd=1;
    		check_answer();
    	}
    	else
    	{
    		cout<<"\nTry Again";
    		get_answer();
    		dd=1;
    		check_answer();
    	}
    }
    else if(user_ans=='4' && lifeline[3]==0 && dd==0)
    {
    	lifeline[3]=1;
      	cout<<"\nAccording to Audience answer is "<<answer;
      	printf("\nPress any key to continue...");
       	getch();
      	show_question();
    }
	else
	{
		cout<<"\n\aSorry, you are disqualify, Your Total winning amount is "<<winning<<" INR";
		exit(0);
	}
}

void display()
{
	char s[]="KAUN BANEGA\n\t\t\t\tCROREPATI";
	int i=0;
	system("cls");
	cout<<"\n\n\n\n\n\n\n\n\n\t\t\t\t";
	while(s[i]!='\0')
	{
		if(i%2==0)
			system("color 1E");
		else
			system("color E1");
		while(s[i]=='\t' || s[i]=='\n')
		{
			cout<<s[i++];
		}
		cout<<s[i++]<<"\a";
		Sleep(500);
	}
	cout<<"\n\n\t\t\t\t\tDeveloped by, Parth Shinojiya";
	cout<<"\n\t\t\t\t\tPowered by, Try Something New";
	i=0;
	while(i!=25)
	{
		if(i%2==0)
			system("color 1E");
		else
			system("color E1");
		Sleep(100);
		i++;
	}
}

int main()
{
	display();
    question q[50]={
    	question("What is the Binary number of 1?","000000","000001","000111","001010",'B',20000),
        question("What is the Binary number of 2?","000000","000001","000010","001010",'C',20000),
        question("What is the Binary number of 3?","000000","000011","000010","001010",'B',20000),
        question("What is the Binary number of 4?","000000","000001","000010","000100",'D',20000),
        question("What is the Binary number of 5?","000000","000101","000010","001010",'B',20000),
        question("What is the Binary number of 6?","000110","000001","000010","001010",'A',40000),
        question("What is the Binary number of 7?","000000","000001","000111","001010",'C',40000),
        question("What is the Binary number of 8?","000000","000001","000010","001000",'D',40000),
        question("What is the Binary number of 9?","000000","001001","000010","001010",'B',40000),
        question("What is the Binary number of 10?","001010","000001","000010","001011",'A',40000),
        question("What is the Binary number of 11?","001011","000001","000111","001010",'A',80000),
        question("What is the Binary number of 12?","000000","001100","000010","001000",'B',80000),
        question("What is the Binary number of 13?","001101","001001","001011","001010",'A',80000),
        question("What is the Binary number of 14?","001100","000001","001110","001011",'C',80000),
        question("What is the Binary number of 15?","001010","001101","000010","001111",'D',80000),
        question("What is the Binary number of 16?","001011","010000","000111","001010",'B',160000),
        question("What is the Binary number of 17?","000000","001100","010001","001000",'C',160000),
        question("What is the Binary number of 18?","010010","001001","001011","001010",'A',160000),
        question("What is the Binary number of 19?","010011","000001","001110","001011",'A',160000),
        question("What is the Binary number of 20?","011001","011101","010011","010100",'D',160000),
        question("What is the Binary number of 21?","010101","010000","000111","001010",'A',320000),
        question("What is the Binary number of 22?","000000","010110","010001","001000",'B',320000),
        question("What is the Binary number of 23?","010111","001001","001011","001010",'A',320000),
        question("What is the Binary number of 24?","010011","011000","001110","001011",'B',320000),
        question("What is the Binary number of 25?","011001","011101","011001","010100",'C',320000),
        question("What is the Binary number of 26?","001011","010000","011010","001010",'C',640000),
        question("What is the Binary number of 27?","011000","011001","010001","011011",'D',640000),
        question("What is the Binary number of 28?","011100","011010","001011","001010",'A',640000),
        question("What is the Binary number of 29?","010011","010101","011011","011101",'D',640000),
        question("What is the Binary number of 30?","010110","011110","011100","011000",'B',640000),
        question("What is the Binary number of 31?","010111","011111","000111","011001",'B',1250000),
        question("What is the Binary number of 32?","010111","001100","100000","010110",'C',1250000),
        question("What is the Binary number of 33?","011010","001001","001011","100001",'D',1250000),
        question("What is the Binary number of 34?","100010","011000","001110","001011",'A',1250000),
        question("What is the Binary number of 35?","011001","011011","010011","100011",'D',1250000),
        question("What is the Binary number of 36?","100100","010000","000111","001010",'A',2500000),
        question("What is the Binary number of 37?","011111","011110","100101","001000",'C',2500000),
        question("What is the Binary number of 38?","100110","011010","100011","100100",'A',2500000),
        question("What is the Binary number of 39?","010011","100111","001110","100011",'B',2500000),
        question("What is the Binary number of 40?","101000","100100","010011","100010",'A',2500000),
        question("What is the Binary number of 41?","101001","010000","000111","011001",'A',5000000),
        question("What is the Binary number of 42?","010111","001100","101010","010110",'C',5000000),
        question("What is the Binary number of 43?","011110","101011","001011","011010",'B',5000000),
        question("What is the Binary number of 44?","101100","100110","100011","011101",'A',5000000),
        question("What is the Binary number of 45?","011100","101101","010011","010101",'B',5000000),
        question("What is the Binary number of 46?","101110","110010","000111","001100",'A',10000000),
        question("What is the Binary number of 47?","110010","011001","101111","100001",'C',10000000),
        question("What is the Binary number of 48?","110000","101110","110010","101001",'A',10000000),
        question("What is the Binary number of 49?","001011","110000","110010","110001",'D',10000000),
        question("What is the Binary number of 50?","110010","011101","101110","011000",'A',10000000)};
    srand(time(0));
    int upper;
    int num;
    system("color 1E");
    upper=4;
    num = (rand() % (upper - 0 + 1)) + 0;
    q[num].show_question();
    num = (rand() % (upper - 0 + 1)) + 5;
    q[num].show_question();
    num = (rand() % (upper - 0 + 1)) + 10;
    q[num].show_question();
    num = (rand() % (upper - 0 + 1)) + 15;
    q[num].show_question();
    num = (rand() % (upper - 0 + 1)) + 20;
    q[num].show_question();
    num = (rand() % (upper - 0 + 1)) + 25;
    q[num].show_question();
    num = (rand() % (upper - 0 + 1)) + 30;
    q[num].show_question();
    num = (rand() % (upper - 0 + 1)) + 35;
    q[num].show_question();
    num = (rand() % (upper - 0 + 1)) + 40;
    q[num].show_question();
    num = (rand() % (upper - 0 + 1)) + 45;
    q[num].show_question();
	getch();
	return 0;
}