## 2 性质

以下总假设  $ \Omega $ 为空间有界闭区域.

性质 1(求空间区域的体积)  $ \iiint_{\Omega}1\mathrm{d}v=\iiint_{\Omega}\mathrm{d}v=V $，其中 V 为  $ \Omega $ 的体积.

性质 2(可积函数必有界) 设  $ f(x, y, z) $ 在  $ \Omega $ 上可积，则其在  $ \Omega $ 上必有界.

性质 3(积分的线性性质) 设  $ k_{1}, k_{2} $ 为常数，则

 $$ \iiint\limits_{\Omega}[k_{1}f(x,y,z)\pm k_{2}g(x,y,z)]\mathrm{d}v=k_{1}\iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v\pm k_{2}\iiint\limits_{\Omega}g(x,y,z)\mathrm{d}v. $$ 

性质 4(积分的可加性) 设  $ f(x, y, z) $ 在  $ \Omega $ 上可积，且  $ \Omega_1 \cup \Omega_2 = \Omega $， $ \Omega_1 \cap \Omega_2 = \varnothing $，则

 $$ \iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v=\iiint\limits_{\Omega_{1}}f(x,y,z)\mathrm{d}v+\iiint\limits_{\Omega_{2}}f(x,y,z)\mathrm{d}v. $$ 

性质 5(积分的保号性) 设  $ f(x, y, z) $,  $ g(x, y, z) $ 在  $ \Omega $ 上可积，且在  $ \Omega $ 上  $ f(x, y, z) \leqslant g(x, y, z) $，则有

 $$ \iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v\leqslant\iiint\limits_{\Omega}g(x,y,z)\mathrm{d}v. $$ 

特殊地，有

 $$ \left|\iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v\right|\leqslant\iiint\limits_{\Omega}\left|f(x,y,z)\right|\mathrm{d}v\rightarrow 绝对值不等式 $$ 

性质 6(三重积分的估值定理) 设 M, m 分别是  $ f(x, y, z) $ 在  $ \Omega $ 上的最大值和最小值，V 为  $ \Omega $ 的体积，则有

 $$ m V\leqslant\iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v\leqslant M V. $$ 

性质 7(三重积分的中值定理) 设  $ f(x, y, z) $ 在  $ \Omega $ 上连续， $ V $ 为  $ \Omega $ 的体积，则在  $ \Omega $ 上至少存在一点  $ (\xi, \eta, \zeta) $，使得

 $$ \iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v=f(\xi,\eta,\zeta)V. $$ 

## 3 普通对称性与轮换对称性

分析方法与二重积分完全一样． $ \rightarrow $ 关于yOz（前后）： $ (x,y,z) $与 $ (-x,y,z) $对应

 $$  关于 xOy\ ( 上下 )\ :\ (x,\ y,\ z) 与 (x,\ y,\ -z) 对应 $$ 

(1) 普通对称性.

假设  $ \Omega $ 关于 xOz 面对称（见图 18-1），则

x, z 不动，关于 y 为偶函数

 $$ \iiint\limits_{\Omega}f(x,y,z)\mathrm{d}v=\left\{\begin{aligned}&2\iiint\limits_{\Omega_{1}}f(x,y,z)\mathrm{d}v,&f(x,y,z)=f(x,-y,z),\\ &0,&f(x,y,z)=-f(x,-y,z),\end{aligned}\right. $$ 

其中  $ \Omega_{1} $ 是  $ \Omega $ 在 xOz 面右边的部分.