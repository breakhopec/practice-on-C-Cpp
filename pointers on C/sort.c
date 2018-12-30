/*
** 尝试实现 sort 函数，对任何类型的数组进行排序
** 接受四个参数，分别为储存数据的指针，元素数量，元素大小以及一个比较大小的函数指针
** 函数指针接受两个参数，为比较数据的指针，相等时返回 0 ，第一个参数大于第二个参数时返回正值，反之返回负值
** sort 执行成功返回 0
*/

#include<stdio.h>
#include<stddef.h>

/* 示例的第四个参数 */
/* 比较整数 */
int
int_compare(void const *a,void const *b){

	return *(int *)a-*(int *)b;
}

/* 比较字符串 */
int
str_compare(void const *a,void const *b){

	return strcmp(*(char **)a,*(char **)b);
}

int
sort(void *array,int n_ele,size_t size,int (*compare)(void const *,void const *)){

	char temp;
	char *ch=(char *)array;
	char *current1,*current2;

	for(int i=0;i<n_ele-1;i++){

		current1=ch+i*size;
		for(int j=i+1;j<n_ele;j++){
			
			current2=ch+j*size;
			if(compare(current1,current2)>0){

				for(int k=0;k<size;k++){
					temp=*(current1+k);
					*(current1+k)=*(current2+k);
					*(current2+k)=temp;
				}
			}
		}
		
	}
	
	return 0;
}
