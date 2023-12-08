# -*- encoding: utf-8 -*-
"""
@File    :   redis_sentinel.py
@Time    :   2023/12/08 19:09:21
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
"""

# here put the import lib
from redis.sentinel import Sentinel

# 连接哨兵服务器(主机名也可以用域名)
sentinel = Sentinel(
    sentinels=[("1.1.1.1", 26379), ("1.1.1.1", 26380), ("1.1.1.1", 26381)],
    password="YOURASSWORD",
    sentinel_kwargs={"password": "YOURASSWORD"}
)
print(sentinel.discover_master("mymaster"))

master = sentinel.discover_master("mymaster")

print(master)


slave = sentinel.discover_slaves("mymaster")
print(slave)

master = sentinel.master_for(service_name="mymaster",  password="YOURASSWORD",socket_timeout=0.5)

master.set("foo", "bar")

r_get = master.get('foo')
