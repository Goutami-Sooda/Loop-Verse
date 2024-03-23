#1. Right Half Pyramid
#2. Full Pyramid
#3. Rhombus Pattern
#4. Floyd's Triangle
#5. Pascal's Triangle
#6. do-while infinite loop
#7. A number's Multiplication table with 2,4,6,8,10
#8. infinite while loop

qlist = [
'''
for (int i = 0; i < 5; i++) {
    for (int j = 0; j <= i; j++) {
        printf("* ");
    }
}
''',
'''
for (int i = 0; i < 5; i++) {   
    for (int j = 0; j < 2 * (rows - i) - 1; j++) { 
        printf(" "); 
    } 
    for (int k = 0; k < 2 * i + 1; k++) { 
        printf("* "); 
    } 
} 
''',
'''
for (int i = 0; i < 5; i++) { 
    for (int j = 0; j < rows - i - 1; j++) { 
        printf(" "); 
    } 
    for (int k = 0; k < rows; k++) { 
        printf("* "); 
    } 
} 
''',
'''
int rows = 4; 
int n = 1; 
for (int i = 0; i < rows; i++) { 
    for (int j = 0; j <= i; j++) { 
        printf("%d", n++); 
    } 
} 
''',
'''
for (int i = 1; i <= rows; i++) { 
    for (int j = 0; j < rows - i; j++) { 
        printf(" "); 
    } 
    int C = 1; 
    for (int k = 1; k <= i; k++) { 
        printf("%d", C); 
        C = C * (i - k) / k; 
    } 
} 
''',
'''
inti = 1;  
do {  
    printf("Iteration %d", i);  
    i++;  
} while (1); 
''',
'''
int i=1,number=50,b=30;       
while(i<=10 && b%20==0){    
    printf("%d",(number*i));    
    i++;
    b=b+10;    
}    
''',
'''
int x = 10, y = 2;  
while(x+y-1)  
{  
    printf("%d %d",x--,y--);  
}  
'''
]

alist = [
'''
*
* *
* * *
* * * *
* * * * *
''',
'''
    *
   * *
  * * *
 * * * *
* * * * *
''',
'''
    * * * * *   
   * * * * *    
  * * * * *    
 * * * * *      
* * * * *
''',
'''
1
2 3
4 5 6
7 8 9 10
''',
'''
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1
''',
'''
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
.....
''',
'''
100
200
300
400
500
''',
'''
10 2
9  1
8  0
7  -1
.....
'''
]
