故  $ \sum_{n=1}^{\infty}a_{n}=\frac{e^{-\pi}}{5(1-e^{-\pi})}=\frac{1}{5(e^{\pi}-1)} $

下面介绍求复杂级数的和函数的方法。

思路：把复杂级数转化为简单级数！→②求不定积分③组数求和

①解微分方程.

②求不定积分.

③级数求和

基本公式： $ \sum_{n=0}^{\infty}x^{n}=\frac{1}{1-x},\quad|x|<1;\quad\sum_{n=1}^{\infty}x^{n}=\frac{x}{1-x},\quad|x|<1 $

例 16.30 求级数  $ \sum_{n=1}^{\infty}\frac{x^{n}}{n} $ 的和函数.

♣分析 由于 $ (x^n)' = nx^{n-1} $，因此本题应先求导，约掉 $ n $，然后再积分，但要注意 $ S(x) \neq \int S'(x) \, dx $，应写为 $ \int_{x_0}^x S'(t) \, dt = S(t)|_{x_0}^x = S(x) - S(x_0) $，即 $ S(x) = S(x_0) + \int_{x_0}^x S'(t) \, dt $（先导后积公式）。 $ x_0 $点一般选择展开点，例如 $ \sum a_n x^n $， $ x_0 $取0， $ \sum a_n(x - m)^n $， $ x_0 $取 $ m $。

解 设  $ S(x)=\sum_{n=1}^{\infty}\frac{x^n}{n} $，逐项求导，得  $ S'(x)=\sum_{n=1}^{\infty}\left(\frac{x^n}{n}\right)^'=\sum_{n=1}^{\infty}x^{n-1}=\frac{1}{1-x} $， $ |x|<1 $，然后两边积分，得  $ S(x)-S(0)=\int_0^x\frac{dt}{1-t}=-\ln(1-x) $。又因为  $ S(0)=0 $，且当  $ x=-1 $ 时，级数  $ \sum_{n=1}^{\infty}\frac{(-1)^n}{n} $ 收敛，故和函数  $ S(x)=-\ln(1-x)+S(0)=-\ln(1-x) $， $ x\in[-1,1) $。

方法总结 求和函数，先求收敛域，然后根据幂级数  $ \sum_{n=1}^{\infty}\frac{1}{n}x^{n} $ 的特点，选择先求导变为简单的幂级数，便于求和函数，然后用积分还原。

公式  $ \sum_{n=1}^{\infty}x^{n-1}=\frac{1}{1-x},\quad|x|<1;\quad\sum_{n=1}^{\infty}\frac{x^{n}}{n}=-\ln(1-x),\quad x\in[-1,1) $

例 16.31 求级数  $ \sum_{n=1}^{\infty} nx^{n} $ 的和函数.

♡分析 本题 $ \sum_{n=1}^{\infty}nx^{n} $，n在分子上，所以应该先积分，后求导.

解  $ \sum_{n=1}^{\infty}nx^{n}=x\sum_{n=1}^{\infty}nx^{n-1} $，设  $ S(x)=\sum_{n=1}^{\infty}nx^{n-1} $，则原级数  $ \sum_{n=1}^{\infty}nx^{n}=xS(x) $.

对  $ S(x)=\sum_{n=1}^{\infty}nx^{n-1} $ 两边积分，得  $ \int_{0}^{x}S(t)\mathrm{d}t=\sum_{n=1}^{\infty}x^{n}t^{n-1}\mathrm{d}t=\sum_{n=1}^{\infty}x^{n}=\frac{x}{1-x},\left|x\right|<1 $ 。再两边求导，得  $ \left[\int_{0}^{x}S(t)\mathrm{d}t\right]^{\prime}=\left(\frac{x}{1-x}\right)^{\prime}=\frac{1}{(1-x)^{2}} $ ，所以  $ \sum_{n=1}^{\infty}nx^{n}=xS(x)=\frac{x}{(1-x)^{2}},\left|x\right|<1 $ 。

方法总结 求和函数，先求收敛域，本题幂函数为 $ nx^{n} $，应先积分化为简单的幂级数，然后再求导.