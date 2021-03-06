/*
** 按顺序在链表中插入数值
*/

#include<stdio.h>
#include<stdlib.h>
#define TYPENAME int

struct link{

	TYPENAME element;
	struct link *next;
};

typedef struct link node;

int
insert(TYPENAME value,node **linkp){

	node *current,*newnode;

	while((current=*linkp)!=NULL&&current->element<value)
		linkp=&current->next;

	if((newnode=(node *)malloc(sizeof(node)))==NULL){

		printf("Memory error\n");
		exit(0);
	}

	newnode->element=value;
	newnode->next=current;
	*linkp=newnode;
}

void
deletenode(TYPENAME value,node **linkp){

	node *current;
	while((current=*linkp)!=NULL&&current->element!=value)
		linkp=&current->next;

	if(current==NULL) return;
	
	*linkp=current->next;
	free(current);
}

void
deletelist(node *head){

	while(head!=NULL){

		free(head);		/*符合 UNIX 系统第七版参考手册可用*/
		head=head->next;
	}
}
