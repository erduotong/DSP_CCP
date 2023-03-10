import time
import json
import os
encoding = 'utf-8'


def out(x):
    a = x['header']['shortDesc']
    h = "./output/" + a + '.json'
    with open(h, 'w+', encoding="utf-8") as f:
        x = json.dumps(x, ensure_ascii=False)  # 直接进行输出
        f.write(x)


def read_input():
    # 进行文件的格式读写
    datanames = os.listdir(os.path.dirname(os.path.abspath(__file__)))
    for i in datanames:
        af = os.path.splitext(i)
        if af[0] == 'input':
            ad = af[1]
    bl1 = []
    bl2 = []
    error_lines = []
    with open('input' + ad, 'r', encoding='utf-8-sig') as f:
        i: int
        for i, line in enumerate(f):
            try:
                data = line.strip().split(',')
                bl1.append(data[0])
                bl2.append(data[1])
            except:
                error_lines.append(i + 1)
    return bl1, bl2


def output(building_ID, input_):  # 创建生成函数,传入建筑编号(0小塔1大塔2大矿机),以及耗电(占用百分比)输入,基于耗电计算的大矿机单独调用另一个函数
    building_ID = str(building_ID)
    input_ = str(input_)
    if input_.replace('.', '', 1).isdigit():
        input_ = float(input_)
        if building_ID.isdigit():
            building_ID = int(building_ID)
        else:
            return "0y"  # 输入格式error
    else:
        return "0y"  # 输入格式error
    if building_ID == 0 or building_ID == 1:  # 小塔大塔集中处理 #传入为mW
        input_ = input_ / 100
        if building_ID == 1:  # 大塔处理
            json_str = '{"header":{"layout":10,"icons":[0,0,0,0,0],"time":"2023-03-05T11:32:52.660Z","gameVersion":"0.9.27.15466","shortDesc":"新蓝图","desc":""},"version":1,"cursorOffset":{"x":0,"y":0},"cursorTargetArea":0,"dragBoxSize":{"x":1,"y":1},"primaryAreaIdx":0,"areas":[{"index":0,"parentIndex":-1,"tropicAnchor":0,"areaSegments":200,"anchorLocalOffset":{"x":0,"y":0},"size":{"x":1,"y":1}}],"buildings":[{"index":0,"areaIndex":0,"localOffset":[{"x":-0.000009486373528488912,"y":0,"z":-0.000013735146239923779},{"x":-0.000009486373528488912,"y":0,"z":-0.000013735146239923779}],"yaw":[0,0],"itemId":2104,"modelIndex":50,"outputObjIdx":-1,"inputObjIdx":-1,"outputToSlot":0,"inputFromSlot":0,"outputFromSlot":0,"inputToSlot":0,"outputOffset":0,"inputOffset":0,"recipeId":0,"filterId":0,"parameters":{"storage":[{"itemId":0,"localRole":0,"remoteRole":0,"max":0},{"itemId":0,"localRole":0,"remoteRole":0,"max":0},{"itemId":0,"localRole":0,"remoteRole":0,"max":0},{"itemId":0,"localRole":0,"remoteRole":0,"max":0},{"itemId":0,"localRole":0,"remoteRole":0,"max":0}],"slots":[{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0}],"workEnergyPerTick":500000,"tripRangeOfDrones":-1,"tripRangeOfShips":24000000000,"includeOrbitCollector":true,"warpEnableDistance":20000,"warperNecessary":true,"deliveryAmountOfDrones":10,"deliveryAmountOfShips":100,"pilerCount":0,"autoFill_10":1,"autoFill_11":1}}]}'
            data = json.loads(json_str)
            cp = input_ * 5 / 3 + 1  # 转换成蓝图内的格式
            c = input_ / 10000
            if c >= 1000:
                c = c / 1000
                a = str(c) + "G星际物流塔 代码生成"
            else:
                a = str(c) + "MW星际物流塔 代码生成"

            data['header']['shortDesc'] = a
            data['header']['desc'] = a + "by耳朵同"
            data['buildings'][0]['parameters']['workEnergyPerTick'] = cp  # 更改蓝图
            return_ = data
            return return_  # 输出
        elif building_ID == 0:  # 小塔处理
            json_str = '{"header":{"layout":10,"icons":[0,0,0,0,0],"time":"2023-03-05T13:17:15.846Z","gameVersion":"0.9.27.15466","shortDesc":"新蓝图","desc":""},"version":1,"cursorOffset":{"x":0,"y":0},"cursorTargetArea":0,"dragBoxSize":{"x":1,"y":1},"primaryAreaIdx":0,"areas":[{"index":0,"parentIndex":-1,"tropicAnchor":0,"areaSegments":200,"anchorLocalOffset":{"x":0,"y":0},"size":{"x":1,"y":1}}],"buildings":[{"index":0,"areaIndex":0,"localOffset":[{"x":0,"y":0,"z":-0.000013735146239923779},{"x":0,"y":0,"z":-0.000013735146239923779}],"yaw":[0,0],"itemId":2103,"modelIndex":49,"outputObjIdx":-1,"inputObjIdx":-1,"outputToSlot":0,"inputFromSlot":0,"outputFromSlot":0,"inputToSlot":0,"outputOffset":0,"inputOffset":0,"recipeId":0,"filterId":0,"parameters":{"storage":[{"itemId":0,"localRole":0,"remoteRole":0,"max":0},{"itemId":0,"localRole":0,"remoteRole":0,"max":0},{"itemId":0,"localRole":0,"remoteRole":0,"max":0},{"itemId":0,"localRole":0,"remoteRole":0,"max":0}],"slots":[{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0}],"workEnergyPerTick":100000,"tripRangeOfDrones":-1,"tripRangeOfShips":24000000000,"includeOrbitCollector":true,"warpEnableDistance":480000,"warperNecessary":true,"deliveryAmountOfDrones":10,"deliveryAmountOfShips":100,"pilerCount":0,"autoFill_10":1}}]}'
            data = json.loads(json_str)
            cp = input_ * 5 / 3 + 1  # 转换成蓝图内的格式
            c = input_ / 10000
            if c >= 1000:
                c = c / 1000

                a = str(c) + "G行星内物流塔 代码生成"
            else:
                a = str(c) + "MW行星内物流塔 代码生成"
            data['header']['shortDesc'] = a
            data['header']['desc'] = a + "by耳朵同"
            data['buildings'][0]['parameters']['workEnergyPerTick'] = cp  # 更改蓝图
            return_ = data
            return return_  # 输出
    elif building_ID == 2:  # 大矿机 输入无百分号 #外部切分好后再进行输入
        json_str = '{"header":{"layout":10,"icons":[0,0,0,0,0],"time":"2023-03-05T10:36:23.104Z","gameVersion":"0.9.27.15466","shortDesc":"新蓝图","desc":""},"version":1,"cursorOffset":{"x":0,"y":0},"cursorTargetArea":0,"dragBoxSize":{"x":1,"y":1},"primaryAreaIdx":0,"areas":[{"index":0,"parentIndex":-1,"tropicAnchor":0,"areaSegments":200,"anchorLocalOffset":{"x":0,"y":0},"size":{"x":1,"y":1}}],"buildings":[{"index":0,"areaIndex":0,"localOffset":[{"x":0,"y":0,"z":-0.0000022910537609277526},{"x":0,"y":0,"z":-0.0000022910537609277526}],"yaw":[0,0],"itemId":2316,"modelIndex":256,"outputObjIdx":-1,"inputObjIdx":-1,"outputToSlot":0,"inputFromSlot":0,"outputFromSlot":0,"inputToSlot":0,"outputOffset":0,"inputOffset":0,"recipeId":0,"filterId":0,"parameters":{"storage":[{"itemId":1001,"localRole":1,"remoteRole":0,"max":10000}],"slots":[{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0},{"dir":0,"storageIdx":0}],"workEnergyPerTick":49000,"tripRangeOfDrones":-1,"tripRangeOfShips":24000000000,"includeOrbitCollector":true,"warpEnableDistance":480000,"warperNecessary":true,"deliveryAmountOfDrones":10,"deliveryAmountOfShips":100,"pilerCount":0,"miningSpeed":10000}}]}'
        data = json.loads(json_str)  # js字符串转字典
        data['buildings'][0]['parameters']['miningSpeed'] = input_  # 对其中蓝图名称和速度进行编辑
        BP_name = (str(input_) + "%大矿机")
        data['header']['shortDesc'] = BP_name  # 蓝图名
        BP_word = (str(input_) + "%大矿机 由代码自动生成 by耳朵同")
        data['header']['desc'] = BP_word  # 蓝图简介
        return_ = data
        return return_  # 输出


