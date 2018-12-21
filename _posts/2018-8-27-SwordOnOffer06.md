---
layout: post
title:  "斐波那契数列 | 跳台阶 | 矩形覆盖"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}








##斐波那契数列

**题目描述**
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

**分析**

 - 求解斐波那契数列是特别基础和常见的一道题，解法参考《剑指Offer》

### (1)递归求解

 - 效率不高，基本不会在实际中使用

```java 
public class Solution {
    public int Fibonacci(int n) {
        if(n == 0)
            return 0;
        if(n == 1)
            return 1;
        return Fibonacci(n-1) + Fibonacci(n-2);
    }
}
```
### (2)循环求解

 - 从前往后循环求解，直到第n项，时间复杂度为O(n)

```java 
public class Solution {
    public int Fibonacci(int n) {
        int[] results = {0,1};
        if(n < 2)
            return results[n];
        
        int fibN = 0;
        int fibNMinusOne = 1; //第倒数n-1项
        int fibNMinusTwo = 0; //第倒数n-2项
        
        for(int i=2; i <= n; i++){
            fibN = fibNMinusOne + fibNMinusTwo;
            fibNMinusTwo = fibNMinusOne;
            fibNMinusOne = fibN;
        }
        
        return fibN;
    }
}
```

### (3)矩阵迭代求解

>占位，后期补充

## 补充模型：跳台阶

**题目描述**
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

**分析**
就是斐波那契数列套上了一个故事模型而已：

  - 第一次跳1级，剩下的有F(n-1)种跳法
  - 第一次跳2级，剩下的有F(n-2)种跳法

```java 
public class Solution {
    public int JumpFloor(int target) {
        if(target == 1)
            return 1;
        if(target == 2)
            return 2;
        return JumpFloor(target-1)+JumpFloor(target-2);
    }
}
```

## 跳台阶变种
**题目描述**
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

**分析**

 -  数学归纳法可证明有2^(n-1)种方法

```java 
public class Solution {
    public int JumpFloorII(int target) {
        int result = 1;
        for(int i=0; i < target-1; i++)
            result *= 2;
        return result;
    }
}
```

## 补充模型：矩形覆盖
**题目描述**
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

**分析**

 - 还是斐波那契数列：
   - n=0、1、2时分别有0、1、2种情况 
   - 如果竖着覆盖，则还有F(n-1)种可能
   - 如果横着覆盖，剩下的一个2*1部分只能放一个横着的，还有F(n-2)种可能 
 -  这道题OJ测试数据较大，直接使用递归会导致栈溢出

```java 
public class Solution {
    public int RectCover(int target) {
        int[] results = {0,1,2};
        if(target < 3)
            return results[target];
        
        int fibN = 0;
        int fibNMinusOne = 2; //第倒数n-1项
        int fibNMinusTwo = 1; //第倒数n-2项
        
        for(int i=3; i <= target; i++){
            fibN = fibNMinusOne + fibNMinusTwo;
            fibNMinusTwo = fibNMinusOne;
            fibNMinusOne = fibN;
        }
        
        return fibN;
    }
}
```