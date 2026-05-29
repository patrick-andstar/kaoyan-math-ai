再如，

 $$ \begin{aligned}&\frac{\ln\left(e+\frac{1}{x}\right)-1=\ln\left(e+\frac{1}{x}\right)-\ln e}{}\\ &\quad\rightarrow\quad=\ln\left(1+\frac{1}{\mathrm{e}x}\right)．这个转化是极为有意义的 \\ \end{aligned} $$ 

又如  $ \lim_{x\to\infty}x\left[\ln\left(e+\frac{1}{x}\right)-1\right]=\lim_{x\to\infty}x\cdot\frac{1}{ex}=\frac{1}{e} $。如果你考虑用洛必达法则，那么就舍近求远了。

考研需要区分度，考生要掌握一些解题技巧。从辩证法去看，实现“统一美”。

(5) 极限： $ \lim_{x\to0^{+}}\ln x=-\infty,\quad\lim_{x\to+\infty}\ln x=+\infty $

当 x→+∞ 时， e^x→+∞ 的速度越来越快， ln x→+∞ 的速度越来越慢．

(6) 常用公式： $ x = e^{\ln x}(x > 0) $， $ u^y = e^{\ln u^y} = e^{\nu \ln u}(u > 0) $

 $ x^x = e^{\ln x^x} = e^{x \ln x} $，从而可看到， $ x^x $ 是初等函数。

<div style="text-align: center;"><img src="imgs/img_in_image_box_720_399_930_564.jpg" alt="Image" width="20%" /></div>


(7) 对数运算法则. 积变和

①  $ \log_{a}(MN)=\log_{a}M+\log_{a}N $（积的对数 = 对数的和）.

② $ \log_{a}\frac{M}{N}=\log_{a}M-\log_{a}N $（商的对数=对数的差）.

③  $ \log_{a}M^{n}=n\log_{a}M $， $ \log_{a}\sqrt[n]{M}=\frac{1}{n}\log_{a}M $（幂的对数=对数的倍数）.

一定要用好对数的运算法则，如： $ e^{\ln\sqrt{f^{2}(x)-f(x)+1}}=\sqrt{f^{2}(x)-f(x)+1} $

常考：当x>0时，

中值定理（拉格朗日中值定理）证明

 $$ \ln\sqrt{x}=\frac{1}{2}\ln x;\quad\ln\frac{1}{x}=-\ln x;\quad\ln\left(1+\frac{1}{x}\right)=\ln\frac{x+1}{x}=\ln(x+1)-\ln x $$ 

利用例 1.11，学习解题技巧。

例 1.11 已知  $ e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} $， $ x \in \mathbb{R} $，则  $ 2^x = (\quad) $。

(A)  $ \sum_{n=1}^{\infty} \frac{(x \ln 2)^n}{n!} $  

(B)  $ \sum_{n=0}^{\infty} \frac{(x \ln 2)^n}{n!} $  

(C)  $ \sum_{n=1}^{\infty} \frac{(\ln 2)x^n}{n!} $  

(D)  $ \sum_{n=0}^{\infty} \frac{(\ln 2)x^n}{n!} $

分析  $ 2^{x}=e^{\ln 2^{x}}=e^{x\ln 2} $

解 应选(B).

由于  $ 2^{x}=e^{x\ln2} $，又  $ e^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!} $， $ x\in\mathbb{R} $，因此  $ 2^{x}=\sum_{n=0}^{\infty}\frac{(x\ln2)^{n}}{n!} $

方法总结  $ \mathrm{e}^{x}=\sum_{n=0}^{\infty}\frac{x^{n}}{n!} $，广义化： $ 2^{x}=\mathrm{e}^{x\ln2}=\sum_{n=0}^{\infty}\frac{(x\ln2)^{n}}{n!} $