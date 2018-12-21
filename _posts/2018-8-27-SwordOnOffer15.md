---
layout: post
title:  "栈的压入、弹出序列"
categories: 剑指Offer  
tags: DataStructure 
author: mio4
---

* content
{:toc}








## 栈的压入、弹出序列

**题目描述**
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

**分析**

 - 首先使用提供的两个例子可以找出规律
   - 如果栈顶元素和当前元素不同，从pushA中往后元素压栈，直到栈顶元素和当前元素相同，弹出栈顶元素
   - 如果pushA元素已经都入栈，栈顶元素和当前元素相同，那么不是有效序列
 - 要注意的一点是可能上次刚好遍历到pushA的最后一个元素，但是本次栈顶元素不满足条件，如果直接访问pushA的后面一个元素会造成数组溢出，所以应该将是否访问完的检查放在每次访问前
   - 此题花费时间挺多，二刷需要注意   

```java 
import java.util.Stack;
public class Solution {
    public boolean IsPopOrder(int [] pushA,int [] popA) {
        Stack<Integer> s = new Stack<Integer>();
		int len_push = pushA.length;
		int len_pop = popA.length;
		int i = 0;
		for(int j=0; j < len_pop; j++){
			int x = popA[j];
			if(s.isEmpty() || s.peek()!=x){
				while(true){
					if(i >= len_push)
						return false;
					s.push(pushA[i]);
					i++;
					if(s.peek() == x) {
						s.pop();
						break;
					}
				}
			} else {
				s.pop();
			}
		}
		return true;
    }
}
```