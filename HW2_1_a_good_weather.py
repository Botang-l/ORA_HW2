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
x = m.addVars(2, name='crops to purchase')
y = m.addVars(4, name='crops to sell')

#更新環境中的變量
m.update()

#設定參數
yield_per_acre = [i*1.2 for i in [2.5, 3, 20]] 
cattle_feed = [200,240]
plant_cost = [150, 230, 260]
sell_price = [170,150,36,10]
purchase_price = [238,210]
print(yield_per_acre)
name = ["Wheat", "Corn", "Sugar beet", "Wheat","Corn","Wheat", "Corn", "Sugar beet below degree", "Sugar beet upper degree"]
para = yield_per_acre + purchase_price + sell_price
# m.setObjective()設置目標函數
# 最小化損失金額 min(loss) = min(cost - profit) = min(cost_to_plant_crop + cost_to_purchase_crop - profit_to_sell_crop
cost_to_plant_crop = w.prod(plant_cost)
cost_to_purchase_crop = x.prod(purchase_price)
profit_to_sell_crop = y.prod(sell_price)
loss = cost_to_plant_crop + cost_to_purchase_crop - profit_to_sell_crop
m.setObjective(loss, GRB.MINIMIZE)

# m.addConstr()加入限制式

# constraint_1: only 500 acres of land
m.addConstr(sum(w[i] for i in range(3)) <= 500,"constraint_1")

# constraint_2: need 200t of wheat for cattle feed
cattle_wheet = yield_per_acre[0] * w[0] + x[0] - y[0] 
m.addConstr(cattle_wheet == cattle_feed[0], "constraint_2")

# constraint_3: need 240t of corn for cattle feed
cattle_corn = yield_per_acre[1] * w[1] + x[1] - y[1]
m.addConstr(cattle_corn == cattle_feed[1], "constraint_3")

# constraint_4: Sugar beet sell price

m.addConstr((yield_per_acre[2] * w[2]) == (y[2] + y[3]), "constraint_4_1")
m.addConstr(y[2] <= 6000, "constraint_4_2")

m.optimize() # m.optimize()求解

# 透過屬性varName、x顯示決策變數名字及值

for n,v in enumerate(m.getVars()):
    print('%s : %s = %g' % (v.varName, name[n], v.x))
# 透過屬性objVal顯示最佳解
print('Obj : %g' % m.objVal)
print('Profit : %g' % -m.objVal)


