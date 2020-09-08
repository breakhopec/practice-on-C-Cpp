#include<stdio.h>
int removeElement(int* nums, int numsSize, int val){
    int *tmp_nums = nums;
    int count = 0;
    for(int i = 0;i < numsSize;nums++, i++){
        if(val != *nums){
            *tmp_nums++ = *nums;
            count++;
        }
    }
    return count;
}

int main(){

    int array[8] = {1,2,3,3,34,5,3,2};
    int res = removeElement(array, 8, 3);
    printf("%d\n", res);
    return 0;
}