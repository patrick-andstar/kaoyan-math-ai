例6.12 设函数 $ f(x) $在 $ [0,1] $上二阶可导，且 $ \int_{0}^{1}f(x)dx=0 $，则（）.

(A) 当  $  f'(x) < 0  $ 时， $  f\left(\frac{1}{2}\right) < 0  $

(B) 当  $  f''(x) < 0  $ 时， $  f\left(\frac{1}{2}\right) < 0  $

(C) 当  $  f'(x) > 0  $ 时， $  f\left(\frac{1}{2}\right) < 0  $

(D) 当  $  f''(x) > 0  $ 时， $  f\left(\frac{1}{2}\right) < 0  $

分析与高阶导数有关的不等式考虑泰勒公式.

解 应选(D).

方法一 已知 $ f(x) $在 $ [0,1] $上二阶可导，则由带拉格朗日余项的泰勒公式有

 $$ f(x)=f\left(\frac{1}{2}\right)+f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)+\frac{1}{2}f^{\prime \prime}(\xi)\left(x-\frac{1}{2}\right)^{2} $$ 

其中  $ \xi $ 介于 x 与  $ \frac{1}{2} $ 之间. 对上式在  $ [0,1] $ 上取积分得

可从几何上直接得出

 $ \int_{0}^{2x_{0}}(x-x_{0})dx=0 $

 $$ \begin{aligned}\int_{0}^{1}f(x)\mathrm{d}x=&\int_{0}^{1}f\left(\frac{1}{2}\right)\mathrm{d}x+\int_{0}^{1}f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)\mathrm{d}x+\frac{1}{2}\int_{0}^{1}f^{\prime \prime}(\xi)\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x\\=&f\left(\frac{1}{2}\right)+f^{\prime}\left(\frac{1}{2}\right)\bullet\frac{1}{2}\left(x-\frac{1}{2}\right)^{2}\bigg|_{0}^{1}+\frac{1}{2}\int_{0}^{1}f^{\prime \prime}(\xi)\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x=0,\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_739_574_883_686.jpg" alt="Image" width="13%" /></div>


移项整理得 $ f\left(\frac{1}{2}\right)=-\frac{1}{2}\int_{0}^{1}f''(\xi)\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x $。 $ f'(\xi) $不能提至积分号外，因为此处的 $ \xi $与 $ x $有关，是 $ \xi=\xi(x) $，不是常数。

故当 $ f''(x)>0 $时，有 $ f''(\xi)>0 $，则 $ f\left(\frac{1}{2}\right)<0 $。因此选(D)。由积分保号性， $ \int_{0}^{1}f^{*}(\xi)\left(x-\frac{1}{2}\right)^{2}\mathrm{d}x>0 $

方法二 先写出泰勒公式  $ f(x) = f\left(\frac{1}{2}\right) + f'\left(\frac{1}{2}\right)\left(x - \frac{1}{2}\right) + \frac{f''(\xi)}{2}\left(x - \frac{1}{2}\right)^2 $.  $ \xi \in \left(x, \frac{1}{2}\right) \subset (0, 1) $

若  $ f''(\xi) > 0 $，则  $ \frac{f''(\xi)}{2}\left(x - \frac{1}{2}\right)^2 \geq 0 $，故  $ f(x) \geq f\left(\frac{1}{2}\right) + f'\left(\frac{1}{2}\right)\left(x - \frac{1}{2}\right) $.

对上式两边同时积分，在 $ [0,1] $上有

 $$ \int_{0}^{1}f(x)\mathrm{d}x>\int_{0}^{1}\left[f\left(\frac{1}{2}\right)+f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)\right]\mathrm{d}x, $$ 

故

 $$ \int_{0}^{1}\left[f\left(\frac{1}{2}\right)+f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)\right]\mathrm{d}x<0, $$ 

因为 $ \int_{0}^{1}f^{\prime}\left(\frac{1}{2}\right)\left(x-\frac{1}{2}\right)dx=0 $，所以 $ \int_{0}^{1}f\left(\frac{1}{2}\right)dx<0 $， $ f\left(\frac{1}{2}\right)<0 $。

例6.13 设函数 $ f(x) $在区间 $ [-1,1] $上具有三阶连续导数，且 $ f(-1)=0 $， $ f(1)=1 $， $ f'(0)=0 $，证