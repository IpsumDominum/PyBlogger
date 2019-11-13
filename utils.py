import os
import shutil
import mistune
from boilerplates import *
from jinja2 import Template, Environment, BaseLoader,FileSystemLoader
from datetime import date
abs_root_path = os.path.abspath(__file__).strip("utils.py")
class PyBlogger:
    def __init__(self,project_name):
        loader = FileSystemLoader(os.getcwd())
        self.project_name = project_name
        self.jinja = Environment(loader=loader)
        self.markdown = mistune.Markdown()
        try:
            config_dict = {}
            with open("config.txt",'r') as config:
                config = config.readlines();
                config_dict['root_dir'] = config[2].replace(" ","").split(":")[1].strip("\n")
                config_dict['pages_dir'] = config[3].replace(" ","").split(":")[1].strip("\n")
                config_dict['headerfile'] = config[4].replace(" ","").split(":")[1].strip("\n")
                config_dict['blogsdir'] = config[5].replace(" ","").split(":")[1].strip("\n")
            self.config_dict = config_dict
        except FileNotFoundError:
            self.config_dict = {}
    def get_posts(self):
        return [x[:-5] for x in os.listdir(os.path.join(self.project_name,"html"))]
    def get_tabs(self):
        tabs = []
        for i,markdown in enumerate(os.listdir(os.path.join(self.project_name,"tabs"))):
            if(markdown[-2:] !="md"):
                continue
            with open(os.path.join(self.project_name,"tabs",markdown),"r") as markdownfile:
                template = self.compilemarkdown(markdownfile.read())
            with open(os.path.join(self.project_name,"tabshtml",markdown[:-3]+".html"),"w") as file:
                file.write(template.render(project_name=".."))
            tabs.append({'name':markdown[:-3]})
        return tabs
    def initialize_project(self):
        try:
            os.mkdir(self.project_name)
            os.mkdir(self.project_name+"/layouts")
            os.mkdir(self.project_name+"/pages")
            os.mkdir(self.project_name+"/html")
            os.mkdir(self.project_name+"/tabs")
            os.mkdir(self.project_name+"/tabshtml")
            os.mkdir(self.project_name+"/layouts/static")
            shutil.copyfile(os.path.join(abs_root_path,"themes","default","header.html"),os.path.join(self.project_name,"layouts","header.html"))
            shutil.copytree(os.path.join(abs_root_path,"themes","default","css"),os.path.join(self.project_name,"layouts","css"))
            with open(os.path.join(self.project_name,"config.txt"),"w") as configfile:
                configfile.write(default_config)
            with open("index.html","w") as indexfile:
                loader = FileSystemLoader(os.getcwd())
                template = Environment(loader=loader).from_string(default_index)
                indexfile.write(template.render(project_name=self.project_name,posts=["example"]))
            print("-"*40)
            print("successfully created a new project :) edit config.txt to configure")
            print("-"*40)
        except Exception as e:
            print(e)
    def new_post(self):
        #new post, ask for a name, then add an empty page.md in the pages directory :)
        print("What is the name of the post:",end="")
        post_name = input()
        with open(os.path.join(self.project_name,"pages",post_name+".md"),"w") as file:
            file.write("#"+post_name+"\n"+default_page_instructions)
        compiled = self.compilemarkdown(default_page_instructions).render(project_name="..")
        with open(os.path.join(self.project_name,"html",post_name+".html"),"w") as file:
            file.write(compiled)
    def new_tab(self):
        print("What is the name of the tab:",end="")
        tab_name = input()
        with open(os.path.join(self.project_name,"tabs",tab_name+".md"),"w") as file:
            file.write("#"+tab_name+"\n"+default_page_instructions)
        compiled = self.compilemarkdown(default_page_instructions).render(project_name="..")
        with open(os.path.join(self.project_name,"tabshtml",tab_name+".html"),"w") as file:
            file.write(compiled)
    def compile(self):
        #compile all markdown files in the directory,and refresh index page
        posts = []
        tabs = self.get_tabs()
        for i,markdown in enumerate(os.listdir(os.path.join(self.project_name,"pages"))):
            if(markdown[-2:] !="md"):
                continue
            with open(os.path.join(self.project_name,"pages",markdown),"r") as markdownfile:
                template = self.compilemarkdown(markdownfile.read())
            with open(os.path.join(self.project_name,"html",markdown[:-3]+".html"),"w") as file:
                file.write(template.render(project_name=".."))
            today = date.today().strftime("%A %d. %B %Y")
            posts.append({'name':markdown[:-3],'date':today,'index':i+1})
        with open("index.html","w") as indexfile:
            template = self.compilehtml(default_index)
            indexfile.write(template.render(project_name=self.project_name,posts=reversed(posts),tabs=tabs))
    def compilemarkdown(self,md):
        html = extension_header(self.project_name)+self.markdown(md) +extension_footer
        return self.compilehtml(html)
    def compilehtml(self,html):
        compiled = self.jinja.from_string(html)
        return compiled
        
