from gurobipy import*
import numpy as np

#####################



#####################
# 建構Model https://www.gurobi.com/documentation/9.5/refman/py_model2.html 
m = Model()  # Model ( name="", env=defaultEnv )

# 以 addVar() 加入變數 https://www.gurobi.com/documentation/9.5/refman/py_model_addvar.html 



#設定變數
#b = 0.0：变量的下界，默认为 0
#ub = GRB.INFINITY：变量的上界，默认为无穷大
#vtype = GRB.CONTINUOUS ：变量的类型，默认为连续型，可改为 GRB.BINARY 0-1变量，GRB.INTEGER 整型
#name = ""：变量名，默认为空
w = m.addVars(3, name='acres to use for each crop')
x = m.addVars(3, 2, name='crops to purchase')
y = m.addVars(3, 4, name='crops to sell')

#更新環境中的變量
m.update()

#設定參數
yield_per_acre = []
for j in [1.2,1,0.8]:
    yield_per_acre.append([i*j for i in [2.5, 3, 20]])
cattle_feed = [200,240]
plant_cost = [150, 230, 260]
sell_price = [170,150,36,10]
purchase_price = [238,210]

name = ["Wheat", "Corn", "Sugar beet", "Wheat","Corn","Wheat", "Corn", "Sugar beet below degree", "Sugar beet upper degree"]
para = yield_per_acre + purchase_price + sell_price
# m.setObjective()設置目標函數
# 最小化損失金額 min(loss) = min(cost - profit) = min(cost_to_plant_crop + cost_to_purchase_crop - profit_to_sell_crop
print('========\n',w,'\n==========')
cost_to_plant_crop = w.prod(plant_cost)

cost_to_purchase_crop = 0 
profit_to_sell_crop = 0
for i in range(3):
    for j in range(2):
        cost_to_purchase_crop += x[i,j] * purchase_price[j] /3
    for j in range(4):
        profit_to_sell_crop += y[i,j] * sell_price[j] /3
loss = cost_to_plant_crop + cost_to_purchase_crop - profit_to_sell_crop
m.setObjective(loss, GRB.MINIMIZE)

# m.addConstr()加入限制式

# constraint_1: only 500 acres of land
m.addConstr(sum(w[i] for i in range(3)) <= 500,"constraint_1")

# constraint_2: need 200t of wheat for cattle feed
for i in range(3):
    cattle_wheet = yield_per_acre[i][0] * w[0] + x[i,0] - y[i,0] 
    m.addConstr(cattle_wheet == cattle_feed[0], "constraint_2_{}".format(i))

# constraint_3: need 240t of corn for cattle feed
for i in range(3):
    cattle_corn = yield_per_acre[i][1] * w[1] + x[i,1] - y[i,1]
    m.addConstr(cattle_corn == cattle_feed[1], "constraint_3_{}".format(i))

# constraint_4: Sugar beet sell price
for i in range(3):
    m.addConstr((yield_per_acre[i][2] * w[2]) - y[i,2] - y[i,3] == 0, "constraint_4_1_{}".format(i))
    m.addConstr(y[i,2] <= 6000, "constraint_4_2_{}".format(i))
m.addConstr(w[0] == 320, "constraint__{}".format(0))
m.addConstr(w[1] == 80, "constraint_2_{}".format(1))
m.addConstr(w[2] == 100, "constraint_2_{}".format(2))
m.optimize() # m.optimize()求解





# 透過屬性varName、x顯示決策變數名字及值

for n,v in enumerate(m.getVars()):
    print('%s = %g' % (v.varName, v.x))
# 透過屬性objVal顯示最佳解
print('Obj : %g' % m.objVal)
print('Profit : %g' % -m.objVal)


