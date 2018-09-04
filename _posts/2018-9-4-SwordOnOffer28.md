---
layout: post
title:  "剑指Offer面试题：删除链表中重复的结点"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}






## 删除链表中重复的结点

**题目描述**
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

**分析**

 - 首先要意识到“有序”这个条件是一定要使用的
 - 链表头也可能会被“删除”，这种情况需要考虑
 - 关于删除的方式：是一次删除一个点，还是删除一对点？最好的方式是直接将前驱节点指向比当前节点值更大的后继节点
 - 设立三个节点只需要遍历一遍链表即可完成操作，注意对节点的更新和初始化
 - 测试案例
   - 1->1
   - 1->1->2->3
   - 1->2->3->3->4->4->5
   - null
   - 2->3 

```java 
class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
public class Solution {
	public static ListNode deleteDuplication(ListNode pHead)
	{
		if(pHead == null || pHead.next == null) //空节点以及单个节点特殊情况
			return pHead;

		ListNode preNode = null; //记录当前节点的前驱节点
		ListNode nowNode = pHead; //当前节点
		ListNode postNode = pHead; //记录比当前节点数值大的节点
		while(nowNode != null && nowNode.next != null){
			if(nowNode.val == nowNode.next.val){
				while(postNode.val <= nowNode.val){
					postNode = postNode.next;
					if(postNode == null)
						break;
				}
				if(preNode == null) {
					pHead = postNode;
				} else {
					preNode.next = postNode;
				}
				nowNode = postNode;
			} else{
				preNode = nowNode;
				nowNode = nowNode.next;
			}
		}
		return pHead;
	}

	public static void main(String[] args){
		ListNode l1 = new ListNode(1);
		ListNode l2 = new ListNode(2);
		ListNode l3 = new ListNode(3);
		ListNode l4 = new ListNode(3);
		ListNode l5 = new ListNode(4);
		ListNode l6 = new ListNode(4);
		ListNode l7 = new ListNode(5);
		l1.next = l2;
		l2.next = l3;
		l3.next = l4;
		l4.next = l5;
		l5.next = l6;
		l6.next = l7;
		deleteDuplication(l1);
		System.out.println(l1);
	}
}

```