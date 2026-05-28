又如，计算  $ \lim_{x\to\infty}\frac{\left(1+\frac{1}{x}\right)^{x^{2}}}{e^{x}} $，若写  $ \lim_{x\to\infty}\frac{\left(1+\frac{1}{x}\right)^{x^{2}}}{e^{x}}=\lim_{x\to\infty}\frac{\left[\left(1+\frac{1}{x}\right)^{x}\right]^{x}}{e^{x}}=\lim_{x\to\infty}\frac{e^{x}}{e^{x}}=1 $，显然也是错误的。因为， $ \lim_{x\to\infty}\frac{\left(1+\frac{1}{x}\right)^{x^{2}}}{e^{x}} $ 的第一步，要作  $ \frac{\left(1+\frac{1}{x}\right)^{x^{2}}}{e^{x}} $ 的实数运算，即

 $$ \frac{\left(1+\frac{1}{x}\right)^{x^{2}}}{\mathbf{e}^{x}}=\frac{\mathbf{e}^{x^{2}\ln\left(1+\frac{1}{x}\right)}}{\mathbf{e}^{x}}=\mathbf{e}^{x^{2}\ln\left(1+\frac{1}{x}\right)-x} $$ 

第二步，再作  $ \lim_{x\to\infty}e^{x^{2}\ln\left(1+\frac{1}{x}\right)-x} $ 的趋核运算.

上述错误是将 $ \frac{\left[\left(1+\frac{1}{x}\right)^{x}\right]^{x}}{e^{x}} $中的 $ \left(1+\frac{1}{x}\right)^{x} $换成了e，而在实数运算中， $ \left(1+\frac{1}{x}\right)^{x}\neq e $

注 有考生会问，等价无穷小替换的方法是否违背上述规则呢？举例来说，

 $$ \lim_{x\to0}\frac{1-\cos x}{x^{2}}\xlongequal{ 等价无穷小 }\lim_{x\to0}\frac{\frac{1}{2}x^{2}}{x^{2}}=\frac{1}{2}, $$ 

这里是不是在实数运算中将  $ 1 - \cos x $ 写成了  $ \frac{1}{2}x^{2} $？是否犯了错误？

请注意，如果认为  $ \lim_{x\to0}\frac{1-\cos x}{x^{2}}=\lim_{x\to0}\frac{\frac{1}{2}x^{2}}{x^{2}} $ 是在实数运算中进行的，显然是错误的.

这与  $ \lim_{x\to0}(x-\sin x)=\lim_{x\to0}(x-x) $， $ \lim_{x\to\infty}\frac{\left(1+\frac{1}{x}\right)^x}{e^x}=\lim_{x\to\infty}\frac{e^x}{e^x} $ 的错误是一样的.

事实上， $ \lim_{x\to0}\frac{1-\cos x}{x^{2}} $是这样算的：

实数运算，

 $ \frac{1-\cos x}{x^{2}}=\frac{A}{x^{2}}\frac{1-\cos x}{A}=\frac{\frac{1}{2}x^{2}}{x^{2}}\frac{1-\cos x}{\frac{1}{2}x^{2}}\left(=\frac{1}{2}\cdot\frac{1-\cos x}{\frac{1}{2}x^{2}}\right) $，进一步是可以这样写的）.

趋核运算，

 $$ \lim_{x\to0}\frac{1-\cos x}{x^{2}}=\lim_{x\to0}\frac{\frac{1}{2}x^{2}}{x^{2}}\cdot\lim_{x\to0}\frac{1-\cos x}{\frac{1}{2}x^{2}}, $$ 