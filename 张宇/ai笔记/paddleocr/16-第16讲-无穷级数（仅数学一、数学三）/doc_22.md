例 16.21 级数  $ \sum_{n=1}^{\infty}(-1)^{n+1}\frac{\sqrt{n+1}-\sqrt{n}}{n^{p}} $ 条件收敛，则 p 的取值范围为 ___.

解 应填  $ -\frac{1}{2} < p \leqslant \frac{1}{2} $.

令  $ a_{n}=\frac{\sqrt{n+1}-\sqrt{n}}{n^{p}}(>0) $，则当  $ n\to\infty $ 时，

 $$ a_{n}=\frac{1}{(\sqrt{n+1}+\sqrt{n})n^{p}}=\frac{1}{\sqrt{n}\left(\sqrt{1+\frac{1}{n}}+1\right)n^{p}}\sim\frac{1}{2n^{p+\frac{1}{2}}}, $$ 

故当 $ p+\frac{1}{2}>1 $，即 $ p>\frac{1}{2} $时， $ \sum_{n=1}^{\infty}a_{n} $收敛，则原级数绝对收敛；当 $ p+\frac{1}{2}\leq1 $，即 $ p\leq\frac{1}{2} $时， $ \sum_{n=1}^{\infty}a_{n} $发散，则原级数非绝对收敛。

当  $ 0 < p + \frac{1}{2} \leqslant 1 $，即  $ -\frac{1}{2} < p \leqslant \frac{1}{2} $ 时，显然  $ a_{n} \to 0 (n \to \infty) $。令

 $$ f(x)=x^{p}(\sqrt{x+1}+\sqrt{x})(x>0), $$ 

由于

 $$ f^{\prime}(x)=x^{p-1}(\sqrt{x+1}+\sqrt{x})\left(p+\frac{\sqrt{x}}{2\sqrt{x+1}}\right), $$ 

且 $ x^{p-1}>0,\sqrt{x+1}+\sqrt{x}>0 $，而

 $$ \lim_{x\to+\infty}\left(p+\frac{\sqrt{x}}{2\sqrt{x+1}}\right)=p+\frac{1}{2}>0, $$ 

所以当$x$充分大时，$f(x)$单调增加，于是当$n$充分大时，$a_n = \frac{1}{f(n)}$单调减少，故由莱布尼茨判别法知，当$-\frac{1}{2} < p \leq \frac{1}{2}$时，原级数条件收敛；当$p + \frac{1}{2} \leq 0$，即$p \leq -\frac{1}{2}$时，$a_n$不趋于$0(n \to \infty)$，故当$p \leq -\frac{1}{2}$时，原级数发散。

<div style="text-align: center;"><img src="imgs/img_in_image_box_104_1136_140_1173.jpg" alt="Image" width="3%" /></div>


## 幂级数及其收敛域

<div style="text-align: center;"><img src="imgs/img_in_image_box_856_1088_960_1193.jpg" alt="Image" width="10%" /></div>


前面我们花了很大的工夫和精力去判别一个数项级数是否收敛，那么它的意义是什么呢？接下来的内容就会回答这个问题。