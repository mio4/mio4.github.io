---
layout: post
title:  "Spring(3)：AOP"
categories: JavaWeb
tags:  Spring
author: mio4
---

* content
{:toc}






# （一）AOP概述

> AOP（Aspect Oriented Programming） 面向切面编程
>
> OOP（Aspect Oriented Programming）面向对象编程
>
> 在编写DAO层时，一个save \| update方法常常是比较固定的，比如获取session、开启事务，操作数据库，提交事务，释放资源，这些步骤写来写去都大同小异（异常常是对于数据库操作不同），这种事情对于程序员来说就是典型的重复劳动
>
> 现在学到AOP，居然发现还真有人已经解决了这种问题
>
> AOP则**剖开对象内部，将影响多个类的重复的行为封装成一个模块**，这个模块就是Aspect

AOP能做什么：

- 处理日志
- 事务

# （二）JDK动态代理

> Java中的匿名内部类不常用，只在Android组件开发以及JDK动态代理时接触过
>
> 使用Proxy类的newProxyInstance创建动态代理对象，对类原有的方法进行增强
>
> 注意传入的参数是final类型的接口



```java
public class MyProxyUtils {
    public static UserDao getProxy(final UserDao dao){
        return (UserDao) Proxy.newProxyInstance(dao.getClass().getClassLoader(), dao.getClass().getInterfaces(), new InvocationHandler() {
            @Override
            public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                if("save".equals(method.getName()))
                    System.out.println("save method~");
                else if("update".equals(method.getName()))
                    System.out.println("update method~");
                return method.invoke(dao,args);
                //System.out.println("invoke~");
                //return null;
            }
        });
    }
}
```

- 测试类：

```java
@Test
public void test1(){
    UserDao userDao = new UserDaoImpl();
    userDao.save();
    userDao.update();
    System.out.println("***");
    UserDao proxy = MyProxyUtils.getProxy(userDao);
    proxy.save();
    proxy.update();
}
```



> 参考：https://www.cnblogs.com/xiaoluo501395377/p/3383130.html

# （三）Cglib动态代理



- 如果需要被代理的类没有实现接口，那么只能使用Cglib进行代理

```java
public class MyCglibUtils {
    public static BookDaoImpl getProxy(){
        Enhancer enhancer = new Enhancer();
        enhancer.setSuperclass(BookDaoImpl.class); //设置父类
        enhancer.setCallback(new MethodInterceptor() { //设置回调函数
            @Override
            public Object intercept(Object o, Method method, Object[] args, MethodProxy methodProxy) throws Throwable {
                if("save".equals(method.getName()))
                    System.out.println("enhanced save~");
                else if("update".equals(method.getName()))
                    System.out.println("enhanced update~");
                return methodProxy.invokeSuper(o,args);
                //return null;
            }
        });
        return (BookDaoImpl) enhancer.create();
    }
}
```

- 测试类

```java
    @Test
    public void test1(){
        BookDaoImpl bookDao = new BookDaoImpl();
        bookDao.save();
        bookDao.update();
        System.out.println("***");
        BookDaoImpl proxy = MyCglibUtils.getProxy();
        proxy.save();
        proxy.update();
    }
```

//TODO

# （四）AOP术语

Spring AOP中的行话如下：

- Joinpoint连接点：指Spring中的方法
- PointCut切点：指被拦截or增强的方法
- Advice增强：切面要完成的功能（比如代理中增强方法那部分代码）
- Introduction引介
- Target目标对象：被增强的对象（比如UserDaoImpl）
- Weaving织入：将增强添加到目标对象的过程，Spring采用动态代理织入
- Proxy代理：一个类（比如UserDaompl）被AOP增强之后，产生的结果代理类（比如myProxy）
- Aspect切面：切入点和通知的结合

使用Spring框架，要做的事是编写通知(增强功能)，配置切入点

> 参考：https://www.cnblogs.com/yangyquin/p/5462488.html



























