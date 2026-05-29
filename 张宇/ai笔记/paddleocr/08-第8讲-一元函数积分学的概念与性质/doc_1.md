<div style="text-align: center;"><img src="imgs/img_in_image_box_101_136_162_205.jpg" alt="Image" width="5%" /></div>


## 基础内容精讲

## 不定积分

<div style="text-align: center;"><img src="imgs/img_in_image_box_840_245_943_353.jpg" alt="Image" width="9%" /></div>


## 原函数与不定积分

设函数 $ f(x) $定义在某区间 $ I $上，若存在可导函数 $ F(x) $，对于该区间上任意一点都有 $ F'(x)=f(x) $成立，则称 $ F(x) $是 $ f(x) $在区间 $ I $上的一个原函数。称 $ \int f(x)dx=F(x)+C $为 $ f(x) $在区间 $ I $上的不定积分。

问：为什么强调一个？

答：因为若  $ F'(x) = f(x) $，

则对于任意常数 C，都有  $ [F(x) + C]' = F'(x) = f(x) $，

故  $ F(x) + C $ 也是原函数，所以  $ f(x) $ 若有原函数，则原函数

一定有无穷多个， $ F(x) + C $ 称为全体原函数

注 谈到函数 $ f(x) $的原函数与不定积分，必须指明 $ f(x) $所定义的区间.

例 8.1 设 0 < x < 1，且  $ \int (1 - x^2) f(x^2) \, \mathrm{d}x = \arcsin x + C $，则  $ f(x) = (\ ) $.

(A)  $ (1-x)^{\frac{3}{2}} $ (B)  $ (1-x)^{\frac{3}{2}} $ (C)  $ (1-x^2)^{\frac{3}{2}} $ (D)  $ (1-x^2)^{-\frac{3}{2}} $

分析 按照原函数定义  $ \int f(x) \, dx = F(x) + C $.

解 应选(B).  $ F'(x) $

根据原函数  $ F(x) $ 的定义  $ F'(x) = f(x) $ 求解.

将所给表达式的等式两端分别关于x求导，得

 $$ \left[\int(1-x^{2})f(x^{2})\mathrm{d}x\right]^{\prime}=(\arcsin x+C)^{\prime}, $$ 

即

 $$ (1-x^{2})f(x^{2})=\frac{1}{\sqrt{1-x^{2}}}, $$ 

 $$ f(x^{2})=(1-x^{2})^{\frac{3}{2}}, $$ 

故

 $$ f(x)=(1-x)^{-\frac{3}{2}}. $$ 

故选(B).

例 8.2 函数  $ f(x)=\begin{cases}\frac{1}{\sqrt{1+x^{2}}}, & x\leq0, \\ (x+1)\cos x, & x>0\end{cases} $ 的一个原函数为（）.