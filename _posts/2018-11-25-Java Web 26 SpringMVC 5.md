---
layout: post
title:  "SpringMVC(5)：数据校验"
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

# （二）





> 日期转换的几种方式：https://blog.csdn.net/mybook201314/article/details/54232480













