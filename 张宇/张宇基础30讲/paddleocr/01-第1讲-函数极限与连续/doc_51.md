 $$ \begin{aligned}&\left\{\begin{aligned}x_{n}\cos x_{n+1}&=\sin x_{n},\\ &\cos x_{n+1}\end{aligned}\right.\rightarrow\cos x_{n+1}=\frac{\sin x_{n}-\sin0}{x_{n}-0}=\cos\xi\Rightarrow0<\xi<x_{n}\\ &\\ &\cos a_{n}-a_{n}=\cos b_{n}.\\ &\left.\begin{aligned}\cos a_{n}-\cos b_{n}&=a_{n}>0,0<a_{n},b_{n}<\frac{\pi}{2},\\ &\quad\downarrow\quad\downarrow\quad\downarrow\\ &\quad\downarrow\quad\downarrow\quad\downarrow\\ &\quad\downarrow\quad\downarrow\quad\downarrow\\ &\quad\downarrow\quad\downarrow\quad\downarrow\\ &\end{aligned}\right.\\ \end{aligned} $$ 

如：

逼近到0

数学题的最高境界就是那些最简单的地方，不是庞然大物或者是用非常复杂的技巧。大道至简才是考研数学的本质。

这种题是考研的压轴题，但是大家也不要急.在命题老师眼里，他给的东西，他想的东西最简单，最朴素的 $ \cos x $在 $ \left(0,\ \frac{\pi}{2}\right) $内递减，一个中学生也知道啊！但几百万考生，大部分考生都没想到.

而且命题老师又说“不定积分”大家少做啊！因为在命题老师的知识体系中，他是深刻知道世界上能做出来的积分是寥寥无几的，世界上不能做出的积分，多得想象不到。再换句话说，几乎不定积分都没法做，那我们就把他喜欢出的那几个思想、方法掌握了，最基本的东西把握好了，那么考试就成功了，这就叫方向，不做无用功。

① $ \frac{A}{B} $型，适用“上下同阶”原则.

具体说来，如果分母(或分子)是x的k次幂，则应把分子(或分母)展开到x的k次幂，可称为“上下同阶”原则。

例如，计算 $ \lim_{x\to0}\frac{x-\ln(1+x)}{x^{2}} $

由于

 $$ \begin{aligned}&\text{↔不破 }\\ &\ln(1+x)=x+o(x),\ln(1+x)=x-\frac{x^{2}}{2}+o(x^{2}),\\ \end{aligned} $$ 

 $$ \ln(1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{3}+o(x^{3}), $$ 

因此

 $$ \lim_{x\to0}\frac{x-\ln(1+x)}{x^{2}}=\lim_{x\to0}\frac{x-\left[x-\frac{x^{2}}{2}+o(x^{2})\right]}{x^{2}}=\lim_{x\to0}\frac{\frac{x^{2}}{2}}{x^{2}}=\frac{1}{2} $$ 

这里顺便得到了一个重要的等价代换式  $ x - \ln(1 + x) \sim \frac{1}{2} x^{2} (x \to 0) $.

 $$ x-\ln(1+x)\sim1-\cos x\sim\frac{1}{2}x^{2}\quad(x\rightarrow0) $$ 

同理

 $$ x-\sin x\sim\frac{x^{3}}{6}(x\rightarrow0), $$ 

 $$ \arcsin x-x\sim\frac{x^{3}}{6}(x\rightarrow0), $$ 

 $$ \tan x-x\sim\frac{x^{3}}{3}(x\rightarrow0), $$ 