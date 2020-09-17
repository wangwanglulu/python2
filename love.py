# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

print('欢迎来到相亲大作战')
input()
print('请按回车键来进行游戏')
input()
print('今年28岁生日，父母说我的个人问题也要提上日程了，给我介绍了同事家的女儿见面。')
input()
print('加了微信，偶尔聊了一下感觉不错，决定约个饭，第一次见面应该去哪呢？')
input()
print('1.火锅店\t2.咖啡馆\t3.夜店')
option1=int(input('请做出选择：按数字1-3，然后回车\n'))
if option1==1:
    print('火锅店吵死了，没法聊天，不欢而散')
    input()
    print('对不起，你失败了。GAME OVER')
elif option1==2:
    print('安静的环境，比较适合沟通')
    input()
    print('吃完饭，对方看到账单，价格挺高的，提出想AA，我应该说')
    input()
    print('1. 这次我付下次你付 \t2. 同意AA \t3. 我吃得很少，应该对方买单')
    option2=int(input('请做出选择：按数字1-3，然后回车\n'))
    if option2==1:
        print('嗯，这样就有下次了')
    elif option2==2:
        print('亲兄弟明算账，算得很精呀')
        input()
        print('对不起，你失败了。GAME OVER')
    elif option2==3:
        print('你注定单身...') 
        input()
        print('对不起，你失败了。GAME OVER')
    else:
        print('输入错误，请重头来过')
        pass
elif option1==3:
    print('对方直接拒绝了...')
    input()
    print('对不起，你失败了。GAME OVER')
else:
    print('输入错误，请重头来过')
    pass
