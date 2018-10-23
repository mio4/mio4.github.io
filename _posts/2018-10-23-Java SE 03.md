---
layout: post
title:  "Java基础笔记(3)：抽象类&接口"
categories: Java基础
tags:  JavaSE
author: mio4
---

* content
{:toc}



# （一）抽象类

 - 如何定义一个抽象类

```java 
public abstract class ClassName(){
	abstract void f1();
	...
}
```

 - 特点
	 - **抽象类不可以用来创建对象，所以设计抽象类完全是为了继承使用**
	 - 抽象方法不能是private，原因同上
	 - 抽象类中也可以拥有普通的成员变量和方法
	 - 子类必须实现父类的抽象方法，否则子类也应该是abstract

# （二）接口

 - 如何定义一个接口

```java 
	public interface InterfaceName(){
	
	}
```

 - 特点
	 - **接口中的成员变量只能是public static final类型**
	 - 接口中的方法只能是public abstract类型
	 - (接口中不能有静态代码块或者static方法)

# （三）对比

 - 抽象类是对于事物的抽象
 - 接口是对于行为的抽象

>参考：https://www.cnblogs.com/dolphin0520/p/3811437.html
