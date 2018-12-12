---
layout: post
title:  "Redis"
categories: JavaWeb
tags:  Redis
author: mio4
---

* content
{:toc}














# （一）Redis安装

- [x] [ubuntu 安装redis两种方式 教程](https://www.cnblogs.com/langtianya/p/5187681.html)  / [linux安装redis](https://www.cnblogs.com/oskyhg/p/7293905.html)
- [x] [redis如何后台启动](https://blog.csdn.net/ksdb0468473/article/details/52126009) / [如何将 Redis 设置为后台进程](https://blog.csdn.net/a909301740/article/details/81159543)
- 步骤：

  1. 安装Redis
  2. make  /  make install 
  3. 测试redis-server
  4. 修改后台运行方式
- 进入redis目录： `./redis-server redis.conf`
- 查看进程：` ps -aux | grep -redis `
- 启动客户端（src目录下）： `./redis-cli`

# （二）Jedis

- Java连接Redis的工具

> test-case仅供个人服务器测试使用，因为暴露IP和Redis端口有安全隐患，在企业环境中参考：[Redis 请务必注意 Redis 安全配置，否则将导致轻松被入侵](https://blog.csdn.net/u011574239/article/details/78892174) 

- 依赖ar包

```
    commons-pool2-2.3.jar
    jedis-2.7.0.jar
```

- 测试

```java
        Jedis jedis = new Jedis("39.105.222.254",6379); //创建连接
        jedis.set("key2","2");
        System.out.println(jedis.get("key2"));
```

```java
        JedisPool jedisPool = new JedisPool("39.105.222.254",6379); //创建连接池
        Jedis jedis = jedisPool.getResource();
        jedis.set("key3","java");
        System.out.println(jedis.get("key3"));
        jedis.close();
```

- 整合Spring ApplicationContext.xml配置：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:mvc="http://www.springframework.org/schema/mvc"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:aop="http://www.springframework.org/schema/aop" xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
      http://www.springframework.org/schema/beans/spring-beans-3.2.xsd
      http://www.springframework.org/schema/mvc
      http://www.springframework.org/schema/mvc/spring-mvc-3.2.xsd
      http://www.springframework.org/schema/context
      http://www.springframework.org/schema/context/spring-context-3.2.xsd
      http://www.springframework.org/schema/aop
      http://www.springframework.org/schema/aop/spring-aop-3.2.xsd
      http://www.springframework.org/schema/tx
      http://www.springframework.org/schema/tx/spring-tx-3.2.xsd ">

    <!-- 连接池配置 -->
    <bean id="jedisPoolConfig" class="redis.clients.jedis.JedisPoolConfig">
        <!-- 最大连接数 -->
        <property name="maxTotal" value="30" />
        <!-- 最大空闲连接数 -->
        <property name="maxIdle" value="10" />
        <!-- 每次释放连接的最大数目 -->
        <property name="numTestsPerEvictionRun" value="1024" />
        <!-- 释放连接的扫描间隔（毫秒） -->
        <property name="timeBetweenEvictionRunsMillis" value="30000" />
        <!-- 连接最小空闲时间 -->
        <property name="minEvictableIdleTimeMillis" value="1800000" />
        <!-- 连接空闲多久后释放, 当空闲时间>该值 且 空闲连接>最大空闲连接数 时直接释放 -->
        <property name="softMinEvictableIdleTimeMillis" value="10000" />
        <!-- 获取连接时的最大等待毫秒数,小于零:阻塞不确定的时间,默认-1 -->
        <property name="maxWaitMillis" value="1500" />
        <!-- 在获取连接的时候检查有效性, 默认false -->
        <property name="testOnBorrow" value="true" />
        <!-- 在空闲时检查有效性, 默认false -->
        <property name="testWhileIdle" value="true" />
        <!-- 连接耗尽时是否阻塞, false报异常,ture阻塞直到超时, 默认true -->
        <property name="blockWhenExhausted" value="false" />
    </bean>

    <!-- redis单机 通过连接池 -->
    <bean id="jedisPool" class="redis.clients.jedis.JedisPool" destroy-method="close">
        <constructor-arg name="poolConfig" ref="jedisPoolConfig"/>
        <constructor-arg name="host" value="39.105.222.221"/>
        <constructor-arg name="port" value="6379"/>
    </bean>
</beans>
```

# （三）Redis命令



> 参考：https://www.yiibai.com/redis/redis_commands.html

































