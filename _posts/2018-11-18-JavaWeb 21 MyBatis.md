---
layout: post
title:  "MyBatis(1)：入门"
categories: JavaWeb
tags:  MyBatis
author: mio4
---

* content
{:toc}










# （一）Head First

> 原生JDBC中SQL嵌套在代码中，代码维护性差
>
> MyBatis是一个持久层框架，对JDBC的操作过程进行了封装（和Hibernate的作用一样），但是MyBatis上手比Hibernate快一点
>
> 对于MyBatis，从架构到CRUD操作，最后实现和Spring的对接

1. 导入 jar包

```xml
mybatis-3.2.7.jar //核心包
mysql-connector-java-5.1.7-bin.jar //MySQL必备包，因为MyBaits底层实现是JDBC

commons-logging-1.1.1.jar
log4j-1.2.17.jar
log4j-api-2.0-rc1.jar
log4j-core-2.0-rc1.jar
slf4j-api-1.7.5.jar
slf4j-log4j12-1.7.5.jar

asm-3.3.1.jar
cglib-2.2.2.jar
javassist-3.17.1-GA.jar
junit-4.9.jar

```
2. 在config文件夹下：配置SqlMapConfig.xml

```java
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <!--指定Mybatis日志的具体实现-->
    <settings>
        <setting name="logImpl" value="LOG4J"/>
    </settings>
    <environments default="mysql">
        <environment id="mysql">
            <!--指定事务管理类型-->
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/mybatis?characterEncoding=utf-8"/>
                <property name="username" value="root"/>
                <property name="password" value="123456"/>
            </dataSource>
        </environment>
    </environments>

    <!--持久化类的映射文件-->
    <mappers>
    <!--这里的路径是以 / 分割而不是 .-->
        <mapper resource="com/mio4/mapper/UserMapper.xml" />
    </mappers>
</configuration>

```

其中< mappers >标签：需要引入的配置文件，比如：

```xml
<mappers>
    <mapper resource="User.xml" />
    <mapper class="com.mio4.mapper.UserMapper" />
</mappers>
```

3. 配置UserMapper.xml

```java
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.mio4.mapper.UserMapper">
    <insert id="save" parameterType="com.mio4.domain.User" useGeneratedKeys="true">
        INSERT INTO TB_USER(name,sex,age) VALUES(#{name},#{sex},#{age})
    </insert>

    <!--CRUD-->
    <!--parameterType：传入的参数类型-->
    <!--resultType：执行SQL之后返回的结果-->
    <insert id="saveUser" parameterType="com.mio4.domain.User" useGeneratedKeys="true">
        INSERT INTO TB_USER (name,sex,age)
        VALUES (#{name},#{sex},#{age})
    </insert>

    <select id="selectUser" parameterType="int" resultType="com.mio4.domain.User">
        SELECT * FROM TB_USER WHERE id = #{id}
    </select>

    <update id="updateUser" parameterType="com.mio4.domain.User">
        UPDATE TB_USER
        SET name = #{name},sex = #{sex}, age = #{age}
        WHERE id = #{id}
    </update>

    <delete id="deleteUser" parameterType="int">
        DELETE FROM TB_USER WHERE id = #{id}
    </delete>

</mapper>
```

4. 编写测试文件

```java
import com.mio4.pojo.User;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;


@Test
public void testFindUserById() throws SQLException, IOException {
    String resource = "SqlMapConfig.xml";
    InputStream inputStream = Resources.getResourceAsStream(resource); //读取配置文件
    SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream); //创建SessionFactory
    SqlSession sqlSession = sqlSessionFactory.openSession(); //创建session
    User user = sqlSession.selectOne("test.findUserById",1);
    System.out.println(user);
}
```

> 其他步骤：配置log4j.properties，创建数据库和表，插入数据等

注意User.xml中的SQL语句使用了#{ }占位符，不是原生的SQL语句

对于POJO对象，#{ }中间是POJO的私有属性，实际上是填写POJO对象和数据库对应关系

比如实现一个Insert操作：

```java
public void testInsertUser() throws Exception{
    String resource = "SqlMapConfig.xml";
    InputStream inputStream = Resources.getResourceAsStream(resource); //读取配置文件
    SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream); //创建SessionFactory
    SqlSession sqlSession = sqlSessionFactory.openSession(); //创建session

    User user = new User();
    user.setUsername("mio");
    user.setBirthday(new Date());
    user.setSex("2");
    user.setAddress("shanghai");
    sqlSession.insert("test.insertUser",user);
    sqlSession.commit();
}
```

注意：**MyBatis中的事务会自动开启，但是需要手动提交**



5. java.io.IOException: Could not find resource SqlMapConfig.xml报错

在IDEA Project Structure中将Config文件夹添加为Source即可

6. 备选：log4j.properties日志配置

```xml
# Global logging configuration
log4j.rootLogger=DEBUG, stdout
# Console output...
log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern=%5p [%t] - %m%n
```

# （二）ResultMap

当数据库中的字段和POJO的属性名称不同的时候，可以使用resultMap进行手动映射配置

使用ResultMap可以将查询结果转换为JavaBean对象

1. User2的属性

```java
private Integer id;
private String name;
private String sex;
private Integer age;
```

2. 数据库建表

```sql
CREATE TABLE TB_USER2(
	user_id INT PRIMARY KEY AUTO_INCREMENT,
	user_name VARCHAR(20),
	user_sex VARCHAR(20),
	user_age INT
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

3. UserMapper.xml配置

```xml
    <!--手动配置映射关系-->
    <!--id表示数据库的主键-->
    <!--property：POJO中的属性，column:数据表的字段-->
    <!--type:配合select查询时的返回类型-->
    <resultMap id="userResultMap" type="com.mio4.domain.User2">
        <id property="id" column="user_id"/> 
        <result property="name" column="user_name"/>
        <result property="sex" column="user_sex"/>
        <result property="age" column="user_age"/>
    </resultMap>
    
    <select id="selectUser3" resultMap="userResultMap">
        SELECT * FROM TB_USER2
    </select>
```

4. 测试类

```java
public class ResultMapTest {
    public static void main(String[] args){
        SqlSession sqlSession = sessionFactoryUtils.getSqlSession();
        List<User2> list = sqlSession.selectList("com.mio4.mapper.UserMapper.selectUser3");
        for(User2 user: list){
            System.out.println(user);
        }
        sqlSession.commit();
        sqlSession.close();
    }
}
```









> MyBatis官方文档：http://www.mybatis.org/mybatis-3/zh/index.html







