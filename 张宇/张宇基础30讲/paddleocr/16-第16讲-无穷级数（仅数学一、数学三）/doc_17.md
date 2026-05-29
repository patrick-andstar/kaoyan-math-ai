特殊的任意项级数

特别地，若 $ \underline{\text{交错级数}} $ $ \sum_{n=1}^{\infty}(-1)^{n-1}u_{n}(u_{n}>0) $条件收敛，则 $ \sum_{n=1}^{\infty}u_{2n-1} $（全体正项构成的级数）和 $ \sum_{n=1}^{\infty}(-u_{2n}) $（全体负项构成的级数）都发散，此时自然也有 $ \sum_{n=1}^{\infty}u_{2n} $发散．

(2) 若  $ \sum_{n=1}^{\infty}u_{n} $， $ \sum_{n=1}^{\infty}v_{n} $ 均绝对收敛，则  $ \sum_{n=1}^{\infty}(u_{n} \pm v_{n}) $ 绝对收敛。绝对收敛级数加加减减还是绝对收敛

证 因为  $ \sum_{n=1}^{\infty}u_{n},\sum_{n=1}^{\infty}v_{n} $ 均绝对收敛，且  $ 0\leqslant|u_{n}\pm v_{n}|\leqslant|u_{n}|+|v_{n}| $，所以  $ \sum_{n=1}^{\infty}(u_{n}\pm v_{n}) $ 绝对收敛.

(3) 若  $ \sum_{n=1}^{\infty}u_{n} $ 绝对收敛， $ \sum_{n=1}^{\infty}v_{n} $ 条件收敛，则  $ \sum_{n=1}^{\infty}(u_{n} \pm v_{n}) $ 条件收敛.

证 假设  $ \sum_{n=1}^{\infty}(u_n \pm v_n) $ 绝对收敛，而  $ \sum_{n=1}^{\infty} u_n $ 绝对收敛，那么  $ \sum_{n=1}^{\infty} v_n $ 必绝对收敛，这与  $ \sum_{n=1}^{\infty} v_n $ 条件收敛矛盾，所以  $ \sum_{n=1}^{\infty}(u_n \pm v_n) $ 条件收敛。两个收敛参数的加减减肯定是收敛的，所以只需要否定绝对收敛就可以了。

(4) 若  $ \sum_{n=1}^{\infty}u_{n} $， $ \sum_{n=1}^{\infty}v_{n} $ 均条件收敛，则  $ \sum_{n=1}^{\infty}(u_{n} \pm v_{n}) $ 收敛（可能绝对收敛，也可能条件收敛）。

 $$ \begin{cases}n=2k+1\Rightarrow\left|\frac{1}{n^{2}}-(-1)^{n}\frac{1}{n}\right|=\frac{1}{n}+\frac{1}{n^{2}},\\n=2k\Rightarrow\left|\frac{1}{n^{2}}-(-1)^{n}\frac{1}{n}\right|=\frac{1}{n}-\frac{1}{n^{2}},\end{cases} 故 $$ 

极端例子比如取 $ v_{n}=-u_{n} $， $ \sum_{n=1}^{\infty}(u_{n}+v_{n})=\sum_{n=1}^{\infty}(u_{n}-u_{n})=0 $

 $$ v_{n}=u_{n} $$ 

 $$ \sum_{n=1}^{\infty}(u_{n}+v_{n})=\sum_{n=1}^{\infty}(u_{n}+u_{n})=2\sum_{n=1}^{\infty}u_{n} $$ 

 $$ \begin{aligned}\sum_{n=1}^{\infty}\left|\frac{1}{n^{2}}-(-1)^{n}\frac{1}{n}\right|&=\sum_{n=1}^{\infty}\left[\frac{1}{n}+(-1)^{n+1}\frac{1}{n^{2}}\right]\\&=\sum_{n=1}^{\infty}\frac{1}{n}+\sum_{n=1}^{\infty}(-1)^{n+1}\frac{1}{n^{2}}\\&( 发散 + 收敛 = 发散 )\end{aligned} $$ 

 $ \sum_{n=1}^{\infty}(u_{n}\pm v_{n}) $ 可能绝对收敛，如  $ \sum_{n=1}^{\infty}u_{n}=\sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n},\quad\sum_{n=1}^{\infty}v_{n}=\sum_{n=1}^{\infty}\left[\frac{1}{n^{2}}-(-1)^{n}\frac{1}{n}\right] $ 均是条件收敛，而  $ \sum_{n=1}^{\infty}(u_{n}+v_{n})=\sum_{n=1}^{\infty}\frac{1}{n^{2}} $ 绝对收敛；

 $ \sum_{n=1}^{\infty}(u_n \pm v_n) $ 也可能条件收敛，如  $ \sum_{n=1}^{\infty} u_n = \sum_{n=1}^{\infty} (-1)^n \frac{1}{n} $， $ \sum_{n=1}^{\infty} v_n = \sum_{n=1}^{\infty} (-1)^n \frac{1}{\sqrt{n}} $ 均是条件收敛，而  $ \sum_{n=1}^{\infty}(u_n + v_n) = \sum_{n=1}^{\infty} (-1)^n \left( \frac{1}{n} + \frac{1}{\sqrt{n}} \right) $ 条件收敛。