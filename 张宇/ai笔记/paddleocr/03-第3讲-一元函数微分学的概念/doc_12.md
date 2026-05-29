## 3 高阶导数（重点）

函数 $ f(x) $在点 $ x_{0} $处的二阶导数为

 $$ f^{\prime \prime}(x_{0})=\lim_{\Delta x\to0}\frac{f^{\prime}(x_{0}+\Delta x)-f^{\prime}(x_{0})}{\Delta x} 或 f^{\prime \prime}(x_{0})=\lim_{x\to x_{0}}\frac{f^{\prime}(x)-f^{\prime}(x_{0})}{x-x_{0}}. $$ 

函数 $ f(x) $在点 $ x_{0} $处的 $ n(n $为大于2的整数 $ ) $阶导数为

 $$ f^{(n)}(x_{0})=\lim_{\Delta x\to0}\frac{f^{(n-1)}(x_{0}+\Delta x)-f^{(n-1)}(x_{0})}{\Delta x} 或 \left|f^{(n)}(x_{0})=\lim_{x\to x_{0}}\frac{f^{(n-1)}(x)-f^{(n-1)}(x_{0})}{x-x_{0}}\right|. $$ 

写法： $ f'(x) $， $ f''(x) $， $ f'''(x) $，当 $ n\geq4 $时，要写 $ f^{(n)}(x) $。

注 (1) 如果  $ f(x) $ 在点  $ x_{0} $ 处有二阶导数，则  $ f(x) $ 在  $ x_{0} $ 的某个邻域内有一阶导数且  $ f'(x) $ 在  $ x_{0} $ 处连续。

 $ \downarrow $

已知  $ f''(x_0) = \lim_{x \to x_0} \frac{f'(x) - f'(x_0)}{x - x_0} = a $（存在）。

则  $ \lim_{x \to x_0} [f'(x) - f'(x_0)] = \lim_{x \to x_0} \frac{f'(x) - f'(x_0)}{x - x_0} = 0 $。

 $ \Rightarrow $ 意思是从一阶导到  $ n-1 $ 阶导数都存在。

即  $ \lim_{x \to x_0} f'(x) = f'(x_0) $。故  $ f'(x) $ 在  $ x_0 $ 处连续。

(2) 如果  $ f(x) $ 在点  $ x_{0} $ 处有  $ n $ 阶导数，则  $ f(x) $ 在  $ x_{0} $ 的某个邻域内有  $ 1 \sim (n-1) $ 阶的各阶导数。

总结： $ f'(x_{0}) $ 存在  $ \Rightarrow f(x) $ 在  $ x_{0} $ 附近有定义且在  $ x_{0} $ 处连续；

 $ f''(x_{0}) $ 存在  $ \Rightarrow f'(x) $ 在  $ x_{0} $ 附近有定义且在  $ x_{0} $ 处连续；

 $ f^{(n)}(x_{0}) $ 存在  $ \Rightarrow f^{(n-1)}(x) $ 在  $ x_{0} $ 附近有定义且在  $ x_{0} $ 处连续。

例 3.9 设  $ f(x) $ 在  $ x = x_{0} $ 处二阶可导，且  $ f'(x_{0}) = 0 $， $ f''(x_{0}) \neq 0 $。证明：

(1) 若  $ f''(x_0) < 0 $，则  $ f(x) $ 在  $ x_0 $ 处取得极大值；

(2) 若  $ f''(x_0) > 0 $，则  $ f(x) $ 在  $ x_0 $ 处取得极小值。

☐ 分析 概念题.

必背公式来源：函数极限的局部保号性。

 $$ \lim_{x\to x_{0}}f(x)=A<0\xrightarrow{x\in(x_{0}-\delta,x_{0})\bigcup(x_{0},\ x_{0}+\delta)}f(x)<0. $$ 

 $$ \lim_{x\to x_{0}}f(x)=A>0\xrightarrow{x\in(x_{0}-\delta,x_{0})\bigcup(x_{0},x_{0}+\delta)}f(x)>0 $$ 

必背公式应用：

 $$ \lim_{x\to x_{0}}\frac{f^{\prime}(x)-f^{\prime}(x_{0})}{x-x_{0}}<\begin{aligned}&0\Rightarrow\frac{f^{\prime}(x)-f^{\prime}(x_{0})}{x-x_{0}}<\begin{aligned}&0\end{aligned}\\ &\end{aligned}. $$ 

证 (1) 因  $ f''(x_0) < 0 $，故按二阶导数的定义有