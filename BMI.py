print("BMI指数计算器\n")
inp_1 = input('请输入您的体重(kg):\n')
inp_2 = input('请输入您的身高(cm):\n')
try:
    weight = float(inp_1)
except:
    print('Please enter a number')
try:
    height = float(inp_2)
except:
    print('Please enter a number')
BMI = weight/(height/100)**2
if BMI<18.5:
	print("您的体型偏瘦")
elif BMI<24 and BMI>=18.5:
	print("您的体型正常")
elif BMI<28 and BMI>=24:
	print("您的体型偏胖")
elif BMI<32 and BMI>=28:
	print("您的体型肥胖")
elif BMI>=32:
	print("您的体型过于肥胖")