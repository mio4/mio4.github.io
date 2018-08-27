---
layout: post
title:  "数据结构基础(2)：链表"
categories: 数据结构  
tags:  C DataStructure
author: mio4
---

* content
{:toc}






## （一）链表基本操作
带有头结点的链表的基本操作：
 - 初始化链表
 - 删除链表中的节点
 - 向链表中添加节点
 - 查找指定元素
 - 判断链表是否为空

```c 
#include <stdio.h>
#include <stdlib.h>

struct Node;
typedef int ElementType;
typedef struct Node *PtrToNode; 
typedef PtrToNode List;
typedef PtrToNode Position;

struct Node {
    ElementType Element;
    Position Next;
};

List MakeEmptyList(List L); //生成一个空链表
int IsEmpty(List L); //判断链表是否为空
int IsLast(Position P, List L); //是否是链表中的最后一个节点
int Length(List L); //返回链表长度
Position Find(ElementType X, List L); //查找元素在链表中的位置
void Delete(ElementType X, List L); //删除指定元素的节点
Position FindPrevious(ElementType X, List L); //查找指定元素的前节点
void InsertBefore(ElementType X, List L, Position P); //在P节点前插入节点
void InsertAfter(ElementType X, List L, Position P); //在P节点后插入节点
void DeleteList(List L); //删除链表
Position Header(List L); //返回头结点
Position First(List L); //返回第一个节点
Position Advance(Position P); //返回节点的后节点
void Print(List L); //打印链表

List MakeEmptyList(List L){
    if (L != NULL){
        DeleteList(L);
    }
    L = (List) malloc(sizeof(struct Node));
    if(L == NULL){
        printf("Out of space\n");
        exit(1);
    }
    L->Next = NULL;
    return L;
}

int IsEmpty(List L){
    return L->Next == NULL; 
}

int IsLast(Position P, List L){
    return P->Next == NULL;
}

int Length(List L){
    int length = 0;
    Position P = L->Next; 
    while(P->Next != NULL){
        length++;
        P = P->Next; 
    }
    return length;
}

Position Find(ElementType X,List L){
    Position P = L->Next;
    while(P!=NULL && P->Element != X){ 
        P = P->Next;
    }
    return P;
}

void Delete(ElementType X, List L){
    Position TmpNode;
    Position P = FindPrevious(X,L);
    if(!IsLast(P,L)){
        TmpNode = P->Next;
        P->Next = TmpNode->Next;
        free(TmpNode);
    }
}

Position FindPrevious(ElementType X, List L){ 
    Position P = L;
    while(P->Next != NULL && P->Next->Element != X){
        P = P->Next;
    }
    return P;
}

void InsertBefore(ElementType X, List L, Position P){
    Position AddNode = (Position)malloc(sizeof(struct Node));
    Position PreviousNode = L;
    
    if(AddNode == NULL){
        printf("Out of space\n");
        exit(1);
    }
    while(PreviousNode->Next != P){ 
        PreviousNode = PreviousNode->Next;
    }
    AddNode->Element = X;
    PreviousNode->Next = AddNode;
    AddNode->Next = P;
}

void InsertAfter(ElementType X, List L, Position P){
    Position AddNode = (Position)malloc(sizeof(struct Node));
    Position AfterNode = P->Next;

    if(AddNode == NULL){
        printf("Out of space\n");
        exit(1);
    }
    AddNode->Element = X;
    AddNode->Next = P->Next;
    P->Next = AddNode;
}

void DeleteList(List L){
    Position tmp;
    Position P = L->Next;
    L->Next = NULL;
    while(P != NULL){
        tmp = P->Next;
        free(P);
        P = tmp;
    }
}

Position Header(List L){
    return L;
}

Position First(List L){
    return L->Next;
}

Position Advance(Position P){
    return P->Next;
}

void Print(List L){
    Position P = L->Next;
    while(P!=NULL){
        printf("%d ",P->Element);
        P = P->Next;
    }
    printf("\n");
}

int main(void){ //测试函数
    int i;
    List L = NULL;
    printf("创建一个空链表\n");
    L = MakeEmptyList(L);
    
    Position P = L;
    for(i=0;i <= 5;i++){
        InsertAfter(i,L,P);
        P = Advance(P);
    }
    printf("链表的长度是 %d\n",Length(L));
    printf("打印链表中的所有元素:\n");
    Print(L);

    printf("删除链表中的前两个元素\n");
    for(i=0;i < 2;i++){
        Delete(i,L);
    }
    printf("链表的长度是 %d\n",Length(L));
    printf("打印链表中的所有元素:\n");
    Print(L);

    printf("删除链表\n");
    DeleteList(L);
    if(IsEmpty(L)){
        printf("L是一个空链表\n");
    }
    system("pause");
    return 0;
}
```

## （二）单链表相关题型

