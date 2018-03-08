# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

print('欢迎来到恋爱大冒险')
input()
print('请按回车键来进行游戏')
input()
print('经过三年的高中学习，我终于和同年级的暗恋的女生考上了同一所大学')
input()
print('开学第一天，我在食堂遇到她了，我应该')
input()
print('1.直接上去要微信\t2.以老乡的名义上去聊天\t3.继续吃饭')
option1=int(input('请做出选择：按数字1-3，然后回车\n'))
if option1==1:
    print('太仓促了，机会还不成熟')
    input()
    print('对不起，你失败了。GAME OVER')
elif option1==2:
    print('似乎认识了，而且加了微信好友')
    input()
    print('下午上完课回到寝室，心情激动，发条什么微信呢？')
    input()
    print('1.你加了什么社团\t2.晚饭准备吃啥？\t3.周末有空吗？')
    option2=int(input('请做出选择：按数字1-3，然后回车\n'))
    if option2==1:
        print('我知道她在哪个社团了，我也挺有兴趣，可以一同加入')
    elif option2==2:
        print('太庸俗了，这是尬聊')
        input()
        print('对不起，你失败了。GAME OVER')
    elif option2==3:
        print('还不熟，乱约什么') 
        input()
        print('对不起，你失败了。GAME OVER')
elif option1==3:
    print('太怂了，注定单身')
    input()
    print('对不起，你失败了。GAME OVER')
