 $$ \lim_{x\to0}\left(\frac{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}}{n}\right)^{\frac{n}{x}}=\lim_{x\to0}\left(1+\frac{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}-n}{n}\right)^{\frac{n}{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}-n}\cdot\frac{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}-n}{x}}, $$ 

其中

 $$ \lim_{x\to0}\frac{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}-n}{x}=\ln(a_{1}a_{2}\cdots a_{n}),\lim_{x\to0}\left(1+\frac{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}-n}{n}\right)^{\frac{n}{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}-n}}=e, $$ 

所以，原式 $ =a_{1}a_{2}\cdots a_{n} $

1.14 解 因为  $ \lim_{x\to0}\left[a\frac{2+\mathrm{e}^{\frac{1}{x}}}{1+\mathrm{e}^{\frac{4}{x}}}+(1+|x|)^{\frac{1}{x}}\right] $ 存在，且

 $$ \lim_{x\to0^{+}}\left[a\frac{2+\mathrm{e}^{\frac{1}{x}}}{1+\mathrm{e}^{\frac{4}{x}}}+(1+|x|)^{\frac{1}{x}}\right]=\lim_{x\to0^{+}}\left[a\frac{2+\mathrm{e}^{\frac{1}{x}}}{1+\mathrm{e}^{\frac{4}{x}}}+(1+x)^{\frac{1}{x}}\right]=0+\mathrm{e}=\mathrm{e}, $$ 

 $$ \lim_{x\to0^{-}}\left[a\frac{2+\mathrm{e}^{\frac{1}{x}}}{1+\mathrm{e}^{\frac{4}{x}}}+(1+|x|)^{\frac{1}{x}}\right]=\lim_{x\to0^{-}}\left[a\frac{2+\mathrm{e}^{\frac{1}{x}}}{1+\mathrm{e}^{\frac{4}{x}}}+(1-x)^{\frac{1}{x}}\right]=2a+\frac{1}{\mathrm{e}}, $$ 

所以

 $$ \mathbf{e}=2a+\frac{1}{\mathbf{e}}, $$ 

解得

 $$ a=\frac{\mathbf{e}}{2}-\frac{1}{2\mathbf{e}}. $$ 

1.15 解 原极限  $ =\lim_{x\to0}\frac{x-\frac{1}{2}x^{2}+o(x^{2})-ax-bx^{2}}{x^{2}}=\lim_{x\to0}\frac{(1-a)x-\left(\frac{1}{2}+b\right)x^{2}+o(x^{2})}{x^{2}}=2 $ ，从而

 $$ 1-a=0,\ -\left(\frac{1}{2}+b\right)=2\ , $$ 

解得 a=1,  $ b=-\frac{5}{2} $

## 注 本题还有一个值得借鉴的解法

根据泰勒公式容易得： $ x - \ln(1 + x) \sim \frac{1}{2} x^2 (x \to 0) $（请考生记住此式），故想办法把分子凑出这种形式。

 $$ \begin{aligned}2=&\lim_{x\rightarrow0}\frac{\ln(1+x)-(ax+bx^{2})}{x^{2}}=-\lim_{x\rightarrow0}\frac{x-\ln(1+x)-x+(ax+bx^{2})}{x^{2}}\\=&-\lim_{x\rightarrow0}\frac{x-\ln(1+x)}{x^{2}}-\lim_{x\rightarrow0}\frac{(a-1)x}{x^{2}}-\lim_{x\rightarrow0}\frac{bx^{2}}{x^{2}}=-\frac{1}{2}-b-\lim_{x\rightarrow0}\frac{(a-1)x}{x^{2}},\end{aligned} $$ 

故 a-1=0，得 a=1。因而  $ -\frac{1}{2}-b=2 $，得  $ b=-\frac{5}{2} $