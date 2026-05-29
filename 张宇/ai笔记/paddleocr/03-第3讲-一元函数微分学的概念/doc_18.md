 $$ \lim_{\Delta x\to0}\frac{\Delta y-\mathrm{d}y}{\mathrm{d}y}=\lim_{\Delta x\to0}\frac{o(\Delta x)}{f^{\prime}(x_{0})\Delta x}=\lim_{\Delta x\to0}\frac{1}{f^{\prime}(x_{0})}\cdot\frac{o(\Delta x)}{\Delta x}=0, $$ 

故选(A).

3.5  $ \varphi(a) $ 分析 概念题. 有的同学用公式法求出  $ f'(a) $，但这是错误解法，

 $$ f^{\prime}(a)=f^{\prime}(x)\big|_{x=a}=\left[\varphi(x)+(x-a)\bullet\varphi^{\prime}(x)\right]\big|_{x=a}=\varphi(a)+0=\varphi(a), $$ 

错误，因为  $ \varphi(x) $ 仅连续， $ \varphi'(x) $ 不一定存在！应该用 “导数定义” 求出.

解 导数定义.

 $$ f^{\prime}(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}=\lim_{x\to a}\frac{(x-a)\cdot\varphi(x)-0}{x-a}=\lim_{x\to a}\varphi(x)=\varphi(a) $$ 

注 求导数时，当函数不具备“导数存在”的条件时，往往只能用“导数定义”求.

 $$ \begin{aligned}3.6\quad-\frac{1}{4}f^{\prime}(0)\quad 解 \quad& 原式 =\lim_{x\to0}\frac{f(1-\sqrt{\cos x})-f(0)}{(1-\sqrt{\cos x})-0}\cdot\lim_{x\to0}\frac{1-\sqrt{\cos x}}{\ln(1-x\sin x)}\\&=f^{\prime}(0)\lim_{x\to0}\frac{1-\sqrt{\cos x}}{\ln(1-x\sin x)}\\&\xlongequal{ 等价无穷小替换 }f^{\prime}(0)\lim_{x\to0}\frac{\frac{1}{2}\cdot\frac{1}{2}x^{2}}{-x\sin x}=-\frac{1}{4}f^{\prime}(0)\lim_{x\to0}\frac{x^{2}}{x^{2}}=-\frac{1}{4}f^{\prime}(0)\ .\\ \end{aligned} $$ 

3.7 证明 (1)  $ F_{+}^{\prime}(x_{0})=\lim_{x\to x_{0}^{+}}\frac{F(x)-F(x_{0})}{x-x_{0}}\xlongequal{洛必达法则}\lim_{x\to x_{0}^{+}}\frac{F^{\prime}(x)}{1}=A $

(2) $ F_{-}^{\prime}(x_{0})=\lim_{x\to x_{0}^{-}}\frac{F(x)-F(x_{0})}{x-x_{0}}\xlongequal{洛必达法则}\lim_{x\to x_{0}^{-}}\frac{F^{\prime}(x)}{1}=A $

注 满足(1)，(2)的条件时，有  $ \lim_{x\to x_0\atop(x_0)}F'(x)\xlongequal{存在}A $，则  $ F'_{+}(x_0)\xlongequal{存在}A $ 。但  $ \lim_{x\to x_0\atop(x_0)}F'(x) $ 不存在时， $ F'_{+}(x_0) $ 亦可能存在。如  $ F(x)=\begin{cases}x^2\sin\frac{1}{x},&x\neq0,\\0,&x=0.\end{cases} $

当 x=0 时， $ F'(0)=\lim_{x\to0}\frac{F(x)-F(0)}{x-0}=\lim_{x\to0}x\sin\frac{1}{x}=0. $

当  $ x \neq 0 $ 时， $ F'(x) = 2x \sin \frac{1}{x} - \cos \frac{1}{x} $， $ \lim_{x \to 0^+} F'(x) $ 不存在。但由  $ F'(0) = 0 $，知  $ F_{+}'(0) = 0 $（存在）。

3.8 解 由可导与连续的关系有

 $$ \lim_{x\to0^{-}}x^{2}\sin\frac{\pi}{x}=\lim_{x\to0^{+}}(ax^{2}+b)=A, $$ 