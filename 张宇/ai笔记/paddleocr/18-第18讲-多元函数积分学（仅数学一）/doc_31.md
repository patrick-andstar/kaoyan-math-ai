四 平面第二型曲线积分  $ \rightarrow $ 进入向量型被积函数求积分

<div style="text-align: center;"><img src="imgs/img_in_image_box_864_156_969_264.jpg" alt="Image" width="10%" /></div>


## 变力沿曲线做功

在一个向量场——变力场中，设某质点在变力  $ F(x, y) = P(x, y)i + Q(x, y)j $ 作用下，沿着有向曲线  $ L $ 从起点  $ A $ 移动到终点  $ B $，总共做了多少功？(这个物理背景请大家熟记，考研中出现过基于这种背景的考题.)

设沿着有向曲线  $ L $ 在  $ M(x, y) $ 点移动了一个微位移  $ ds = \mathrm{d}xi + \mathrm{d}yj $，将变力  $ F(x, y) $ 近似看作常力，则力在此微位移上的微功  $ \mathrm{d}W = F(x, y) \cdot \mathrm{d}s $，于是变力  $ F(x, y) $ 沿着有向曲线  $ L $ 从起点  $ A $ 移动到终点  $ B $ 所做的总功为



<div style="text-align: center;"><img src="imgs/img_in_image_box_676_424_967_587.jpg" alt="Image" width="28%" /></div>


 $$ \begin{aligned}W=&\int_{L}\mathrm{d}W=\int_{L}F(x,y)\cdot\mathrm{d}s=\int_{L}(P(x,y),Q(x,y))\cdot(\mathrm{d}x,\mathrm{d}y)\\ &=\int_{L}\frac{F 在 \mathrm{d}s 上的做功微元 }{\sqrt{\frac{P(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y}{\sqrt{\frac{P(x,y)x+Q(x,y)y}{\sqrt{x+y}}}}=\int_{L}P\mathrm{d}x+\int_{L}Q\mathrm{d}y},\\ &\quad 水平方向 \quad 铅直方向 \quad\\ &\quad 做功微元 \quad 做功微元 \end{aligned} $$ 

于是我们就引出了第二型曲线积分的概念.

## 2 概念

第二型曲线积分的被积函数  $ F(x, y) = P(x, y)i + Q(x, y)j $ 定义在平面有向曲线 L 上，其物理背景是变力  $ F(x, y) $ 在平面曲线 L 上从起点移动到终点所做的总功：

 $$ \int_{L}P(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y. $$ 

由此可以看出，前面所学的定积分、二重积分、三重积分、第一型曲线积分和第一型曲面积分有着完全一致的背景，都是一个数量函数在定义区域上计算几何量（面积、体积等），但是第二型曲线积分与之不同，它是一个向量函数沿有向曲线的积分（无几何量可言）。于是，有些性质和计算方法都不一样了，一定要加以对比，理解它们的区别和联系，不要用错或者用混了。

 $$ \int_{L}F\mathrm{d}s $$ 

## 3 性质

以下总假设  $ \Gamma $ 为空间有限长分段光滑曲线.

性质 1(积分的线性性质) 设  $ k_{1}, k_{2} $ 为常数，则  $ \int_{\Gamma}\left(k_{1}F_{1}\pm k_{2}F_{2}\right)\cdot\mathrm{d}s=k_{1}\int_{\Gamma}F_{1}\cdot\mathrm{d}s\pm k_{2}\int_{\Gamma}F_{2}\cdot\mathrm{d}s $

性质 2(积分的有向性)  $ \int_{\widehat{AB}} F \cdot ds = -\int_{\widehat{BA}} F \cdot ds $. 两个力的线性组合