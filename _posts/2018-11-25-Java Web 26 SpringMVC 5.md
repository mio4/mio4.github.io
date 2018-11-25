---
layout: post
title:  "SpringMVC(5)：数据转换"
categories: JavaWeb
tags:  SpringMVC
author: mio4
---

* content
{:toc}






# （一）解析html

为了能够正常跳转到WEB-INF目录下的html页面

1. 导入freemarker jar包
2.  在springmvc-config.xml中加入对HTML的支持

```xml
<bean id="freemarkerConfig" class="org.springframework.web.servlet.view.freemarker.FreeMarkerConfigurer">
    <property name="templateLoaderPath">
        <value>/WEB-INF/content</value>
    </property>
    <property name="freemarkerSettings">
        <props>
            <prop key="default_encoding">UTF-8</prop>
        </props>
    </property>
</bean>

<bean id="htmlviewResolver"
      class="org.springframework.web.servlet.view.freemarker.FreeMarkerViewResolver">
    <property name="suffix" value=".html" />
    <property name="order" value="0"/>
    <property name="contentType" value="text/html;charset=UTF-8"/>
</bean>
```

# （二）日期转换

如果从前端接受的是String类型的日期，那么在POJO中加入一行注解即可

```java
@DateTimeFormat(pattern="yyyy-MM-dd")
private Date birthday;
```

但是这样只能接受yyyy-MM-dd格式的数据，如果发送的数据格式有误，那么会产生400 Error

稍微和谐一点的容错方式，修改setBirthday方法：

```java
public void setBirthday(String birthday) {
    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
    Date date;
    try{
        date = sdf.parse(birthday);
        this.birthday = date;
    }catch(Exception e){
        e.printStackTrace();
    }
}
```





> 日期转换的几种方式：[Spring MVC 自学杂记（二） -- 数据绑定之日期转换](https://blog.csdn.net/mybook201314/article/details/54232480)















