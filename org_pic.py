# -*- coding: utf-8 -*- 
import pinyin
converter = pinyin.CConvert()

# print "我的".decode("UTF-8")
print converter.convert(unicode("阿虎是个一笔男", "utf-8"))