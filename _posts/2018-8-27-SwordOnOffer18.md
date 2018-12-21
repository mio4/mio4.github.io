---
layout: post
title:  "数组中出现次数超过一半的数字"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}








## 数组中出现次数超过一半的数字

**题目描述**
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

**分析**

### 解法1
 - 可以使用面向对象的思想，将数字和数字出现的次数封装，遍历一遍数组，同时每次遍历结果集
 - 这种方法思路简单，缺点就是时间复杂度太大（O(n^2)），可以优化

```java 
public class Solution {
	public int MoreThanHalfNum_Solution(int [] array) {
		int len = array.length;
		ArrayList<Num> nums = new ArrayList<Num>();
		for(int i=0; i < len;i++){
			int j = 0;
			for(; j < nums.size(); j++){
				if(array[i] == nums.get(j).num) {
					nums.get(j).cnt++;
					break;
				}
			}
			if(j == nums.size())
				nums.add(new Num(array[i]));
		}
		for(int i=0; i < nums.size(); i++){
			if(nums.get(i).cnt >= len/2)
				return nums.get(i).num;
		}
		return 0;
	}
}
class Num {
	public int num;
	public int cnt = 0;
	public Num(int num){
		this.num = num;
	}
}
```

### 解法2
 - 如果使用快速排序后，统计出现次数就很方便，这种方法时间复杂度为O(nlogn)

```java 
public class Solution2 {
	public int MoreThanHalfNum_Solution(int [] array) {
		Arrays.sort(array);
		int len = array.length;
		int before = array[0];
		int cnt = 1;
		if(len == 1)
			return array[0];
		for(int i=1; i < len; i++){
			if(cnt > len/2)
				return before;
			if(array[i] != before){
				cnt = 1;
				before = array[i];
			} else {
				cnt++;
			}
		}
		return 0;
	}
}

```

### 解法3
 - 考虑使用时间复杂度为O(n)的解法
 - 两个边界条件处理
   - 传入的数组是否为空
   - 整个数组都没有出现次数大于len/2的数时的处理
 - 设立一个全局变量times,如果数前面的数相同，则times+1，如果不同则times-1，如果times=0则更新前面的数，对于数组中出现次数大于len/2的数（前提是的确存在这个数），一定是最后times=1时更新的那个数


```java 
public class Solution3 {
	public static int MoreThanHalfNum_Solution(int [] array) {
		if(array.length <= 0) //检查数组有效性
			return 0;
		int result = array[0];
		int times = 1;
		int len = array.length;
		for(int i=1; i < len; i++){
			if(array[i] == result)
				times++;
			else
				times--;
			if(times == 0) {
				result = array[i];
				times = 1;
			}
		}
		if(!checkIfMoreThanHalf(array,result))
			return 0;
		return result;
	}
	public static boolean checkIfMoreThanHalf(int[] array, int result){
		boolean flag = false;
		int len = array.length;
		int times = 0;
		for(int i=0; i < len; i++){
			if(array[i] == result)
				times++;
		}
		if(times * 2 > len)
			flag = true;
		return flag;
	}
	public static void main(String[] args){
		int[] a = {1,2,3,2,2,2,5,4,2};
		int[] b = {1,2,3,2,4,2,5,2,3};
		//System.out.println(MoreThanHalfNum_Solution(a));
		System.out.println(MoreThanHalfNum_Solution(b));
	}
}

```



### 解法4
 - 待补充：使用Partition函数的时间复杂度为O(1)的算法