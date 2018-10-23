---
layout: post
title:  " 包含min函数的栈"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 包含min函数的栈

**题目描述**
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

**分析**

 - 题目要求在给定的时间复杂度内完成对于最小元素的查找
   - 但是并没有规定空间复杂度，也就是在暗示可以使用额外的存储空间
 - 对于O(1)的时间复杂度，可以考虑使用一个额外栈来保存对应时刻的最小值，两个栈具有同步性
   - 这里需要注意假如栈顶是最小值时又弹出了元素，需要对辅助栈也同时进行更新
 - 总结
   - 一般的提醒规定了时间复杂度，就可以利用辅助空间来安排算法；如果规定了空间复杂度，那么就对于时间复杂度的要求相对变低，对于解题也是一种提示  



```java 
import java.util.Stack;

public class Solution {
	public Stack<Integer> val_stack = new Stack<Integer>();
	public Stack<Integer> min_stack = new Stack<Integer>();
	public int min = Integer.MAX_VALUE;

	public void push(int node) {
		val_stack.push(node);
		if(node < min)
			min = node;
		min_stack.push(min);
	}

	public void pop() {
		if(!val_stack.isEmpty()) {
			val_stack.pop();
			min_stack.pop();
		}
	}

	public int top() {
		int min = min_stack.pop();
		min_stack.push(min);
		return min;
	}

	public int min() {
		return top();
	}
}

```