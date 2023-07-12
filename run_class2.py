from XAJ_class_LIU_2 import XajModelLiu

P = [10, 30, 50, 70, 4, 6, 1, 5, 2, 3, 2, 8, 6, 4, 0]  # 逐小时面雨量过程
EM = [2, 3, 5, 8, 1, 2, 3, 1, 4, 1, 2, 1, 3, 2, 2]  # 逐小时水面蒸发过程

xaj=XajModelLiu(P, EM, KC=0.9, C=0.15, B=0.3, SM=40, WU=0, WL=33, WD=30, WUM=40, WLM=66, WDM=24, EX=1.4, KI=0.3, KG=0.4, F=2000, t=1, CI=0.8, CG=0.9, CR=0.5, L=2)

xaj.simulate()
xaj.result_show()