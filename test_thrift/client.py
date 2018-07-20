# -*- coding: utf-8 -*-
import thriftpy

from thriftpy.rpc import make_client

pingpong_thrift = thriftpy.load("test_thrift/proto/pingpong.thrift", module_name="pingpong_thrift")
client = make_client(pingpong_thrift.PingService, '127.0.0.1', 8000)
print(client.ping())
