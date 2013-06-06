# coding: utf-8

from tag import Tag
from style import Style

# style test
style = Style(color='red')

style['text-align'] = "center"
style['margin-left'] = "20px"

# tag test
tag = Tag(type='p', content='python is the best', style=style)

print style
print tag

# tag inside tag
li = [Tag(type='li', content='python is the best - %s'%i, style=style) for i in range(10)]

tag = Tag(type='ul', content=li, style=style)

print tag