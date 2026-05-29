(♣分析)  $ y^* = e^{2x} + e^x + xe^x $，其中  $ e^{2x} $ 不可能为非齐次方程的解，故只能是齐次方程的解，若  $ xe^x $ 为齐次方程的解，则至少对应二重根。

解 由  $ f(x) = \gamma e^x $ 可知  $ e^{ax}(a \neq 1) $ 不可能是非齐次方程的特解，故  $ e^{2x} $ 不可能是非齐次方程的特解，又因为  $ y = e^{2x} + e^x + xe^x $ 是非齐次方程的解，所以  $ e^{2x} $ 必是对应齐次方程的解，故微分方程有一个特征根  $ r_1 = 2 $。

若  $ e^x $ 是非齐次方程的解，则  $ xe^x $ 就是齐次方程的解，此时  $ r_1 = r_2 = 1 $，与上述  $ r_1 = 2 $ 矛盾，于是  $ e^x $ 也是齐次方程的解，此时  $ r_2 = 1 $。所以特征方程为  $ (r-1)(r-2) = 0 $，即

 $$ r^{2}-3r+2=0, $$ 

于是  $ \alpha = -3, \beta = 2 $

为确定  $ \gamma $，只需将特解  $ y^{*}=xe^{x} $ 代入方程，得

 $$ (x+2)\mathrm{e}^{x}-3(x+1)\mathrm{e}^{x}+2x\mathrm{e}^{x}=\gamma\mathrm{e}^{x}, $$ 

解得  $ \gamma = -1 $.

原方程的通解为  $ y = C_{1} e^{x} + C_{2} e^{2x} + xe^{x} $，其中  $ C_{1}, C_{2} $ 为任意常数.

## 3 n(n>2) 阶常系数齐次线性微分方程

①若 r 为单实根，写  $ Ce^{rx} $;

②若 r 为 k 重实根，写

一般不超过三重

 $$ (C_{1}+C_{2}x+C_{3}x^{2}+\cdots+C_{k}x^{k-1})\mathrm{e}^{rx} $$ 

③若r为单复根 $ \alpha\pm\beta i $，写

 $$ \mathrm{e}^{\alpha x}(C_{1}\cos\beta x+C_{2}\sin\beta x); $$ 

④若r为二重复根 $ \alpha\pm\beta i $，写

这是反求方程的理论基础

 $$ \mathrm{e}^{\alpha x}(C_{1}\cos\beta x+C_{2}\sin\beta x+C_{3}x\cos\beta x+C_{4}x\sin\beta x). $$ 

注 (1) 如果解中含特解  $ e^{rx} $，则 r 至少为单实根，如二重根  $ (C_{1}+C_{2}x)e^{rx} $，令  $ C_{1}=1 $， $ C_{2}=0 $；

(2) 如果解中含特解  $ x^{k-1}e^{rx} $，则 r 至少为 k 重实根；

(3) 如果解中含特解  $ e^{\alpha x} \cos \beta x $ 或  $ e^{\alpha x} \sin \beta x $，则  $ \alpha \pm \beta i $ 至少为单复根；

(4) 如果解中含特解  $ e^{\alpha x} x \cos \beta x $ 或  $ e^{\alpha x} x \sin \beta x $，则  $ \alpha \pm \beta i $ 至少为二重复根。

例 15.19 已知某四阶常系数齐次线性微分方程有特解  $ y_{1}(x) = e^{x} \cos 2x $,  $ y_{2}(x) = x $，且方程中  $ y^{(4)} $ 前的系数为 1，该方程为 ___.

 $$ 0+1\cdot x)e^{0x} $$ 