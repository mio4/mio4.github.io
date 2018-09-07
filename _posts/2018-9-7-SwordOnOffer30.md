---
layout: post
title:  "剑指Offer面试题：表示数值的字符串"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}






## 表示数值的字符串

**题目描述**
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。


**分析**

 - 对于实例demo分析：典型的数值非法的情况有
   - +-号同时出现，不是第一次出现+-号并且不在E/e之后一个字符
   - 出现多个小数点，出现多个E/e
   - E/e不能是最后一个字符
   - 小数点在E/e之后出现
   - 出现非法字符


```java 
public class Solution {
	public static boolean isNumeric(char[] str) {
		boolean havesignal=false; //是否出现了+-号
		boolean haveE=false; //是否出现E/e
		boolean haveRadix=false; //是否出现小数点
		if(str == null || str.length == 0) //边界条件
			return false;

		for(int i=0; i < str.length; i++){
			if(str[i] == 'E' || str[i] == 'e'){
				if(haveE) //不能有多个E/e
					return false;
				if(i == str.length-1) //E/e不能是最后一个字符
					return false;
				haveE = true;
			} else if(str[i] == '+' || str[i] == '-'){
				if(havesignal  && (str[i-1] != 'E' && str[i-1] != 'e')) //如果已经出现了符号但是这个+-号不在E/e之后
					return false;
				if(!havesignal && i > 0 && str[i-1] != 'E' && str[i-1] != 'e')
					return false;
				havesignal = true;
			} else if(str[i] == '.'){
				if(haveRadix) //不能有多个小数点
					return false;
				if(haveE) //小数点不能在E/e之后
					return false;
				haveRadix = true;
			} else if(!(str[i] >= '0' && str[i] <= '9')){
				return false;
			}
		}

		return true;
	}


	public static void main(String[] args){
		String s1 = "+100";
		String s2 = "5e2";
		String s3 = "-123";
		String s4 = "3.14159";
		String s5 = "-1E-16";
		String s6 = "12e";
		String s7 = "1a3.14";
		String s8 = "1.2.3";
		String s9 = "+-5";
		String s10 = "12e+5.4";
		System.out.println("s1 " + isNumeric(s1.toCharArray())); //true
		System.out.println("s2 " + isNumeric(s2.toCharArray())); //true
		System.out.println("s3 " + isNumeric(s3.toCharArray())); //true
		System.out.println("s4 " + isNumeric(s4.toCharArray())); //true
		System.out.println("s5 " + isNumeric(s5.toCharArray())); //true
		System.out.println("s6 " + isNumeric(s6.toCharArray())); //false
		System.out.println("s7 " + isNumeric(s7.toCharArray())); //false
		System.out.println("s8 " + isNumeric(s8.toCharArray())); //false
		System.out.println("s9 " + isNumeric(s9.toCharArray())); //false
		System.out.println("s10 " + isNumeric(s10.toCharArray())); //true
		char[] cs = {'a','b'};
		System.out.println(String.valueOf(cs));
	}
}

```