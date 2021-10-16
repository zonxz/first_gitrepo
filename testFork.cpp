//test_fork.cpp
/*

Code orgin CSE4600 Bilal Kahn

Student: Caleb Reiman ID: 003255251 
Modifications will be taged with comments
For Exp. //@# foobarwundebar! or //@# Create a orphan pid state 

*/
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <iostream>
 
using namespace std;
 
int main()
{
  pid_t pid;        //process id
 
 
  //pid_t test; //@# want to compare the the pid obj contents\
                to see if why calling pid yields 3xxxx number
  //printf("Here is Testpid for pid comparison: %d\n",test);
  
  //@# Examining pid obj and getpid() before fork
  printf("Called with pid obj PID:%d\n",pid);
  printf("Called with getpid function:%d\n",getpid());
  //@# Calling for parent pid of contructed pid test
  printf("Called with getppid function:%d\n",getppid());
  
  
  char *message;
  int n;
  int status;
  cout << "\nfork program starting\n";
  pid = fork();
  
  //@# Examine after fork occured. 
  printf("\nA fork occured!\n");
  printf("Called with pid obj PID:%d\n",pid);
  printf("Called with getpid function:%d\n",getpid());
  
  switch (pid) {
  case -1:
    cout << "Fork failure!\n";
    return 1;
  
  case 0:
    message = "This is the child\n";
    n = 5;
    break;
  
  default:
    message = "This is the parent\n";
    n = 3;
    break;
  }
  
  for (int i = 0; i < n; ++i) {
    cout << "\n" << message << getpid() << endl;
    sleep (1);
    
  }
  
 cout <<"The pidobj: "<< pid << endl\
      <<"\ngetpid: "<< getpid() <<\
      endl <<"\ngetppid: "<< getppid()\
      << endl;
  return 0; 
}
