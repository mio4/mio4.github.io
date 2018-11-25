---
layout: post
title:  "SpringMVC(4)：拦截器"
categories: JavaWeb
tags:  SpringMVC
author: mio4
---

* content
{:toc}






# （一）Interceptor

> 拦截器可以拦截制定的请求
>
> 通过拦截器可以进行权限认证，比如判断用户是否处于登录状态

拦截器必须实现**HandlerInterceptor**接口，对于登录的验证在preHandle中进行

将页面分为不验证的【登录 注册页面】和需要验证的【如果处于登录状态则不拦截，否则拦截并且跳转请求】

```java
public class AuthorizationInterceptor implements HandlerInterceptor {
    private static final String[] IGNORE_URL = {"/loginForm","/login"};

    //在Controller之前调用
    //如果返回值为false，则整个请求结束
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object o) throws Exception {
        System.out.println("Authorization Interceptor preHandle~");
        boolean is_login = false; //用户是否登录
        String servlet_path = request.getServletPath();
        //判断请求是否需要被拦截
        for(String s: IGNORE_URL){
            if(servlet_path.contains(s)){
                is_login = true;
                break;
            }
        }
        //判断用户是否登录
        if(!is_login){
            User user = (User) request.getSession().getAttribute("user");
            if(user == null){
                System.out.println("Authorization Interceptor 拦截请求");
                request.setAttribute("message","请登录后访问网站");
                //request.getRequestDispatcher("/loginForm").forward(request,response);
                request.getRequestDispatcher("content/loginForm.jsp").forward(request,response);
            } else{
                System.out.println("Authorization Interceptor 放行请求");
                is_login = true;
            }
        }
        return is_login;
    }

    //当Controller方法调用之后执行
    //只有当前Interceptor的preHandle返回为true时才执行
    @Override
    public void postHandle(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, Object o, ModelAndView modelAndView) throws Exception {
        System.out.println("Authorization Interceptor postHandle~");
    }

    //请求完成之后执行，用于清理资源
    //只有当前Interceptor的preHandle返回为true时才执行
    @Override
    public void afterCompletion(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, Object o, Exception e) throws Exception {
        System.out.println("Authorization Interceptor afterCompletion~");
    }
}
```

需要注意的是Interceptor只会拦截Controller，**而不能拦截JSP页面的直接访问**

所以一般讲JSP页面放在WEB-INF目录下，这样用户也不能通过URL的方式直接访问JSP页面，而只能通过Controller的@RequestMapping，处理请求之后跳转到视图

在springmvc-config中配置：

```xml
<!--拦截器-->
<mvc:interceptors>
    <mvc:interceptor>
        <mvc:mapping path="/**"/>
        <bean class="com.mio4.interceptor.AuthorizationInterceptor"/>
    </mvc:interceptor>
</mvc:interceptors>
```



> 参考：http://www.cnblogs.com/Anders888/p/6073190.html













