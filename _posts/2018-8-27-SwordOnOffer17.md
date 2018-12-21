---
layout: post
title:  "二叉搜索树的后序遍历序列"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}








##  二叉搜索树的后序遍历序列
**题目描述**
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

**分析**

 - 合法的二叉搜索树的后序遍历序列很多，所以首先默认序列是合法的
 - 然后只需要对于不合法的情况进行判定，同时涉及到二叉树的题型考虑使用递归解法
   - 首先序列的最后一个元素一定是根节点
   - 然后可以将剩余部分分为左子树部分和右子树部分
   - 对于找到的右子树部分，如果树中有任意一个节点值小于根节点值，那么整个序列是非法序列 
 - 对于二叉树，在提交OJ之前需要自己判断根节点为空的情况（或者输入对象是空对象的情况）下，程序是否能够正常运行

```java 
import java.util.Arrays;
public class Solution {
    public boolean VerifySquenceOfBST(int [] sequence) {
        int len = sequence.length;
        if(len <= 0)
			return false;
		int root = sequence[len-1];
		int index = -1;
		boolean flag = true;
		for(int i=0; i < len-1; i++){
			if(sequence[i] > root){
				index = i;
				break;
			}
		}
		if(index == -1){ //说明没有存在右子树遍历的情况
			index = len-1;
		}
		int[] left_arr =  Arrays.copyOfRange(sequence,0,index);
		int[] right_arr = Arrays.copyOfRange(sequence,index,len-1);

		for(int i=index; i < len-1; i++){
			if(sequence[i] < root)
				return false;
		}
		if(index > 1){ //这里保证数组的长度必须大于1
			flag = flag & VerifySquenceOfBST(left_arr);
		}
		if(len-index > 1){
			flag = flag & VerifySquenceOfBST(right_arr);
		}
		return flag;
    }
}
```

