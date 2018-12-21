---
layout: post
title:  "整数中1出现的次数"
categories: 剑指Offer  
tags: DataStructure
author: mio4
---

* content
{:toc}






## 整数中1出现的次数
**题目描述**
求出1~ 13的整数中1出现的次数,并算出100~ 1300的整数中1出现的次数？为此他特别数了一下1~ 13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1到n中1出现的次数）。


**分析**

 - 首先最容易想到的方法就是遍历1 ~ n中的每个数，统计1出现的次数，求和之后得到结果

```java 
public class Solution {
	public static int NumberOf1Between1AndN_Solution(int n) {
		int cnt = 0;
		for(int i=1; i <= n; i++){
			cnt += getOneNum(i);
		}
		return cnt;
	}

	public static int getOneNum(int n){
		int cnt = 0;
		while(n != 0){
			if(n % 10 == 1)
				cnt++;
			n /= 10;
		}
		return cnt;
	}
}
```

  - 对于每个getOneNum的时间复杂度为O(logn)，对于所有数求和的时间复杂度为O(nlogn)
  - 这个算法的问题和递归求解斐波那契数列一样实质上是进入了冗余计算的，比如统计211和212的1的数量，使用取余和求模都统计了210这个相同的部分，所以增加了时间复杂度
  - 如果将1 ~ n看作一个整体，对于整体进行分析，就能减少冗余计算（比较考验数学功底）


```java 


public static int NumberOf1Between1AndN_Solution(int n) {
		return NumberOfXBetween1AndN_Solution(n,1);
	}

  public static int NumberOfXBetween1AndN_Solution(int n,int x) {
        int high,low,curr,tmp,i = 1;
        high = n;
        int total = 0;
        while(high!=0){
            high = n/(int)Math.pow(10, i);// 获取第i位的高位
            tmp = n%(int)Math.pow(10, i);
            curr = tmp/(int)Math.pow(10, i-1);// 获取第i位
            low = tmp%(int)Math.pow(10, i-1);// 获取第i位的低位
            if(curr==x){
                total+= high*(int)Math.pow(10, i-1)+low+1;
            }else if(curr<x){
                total+=high*(int)Math.pow(10, i-1);
            }else{
                total+=(high+1)*(int)Math.pow(10, i-1);
            }
            i++;
        }
        return total;        
    }
```



### 参考文章
http://www.cnblogs.com/nailperry/p/4752987.html 