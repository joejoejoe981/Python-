from Lab10.Html_parser import Htmlparser

html_doc = '<html><head><title>我是標題</title></head></html>'
tag = Htmlparser.string_to_tag(html_doc)
print('name',tag)