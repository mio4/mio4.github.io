---
layout: post
title:  "二进制中1的个数"
categories: 剑指Offer  
tags: DataStructure Offer 
author: mio4
---

* content
{:toc}








## 二进制中1的个数

**题目描述**
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
**分析**

 - 这道题最开始的想法是将十进制转为二进制数 ，然后二进制每移动一位判断是否为1，直到二进制数为0，但是这种情况下对于负数的转换很难处理。
 - 实质上考察的是二进制的位运算
   - 对于二进制数n，n-1与n的与运算会消除n的最右边一位1
   - 这样有多少个1，循环就会执行多少次
 - 这种处理方式将正数、负数的情况统一，非常巧妙    

```java 
public class Solution {
    public int NumberOf1(int n) {
        int count = 0;
        while(n != 0){
            count++;
            n = (n-1) & n;
        }
        return count;
    }
}
```