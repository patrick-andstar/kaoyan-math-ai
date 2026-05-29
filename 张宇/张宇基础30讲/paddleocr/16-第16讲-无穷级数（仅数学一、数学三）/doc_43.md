在x=1处， $ \sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1}x^{2n+1} $虽然收敛，但函数 $ f(x)=\arctan\frac{1+x}{1-x} $无定义，所以成立范围不能扩大到x=1。

在x=-1处， $ \sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1}x^{2n+1} $收敛，而 $ f(x)=\arctan\frac{1+x}{1-x} $在x=-1处右连续，于是

 $$ f(-1)=\lim_{x\to-1^{+}}f(x)=\lim_{x\to-1^{+}}\left[\frac{\pi}{4}+\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1}x^{2n+1}\right]=\frac{\pi}{4}+\sum_{n=0}^{\infty}\frac{(-1)^{n+1}}{2n+1} $$ 

所以有

 $$ \arctan\frac{1+x}{1-x}=\frac{\pi}{4}+\sum_{n=0}^{\infty}\frac{(-1)^{n}}{2n+1}x^{2n+1},-1\leqslant x<1 $$ 

注 (1) 展开式在收敛区间内部可以逐项求导、逐项积分，但由此得到的新的展开式在收敛区间

的端点处是否成立？要检查两点：若端点处级数收敛，并且被展开的函数在该端点单侧连续（左端点处右连续，右端点处左连续），像本例这样，则此展开式在端点处也成立，在具体做题时， $ \left(^{*}\right) $式可以不写，考试中常有涉及端点处展开式是否成立的问题，考生应按这个注的办法处理。

(2) 小结. (全背. 注意每个函数的做题标志)

①  $ \ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n-1}\cdot\frac{x^{n}}{n},-1<x\leq1 $

→  $ \left[\ln(1+x)\right]^{\prime}=\sum_{n=0}^{\infty}(-1)^{n}x^{n},-1<x<1 $

→ 分母有  $ n $ 的往  $ \ln $ 去想

②  $ \frac{1}{2}\ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n-1}\cdot\frac{x^{n}}{2n},-1<x\leq1 $

→ 分母有  $ 2n $ 的往  $ \frac{1}{2}\ln $ 去想

③  $ \arctan x = \sum_{n=0}^{\infty} (-1)^n \cdot \frac{x^{2n+1}}{2n+1}, -1 \leqslant x \leqslant 1 $  $ \rightarrow (\arctan x)' = \frac{1}{1 + x^2} = \sum_{n=0}^{\infty} (-1)^n x^{2n}, -1 < x < 1 $

 $$ (-1)^{*} $$ 

④  $ e^{x} = \sum_{n=0}^{\infty} \frac{x^{n}}{n!}, -\infty < x < +\infty. $

→ 分母上看到阶乘，如果是n!，那会不会是  $ e^{x} $

⑤  $ \frac{e^x + e^{-x}}{2} = \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!}, -\infty < x < +\infty $.

⑥  $ \cos x = \sum_{n=0}^{\infty} (-1)^n \cdot \frac{x^{2n}}{(2n)!}, -\infty < x < +\infty $. ②前面有 $ (-1) $

 $$ \frac{e^{x}+e^{-x}}{2} $$ 

⑦ $ \frac{e^x - e^{-x}}{2} = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}, -\infty < x < +\infty $.

⑧  $ \sin x = \sum_{n=0}^{\infty}(-1)^{n} \cdot \frac{x^{2n+1}}{(2n+1)!}, -\infty < x < +\infty $

 $$ \frac{e^{x}-e^{-x}}{2} $$ 

常用上述 8 个公式来考一些简单的数项级数的和，如  $ \sum_{n=0}^{\infty}\frac{1}{(2n)!}=\frac{e+e^{-1}}{2} $，再如