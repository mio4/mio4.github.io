---
layout: post
title:  "替换空格"
categories: 剑指Offer
tags: DataStructure
author: mio4
---

* content
{:toc}







## 替换空格


**题目描述**
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

**分析**

 - 最开始使用Java解题，如果是建立新的字符串拷贝原有的字符串，时间复杂度只有O(n)


```java
public class Solution {
    public String replaceSpace(StringBuffer str) {
    	StringBuffer after = new StringBuffer();
		int len = str.length();
		for(int i=0; i < len; i++){
			if(str.charAt(i) == ' ') {
				after.append("%20");
			} else {
				after.append(str.charAt(i));
			}
		}
		return after.toString();
    }
}
```

 - 看了别人的解答之后发现Java库中的replaceAll()函数能够一行代码解决问题：


```java 
public class Solution {
    public String replaceSpace(StringBuffer str) {
    	return str.toString().replaceAll(" ","%20");
    }
}
```

 - 但是这道题本身有趣的地方在于使用C/C++的指针表示字符串时，在原有字符串的基础上扩展的方式来解决问题


```c
	//占位，下次补充C指针解法
```