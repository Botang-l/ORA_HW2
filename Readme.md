# Operations Research Applications Assignment 2
[toc]
## Question1

### 1-(a)

- dicision variables : Ww, Wc, Wsb, Xw, Xc, Yw, Yc, Ysb1 and Ysb2
    - Ww, Wc 和 Wsb 分別代表 wheat, corn 和 sugar beet 三樣作物在土地中被種植的數量。
    
    - Xw 和 Xc 分別代表 wheat 和 corn 兩項作物明年購買的數量。
    - Yw 和 Yc 分別代表 wheat 和 corn 兩項作物明年賣出的數量。
    - Ysb1 和 Ysb2 分別代表 sugar beet 在 $36/t 和 $10/t 所賣出的數量。

- linear programming (LP) formulation with respect to average yield scenario
    
    - 目標函數 :

        本題目標函數應為最大化作物總收益；換言之，亦可將其內容表達為最小化作物總損失，其表達式如下所示:
        
         $$min ( \underbrace{150 \times Ww + 230 \times Wc + 260 \times Wsb}_{種植三種作物分別要付出的成本} + \underbrace{238 \times Xw + 210 \times Xc}_{購買 wheat 和 corn 所需付出的成本} - \underbrace{170 \times Yw - 150 \times Yc - 36 \times Ysb1 - 10 \times Ysb2}_{種植三種作物分別獲得的收益} )$$

    <br>

        
    - 限制式:
        
        本題限制式如下所示:

        1. 種植作物種量不得大於土地總面積。
            
            $Ww + Wc + Wsb <= 500$

        <br>   

        2. wheat 種植量 + wheat 購買量 - wheat 賣出量 = 製作飼料所需的 wheat 量
            
            $2.5 \times Ww + Xw - Yw >= 200$
        
        <br>

        3. corn 種植量 + corn 購買量 - corn 賣出量 = 製作飼料所需的 corn 量
            
            $3 \times Wc + Xc - Yc >= 240$

        <br>

        4.  sugar beet 種植量 - sugar beet 在 $36/t 和 $10/t 的賣出量 = 0
            
            $20 \times Wsb - Ysb1 - Ysb2 >= 0$
    
        <br>

        5. sugar beet 只有在產量低於 6000t 的部分才能以 $36/t 的價格賣出
            
            $Ysb1 <= 6000$
            
        <br>

        6. 所有決策變數皆大於等於 0
            
            $Ww, Wc, Wsb, Xw, Xc, Yw, Yc, Ysb1, Ysb2 >= 0$
            

---  

### 1-(b) 

求解結果:

- $Ww = 120$
- $Wc = 80$
- $Wsb = 300$
- $Xw = 0$
- $Xc = 0$
- $Yw = 100$
- $Yc = 0$
- $Ysb1 = 6000$
- $Ysb2 = 0$

- $Objective = -118600$

- $Profit = 118600$

---

### 1-(c) 

- decision variable : Ww, Wc, Wsb, Xw[n], Xc[n], Yw[n],  Yc[n], Ysb1[n], Ysb2[n]
    
    - 本例中，我們考慮3種不同場景，各場景情境如下所述:
    
        - 場景1：單位畝產量增產20%
    
        - 場景2：單位畝產量等於平均值
    
        - 場景3：單位畝產量減產20%
        

    - 上述 n = 1, 2, 3，且分別代表場景 1~3 時的決策變數變化。
    
    - Ww, Wc 和 Wsb 分別代表 wheat, corn 和 sugar beet 三樣作物在土地中被種植的數量。
    
    - Xw[n] 和 Xc[n] 分別代表 wheat 和 corn 兩項作物明年於三種場景中購買的數量。
    - Yw[n] 和 Yc[n] 分別代表 wheat 和 corn 兩項作物明年於三種場景中賣出的數量。
    - Ysb1[n] 和 Ysb2[n] 分別代表 sugar beet 於三種場景中在 $36/t 和 $10/t 所賣出的數量。
