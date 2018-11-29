---
layout: post
title:  "MyBatis(3)：缓存"
categories: JavaWeb
tags:  MyBatis
author: mio4
---

* content
{:toc}












# （一）缓存

缓存的作用：从内存中查询数据，而不从数据库查询，减轻服务器压力

一级缓存：基于SqlSession级别

二级缓存：基于Mapper级别



# （二）一级缓存





# （三）二级缓存

1. Mybatis中默认关闭二级缓存，首先在mybatis-config.xml中开启二级缓存

```xml
<settings>
    <!--开启二级缓存-->
    <setting name="cacheEnabled" value="true"/>
</settings>
```

2. 然后在XXXMapper.xml中配置缓存

```xml
<mapper namespace="com.mio4.mapper.UserMapper">
    <cache eviction="LRU" flushInterval="60000" size="512" readOnly="true"/>

</mapper>
```

3. 实现二级缓存的POJO类必须要实现io.Serializable接口
4. 测试二级缓存

```java
@Test
public void testCache2(){
    SqlSession sqlSession = mySqlSessionFactory.getSqlSession();
    UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
    User user1 = userMapper.selectUserById(1);
    System.out.println(user1);
    sqlSession.close(); //关闭一级缓存

    sqlSession = mySqlSessionFactory.getSqlSession();
    userMapper = sqlSession.getMapper(UserMapper.class);
    User user2 = userMapper.selectUserById(1);
    System.out.println(user2);
	//Cache Hit Ratio [com.mio4.mapper.UserMapper]: 0.5
    sqlSession.close();
}
```











