import requests
from bs4 import BeautifulSoup

# import mysql.connector

# from py2neo import Graph,Node,Relationship

# 链接mysql数据库
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="xxxxxx",
#     database="four_python_crawler"
# )
# mysql游标
# mycursor=mydb.cursor()

# 链接neo4j数据库
# graph=Graph("http://localhost:7474",username="neo4j",password="xxxxxx")

#链接到药品网站的药品列表页面
url="https://www.360kad.com/Spzt/www_yjjc.shtml?pageType=1"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

#获取到该药品列表页面的每个药品html标签
tag_main_div=soup.find(class_='YproList2 clearfix')
tag_div_ul=tag_main_div.find('ul')
tag_ul_lis=tag_div_ul.find_all('li')

#开始循环爬取每个药品信息
intro_href_before="https://www.360kad.com/product/"
for li in tag_ul_lis:
    # 爬取当前药品的名称
    name=li.find(class_='Yname').find('a')['title']
    # print(name,end=' / ')
    # 爬取当前药品的价格
    price = li.find(class_='Ypribox').find(class_='RMB').text
    # print(price,end=' / ')
    price_db=float(price[1:])
    # print(price_db,end=' / ')
    # 链接到当前药品的详情界面
    href = intro_href_before + li.find('input')['value'] + ".shtml"
    li_res = requests.get(href)
    li_soup = BeautifulSoup(li_res.text, 'html.parser')
    # 爬取详情界面中的药品说明信息
    tag_intro_ul=li_soup.find('ul',class_='instructions-ul')
    intro=tag_intro_ul.text.replace(" ","")
    #爬取当前药品的成份
    comp_poss_words=["【成份】","【成分】"]
    comp_begin=-1
    for comp_word in comp_poss_words:
        comp_begin=intro.find(comp_word)
        if comp_begin!=-1:
            comp_begin+=len(comp_word)
            break
    comp_str=""
    if comp_begin!=-1:
        comp_end=intro.find("【性状】")
        comp_str=intro[comp_begin:comp_end].replace('\n','')
    # print(comp_str, end=' / ')
    #爬取当前药品的功能
    func_poss_words=["【适应症】","【功能主治】","【功效主治】"]
    func_begin=-1
    for func_word in func_poss_words:
        func_begin=intro.find(func_word)
        if func_begin!=-1:
            func_begin+=len(func_word)
            break
    func_str=""
    if func_begin!=-1:
        func_end = intro.find("【规格】")
        func_str=intro[func_begin:func_end].replace('\n','')
    # print(func_str,end=' / ')
    #爬取当前药品的生产者
    manu_poss_words=["【生产企业】","【生产厂家】"]
    manu_begin = -1
    cur_manu_word=""
    for manu_word in manu_poss_words:
        manu_begin = intro.find(manu_word)
        if manu_begin != -1:
            manu_begin += len(manu_word)
            cur_manu_word=manu_word
            break
    manu_str = ""
    if manu_begin != -1:
        manu_str = intro[manu_begin:].replace('\n', '')
        # 处理信息重复出现的意外情况
        unexp_begin=manu_str.find(cur_manu_word)
        if unexp_begin!=-1:
            manu_str=manu_str[unexp_begin+len(cur_manu_word):]
    # print(manu_str, end=' / ')
    #换行
    # print("")

    # 向mysql数据库中增数据
    # mycursor.execute("INSERT INTO 360kad VALUES('%s','%f','%s','%s','%s')" % (name,price_db,comp_str,func_str,manu_str))
    # mydb.commit()

    # 创建药品节点，属性为（name，price，component，function）
    # m=Node('Medicine',name=name,price=price_db,component=comp_str,function=func_str)
    # 创建企业节点
    # e=Node('Enterprise',name=manu_str)
    # 创建药品节点与企业节点的关系：生产
    # r=Relationship(e,'生产',m)
    # 向neo4j数据库插入数据
    # s=m|e|r
    # graph.create(s)

# 关闭游标、数据库
# mycursor.close()
# mydb.close()

