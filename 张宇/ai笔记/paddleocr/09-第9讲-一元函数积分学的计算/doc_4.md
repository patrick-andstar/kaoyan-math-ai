 $$ \frac{2}{3}\int\frac{\mathrm{d}\left(\frac{1}{2}x^{\frac{3}{2}}\right)}{\sqrt{1-\left(\frac{1}{2}x^{\frac{3}{2}}\right)^{2}}}=\frac{2}{3}\arcsin\left(\frac{1}{2}x^{\frac{3}{2}}\right)+C $$ 

例 9.2 求不定积分  $ \int e^{\frac{\sin\theta}{\cos\theta+\sin\theta}}\cdot\frac{1}{(\cos\theta+\sin\theta)^{2}}d\theta $。（真题中大题最后一步）

♣分析 若不是常用的凑微分公式，则可对被积函数的复杂部分 $ g(x) $求导，若 $ g'(x)=f(x) $，即 $ \mathrm{d}[g(x)]=f(x)\mathrm{d}x $，则 $ \int f(x)g(x)\mathrm{d}x=\int g(x)\mathrm{d}[g(x)] $，凑微分成功。

解 对复杂部分求导：

 $$ \left(\frac{\sin\theta}{\cos\theta+\sin\theta}\right)^{\prime}=\frac{\cos\theta(\cos\theta+\sin\theta)-\sin\theta(-\sin\theta+\cos\theta)}{(\cos\theta+\sin\theta)^{2}}=\frac{1}{(\cos\theta+\sin\theta)^{2}}, $$ 

故

 $$ \mathrm{d}\left(\frac{\sin\theta}{\cos\theta+\sin\theta}\right)=\frac{1}{\left(\cos\theta+\sin\theta\right)^{2}}\mathrm{d}\theta, $$ 

于是

 $$  原式 =\int\limits_{f[g(x)]}^{\frac{\sin\theta}{\cos\theta+\sin\theta}}\mathrm{d}\left(\frac{\sin\theta}{\cos\theta+\sin\theta}\right)=\mathrm{e}^{\frac{\sin\theta}{\cos\theta+\sin\theta}}+C. $$ 

## 2 换元法

(1) 基本思想.

 $$ \int\limits_{|}f(x)\mathrm{d}x\xlongequal{x=g(u)}\int f[g(u)]\mathrm{d}[g(u)]=\int f[g(u)]g^{\prime}(u)\mathrm{d}u. $$ 

本质： $ f(x) $ 比较复杂，如  $ \sqrt{x} $， $ \sqrt{e^{x}+1} $， $ \sqrt{\frac{2x+1}{x+1}} $， $ \frac{1}{\sqrt{e^{2x}+1}} $。

引入新的自变量u，将原式化简为 $ \int h(u)du $，可代入公式

注 (1) 当被积函数不容易积分 (比如含有根式或含有反三角函数) 时，可以通过换元的方法从 d 后面拿出一部分放到前面来，就成为  $ \int f[g(u)]g'(u)du $ 的形式，若  $ f[g(u)]g'(u) $ 容易积分，则换元成功。

(2)  $ x = g(u) $ 须是单调可导函数，且不要忘记计算结束后用反函数  $ u = g^{-1}(x) $ 回代。

(2) 常用换元法.

①三角函数代换——当被积函数含有如下根式时，可作三角函数代换，这里a>0