- deterministic equivalent problem (DEP) formulation of two-stage recourse problem (RP)
    - 目標函數 :

        本題目標函數應為最大化作物總收益；換言之，亦可將其內容表達為最小化作物總損失，其表達式如下所示:

        $$min ( \underbrace{150 \times Ww + 230 \times Wc + 260 \times Wsb}_{種植三種作物分別要付出的成本} + \frac{1}{3}\sum_{n=1}^3 \underbrace{(238 \times Xw[n] + 210 \times Xc[n] - 170 \times Yw[n]}_{各場景中購買 wheat 和 corn 所需付出的成本})$$
        $$-\frac{1}{3}\sum_{n=1}^3(\underbrace{150 \times Yc[n] - 36 \times Ysb1[n] - 10 \times Ysb2[n]}_{各場景中種植三種作物分別獲得的收益}))$$
        
    - 限制式:
            
        本題限制式如下所示:

        1. 種植作物種量不得大於土地總面積。
            
            $Ww + Wc + Wsb <= 500$

        <br>   

        2. wheat 種植量 + wheat 購買量 - wheat 賣出量 = 製作飼料所需的 wheat 量
            
            場景一 : $3 \times Ww + Xw[1] - Yw[1] >= 200$

            場景二 : $2.5 \times Ww + Xw[2] - Yw[2] >= 200$
            
            場景三 : $2 \times Ww + Xw[3] - Yw[3] >= 200$
        
        <br>

        3. corn 種植量 + corn 購買量 - corn 賣出量 = 製作飼料所需的 corn 量
            
            場景一 : $3.6 \times Wc + Xc[1] - Yc[1] >= 240$

            場景二 : $3 \times Wc + Xc[2] - Yc[2] >= 240$

            場景三 : $2.4 \times Wc + Xc[3] - Yc[3] >= 240$
            
        <br>

        4.  sugar beet 種植量 - sugar beet 在 $36/t 和 $10/t 的賣出量 = 0
            
            場景一 : $24 \times Wsb - Ysb1[1] - Ysb2[1] >= 0$

            場景二 : $20 \times Wsb - Ysb1[2] - Ysb2[2] >= 0$

            場景三 : $16 \times Wsb - Ysb1[3] - Ysb2[3] >= 0$

        <br>

        5. sugar beet 只有在產量低於 6000t 的部分才能以 $36/t 的價格賣出
            
            $Ysb1[n] <= 6000$

            $ n = 1, 2, 3$
            
        <br>

        6. 所有決策變數皆大於等於 0
            
            $Ww, Wc, Wsb, Xw[n], Xc[n], Yw[n], Yc[n], Ysb1[n], Ysb2[n] >= 0$

            $ n = 1, 2, 3$

--- 

### 1-(d)

求解結果

- $Ww = 170$
- $Wc = 80$
- $Wsb = 250$
- $Xw[1] = 0$
- $Xc[1] = 0$
- $Xw[2] = 0$
- $Xc[2] = 0$
- $Xw[3] = 0$
- $Xc[3] = 48$
- $Yw[1] = 310$
- $Yc[1] = 48$
- $Ysb1[1] = 6000$
- $Ysb2[1] = 0$
- $Yw[2] = 225$
- $Yc[2] = 0$
- $Ysb1[2] = 5000$
- $Ysb2[2] = 0$
- $Yw[3] = 140$
- $Yc[3] = 0$
- $Ysb1[3] = 4000$
- $Ysb2[3] = 0$
<br>
- $Objective = -108390$
- $Profit = 108390$
---

### 1-(e)

- EVPI
    EVPI = WS - RP<br>
    WS : 
    - 場景一最佳解 = 167667
    - 場景二最佳解 = 118600
    - 場景三最佳解 = 59950
    WS = $\frac{1}{3}( 167667 + 118600 + 59950)$ = 115406
    <br>

    EVPI = 115406 - 108390 = 7016
    
