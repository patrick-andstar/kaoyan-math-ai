例1.36 已知 $ f(x)=\begin{cases}(\cos x)^{x-2},&x\neq0,\\a,&x=0\end{cases} $，在x=0处连续，则 $ a= $___。

分析  $ \lim_{x\to x_0}f(x)=f(x_0)\Leftrightarrow f(x) $ 在  $ x_0 $ 处连续.

解 应填  $ e^{-\frac{1}{2}} $

 $ \lim_{x\to0}f(x)=\lim_{x\to0}(\cos x)^{x^{-2}}=\lim_{x\to0}e^{x} $，式中 $ A=\lim_{x\to0}\frac{\cos x-1}{x^{2}}=-\frac{1}{2} $，故 $ \lim_{x\to0}f(x)=\mathrm{e}^{-\frac{1}{2}} $。

又 $ f(x) $在x=0处连续，所以 $ a=\lim_{x\to0}f(x)=\mathrm{e}^{-\frac{1}{2}} $.

方法总结 计算  $ \lim_{x\to x_{0}}f(x) $ 即可.

∅公式  $ \lim_{n\to\infty}u(x)^{\nu(x)} = e^{\lim_{n\to\infty}\nu(x)[u(x)-1]} $

例 1.37 函数  $ f(x)=\frac{\mathrm{e}^{\frac{1}{x-1}}\ln\left|1+x\right|}{(\mathrm{e}^{x}-1)(x-2)} $ 的第二类间断点的个数为（ ）.

(A) 1          (B) 2          (C) 3          (D) 4

分析 找无定义点和分段函数的分界点，求  $ \lim_{x\to x_0}f(x) $，进而判断间断点类型.

解 应选(C).

本题考查初等函数的连续性、间断点、间断点分类等基本概念，考查利用等价无穷小替换及洛必达法则求极限的方法，是一道考查基本概念和简单运算的题目.

 $ f(x) $ 的定义域为  $ \left\{x \mid x \in (-\infty, +\infty), x \neq -1, x \neq 0, x \neq 1, x \neq 2\right\} $，而初等函数在定义域内是连续的，所以该函数的所有间断点是 -1, 0, 1, 2. 由于

 $$ \lim_{x\to-1}f(x)=\lim_{x\to-1}\frac{\mathrm{e}^{\frac{1}{x-1}}\ln\left|1+x\right|}{(\mathrm{e}^{x}-1)(x-2)}=-\infty, $$ 

 $$ \lim_{x\to2}f(x)=\lim_{x\to2}\frac{\mathrm{e}^{\frac{1}{x-1}}\ln\left|1+x\right|}{(\mathrm{e}^{x}-1)(x-2)}=\infty, $$ 

由例 1.15 知，

 $$ \lim_{x\to1^{+}}f(x)=+\infty, $$ 

 $$ \lim_{x\to0}f(x)=\lim_{x\to0}\frac{\mathrm{e}^{\frac{1}{x-1}}\ln\left|1+x\right|}{(\mathrm{e}^{x}-1)(x-2)}=-\frac{1}{2\mathrm{e}}\lim_{x\to0}\frac{\ln(1+x)}{\mathrm{e}^{x}-1}=-\frac{1}{2\mathrm{e}}, $$ 

因此 x=0 是函数的可去间断点，而其余 3 个点均为函数的第二类间断点，故选 (C).

☑ 方法总结 间断点找无定义点和分段函数的分界点.

公式  $ e^{\infty} $ 要分  $ e^{+\infty} $， $ e^{-\infty} $