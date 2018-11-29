---
layout: post
title:  "MyBatis(2)：关联映射"
categories: JavaWeb
tags:  MyBatis
author: mio4
---

* content
{:toc}










# （一）查询结果

对于数据库中主键修饰的字段，查询的结果用对象【如User】来接受

对于非唯一性约束的字段【如年龄】，可以预期查询到多个返回结果，使用集合【如List< User >】来接受

```xml
<select id="selectUserById" parameterType="int" resultType="com.mio4.domain.User">
    SELECT * FROM TB_USER WHERE id = #{id}
</select>

<!--测试-->
<select id="selectUserByAge" parameterType="int" resultType="com.mio4.domain.User">
    SELECT * FROM TB_USER WHERE age = #{age}
</select>
```



```java
public interface UserMapper {
    User selectUserById(Integer id);
    List<User> selectUserByAge(Integer id);
}
```



# （二）一对一查询



# （三）一对多查询