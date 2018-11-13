---
layout: post
title:  "Spring(2)：注解"
categories: JavaWeb
tags:  Spring
author: mio4
---

* content
{:toc}






#  (一) IoC-注解入门

> 使用注解来替代配置文件，能在一定程度上简化代码
>
> 使用步骤：1.开启注解扫描 2.对类做标记 

## 1. 配置文件

配置applicationContext.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:aop="http://www.springframework.org/schema/aop"
	xmlns:tx="http://www.springframework.org/schema/tx"
	xsi:schemaLocation="http://www.springframework.org/schema/beans 
	http://www.springframework.org/schema/beans/spring-beans.xsd
	http://www.springframework.org/schema/context
	http://www.springframework.org/schema/context/spring-context.xsd
	http://www.springframework.org/schema/aop
	http://www.springframework.org/schema/aop/spring-aop.xsd
	http://www.springframework.org/schema/tx 
	http://www.springframework.org/schema/tx/spring-tx.xsd">
    
    <!--开启注解扫描-->
    <context:component-scan base-package="com.mio4.demo1"/>
</beans>
```



## 2. 类注解

在类前面加上@Component注解

```java
@Component(value="userServiceImpl") //对应<beans>标签中的id
public class UserServiceImpl implements UserService {
    public void sayHello(){
        System.out.println("Hello!");
    }
}
```



## 3. 属性注解

- 使用value标签

```java
//为UserServiceImpl提供一个Set方法，就可以使用注解赋值
@Value(value="mio")
private String name;
public void setName(String name) {
    this.name = name;
}
```



## 4.  测试

```java
@Test
public void test(){
    ApplicationContext applicationContext = new ClassPathXmlApplicationContext("applicationContext.xml");
    UserService userService = (UserService) applicationContext.getBean("userServiceImpl"); 
    userService.sayHello();
}
```

# （二）@Autowired自动装配

- 首先制定UserDaoImpl标识符为userDao

```java
@Repository(value="userDao")
public class UserDaoImpl implements UserDao{
    public void save(){
        System.out.println("save...");
    }
}
```

- @Autowired自动装配，使用Autowired可以省略Set方法
- @Qualifier标签需要配合@Autowired使用，当Spring上下文中存在不止一个UserDao接口的实现类时，通过Qualifier限定标识符

```java
//UserServiceImpl类
@Autowired
@Qualifier(value="userDao")
//@Resource(name="userDao")
private UserDao userDao;
```

> Java自带的Resource注解也可以从容器中按照名称装配

# （三）Spring整合Junit单元测试

> Spring框架整合了Junit测试，使用时配合注解

- 依赖Jar包：spring-test.jar

- 优点：不需要调用工厂对象就能实现注入

```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("classpath:applicationContext.xml")
public class demo2 {

    @Resource(name="userServiceImpl")
    private UserService userService;

    @Test
    public void test1(){
        userService.sayHello();
    }
}
```






































