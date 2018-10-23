---
layout: post
title:  "顺时针打印矩阵"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 顺时针打印矩阵

**题目描述**
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

**分析**

  - 这道题和前面做的 [Z字形打印矩阵](https://blog.csdn.net/H_Targaryen/article/details/81587956) CCF题一样，都是对于二维矩阵的自定义打印
  - 把矩阵的四面看做是四个围墙(North、East、South、West)，围墙不断缩进，直到打印完所有的数字
  - 打印方向用flag表示，flag = 1表示从左往右，2表示从上往下，3表示从右往左，4表示从下往上
  - 然后Debug之后写出了下面的程序，虽然AC了，但是很繁琐


```java 
import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printMatrix(int [][] matrix) {
       		ArrayList<Integer> result = new ArrayList<Integer>();
		int NORTH = 0;
		int EAST = 0;
		int SOUTH = 0;
		int WEST = 0;
		int flag = 1;
		int cnt = 0;
		int n = matrix.length; //行数
		int m = matrix[0].length; //列数
		int i = 0;
		int j = 0;
		while(cnt < m*n){
			if(flag == 1){
				for(int k=WEST; k < m-EAST; k++) {
					result.add(matrix[i][j]);
					j++;
					cnt++;
				}
				j--;
				i++;
				NORTH++;
				flag = 2;
			} else if(flag == 2){
				for(int k=NORTH; k < n-SOUTH; k++){
					result.add(matrix[i][j]);
					i++;
					cnt++;
				}
				i--;
				j--;
				EAST++;
				flag = 3;
			} else if(flag == 3){
				for(int k=m-EAST-1; k >= WEST ;k--){
					result.add(matrix[i][j]);
					j--;
					cnt++;
				}
				j++;
				i--;
				SOUTH++;
				flag = 4;
			} else if(flag == 4){
				for(int k=n-SOUTH-1; k >= NORTH; k--){
					result.add(matrix[i][j]);
					i--;
					cnt++;
				}
				i++;
				j++;
				WEST++;
				flag = 1;
			}
		}
		return result;
    }
}
```

 - 现在考虑程序的优化
   - 发现循环变量k的存在意义不大，将其由i和j表示 

```java 
		ArrayList<Integer> result = new ArrayList<Integer>();
		int NORTH = 0;
		int EAST = 0;
		int SOUTH = 0;
		int WEST = 0;
		int flag = 1;
		int cnt = 0;
		int n = matrix.length; //行数
		int m = matrix[0].length; //列数
		int i = 0;
		int j = 0;
		while(cnt < m*n){
			if(flag == 1){
				for(j=WEST; j < m-EAST; j++) {
					result.add(matrix[i][j]);
					cnt++;
				}
				j--;
				i++;
				NORTH++;
				flag = 2;
			} else if(flag == 2){
				for(i=NORTH; i < n-SOUTH; i++){
					result.add(matrix[i][j]);
					cnt++;
				}
				i--;
				j--;
				EAST++;
				flag = 3;
			} else if(flag == 3){
				for(j=m-EAST-1; j >= WEST ;j--){
					result.add(matrix[i][j]);
					cnt++;
				}
				j++;
				i--;
				SOUTH++;
				flag = 4;
			} else if(flag == 4){
				for(i=n-SOUTH-1; i >= NORTH; i--){
					result.add(matrix[i][j]);
					cnt++;
				}
				i++;
				j++;
				WEST++;
				flag = 1;
			}
		}
		return result;
```

 - 看了一下《剑指Offer》上的解法，书上的解法和上面AC的差不多
 - 但是书中对于最后一圈打印时分出了三种情况
   - 我是使用count变量计数到m*n就结束打印
   