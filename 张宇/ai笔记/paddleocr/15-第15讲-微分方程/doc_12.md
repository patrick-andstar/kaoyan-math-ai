②若 $ p^{2}-4q=0 $，设 $ r_{1},r_{2} $是特征方程的两个相等的实根，即二重根，令 $ r_{1}=r_{2}=r $，可得其通解为

 $$ y=(C_{1}+C_{2}x)\mathrm{e}^{rx}\cdot\frac{\mathrm{e}^{rx}}{x\mathrm{e}^{rx}}\neq 常数 $$ 

③若 $ p^{2}-4q<0 $，设 $ \alpha\pm\beta i $是特征方程的一对共轭复根，可得其通解为

 $$ y=e^{\alpha x}(C_{1}\cos\beta x+C_{2}\sin\beta x)\cdot\frac{e^{\alpha x}\cos\beta x}{e^{\alpha x}\sin\beta x}\neq 常数 $$ 

注 $ ^{(1)} $若解中含有 $ e^{n} $，则

当  $ r > 0 $ 时， $ e^{rx} $ 在  $ x \to +\infty $ 时无界；

当  $ r < 0 $ 时， $ e^{r\pi} $ 在  $ x \to -\infty $ 时无界。

(2) 由于  $ \cos\beta x $ 与  $ \sin\beta x $ 有周期性，因此若解具有周期性，则  $ e^{\alpha x}=1 $，即  $ \alpha=0 $

此外， $ \cos\beta x $ 与  $ \sin\beta x $ 均有界.

例 15.15 设函数  $ y = y(x) $ 是微分方程  $ y'' + y' - 2y = 0 $ 的解，且在 x = 0 处  $ y(x) $ 取得极值 3，则  $ y(x) = $ ___。

解 应填  $ e^{-2x} + 2e^{x} $.

这是二阶常系数齐次线性微分方程，其特征方程为

 $$ r^{2}+r-2=0, $$ 

可知特征根为 $ r_{1}=-2,\quad r_{2}=1 $，故通解为 $ y(x)=C_{1}e^{-2x}+C_{2}e^{x} $

由于在x=0处 $ y(x) $取得极值3，可知 $ y(0)=C_{1}+C_{2}=3 $，且

 $$ y^{\prime}(x)=-2C_{1}\mathrm{e}^{-2x}+C_{2}\mathrm{e}^{x},\ y^{\prime}(0)=-2C_{1}+C_{2}=0, $$ 

因此  $ C_{1}=1,\quad C_{2}=2 $ 。故  $ y(x)=\mathrm{e}^{-2x}+2\mathrm{e}^{x} $ 。

例 15.16 设函数  $ y = f(x) $ 满足微分方程  $ y'' + 2y' + 5y = 0 $，且  $ f(0) = 1 $， $ f'(0) = -1 $，则  $ f(x) = $ ___.

解 应填  $ e^{-x} \cos 2x $

 $$ \begin{aligned}&\rightarrow r_{1,2}=\frac{-2\pm\sqrt{2^{2}-4\times5}}{2}=-1\pm2i\end{aligned} $$ 

特征方程为  $ r^{2}+2r+5=0 $,  $ r_{1,2}=-1\pm2i $，故通解为

 $$ y=C_{1}\mathrm{e}^{-x}\cos2x+C_{2}\mathrm{e}^{-x}\sin2x, $$ 

由 $ f(0)=1 $， $ f'(0)=-1 $，得 $ C_{1}=1 $， $ C_{2}=0 $，即 $ f(x)=\mathrm{e}^{-x}\cos 2x $．