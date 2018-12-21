---
layout: post
title:  "从上往下打印二叉树"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}








## 从上往下打印二叉树

**题目描述**
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

**分析**

 - 和平时接触到的二叉树的前中后序遍历不一样，画图遍历例子以后其实很简单
 - 实质过程就是有个容器（队列），将当前节点值拿出来，然后当前节点出队，如果当前节点有子节点，再将左右子节点入队即可

```java 
import java.util.ArrayList;

public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }
}

public class Solution {
    public ArrayList<Integer> PrintFromTopToBottom(TreeNode root) {
        ArrayList<TreeNode> collec = new ArrayList<TreeNode>();
		ArrayList<Integer> result = new ArrayList<Integer>();
		if(root != null){
			collec.add(root);
		}
		while(collec.size() != 0){
			TreeNode tmp = collec.get(0);
			if(tmp.left != null)
				collec.add(tmp.left);
			if(tmp.right != null)
				collec.add(tmp.right);
			collec.remove(0);
			result.add(tmp.val);
		}
		return result;
    }
}
```