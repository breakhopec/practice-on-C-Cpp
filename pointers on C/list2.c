/*
** 第二个链表版本，不按顺序插入了
** 同时增加了一个哑结点
** 感觉第一个版本要好些...
*/

#include<stdio.h>
#include<stdlib.h>
#define TYPENAME int

struct link{

	TYPENAME element;
	struct link *next;
};

typedef struct link node;

node *
createhead(){

	return (node *)malloc(sizeof(node));
}

void
insert(TYPENAME value,node *head){

	node *newnode;
	if((newnode=(node *)malloc(sizeof(node)))==NULL){

		printf("Out of memory\n");
		exit(1);
	}

	newnode->element=value;
	newnode->next=head->next;
	head->next=newnode;
}

void
deletenode(TYPENAME value,node *head){

	node *previous;
	while((head=(previous=head)->next)!=NULL&&head->element!=value)
		;

	if(head==NULL) return;

	previous->next=head->next;
	free(head);
}

void
deletelist(node *head){

	while(head!=NULL){

		free(head);
		head=head->next;
	}
}
