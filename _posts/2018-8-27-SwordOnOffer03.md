---
layout: post
title:  "重建二叉树"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}







## 重建二叉树

**题目描述**
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

**分析**

 - 这是一道比较基础的二叉树问题
 - 前序遍历的第一个节点一定是根节点，首先得到根节点，然后利用根节点将中序遍历分为左子树部分+根节点+右子树部分
 - 然后发现左右子树的处理情况是相同的，使用递归即可

```java 
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        if((pre.length <= 0 && in.length <= 0) || pre.length != in.length)
			return null;
		//首先找到根节点
		TreeNode root = new TreeNode(pre[0]);
		//然后找到左右子树
		int middle = 0;
		for(int i=0; i < pre.length; i++){
			if(in[i] == pre[0])
				middle = i;
		}
		//数组边界条件：大小为零
		int[] new_pre_left = new int[middle];
		int[] new_pre_right = new int[in.length - middle - 1];
		int[] new_in_left = new int[middle];
		int[] new_in_right = new int[in.length - middle - 1];

		for(int i=0; i < middle; i++){
			new_pre_left[i] = pre[i+1];
			new_in_left[i] = in[i];
		}
		for(int i=0; i < in.length - middle - 1; i++){
			new_pre_right[i] = pre[i+middle+1];
			new_in_right[i] = in[i+middle+1];
		}
		//根据左右子树递归生成新的树
		root.left = reConstructBinaryTree(new_pre_left, new_in_left);
		root.right = reConstructBinaryTree(new_pre_right, new_in_right);
		
		return root;
    }
}
```

 - 第一遍AC的代码比较繁琐，使用Java库函数可以化简后半部分关于数组的操作：

```java 
import java.util.*;
public class Solution {
    public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        if((pre.length <= 0 && in.length <= 0) || pre.length != in.length)
			return null;
		//首先找到根节点
		TreeNode root = new TreeNode(pre[0]);
		//然后找到左右子树
		int middle = 0;
		for(int i=0; i < pre.length; i++){
			if(in[i] == pre[0])
				middle = i;
		}
		
        root.left = reConstructBinaryTree(Arrays.copyOfRange(pre,1,middle+1),Arrays.copyOfRange(in,0,middle));
		root.right = reConstructBinaryTree(Arrays.copyOfRange(pre,middle+1,in.length),Arrays.copyOfRange(in,middle+1,in.length));
		
        return root;
    }
}
```