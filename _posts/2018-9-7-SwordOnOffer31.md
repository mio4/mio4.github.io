---
layout: post
title:  "调整数组顺序使奇数位于偶数前面"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 调整数组顺序使奇数位于偶数前面

**题目描述**
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分。【OJ测试要求：并保证并保证奇数和奇数，偶数和偶数之间的相对位置不变，下面解法1能通过测试】

**分析**

 - 剑指Offer题目已经刷了30+道，可以将题型分为两类
   - 第一种是一般思路都比较难实现的，主要考察如何解决问题，光是想到一种解法都比较hard，优化是可以放在能够AC之后考虑的
   - 第二种就是从普通思路上一眼就能看出问题解法的，但是这种问题要么是可以有更好的解题方法，要么就是有各种隐晦的边界条件需要注意（各种空指针以及特殊情况输入） ，这种题一般需要考虑**优化**
 - 本题很明显是第二种类型
   - 第一种基础解法是遍历数组两遍，第一遍将奇数放在新数组中，第二遍将偶数放在新数组中，然后将新数组拷贝到旧数组，缺点是利用了多余的空间
   - 第二种基础解法是遍历一遍数组，每找到一个偶数就将其放在数组末尾，整个数组向前移动一位，缺点是时间复杂度太高为O(n^2)
 - 另外的解法是设立两个指针变量，类似的也是通过设立双指针解决问题的有[和为S的两个数字](https://blog.csdn.net/H_Targaryen/article/details/82229441)和[和为S的连续正数序列](https://blog.csdn.net/H_Targaryen/article/details/82230050)
   - begin指针找到一个偶数，end指针找到一个奇数，就交换两者的位置，知道两指针相遇（这种思想在快速排序中也存在） 
   - 这种解法不能保证“并保证奇数和奇数，偶数和偶数之间的相对位置不变”

```java 
public class Solution2 {
	public static void reOrderArray(int [] array) {
		if(array == null || array.length == 0)
			return;
		int begin = 0;
		int end = array.length-1;
		while(begin < end){
			while(array[begin] %2 != 0 && begin < end) //找到一个偶数
				begin++;
			while(array[end] %2 == 0 && begin < end) //找到一个奇数
				end--;
			int tmp = array[begin];
			array[begin] = array[end];
			array[end] = tmp;
		}
	}


	public static void main(String[] args){
		int[] num = {1,2,3,4,5,6,7,8,9,10};
		reOrderArray(num);
		for(int i=0; i < 10; i++){
			System.out.println(num[i]);
		}
	}
}

```