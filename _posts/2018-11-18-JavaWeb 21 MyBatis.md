---
layout: post
title:  "MyBatis(1)："
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

asm-3.3.1.jar
cglib-2.2.2.jar
commons-logging-1.1.1.jar
javassist-3.17.1-GA.jar
junit-4.9.jar
log4j-1.2.17.jar
log4j-api-2.0-rc1.jar
log4j-core-2.0-rc1.jar
slf4j-api-1.7.5.jar
slf4j-log4j12-1.7.5.jar
```
2. 在config文件夹下：配置SqlMapConfig.xml

```java
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/mybatis?characterEncoding=utf-8"/>
                <property name="username" value="root"/>
                <property name="password" value="123456"/>
            </dataSource>
        </environment>
    </environments>
    <mappers>
        <mapper resource="User.xml" />
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

3. 配置User.xml

```java
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
        
<!--命名空间：和C++中作用类似-->
<mapper namespace="test"> 
    <!--id:标注SQL语句-->
    <!--parameterType：Java中id类型-->
    <select id="findUserById" parameterType="java.lang.Integer" resultType="com.mio4.pojo.User">
        select * from user where id = #{id}
    </select>
    
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

# （二）加载Mapper

> 上述代码过于冗余，适合测试，但不应该出现在正式工程中















> MyBatis官方文档：http://www.mybatis.org/mybatis-3/zh/index.html







