import uiautomation as auto
import random
import os
from colorama import init, Fore, Style

# 初始化 colorama
init()

auto.uiautomation.SetGlobalSearchTimeout(1)

friendWindow = auto.WindowControl(searchDepth=1, Name="朋友圈", ClassName='SnsWnd')
friendWindow.SetActive()
item = friendWindow.ListItemControl(searchDepth=6, searchInterval=0.01)
comment_button = item.ButtonControl(Name="评论")
comment_pane = comment_button.GetParentControl().GetNextSiblingControl()
like_pane = comment_pane.GetFirstChildControl()

nicknames = []
for control, depth in auto.WalkControl(like_pane, maxDepth=4):
    if not control.Name or depth != 4 or not isinstance(control, auto.ButtonControl):
        continue
    nicknames.append(control.Name)

# 统计参与者总数
total_participants = len(nicknames)

# 使用 colorama 输出绿色字体
print(Fore.GREEN + "所有参与者名单：" + Style.RESET_ALL)
print(nicknames)
print(Fore.YELLOW + f"\n参与者总数：{total_participants}\n" + Style.RESET_ALL)

print(Fore.GREEN + "中奖者名单：\n" + Style.RESET_ALL)

def draw_prizes(participants, num_prizes, prize_name):  # 抽奖函数
    winners = random.sample(participants, k=num_prizes)  # 随机抽取指定数量的获奖者
    for winner in winners:  # 遍历获奖者
        participants.remove(winner)  # 从参与名单中移除获奖者（避免重复获奖）
    print(Fore.GREEN + f"{prize_name}: {winners}" + Style.RESET_ALL)  # 输出获奖者名单

draw_prizes(nicknames, 1, "特等奖")
draw_prizes(nicknames, 2, "一等奖")
draw_prizes(nicknames, 3, "二等奖")
draw_prizes(nicknames, 4, "三等奖")
draw_prizes(nicknames, 5, "幸运奖")
print("按下任意键继续......")
# 派大星V：hfcloud6
