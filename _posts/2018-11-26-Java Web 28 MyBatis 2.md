---
layout: post
title:  "MyBatis(2)������ӳ��"
categories: JavaWeb
tags:  MyBatis
author: mio4
---

* content
{:toc}










# ��һ����ѯ���

�������ݿ����������ε��ֶΣ���ѯ�Ľ���ö�����User��������

���ڷ�Ψһ��Լ�����ֶΡ������䡿������Ԥ�ڲ�ѯ��������ؽ����ʹ�ü��ϡ���List< User >��������

```xml
<select id="selectUserById" parameterType="int" resultType="com.mio4.domain.User">
    SELECT * FROM TB_USER WHERE id = #{id}
</select>

<!--����-->
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



# ������һ��һ��ѯ



# ������һ�Զ��ѯ