①  $ \int_{0}^{1}\frac{1}{x^{p}}dx $ 收敛， $ 0<p<1 $，

发散， $ p\geq1 $

 $ \rightarrow p=1 $ 是临界值， $ \int_{0}^{1}\frac{1}{x}dx=0-\lim_{x\to0^{+}}\ln x=+\infty $

p越小越收敛

②  $ \int_{1}^{+\infty}\frac{1}{x^{p}}dx $  $ \left\{\begin{array}{l} 收敛 , p>1 , \\  发散 , p\leq1 \end{array}\right. $  $ \rightarrow $  $ \int_{1}^{+\infty}\frac{1}{x}dx=\lim_{x\to+\infty}\ln x-\ln1=+\infty $

<div style="text-align: center;"><img src="imgs/img_in_image_box_598_226_925_403.jpg" alt="Image" width="31%" /></div>


对于①，盯着  $ x \to 0^+ $ 看， $ x^p $ 的次数  $ p $ ：当  $ p \geq 1 $ 时， $ x^p $ 趋于 0 的“速度”够快，其倒数  $ \frac{1}{x^p} $ 趋于  $ +\infty $ 的“速度”亦够快，积分发散；当  $ 0 < p < 1 $ 时， $ x^p $ 趋于 0 的“速度”不够快，其倒数  $ \frac{1}{x^p} $ 趋于  $ +\infty $ 的“速度”亦不够快，积分收敛。

懂得了以上道理后，便可有所发挥，如当  $ x \to 0^{+} $ 时， $ \sin x \sim x $，这意味着  $ \sin x $ 与  $ x $ 趋于 0 的 “速度” 一样。故  $ \int_{0}^{1} \frac{1}{\sin^{p} x} \, dx $（有时命制成  $ \int_{0}^{\frac{\pi}{2}} \frac{1}{\sin^{p} x} \, dx $）依然满足  $ \lim_{x \to 0^{+}} \frac{\sin x}{x} = 1 $，故  $ \lim_{x \to 0^{+}} \frac{\sin^{p} x}{x^{p}} = 1 $。

收敛， $ 0 < p < 1 $，

发散， $ p \geq 1 $。

事实上，凡是与x趋于0的“速度”一样的函数 $ f(x) $均可如上讨论。

对于②，盯着 $ x\to+\infty $看， $ x^{p} $的次数p:当p>1时， $ x^{p} $趋于+ $ \infty $的“速度”够快，其倒数 $ \frac{1}{x^{p}} $趋于0的“速度”亦够快，积分收敛；当 $ p\leq1 $时， $ x^{p} $趋于+ $ \infty $的“速度”不够快，其倒数 $ \frac{1}{x^{p}} $趋于0的“速度”亦不够快，积分发散。

这里的发挥简单些，如当 $ x\to+\infty $且a>0时， $ ax+b $亦趋于+ $ \infty $，与x趋于+ $ \infty $的“速度”一样。

当 $ ax+b\geq k>0 $时， $ \int_{1}^{+\infty}\frac{1}{(ax+b)^{p}}dx $依然满足 $ \left\{\begin{aligned} 收敛,p>1,\\ 发散,p\leq1.\end{aligned}\right. $  $ \Rightarrow\lim_{x\to+\infty}\frac{(ax+b)^{p}}{(ax)^{p}}=1 $

例8.15 设a>b>0，反常积分 $ \int_{0}^{+\infty}\frac{1}{x^{a}+x^{b}}dx $收敛，则（）.

(A) a>1 且 b>1 (B) a>1 且 b<1 (C) a<1 且  $ a+b>1 $ (D) a<1 且 b<1

解 应选(B).

理论依据在 “四、2” 的注中讲过了，来看此题：

 $$ I=\int_{0}^{1}\frac{1}{x^{a}+x^{b}}\mathrm{d}x+\int_{1}^{+\infty}\frac{1}{x^{a}+x^{b}}\mathrm{d}x=I_{1}+I_{2}. $$ 

对于  $ I_{1} $，盯着  $ x \rightarrow 0^{+} $ 看，由于 a > b > 0，因此  $ x^{b} $ 趋于 0 的 “速度” 慢于  $ x^{a} $ 趋于 0 的 “速度” ，