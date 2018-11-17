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

# （二）连接JDBC

> 使用Spring连接数据库
>
> Spring提供了一些模板类，如JdbcTemplate和HibernateTemplate

1. 导入jar包

```xml
mysql-connector-java.jar //不然tomcat找不到mysql

spring-tx.jar //事务
spring-jdbc.jar
```



## （1）JdbcTemplate

```java
//Spring自带连接池
DriverManagerDataSource driverManagerDataSource = new DriverManagerDataSource();
driverManagerDataSource.setDriverClassName("com.mysql.jdbc.Driver");
driverManagerDataSource.setUrl("jdbc:mysql:///spring");
driverManagerDataSource.setUsername("root");
driverManagerDataSource.setPassword("123456");

//创建模板类
JdbcTemplate jdbcTemplate = new JdbcTemplate();
jdbcTemplate.setDataSource(driverManagerDataSource);

//CRUD操作
String sql = "insert into t_account values(null,?,?)";
jdbcTemplate.update(sql,"mio",100.0);
```

> 使用new创建对象，这种方式一点也不Spring，所以改用IoC方式

```java
<!--开启自动扫描-->
<context:component-scan base-package="com.mio4.demo1" />

<!--配置连接池-->
<bean id="driverManagerDataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
    <property name="url" value="jdbc:mysql:///spring"/>
    <property name="username" value="root"/>
    <property name="password" value="123456"/>
</bean>
<!--配置JdbcTemplate-->
<bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">
    <property name="dataSource" ref="driverManagerDataSource"/>
</bean>
```

测试有两种方式，这里采用第二种：

（1）使用工厂

（2）SpringJunit4注解

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("classpath:applicationContext.xml")
public class demo2 {

    @Resource(name="jdbcTemplate")
    private JdbcTemplate jdbcTemplate;

    @Test
    public void test1(){
        jdbcTemplate.update("insert into t_account values(null,?,?)","mio2",10.0);
    }
}
```

运行中报错，发现是在lib中混用了spring4.2和spring4.3的包导致，将所有的包版本保持一致，问题解决：

```xml
java.lang.NoClassDefFoundError: org/springframework/core/MethodClassKey

	at org.springframework.transaction.interceptor.AbstractFallbackTransactionAttributeSource.getCacheKey(AbstractFallbackTransactionAttributeSource.java:133)
	at org.springframework.transaction.interceptor.AbstractFallbackTransactionAttributeSource.getTransactionAttribute(AbstractFallbackTransactionAttributeSource.java:91)
	at org.springframework.test.context.transaction.TransactionalTestExecutionListener.beforeTestMethod(TransactionalTestExecutionListener.java:173)
	at org.springframework.test.context.TestContextManager.beforeTestMethod(TestContextManager.java:265)
	at org.springframework.test.context.junit4.statements.RunBeforeTestMethodCallbacks.evaluate(RunBeforeTestMethodCallbacks.java:74)
	at org.springframework.test.context.junit4.statements.RunAfterTestMethodCallbacks.evaluate(RunAfterTestMethodCallbacks.java:86)
	at org.springframework.test.context.junit4.statements.SpringRepeat.evaluate(SpringRepeat.java:84)
	at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:325)
	at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:254)
	at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:89)
	at org.junit.runners.ParentRunner$3.run(ParentRunner.java:290)
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:71)
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:288)
	at org.junit.runners.ParentRunner.access$000(ParentRunner.java:58)
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:268)
	at org.springframework.test.context.junit4.statements.RunBeforeTestClassCallbacks.evaluate(RunBeforeTestClassCallbacks.java:61)
	at org.springframework.test.context.junit4.statements.RunAfterTestClassCallbacks.evaluate(RunAfterTestClassCallbacks.java:70)
	at org.junit.runners.ParentRunner.run(ParentRunner.java:363)
	at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.run(SpringJUnit4ClassRunner.java:193)
	at org.junit.runner.JUnitCore.run(JUnitCore.java:137)
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:68)
	at com.intellij.rt.execution.junit.IdeaTestRunner$Repeater.startRunnerWithArgs(IdeaTestRunner.java:47)
	at com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:242)
	at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:70)
Caused by: java.lang.ClassNotFoundException: org.springframework.core.MethodClassKey
```



## （2）dbcp连接池

依赖jar包：

```xml
com.springsource.org.apache.commons.dbcp-1.2.2.osgi.jar
com.springsource.org.apache.commons.pool-1.5.3.jar
```

使用dbcp连接池代替上面原有的jdbc连接

```xml
<!--配置连接池-->
<bean id="basicDataSource" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
    <property name="url" value="jdbc:mysql:///spring"/>
    <property name="username" value="root"/>
    <property name="password" value="123456"/>
</bean>

<bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">
    <property name="dataSource" ref="basicDataSource"/>
</bean>
```

## （3）c3p0连接池

导入jar包

```xml
com.springsource.com.mchange.v2.c3p0-0.9.1.2
```

c3p0的property name需要注意一下，jdbcUrl和user

```xml
<bean id="comboPooledDataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
    <property name="driverClass" value="com.mysql.jdbc.Driver"/>
    <property name="jdbcUrl" value="jdbc:mysql:///spring"/>
    <property name="user" value="root"/>
    <property name="password" value="123456"/>
</bean>

<!--配置JdbcTemplate-->
<bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">
    <property name="dataSource" ref="comboPooledDataSource"/>
</bean>
```























