## 9 无穷大的定义

如果当 $ x \to x_0 $（或 $ x \to \infty $）时，函数 $ |f(x)| $无限增大，那么称函数 $ f(x) $为当 $ x \to x_0 $（或 $ x \to \infty $）时的无穷大，记为

同无穷小，也是一个极限过程

一定无界，但无界不一定是无穷大量

超实数

 $$ \lim_{x\to x_{0}}f(x)=\infty\quad( 或 \lim_{x\to\infty}f(x)=\infty) $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_222_360_837_543.jpg" alt="Image" width="59%" /></div>


注 无穷小与无穷大的关系.

在自变量的同一变化过程中，如果 $ f(x) $为无穷大，则 $ \frac{1}{f(x)} $为无穷小；反之，如果 $ f(x) $为无穷小，且 $ f(x)\neq0 $，则 $ \frac{1}{f(x)} $为无穷大。

用除法的新颖观点来理解“无穷”.

例1.19 设  $ x \to 0 $ 时， $ e^{\tan x} - e^{\sin x} $ 与  $ x^n $ 是同阶无穷小，则  $ n $ 为（ ）。

 $$ \frac{1}{1/2}=2\left( 次 \right),\quad1-\frac{1}{2}-\frac{1}{2}=0. $$ 

(A)1

 $$ \frac{1}{1/4}=4( 次 ),\quad1-\frac{1}{4}-\frac{1}{4}-\frac{1}{4}-\frac{1}{4}=0. $$ 

(C)3

 $$ \frac{1}{0}= 不存在：1-0-0-\cdots\neq0. $$ 

(0不能当分母)

♂分析 无穷小的比阶问题.

 $$ \lim_{x\to0^{+}}\frac{1}{x}=+\infty( 次 ),\quad1-x-x-\cdots=0 $$ 

当  $ x \to 0 $ 时， $ e^{\tan x} - e^{\sin x} = e^{\sin x} (e^{\tan x - \sin x} - 1) $ 是以 1 作为标准实数部分。这种题往往需要提出公因式。（数学中的恒等变形）

 $$ \mathbf{e}^{ 砲 }-1\sim 礻 ( 礻 \rightarrow0) $$ 

解 应选(C).

当 $ x\to0 $时，

 $$ \begin{array}{l} 现在没有讲到泰勒公式 \quad 恒等变形 \\ 式，暂时不用 \quad\leftarrow\\ \end{array} $$ 

 $$ \mathrm{e}^{\tan x}-\mathrm{e}^{\sin x}=\mathrm{e}^{\sin x}\left(\mathrm{e}^{\tan x-\sin x}-1\right)\sim\frac{1}{\tan x-\sin x}=\frac{1}{\tan x(1-\cos x)}\sim\frac{1}{2}x^{3} $$ 

因此选(C).

☑ 方法总结  $ e^{\tan x} - e^{\sin x} $，通常要提公因式出现  $ e^{\alpha} - 1 $ 的形式。

公式 当  $ x \to 0 $ 时，  $ \tan x - \sin x = \tan x (1 - \cos x) \sim \frac{1}{2} x^{3} $