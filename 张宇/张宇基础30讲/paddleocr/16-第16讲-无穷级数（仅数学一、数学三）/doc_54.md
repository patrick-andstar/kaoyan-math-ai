 $$ =\sum_{n=0}^{\infty}\left[\left(-\frac{1}{3}\right)(-1)^{n}+\frac{2^{n}}{3}\right]\frac{x^{n}}{n!}, $$ 

故  $ a_{n}=\frac{1}{3}[(-1)^{n+1}+2^{n}] $

16.17 解 令  $  S(x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{(2n-1)! 2^{2n-2}} x^{2n-1} = 2 \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{(2n-1)!} \left( \frac{x}{2} \right)^{2n-1} = 2 \sin \frac{x}{2}, -\infty < x < +\infty  $，利用三角函数公式展开，得

 $$ \begin{aligned}S(x)&=2\sin\frac{x}{2}=2\sin\frac{1+x-1}{2}=2\Bigg(\sin\frac{1}{2}\cos\frac{x-1}{2}+\cos\frac{1}{2}\sin\frac{x-1}{2}\Bigg)\\&=2\sin\frac{1}{2}\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n)!}\Bigg(\frac{x-1}{2}\Bigg)^{2n}+2\cos\frac{1}{2}\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n+1)!}\Bigg(\frac{x-1}{2}\Bigg)^{2n+1},-\infty<x<+\infty.\end{aligned} $$ 

注 本题用幂级数  $ \sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{(2n-1)!2^{2n-2}}x^{2n-1} $ 来包装函数  $ 2\sin\frac{x}{2} $，这种包装要能识别出来。