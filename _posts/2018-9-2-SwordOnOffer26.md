---
layout: post
title:  "矩阵中的路径"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}






## 矩阵中的路径

**题目描述**
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

**分析**

 - 在二维矩阵中寻找指定路径，经常使用回溯法
 -  代码执行的顺序是
   - 首先遍历整个矩阵，直到找到字符和元素的第一个字符相同的点
   - 然后从这个点开始，找第二个点，怎么找呢？就这个点的上下左右四个方向去探测，如果探测成功，那么递归到下一个点的情况，如果探测失败，那么就倒退到上一步（回溯），从另外的点开始
   - 需要注意的是，设置visited数组表示点是否已经走过，如果回溯的话，不仅需要把路径长度-1，还需要清除走过的痕迹即visited数组对应点的值
   - PathLength表示走过的长度，如果PathLength==str.length，则表示已经找到所有字符，完成寻找，返回true   
 - 边界条件
   - 矩阵为空，字符串集合为空 


```java 
public class Solution {
	public static boolean[][] visited = null;
	public static boolean hasPath(char[] matrix, int rows, int cols, char[] str)
	{
		if(matrix == null || rows < 1 || cols < 1 || str == null)
			return false;

		int PathLength = 0;
		visited = new boolean[rows][cols];
		for(int i = 0; i < rows; i++){
			for(int j = 0; j < cols; j++){
				if(PathHelper(matrix,i,rows,j,cols,str,PathLength))
					return true;
			}
		}

		return false;
	}

	public static boolean PathHelper(char[] matrix, int i,int rows, int j,int cols,char[] str, int PathLength){
		if(PathLength == str.length)
			return true;

		boolean hasPath = false;
		if(i>=0 && i < rows && j >= 0 && j < cols && matrix[i*cols+j] == str[PathLength] && !visited[i][j]){ //找到了字符
			PathLength++;
			visited[i][j] = true;

			//接下来继续判断
			hasPath = PathHelper(matrix,i-1,rows,j,cols,str,PathLength)
					|| PathHelper(matrix,i+1,rows,j,cols,str,PathLength)
					|| PathHelper(matrix,i,rows,j-1,cols,str,PathLength)
					|| PathHelper(matrix,i,rows,j+1,cols,str,PathLength);

			if(!hasPath){
				PathLength--;
				visited[i][j] = false;
			}
		}

		//没有找到字符，返回false
		return hasPath;
	}

	public static void main(String[] args){
		char[] cs = {'a','b','t','g','c','f','c','s','j','d','e','h'};
		char[] str = {'b','f','c','e'};
		System.out.println(hasPath(cs,3,4,str));

		char[] cs2 = {'A','B','C','E','S','F','C','S','A','D','E','E'};
		char[] str2 = {'A','B','C','B'};
		System.out.println(hasPath(cs2,3,4,str2));
	}


}
```