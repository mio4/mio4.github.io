---
layout: post
title:  "剑指Offer面试题：反转链表"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 反转链表


**题目描述**
输入一个链表，反转链表后，输出新链表的表头。

**分析**

 - 注意代码的鲁棒性，考虑链表的三种情况
   - 链表为空
   - 链表只有一个元素，反转之后头节点不变
   - 链表有多个元素的一般情况
 - 使用三个指针记录pre now next：前驱节点、当前节点、后继节点，从左往右移动指针，直到链表末尾即可
   - 特别要注意preNode和nowNode的赋值顺序，不然会造成死循环  

```java 
class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
public class Solution {
	public ListNode ReverseList(ListNode head) {
		ListNode reverseListHead = null; //针对空链表的情况进行初始化
		ListNode preNode = null; //头节点前面是null
		ListNode nowNode = head;
		while(nowNode != null){
			ListNode nextNode = nowNode.next;
			//处理链表只有一个节点的情况
			if(nextNode == null)
				reverseListHead = nowNode;
			//处理一般多节点的链表
			nowNode.next = preNode;
			preNode = nowNode;
			nowNode = nextNode;
		}
		return reverseListHead;
	}
}

```