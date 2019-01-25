/*
** 八皇后问题
** 貌似有 92 种结果??
** 调用 call 函数输出结果
*/
#include<stdio.h>
#include<string.h>

/*
** 枚举用的数组和储存结果的数组
*/
static char array[8][8][8]={0};
static char res[8][8]={0};
static int count=0;

static int check_pre(int y,int z);	/*检查已放置的皇后*/
static void set(int y,int x);		/*设置攻击路径*/
static void empty(int num);		/*清空一个棋盘*/
static void emu(int z);			/*枚举*/
static void print(void);		/*输出结果*/
static void store_res(void);		/*储存结果*/

void call(void);

static void
set(int y,int z){

	for(int i=y+1,j=z+1;i<8&&j<8;i++,j++)
		array[z][i][j]=2;

	for(int i=y-1,j=z+1;i>=0&&j<8;i--,j++)
		array[z][i][j]=2;

	for(int i=z+1;i<8;i++)
		array[z][y][i]=2;

	array[z][y][z]=1;
}

static void
empty(int num){

	memset(array[num],0,sizeof(char)*64);
}

static void
emu(int z){

	if(z==8){

		store_res();
		print();
		return;
	}

	for(int i=0;i<8;i++)
		if(check_pre(i,z)){

			set(i,z);
			emu(z+1);
			empty(z);
		}
}

static int
check_pre(int y,int z){

	for(int i=0;i<z;i++)
		if(array[i][y][z]==2)
			return 0;

	return 1;
}

static void
store_res(void){

	for(int i=0;i<8;i++)
		for(int j=0;j<8;j++)
	 		for(int k=0;k<8;k++)
				if(array[i][j][k]==1)
					res[k][j]=1;
}

static void
print(void){

	count++;
	printf("solution %d:\n",count);

	for(int i=0;i<8;i++){

		for(int j=0;j<8;j++)
			printf("%d ",res[i][j]);

		printf("\n");
	}

	printf("\n\n\n");
	memset(res,0,sizeof(char)*64);

}

void call(){

	emu(0);
}
