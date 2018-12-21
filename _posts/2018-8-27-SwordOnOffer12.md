---
layout: post
title:  " 二叉树的镜像"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}








## 二叉树的镜像

**题目描述**
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树 
​    	    8
​    	   /  \
​    	  6   10
​    	 / \  / \
​    	5  7 9 11
​    	镜像二叉树
​    	    8
​    	   /  \
​    	  10   6
​    	 / \  / \
​    	11 9 7  5
​		
​		
**分析**

 - 这道题Wrong了几次，是因为没有考虑到空树的情况导致了NullPointerException
 - 首先由图可知镜像就是对于非叶子节点，树的左右子树交换
   - 所以可以使用递归，交换左右节点之后，对左右子树进行相同操作
 - 边界条件
   - 需要在一开始判断root是否为null，针对一开始就是空树的情况   

```java 
class TreeNode {
	 int val = 0;
	 TreeNode left = null;
	 TreeNode right = null;

	 public TreeNode(int val) {
	 this.val = val;

	 }
 }

public class Solution {
	public void Mirror(TreeNode root) {
		if(root != null) {
			if (root.left != null || root.right != null) { //交换节点
				TreeNode tmpNode = root.left;
				root.left = root.right;
				root.right = tmpNode;
			}
			if (root.left != null)
				Mirror(root.left);
			if (root.right != null)
				Mirror(root.right);
		}
	}
}

```