def conversion_power_unit(x):  # 将用户输入的充电功率转换成以mW为单位的字符串
    # 定义合法的单位
    units = ['mW', 'kW', 'MW', 'G']
    # 去掉字符串中的空格
    x = x.replace(' ', '')
    # 切割字符串
    for unit in units:
        if x.endswith(unit):
            value_str = x[:-len(unit)]
            break
    else:
        return "输入错误"
    # 检查切割后的字符串是否为浮点数
    try:
        value = float(value_str)
    except ValueError:
        return "输入错误"
    # 返回结果 #value=切割后的功率 unit=单位
    if unit == "mW":
        return value
    elif unit == "kW":
        return value * 1000
    elif unit == "MW":
        return value * 1000000
    elif unit == "G":
        return value * 1000000000
    else:
        return "输入错误"


def remove_percent(x):  # 百分号切割函数
    # 去掉字符串中的空格和百分号
    x = x.replace(' ', '')
    if "%" not in x:
        return "输入错误"
    x = x.replace('%', '')
    # 判断字符串是否为数字
    if x.replace(".", '', 1).isdigit():  # 去掉第一个小数点
        return float(x)  # 输出为float类型
    else:
        return "输入错误"


def building_0():  # 小塔的处理函数
    print("请输入充电功率,输入格式: 数值+单位 如60MW 100mW 900kW")
    print("可使用单位:mW kW MW G")
    a = input("请输入充电功率>>>")
    a = conversion_power_unit(a)
    return output("0", a)


