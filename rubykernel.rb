#coding:utf-8
require "kconv"
def printHello
	print("Hello\n")
end
stringarray=["山田","田中","藤原"]
#配列の中身を出力する
stringarray.each {|array|
#macでは¥は環境依存文字のため改行はできない\で改行する必要がある
print(Kconv.toutf8("氏名:"+array[0]+array[1]),"\n")
}
#kconv.toutf8で文字列をutf-8に変換する
print(Kconv.toutf8("メソッドを呼び出す"))
printHello

