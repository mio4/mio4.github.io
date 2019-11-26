#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# 生成特定的博客文件
import time

name = raw_input("input file name：")
title = raw_input("input title：");
cate = raw_input("input category：")
tags = raw_input("input tags：")
cur_time = time.strftime("%Y-%m-%d")

blog = open(cur_time+'-'+name+'.md','w')
blog.write('---\n')
blog.write('layout: post\n')
blog.write('title: \"'+title+'\"\n')
blog.write('categories: '+cate+'\n')
blog.write('tags: '+tags+'\n')
blog.write('author: mio4\n')
blog.write('---\n')
blog.write('\n')
blog.write('\n')
blog.write('\n')
blog.write('\n')
blog.write('\n')
blog.write('* content\n')
blog.write('{:toc}\n')

blog.write('~~引用图片的路径 ![](https://raw.githubusercontent.com/mio4/mio4.github.io/master/pics/)~~')

blog.close()

