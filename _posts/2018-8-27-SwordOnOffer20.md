---
layout: post
title:  "二叉树的深度"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}








## 二叉树的深度

**题目描述**
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

**分析**

 - 首先要理解什么是二叉树的深度
 - 最开始想到的是对二叉树进行前序遍历，得到最深的根节点，但是这样需要对比各个栈的深度，比较难处理
 - 然后对于树，最多的操作是递归操作：将二叉树深度定义为根节点+Max（左子树深度，右子树深度），递归处理即可

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
	public int TreeDepth(TreeNode root) {
		if(root == null)
			return 0;
		if(root.left == null && root.right == null)
			return 1;
		return Max(TreeDepth(root.left),TreeDepth(root.right)) + 1;
	}
	public int Max(int a, int b){
		if(a > b)
			return a;
		return b;
	}
}
```