/**
01-01-Selection-Sort

��MArr���̤p�ȡA�ç�}�Y�մ��C
**/

#include <iostream>
#include <vector>
using namespace std;

void SelectionSort(vector<int>& nums)
{
    for(int i=0; i<nums.size(); i++)
    {
        int minIndex=nums[i];
        for(int j=i; j<nums.size(); j++)
        {
            if(nums[minIndex]>nums[j])
            {
                minIndex=j;
            }
        }
        int tmp=nums[i];
        nums[i]=nums[minIndex];
        nums[minIndex]=tmp;
    }
}

int main()
{
    vector<int> nums= {10,9,8,7,6,5,4,3,2,1,0};
    SelectionSort(nums);

    for(int i=0; i<nums.size(); i++)
        cout<<nums.at(i)<<" ";
    cout<<endl;

    return 0;
}
