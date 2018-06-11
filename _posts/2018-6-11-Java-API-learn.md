---
layout: post
title:  "My first demo"
categories: SnakeSon
tags:  Ubuntu Pycharm 
author: SnakeSon
---

* content
{:toc}


## API学习

### (一)String、StringBuffer、StringBuilder

两种创建String字符串方式的区别（涉及到JVM虚拟机机制以及常量池、堆区）

```java
public class testString {
	public static void main(String[] args){
		String str1 = "hello world";
		String str2 = new String("hello world");
		String str3 = "hello world";
		String str4=  new String("hello world");

		//==对比的是两个对象的内存地址，如果内存地址相同，返回true
		//equals对比的是字符串序列是否完全相同
		System.out.println(str1 == str3); //true
		System.out.println(str1 == str2); //false
		System.out.println(str2 == str4); //false
	}
}
```

(1)str1和str3创建时，是在常量池中查找是否存在"hello world"字符串常量，存在则引用，否则创建新的常量。
(2)通过new创建的对象在堆区，堆区创建对象时不会查重，所以new出来的对象是不同的对象（即使字符串是相同的）。
(3)str1、str2、str3和str4的哈希值都是相同的

StringBuffer是线程安全的（synchonized）
StringBuilder不是线程安全的
StringBuilder和StringBuffer在大规模字符串相加的时候效率远高于String
效率：StringBuilder >= StringBuffer > String

> 通过阅读jdk中类的源码来比较区别和实现原理,javap -c的使用
> 残留问题：JVM运行机制、常量池、堆区保存元素

[Java推荐书籍](http://www.importnew.com/26932.html)

### （二）集合和包装类

Java语言是面向对象的，但是8中基本数据类型不是面向对象的，所以设计对应的包装类可以实现很多有用的API。

| 基本数据类型 | 包装类    |
| ------------ | --------- |
| short        | Short     |
| int          | Integer   |
| long         | Long      |
| char         | Character |
| byte         | Byte      |
| float        | Float     |
| boolean      | Boolean   |
| double       | Double    |

自动装箱与自动拆箱由JVM执行：
自动装箱：将基本数据类型转换为对应包装类
自动拆箱：将包装类转换为对应基本数据类型

拿Integer类举例：

```java 
public class testInteger {
	public static void main(String[] args){
		Integer i1 = 127;
		Integer i2 = 127;
		Integer i3 = 128;
		Integer i4 = 128;

		System.out.println(i1 == i2); \\return true;
		System.out.println(i3 == i4); \\return false;
	}
}
```

在"C:\Program Files\Java\jdk1.8.0_162\src.zip\java\lang"的Integer.java中查看Integer源码：

```java 
    public static Integer valueOf(int i) {
        if (i >= IntegerCache.low && i <= IntegerCache.high)
            return IntegerCache.cache[i + (-IntegerCache.low)];
        return new Integer(i);
    }
```

其中IntegerCache.low 为-128,IntgerCache.high为128
所以在[-128,127]之间是相同的对象，而之外的数值则是不同的对象

### （三）



## JDBC

Java Database Connectivity是Java中与数据库连接的API

### （一）基本步骤

(1)导入sql包

```java 
import java.sql.*;
```

(2)加载JDBC驱动

```java 
static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
Class.forName(JDBC_DRIVER);
```

(3)连接到数据库，实例化statement对象

```java 
Connection conn = DriverManager.getConnection(DB_URL,USER,PASS);
stmt = conn.createStatement();
```

(4)执行sql语句

```java 
String sql = "...";
stmt.executeUpdate(sql);
```

(5)关闭数据库连接

```java 
 		if(stmt != null)
			stmt.close();
		if(conn != null)
			conn.close();
```

### （二）

### （三）

