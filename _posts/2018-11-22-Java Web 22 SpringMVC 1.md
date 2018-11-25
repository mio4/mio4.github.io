---
layout: post
title:  "SpringMVC(1)：入门"
categories: JavaWeb
tags:  SpringMVC
author: mio4
---

* content
{:toc}






# （一）Hello springMVC

### 步骤

1. 导入jar包

```
    commons-logging-1.1.1.jar
    jstl-1.2.jar
    spring-aop-4.1.3.RELEASE.jar
    spring-aspects-4.1.3.RELEASE.jar
    spring-beans-4.1.3.RELEASE.jar
    spring-context-4.1.3.RELEASE.jar
    spring-context-support-4.1.3.RELEASE.jar
    spring-core-4.1.3.RELEASE.jar
    spring-expression-4.1.3.RELEASE.jar
    spring-jdbc-4.1.3.RELEASE.jar
    spring-jms-4.1.3.RELEASE.jar
    spring-messaging-4.1.3.RELEASE.jar
    spring-tx-4.1.3.RELEASE.jar
    spring-web-4.1.3.RELEASE.jar
    spring-webmvc-4.1.3.RELEASE.jar
```

2. 配置web.xml文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
<!--配置前端控制器-->    
    <servlet>
        <servlet-name>springMVC</servlet-name>
        <servlet-class>
            org.springframework.web.servlet.DispatcherServlet
        </servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/springmvc-config.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>springMVC</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
</web-app>
```

3. 配置springmvc-config.xml文件

```xml
	<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans-4.1.xsd
        http://www.springframework.org/schema/mvc
        http://www.springframework.org/schema/mvc/spring-mvc-4.1.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context-4.1.xsd">

    <!--开启注解扫描-->
    <context:component-scan base-package="com.mio4"/>
    <!--配置注解驱动：-->
    <!--自动配置最新的处理映射器和处理器适配器-->
    <mvc:annotation-driven/>

    <!--配置视图解析器-->
    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/user/"/>
        <property name="suffix" value=".jsp"/>
    </bean>
    
</beans>    
```

4.  Controller类

```java
@Controller
public class HelloController {
    private static final Log logger = LogFactory.getLog(HelloController.class);

    @RequestMapping(value = "/hello")
    public ModelAndView hello(){
        logger.info("hello方法被调用");
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("message","Hello SpringMVC");
        modelAndView.setViewName("/WEB-INF/jsp/welcome.jsp");
        return modelAndView;
    }
}
```

5. 配置jsp页面

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>welcome</title>
</head>
<body>
    <%--等价于request.getAttribute(message)--%>
    这是一个从HelloController传来的数据：<br>
    ${requestScope.message}
</body>
</html>
```

> 使用Spring4.1.3 jar 包 + JDK7 + tomcat7.0
>
> 或者Spring4.1.3 jar 包 + JDK8 + tomcat9.0
>
> 备注：在尝试使用Spring 4.3.1 jar包时报错Servlet.init() for servlet [springMVC] threw exception...
>

在浏览器输入http://localhost:8080/demo10/hello 可以得到welcome.jsp页面











