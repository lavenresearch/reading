# this program generate a post for jekyll automatically
import time

# basic information start

name = "An Overview of Data Warehousing and OLAP Technology"
category = "OLAP"
tags = "data warehouse","OLAP"
types = 0 # 0 for NOTE@, 1 for CONCLUSION@

# end

if types == 0:
    name = "NOTE@ " + name
else:
    name = "CONCLUSION@ " + name

content = '''---
layout: post
'''
content += "category : " + category
content += '''
tagline: ""
'''
i = len(tags)
content += "tags : ["
for tag in tags:
    content += tag
    i -= 1
    if i > 0:
        content += ","
content += "]"
content += '''
---
{% include JB/setup %}
'''

def gen_post(name, post_content, t = time.localtime()):
    post_name = time.strftime("%Y-%m-%d",t)+"-"+name
    f = open(post_name,"w")
    f.write(post_content)
    f.close()

def parse_name(origin_name):
    name_list = origin_name.split()
    return '-'.join(name_list)+".md"

gen_post(parse_name(name),content)
