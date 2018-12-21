---
layout: post
title:  "旋转数组的最小数字"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}








## 旋转数组的最小数字

**题目描述**
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

**分析**

 - 这道题显然需要对时间复杂度进行限制，不能直接使用一般的顺序查找，需要考虑到旋转数组的性质
 - 旋转数组本质上是两个有序数组，对于有序数组使用二分法查找时间复杂度只有O(nlogn)
 - 有两种边界条件需要考虑
   - 数组并没有发生旋转，第一个数就是最小数
   - 数组中存在相同元素并且查找时index1、mid_index、index2位置值都相同时，并不能确定最值在左边子数组还是右边子数组，需要改为顺序查找
 - 其他情况下使用二分查找即可，结束条件是index1在左子数组的最大值出，index2在右子数组的最小值处，index2的位置即是最小值  

```java 

import java.util.ArrayList;
public class Solution {
	public int minNumberInRotateArray(int [] array) {
		int index1 = 0;
		int index2 = array.length-1;
		int mid_index = index1;
		
		//这里有两种情况：
		//1.数组发生了旋转，必定会进入循环体内
		//2.数组没有发生旋转，直接返回array[mid_index]，此时数组的最小值就是第一个值
		while(array[index1] >= array[index2]){
			//找到最小值
			if(index1+1 == index2) {
				mid_index = index2;
				break;
			}
			mid_index = (index1 + index2) / 2;
			
			//考虑一种边界情况，需要改变查找方式为顺序查找
			if(array[index1]==array[mid_index] && array[mid_index]==array[index2])
				return findmin(array,index1,index2);
			
			//一般情况处理
			if(array[mid_index] >= array[index1])
				index1 = mid_index;
			else if(array[mid_index] <= array[index2])
				index2 = mid_index;
		}
		
		return array[mid_index];
	}

	public int findmin(int[] array, int index1, int index2){
		int min = array[index1];
		for(int i=0; i <= index2; i++)
			if(array[i] < min)
				min = array[i];
		return min;
	}
}

```
