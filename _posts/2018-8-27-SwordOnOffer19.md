---
layout: post
title:  "剑指Offer面试题：翻转单词顺序列"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 翻转单词顺序列
 - 算法：首先将整个句子翻转一遍，然后对每个单词进行翻转
 - 需要考虑两种边界情况
   - 输入字符串是空字符串
   - 输入的字符串只有一个单词，不需要进行翻转（这种情况更难处理）：使用一个专门检查字符串是否为单个单词的函数即可 
 - 残留问题：本地能够通过对于输入字符串为""和" "的输出，OJ上会出现对输入" "的异常java.lang.StringIndexOutOfBoundsException: String index out of range: 3 

**分析**

```java 
public class Solution {
	public static String ReverseSentence(String str) {
		if(str.equals(" "))
			return str;
		if(str == null || str == "") //如果是空字符串
			return str;
		int len = str.length();
		char[] chars = str.toCharArray();
		if(checkIfOneWord(chars))
			return str;
		ReverseWord(chars,0,len-1);
		int i = 0;
		int before_blank = 0;
		int next_blank = 0;
		while(i < len){
			if(chars[i] == ' '){
				next_blank = i;
				ReverseWord(chars,before_blank,next_blank-1);
				i++;
				before_blank = i;
			} else{
				i++;
			}

		}
		String result = new String(chars);
		return result;
	}

	public static void ReverseWord(char[] chars, int left, int right){
		while(left < right){
			char tmp = chars[left];
			chars[left] = chars[right];
			chars[right] = tmp;
			left++;
			right--;
		}
	}

	public static boolean checkIfOneWord(char[] chars){
		for(int i=0; i < chars.length; i++){
			if(chars[i] == ' ')
				return false;
		}
		return true;
	}

	public static void main(String[] args){
		String str = "I am a student.";
		String s2 ="Wonderful";
		System.out.println(ReverseSentence(" "));
		System.out.println(ReverseSentence(str));
		System.out.println(ReverseSentence(s2));
	}
}

```