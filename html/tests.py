# coding: utf-8

from style import Style
from tag import Tag

# style test
style = Style(color='red')

style['text-align'] = "center"
style['margin-left'] = "20px"

# tag test
tag = Tag(type='p', content='python is the best', style=style)

print style
print tag
print

# tag inside tag
li = [Tag(type='li', content='python is the best - %s' % i, style=style) for i in range(3)]
tag = Tag(type='ul', content=li, style=style)

print tag
print
print

# tag groups chain
tag = Tag(type='div', content=[], style=style)
tag['content'].append(Tag(type='p', content='hello!'))

print tag
print

# Adding Attribute
tag = Tag(type='div', content=Tag(type='a', attr={'href': 'goto1'}, content='i am p tag!'), style=style)
tag['attr']['class'] = 'main-div'
tag['attr']['id'] = '#main-div'
print tag
