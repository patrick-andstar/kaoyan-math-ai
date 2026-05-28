1.12 求极限  $ \lim_{x\to0}\left(\frac{e^{x}+xe^{x}}{e^{x}-1}-\frac{1}{x}\right) $.

1.13 求极限  $ \lim_{x\to0}\left(\frac{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}}{n}\right)^{\frac{n}{x}} $，其中  $ a_{i}>0, i=1,2,\cdots,n $

1.14 已知  $ \lim_{x\to0}\left[a\frac{2+\mathrm{e}^{\frac{1}{x}}}{1+\mathrm{e}^{\frac{4}{x}}}+(1+|x|)^{\frac{1}{x}}\right] $ 存在，求 a 的值.

1.15 设  $ \lim_{x\to0}\frac{\ln(1+x)-(ax+bx^{2})}{x^{2}}=2 $，求常数 a, b.

1.16 求常数 a 和 b 的值，使得函数  $ f(x) = x - (a + b \cos x) \sin x $ 在  $ x \to 0 $ 时是 x 的 5 阶无穷小.

## 解答

1.1 (C) 解 方法一  $ \lim_{x\to0}\frac{\sin x+xf(x)}{x^{3}}=\lim_{x\to0}\frac{\sin x-x+x+xf(x)}{x^{3}}=\lim_{x\to0}\frac{\sin x-x}{x^{3}}+\lim_{x\to0}\frac{x+xf(x)}{x^{3}} $

 $  = -\frac{1}{6} + \lim_{x\to0}\frac{1+f(x)}{x^{2}} = 0  $,

则 $ \lim_{x\to0}\frac{1+f(x)}{x^{2}}=\frac{1}{6} $.故选(C).

方法二 对  $ \sin x $ 使用泰勒展开，

 $$ \lim_{x\to0}\frac{\sin x+xf(x)}{x^{3}}=\lim_{x\to0}\frac{x-\frac{1}{6}x^{3}+o(x^{3})+xf(x)}{x^{3}}=\lim_{x\to0}\frac{1+f(x)}{x^{2}}-\frac{1}{6}=0 $$ 

故  $ \lim_{x\to0}\frac{1+f(x)}{x^{2}}=\frac{1}{6} $ 。故选 (C).

方法三 由  $ \lim_{x\to0}\frac{\sin x+xf(x)}{x^{3}}=0 $ ，得  $ \frac{\sin x+xf(x)}{x^{3}}=0+\alpha $ ，其中  $ \lim_{x\to0}\alpha=0 $ ，于是得

 $$ xf(x)=-\sin x+o(x^{3}). $$ 

故  $ \lim_{x\to0}\frac{1+f(x)}{x^{2}}=\lim_{x\to0}\frac{x-\sin x+o(x^{3})}{x^{3}}=\frac{1}{6} $ 。故选 (C).

1.2 (D) 解 因为  $ \lim_{x\to0}g(x)=\lim_{x\to0}f\left(\frac{1}{x}\right)=\lim_{x\to\infty}f(x)=a $，而  $ g(0)=0 $，所以当 a=0 时，函数  $ g(x) $ 在点 x=0 处连续；当  $ a\neq0 $ 时，函数  $ g(x) $ 在点 x=0 处不连续，故选 (D).

1.3 (D) 解  $ f(x) $ 非分段函数，只需讨论函数的无定义点 x=0,1 。因为