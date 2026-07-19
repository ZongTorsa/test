 
import re

def outer (accountmoney):
    def cash (num,x):
        nonlocal accountmoney # 非本地变量
        if x == 1:
            accountmoney += num
            print(f"账户余额已完成存款{num}元\n账户余额为{accountmoney}元")
        elif x == 2:
            if accountmoney - num > 0:
                accountmoney -= num
                print(f"账户余额已完成取款{num}元\n账户余额为{accountmoney}元")
            else:
                print("取款失败\n账户余额不足,请重新输入")
        elif x == 3:
            print(f"账户余额为{accountmoney}元")
        else:
            print("输入错误")
    return cash

atm = outer(1000)


while True:
    try:
        print("0. 退出")
        print("1. 存款")
        print("2. 取款")
        print("3. 查询余额")
        choice = int(input("请输入您的选择："))
        if choice == 0:
            print("欢迎下次光临")
            break
    
        if choice == 1:
            num = int(input("请输入存款金额："))
            atm(num,1)

        elif choice == 2:
            num = int(input("请输入取款金额："))
            
            
            atm(num,2)
        elif choice == 3:
            atm(0,3)
    except Exception as e:
        print("输入错误\n请重新输入")
        print(e)
        continue





                  