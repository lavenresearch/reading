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
  &raquo;&raquo;&raquo;&raquo;<span class="post-date">{{ post.date | date_to_string }}</span>&raquo;&raquo;&raquo;&raquo;

  <div class="post">
    <h3 class="post-title">
      <a href="{{ BASE_PATH }}{{ post.url }}">
        {{ post.title }}
      </a>
    </h3>

  </div>
  {% endfor %}
</ul>


