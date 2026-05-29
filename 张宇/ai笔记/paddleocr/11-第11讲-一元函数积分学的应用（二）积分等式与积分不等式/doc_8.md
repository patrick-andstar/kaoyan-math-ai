 $$ \left|f(x)\right|=\left|\int_{b}^{x}f^{\prime}(t)dt\right|=\left|\int_{x}^{b}f^{\prime}(t)dt\right|\leqslant\int_{x}^{b}\left|f^{\prime}(t)\right|dt $$ 

式① + 式②，得  $ 2\left|f(x)\right|\leqslant\int_{a}^{x}\left|f'(t)\right|\mathrm{d}t+\int_{x}^{b}\left|f'(t)\right|\mathrm{d}t=\int_{a}^{b}\left|f'(t)\right|\mathrm{d}t $，即

 $$ \left|f(x)\right|\leqslant\frac{1}{2}\int_{a}^{b}\left|f^{\prime}(x)\right|\mathrm{d}x\quad. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_74_392_155_454.jpg" alt="Image" width="7%" /></div>


## 基础习题精练

## 习题

11.1 若函数  $ \varphi(x) $ 具有二阶导数，且满足  $ \varphi(2) > \varphi(1) $， $ \varphi(2) > \int_{2}^{3} \varphi(x) \, dx $，证明：至少存在一点  $ \xi \in (1, 3) $，使得  $ \varphi''(\xi) < 0 $。

11.2 证明： $ \int_{0}^{\frac{\pi}{2}}\frac{\cos x}{1+x^{2}}dx\geqslant\int_{0}^{\frac{\pi}{2}}\frac{\sin x}{1+x^{2}}dx $

11.3 设  $ \varphi(x) $ 是可微函数  $ f(x) $ 的反函数，且  $ f(1)=0 $ ，证明：

 $$ \int_{0}^{1}\left[\int_{0}^{f(x)}\varphi(t)\mathrm{d}t\right]\mathrm{d}x=2\int_{0}^{1}x f(x)\mathrm{d}x\ . $$ 

11.4 设 $ f(x) $在 $ [a,b] $上连续且严格单调增加，证明：

 $$ (a+b)\int_{a}^{b}f(x)\mathrm{d}x<2\int_{a}^{b}x f(x)\mathrm{d}x\quad. $$ 

11.5 设  $ f'(x) $ 在  $ [0, a] $ 上连续，且  $ f(0) = 0 $，证明：

 $$ \left|\int_{0}^{a}f(x)\mathrm{d}x\right|\leqslant\frac{Ma^{2}}{2}, $$ 

其中  $ M = \max_{0 \leq x \leq a} |f'(x)| $

11.6 设  $ f(x) $ 在区间  $ [0,1] $ 上有二阶导数，且  $ f\left(\frac{1}{2}\right)=1 $， $ f''(x)>0 $，证明： $ \int_{0}^{1}f(x)dx\geqslant1 $

## 解答

11.1 证明 由积分中值定理，可知至少存在一点  $ \eta \in (2, 3] $，使得