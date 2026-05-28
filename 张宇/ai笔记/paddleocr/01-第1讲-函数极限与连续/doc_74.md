1.16 解 先作恒等变形： $ f(x)=x-a\sin x-\frac{1}{2}b\sin 2x $，再利用泰勒展开式，由

 $$ \sin x=x-\frac{x^{3}}{6}+\frac{x^{5}}{120}+o(x^{5}), $$ 

 $$ \sin2x=2x-\frac{(2x)^{3}}{6}+\frac{(2x)^{5}}{120}+o(x^{5})=2x-\frac{4}{3}x^{3}+\frac{4}{15}x^{5}+o(x^{5}), $$ 

可得

 $$ f(x)=(1-a-b)x+\left(\frac{a}{6}+\frac{2b}{3}\right)x^{3}-\left(\frac{a}{120}+\frac{2b}{15}\right)x^{5}+o(x^{5}). $$ 

欲使在  $ x \rightarrow 0 $ 时，函数  $ f(x) $ 是 x 的 5 阶无穷小，则  $ \left\{\begin{aligned}&1-a-b=0,\\&\frac{a}{6}+\frac{2b}{3}=0,\\&\frac{a}{120}+\frac{2b}{15}\neq0,\end{aligned}\right. $ 解得  $ a=\frac{4}{3}, b=-\frac{1}{3} $