import os

default_config = """##CONFIG FILE FOR PYBLOGGER1.0##
--------------------------------------------------------------------------------------
root_dir:layouts             : Leave blank if not organized, highly not recommended.
pages_dir:pages              : Where the pages live :) they live happily organised.
headerfile:header.html       : Some headerfile that you'll use.
blogsdir:blogs               : A place to keep all the blogs.
---------------------------------------------------------------------------------------"""
#==========================================================================================================================
default_index = """{% extends project_name+"/layouts/header.html" %}

{% block main %}
 <!-- Start Block
 –––––––––––––––––––––––––––––––––––––––––––––––––– -->
<div class="row">
<div class="six columns offset-by-three">
<h1 ><strong>{{project_name}}</strong><br></h1>
<p>Welcome to my blog, here I talk about things that are of interest to me. And hopefully will be of interest to you too.</div></p>
</div>
<ul>
<li><a href="#">Home</a></li>
{% for tab in tabs %}
<li><a href="{{project_name}}/tabshtml/{{tab.name}}.html">{{tab.name}}</a></li>
{% endfor %}
</ul>
<h4>Featured Blogs<h4>
<div class="row">
{% for post in posts %}
    {% if loop.index >3 %}
        </div>
<br>
        <div class="row">
    {% endif %}
    <div class="one-third column itembox">
    <div class="row info">
<center><h6>#{{post['index']}} {{post['date']}}</h6></center>
   <button style="width:100%" onclick="document.location='./{{project_name}}/html/{{post['name']}}.html'">{{post['name']}}</button>
</div>
     </div>
{% endfor %}
</div>
</div>
<!-- End block
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
{% endblock %}
"""
#==========================================================================================================================
def extension_header(project_name):
    extension_header = """{% extends '"""+project_name+"""/layouts/header.html' %}
{% block main %}
<button onclick="document.location='./../../index.html'"> Back to home</button>
"""
    return extension_header
extension_footer = """
{% endblock %}
"""
#==========================================================================================================================
default_page_instructions = """
**Lesson 1:** Introduction and enviornment setup
 
> **ProTip:** You can disable any **Markdown extension** in the **File properties** dialog.


## Why python?

As of 2019. Python surpasses Java to become the second most popular language on git hub open source repos.[Most popular languages on Github 2019](https://octoverse.github.com/#top-languages). 

|                |    Speed                      |Simplicity                   |Utility|Popularity|packagemanager | 
|----------------|-------------------------------|-----------------------------|-----------|----|---|
|C               |fast            |medium           | Pretty good, doesn't have a massive confusing web of libraries to learn, but can mean you have to implement your own solutions          |  ok  | not so good|
|C++          |fast            |medium              | Lower level, controlling hardware,backend for engines(game engines,etc) and compute frameworks(tensorflow etc)  | highish  | not so good
|`Python`          |slow|simple|Pretty good, source of interface for a lot of open source projects, Open BCI, open AI gym, etc etc etc.      |      high      |   pretty good|
|JavaScript          |slow|simple| Pretty much mostly the web, can be used to do other things, but javascript is not really the most well designed language...     |  high |    pretty good|
|  Java     |fast|simple|     Pretty good, Android development etc, all kinds of things run java, but getting out of date and the package manager sucks...             |  medium |  pretty good

Professor Peter Norvig on python: "I was trying to find a language that could most resemble my pseudo code and be intuitive for my students, and it turned out that python was basically my pseudo code"
`Python` is Simple, compact,and well supported, it is useful for many things and really great  as a language for non-programmers.



"""
