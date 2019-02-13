struct link{

	int element;
	int num;
	struct link *next;
};

typedef struct link node;

void insert(int value,int num,node **linkp);	/* 插入一个值 */
void deletelist(node *head);			/* 释放内存 */
void print(node *head);				/* 输出结果 */
node *multpolynomial(node *p1,node *p2);	/* 将两个多项式相乘 */

void
insert(int value,int num,node **linkp){

	node *current,*newnode;

	while((current=*linkp)!=NULL&&current->element<value)
		linkp=&current->next;

	if(current!=NULL&&current->element==value){

		current->num+=num;
		return;
	}

	if((newnode=malloc(sizeof(node)))==NULL){

		printf("Memory error\n");
		exit(0);
	}

	newnode->element=value;
	newnode->next=current;
	newnode->num=num;
	*linkp=newnode;
}

void
deletelist(node *head){

	while(head!=NULL){

		free(head);
		head=head->next;
	}
}

node *
multpolynomial(node *p1,node *p2){

	node *current1;
	node *current2;
	node *res=NULL;
	for(current1=p1;current1!=NULL;current1=current1->next){

		for(current2=p2;current2!=NULL;current2=current2->next){

			insert(current1->element+current2->element,current1->num*current2->num,&res);
		}
	}

	return res;
}

void
print(node *head){

	printf("%dx^%d",head->num,head->element);
	while((head=head->next)!=NULL){

		printf("+");
		printf("%dx^%d",head->num,head->element);
	}

	printf("\n");
}
