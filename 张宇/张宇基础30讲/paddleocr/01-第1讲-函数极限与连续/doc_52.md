 $$ x-\arctan x\sim\frac{x^{3}}{3}(x\rightarrow0), $$ 

均可由“上下同阶”原则得到.

②A-B型，适用“幂次最低”原则. $ A+B=A-(-B) $

具体说来，即将 A, B 分别展开到它们的系数不相等的 x 的最低次幂为止.

例如，已知当 $ x\to0 $时， $ \cos x-e^{-\frac{x^{2}}{2}} $与 $ ax^{b} $为等价无穷小，求a,b.

用泰勒公式， $ \cos x=1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}+o(x^{4}) $， $ e^{-\frac{x^{2}}{2}}=1-\frac{x^{2}}{2}+\frac{1}{2!}\frac{x^{4}}{4}+o(x^{4}) $

显然，将  $ \cos x, e^{-2} $ 展开到  $ x^{4} $ 时，其系数就不一样了，使用“幂次最低”原则，展开到此项后，进行运算，得

 $$ \cos x-\mathrm{e}^{-\frac{x^{2}}{2}}=\left[1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}+o(x^{4})\right]-\left[1-\frac{x^{2}}{2}+\frac{1}{2!}\frac{x^{4}}{4}+o(x^{4})\right]=-\frac{1}{12}x^{4}+o(x^{4}), $$ 

于是可知  $ \cos x - e^{-\frac{x^{2}}{2}} \sim -\frac{1}{12} x^{4} (x \to 0) $，故  $ a = -\frac{1}{12} $，b = 4。

到此为止，整个泰勒公式就学习完了，在一般计算中，四则运算法则，洛必达法则，泰勒公式就够了，除此之外常用的，还有两个重要极限。

(6) 两个重要极限.

 $$ \lim_{x\to0}\frac{\sin x}{x}=1,\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^{x}=e\quad. $$ 

## 注 常考变量广义化

 $$ \lim_{ 狗 \to0}\frac{\sin 狗 }{ 狗 }=1,\lim_{ 狗 \to\infty}\left(1+\frac{1}{ 狗 }\right)^{ 狗 }=e $$ 

如狗 $ =\frac{1}{x} $，则上述式子为

 $ \lim_{x \to 0} \frac{\sin \frac{1}{x}}{\frac{1}{x}} = 1 $，即  $ \lim_{x \to \infty} x \sin \frac{1}{x} = 1 $，

 $ \lim_{\substack{\frac{1}{x}\to\infty\\x}}\left(1+\frac{1}{\frac{1}{x}}\right)^{\frac{1}{x}}=\mathrm{e} $，即 $ \lim_{x\to0}(1+x)^{\frac{1}{x}}=\mathrm{e} $。