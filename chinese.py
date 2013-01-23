#!/usr/bin/python2.7
# -*- coding: utf-8 -*-  

import re
s="123中文xxx"
print s
s1 = unicode(s, "utf-8")
m =re.sub(ur"[\u4e00-\u9fa5]",'',s1)
print m
