妨设  $ a < b < c $），分别在  $ [a, b] $， $ [b, c] $ 上使用罗尔定理，有  $ f'(\xi_1) = f'(\xi_2) = 0 $， $ \xi_1 \in (a, b) $， $ \xi_2 \in (b, c) $，进而在  $ [\xi_1, \xi_2] $ 上再对  $ f'(x) $ 使用罗尔定理，得  $ f''(\xi) = 0 $，其中  $ \xi \in (\xi_1, \xi_2) \subset (a, c) $。如例 6.6.

<div style="text-align: center;"><img src="imgs/img_in_image_box_360_251_629_317.jpg" alt="Image" width="26%" /></div>


 $$  由 F^{\prime}(\xi_{1})=F^{\prime}(\xi_{2})=0, 得 F^{\prime \prime}(\xi)=0 $$ 

例 6.6 设函数  $ f(x) $ 在  $ [0,1] $ 上连续，在  $ (0,1) $ 内二阶可导，过点  $ A(0,f(0)) $ 与点  $ B(1,f(1)) $ 的直线与曲线  $ y = f(x) $ 相交于点  $ C(c,f(c)) $，其中  $ 0 < c < 1 $，证明：存在  $ \xi \in (0,1) $，使得  $ f''(\xi) = 0 $。

证 根据题意，过点 A 与点 B 的直线方程为  $ y_{1}=[f(1)-f(0)]x+f(0) $.

令 $ F(x)=f(x)-y_1=f(x)-\left[f(1)-f(0)\right]x-f(0) $，又 $ f(c)=\left[f(1)-f(0)\right]\cdot c+f(0) $，且 $ F(0)=0 $， $ F(1)=0 $， $ F(c)=f(c)-\left[f(1)-f(0)\right]\cdot c-f(0)=0 $，则 $ F(x) $在 $ [0,c] $与 $ [c,1] $上均满足罗尔定理的条件，于是可得 $ F'(\xi_1)=F'(\xi_2)=0 $， $ \xi_1\in(0,c) $， $ \xi_2\in(c,1) $。因为 $ F(x) $有三个零点 $ \frac{1}{0} $， $ \frac{1}{c} $， $ \frac{1}{1} $， $ \frac{1}{x} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_742_581_881_640.jpg" alt="Image" width="13%" /></div>


再由罗尔定理可得  $ F''(\xi) = f''(\xi) = 0, \quad \xi \in (\xi_1, \xi_2) \subset (0, 1) $，命题得证。

公式 直线方程  $ y_{1}-f(0)=\frac{f(1)-f(0)}{1-0}(x-0) $.

注大于等于2阶为高阶.

若证 $ f^{(n)}(\xi)=0 $用罗尔定理可能性大；

若证 $ f^{(n)}(\xi)\neq0 $（不等式）用泰勒公式可能性大。

例 6.7 设函数  $ f(x) $ 在区间  $ [0,1] $ 上具有二阶导数，且  $ f(1)>0 $， $ \lim_{x\to0^{+}}\frac{f(x)}{x}<0 $ 。证明：方程  $ f(x)f''(x)+\left[f'(x)\right]^2=0 $ 在区间  $ (0,1) $ 内至少存在两个不同实根。

♡分析 辅助函数为  $ F(x)=f(x)\cdot f'(x) $，即证  $ \begin{cases}F'(\xi_{1})=0,\\F'(\xi_{2})=0,\end{cases} $ 其中  $ \xi_{1} $ 与  $ \xi_{2} $ 不相等.

证 由题设知 $ f(x) $连续且 $ \lim_{x\to0^{+}}\frac{f(x)}{x} $存在，所以 $ f(0)=0 $．又由例6.2知 $ f(b)=0,\quad b\in(0,1) $，由罗尔定理知，存在 $ c\in(0,b)\subset(0,1) $，使得

 $$ f^{\prime}(c)=0. $$ 

令  $ F(x)=f(x)f'(x) $，由题设知  $ F(x) $ 在区间  $ [0,b] $ 上可导，且

 $ F(0)=0,\quad F(c)=0,\quad F(b)=0. $  $ \rightarrow $ 由  $ f'(c)=0 $ 得到

根据罗尔定理，存在  $ \xi \in (0, c) $， $ \eta \in (c, b) $，使得  $ F'(\xi) = F'(\eta) = 0 $，即  $ \xi $， $ \eta $ 是方程  $ f(x)f''(x) + [f'(x)]^2 = 0 $ 在区间  $ (0, 1) $ 内的两个不同实根。