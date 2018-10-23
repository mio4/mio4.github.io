---
layout: post
title:  "二维数组中的查找"
categories: 剑指Offer
tags:  DataStructure Offer 
author: mio4
---

* content
{:toc}







## 二维数组中的查找

**题目描述**
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

**分析**


  - 首先矩阵是有序的，所以实质上不需要遍历矩阵中所有的元素来判断是否含有目标整数。
  - 然后观察到矩阵的右上角元素的性质：是每一行中的最大元素，也是每一列中的最小元素。
  - 所以从矩阵的右上角开始判断，如果大于目标整数，那么这一列可以被排除，坐标左移；如果小于目标整数，那么这一行可以被排除，坐标下移。


```java
public class Solution {
	public boolean Find(int target, int [][] array) {
		int n = array.length; //行数
		int m = array[0].length; //列数
		int i = 0;
		int j = m-1;
		while(true){
			if(array[i][j] == target) {
				return true;
			} else if(array[i][j] < target){
				i++; //排除本行
				if(i >= n)
					break;
			} else if (array[i][j] > target){
				j--; //排除本列
				if(j < 0)
					break;
			}
		}
		return false;
	}
}

```

在OJ上提交之后发现只过了部分点，并且对于输入空数组的情况产生了数组溢出，发现是没有考虑到输入为空矩阵时的边界情况，修改之后AC：


```java 
public class Solution {
	public boolean Find(int target, int [][] array) {
		int n = array.length; //行数
		int m = array[0].length; //列数
		if(m == 0) //空矩阵判断
			return false;
		int i = 0;
		int j = m-1;
		while(true){
			if(array[i][j] == target) {
				return true;
			} else if(array[i][j] < target){
				i++; //排除本行
				if(i >= n)
					break;
			} else if (array[i][j] > target){
				j--; //排除本列
				if(j < 0)
					break;
			}
		}
		return false;
	}
}

```