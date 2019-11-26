#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# 生成特定的博客文件
import time

name = raw_input("input file name：")
title = raw_input("input title：");
cate = raw_input("input category：")
tags = raw_input("input tags：")
cur_time = time.strftime("%Y-%m-%d")

blog = open(cur_time+'-'+name,'w')
blog.write('---\n')
blog.write('layout:post\n')
blog.write('title:'+title+'\n')
blog.write('tags:'+tags+'\n')
blog.write('author:mio4\n')
blog.write('---\n')
blog.write('\n')
blog.write('\n')
blog.write('\n')
blog.write('\n')
blog.write('\n')
blog.write('* content\n')
blog.write('{:toc}\n')

blog.close()

