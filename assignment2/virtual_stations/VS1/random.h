// C program for generating a 
// random number in a given range. 
#include <stdio.h> 
#include <stdlib.h> 
#include <time.h> 
  
// Generates and prints 'count' random 
// numbers in range [lower, upper]. 
int getRandom(int lower, int upper) 
{  
    int num = (rand() % 
        (upper - lower + 1)) + lower; 
    return num;
} 
  