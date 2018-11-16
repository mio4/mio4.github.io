---
layout: post
title:  "Spring(4)：注解&JDBC"
categories: JavaWeb
tags:  Spring
author: mio4
---

* content
{:toc}






# （一）AOP-注解方式

> 上一节中使用的是applicationContext.xml配置切面，和IoC一样，AOP也存在注解配置的方式，思想是相同的
>
> Spring框架中的很多设计比较精妙，只要熟练度足够高，就能实现框架的一般使用，所以笔记是比较有效的。但是要涉及到原理层面，就要去刷书了



## 1. 开启自动代理

 在applicationContext.xml中配置：

```xml
<!--开启自动代理-->
<aop:aspectj-autoproxy/>
```

## 2. 注解类注解

用@Aspect和@Before或@After替代 < aop : aspect >配置, value值中切入点表达式

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;

@Aspect 
public class MyAspectAnno {
    @Before(value="execution(public void com.mio4.demo1.CustomerDaoImpl.save())") //通知类型+切入点表达式
    public void log(){
        System.out.println("set some log~");
    }
}
```

这样就实现了注解方式的AOP



如果一个切面中多个注解的目标方法是相同的，为了防止繁琐代码，则可以自定义切入

```java
@Aspect
public class MyAspectAnno {
	//自定义切入点
    @Pointcut(value="execution(public void com.mio4.demo1.CustomerDaoImpl.save())")
    public void pc(){}

    @Before(value="MyAspectAnno.pc()")
    public void log(){
        System.out.println("set some log~");
    }

    @After(value="MyAspectAnno.pc()")
    public void afterLog(){
        System.out.println("set some log after~");
    }
    
}
```

# （二）

