### 0x0 逆序打印单链表
 - 使用递归实现单链表的逆序数据输出
```c 
void ReversePrint(pList plist){
    pNode cur = plist;

    if(cur == NULL){ //最后一层，直接return 
        return;
    }
    if(cur->next == NULL){ //倒数第二层，打印数据之后return 
        printf("%d ",cur->data);
        return;
    }
    ReversePrint(cur->next);
    printf("%d ",cur->data); 
}
```

### 0x1 反转单链表
 - 首先，如果是空链表不需要反转
 - 其次，如果链表只有一个节点不需要反转
 - 最后，考虑一般情况，从链表的头结点开始，逐个改变节点的指针直到尾节点

```c 
//逆转单链表
#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node* next;
}Node , *pNode;
typedef pNode pList;

void ReverseList(pList *pplist){ //因为需要改变
    pNode new_tmp_head = *pplist;
    pNode cur_node = NULL;
    pNode tmp_node = NULL;
    if(*pplist == NULL){
        return;
    } else if ((*pplist)->next == NULL){
        return;
    } else {
        cur_node = new_tmp_head->next; //从第二个节点开始
        new_tmp_head->next = NULL; //头节点指针置空
        while(cur_node != NULL){
            tmp_node = cur_node;
            cur_node = cur_node->next;
            tmp_node->next = new_tmp_head;
            new_tmp_head = tmp_node;
        }
        *pplist = new_tmp_head;
    }
}

pNode CreateList(int len){ //创建测试链表
    pNode pHead = (pNode)malloc(sizeof(Node));
    pHead->data = 1;
    pHead->next = NULL;
    int i;
    pNode pTail = pHead;
    for(i = 0;i < len-1;i++){
        pNode tmp = (pNode)malloc(sizeof(Node));
        tmp->data = i+2;
        tmp->next = NULL;
        pTail->next = tmp;
        pTail = tmp;
    }
    return pHead;
}

void PrintList(pNode pHead){ //打印链表
    pNode tmp_node = pHead;
    while(tmp_node != NULL){
        printf("%d ",tmp_node->data);
        tmp_node = tmp_node->next;
    }    
    printf("\n");
}

int main(void){ //验证链表是否成功逆转
    pNode pHead = CreateList(10);
    PrintList(pHead);
    ReverseList(&pHead);
    PrintList(pHead);
    system("pause");
    return 0;
}
```

### 0x2 单链表排序
 - 如果是空链表，不需要排序
 - 如果链表中只有一个节点，不需要排序
 - 对于一般情况，使用冒泡排序，定义一个尾指针，每次循环时从pHead开始比较，直到节点指针指向的是尾节点。这样一次循环后最后一个节点的值是最大值。然后将尾指针往前移动一个位，进行下一次循环。

```c 
void BubbleSort(pList *pplist){
    pNode cur_node = *pplist;
    pNode tail_node = NULL;
    if(cur_node == NULL){
        return;
    }
    if(cur_node->next == NULL){
        return;
    }
    while(cur_node != tail_node){
        while(cur_node->next != tail_node){
            if(cur_node->data > cur_node->next->data){
                int tmp = cur_node->data;
                cur_node->data = cur_node->next->data;
                cur_node->next->data = tmp;
                tail_node = NULL;
            }
            cur_node = cur_node->next;
        }
        tail_node = cur_node;
        cur_node = *pplist;
    }
}
```

## （三）双向循环链表
 - 双向链表：能够从某一节点从后向前遍历
 - 循环链表：链表的尾节点的next指针指向链表的头节点

```c 
#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next; //指向后继节点
    struct Node *prior; //指向前驱节点
}Node,*pNode;

pNode Create_List(int len){ //创建一个双向循环链表
    int i;
    pNode pHead = NULL;
    pNode tmp,pTail;

    for(i = 0;i < len;i++){
        //生成新节点
        tmp = (pNode) malloc(sizeof(Node));
        if(tmp == NULL){ //分配失败
            printf("Error\n");
            exit(1);
        }
        tmp->data = i+1;
        tmp->next = NULL;
        //将新节点插入链表中
        if(pHead == NULL){
            pHead = tmp;
            pHead->prior = pHead; //定义只有一个节点的双向循环链表：指针都指向自身
            pHead->next = pHead; 
        } else {
            tmp->next = pTail->next;
            pHead->prior = tmp;
            pTail->next = tmp;
            tmp->prior = pTail;
        }
        pTail = tmp;
    }
    return pHead;
}

void Print(pNode pHead){ 
    printf("%d ",pHead->data);
    pNode tmp = pHead->next;
    while(tmp != pHead){
        printf("%d ",tmp->data);
        tmp = tmp->next;
    }
}

int main(void){
    pNode pHead = Create_List(10);
    Print(pHead);
    system("pause");
    return 0;
}
```
