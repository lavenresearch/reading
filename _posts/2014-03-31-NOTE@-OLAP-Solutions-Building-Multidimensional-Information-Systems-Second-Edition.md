---
layout: post
category : OLAP
tagline: ""
tags : [data warehouse,OLAP]
---
{% include JB/setup %}

# Preparation for Reading
## 内容组织
1. Part One The Need for Multidimensional Technology
    * OLAP 的定义、源起、基本要求以及如何与企业信息系统进行整合。
    * 从传统的行列存储为起点，进入 multidimensional data structures and flows。
    * how to think clearly in N dimensions.(to design or use multidimensional information system)
2. Part Two Core Technology
    * 介绍本书使用的语言和教学方式（chapter 4）。
    * 一个dimension的内部机制，例如，分层和排序（chapter 5）。
    * 介绍多维的模型，处理稀疏问题及异构数据源的信息整合（chapter 6）。
    * 介绍写multidimensional formulas的方式，及一些可重用的formulas。（chapter 7）。
    * 建立源数据和多维数据模型之间的联系（chapter 8）。
    * 数据可视化的应用场景，原理及相关技术（chapter 9）。
    * 多维数据模型可进行的优化的 方 面（**physically optimized, exploring optimization within machines, across applications, across network tiers, and across time.**）（chapter 10）
3. Part Three Applications
    * 一个设计及使用多维信息系统的实例。
    * 一个企业级OLAP解决方案的背景，为13~16章服务（chapter 12）
    * 特定商业过程（例如，出售，市场，购买，存货，基于事件的管理等）相关的dimension，cube design和key formula creation（chapter 13-16）。
    * 一个完全整合的跨企业的计算实例，从某一个商品的售出到原料购买，计算在这个过程中的利润（chapter 17）。
4. Part Four Further Issues
    * 总结和扩展前三部分的内容。
    * 给出评价OLAP产品的综合标准（chapter 18）。
    * 对几个商业产品的OLAP语言进行对比（chapter 19）。
    * 统一的decision support system的需求及属性（chapter 20）。
5. appendix
    * formulas的索引（A）
    * 从benchmark和api的角度对一些工业事件进行描述（B）
    * 书中使用的语言的简介（C）
    * 术语表（D）
    * dimensions和measures之间的一些区别（E）
    * 多维信息系统的逻辑基础，及这些基础需求与标准规范之间的对比（F）
    * Codd's 原始的12个特点（关系型数据库的基本特点）（G）

# The Functional Requirements of OLAP Systems
## Requirements in short
1. Rich dimensional structuring with hierarchical referencing
2. Efficient specification of dimensions and dimensional calculations
3. Separation of structure and representation
4. Flexibility
5. Sufficient speed to support ad hoc analysis
6. Multi-user support

## OLAP的层次
1. OLAP的概念
    * the notion or idea of multiple hierarchical dimensions
2. OLAP的语言
    * 数据定义语言（DDL），数据管理语言（DML），数据表示语言（DRL）。更多的是对这些已有语言进行OLAP需求的优化，而不是重新建立新的OLAP专属语言。
    * 相对应的language parser。
3. OLAP产品
4. Full OLAP product
    * 包括compiler，storage还有access method（针对决策系统的快速数据访问及计算需求进行优化）。

## olap和data mining的区别
olap提供数据描述模型，data mining提供数据解释模型。




