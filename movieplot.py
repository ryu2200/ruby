#coding:utf-8
import sys #モジュール属性を取得するため
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#読み込んだ値を格納する配列
x=[0]*3
y=[0]*3
z=[0]*3
#コマンドラインから引数を読み込む
argvs=sys.argv
argc=len(argvs)
#デバッグプリント
print u"引数は%sです"%argvs
print u"個数は%sです"%argc
if(argc!=2):
	print "Usage:invalid"
	quit()
#argvs[0]はpyファイル"qqq
f=open(argvs[1])
i=0
line=f.readline()
while line:
	x[i]=int(line[0])
	y[i]=int(line[2])
	#次の行を読み込む
	line=f.readline()
	i+=1
f.close
#読み込んだ値を元にアニメーションを描画する
fig=plt.figure()
# データを作成
data= []
for i in range(3):
    im = plt.scatter(x[i], y[i])
    data.append([im])
# 動画保存の準備
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# アニメーション作成
#intervalでplot間隔を調整
ani = animation.ArtistAnimation(fig, data, interval=10000, repeat_delay=1000)
#動画として保存
ani.save('im.mp4', writer=writer)
# 表示
plt.show()
