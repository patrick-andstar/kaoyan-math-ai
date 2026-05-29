## 经济应用（仅数学三）

①总成本  $ C(Q) $，边际成本  $ C'(Q) $，固定成本  $ C_{0} $ 之间的关系为

<div style="text-align: center;"><img src="imgs/img_in_image_box_854_136_959_243.jpg" alt="Image" width="10%" /></div>


 $$ C(Q)=\int_{0}^{\mathcal{Q}}C^{\prime}(t)\mathrm{d}t+C_{0}. $$ 

②总收益 $ R(Q) $与边际收益 $ R'(Q) $之间的关系为

 $$ R(Q)=\int_{0}^{Q}R^{\prime}(t)\mathrm{d}t $$ 

注  $ \overline{y}=\frac{1}{b-a}\int_{a}^{b}f(x)dx $

例 12.4 已知某产品的边际成本为  $ 4 + \frac{x}{4} $（万元 / 单位），固定成本为 1 万元，产品对价格的需求弹性为  $ \frac{p}{8 - p} $，p > 0，产品最大需求量为 8，其中 x 表示产量，p 表示价格，求使产品取最大利润时的产量和价格。

分析 翻译成数学语言 + 引入记号： $ \left\{\begin{aligned}C'(x)&=4+\frac{x}{4}, C(0)=1,\\ -\frac{dx}{dp}&\cdot\frac{p}{x}=\frac{p}{8-p}, x(0)=8.\end{aligned}\right. $

解 由  $ C'(x)=4+\frac{x}{4} $， $ C(0)=1 $，可得

 $$ C(x)=\int_{0}^{x}C^{\prime}(t)\mathrm{d}t+C(0)=4x+\frac{x^{2}}{8}+1\quad. $$ 

又  $ \eta_{0}=\frac{-p\mathrm{d}x}{x\mathrm{d}p}=\frac{p}{8-p} $ （注意：由经济意义知  $ \frac{p}{8-p}>0 $），故  $ \frac{\mathrm{d}x}{x}=\frac{\mathrm{d}p}{p-8} $，可得

 $$ \ln\left|x\right|=\ln\left|p-8\right|+\ln c. $$ 

由 $ x(0)=8 $可得c=1。所以x=8-p， $ R(x)=8x-x^{2} $。故

 $$ \begin{aligned}L(x)&=R(x)-C(x)=(8x-x^{2})-\left(4x+\frac{x^{2}}{8}+1\right)\\&=-\frac{9}{8}x^{2}+4x-1\end{aligned} $$ 

令  $ L'(x)=4-\frac{9}{4}x=0 $ ，可得  $ x_{0}=\frac{16}{9} $

因为  $ L''(x) = -\frac{9}{4} < 0 $，所以  $ x_0 = \frac{16}{9} $ 为最大值点，这时  $ p = 8 - x_0 = \frac{56}{9} $。故当产量为  $ \frac{16}{9} $ 个单位，价格

为 $ \frac{56}{8} $万元时，利润最大