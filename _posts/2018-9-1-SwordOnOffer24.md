---
layout: post
title:  "字符串的排列"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}






## 字符串的排列

**题目描述**
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

**分析**

 - 只需要得到所有的字符串，然后对集合进行排序即可
 - 对于这种问题，可以先从abc的例子入手，从特殊解到一般解
   - 第一步：没有固定的字符，将a和a、b、c分别交换得到abc、bac、cba
   - 第二步：对于每一种情况，将第一个字符固定，对剩下的部分进行交换（比如对于abc，将a固定，将b和b、c进行交换得到abc、acb）
 - 将问题拆分为小的部分，很明显是一种递归，递归结束的条件是遍历到了字符串的末尾
 - 边界条件
   - 空字符串

```java
import java.util.ArrayList;
import java.util.Collections;

public class Solution {
	public ArrayList<String> Permutation(String str) {
		ArrayList<String> result = new ArrayList<String>();
		if(str == null) //边界条件
			return result;

		char[] cs = str.toCharArray();
		PermutationHelper(cs,0,result);
		Collections.sort(result);
		return result;
	}
	public void PermutationHelper(char[] cs, int i, ArrayList<String> result){ //字符集合，固定元素位置，结果集
		if(i == cs.length-1){
			if(!result.contains(new String(cs))){
				result.add(new String(cs)); //String()构造方法传参为char[]数组，生成字符串
				return; //返回到上一层
			}
		} else{
			for(int j=i; j < cs.length; j++){
				Swap(cs,i,j);
				PermutationHelper(cs,i+1,result); //这里为什么i成为了i+1？表示当前层的交换进行成功，第i个元素已经固定
				Swap(cs,i,j); //复原数组到上一步
			}
		}
	}

	public void Swap(char[] cs, int i, int j){
		char tmp = cs[i];
		cs[i] = cs[j];
		cs[j] = tmp;
	}
}
```

 - 这道题理解了很久，很有回溯法的精髓
 - 首先是变量的含义
   - i表示从下标0开始到i（不包含i）的字符是已经固定的
   - j用于从i到数组末尾的字符的交换
   - 因为数组只有一个，每次从栈中退回需要还原之前的状态
   - 对于最后的结果，使用Collections.sort()方法进行字典序排序