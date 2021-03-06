---
layout: post
title:  "Java基础笔记(1)：数组"
categories: Java基础
tags:  JavaSE
author: mio4
---

* content
{:toc}




## （一）创建数组

 ```java
  Sphere[] a; //尚未初始化的局部变量
  Sphere[] b = new Sphere[size]; //new方法创建,保存在堆中，必须给定数组维度
  Sphere[] c = {new Sphere(), new Sphere(), new Sphere()}; //动态，必须在定义的时候初始化
 ```

**length属性**：
 - length表示数组的大小，即最多能够容纳多少个元素
 - length并不表示实际容纳元素的个数，因为数组初始化的null也会被计数

## （二）数组与泛型


## （三）常用方法
### (1)System.arrayCopy
 >浅复制：只复制对象的引用，不复制对象本身

 - System.arrayCopy()的效率比for循环高
 - System.arrayCopy(源数组，srcPos,目标数组，dstPos，复制长度)
 - System.arrayCopy是一种浅复制
 - 拷贝的数组和原数组的数据类型必须相同

### (2)Arrays.equals
 - arrays.equals(Object[] o1, Object[] o2)比较两个数组是否相等
 - 具体的方法是比较数组中对应位置的元素是否相等（通过Object.equals()比较）,也就是基于内容比较

### (3)Arrays.sort
 - 对数组中的元素进行排序，由小到大的方式

### (4)Arrays.deepToString
 - Arrays.deepToString()方法将多维数组以String类型的方式表示出来，使用[]进行分离
 - 对于基本数据类型和对象数组都起作用

### (5)Arrays.fill
 - 对数组填充特定的元素

## （四）总结
 - Array相对于ArrayList，优势在于效率，但是灵活度不够
 - 优先使用容器，在性能成为瓶颈的时候考虑使用数组