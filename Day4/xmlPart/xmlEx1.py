from bs4 import BeautifulSoup

file = open('books.xml', encoding='utf-8')
book_xml = file.read()
file.close()

# pip install lxml로 해줘야한다. html.parser보다 성능이 약간 좋다
bsObj = BeautifulSoup(book_xml,'lxml')

for book_info in bsObj.findAll('author'):
    print(book_info.text)

# book_xml.find('author')
# print(book_xml)