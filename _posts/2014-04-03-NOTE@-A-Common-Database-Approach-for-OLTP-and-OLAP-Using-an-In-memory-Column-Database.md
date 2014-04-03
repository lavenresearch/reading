---
layout: post
category : OLAP
tagline: ""
tags : [In-memory,OLAP,OLTP,Column Database]
---
{% include JB/setup %}

20140403[^1]

# 背景知识补充
1. star schemas
2. shared nothing approach
3. time travel
4. snapshot isolation via timestamps[15]
5. minimal projection
6. horizontal and vertical partition
7. compression for column store( by dictionaries )

# 想法
1. real time BI
    * materialized view calculating on the fly means real time query calculation. In real time BI, any pre-built materialized view or aggregated information is considered stale.
    * to realize the real time BI, streaming processing related technology may be needed.

# Introduction
**这篇论文的最终目标是：**
_all business transaction queries, including unrestricted aggregations and time-base sequences, can be answered in just a couple of seconds(including the surprisingly costly presentation layer)_

## OLTP and OLAP
1. both system are based on the relational theory, but use different technical approaches.
2. OLTP
    * tuples are arranged in rows
    * rows are stored in blocks( blocks reside on disk and are cached in memory in database server. )
    * sophisticated indexing for fast access to single tuples
    * query requesting multiple tuples will became slower as the number of requested tuples increase
3. OLAP
    * data organized in star schemas
    * a popular optimization: compress attributes(columns) with the help of dictionaries
    * after the conversion of attributes into integers, processing becomes faster

## shortcomings of data warehouse
with the flexibility and speed we gained, the price are:
1. additional management of extracting, and loading data, as well as controlling the redundancy.

## column store for OLTP
1. 虽然OLTP只是作为OLAP的一个数据来源，但是在一个系统中同时支持OLTP和OLAP能够使这两个部分对它们的用户更有价值
2. 多核环境下，transaction不能很好的并行
3. in-memory row database 相对于等量内存的 cache 没有性能优势

因此，使用 in-memory column store for OLTP 的想法诞生了。

## 论述思路概述
1. column store for OLTP 的可行性
    * column store 适应现代的CPU结构
    * 可以适应 update-intensive 的应用（使用 insert 代替 update）
        - insert-only 造成的影响（lock）
    * 内存使用效率更高
2. 使用 column store 时 transaction 的执行
3. 对应用开发的影响
4. 在 SaaS 中使用

# column storage is best suited for modern CPUs
enterprise applications are to a large extent memory bound

1. 列存储节省存储空间
2. 企业级计算更多是基于 set processing 而不是 direct tuple access
    * 因此列存储能够带来实质的好处
3. 列存储具有良好的并行性（更好的任务划分）
4. 更高的 scaning 性能
    * 以良好的并行性作为基础
    * 使用 full column scan 代替 index 具有可行性
        - 解放了应用的数据访问限制
        - 消除了数据更新时的冗余数据的更新的问题

# column storage is suited for update-intensive applications
面临的问题：数据更新可能需要重新进行 compression（对整个 column 都有影响）

1. materialized views and aggregates
    * 优化了读性能
    * 增加了写开销和系统管理复杂性
2. 三种 update
    * aggregate update
        - 采用 always on the fly 的方式
        - 这种情况，需要进行越多的 aggregation 越好，因为无论多少只需要进行一次完整的 column scan（但是对于 row 存储，更多的aggregation意味着读取更多的已有aggregation信息，因此其与时延成线性增长关系。）
    * status update
        - 建议不对其进行 compression
        - 也可以使用 insert-only 的方式实现 update
    * value update
        - 企业级应用更新很少
        - 使用insert-only的方式（用insert替换update）
            + 更新全部交给 delta manager（写优化存储）
            + 减少的update相当于减少lock，这使得任务更容易被分割，有利于并行化
3. 结果是
    * 使用 insert-only + calculation on the fly 代替了 indices + materialized views + change history

# consequences of the insert-only approach
1. application level locks
    * applications "think" in Object(multiple tables, multiple tuples in on table)
    * shared lock on object( 一次只能有一个 transaction 修改一个 object)
    * implemented using an in-memory data structure
2. database locks
    * 定位最新的tuple（无 update timestamps）（ time travel ）
    * 保存tuple所有的versions
        - 对历史数据的检索很常见
        - 省去了 log 的开销
    * 不存在并发中的一致性问题
        - 所有queries通过对比timestamps后看到的数据是一致的

# column storage is superior to row storage with regards to memory consumption
1. combined system for OLTP and OLAP 的需求
    * set processing
    * fast inserts
    * maximum (read) concurrency
    * low impact of reorganization
2. 上述需求对compression有影响
    * column store compression
        - conversion of attributes values
        - elimination of column with null values
        - interpreting the values(0,0.0,空白) to null
        - applications "think" in default value, 需要在 default value and null 之间进行变换
3. 内存的高效使用
    * 列存储压缩效率更高：10x
    * 无 materialized views 等存储开销：2x
    * horizontal partition：5x

# what happens to typical data-entry transactions?
1. transaction 的三个部分：
    * user data entry(登记？)
    * data validation
    * database update(reduce to mere insert)
2. delta storage
    * column storage
    * insert 和 retrieval 互相影响（需要避免不必要的locking）
    * 为了减小insert对 dictionary tables 和 合并操作（main storage 和 delta storage），一个两层的delta storage的组织方式正在调研阶段）
3. 研究的重点在于
    * 在 compression, insert speed, concurrent queries interfere 之间的权衡

# the impact on application development
1. 使用 extended SQL 完全控制算法参数
2. 应用级的cache失去效果
3. adding new column is simple
4. transaction 的简洁性：forword recovery approach
5. 应用可以认为SQL server没有错误，因此免除检查

# column storage in SaaS applications
In SaaS (Software as a Service) applications several aspects of column storage are helpful. Columns which are unused are only represented by a stub. The introduction of a new attribute to a table means an update of the metadata and the creation of a stub for the column [2]. The attributes can from then on be used by the application. This is an important feature for the ongoing development of the application without any interruption for the user. The join with external data, which after import into the host system is held in column storage, is extremely efficient even for very large tables (minimum main memory accessed). In both cases the greatly improved response time will be appreciated. Not only can the application now determine what base date for a query should be chosen but the development of the content (attributes) of individual tuples can be monitored (e.g. lifecycle of a customer order, control of sensitive data in human resources or accounts payable). 

# future research
1. 根据时间划分数据的标准，将历史数据设置为只读
2. Vertical Partitioning - In enterprise applications several chunks of a single relation tend to be grouped together by their access patterns. Using a vertical partitioning approach allows performance improvements when reading the content of those groups. 


[^1]: H. Plattner, “A Common Database Approach for OLTP and OLAP Using an In-memory Column Database,” in Proceedings of the 2009 ACM SIGMOD International Conference on Management of Data, New York, NY, USA, 2009, pp. 1–2.
