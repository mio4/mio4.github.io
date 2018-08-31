---
layout: post
title:  "剑指Offer面试题：扑克牌顺子"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}






## 扑克牌顺子


**题目描述**
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

**分析**

 - 输入的是一个长度为5的数组，数组的值在0~13的范围
 - 对数组排序之后，首先求出大小王的个数，然后判断是否存在相同的数，如果存在则一定不是连续正数序列
 - 统计牌之间的差距，看是否能够通过大小王的个人来填补空缺的位置

```java 
import java.util.Arrays;

public class Solution {
	public boolean isContinuous(int [] numbers) {
		Arrays.sort(numbers);

		//0的个数
		int len = numbers.length;
		int zero_cnt = 0;
		for(int i=0; i < len; i++){
			if(numbers[i] == 0)
				zero_cnt++;
		}
		//如果存在对子，那么一定不是顺子
		for(int i=zero_cnt; i < len-1; i++){
			if(numbers[i] == numbers[i+1])
				return false;
		}
		//统计数之间的差距
		int sum = 0;
		for(int i=zero_cnt; i < len-1; i++){
			if(numbers[i+1] - numbers[i] > 1)
				sum = sum + numbers[i+1] - numbers[i] - 1;
		}
		return (sum <= zero_cnt);
	}
}
```