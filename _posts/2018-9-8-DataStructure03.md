---
layout: post
title:  "数据结构基础(3)：树"
categories: 数据结构
tags:  C DataStructure
author: mio4
---

* content
{:toc}




[TOC]


# （一）树
## (1)基本概念

 - 根：没有父亲的节点
 - 树叶：没有儿子的节点
 - 兄弟节点：具有相同的父亲节点
 - 深度：从根到节点之间的唯一路径长度
 - 高度：从节点到所有树叶中最长的长度

>深度和高度的概念和现实中树的模型一致

## (2)基本分类

 - 二叉树(Binary Tree)：对于树中的每一个节点，最多有两个子节点
 - 满二叉树(Perfect Binary Tree)：所有的叶子节点的深度相同，并且除了叶子节点的节点的度都为2
 - 完全二叉树(Complete Binary Tree)：从根节点到倒数第二层是满二叉树，最底层可以不填满，但是所有的叶子节点必须靠左对齐

>所有的满二叉树都是完全二叉树，而完全二叉树不一定是满二叉树


# （二）二叉查找树
> 二叉查找树/二叉搜索树(Binary Search Tree)，对于树中每一个节点，它的左节点（如果存在）的值总是小于根节点，它的右节点（如果存在）的值总是大于根节点。

二叉查找树的性质：

 - 左子树上所有节点的值都小于根节点
 - 右子树上所有节点的值都大于根节点
 - 左右子树都是二叉查找树

使用结构体来描述一般的树：

```c
typedef struct TreeNode *PtrToNode;
typedef struct TreeNode *Tree;
typedef struct TreeNode *Position;
typedef int ElementType;

struct TreeNode {
    ElementType element;
    Tree lchild;
    Tree rchild;
};
```

## (1)BST树添加节点
树添加节点是一个从上往下的过程，如果当前树是空节点，那么构造一个节点填充数据，否则根据存储数据的相对大小来决定是插入到树的左子树还是右子树，然后在子树中进行判断，这是一个递归过程。

```c 
Tree Insert(ElementType x, Tree T){
    if(T == NULL) {
        //create and return one-node tree
        T = (Tree) malloc(sizeof(struct TreeNode));
        if(T == NULL) {
            printf("malloc tree node error!");
        } else {
            T->element = x;
            T->rchild = T->lchild = NULL;
        }
    } else if (x < T->element) {
        T->lchild = Insert(x, T->lchild);
    } else if (x > T->element) {
        T->rchild = Insert(x, T->rchild);
    }
    return T;
}
```

## (2)BST树删除节点

```c 

```

# （三）二叉树的遍历
二叉树一般有三种遍历方式：

  - 中序遍历：先遍历左子树，再访问根节点，再遍历右子树
  - 前序遍历：先访问根节点，再遍历左子树和右子树
  - 后序遍历：先遍历左子树和右子树，再访问根节点

三种遍历方式的区别实质是访问根节点的顺序，实现方式可以分为递归实现和循环实现

## (1)递归实现

```c 
void inOrder(Tree T) {  //中序遍历
    if(T != NULL){
        inOrder(T->lchild);
        printf("%d ",T->element);
        inOrder(T->rchild);
    }
}

void postOrder(Tree T) { //后序遍历
    if(T != NULL) {
        postOrder(T->lchild);
        postOrder(T->rchild);
        printf("%d ",T->element);
    }
}

void preOrder(Tree T) { //前序遍历
    if(T != NULL) {
        printf("%d ", T->element);
        preOrder(T->lchild);
        preOrder(T->rchild);
    }
}
```

中序遍历的性质：

 - 对二叉搜索树的中序遍历可以得到一个顺序递增的序列

## (2)非递归实现

>要实现非递归可以是自己维护一个栈，个人感觉非递归的代码虽然不长，但是设计非常精妙，值得反复品位。

**前序遍历**：

```c 
void preOrder2(Tree T){
    Tree stack[1000];
    Tree p = T;
    int top = 0;
    while(p!=NULL || top!=0){
        if(p!=NULL){
            printf("%d ",p->element);
            stack[top++] = p;
            p = p->lchild;
        } else{
            p = stack[--top];
            p = p->rchild;
        }
    }
}
```


**中序遍历**：

 - 循环结束的条件是栈为空并且p节点为空
 - 首先将所有"靠左"的节点存入栈中，栈中节点的意义是当前节点的父节点
 - 如果节点为空，则访问父节点，下一个访问的节点是右子节点

```c 
void inOrder2(Tree T){
    Tree stack[1000];
    Tree p = T; 
    int top = 0;
    while(p!=NULL || top!=0){ 
        if(p!= NULL){
            stack[top++] = p;
            p = p->lchild;
        }
        else{
            p = stack[--top];
            printf("%d ",p->element);
            p = p->rchild;
        }
    }
}
```

前序遍历和中序遍历代码的区别是访问根节点的时间，后序遍历代码相对复杂一点：

**后序遍历**：

```c 

```

# （三）红黑树


# （四）