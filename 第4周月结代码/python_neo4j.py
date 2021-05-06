# 导入包
from py2neo import Graph,Node,Relationship,RelationshipMatcher

# 链接到neo4j数据库
graph=Graph('http://localhost:7474',username='neo4j',password='xxxxxx')

# 创建节点（均可直接赋值变量）
a=Node('User',name='yaim') #第1个参数为节点类型，第2个参数为节点属性和值
b=Node('User',name='fyl')
# 创建关系
r=Relationship(a,'SAME',b)
# 将节点和关系加入到数据库
s=a|b|r
graph.create(s)

#查询节点
print(graph.nodes[0]) #根据节点id，返回节点
print(graph.nodes.get(0)) #同上
print(list(graph.nodes.match('User'))) #根据条件，返回节点列表
print(graph.nodes.match('User',name='yaim').first()) #根据条件，返回第1个节点
# 查询关系
rel_matcher=RelationshipMatcher(graph)
rel_all=list(rel_matcher.match()) #获取所有关系，返回列表
rel_this=list(rel_matcher.match(r_type='SAME')) #获取某一关系，返回列表

# 删除节点
node_del=graph.nodes.match('User',name='temp').first() #先查询到某一个节点
graph.delete(node_del) #再删除
# ***删除关系
rel_del=rel_matcher.match(r_type='SAME').first() #先查询到某一个关系
graph.delete(rel_del) #再删除，*连带删除节点？*

# 更新节点
node_update=graph.nodes.match('User',name='yaim').first() #先查询到某一个节点
node_update['name']='yaim_new' #更新该节点某一属性值
graph.push(node_update) #提交更新
# ***更新关系