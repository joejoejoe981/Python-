
from Lab10.element import Tag

p_tag = Tag(name = 'p',content='This is a paragraph',id = 'special',class_ = 'headline')
# print(p_tag)#自動呼叫p.tag.__str__
# print(p_tag.name)
# print(p_tag.content)
# print(p_tag.attrs['id'])
print(p_tag.id)
print(p_tag.class_)
# print(p_tag.content)

# link_tag = Tag(name='link',content='這裡是標題',id = 'special',class_= 'headline')
# print(link_tag)
# print(link_tag.content)
