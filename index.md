---
layout: page
title: Hello Papers!
tagline: Research Reading Notes
---
{% include JB/setup %}

## Reading Notes

<ul class="posts">
  {% for post in site.posts %}
<!--     <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li> -->
  <div class="post">
    <h3 class="post-title">
      <a href="{{ BASE_PATH }}{{ post.url }}">
        {{ post.title }}
      </a>
    </h3>

    <span class="post-date">{{ post.date | date_to_string }}</span>

  </div>
  {% endfor %}
</ul>


