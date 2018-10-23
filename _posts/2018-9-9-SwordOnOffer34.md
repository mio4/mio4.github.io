---
layout: post
title:  "把数组排成最小的数"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}






## 把数组排成最小的数

**题目描述**
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323


**分析**

 - 最开始想到的是将所有的排列情况枚举出来，然后使用字符串比较对于所有的情况进行排序，但是这样就做成了全排列的题（涉及到回溯）
 - 其实也不需要全局对比，只需要局部进行比较就可以得到“升序”的顺序
   - 自定义Compare函数：对于字符串A、B，如果字典序AB > BA，则定义为A>B
   - 将int数组转换为String数组，对数组进入冒泡排序
   - 将升序结果加起来就是需要的字符串 


```java 
public class Solution {
	public static String PrintMinNumber(int [] numbers) {
		String result = "";
		if(numbers == null)
			return null;
		if(numbers.length == 0)
			return result;
		int len = numbers.length;


		String[] strs = new String[numbers.length];
		for(int i=0; i < len; i++){
			strs[i] = String.valueOf(numbers[i]);
		}
		BubbleSort(strs,len);

		for(int i=0; i < len; i++){
			result += strs[i];
		}
		return result;
	}

	public static void BubbleSort(String[] strs, int len){
		for(int i=0; i < len; i++){
			for(int j=0; j < len-1-i;j++){
				if(BiggerThanOrEqual(strs[j],strs[j+1])){
					String temp = strs[j];
					strs[j] = strs[j+1];
					strs[j+1] = temp;
				}
			}
		}
	}

	public static boolean BiggerThanOrEqual(String a, String b){  //a是否大于等于b
		String ab = a + b;
		String ba = b + a;
		int len = ab.length();
		for(int i=0; i < len; i++){
				if(ab.charAt(i) > ba.charAt(i))
					return true;
				else if(ab.charAt(i) < ba.charAt(i))
					return false;
		}
		return true;
	}

	public static void main(String[] args){
		int[] a = {3,32,321};
		System.out.println(PrintMinNumber(a));
	}
}
```


