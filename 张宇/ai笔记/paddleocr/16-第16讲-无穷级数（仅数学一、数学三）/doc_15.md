解 令  $ f(x)=\frac{1}{\sqrt{x}-\ln x} $，由于  $ \lim_{x\to+\infty}f(x)=\lim_{x\to+\infty}\frac{1}{\sqrt{x}-\ln x}=0 $，且

 $$ f^{\prime}(x)=\frac{-\left(\frac{1}{2\sqrt{x}}-\frac{1}{x}\right)}{\left(\sqrt{x}-\ln x\right)^{2}}=\frac{-\left(\sqrt{x}-2\right)}{2x\left(\sqrt{x}-\ln x\right)^{2}}<0(x>4), $$ 

故由莱布尼茨判别法知，原级数收敛。

例16.16 判别级数  $ \sum_{n=2}^{\infty}\frac{(-1)^{n}}{\sqrt{n}+(-1)^{n}} $ 的敛散性.

(2) 分析）令  $ u_n = \frac{1}{\sqrt{n} + (-1)^n} $，则  $ u_{2k} = \frac{1}{\sqrt{2k} + 1} $， $ u_{2k+1} = \frac{1}{\sqrt{2k + 1} - 1} $，分别单调递减，但  $ \sqrt{2k + 1} - 1 - \sqrt{2k} - 1 = \frac{1}{\sqrt{2k + 1} + \sqrt{2k}} - 2 < 0 $，故  $ \sqrt{2k + 1} - 1 < \sqrt{2k} + 1 $，可得  $ u_{2k} < u_{2k+1} $。故  $ \{u_n\} $ 不单调，莱布尼茨判别法失效，故拆项处理。

解 一般项  $ \frac{(-1)^n}{\sqrt{n}+(-1)^n}=\frac{(-1)^n[\sqrt{n}-(-1)^n]}{n-1}=(-1)^n\frac{\sqrt{n}}{n-1}-\frac{1}{n-1} $，其中  $ \sum_{n=2}^{\infty}(-1)^n\frac{\sqrt{n}}{n-1} $ 是交错级数，显然  $ u_n=\frac{\sqrt{n}}{n-1}\to0(n\to\infty) $。令  $ f(x)=\frac{\sqrt{x}}{x-1} $，则  $ f'(x)=\frac{\frac{1}{2\sqrt{x}}(x-1)-\sqrt{x}}{(x-1)^2}=\frac{-1-x}{2\sqrt{x}(x-1)^2}<0(x\geq2) $，于是  $ \sum_{n=2}^{\infty}(-1)^n\frac{\sqrt{n}}{n-1} $ 收敛，但  $ \sum_{n=2}^{\infty}\frac{1}{n-1} $ 发散，故原级数发散。

注 此题  $ \left\{u_{n}=\frac{1}{\sqrt{n}+(-1)^{n}}\right\} $ 是不单调的，将原级数“拆”开，瓦解敌人，各个击破，不失为好的办法.

## 3 任意项级数及其敛散性判别（绝对值判别法）

若级数各项可正、可负、亦可为零，则称这样的级数为任意项级数，写为  $ \sum_{n=1}^{\infty}u_{n} $ 。任意项级数是按下述方式研究敛散性的。

给任意项级数的每一项加上绝对值，写成  $ \sum_{n=1}^{\infty}|u_{n}| $，这样就使得  $ |u_{n}|\geq0 $ 成了正项级数，它叫作原级数。这样的转化是很有意义的，因为正项级数我们研究得很透彻，不会出现正负相间的情况。

绝对值级数就自然站到了正项级数的队伍中，前面讲过的六种正项级数的敛散性判别法均可派上用场了。绝对值级数  $ \sum_{n=1}^{\infty}|u_n| $ 与原级数  $ \sum_{n=1}^{\infty}u_n $ 的敛散性有何关系呢？看下面的定义。