<div style="text-align: center;"><img src="imgs/img_in_image_box_346_140_947_362.jpg" alt="Image" width="58%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 18-11</div>


(3) 第一型曲面积分是由二重积分变换来的.

## 2 性质

以下均假设  $ \Sigma $ 为空间有限分片光滑曲面.

性质 1(求空间曲面的面积)  $ \iint_{D}1dS=S $，其中 S 为  $ \Sigma $ 的面积.

性质 2(可积函数必有界) 设  $ f(x, y, z) $ 在  $ \Sigma $ 上可积，则其在  $ \Sigma $ 上必有界.

性质 3(积分的线性性质) 设  $ k_{1}, k_{2} $ 为常数，则

 $$ \iint\limits_{\Sigma}[k_{1}f(x,y,z)\pm k_{2}g(x,y,z)]\mathrm{d}S=k_{1}\iint\limits_{\Sigma}f(x,y,z)\mathrm{d}S\pm k_{2}\iint\limits_{\Sigma}g(x,y,z)\mathrm{d}S. $$ 

性质 4(积分的可加性) 设  $ f(x, y, z) $ 在  $ \Sigma $ 上可积，且  $ \Sigma_1 \cup \Sigma_2 = \Sigma, \Sigma_1 \cap \Sigma_2 = \varnothing $，则

 $$ \iint\limits_{\Sigma}f(x,y,z)\mathrm{d}S=\iint\limits_{\Sigma_{1}}f(x,y,z)\mathrm{d}S+\iint\limits_{\Sigma_{2}}f(x,y,z)\mathrm{d}S. $$ 

性质 5(积分的保号性) 设  $ f(x, y, z) $,  $ g(x, y, z) $ 在  $ \Sigma $ 上可积，且在  $ \Sigma $ 上  $ f(x, y, z) \leqslant g(x, y, z) $，则有

 $$ \iint\limits_{\Sigma}f(x,y,z)\mathrm{d}S\leqslant\iint\limits_{\Sigma}g(x,y,z)\mathrm{d}S. $$ 

特殊地，有

 $$ \left|\iint_{\Sigma}f(x,y,z)\mathrm{d}S\right|\leqslant\iint_{\Sigma}\left|f(x,y,z)\right|\mathrm{d}S. $$ 

性质 6(第一型曲面积分的估值定理) 设 M, m 分别是  $ f(x, y, z) $ 在  $ \Sigma $ 上的最大值和最小值，S 为  $ \Sigma $ 的面积，则有

 $$ m S\leqslant\iint\limits_{\Sigma}f(x,y,z)\mathrm{d}S\leqslant M S. $$ 

性质 7(第一型曲面积分的中值定理) 设  $ f(x, y, z) $ 在  $ \Sigma $ 上连续， $ S $ 为  $ \Sigma $ 的面积，则在  $ \Sigma $ 上至少存在一点  $ (\xi, \eta, \zeta) $，使得

 $$ \iint\limits_{\Sigma}f(x,y,z)\mathrm{d}S=f(\xi,\eta,\zeta)S. $$ 