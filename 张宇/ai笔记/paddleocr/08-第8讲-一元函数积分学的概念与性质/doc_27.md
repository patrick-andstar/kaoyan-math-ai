 $ x^{a}+x^{b}\sim x^{b} $，于是 $ I_{1} $与 $ \int_{0}^{1}\frac{1}{x^{b}}dx $同敛散，则b<1

对于  $ I_{2} $，盯着  $ x \to +\infty $ 看，由于 a > b > 0，因此  $ x^{a} $ 趋于  $ +\infty $ 的“速度”快于  $ x^{b} $ 趋于  $ +\infty $ 的“速度”， $ x^{a} + x^{b} $ 与  $ x^{a} $ 为等价无穷大量，于是  $ I_{2} $ 与  $ \int_{1}^{+\infty} \frac{1}{x^{a}} dx $ 同敛散，则 a > 1。

综上，a>1 且 b<1，故选(B).

例8.16 若反常积分  $ \int_{1}^{+\infty}\left(e^{-\cos\frac{1}{x}}-e^{-1}\right)x^{k}dx $ 收敛，则 k 的取值范围是 ___.

解 应填 k<1

盯着  $ x \rightarrow +\infty $ 看，由  $ e^{-\cos\frac{1}{x}} - e^{-1} = e^{-1} \left( e^{-\cos\frac{1}{x} + 1} - 1 \right) $，又当  $ x \rightarrow +\infty $ 时，

 $$ \mathrm{e}^{-\cos\frac{1}{x}+1}-1\sim1-\cos\frac{1}{x}\sim\frac{1}{2}\cdot\frac{1}{x^{2}}, $$ 

故原反常积分与 $ \int_{1}^{+\infty}\frac{1}{x^{2-k}}dx $同敛散，故当2-k>1，即k<1时，原反常积分收敛.

### 例8.17 以下反常积分发散的是（）

例8.17 以下反常积分发散的是（）.

(A)  $ \int_{1}^{+\infty}\left[\ln\left(1+\frac{1}{x}\right)-\frac{1}{1+x}\right]dx $ (B)  $ \int_{0}^{+\infty}\frac{\ln x}{1+x^{2}}dx $ (C)  $ \int_{-1}^{1}\frac{dx}{\sin x} $ (D)  $ \int_{-\infty}^{+\infty}\frac{\sin x}{1+x^{2}}dx $

解 应选(C).

对于(A)，对  $ x \in [1, +\infty) $，有

 $ 0 < \ln\left(1 + \frac{1}{x}\right) - \frac{1}{1 + x} < \frac{1}{x} - \frac{1}{x + 1} = \frac{1}{x(x + 1)} < \frac{1}{x^2} $.

由 $ \int_{1}^{+\infty}\frac{1}{x^{2}}dx $收敛，可知 $ \int_{1}^{+\infty}\left[\ln\left(1+\frac{1}{x}\right)-\frac{1}{1+x}\right]dx $收敛.

对于(B)， $ \int_{0}^{+\infty}\frac{\ln x}{1+x^{2}}dx=\int_{0}^{1}\frac{\ln x}{1+x^{2}}dx+\int_{1}^{+\infty}\frac{\ln x}{1+x^{2}}dx $。当 $ x\to+\infty $时， $ \lim_{x\to+\infty}\frac{\frac{\ln x}{1+x^{2}}}{\frac{\ln x}{x^{2}}}=1 $。

因为

故 $ \int_{1}^{+\infty}\frac{\ln x}{1+x^{2}}dx $ 敛散性与 $ \int_{1}^{+\infty}\frac{\ln x}{x^{2}}dx $ 相同，此式收敛，则 $ \int_{1}^{+\infty}\frac{\ln x}{1+x^{2}}dx $ 收敛

且反常积分  $ \int_{0}^{1} \ln x \, dx $ 收敛，所以反常积分  $ \int_{0}^{1} \frac{\ln x}{1 + x^{2}} \, dx $ 收敛．

又因为  $ \lim_{x\to0^{+}}\frac{\ln x}{\frac{1}{\sqrt{x}}}=\lim_{x\to0^{+}}\sqrt{x}\ln x=0 $ ，而  $ \int_{0}^{1}\frac{1}{\sqrt{x}}dx $ 收敛，故  $ \int_{0}^{1}\ln xdx $ 收敛.