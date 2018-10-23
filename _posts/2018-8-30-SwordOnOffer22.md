---
layout: post
title:  "和为S的两个数字"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}






## 和为S的两个数字

**题目描述**
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。


**分析**

 - 特别明显的算法是先固定一个数，然后对剩下的n-1个数进行遍历，查看是否满足条件，时间复杂度为O(n^2)
   - 这种算法的缺点在于没有利用数组已经排序的特点

 - 可以从数组的首尾选定最大的和最小的两个数逐步逼近结果
   - 如果和小于sum，index_i++
   - 如果和大于sum，index_i-- 
 - 边界条件
   - 数组为null，数组长度为0 
   - 这是两个边界条件最开始没有考虑array!=null但是array==[]的情况导致WA了一个点 

```java 
import java.util.ArrayList;
public class Solution {
	public ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		if(array == null || array.length == 0) //边界情况
			return result;

		int len = array.length;
		int i = 0;
		int j = len-1;
		while(i != j){
			if(array[i] + array[j] == sum){
				result.add(array[i]);
				result.add(array[j]);
				break;
			} else if(array[i] + array[j] < sum){
				i++;
			} else if(array[i] + array[j] > sum){
				j--;
			}
		}
		return result;
	}
}
```