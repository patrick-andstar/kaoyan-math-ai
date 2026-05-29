 $$ y_{t}=y_{C}(t)+y_{t}^{*}. $$ 

定理 2 若  $ \bar{y}_{t} $ 与  $ \bar{y}_{t} $ 分别是差分方程

 $$ y_{t+1}+a y_{t}=f_{1}(t) $$ 

和

 $$ y_{t+1}+a y_{t}=f_{2}(t) $$ 

 $$ y_{t}=\overline{y}_{t}+\tilde{y}_{t} $$ 

是差分方程

 $$ y_{t+1}+a y_{t}=f_{1}(t)+f_{2}(t) $$ 

的解.

非齐次差分方程 $ ^{①} $的特解 $ y_{t}^{*} $形式的设定见下表.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>①中 $ f(t) $的形式</td><td style='text-align: center; word-wrap: break-word;'>取待定特解的条件</td><td style='text-align: center; word-wrap: break-word;'>试取特解的形式</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ f(t)=d^{t}\cdot P_{m}(t) $</td><td style='text-align: center; word-wrap: break-word;'>$ a+d\neq0 $</td><td style='text-align: center; word-wrap: break-word;'>$ y_{t}^{*}=d^{t}\cdot Q_{m}(t) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ d $为非零常数</td><td style='text-align: center; word-wrap: break-word;'>$ a+d=0 $</td><td style='text-align: center; word-wrap: break-word;'>$ y_{t}^{*}=t\cdot d^{t}\cdot Q_{m}(t) $</td></tr><tr><td rowspan="2">$ f(t)=b_{1}\cos\omega t+b_{2}\sin\omega t $  $ \omega\neq0 $且 $ b_{1},b_{2} $为不同时为零的常数</td><td style='text-align: center; word-wrap: break-word;'>$ D=\left|\begin{matrix}a+\cos\omega &amp; \sin\omega \\ -\sin\omega &amp; a+\cos\omega\end{matrix}\right|\neq0 $</td><td style='text-align: center; word-wrap: break-word;'>$ y_{t}^{*}=\alpha\cos\omega t+\beta\sin\omega t $  $ \alpha,\beta $为待定常数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ D=0 $</td><td style='text-align: center; word-wrap: break-word;'>$ y_{t}^{*}=t(\alpha\cos\omega t+\beta\sin\omega t) $</td></tr></table>

例 15.24 差分方程  $ \Delta y_t = t $ 的通解为  $ y_t = \_\

解 应填  $ \frac{1}{2}t(t-1)+C $ (C 为任意常数).

 $ y_{t+1}-y_{t}=t $，其中 $ a+d=0 $，即知特解

 $ y^{*}=t(a+bt) $，代入原式后求解即可

齐次差分方程 $ y_{t+1}-y_{t}=0 $的特征根为r=1，其通解为y=C。

设非齐次差分方程 $ y_{t+1}-y_{t}=t $的一个特解为

 $$ \boldsymbol{y}^{*}=t(\boldsymbol{a}+b t), $$ 

代入方程并整理，得  $ a + b + 2bt = t $，所以  $ b = \frac{1}{2} $， $ a = -\frac{1}{2} $，故差分方程  $ \Delta y_{t} = t $ 的通解为

 $$ y_{t}=\frac{1}{2}t(t-1)+C(C 为任意常数 ). $$ 

例 15.25 求一阶差分方程  $ y_{t+1} - y_t = 4 \cos \frac{\pi}{3} t $ 的通解.  $ \rightarrow $ 分析形式： $ f(t) = b_1 \cos \omega t + b_2 \sin \omega t $.

解 对应齐次差分方程的通解为  $ y_{A}(t)=A $ 。由于

 $$ \begin{aligned} 套 D=\begin{vmatrix}a+\cos\omega&\sin\omega\\ -\sin\omega&a+\cos\omega\end{vmatrix} 即可 \end{aligned} $$ 