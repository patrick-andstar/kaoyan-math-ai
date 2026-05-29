注 对积分  $ \left|\int_{0}^{a}f(x)dx\right| $ 作估计，只要对被积函数  $ f(x) $ 作估计即可。条件中给出导数  $ f'(x) $ 及  $ f(0)=0 $ 的信息，自然想办法把  $ f(x) $ 和  $ f'(x) $ 联系起来。在高等数学中，联系  $ f(x) $ 和  $ f'(x) $ 有两种常用的办法，一是微分学中的拉格朗日中值定理（方法一），二是积分学中的牛顿－莱布尼茨公式（方法二）。

11.6 证明

 $$ f(x)=f\left(\frac{1}{2}\right)+f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)+\frac{f^{\prime \prime}(\xi)}{2!}\left(x-\frac{1}{2}\right)^{2}, $$ 

其中  $ \xi $ 介于 x 与  $ \frac{1}{2} $ 之间．又由  $ f''(x) > 0 $ ，则  $ f''(\xi) > 0 $ ，于是

 $$ f(x)\geqslant f\left(\frac{1}{2}\right)+f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right). $$ 

两边在区间  $ [0,1] $ 上对 x 积分，得

 $$ \begin{aligned}\int_{0}^{1}f(x)\mathrm{d}x&\geqslant\int_{0}^{1}\left[f\left(\frac{1}{2}\right)+f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)\right]\mathrm{d}x\\&=f\left(\frac{1}{2}\right)+f^{\prime}\left(\frac{1}{2}\right)\int_{0}^{1}\left(x-\frac{1}{2}\right)\mathrm{d}x=f\left(\frac{1}{2}\right)=1.\end{aligned} $$ 