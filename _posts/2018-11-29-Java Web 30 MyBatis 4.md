---
layout: post
title:  "MyBatis(3)：注解开发"
categories: JavaWeb
tags:  MyBatis
author: mio4
---

* content
{:toc}












# （一）注解-CRUD

MyBatis中的注解开发基于接口，和XML文件一样，首先要注册这个接口

1. 在mybatis-config.xml中注册接口

```xml
<!--持久化类的映射文件-->
<mappers>
    <mapper class="com.mio4.mapper.UserMapper"/>
</mappers>
```

2. 接口方法配置注解

```java
public interface UserMapper {
    @Insert("INSERT INTO TB_USER(name,age,sex) VALUES (#{name},#{age},#{sex})")
    @Options(useGeneratedKeys = true,keyProperty = "id")
    int saveUser(User user);

    @Delete("DELETE FROM TB_USER WHERE id = #{id}")
    int removeUser(@Param("id") Integer id);

    @Update("UPDATE TB_USER SET name = #{name},sex = #{sex}, age = #{age} WHERE id = #{id}")
    void modifyUser(User user);

    @Select("SELECT * FROM TB_USER WHERE id = #{id}")
    @Results({
            @Result(id = true, property = "id", column = "id"),
            @Result(property = "name", column = "name"),
            @Result(property = "sex", column = "sex"),
            @Result(property = "age",column = "age")
    })
    User selectUserById(Integer id);

    @Select("SELECT * FROM TB_USER")
    List<User> selectAllUser();
}
```

3. 基于Junit测试

```java
@Test
public void testInsert(){
    SqlSession sqlSession = mySqlSessionFactory.getSqlSession();
    UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

    User user = new User();
    user.setName("test");
    user.setSex("male");
    user.setAge(30);
    userMapper.saveUser(user);

    sqlSession.commit();
    sqlSession.close();
}
```







