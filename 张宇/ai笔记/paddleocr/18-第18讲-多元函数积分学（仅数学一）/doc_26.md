## 3 普通对称性与轮换对称性

分析方法与二重积分、三重积分和第一型曲线积分完全一样。

(1) 普通对称性.

<div style="text-align: center;"><img src="imgs/img_in_image_box_730_138_937_270.jpg" alt="Image" width="20%" /></div>


假设  $ \Sigma $ 关于 xOz 面对称，则

 $$ \iint\limits_{\Sigma}f(x,y,z)\mathrm{d}S=\left\{\begin{aligned}&2\iint\limits_{\Sigma_{1}}f(x,y,z)\mathrm{d}S,\quad&f(x,y,z)=f(x,-y,z),\\ &0,\quad&f(x,y,z)=-f(x,-y,z),\end{aligned}\right. $$ 

其中  $ \Sigma_{1} $ 是  $ \Sigma $ 在 xOz 面右边的部分.

补充：

关于其他坐标面对称的情况与此类似.

 $$  记忆 \begin{aligned}&\left\{\begin{aligned} \textcircled{7} \left[\begin{aligned} 面微分 \mathrm{d}S&=\sqrt{1+(z_{x}^{\prime})^{2}+(z_{y}^{\prime})^{2}}\mathrm{d}x\mathrm{d}y\\ 孤微分 \mathrm{d}s&=\sqrt{1+(y_{x}^{\prime})^{2}}\mathrm{d}x\end{aligned}\right.\\ \textcircled{2} \mathrm{d}S&=\sqrt{1+(y_{z}^{\prime})^{2}+(y_{x}^{\prime})^{2}}\mathrm{d}z\mathrm{d}x\end{aligned}\right.\\ &\textcircled{3} \mathrm{d}S=\sqrt{1+(x_{y}^{\prime})^{2}+(x_{z}^{\prime})^{2}}\mathrm{d}y\mathrm{d}z\\ \end{aligned} $$ 

(2) 轮换对称性.

当  $ \Sigma: z = z(x, y) $ 为单值函数时，若把  $ x $ 与  $ y $ 对调后， $ \Sigma $ 不变，则  $ \iint_{\Sigma} f(x, y, z) \, \mathrm{d}S = \iint_{\Sigma} f(y, x, z) \, \mathrm{d}S $，这就是轮换对称性。

关于其他情况与此类似。

## 4 计算

因为第一型曲面积分就是由二重积分推广而来的，所以计算第一型曲面积分的基本方法就是将其化为二重积分．口诀为“一投二代三计算”．

无论空间曲面Σ是由显式 $ z=z(x,y) $还是隐式 $ F(x,y,z)=0 $给出的，我们都需要做三件事（无逻辑上的先后顺序，哪件事情最有利于解题就先做哪件）.

①一投：将  $ \Sigma $ 投影到某一平面（比如 xOy 面）上，设投影区域为 D（比如  $ D_{xy} $）；

②二代：将 $ z=z(x,y) $或 $ F(x,y,z)=0 $代入 $ f(x,y,z) $;

③三计算：计算 $ z_{x}^{\prime} $， $ z_{y}^{\prime} $，则 $ \mathrm{d}S=\sqrt{1+\left(z_{x}^{\prime}\right)^{2}+\left(z_{y}^{\prime}\right)^{2}}\mathrm{d}x\mathrm{d}y $

这就把第一型曲面积分化成了二重积分（比如化成关于x, y的二重积分），得到

<div style="text-align: center;"><img src="imgs/img_in_image_box_206_1104_667_1268.jpg" alt="Image" width="44%" /></div>


化成关于其他变量的二重积分与此类似.