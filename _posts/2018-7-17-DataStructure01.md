---
layout: post
title:  "数据结构基础(1)：栈和队列"
categories: 数据结构
tags:  C DataStructure
author: mio4
---

* content
{:toc}


 



> - 栈是一个先进后出(FILO)的数据结构。往箱子里放盘子是一个典型的栈模型，后放入的盘子会先被取出来
> - 队列是一个先进先出(FIFO)的数据结构。例如生活中的各种排队模型。


## （一）栈的数组实现
```c
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 100
typedef int Element;

typedef struct Stack{
    int data[MAXSIZE];
    int top;
}Stack;

void initStack(Stack *s){
    s->top = -1;
}

int isStackEmpty(Stack *s){
    return (s->top==-1 ? 1 : 0);
}

int push(Stack *s, Element x){
    if(s->top == MAXSIZE){
        return 0;  
    }
    s->data[++s->top] = x;
    return 1;
}

int pop(Stack *s,int *x){
    if(s->top == -1){
        return 0;
    }
    *x = s->data[s->top--];
    return 1;
}

void printStack(Stack *s){
    while(s->top != -1){
        printf("%d ",s->data[s->top--]);
    }
}

int main(void){
    int x;
    Stack s;
    //初始化
    s.data[0] = 1;
    s.data[1] = 2;
    s.data[2] = 3;
    s.top = 2;
    push(&s,4);
    pop(&s,&x);
    printf("pop = %d\n",x);
    printStack(&s);
    system("pause");
    return 0;
}
```

## （二）栈的链表实现
```c 
//使用链表的形式实现栈——修改版本
#include<stdio.h>
#include<stdlib.h>
typedef struct Lnode{
	int data;
	struct Lnode *next;
}Lnode;

//初始化链栈
void initStack(Lnode **ln){
    *ln = (Lnode *)malloc(sizeof(Lnode));
    if(*ln == NULL){
        printf("error");
    }
    (*ln)->next = NULL;
}

//判断链栈是否为空
int StackEmpty(Lnode *ln){
	return (ln->next==NULL?1:0);
}
//进栈
void push(Lnode *ln,int x){
	Lnode *p;
	p=(Lnode *)malloc(sizeof(Lnode));
	if(p ==NULL){
		printf("ERROR");
		exit(0);
	}
	p->next=NULL;
	p->data=x;
	p->next=ln->next;
	ln->next=p;
}
//出栈
int pop(Lnode *ln,int *x){
	Lnode *p=ln->next;
	if(p ==NULL){
		return 0;
	}
	*x=p->data;
	ln->next=p->next;
	free(p);
	return 1;
}
void printStack(Lnode *ln){
	Lnode *p=ln->next;
	while(p!=NULL){
		printf("%d\n",p->data);
		p=p->next;
	}
}
int main(void){
	Lnode *ln;
	int x;
	initStack(&ln);
	//ln.next = NULL;
    push(ln,2);
	push(ln,3);
	push(ln,4);
	push(ln,5);
	pop(ln,&x); 
	printf("popped element:%d\n",x);

	printStack(ln);
    system("pause");
    return 0;
}
```
 - 进栈前需要判断栈是否已满
 - 出栈前需要判断栈是否为空

## （三）简单队列数组实现
 - 简单队列的不足：不断入队、出队之后，front和rear“指针”会不断后移，最后队列虽然没有满但是无法再添加元素

```c 
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 100
typedef struct Queue {
    int elements[MAXSIZE];
    int front;
    int rear;
}Queue;

//初始化队列
void initQueue(Queue **q){
    *q = (Queue *)malloc(sizeof(Queue));
    (*q)->front = -1;
    (*q)->rear = -1;
}

//添加元素
void addQ(Queue *q,int e){
    q->elements[++q->rear] = e;
}

//删除元素
void deleteQ(Queue *q,int *e){
    *e = q->elements[++q->front]; 
}

//队列是否为空
int IsEmpty(Queue *q){
    return (q->front == q->rear ? 1 : 0);
}

//队列是否已满
int IsFull(Queue *q){
    return (q->front == MAXSIZE-1 ? 1 : 0);
}

int main(void){
    int i;
    Queue *q;
    initQueue(&q);
    //printf("add elements:\n");
    for(i=0; i < 30; i++){
        if(!IsFull(q)){
            addQ(q,i);
        }
    }
    printf("del the elements:\n");
    while(!IsEmpty(q)){
        deleteQ(q,&i);
        printf("%d\n",i);
    }
    system("pause");
    return 0;
}
```

## （四）循环队列数组实现
 - 使用循环队列可以对数组中的空间重复使用
 - 循环队列相对于简单队列的核心区别在于%MAXSIZE

```c
//循环队列的实现
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 100
typedef struct Queue {
    int elements[MAXSIZE];
    int front; //队首指针
    int rear; //队尾指针
}Queue;
void initQueue(Queue **q){
    *q = (Queue *)malloc(sizeof(Queue));
    (*q)->front = 0;
    (*q)->rear = 0;
}

void addQ(Queue *q, int e){
    q->rear = (q->rear + 1)%MAXSIZE;
    q->elements[q->rear] = e;
}

void delQ(Queue *q, int *e){
    q->front = (q->front + 1)%MAXSIZE;
    *e = q->elements[q->front];
}

int IsEmpty(Queue *q){
    return (q->front == q->rear ? 1 : 0);
}

int IsFull(Queue *q){
    return ((q->rear + 1)%MAXSIZE == q->front ? 1 :0);
}

int main(void){
    int i;
    Queue *q;
    initQueue(&q);

    for(i=0; i < 30; i++){
        if(!IsFull(q)){
            addQ(q,i);
        }
    }
    printf("del the elements:\n");
    while(!IsEmpty(q)){
        delQ(q,&i);
        printf("%d\n",i);
    }
    system("pause");
    return 0;
}
```
