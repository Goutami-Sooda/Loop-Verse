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
for (int i=0;i<5;i++) {
    for (int j=0;j<=i;j++) {
        printf("* ");
    }
}
''',
'''
for (int i=0;i<5;i++) { 
for (int j=0;j<5-i;j++) { 
printf("j "); 
	} 
} 
''',
'''
for (int i=0;i<5;i++) { 
for (int j=0; j<5;j++) { 
if (i>0 && i<4 && j>0 && j<4)  
	printf("  ");  
else  
	printf("* "); 
	}
} 
''',
'''
int rows = 4; 
int n = 1; 
for (int i=0;i<rows;i++) { 
for (int j=0;j<=i;j++) { 
printf("%d",n++); 
    } 
} 
''',
'''
int x=10, y=2;  
while(x+y-1)  
{  
printf("%d %d",x--,y--);  
}  
''',
'''
I run atleast once and need not 
stop unless you give me a good 
reason to! I am a _______ loop!
''',
'''
I am an infinity loop!
Put a face to my name!
''',
'''
int k = 0;
for (k < 3; k++)
printf("Hello");
What does this result in?
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
1 2 3 4 5
1 2 3 4
1 2 3 
1 2
1
''',
'''
* * * * *
*       *
*       *
*       *
* * * * *
''',
'''
1
2 3
4 5 6
7 8 9 10
''',
'''
10 2
9  1
8  0
7  -1
.....
''',
'''
do - while loop
''',
'''
for(;;)
''',
'''
Compile - time error!
'''

]