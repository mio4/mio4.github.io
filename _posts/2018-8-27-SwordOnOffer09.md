---
layout: post
title:  "链表中倒数第k个结点"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 链表中倒数第k个结点
**题目描述**
输入一个链表，输出该链表中倒数第k个结点。
**分析**

 - 这是一道在面试中比较常见的问题
 - 可以首先遍历一遍链表得到长度n，然后遍历时取第n-k+1个节点就是目标节点，虽然时间复杂度为O(n)，但是需要遍历两遍链表
 - 使用双指针的方式只用遍历一遍链表就能得到倒数第k个节点：首先让两个指针距离为k-1，然后往后同时移动两个指针，这样第二个指针指向最后一个节点时，第一个指针指向的节点距离最后一个节点为k-1，即是倒数第k个节点
 - 需要注意的边界条件
   - 输入的链表是空链表
   - 链表的长度实质上并没有达到k   

```java 
class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
public class Solution {
	public ListNode FindKthToTail(ListNode head,int k) {
		ListNode p1 = head;
		if(p1 == null || k <= 0)
			return null;
		for(int i=0; i < k-1; i++){
			if(p1.next == null)
				return null;
			p1 = p1.next;
		}
		ListNode p2 = head;

		while(p1.next != null){
			p1 = p1.next;
			p2 = p2.next;
		}
		return p2;
	}
}

```