def building_1():  # 大塔的处理函数
    print("请输入充电功率,输入格式: 数值+单位 如60MW 100mW 900kW")
    print("可使用单位:mW kW MW G")
    a = input("请输入充电功率>>>")
    a = conversion_power_unit(a)
    return output("1", a)


def building_2():  # 大矿机的处理
    print("请输入速度百分比 默认矿机速度为100% 输入实例:114514%")
    a = input("请输入速度百分比>>>")
    a = remove_percent(a)
    if a == "输入错误":
        return "输入错误"
    a = output("2", a)
    return a


DSP_CCP = '''
 ______   _______  _______  _______  _______  _______ 
(  __  \ (  ____ \(  ____ )(  ____ \(  ____ \(  ____ )
| (  \  )| (    \/| (    )|| (    \/| (    \/| (    )|
| |   ) || (_____ | (____)|| |      | |      | (____)|
| |   | |(_____  )|  _____)| |      | |      |  _____)
| |   ) |      ) || (      | |      | |      | (      
| (__/  )/\____) || )      | (____/\| (____/\| )      
(______/ \_______)|/_____  (_______/(_______/|/       
                   (_____)                            
                                                    
'''
BYE = r'''  
______            _______ 
(  ___ \ |\     /|(  ____ \
| (   ) )( \   / )| (    \/
| (__/ /  \ (_) / | (__    
|  __ (    \   /  |  __)   
| (  \ \    ) (   | (      
| )___) )   | |   | (____/\
|/ \___/    \_/   (_______/
'''
# main
can_use_building = ["小塔", "大塔", "大矿机"]  # 可以使用的建筑，方便后期修改
can_use_building_number = ["数字+单位(可用mW kW MW G),如100G", "数字+单位(可用mW kW MW G),如100G","需要的速度+百分号,如114%"]
print(DSP_CCP)
print("欢迎使用DSP仙术物流塔/矿机生成工具")
a = ''
while True:
    if a == 'quit':
        break
    print("\n\n蓝图文件输出将位于该程序目录下的output文件夹，如果不存在将自动生成")
    if not os.path.exists('output'):  # 创建输出文件夹
        os.makedirs('output')
    print("请选择输入模式")
    print("1:直接输入\n2:通过txt文件输入(逗号分割)\nquit:退出\nM:显示制作人和感谢名单")
    a = input("请输入编号>>>")
    if a == "1":  # 直接输入模式
        print("已进入直接输入模式")
        print("请选择你的建筑编号")
        for i in range(len(can_use_building)):  # 输出编号
            print(str(i + 1) + ":" + can_use_building[i])
        a = input("请输入对应编号>>>")
        if a.isdigit():  # 对输入进行判断
            a = int(a)
            if a < 1 or a > (len(can_use_building)):
                print("输入编号错误\n\n")
            else:
                run = 'building_' + str(a - 1) + "()"
                a = eval(run)  # 进行调用函数
                if a == '输入错误' or a == '0y':
                    print("输入错误")
                    continue
                out(a)
                print("已完成!")
                print("请自行使用晨隐的蓝图变换工具转换成可导入游戏内的蓝图")
                time.sleep(1)

        else:
            print("输入编号错误\n\n")
        if a == "0y":
            print("输入错误")
        else:  # 输出蓝图
            pass
    elif a == "2":  # txt输入模式
        print("输入格式:每一行一个建筑 a,b")
        print("支持csv,txt等最终能被读取成下面格式的文件(csv只能使用前两列")
        print("其中a代表建筑编号,b代表你需要填的对应参数 下面是对照表")
        for i in range(len(can_use_building)):  # 输出编号
            print(str(i + 1) + ":" + can_use_building[i], end='')
            print(" 实例:" + can_use_building_number[i])
        print("quit 退出程序 实例:quit,quit")
        input("当准备好后，按下回车")
        bl1, bl2 = read_input()
        if len(bl1) != len(bl2):
            print("输入错误!两个变量不等长")
        else:  # 输入部分
            for i in range(len(bl1)):
                bl1nw = bl1[i]
                bl2nw = bl2[i]  # 按找顺序对两个列表中的参数进行读取
                if bl1nw == 'quit':
                    a = bl1nw
                    break

                if bl1nw.isdigit():  # 对bl1bn输入进行判断,是否过大
                    hl = int(bl1nw)
                    bl1n = bl1nw
                    if hl < 1 or hl > (len(can_use_building)):
                        print("输入编号错误,位于输入的第" + str(i + 1) + "行")
                    else:  # 输入编号判断成功

                        if bl1n == '1':  # 小塔

                            bl1n = conversion_power_unit(bl2nw)
                            if bl1n == "输入错误":
                                print("输入编号错误,位于输入的第" + str(i + 1) + "行")
                            else:
                                bl1n = output("0", bl1n)
                                if bl1n == '输入错误' or bl1n == '0y':
                                    print("输入编号错误,位于输入的第" + str(i + 1) + "行")
                                else:
                                    out(bl1n)
                        elif bl1n == '2':  # 大塔
                            bl1n = conversion_power_unit(bl2nw)
                            if bl1n == "输入错误":
                                print("输入编号错误,位于输入的第" + str(i + 1) + "行")
                            else:
                                bl1n = output("1", bl1n)
                                if bl1n == '输入错误' or bl1n == '0y':
                                    print("输入编号错误,位于输入的第" + str(i + 1) + "行")
                                else:
                                    out(bl1n)
                        elif bl1n == '3':  # 大矿机
                            bl1n = remove_percent(bl2nw)
                            if bl1n == "输入错误":
                                print("输入编号错误,位于输入的第" + str(i + 1) + "行")
                            else:
                                bl1n = output("2", bl1n)
                                if bl1n == '输入错误' or bl1n == '0y':
                                    print("输入编号错误,位于输入的第" + str(i + 1) + "行")
                                else:
                                    out(bl1n)
                else:
                    print("输入编号错误,位于输入的第" + str(i + 1) + "行")
        print("已完成!请前往output查看输出文件")
        print("请自行使用晨隐的蓝图变换工具转换成可导入游戏内的蓝图")
        time.sleep(1)

    elif a == "quit":  # 退出
        break
    elif a == "M":  # 制作/感谢
        print("制作:耳朵同")
        print("感谢shenjack提供的部分指导")
        print("也同时感谢162065696戴森球计划蓝图仓库群内的包括但不限于莳槡等人的帮助")
        input("按任意键继续")
    else:
        print("输入错误,请输入正确的编号!")
        time.sleep(0.1)
        print("\n\n\n")

print("已退出程序,即将在1秒后关闭窗口")
print(BYE)
time.sleep(1)
