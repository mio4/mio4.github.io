---
layout: post
title:  "剑指Offer面试题：正则表达式匹配"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}





## 正则表达式匹配
**题目描述**
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

**分析**

  - 本题字符串匹配本质上是构造一个有限状态机
    - 首先可以从给出的实例开始分析匹配方式
  - 模式中的字符可以分为两类，一种是普通字符和'.'，另外一种是'*'表示特定的匹配模式，本身不等价任何字符
  - 首先是边界条件判断：是否匹配到字符串末端
  - 然后分两种情况：
    - (1) 模式第二个字符是'*'，此时进入有限状态机的转换:
    - (1.1) '*'字符当做**只出现一次**的情况，字符串使用1个字符，模式使用2个字符
    - (1.2) '*'字符当做**出现多次**的情况，字符串使用1个字符，模式不移动（不使用字符）
    - (1.3) '*'字符当做**不出现**的情况，字符串不移动（不使用字符），模式使用2个字符
    - (2) 模式的第二个字符不是'*'，那么递归判断除开第1个字符的字符串和除开第1个字符的模式是否匹配
  - 本题很有意思，适合二刷 

```java 
import java.util.Arrays;

public class Solution {
	public static boolean match(char[] str, char[] pattern)
	{
		if(str == null || pattern == null) //对于边界进行处理
			return false;
		return MatchCore(str,pattern);
	}

	public static boolean MatchCore(char[] str, char[] pattern){
		if(str.length == 0 && pattern.length == 0) //都匹配到字符串末端
			return true;
		if(str.length != 0 && pattern.length == 0) //模式已经用光，字符串还有剩余的情况
			return false;

		if(pattern.length > 1 && pattern[1] == '*'){ //对于模式第二个字符是*
			if(str.length > 0 && (pattern[0] == str[0] || pattern[0] == '.' && str.length != 0))
				return MatchCore(Arrays.copyOfRange(str,1,str.length),Arrays.copyOfRange(pattern,2,pattern.length))
				|| MatchCore(Arrays.copyOfRange(str,1,str.length),pattern)
				|| MatchCore(str,Arrays.copyOfRange(pattern,2,pattern.length));
			else
				return MatchCore(str,Arrays.copyOfRange(pattern,2,pattern.length));
		}

		if(str.length!=0 && (pattern[0] == str[0] || pattern[0] == '.' && str.length != 0)) //对于一般的匹配情况
			return MatchCore(Arrays.copyOfRange(str,1,str.length),Arrays.copyOfRange(pattern,1,pattern.length));

		return false;
	}

	public static void main(String[] args){
		char[] str = {'a','a','a'};
		char[] pattern = {'a','.','a'};
		System.out.println(match(str,pattern));

		char[] str2 = {'a','a','a'};
		char[] pattern2 = {'a','b','*','a','c','*','a'};
		System.out.println(match(str2,pattern2));

		char[] str3 = {'a','a','a'};
		char[] pattern3 = {'a','a','.','a'};
		System.out.println(match(str3,pattern3));

		char[] str4 = {};
		char[] pattern4 = {'.','*'};
		System.out.println(match(str4,pattern4));
	}
}

```