<br>

- VSS
    VSS = RP - EEV
    RP = 108390

    EEV :
    - 綜觀三種場景下單位生產期望值，可得到三種作物生產期望值如下所述:
        - 小麥 : 2.5 t /acre
        - 玉米 : 3 t /acre
        - 甜菜 : 20 t /acre
    - 場景一的解 = 148000
    - 場景二的解 = 118600
    - 場景三的解 = 55120
    EEV = $\frac{1}{3}( 148000 + 118600 + 55120)$ = 107240
    VSS = 108390 - 107240 = 1150
---

### 1-(f)

- I agree RP to provide a good solution in this study

    - 雖然 VSS 比 EVPI 少了 $115406 - 108390 = 7016$ 的獲利量，但事實上因為完全資訊難以取得，故 EVPI 經常僅是理想情況，實則難以達到。

    - 在無法獲取 EVPI 的狀況下，綜觀三種場景下單位生產期望值，可得到三種作物生產期望值如下所述:
        - 小麥 : 2.5 t /acre
        - 玉米 : 3 t /acre
        - 甜菜 : 20 t /acre

    - 而得到的求解結果中，三種作物個別生產量分別如下所示:

        - $Ww = 120$
        - $Wc = 80$
        - $Wsb = 300$
        
    - 接著，為確認該上述結果於三種下的生產量，需將生產計畫帶入三種場景進行計算，結果如下:
        
        - 場景一的解 = 148000
        - 場景二的解 = 118600
        - 場景三的解 = 55120

    - 計算加權平均值為 :

        - $\frac{1}{3}( 148000 + 118600 + 55120)$ = 107240 < VSS = 108390

    - 由此可知，隨機規劃的解相較於計算期望值，在目標函數上多出 $108390-107240=1150$ 的效益；故利用隨機規劃考慮不確定之信息，可在本案例中得到更加優越的解。

  
### 1-(g)

## Question2

### 2-(a)
本題因有三個決策可供選擇，故需要一個 decision node，且該 decision node 提供三個 branch。 

### 2-(b)
本題共有三個 chance node，且每一個 chance node 提供二個 branch。

### 2-(c)
![](https://playlab.computing.ncku.edu.tw:3001/uploads/upload_29b9ed9ab7596671727cfb873f21b785.png)

### 2-(d)
![](https://playlab.computing.ncku.edu.tw:3001/uploads/upload_141cbbc2b1c439932bfb6d48950121ff.png)

### 2-(e)
![](https://playlab.computing.ncku.edu.tw:3001/uploads/upload_03e06ad66574e7153bf1c866b3313277.png)

### 2-(f)
![](https://playlab.computing.ncku.edu.tw:3001/uploads/upload_4a55c0f6f52c351334688a51923928c6.png)

### 2-(g)
![](https://playlab.computing.ncku.edu.tw:3001/uploads/upload_cadcc93df8170a3e4134dc9212092c4f.png)

### 2-(h)
![](https://playlab.computing.ncku.edu.tw:3001/uploads/upload_f0b874e12b0ac2e4fe97aa5b357c9c87.png)

### 2-(i)
$EVPI = ERPI - ERw/o$
$ERPI = 0.59 \times 100000 + 0.41 \times 400000 = 754000$
$ERw/o = using strategy B = 423000$

$EVPI = 754000 - 423000 = 331000$

### 2-(j)

$決策方式 : if x=1, using strategy A ； if x=0, using strategy B$
$EMV(A|x=1) = 0.6495 \times 1000000 + 0.3505 \times (-400000) = 509300$ 
$EMV(C|x=0) = 0.1657 \times 100000 + 0.8343 \times (400000) = 350290$ 
$ERE = 0.505 \times 509300 + 0.495 \times 350290 = 430590.05$

### 2-(k)
$EVE = ERE - ERw/o$
$EVE = 430590.05 - 331000 = 99590.05 > 50000$

承上所述，應推薦雇請 marketing research。