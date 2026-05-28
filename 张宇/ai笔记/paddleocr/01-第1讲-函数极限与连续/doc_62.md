方法一 由泰勒公式可知

 $$ \mathrm{e}^{x}=1+x+\frac{x^{2}}{2!}+o(x^{2}) $$ 

由题设可知

 $$ \lim_{x\to0}\frac{\mathrm{e}^{x}-(ax^{2}+bx+1)}{x^{2}}=0, $$ 

即

 $$ \lim_{x\to0}\frac{\left(\frac{1}{2}-a\right)x^{2}+\left(1-b\right)x+o\left(x^{2}\right)}{x^{2}}=0,\quad\frac{o\left(x^{2}\right)}{x^{2}}=0 $$ 

则 $ a=\frac{1}{2} $，b=1

方法二 由洛必达法则可知

 $$ \lim_{x\to0}\frac{e^{x}-(ax^{2}+bx+1)}{x^{2}}=\lim_{x\to0}\frac{e^{x}-2ax-b}{2x} $$ 

若 $ b\neq1 $，上式右端趋于无穷，从而左端也趋于无穷，与原题设矛盾，所以b=1。因此

 $$ \lim_{x\to0}\frac{\mathrm{e}^{x}-2ax-b}{2x}=\lim_{x\to0}\frac{\mathrm{e}^{x}-1}{2x}-a=\frac{1}{2}-a=0, $$ 

故  $ a=\frac{1}{2} $，所以应选(A).

公式 当  $ x \to 0 $ 时， $ e^{x} = 1 + x + \frac{x^{2}}{2!} + o(x^{2}) $

例1.35 设函数 $ f(x)=\frac{\sin x}{1+x^{2}} $在x=0处的3次泰勒多项式为 $ ax+bx^{2}+cx^{3} $，则（）.

(A) a=1, b=0,  $ c=-\frac{7}{6} $

(B)a=1,b=0,c= $ \frac{7}{6} $

(C)a=-1,b=-1,c=- $ \frac{7}{6} $

(D)  $ a = -1, b = -1, c = \frac{7}{6} $

解 应选(A).

方法一 由于在x=0处有泰勒展开式

 $$ \sin x=x-\frac{x^{3}}{3!}+\cdots,\frac{1}{1+x^{2}}=1-x^{2}+x^{4}-\cdots, $$ 

因此

 $$ \frac{\sin x}{1+x^{2}}=\left(x-\frac{x^{3}}{3!}+\cdots\right)\left(1-x^{2}+x^{4}-\cdots\right)=x-\frac{7}{6}x^{3}+\cdots $$ 

又由题设知，在x=0处有

 $$ \frac{\sin x}{1+x^{2}}=ax+bx^{2}+cx^{3}+\cdots, $$ 

所以

 $$ a=1,b=0,c=-\frac{7}{6}. $$ 