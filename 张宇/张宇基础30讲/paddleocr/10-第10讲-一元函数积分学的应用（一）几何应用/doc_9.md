## 考研数学基础30讲·高等数学分册

②a. $ f(x+2)-f(x)\Rightarrow $联想周期性（本题中的 $ f(x) $未必具有周期性）.

若 $ f(x) $是周期为T的周期函数，则 $ \int_{a}^{a+T}f(x)\mathrm{d}x=\int_{0}^{T}f(x)\mathrm{d}x(f(x+T)=f(x)) $.

设  $ F(x)=\int_{x}^{x+2}f(t)dt $，则  $ \overline{f}=\frac{F(1)}{2} $

b. 反写一至两步，联想经典形式  $ \left[\int_{\phi_{1}(x)}^{\phi_{2}(x)}f(t)\mathrm{d}t\right]^{\prime} $，则

 $$ \left[\int_{x}^{x+2}f(t)\mathrm{d}t\right]^{\prime}=f(x+2)-f(x)\;. $$ 

由 a. 或者 b. 都可以想到，令  $ F(x)=\int_{x}^{x+2}f(t)dt $

解 应填 $ \frac{1}{4} $

记 $ F(x)=\int_{x}^{x+2}f(t)dt $，则

变限积分函数

 $$ F^{\prime}(x)=f(x+2)-f(x)=x\ , $$ 

故

 $$ F(x)=\int x\mathrm{d}x=\frac{1}{2}x^{2}+C. $$ 

由  $ F(0)=\int_{0}^{2}f(x)dx=0=C $ ，得  $ F(x)=\frac{1}{2}x^{2} $ ，则  $ \int_{1}^{3}f(x)dx=F(1)=\frac{1}{2} $ ，故

 $$ \overline{f}=\frac{1}{3-1}\int_{1}^{3}f(x)\mathrm{d}x=\frac{1}{2}F(1)=\frac{1}{4}\;. $$ 

☑ 方法总结 学会观察条件，得到有效信息，产生联想，进而快速解题。

## 4 其他几何应用（仅数学一、数学二）

(1)“平面上的曲边梯形”的形心坐标公式.

设平面区域  $ D=\left\{(x,y)|0\leq y\leq f(x), a\leq x\leq b\right\} $， $ y=f(x) $ 在  $ [a,b] $ 上连续，如图 10-9 所示。现推导 D 的形心坐标  $ \vec{x} $， $ \vec{y} $ 的计算公式。

 $$ \overline{x}=\frac{\iint\limits_{D}x\mathrm{d}\sigma}{\iint\limits_{D}\mathrm{d}\sigma}=\frac{\int_{a}^{b}\mathrm{d}x\int_{0}^{f(x)}x\mathrm{d}y}{\int_{a}^{b}\mathrm{d}x\int_{0}^{f(x)}\mathrm{d}y}=\frac{\int_{a}^{b}x f(x)\mathrm{d}x}{\int_{a}^{b}f(x)\mathrm{d}x} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_672_1012_933_1161.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">图 10-9</div>


 $$ \overline{y}=\frac{\iint_{D}y\mathrm{d}\sigma}{\iint_{D}\mathrm{d}\sigma}=\frac{\int_{a}^{b}\mathrm{d}x\int_{0}^{f(x)}y\mathrm{d}y}{\int_{a}^{b}\mathrm{d}x\int_{0}^{f(x)}\mathrm{d}y}=\frac{\frac{1}{2}\int_{a}^{b}f^{2}(x)\mathrm{d}x}{\int_{a}^{b}f(x)\mathrm{d}x}. $$ 

秦公式，记住结论即可

例 10.9 设曲线  $ L $ 的方程为  $ y = \frac{1}{4}x^2 - \frac{1}{2}\ln x $， $ 1 \leq x \leq e $， $ D $ 是由曲线  $ L $ 和直线  $ x = 1 $， $ x = e $ 及  $ x $ 轴围成的平面图形，则  $ D $ 的形心的横坐标为___。