---
layout: post
title:  "剑指Offer面试题：滑动窗口的最大值"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}






## 滑动窗口的最大值

**题目描述**
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

**分析**

 - 边界条件:只需要返回一个为空的ArrayList即可
   - size小于等于0以及size大于数组长度时
   - 数组为null时
 - 没有优化过的算法复杂度为O(nk) 

```java 
import java.util.ArrayList;

public class Solution {
	public static ArrayList<Integer> maxInWindows(int [] num, int size)
	{
		ArrayList<Integer> result = new ArrayList<Integer>();
		int len = num.length; //对于数组取长为length属性，对于ArrayList取长为size()方法
		if(num == null ||size <= 0 ||  size >len) //对于边界情况进行考虑
			return result;

		//对于一般情况的一般算法
		int j = 0;
		while(j <= len-size){
			int max = num[j];
			for(int i=j; i < size+j; i++)
				if(num[i] > max)
					max = num[i];
			result.add(max);
			j++;
		}

		return result;
	}
}
```

 - 使用队列，可以优化时间复杂度
   - 使用LinkedList模拟队列，存储的是数组的下标
   - 第一个窗口比较特殊，首先是找到第一个窗口的最大值 
   - 对于后面每次移动一个位置，新元素如果比队列尾部的元素大， 则弹出队列尾部元素
   - 新元素可能会是后面窗口的最大值，所以一定会进入队列
   - 注意每次判断队首元素是否在窗口里
   - 队首元素一定是最大值，添加到结果集

```java 
import java.util.ArrayList;
import java.util.LinkedList;
public class Solution {
    public ArrayList<Integer> maxInWindows(int [] num, int size)
    {
        ArrayList<Integer> result = new ArrayList<Integer>();
		if(num == null ||size <= 0 || size > num.length)
			return result;

		LinkedList<Integer> indexQueue = new LinkedList<Integer>(); //下标队列

		for(int i=0; i < size; i++){
			if(!indexQueue.isEmpty() && num[i] > num[indexQueue.getLast()])
				indexQueue.removeLast();
			indexQueue.addLast(i);
		}
		result.add(num[indexQueue.getFirst()]); //第一个窗口开放之后，队首元素就是最大值

		for(int i=size; i < num.length; i++){
			while(!indexQueue.isEmpty() && num[i] > num[indexQueue.getLast()])
				indexQueue.removeLast();
			indexQueue.addLast(i);
			if(i - indexQueue.getFirst() >= size)
				indexQueue.removeFirst();
			result.add(num[indexQueue.getFirst()]);
		}

		return result;
    }
}
```
