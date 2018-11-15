---
layout: post
title:  "读书笔记：【C和指针】"
categories: 读书笔记
tags:  C
author: mio4
---

* content
{:toc}






> 【C和指针】读书笔记
>
> 刷好书的好处在于，如果对于一本经典中所有的大部分都理解，看过的知识进行了整理，那么在使用的时候就非常放心，就算有忘记的地方也可以回来马上复习，同时也知道自己知识的边界
>
> 在时间有限的情况下，学习优先程度： 重要章节>知识盲区
>
> 对于语言越是熟悉，在实现工程的时候越能将更多的精力放在算法的实现上

实验环境：Visual Studio 2017 - C++ 工程



# Visual Studio  2017 快捷键

Ctrl+K+C: 注释

Ctrl+K+U: 取消注释

# 指针

> 指针可以说是C最重要并且经常使用的部分，而指针使用不当可能会导致整个程序崩溃，所以第一个要复习的部分是C中的指针

良好的编程习惯：在程序中对指针显示地初始化

硬件通过地址直接访问值，而高级语言一般都提供了名字作为助记符来访问内存的值，名字和内存地址之间的映射由编译器实现

指针存放的是变量的地址，指针内部不存在间接访问属性，通过 * 符号实现由地址访问值的间接访问（解引用指针）

```c
 int a = 112;
 float b = 3.14;

 //* ：解引用符，表示通过地址获取存放的变量
 //& ：取地址符，表示获取变量的地址

 //将int *看作一个整体，即将c赋值为a的地址
 int *c = &a; //c是一个指向整形的指针
 float *d = &b; //d是一个指向浮点型的指针
```

野指针： **指针在使用前必须要初始化，否则如果初始值是非法地址，那么会产生异常；如果是合法地址，那么可能会修改对应位置的值，对程序正确性产生隐患。**（在VS 2017的环境中，未初始化的局部变量不能使用）

对NULL空指针的解引用操作是非法的，会导致程序Crash（这种情况下，程序Crash反而是一件好事，降低了Debug的难度）

## 1. 指针的指针



## 2. 指针运算





# 函数

函数原型（Function Prototype）：定义了函数的返回值、函数名、函数参数，也就是我们说的函数声明

```c
int myfunction(int n); //一种风格：放在main函数之前，函数定义放在main函数之后
```

> 关于函数原型，见Wiki：https://en.wikipedia.org/wiki/Function_prototype

编程习惯：将函数原型放在.h文件中，使用include导入文件。这样原型就有文件作用域，并且实现了模块化



## 1. 函数参数

C中函数只有一种参数传递模式：**传值调用**，函数可以获得参数的一份拷贝，修改这个拷贝值不会影响原有的参数——验证传值调用的最基本方式就是swap(int a,int b)函数

> 使用static修饰的函数，使用范围限定在当前文件内，其他源文件中不能调用

## 2.递归



## 3.可变参数列表



# 数组

数组名是一个指针常量，也就是数组第一个元素的地址（但数组和指针不能完全划等号）

```c
 int a[10];
 int *b;
 a = b; //非法操作，数组名是常量，不能进行这样的赋值
```

访问数组元素有两种方式：下标访问和指针

```c

```

指针在某些场合下比下标访问更有效率

## 多维数组





## 指针数组





# 字符串

C中没有Java中String这种字符串类型，而是以字符常量的形式存放的字符数组来表示一个字符串，以'\0'作为字符串结束的标志

```c
	char message[] = "Original message"; //注意中括号的位置
	char message2[10]; //字符串长度为10
```



> strlen()的返回值是size_t类型（注意不是int），是一个无符号类型

```c
//两表达式不等价
if ( strlen(x) >= strlen (y) )
if ( strlen(x) - strlen(y) >=0 )
//strlen(x)-strlen(y)的返回值是无符号类型，无符号类型不可能是负数，if永真
```

## 1. strcpy函数

```c
#include <string.h>
strcpy(char *dst, char *src); //将src的字符串拷贝到dst中
```

使用strcpy必须要保证dst的长度范围大于src，否则多出来的部分会导致数组后面的内存被修改，程序Crash

Visual Studio 中因为strcpy不会对字符串做越界检查，所以不能通过编译，在编译预选项中设置即可

> 解决方案参考：https://blog.csdn.net/TimeOverflow/article/details/75253324

## 2. strcat函数

```c
strcat(char *dst, char *src);  //将src字符串追加到dst字符串后面
```

strcat和strcpy一样是比较危险的函数，需要保证原字符串有足够多的位置放下新的字符

```c
	char a[] = "string a";
	char b[] = "string b";
	strcat(a, b);
	printf("%s", a);
```

