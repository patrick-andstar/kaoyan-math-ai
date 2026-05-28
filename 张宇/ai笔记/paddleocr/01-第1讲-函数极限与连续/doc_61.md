因为  $ \lim_{x\to+\infty}\frac{1}{x}\ln\left(x+\sqrt{1+x^{2}}\right)=\lim_{x\to+\infty}\frac{1}{x+\sqrt{1+x^{2}}}\left(1+\frac{x}{\sqrt{1+x^{2}}}\right)=\lim_{x\to+\infty}\frac{1}{\sqrt{1+x^{2}}}=0 $，所以  $ \lim_{x\to+\infty}\left(x+\sqrt{1+x^{2}}\right)^{\frac{1}{x}}=\mathrm{e}^{0}=1 $

(4) “ $ 1^{\infty} $” $ \rightarrow $简化公式  $ \lim_{n\to\infty}u^{n}=e^{\lim_{n\to\infty}(u-1)} $

例1.33 求极限  $ \lim_{x\to0}\left(\frac{e^{x}+e^{2x}+e^{3x}}{3}\right)^{\frac{e}{x}} $

分析“ $ 1^{\infty} $”型未定式，用好公式“ $ \lim_{n\to\infty}u^{n}=e^{\lim_{n\to\infty}(u-1)} $”

解 这是 “1” 型未定式，是幂指函数的极限，如果  $ \lim_{x\to0}u^x $ 属于 “1” 型，则有一个重要且简单的计算方法： $ \lim_{x\to0}u^x = e^{\lim_{x\to0}(u-1)v} $。→这类问题不用凑重要极限  $ \lim_{x\to0}(1+x)^{\frac{1}{x}} = e $，用这个公式解决更快。

推导如下：利用第二重要极限公式  $ \lim_{x\to\infty}\left(1+\frac{1}{x}\right)^x=e $ ，得

 $$ \lim u^{\nu}=\lim\left\{\left[1+\left(u-1\right)\right]^{\frac{1}{u-1}}\right\}^{(u-1)\nu}=e^{\lim\left(u-1\right)\nu}, $$ 

故

 $$ \begin{aligned} 原式 &=\exp\left\{\lim_{x\to0}\frac{\mathrm{e}}{x}\left(\frac{\mathrm{e}^{x}+\mathrm{e}^{2x}+\mathrm{e}^{3x}}{3}-1\right)\right\}=\exp\left\{\lim_{x\to0}\frac{\mathrm{e}}{3}\left(\frac{\mathrm{e}^{x}-1}{x}+\frac{\mathrm{e}^{2x}-1}{x}+\frac{\mathrm{e}^{3x}-1}{x}\right)\right\}\\&=\exp\left\{\frac{\mathrm{e}}{3}\left(\lim_{x\to0}\frac{\mathrm{e}^{x}-1}{x}+\lim_{x\to0}\frac{\mathrm{e}^{2x}-1}{x}+\lim_{x\to0}\frac{\mathrm{e}^{3x}-1}{x}\right)\right\}=\mathrm{e}^{\frac{\mathrm{e}}{3}(1+2+3)}=\mathrm{e}^{2\mathrm{e}}.\end{aligned} $$ 

注 整体“抄”，不要只算指数部分  $ \lim_{n\to\infty}v(x)[u(x)-1] $，免得忘记！

(5) 泰勒公式.

泰勒公式是极为重要的，它在处理“ $ \frac{0}{0} $”型未定式时，很好用.

★例1.34 设当 $ x \to 0 $时， $ e^x - (ax^2 + bx + 1) $是比 $ x^2 $高阶的无穷小，则（）.

(A)  $ a = \frac{1}{2} $,  $ b = 1 $

(B)  $ a = 1 $,  $ b = 1 $

(C)  $ a = -\frac{1}{2} $,  $ b = -1 $

(D)  $ a = -1 $,  $ b = 1 $

♡ 分析 在无穷小比阶相关问题中，可优先考虑“泰勒公式”。

解 应选(A).