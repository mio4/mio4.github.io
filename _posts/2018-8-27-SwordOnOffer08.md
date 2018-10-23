---
layout: post
title:  "数值的整数次方"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 数值的整数次方

**题目描述**
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

**分析**

 - 题目本身没有难度，关键在于边界条件和效率优化
   - 指数为负数时，涉及到除法，那么就涉及到除零判断
   - 0的非负整数次方都是0（其中0的0次方视作0）
   - double类型不能直接使用==进行比较

```java 
public class Solution {
	public double Power(double base, int exponent) {
		//底数是否为零
		if(base == 0 && exponent < 0){
			System.out.println("除零错误");
			return 0;
		}

		double result = 1.0;
		//指数是否是负数
		if(exponent < 0){
			result = PowerWithPositiveExp(base,-exponent);
			result = 1 / result;
		} else{
			result = PowerWithPositiveExp(base,exponent);
		}

		return result;
	}

	public double PowerWithPositiveExp(double base, int exponent){
		double result = 1.0;
		for(int i=0; i < exponent; i++)
			result *= base;
		return result;
	}

	public boolean equal(double x, double y){ //如果x和y差距足够小，可以默认为相等
		return ((x-y < 0.0000001));
	}
}

```
 - 可以将PowerWithPositiveExp函数进行如下优化
 - 类似于矩阵的快速幂，可以在logn时间内求出次方结果
 - 使用>>1代替除法，使用& 0x1代替取模运算，提高时间效率

```java
public double PowerWithPositiveExp2(double base, int exponent){
		if(exponent == 0)
			return 1;
		if(exponent == 1)
			return base;
		double result = PowerWithPositiveExp2(base,exponent >> 1);
		result *= result;
		if((exponent & 0x1) == 1)
			result *= base;
		return result;
	}
```