由于当 $ x\to0 $时， $ 1-\cos x $与 $ \frac{1}{2}x^{2} $是等价无穷小量，即它们趋核速度相同，用趋核运算来刻画，即 $ \lim_{x\to0}\frac{1-\cos x}{\frac{1}{2}x^{2}}=1 $，故 $ \lim_{x\to0}\frac{1-\cos x}{x^{2}}=\lim_{x\to0}\frac{\frac{1}{2}x^{2}}{x^{2}}\cdot1 $，这是此问题的正确来由。

1- $ \cos x $与 $ \frac{1}{2}x^{2} $趋核速度相同

显然，上述 $ \lim_{x\to0}\frac{1-\cos x}{\frac{1}{2}x^{2}}=1 $涉及“趋核速度”，需要详细说一说。

(4) 趋核速度.

既然一个核值 $ x_{0} $周围有无数个光环，这些光环的本质区别是什么呢？这就要提出“趋核速度”的问题了.

比如，如图 1-25 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_429_626_605_709.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">图 1-25</div>


 $ \sin x(x \rightarrow 0) $ 与  $ x(x \rightarrow 0) $ 均以 0 为核值，且趋核速度相同，则用下式来刻画这种关系：

 $$ \lim_{x\to0}\frac{\sin x}{x}=1 $$ 

 $ \sin x(x \rightarrow 0) $ 与  $ x(x \rightarrow 0) $ 趋缓速度相同

于是，有下面的结论：

若 $ f(x)(x\to x_0) $与 $ g(x)(x\to x_0) $均以0为核值，则 $ \lim_{x\to x_0}\frac{f(x)}{g(x)}=a\neq0\Leftrightarrow f(x)(x\to x_0) $与 $ g(x)(x\to x_0) $趋核速度相同.

 $ \lim_{x\to x_0}\frac{f(x)}{g(x)}=0\Leftrightarrow f(x)(x\to x_0) $ 比  $ g(x)(x\to x_0) $ 趋核速度快.

 $ \lim_{x\to x_0}\frac{f(x)}{g(x)}=\infty\Leftrightarrow f(x)(x\to x_0) $ 比  $ g(x)(x\to x_0) $ 趋核速度慢.

(5) 极限四则运算规则.

这也称为超实数趋核四则运算规则。

设  $ \lim_{x\to x_0}f(x)=A,\quad\lim_{x\to x_0}g(x)=B $ ，则有

 $$ \lim_{x\to x_{0}}\left[f(x)\pm g(x)\right]=A\pm B $$ 

②  $ \lim_{x\to x_0}f(x)g(x)=AB $;