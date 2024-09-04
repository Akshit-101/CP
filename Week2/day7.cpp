/*
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
*/

void nTriangle(int n) {
	for (int i = 1; i<=n; i++){
		for (int j=1; j<=i; j++){
			cout <<  j << " ";
		}
		cout << endl;
	}
}


/* 
    *       
   ***      
  *****     
 *******    
*********   

*/

void nStarTriangle(int n) {
    int space;
    int star;
    for (int i = 0; i < n; i++) {
        star = 2 * i + 1;
        space = n - i - 1;
        cout << string(space, ' ') << string(star, '*') << string(space, ' ') << endl;
    }
}


/*

  *
 ***
*****
*****
 ***
  *

*/

void nStarDiamond(int n) {
    for (int i =0; i<n; i++) {
        for (int j=0; j<n-i-1; j++){
            cout << " ";
        }

        for (int j=0; j<2*i+1; j++) {
            cout << "*";
        }

        for (int j= 0; j<n-i-1; j++){
            cout << " ";
        }
        cout << endl;
    }


    for (int i=0; i<n; i++){
        for (int k = 0; k<i; k++){
            cout << " ";
        }

        for (int k=0; k < 2*n - (2*i + 1); k++) {
            cout << "*";
        }

        for (int k=0; k<i; k++) {
            cout << " ";
        }
        cout << endl;
    }
}


/*
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
*/

#include <bits/stdc++.h>
using namespace std;

void pattern11(int N)
{
      // First row starts by printing a single 1.
      int start =1;
      
      // Outer loop for the no. of rows
      for(int i=0;i<N;i++){
          
          // if the row index is even then 1 is printed first
          // in that row.
          if(i%2 ==0) start = 1;
          
          // if odd, then the first 0 will be printed in that row.
          else start = 0;
          
          // We alternatively print 1's and 0's in each row by using
          // the inner for loop.
          for(int j=0;j<=i;j++){
              cout<<start;
              start = 1-start;
          }
      
      
        // As soon as the numbers for each iteration are printed, we move to the
        // next row and give a line break otherwise all numbers
        // would get printed in 1 line.
        cout<<endl;
      }
}

int main()
{   
    // Here, we have taken the value of N as 5.
    // We can also take input from the user.
    int N = 5;
    pattern11(N);

    return 0;
}
