以上例子说明 $ f(x) $在一点处连续，并不意味着 $ f(x) $在这点的附近连续.

例 2.8 求  $ \lim_{n\to\infty}\sqrt[n]{\left(\cos\frac{1}{\sqrt{n}}\right)^{n^2}} $

♡分析 “ $ 1^\infty $” 型极限，使用等价代换  $ u^v \sim e^{v(u-1)} $

解  $ \lim_{n\to\infty}\sqrt[n]{\left(\cos\frac{1}{\sqrt{n}}\right)^{n^{2}}}=\lim_{n\to\infty}\left(\cos\frac{1}{\sqrt{n}}\right)^{n}=\mathrm{e}^{\lim_{n\to\infty}n\ln\left(\cos\frac{1}{\sqrt{n}}\right)} $

因

 $$ \begin{aligned}\lim_{x\rightarrow+\infty}x\ln\left(\cos\frac{1}{\sqrt{x}}\right)&=\lim_{x\rightarrow+\infty}x\ln\left(1+\cos\frac{1}{\sqrt{x}}-1\right)\\&=\lim_{x\rightarrow+\infty}x\left(\cos\frac{1}{\sqrt{x}}-1\right)\\&=\lim_{x\rightarrow+\infty}x\bullet\left[-\frac{1}{2}\left(\frac{1}{\sqrt{x}}\right)^{2}\right]=-\frac{1}{2},\end{aligned} $$ 

故由归结原则知， $ \lim_{n\to\infty}n\ln\left(\cos\frac{1}{\sqrt{n}}\right)=-\frac{1}{2} $，即原式 $ e^{-\frac{1}{2}} $

注 当  $ n \to \infty $ 时，若  $ \left(1 + \frac{1}{n}\right)^n - e $ 与  $ \frac{a}{n} $ 是等价无穷小，则  $ a = -\frac{e}{2} $

解 由例 1.24 知， $ \left(1+x\right)^{\frac{1}{x}}-e\sim-\frac{e}{2}x(x\rightarrow0^{+}) $.  $ \rightarrow\left(1+\frac{1}{n}\right)^{n}-e\sim-\frac{e}{2}\cdot\frac{1}{n}(n\rightarrow\infty) $

 $ 0^{+} \leftarrow x = \frac{1}{n} $.  $ \rightarrow $ 这里x相当于 $ \frac{1}{n} $，当 $ n \rightarrow \infty $时， $ x \rightarrow 0^{+} $

## 6 夹逼准则

如果数列  $ \{x_{n}\} $， $ \{y_{n}\} $ 及  $ \{z_{n}\} $ 满足下列条件：

①从某项起，即存在  $ n_{0} \in \mathbb{N}_{+} $，当  $ n > n_{0} $ 时， $ y_{n} \leqslant x_{n} \leqslant z_{n} $;

②  $ \lim_{n\to\infty}y_n=a,\lim_{n\to\infty}z_n=a $

 $$ \begin{aligned}& 号 \quad\begin{aligned}\\ &\quad\begin{aligned}\\ &\leqslant&&\quad\searrow&<\\&\quad<&&\quad<&\\&y_{n}&\leqslant&x_{n}&\leqslant&z_{n}\\&n\rightarrow\infty&\downarrow&<&\downarrow&\leqslant&\downarrow\\&a&\Rightarrow&a&\Leftarrow&a\\&\quad(+∞)&\quad(+∞)&\quad(+∞)\\&\quad(-∞)&\quad(-∞)&\quad(-∞)\\ &\end{aligned}\\ &\end{aligned}\\ \end{aligned} $$ 

则数列  $ \left\{x_{n}\right\} $ 的极限存在，且  $ \lim_{n\to\infty}x_{n}=a $

注 放缩的常用方法如下.  $ \left\{\begin{array}{l} 已知方法:  \\  未知方法（题设给出） \end{array}\right. $

(1) 利用简单的放大与缩小.