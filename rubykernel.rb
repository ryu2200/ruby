#coding:utf-8
#ruby -Ku
require "kconv"

def printHello
	print("Hello¥n")
end
#kconv.toutf8で文字列をutf-8に変換する
print(Kconv.toutf8("メソッドを呼び出す"))
printHello
print 

