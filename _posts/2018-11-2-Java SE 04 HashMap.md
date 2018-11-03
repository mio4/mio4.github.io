---
layout: post
title:  "Java基础笔记(4)：HashMap"
categories: Java基础
tags:  JavaSE
author: mio4
---

* content
{:toc}







# HashMap



> 1.为什么要学习底层的原理？
>
> JDK源码大多出自专家之手，代码的逻辑性和设计思维值得学习。Coding就像写作一样，知道了什么是好的代码，自己写出来的可能性越大。
>
> 2.阅读JDK源码的姿势
>
> 一个HashMap的源码就有两千多行，如果是一行一行， 不从整体上去把握，就算花了很多时间把Utils包和并发包读完了，估计等一段时间就会忘得差不多了。
>
> 阅读源码，要从整体和细节上观察：
>
> （1）剖析数据结构
>
> （2）把握设计模式
>
> （3）基本实现原理



> 要注意的问题：
>
> 1.之所以经常使用HashMap是因为它的效率高，为什么？
>
> 2.遍历HashMap的方式



## 0x0特性

1. HashMap不是线程安全的，在高并发时可能产生死锁

   （1）HashTable是线程安全的， 不过线程安全的代价是降低程序效率

2. 元素存入HashMap中并不是按照顺序存放的，所以输出是无序的

   （1）LinkedHashMap是有序存放数据的

3. JDK7中的HashMap是基于数组+链表实现的，JDK8中的HashMap是基于数组+链表/红黑树实现的

## 0x1API

- put(key, value)：HashMap中Key是唯一的，所以对于相同的key值，后put的value会覆盖前面的value
- get(key)：通过key值可以获取对应的value
- iterator：

## 0x2源码

- HashMap有三个构造方法，默认构造方法中数组初始容量是16，加载因子是0.75。让initial capacity是2的幂的原因：这样在Put元素的时候产生的index更加均匀
- HashMap采用Hash算法确定元素在集合中存放的位置
- 为了实现一个分布尽量均匀的Hash函数，可以使用Key.hashCode()来进行，令```hash = (h = key.hashCode()) ^ (h >>> 16)``` ，```index = hash(key) & (length - 1)```，其中length是HashMap的长度，使用&运算效率比%更高





> 参考：[Java8系列之重新认识HashMap](http://www.importnew.com/20386.html)

























