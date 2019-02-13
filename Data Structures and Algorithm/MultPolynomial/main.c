/*
** 这个是示例文件。计算多项式 POLYNOMAIAL1*POLYNOMAIAL2 的值
** 输入文件为 "input.in"
** 计算 ( 3x + 5x^3 + x^2 )( x^2 + 2x ) 的值
** 幂与系数交替输入
** 结果以幂的升序输出
*/

#include<stdio.h>
#include"MultPolynomial.h"
#define POLYNOMAIAL1 3
#define POLYNOMAIAL2 2

int main(){

	FILE *in;
	node *p1=NULL;
	node *p2=NULL;
	node *res;
	int value,num;

	in=fopen("input.in","r");
	for(int i=0;i<POLYNOMAIAL1;i++){

		fscanf(in,"%d %d",&value,&num);
		insert(value,num,&p1);
	}

	for(int i=0;i<POLYNOMAIAL2;i++){

		fscanf(in,"%d %d",&value,&num);
		insert(value,num,&p2);
	}

	res=multpolynomial(p1,p2);

	print(res);

	deletelist(p1);
	deletelist(p2);
	deletelist(res);
	fclose(in);
	return 0;
}
