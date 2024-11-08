from lxml import etree

xml = """
<book>
    <name>野花遍地香</name>
    <author>
        <nick id="1">周杰伦</nick>
        <nick id="2">林俊杰</nick>
        <nick id="3">郭麒麟</nick>
        <div>
            <nick>热热热热1</nick>
        </div>
        <span>
            <nick>热热热热2</nick>
        </span>
        <span>
            <nick>热热热热3</nick>
        </span>                
    </author>
</book>
"""

tree = etree.XML(xml)
result = tree.xpath('//book') # /表示层级关系，第一个/是根节点
result1 = tree.xpath('/book/name/text()')
print(result)
print(result1)

result2 = tree.xpath('/book/author/nick/text()')
print(result2)

result3 = tree.xpath('/book/author//nick/text()') # //找到父节点中所有有nick的节点
print(result3)

result4 = tree.xpath('/book/author/*/nick/text()') # * 任意的节点，表示通配符
print(result4)

ol_li_list = tree.xpath('/book/author')

for li in ol_li_list:
    result = li.xpath('./nick/text()') # ./表示相对路径，在author中进行查找
    result1 = li.xpath('./nick/@id') # @属性 ：拿到属性值
    print(result1)
