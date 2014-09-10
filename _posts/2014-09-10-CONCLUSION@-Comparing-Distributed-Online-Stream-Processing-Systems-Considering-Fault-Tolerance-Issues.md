---
layout: post
category : Stream Processing
tagline: ""
tags : [storm,survey,millwheel,s4,spark streaming,Fault Tolerance]
---
{% include JB/setup %}

# 基本知识

- 流计算中会遇到的两种错误
    + 缓存溢出
    + 节点失效
- 错误类型
    + Byzantine faults : 在运行，但是输出有错误，难以检测。
    + fail-stop faults : 不能运行，容易检测。
    + fail-stutter faults : 在运行，但是性能很差，就是stragglers。难以检测。

# 容错策略

1. Active Replication
    - 通过对比冗余operators之间的输出，可以检测异常。
2. Passive Replication
    - 只需要设置固定个数的容错节点，这些节点在没有错误发生时，什么也不做。在有错误发生时，使用全部的历史输入将operator的状态恢复出来。
    - 恢复时间很长。
3. Checkpoint
    - 将整个系统的看作是一系列的状态，将这些状态的checkpoint数据存储在可靠存储里。
        + 涉及到状态间的一致性问题。因此有uncoordinated和coordinated的checkpoint。
        + 但是在流数据处理系统中，由于可以容忍恢复后的非一致状态，因此，通常不用生成一致的checkpoint。这是流处理容错和传统分布式计算容错不同的地方。
4. Upstream Backup
    - 在失效和恢复之间的备份队列可能会很长。

# 主要流处理框架中容错

1. MillWheel
    - 特点
        + tuple中包含timestamp
        + 可动态增加或删除topology中的operators
    - 将persistent state保存在可靠存储中，如，bigtable，spanner。
    - Operator接收到tuples后会检查其是否为duplicated，如果不是，处理tuple，将状态存储到bigtable中，向发送方发送确认消息。
2. S4
    - 使用zookeeper进行错误检测。其中timeout阈值由node规定。
    - 状态恢复需要用户程序显式参与。
    - 使用异步checkpoint。
3. Spark Streaming
    - 使用RRD，在失效后，从最近的checkpoint重新计算出来。
    - 输入数据以多副本的方式存储在多个节点的内存中，因此其中之一失效了，不会影响整体对输入数据的处理。
4. Storm
    - 使用zookeeper协调nimbus和worker。
    - 在spout备份输出的tuples，直到接收到bolts的ACK。
    - Nimbus和Supervisor是无状态的。
