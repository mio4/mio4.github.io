---
layout: post
title:  "SpringMVC(2)：JSON"
categories: JavaWeb
tags:  SpringMVC
author: mio4
---

* content
{:toc}






# （一）SpringMVC发送JSON数据

> 前面在前后端交互的时候使用的方式都是JSP，在HTML中插入Java代码的方式对于前端来说不是很友好，为了让前后端的工作分离，可以使用JSON来交互数据

1. 导入JS包： jQuery.js和Json2.js
2. 导入Jackson Jar包：

```xml
    jackson-annotations-2.4.0.jar
    jackson-core-2.4.2.jar
    jackson-databind-2.4.2.jar
```

3. 前端发送JSON数据【使用AJAX】

   index.html：

```html
<script src="js/jquery-1.11.0.min.js"></script>
<script src="js/json2.js"></script>
<script>
    $(document).ready(function(){
        testRequestBody();
    });
    function testRequestBody(){
        $.ajax({
            url:"${pageContext.request.contextPath}/json/testRequestBody", //发送的地址
            dataType:"json", //预期服务器发送的数据类型
            type: "post", //请求方式
            contentType:"application/json", //发送信息到服务器时的内容编码格式
            data:JSON.stringify({id:1,name:"SpringMVC企业应用实战"}), //发送的JSON数据
            async:true, //异步发送
            success:function(data){ //请求成功后的回调函数
                console.log(data);
                $("#id").html(data.id);
                $("#name").html(data.name);
                $("#author").html(data.author);
            },
            error:function(){ //请求失败后调用的函数
                alert("数据发送失败");
            }
        });
    }
</script>
<html>
  <head>
    <title>发送接收JSON数据</title>
  </head>
  <body>
    编号：<span id="id"></span> <br>
    书名：<span id="name"></span> <br>
    作者：<span id="author"></span> <br>
  </body>
</html>
```

4. 后台接受JSON数据，发送JSON数据

```java
@Controller
@RequestMapping("/json")
public class BookController {
    private static final Log logger = LogFactory.getLog(BookController.class);

    @RequestMapping(value = "/testRequestBody")
    public void setJson(@RequestBody Book book, HttpServletResponse response)  throws Exception{
        ObjectMapper mapper = new ObjectMapper();
        logger.info(mapper.writeValueAsString(book));
        book.setAuthor("写书人");
        response.setContentType("text/html;charset=UTF-8");
        response.getWriter().println(mapper.writeValueAsString(book));
    }

}
```

5. 配置springmvc-config.xml

   处理< script >引入的js文件

```xml
<!--使用默认的servlet来处理静态文件-->
<mvc:default-servlet-handler/>
```

> 这种方式的问题在于前端还是要编写JSP页面，如果使用纯HTML，则EL表达式会失效，所以在HTML中使用相对路径达到访问制定URL的目的

# （二）向前端发送JSON数据

使用@ResponseBody注释

```java
//发送JSON
@RequestMapping(value = "/testResponseBody")
@ResponseBody
public Object getJon(){
    List<Book> bookList = new ArrayList<Book>();
    bookList.add(new Book(1,"SpringMVC企业应用实战","author1"));
    bookList.add(new Book(2,"SpringMVC企业开发实战","author2"));
    return bookList;
}
```

前台使用jQuery的.POST方法接受JSON数据



```html
<!DOCTYPE html>
<html>
<head>
    <title>Title</title>
    <meta charset="UTF-8"/>
    <script src="js/jquery-1.11.0.min.js"></script>
    <script src="js/json2.js"></script>
    <script>
        $(document).ready(function(){
            testResponseBody();
        });

        function testResponseBody(){
            //.post()是jQuery中的方法，文档：http://api.jquery.com/jQuery.post/
            //url：请求发送的路径
            //data：null:发送的data为空
            //success:function(data){} 请求成功后的回调函数
            //dataType:"json" 期望从服务器传来的数据u
            $.post("json/testResponseBody",null,
                function(data){
                    $.each(data,function(){//遍历JSON
                        var tr = $("<tr align='center'/>"); //新建一行
                        $("<td/>").html(this.id).appendTo(tr); //将<td>id</td>插入tr
                        $("<td/>").html(this.name).appendTo(tr);
                        $("<td/>").html(this.author).appendTo(tr);
                        $("#bookTable").append(tr); //插入tr
                    })
                },"json");
        }
    </script>
</head>
<body>
<table id="bookTable" border="1" style="border-collapse:collapse;">
    <tr align="center">
        <th>编号</th>
        <th>书名</th>
        <th>作者</th>
    </tr>
</table>
</body>
</html>
```

















