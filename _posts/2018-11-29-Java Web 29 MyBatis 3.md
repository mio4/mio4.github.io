---
layout: post
title:  "MyBatis(3)������"
categories: JavaWeb
tags:  MyBatis
author: mio4
---

* content
{:toc}












# ��һ������

��������ã����ڴ��в�ѯ���ݣ����������ݿ��ѯ�����������ѹ��

һ�����棺����SqlSession����

�������棺����Mapper����



# ������һ������





# ��������������

1. Mybatis��Ĭ�Ϲرն������棬������mybatis-config.xml�п�����������

```xml
<settings>
    <!--������������-->
    <setting name="cacheEnabled" value="true"/>
</settings>
```

2. Ȼ����XXXMapper.xml�����û���

```xml
<mapper namespace="com.mio4.mapper.UserMapper">
    <cache eviction="LRU" flushInterval="60000" size="512" readOnly="true"/>

</mapper>
```

3. ʵ�ֶ��������POJO�����Ҫʵ��io.Serializable�ӿ�
4. ���Զ�������

```java
@Test
public void testCache2(){
    SqlSession sqlSession = mySqlSessionFactory.getSqlSession();
    UserMapper userMapper = sqlSession.getMapper(UserMapper.class);
    User user1 = userMapper.selectUserById(1);
    System.out.println(user1);
    sqlSession.close(); //�ر�һ������

    sqlSession = mySqlSessionFactory.getSqlSession();
    userMapper = sqlSession.getMapper(UserMapper.class);
    User user2 = userMapper.selectUserById(1);
    System.out.println(user2);
	//Cache Hit Ratio [com.mio4.mapper.UserMapper]: 0.5
    sqlSession.close();
}
```











