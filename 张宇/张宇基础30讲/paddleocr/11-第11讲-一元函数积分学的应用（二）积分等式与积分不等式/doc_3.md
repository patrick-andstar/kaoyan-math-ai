## 2 用夹逼准则

例 11.3  $ \lim_{n\to\infty}\int_{0}^{1}(n+1)x^n\ln(1+x)dx= $（）.

(A) $ \ln 2 $

(B) 1

(C) $ e^{2} $

(D) $ +\infty $

解 应选(A).

凑微分法

 $$ \begin{aligned}\int_{0}^{1}(n+1)x^{n}\ln(1+x)\mathrm{d}x&=\int_{0}^{1}\ln(1+x)\mathrm{d}(x^{n+1})\\&=x^{n+1}\ln(1+x)\Big|_{0}^{1}-\int_{0}^{1}\frac{x^{n+1}}{1+x}\mathrm{d}x\\&=\ln2-\int_{0}^{1}\frac{x^{n+1}}{1+x}\mathrm{d}x,\end{aligned} $$ 

对于 $ \lim_{n\to\infty}\int_{0}^{1}\frac{x^{n+1}}{1+x}dx $，利用放缩法．由于 $ 0\leqslant\frac{x^{n+1}}{1+x}\leqslant x^{n+1} $， $ 0\leqslant x\leqslant1 $，故

 $$ 0\leqslant\int_{0}^{1}\frac{x^{n+1}}{1+x}\mathrm{d}x\leqslant\int_{0}^{1}x^{n+1}\mathrm{d}x=\frac{1}{n+2} $$ 

当 $ n\to\infty $时，由夹逼准则，有 $ \lim_{n\to\infty}\int_{0}^{1}\frac{x^{n+1}}{1+x}dx=0 $．于是原式 $ =\ln2 $．

例 11.4 (1) 比较  $ \int_{0}^{1} \ln t \left[ \ln(1 + t) \right]^n dt $ 与  $ \int_{0}^{1} t^n \left| \ln t \right| dt $ ( $ n = 1, 2, \cdots $) 的大小，说明理由；

(2) 记  $ u_n = \int_0^1 |\ln t| [\ln(1+t)]^n \, dt $ ( $ n = 1, 2, \cdots $)，求  $ \lim_{n \to \infty} u_n  $

解 (1) 当  $ 0 \leqslant t \leqslant 1 $ 时， $ 0 \leqslant \ln(1+t) \leqslant t $，则  $ 0 \leqslant [\ln(1+t)]^n \leqslant t^n $，两边同时乘以  $ |\ln t| $，有

 $$ 0\leqslant\left|\ln t\right|\left[\ln(1+t)\right]^{n}\leqslant t^{n}\left|\ln t\right|, $$ 

根据积分的保号性，得

 $$ \int_{0}^{1}\left|\ln t\right|\left[\ln(1+t)\right]^{n}\mathrm{d}t\leqslant\int_{0}^{1}t^{n}\left|\ln t\right|\mathrm{d}t\quad. $$ 

(2) 由 (1) 知，

 $$ 0\leqslant u_{n}=\int_{0}^{1}\left|\ln t\right|\left[\ln(1+t)\right]^{n}\mathrm{d}t\leqslant\int_{0}^{1}t^{n}\left|\ln t\right|\mathrm{d}t\quad. $$ 

重要结论  $ \lim_{t\to0^{+}}t^{a}\ln t=0(a>0) $

因为  $ \int_{0}^{1}t^{n}\left|\ln t\right|\mathrm{d}t = -\int_{0}^{1}t^{n}\ln t\mathrm{d}t = -\frac{t^{n+1}}{n+1}\ln t\bigg|_{0}^{1} + \frac{1}{n+1}\int_{0}^{1}t^{n}\mathrm{d}t = 0 + \frac{1}{n+1}\lim_{t\to0^{+}}t^{n+1}\ln t + \frac{t^{n+1}}{(n+1)^{2}}\bigg|_{0}^{1} = \frac{1}{(n+1)^{2}} $,

所以  $ \lim_{n\to\infty}\int_{0}^{1}t^{n}\left|\ln t\right|dt=0 $ ，于是由夹逼准则得  $ \lim_{n\to\infty}u_{n}=0 $

注 更为一般的结论：设 $ f(x) $在 $ [0,1] $上连续，则 $ \lim_{n\to\infty}\int_{0}^{1}x^n f(x)dx=0 $