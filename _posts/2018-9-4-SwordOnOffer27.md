---
layout: post
title:  "机器人的运动范围"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}






## 机器人的运动范围


**题目描述**
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

**分析**

 - 这道题自己调试了一会儿，主要问题出在没有将函数处理的部分抽离出来，所以出现了重复定义变量的情况，AC之后发现和书上的代码思路还是不一样的
   - 根据“矩阵中的路径”的解题方法， 我也设立了一个全局visited变量，表示这个格子是否已经被计入count中
   - 另外格子要计入count的条件是：1.满足位数和小于k的条件 2.满足在矩阵内的坐标 3.没有被访问过
   - 所以直接使用了递归：对于每个格子，按照四个方向去寻找，找不到就结束这条路径的寻找，否则进行新的递归 

```java 
public class Solution {
	public static int count = 0;
	public static boolean visited[][];
	static int i = 0;
	static int j = 0;
	static int m_rows;
	static int m_cols;
	public static  int movingCount(int threshold, int rows, int cols)
	{
		m_rows = rows;
		m_cols = cols;
		visited = new boolean[rows][cols];
		Moving(threshold,i,j);
		return count;
	}

	public static void Moving(int threshold, int i, int j){
		if(!isMoreK(threshold,i,j)  && i >= 0 && i < m_rows && j >= 0 && j < m_cols && !visited[i][j]) { //位数和小于k，在矩阵内,没有被访问过
			count++;
			visited[i][j] = true;
			Moving(threshold, i, j + 1);
			Moving(threshold, i, j - 1);
			Moving(threshold, i - 1, j);
			Moving(threshold, i + 1, j);
		}
	}

	public static boolean isMoreK(int k, int i, int j){ //判断i和j的位数和是否大于K
		int cnt = 0;
		while(i != 0){
			cnt += i%10;
			i /= 10;
		}
		while(j != 0){
			cnt += j%10;
			j /= 10;
		}
		return (cnt > k);
	}

	public static void main(String[] args){
		System.out.println(movingCount(15,20,20));
	}
}

```