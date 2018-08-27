---
layout: post
title:  "剑指Offer面试题：用两个栈实现队列"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 用两个栈实现队列

**题目描述**
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

**分析**

 - 首先可以自己尝试使用1 2 3少量元素的入栈出栈摸索两个栈的使用，从特殊到一般
 - 最开始出栈的时候将栈1的元素弹出再次压进栈2，然后栈2此时最顶上的元素是最开始进来的元素，弹出即可
 - 对于一般情况下的出栈：如果栈2不为空，弹出栈2栈顶元素；如果栈2位空，将栈1所有的元素依次压入栈2
 - 对于入栈：直接压入栈1即可

```java 
import java.util.Stack;

public class Solution {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();
    
    public void push(int node) {
        stack1.push(node);
    }
    
    public int pop() {
        if(stack2.size() != 0){
			return stack2.pop();
		}
		while(stack1.size() != 0){
			stack2.push(stack1.pop());
		}
		int res = stack2.pop();
		return res;
    }
}
```
