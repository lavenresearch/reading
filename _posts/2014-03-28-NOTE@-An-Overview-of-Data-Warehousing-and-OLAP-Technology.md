---
layout: post
category : OLAP
tagline: ""
tags : [data warehouse,OLAP]
---
{% include JB/setup %}

20140328-An Overview of Data Warehousing and OLAP Technology[^1]
# 融合
1. 衍生数据的更新问题
2. 数据存储格式不同
3. 数据范围不同

# OLAP 的特殊需求（相对于OLTP）
1. OLAP 要求多个 OLTP 数据库及其历史数据的融合
    * 数据异构
    * 数据库规模大（几百GBs或者TBs）
2. query 涉及范围广
    * 一个 query 可以涉及到几百万条记录
3. 数据多维组织方式（列存储）
    * 每一个维度由多个属性组成。属性之间可能具有层级关系（例如，时间维度的属性包括：年，季度，月，周，日等，这几个属性之间具有层级关系；产品维度的属性，包括：类别，上市时间，平均利润率等属性）

# Data Warehouse 的组成
1. 实现方式：基于RDBMS，列存储
2. 涉及范围：enterprise-wide，departmental subsets（ data marts ）

## 组件
1. 数据收集（ 来自多个operational databases和外部数据 ）
2. 数据整合（ 异构数据的 cleaning, transforming and integrating ）
    * After extracting, cleaning and transforming, data must be loaded into the warehouse. Additional preprocessing may still be required: **checking integrity constraints; sorting; summarization, aggregation and other computation to build the derived tables** stored in the warehouse; **building indices** and other access paths; and **partitioning** to multiple target storage areas. Typically, batch load utilities are used for this purpose. In addition to populating the warehouse, a load utility must allow the system administrator to **monitor status, to cancel, suspend and resume a load, and to restart after failure with no loss of data integrity**.
3. 数据更新（ 将数据加载到 data warehouse 中，并更新 ）
    * 数据更新包括相应数据及其**衍生数据**，例如，indices 和 materialized views。
4. 数据备份（ 将数据备份到慢一些的存储设备中 ）
5. 数据处理（ query tools, report writers, analysis tools, and data mining tools. ）
6. data warehouse 管理（ repository for storing and managing meta data, and tools for monitoring and administering the warehousing system. ）

## Warehouse Server
1. choose indices and materialized views( pre-computed summary information )
2. Optimization of complex queries
3. parallelism needs to be exploited to reduce query response times.
4. Finally, decision support databases contain a significant amount of descriptive text and so indices to support text search are useful as well.

### Materialized Views(整合信息)
1. challenges to use materialized views
    * identify the views to materialize
    * exploit the materialized views to answer queries
    * efficiently **update** the materialized views **during load and refresh**.
2. 使用
    * 使用部分整合信息组合生成更进一步的整合信息。因此选择部分整合信息（generator）也很重要。

### 其他优化
1. 复杂query的优化
    * queries 和合并
    * reduce invocations
    * flattening queries 的优化
2. 并行处理
    * overlapping scans of multiple concurrent requests
# Metadata 及 warehouse 管理
1. administrative metadata
    * Administrative metadata includes all of the information necessary for setting up and using a warehouse: descriptions of the source databases, back-end and front-end tools; definitions of the warehouse schema, derived data, dimensions and hierarchies, predefined queries and reports; data mart locations and contents; physical organization such as data partitions; data extraction, cleaning, and transformation rules; data refresh and purging policies; and user profiles, user authorization and access control policies.
2. business metadata
    * Business metadata includes business terms and definitions, ownership of the data, and charging policies.
3. operational metadata
    * Operational metadata includes information that is collected during the operation of the warehouse: the lineage of migrated and transformed data; the currency of data in the warehouse (active, archived or purged); and monitoring information such as usage statistics, error reports, and audit trails.

[^1]: S. Chaudhuri and U. Dayal, “An overview of data warehousing and OLAP technology,” Sigmod Record, vol. 26, no. 1, pp. 65–74, 1997.