上述代码会报错：因为a是一个字符串常量，没有足够多的空间容量字符串常量b，程序Crash

> strcpy很strcat函数都返回目标字符串指针，即结果指针

## 3.字符串查找函数



# 结构

## 1.结构声明

数组只能保存相同类型的变量，而结构则可以保存一个变量集合，其中包含不同类型的变量（比如在C中使用结构描述链表节点，而在Java中面向对象地创建对象来描述链表节点）

```c
struct tag { member-list } variable-list; //结构声明语句
```

```c
struct SIMPLE {
	int a; //member-list是语句集合，以 ';' 结尾而不是 ','
	char b;
	float c;
}; //特别注意这里的分号

struct SIMPLE x,y[20],*z; //创建变量
```

为了让声明变量的时候更加方便，一般结合typedef：

```c
typedef struct {
	int a;
	char b;
	float c;
} Simple;

Simple x,y[20],*z; //z是一个指向Simple结构体的指针	
```

结构成员可以是其他结构，就像Java中类成员变量可以是其他类的实体一样

## 2.结构成员

> 对于成员的间接访问方式很重要

（1）直接访问

```c
struct COMPLEX {
    int a;
    struct SIMPLE s;
};

struct COMPLEX comp;
```

使用comp.a即可访问comp结构体下的a成员变量

（2）间接访问

```c
struct COMPLEX *cp;
```

传统方式是`(*cp).a`来访问，为了简化定义了`->`运算符

`->`运算符左边是一个指向结构体的指针，右边是获取的成员变量，比如使用`cp->a`访问cp指向的结构体下的a成员变量

## 3.结构体初始化

类推数组的初始化，对于不够的值按照默认缺省值赋值

```c
struct INIT_EX {
	int a;
	short b[10];
	SIMPLE c;
} x = {
	10,
	{ 1,2,3 }, //数组剩下的部分赋值为0
	{ 10,'m',2.0 }
};
```



# 动态内存分配

数组的长度往往在运行时才知道，所以动态内存分配能够解决过大声明数组导致空间浪费和过小声明数组可能溢出的问题

## 1.malloc

malloc(int x)函数获取的内存是连续的

malloc(int x) ，函数的参数x是以字节作为单位，可以使用`malloc(100)`获取100个字节的内存空间

```c
	int * pi;
	pi = (int *)malloc( 25 * sizeof(int)); //malloc函数的返回值是int *类型，一般需要类型转换之后使用
	if (pi == NULL) { //对于malloc的返回值都要进行检查，如果为空说明内存池已满
		printf("out of memory\n");
	}
```

## 2. free





# 输入输出

> 本小节主要注重C中控制台输入输出函数，以及对于文件的操作函数的使用

## 1.流

操作系统负责计算机中不同设备的I/O通信细节，而对C提供了同一的I/O接口

流分为文本流和二进制流，二进制流适用于非文本数据

## 2.文件I/O

一个典型的文件操作流程：

（1）声明FILE * 文件指针

（2）使用fopen函数打开流，指定访问方式（mode）

（3）对文件进行读写操作

（4）调用fclose函数关闭流

### 1. fopen函数

```c
//name表示打开文件的全路径，mode表示操作方式
FILE *fopen( char const *name, char const *mode);
```

关于mode选项：

1. r  ：只对文件进行读操作
2. w ：如果文件不存在，则创建一个新文件；如果文件存在，则将文件中的内容删除
3. a ：如果文件不存在，则创建一个新文件；如果文件存在，则在文件末尾追加内容


```c
	FILE * f;
	f = fopen("test.txt", "r");
	if (f == NULL) {
	    //perror:将上一个函数发生错误的原因输出到stderr
        perror("data3");
        
         //对于exit()函数，0表示正常退出，非零表示异常
         //EXIT_SUCCESS = 0, EXIT_FAILURE = 1
		//exit(EXIT_FAILURE);
	}
```

### 2.fclose函数

```c
int fclose(FILE * f); 
```

关闭流之后，FILE指针释放，可以作用于其他的文件

## 3.字符I/O

### 1. getchar函数

getchar并不会过滤回车

```c
int getchar(void); //函数定义

char c = getchar(); //从键盘中读取一个字符
```

getchar工作原理：当程序调用getchar时，程序等待用户按键，输入的字符放在键盘缓冲区中，直到用户按回车位置，回车字符也被放在缓冲区。所以getchar并不会过滤回车


### 2. putchar函数

```c
void putchar(int character); //putchar只接受一个参数
```

对于多余的参数，putchar选择其中的一个输出

### 3.ungetc函数

```c
int ungetc(int character, FILE *stream);
    
ungetc(ch,stdin);//将多读入的字符放回标准输入流
```



# 编程风格































































