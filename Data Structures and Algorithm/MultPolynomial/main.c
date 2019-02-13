#include<stdio.h>
#include"MultPolynomial.h"

int main(){

	FILE *in;
	node *p1=NULL;
	node *p2=NULL;
	node *res;
	int value,num;

	in=fopen("input.in","r");
	for(int i=0;i<3;i++){

		fscanf(in,"%d %d",&value,&num);
		insert(value,num,&p1);
	}

	for(int i=0;i<2;i++){

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
