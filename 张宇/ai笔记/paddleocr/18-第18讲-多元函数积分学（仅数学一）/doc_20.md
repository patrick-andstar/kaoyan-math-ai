性质 1(求空间曲线的长度 (弧长))  $ \int_{\Gamma}1ds=l_{\Gamma} $，其中 $ l_{\Gamma} $为 $ \Gamma $的长度.

性质 2(可积函数必有界) 设  $ f(x, y, z) $ 在  $ \Gamma $ 上可积，则其在  $ \Gamma $ 上必有界.

 $$ \downarrow $$ 

同定积分

性质 3(积分的线性性质) 设  $ k_{1}, k_{2} $ 为常数，则

 $$ \int_{r}[k_{1}f(x,\ y,\ z)\pm k_{2}g(x,\ y,\ z)]\mathrm{d}s=k_{1}\int_{r}f(x,\ y,\ z)\mathrm{d}s\pm k_{2}\int_{r}g(x,\ y,\ z)\mathrm{d}s\ . $$ 

性质 4(积分的可加性) 设  $ f(x, y, z) $ 在  $ \Gamma $ 上可积，且  $ \Gamma_1 \cup \Gamma_2 = \Gamma $， $ \Gamma_1 \cap \Gamma_2 = \varnothing $，则

 $$ \int_{r}f(x,y,z)\mathrm{d}s=\int_{r_{1}}f(x,y,z)\mathrm{d}s+\int_{r_{2}}f(x,y,z)\mathrm{d}s. $$ 

性质 5(积分的保号性) 设  $ f(x, y, z) $,  $ g(x, y, z) $ 在  $ \Gamma $ 上可积，且在  $ \Gamma $ 上  $ f(x, y, z) \leqslant g(x, y, z) $,

则有

 $$ \int_{\Gamma}f(x,y,z)\underline{\mathrm{d}s}\leqslant\int_{\Gamma}g(x,y,z)\mathrm{d}s. $$ 

①定积分 $ \int_{a}^{b}f(x)dx $.

 $$  若 a<b\Rightarrow\mathrm{d}x>0\text{．} $$ 

 $$  若 a>b\Rightarrow\mathrm{d}x<0. $$ 

特殊地，有

 $$ \left|\int_{r}f(x,y,z)\mathrm{d}s\right|\leqslant\int_{r}\left|f(x,y,z)\right|\mathrm{d}s\ . 积分的保号性 $$ 

注意： $ d\sigma>0 $

③三重积分  $ \iiint\limits_{\Omega} f(x, y, z) \, \mathrm{d}v $.

注意： $ d\nu>0 $

性质 6(第一型曲线积分的估值定理) 设 M, m 分别是  $ f(x, y, z) $ 在  $ \Gamma $ 上的最大值和最小值， $ l_{r} $ 为  $ \Gamma $ 的长度，则有

与定积分、二重积分、三重积分类似

 $$ m l_{_{F}}\leqslant\int_{_{F}}f(x,y,z)\mathrm{d}s\leqslant M l_{_{F}}. $$ 

性质 7(第一型曲线积分的中值定理) 设  $ f(x, y, z) $ 在  $ \Gamma $ 上连续， $ l_{r} $ 为  $ \Gamma $ 的长度，则在  $ \Gamma $ 上至少存在一点  $ (\xi, \eta, \zeta) $，使得

 $$ \int_{r}f(x,y,z)\mathrm{d}s=f(\xi,\eta,\zeta)l_{r}. $$ 

## 3 普通对称性与轮换对称性

分析方法与二重积分、三重积分完全一样。

(1) 普通对称性.

<div style="text-align: center;"><img src="imgs/img_in_image_box_763_1024_947_1172.jpg" alt="Image" width="17%" /></div>


假设  $ \Gamma $ 关于 xOz 面对称，则

同理：上下对称，变的是

 $$ \int_{r}f(x,y,z)\mathrm{d}s=\left\{\begin{aligned}&2\int_{r_{1}}f(x,y,z)\mathrm{d}s,&f(x,y,z)=f(x,-y,z),\\ &0,&f(x,y,z)=-f(x,-y,z),\end{aligned}\right. $$ 

其中  $ \Gamma_{1} $ 是  $ \Gamma $ 在 xOz 面右边的部分.

关于其他坐标面对称的情况与此类似.

(2) 轮换对称性.