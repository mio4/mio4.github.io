---
layout: post
title:  "剑指Offer面试题：序列化二叉树"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}






## 序列化二叉树


**题目描述**
请实现两个函数，分别用来序列化和反序列化二叉树


 **分析**
  - 序列化：将对象的信息/状态转换为可以存储的方式
  - 反序列化：将存储的信息转换为对象
  - 对本题来说就是将多维的二叉树转换为一维数组，以及提取一维数组信息还原二叉树的过程
  - 序列化很简单，对于空节点使用$符号代替，将树分为根节点、左子树、右子树递归遍历（前序）加入数组
  - 反序列化也是同样递归处理

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
	public static int cnt = -1;
	public static String Serialize(TreeNode root) {
		StringBuffer sb = new StringBuffer();
		if(root == null){
			sb.append("$,");
			return sb.toString();
		}
		sb.append(root.val + ",");
		sb.append(Serialize(root.left));
		sb.append(Serialize(root.right));
		return sb.toString();
	}
	public static TreeNode Deserialize(String str) {
		cnt++;
		String[] strs = str.split(",");
		TreeNode node = null;
		if(!strs[cnt].equals("$") ) {
			node = new TreeNode(Integer.valueOf(strs[cnt]));
			node.left = Deserialize(str);
			node.right = Deserialize(str);
		}
		return node;
	}

	public static void main(String[] args){
		TreeNode root = new TreeNode(1);
		TreeNode p1 = new TreeNode(2);
		TreeNode p2 = new TreeNode(3);
		root.left = p1;
		root.right = p2;
		String str = Serialize(root);
		Deserialize(str);
	}
}

```

 - 难点在于反序列化
   - 上述中cnt的作用是记录对于str的解析位置，从0开始，每次生成一个节点则+1
   - 有意义的节点一定是不为$并且由于cnt约束一定是先前没有生成的，同时由于递归在字符串数组中也会满足根节点-左子树部分-右子树部分的解析顺序 