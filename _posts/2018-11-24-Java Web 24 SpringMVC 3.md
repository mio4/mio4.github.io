---
layout: post
title:  "SpringMVC(3)：文件上传和下载"
categories: JavaWeb
tags:  SpringMVC
author: mio4
---

* content
{:toc}






# （一）上传文件

> 文件上传和下载是网站常用的功能

1. 依赖的jar包

```xml
	commons-fileupload1.3.3.jar
	commons-io-2.6.jar
```

2. springmvc-config文件配置

```xml
<bean id="multipartResolver" class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
    <!--限制上传文件大小/字节(10MB)-->
    <property name="maxUploadSize">
        <value>10485760</value>
    </property>
    <!--请求编码格式，和JSP/HTML页面pageEncoding相同-->
    <property name="defaultEncoding">
        <value>UTF-8</value>
    </property>
</bean>
```

3. 前端

提交表单时要只能使用POST请求，并且必须标注enctype的类型

```html
<html>
<head>
    <title>文件上传</title>
</head>
<body>
    <h2>文件上传</h2>
    <form action="../upload" enctype="multipart/form-data" method="post">
        <table>
            <tr>
                <td>文件描述：</td>
                <td><input type="text" name="description"></td>
            </tr>
            <tr>
                <td>选择文件：</td>
                <td><input type="file" name="file"></td>
            </tr>
            <tr>
                <td colspan="2"><input type="submit" value="submit"></td>
            </tr>
        </table>
    </form>
</body>
</html>
```

4. 后台

   使用MultipartFile类型接受File文件，将File文件保存到特定的路径中

   【问题：当项目打包war之后，如何设置保存文件的路径，已经从路径中取出文件】

```java
@Controller
public class FileUploadController {

    @RequestMapping(value = "/upload",method = RequestMethod.POST)
    public String upload(HttpServletRequest request,
                         @RequestParam("description") String description,
                         @RequestParam("file") MultipartFile file) throws IOException {
        System.out.println(description);

        if(!file.isEmpty()){
            String path = request.getServletContext().getRealPath("/images/");
            String filename = file.getOriginalFilename();
            File filepath = new File(path,filename);
            if(!filepath.getParentFile().exists()){
                filepath.getParentFile().mkdirs();
            }
            file.transferTo(new File(path + File.separator + filename));
            return "success"; //@Controller返回的String参数是视图名称
        }else{
            return "error";
        }
    }
}
```

> 可以对用户上传的文件添加额外信息，主要是对于同名文件的处理

为了在SpringMVC中正常访问HTML页面，在web.xml中加入：

```xml
<servlet-mapping>
    <servlet-name>default</servlet-name>
    <url-pattern>*.css</url-pattern>
    <url-pattern>*.js</url-pattern>
    <url-pattern>*.html</url-pattern>
</servlet-mapping>
```

> 参考：https://blog.csdn.net/Princeliu999/article/details/55270738

# （二）下载文件

> 以下载给定文件名的文件为例

通过超链接的形式发送下载请求：

```html
<a href="download?filename=${requestScope.user.file.originalFilename}">
    ${requestScope.user.file.originalFilename}
</a>
```

后台的处理函数：

```java
@RequestMapping(value = "/download")
public ResponseEntity<byte[]> download(HttpServletRequest request,
                                       @RequestParam("filename") String filename,
                                       Model model
                                       ) throws Exception{
    //下载文件路径
    String path = request.getServletContext().getRealPath("/images/");
    File file = new File(path + File.separator + filename);
    HttpHeaders headers = new HttpHeaders();

    //下载时显示的中文名，访问乱码
    String download_filename = new String(filename.getBytes("UTF-8"),"iso-8859-1");
    //以下载方式打开文件
    headers.setContentDispositionFormData("attachment",download_filename);
    headers.setContentType(MediaType.APPLICATION_OCTET_STREAM);
    return new ResponseEntity<byte[]>(FileUtils.readFileToByteArray(file),headers,HttpStatus.CREATED);
}
```

























