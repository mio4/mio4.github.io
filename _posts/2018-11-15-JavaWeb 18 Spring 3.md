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

Spring AOP底层的实现原理是动态代理，分两种方式：JDK动态代理和Cglib动态代理

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

# （五）Hello，AOP

> 关于Jar包：大多数的包在IDEA创建Spring项目时会自动导入，少数日志包需要手动导入

- 首先需要导入的包

```xml
com.springsource.org.aspectj.weaver-1.6.8.RELEASE.jar
spring-aspects-4.3.18.RELEASE.jar
```

- 实现切面类以及增强方法
- 配置切面类bean
- 配置AOP

## 1. applicationContext.xml配置

> 配置applicationContext.xml约束头

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:aop="http://www.springframework.org/schema/aop" xsi:schemaLocation="
        http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop.xsd"> <!-- bean definitions here -->
</beans>
```

> AOP的另一个好处在于可以在不修改源代码的基础上，“动态”添加功能



## 2. 配置切面类&AOP

```xml
	<!--配置切面类-->
	<bean id="myAspectXML" class="com.mio4.demo3.MyAspectXML"/>
    <!--配置AOP-->
    <aop:config>
        <!--ref:切面类bean的id-->
        <aop:aspect ref="myAspectXML">
            <!--method:切面类中的增强方法 pointcut：切入点-->
            <aop:before method="log" pointcut="execution(public void com.mio4.demo3.CustomerDaoImpl.save())"/>
        </aop:aspect>
    </aop:config>
```



## 3. Error creating bean with name  "XXX"

- 在首次运行时出现了Error creating bean的Exception
  - 首先检查注解是否有拼写错误，然后检查包是否完整（依赖缺少的错误）
  - 最后发现是少导入了weaver.jar包

```xml
java.lang.IllegalStateException: Failed to load ApplicationContext

	at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:124)
	at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:83)
	at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:117)
	at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:83)
	at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:230)
	at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.createTest(SpringJUnit4ClassRunner.java:228)
	at org.springframework.test.context.junit4.SpringJUnit4ClassRunner$1.runReflectiveCall(SpringJUnit4ClassRunner.java:287)
	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)
	at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.methodBlock(SpringJUnit4ClassRunner.java:289)
	at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:247)
	at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:94)
	at org.junit.runners.ParentRunner$3.run(ParentRunner.java:290)
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:71)
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:288)
	at org.junit.runners.ParentRunner.access$000(ParentRunner.java:58)
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:268)
	at org.springframework.test.context.junit4.statements.RunBeforeTestClassCallbacks.evaluate(RunBeforeTestClassCallbacks.java:61)
	at org.springframework.test.context.junit4.statements.RunAfterTestClassCallbacks.evaluate(RunAfterTestClassCallbacks.java:70)
	at org.junit.runners.ParentRunner.run(ParentRunner.java:363)
	at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.run(SpringJUnit4ClassRunner.java:191)
	at org.junit.runner.JUnitCore.run(JUnitCore.java:137)
	at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:68)
	at com.intellij.rt.execution.junit.IdeaTestRunner$Repeater.startRunnerWithArgs(IdeaTestRunner.java:47)
	at com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:242)
	at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:70)
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'customerDao' defined in class path resource [applicationContext.xml]: BeanPostProcessor before instantiation of bean failed; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'org.springframework.aop.aspectj.AspectJPointcutAdvisor#0': Cannot create inner bean '(inner bean)#ec756bd' of type [org.springframework.aop.aspectj.AspectJMethodBeforeAdvice] while setting constructor argument; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name '(inner bean)#ec756bd': Failed to introspect bean class [org.springframework.aop.aspectj.AspectJMethodBeforeAdvice] for lookup method metadata: could not find class that it depends on; nested exception is java.lang.NoClassDefFoundError: org/aspectj/lang/JoinPoint
	at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:479)
	at org.springframework.beans.factory.support.AbstractBeanFactory$1.getObject(AbstractBeanFactory.java:312)
	at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:230)
	at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:308)
	at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:197)
	at org.springframework.beans.factory.support.DefaultListableBeanFactory.preInstantiateSingletons(DefaultListableBeanFactory.java:761)
	at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:867)
	at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:543)
	at org.springframework.test.context.support.AbstractGenericContextLoader.loadContext(AbstractGenericContextLoader.java:128)
	at org.springframework.test.context.support.AbstractGenericContextLoader.loadContext(AbstractGenericContextLoader.java:60)
	at org.springframework.test.context.support.AbstractDelegatingSmartContextLoader.delegateLoading(AbstractDelegatingSmartContextLoader.java:106)
	at org.springframework.test.context.support.AbstractDelegatingSmartContextLoader.loadContext(AbstractDelegatingSmartContextLoader.java:249)
	at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:98)
	at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:116)
	... 24 more
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'org.springframework.aop.aspectj.AspectJPointcutAdvisor#0': Cannot create inner bean '(inner bean)#ec756bd' of type [org.springframework.aop.aspectj.AspectJMethodBeforeAdvice] while setting constructor argument; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name '(inner bean)#ec756bd': Failed to introspect bean class [org.springframework.aop.aspectj.AspectJMethodBeforeAdvice] for lookup method metadata: could not find class that it depends on; nested exception is java.lang.NoClassDefFoundError: org/aspectj/lang/JoinPoint
```



# （六）切入点配置

> 切入点的配置可以说是AOP中的配置核心了
>
> 可以看出Spring中的逻辑是比较强的，execution()中约束了方法的返回值，以及参数列表，因为Java中存在重构函数

```xml
<!--aop:before/after-->
<!--execution中： 修饰符 返回值 包名 函数名（参数类型，其中*表示一个参数, ..表示任意参数）-->
<!--*表示通配符，比如可以用*代替void表示返回任意类型-->
<aop:before method="log" pointcut="execution(public void com.mio4.demo3.CustomerDaoImpl.save())"/>
```

# （七）通知类型配置

< aop: before>即是AOP中的通知配置

```xml
<aop:before method="log" pointcut="execution(public void com.mio4.demo3.CustomerDaoImpl.save())"/>
<aop:after method="log" pointcut="execution(public void com.mio4.demo3.CustomerDaoImpl.save())"/>
```



- 最终通知 after : 被增强方法执行之后执行
- 前置通知 before：被增强方法执行之前执行
- 后置通知 after-returning：如果被增强方法因为异常等没有成功执行，不会增强函数
- 异常通知 after-throwing：只有在异常情况下执行
- 环绕通知 around：默认情况下目标方法不会被执行，需要调用ProceedingJoinPoint手动设置



```java
    public void roundLog(ProceedingJoinPoint joinPoint) throws Throwable {
        System.out.println("round method, print the log 1~");
        joinPoint.proceed(); //在这里执行目标方法
        System.out.println("round method, print the log 2~");
    }
```

















