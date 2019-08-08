# coding:utf-8
import urllib
import re

def get_html(url):
    page = urllib.urlopen(url)
    html_code = page.read()
    return html_code

def get_image(html_code):
    reg = r'img src="(http.+?\.jpg)"'
    reg_img = re.compile(reg)
    img_list = reg_img.findall(html_code)
    print img_list
    x = 0
    for img in img_list:
    	try:
            urllib.urlretrieve(img, '%s.jpg' % x)
            x += 1
        except IOError as err:
            print("IO error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
    print x
print u'-------网页图片抓取-------'
print u'请输入url:',
url = raw_input()
if url:
    pass
else:
    print u'---没有地址输入正在使用默认地址---'
    url = 'https://tieba.baidu.com/index.html'
print u'----------正在获取网页---------'
html_code = get_html(url)
print u'----------正在下载图片---------'
get_image(html_code)
print u'-----------下载成功-----------'
raw_input('Press Enter to exit')