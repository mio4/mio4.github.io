---
layout: post
title:  "Java基础笔记()：字符串"
categories: Java基础
tags:  JavaSE
author: mio4
---

* content
{:toc}






> 字符串可以说是Java编程中最常使用的类型，但是学习一门语言不光是只是调用API就算“学懂了”，只会调用API的Fresh Hand不算真正的Coder，正如这个只会调参机器学习烂大街的时候，如果不能深入了解背景和原理，就会在Bug Writer的路上越走越远
>
> 在谈到到String的时候，肯定是要涉及Java内存管理比如常量池、堆区，JVM又是逃不掉的一块

# （一）String

> String一旦被初始化，不可被改变
>
> 备注：String复写了Object的equals方法
>
> equals比较的是字符串的值，而 ==是通用方法，比较两个对象的地址

```java
		//s1：从常量池中创建的"mio"，一个对象
		//s2：new出来的对象存放在堆区，加上常量池已有的"mio"对象
		//s3：此时常量池中已有"mio"对象，直接引用
		String s1 =  "mio";
		String s2 = new String("mio");
		String s3 = "mio";

		System.out.println(s1 == s2); //false
		System.out.println(s1.equals(s2)); //true
		System.out.println(s1 == s3); //true
```



# （二）StringBuilder

StringBuilder不是线程安全的， 但是在单线程的情况下性能比StringBuffer更好

```java
		StringBuilder sb = new StringBuilder();
```











# （三）StringBuffer

StringBuffer是一个字符串容器，StringBuffer是线程安全的字符序列


```java
		StringBuffer sb = new StringBuffer(); 
		StringBuffer sb = new StringBuffer(String str); 
```

> 只需要了解常用方法即可，剩下的查询API，只需要关注重要的细节

- 添加：append()，返回值就是当前StringBuffer对象
- 删除：delete(int from, int to)：返回值是StringBuffer对象
  - deleteCharAt(int index)：删除制定位置的元素
- 替换：replace()


























