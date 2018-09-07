---
layout: post
title:  "Java并发编程笔记(2)：线程创建和运行"
categories: Java多线程
tags:  Java Concurrency
author: mio4
---

* content
{:toc}








## （一）线程的状态

 - 首先要了解Java中线程有哪些状态，状态之间如何进行转换，每个状态的特点是什么 
 - 查看lang包中Thread源码：
```java 
    public enum State {
        /**
         * Thread state for a thread which has not yet started.
         */
        NEW,

        /**
         * Thread state for a runnable thread.  A thread in the runnable
         * state is executing in the Java virtual machine but it may
         * be waiting for other resources from the operating system
         * such as processor.
         */
        RUNNABLE,

        /**
         * Thread state for a thread blocked waiting for a monitor lock.
         * A thread in the blocked state is waiting for a monitor lock
         * to enter a synchronized block/method or
         * reenter a synchronized block/method after calling
         * {@link Object#wait() Object.wait}.
         */
        BLOCKED,

        /**
         * Thread state for a waiting thread.
         * A thread is in the waiting state due to calling one of the
         * following methods:
         * <ul>
         *   <li>{@link Object#wait() Object.wait} with no timeout</li>
         *   <li>{@link #join() Thread.join} with no timeout</li>
         *   <li>{@link LockSupport#park() LockSupport.park}</li>
         * </ul>
         *
         * <p>A thread in the waiting state is waiting for another thread to
         * perform a particular action.
         *
         * For example, a thread that has called <tt>Object.wait()</tt>
         * on an object is waiting for another thread to call
         * <tt>Object.notify()</tt> or <tt>Object.notifyAll()</tt> on
         * that object. A thread that has called <tt>Thread.join()</tt>
         * is waiting for a specified thread to terminate.
         */
        WAITING,

        /**
         * Thread state for a waiting thread with a specified waiting time.
         * A thread is in the timed waiting state due to calling one of
         * the following methods with a specified positive waiting time:
         * <ul>
         *   <li>{@link #sleep Thread.sleep}</li>
         *   <li>{@link Object#wait(long) Object.wait} with timeout</li>
         *   <li>{@link #join(long) Thread.join} with timeout</li>
         *   <li>{@link LockSupport#parkNanos LockSupport.parkNanos}</li>
         *   <li>{@link LockSupport#parkUntil LockSupport.parkUntil}</li>
         * </ul>
         */
        TIMED_WAITING,

        /**
         * Thread state for a terminated thread.
         * The thread has completed execution.
         */
        TERMINATED;
    }
```

 - 源码使用一个枚举类来保证线程的状态
 - 从中可知Java中线程有六种状态
   - NEW
   - RUNNABLE
   - BLOCKED
   - WAITING
   - TIMED_WAITING
   - TERMINATED
 - 线程状态之间的转换如下图 

![线程状态转换图](http://peh5n2dsb.bkt.clouddn.com/ThreadState.png)

 - 关于Waiting状态和Blocked状态的区别
   - Waiting表示线程don't want to be active
   - Blocked表示线程want to be active but can't 

## （二）创建启动线程

  - 创建线程有两种方式
    - extends Thread：继承Thread类
    - implements Runnable：实现Runnable接口
  - 其中第二种方式相对更好 
    - Java不同于C++，是单继承，继承是一种宝贵的资源，但是是可以实现多接口的
    - Thread类构造方法有Thread(Runnable target)，也就是实现Runnable接口的类产生新的线程，更容易实现资源共享
  - 线程启动方式为threadObject.start()
   - 不能直接调用run()方法，因为run方法并不会单独开启一个线程  

## （三）wait()和notify()方法
 - Thread.sleep()方法不会释放任何资源
 - 对于一个Object对象
   - 线程执行object.wait()方法会让这个对象进入等待队列，同时释放掉这个对象的锁，当前线程进入等待状态
   - 线程执行object.notify()方法会从等待队列中随机唤醒一个线程（使用前提是当前线程已经获得这个对象的锁）
 - wait()和notify()语句都应该包含在synchronized块中
 - wait()和notify()方法是线程之间通信的有效手段 
 - notifyAll()方法会唤醒所有线程

## （四）废弃方法
 - Thread.stop()：强制结束线程，可能会对读写数据有严重影响
 - Thread.suspend()和Thread.resume()：线程挂起和恢复，因为Thread.suspend()之后线程还是处于RUNNABLE状态并且不会释放自己资源的锁，所以可能造成系统死锁，不推荐使用

## （五）join()方法

```java 
package testJoin;

public class JoinMain {
	public volatile static int i = 0;
	public static class AddThread extends Thread{
		@Override
		public void run(){
			for(;i<10000;i++);
		}
	}
	public static void main(String[] args) throws InterruptedException{
		AddThread at = new AddThread();
		at.start();
		//at.join();
		System.out.println(i);
	}
}
```

 - at.join()表示当前线程（主线程）愿意等待at线程执行完后执行
   - 没有join()方法，执行结果为0
   - 有join()方法，执行结果为10000

