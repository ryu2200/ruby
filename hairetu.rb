#coding:utf-8
#配列を宣言する
array=[3,2,1]
#配列要素を取得する
array[3]=array[2]-1
#eachにはイテレーター,ブロックにはeltという変数が与えられる
array.each do |elt|
#,#{}セパレータに囲まれた式の値は文字列に変換される
	print "#{elt+1}\n"
end
