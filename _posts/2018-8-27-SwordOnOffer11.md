---
layout: post
title:  "剑指Offer面试题：合并两个排序的链表"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 合并两个排序的链表

**题目描述**
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

**分析**

 - 边界条件
   - 两个链表中存在一个是空链表
   - 两个链表都是空链表
   - 两种边界条件可以合并处理
 - 最开始考虑写循环，语句比较繁琐
 - 即使从list1或者list2中选择了一个节点，剩下的问题没有发生变化
 - 所以可以使用递归：分从list1或者list2取出第一个节点的两种情况处理即可   

```java 
class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
public class Solution {
	public ListNode Merge(ListNode list1,ListNode list2) {
		//假设存在空链表
		if(list1 == null)
			return list2;
		if(list2 == null)
			return list1;

		//对于一般情况
		ListNode pMergeHead = null;
		if(list1.val < list2.val){
			pMergeHead = list1;
			pMergeHead.next = Merge(list1.next,list2);
		}
		else{
			pMergeHead = list2;
			pMergeHead.next = Merge(list1,list2.next);
		}

		return pMergeHead;
	}
}

```