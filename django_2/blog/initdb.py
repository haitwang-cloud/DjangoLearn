#! /usr/bin/env python
from __future__ import unicode_literals
import random
from  django_2.wsgi import *
from blog.models import Author,Article,Tag

author_name_list=['lky','wht','shu','ces','ytu']
article_title_list=['Django教程','python教程','html教程']

def create_authors():
    for author_name in author_name_list:
        author , created=Author.objects.get_or_create(name=author_name)
        #随机生成qq
        author.qq=''.join(str(random.choice(range(10)) for _ in range(9)))
        author.addr='addr_%s' %(random.randrange(1,3))
        author.email='%s@wht.com' % (author.addr)
        author.save()

def create_articles_and_tags():
    #随机生成文章
    for article_title in article_title_list:
        #从不敢文章标题中得到tag
        tag_name=article_title.split(' ',1)[0]
        tag, created=Tag.objects.get_or_create(name=tag_name)

        random_author=random.choice(Author.objects.all())

        for i in range(1,21):
            title='%s_%s'%(article_title,i)
            article,created=Article.objects.get_or_create(
                title=title,defaults={
                    'author':random_author,#随机分配作者
                    'content':'%s 正文' %title,
                    'score':rnadom.randrange(70,101)#随机给文章一个打分
                }
            )
            article.tags.add(tag)
def main():
    create_authors()
    create_articles_and_tags()

if __name__=='__main__':
    main()
    print("OK")

