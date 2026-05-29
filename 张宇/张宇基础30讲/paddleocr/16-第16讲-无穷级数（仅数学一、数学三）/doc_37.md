公式  $ \sum_{n=1}^{\infty}nx^{n}=\frac{x}{(1-x)^{2}},\quad|x|<1 $

注 $ ^{(1)} $ 幂级数求和函数的突破口：

①当 $ (an+b)^{c} $在分母上时，先导后积，见例16.30.

②当 $ (an+b)^{c} $在分子上时，先积后导，见例16.31.

(2) 对于先积后导、先导后积的处理办法：

①先积后导： $ \left[\int S(x)dx\right]' = S(x) $

②先导后积．由于 $ \int_{a}^{x}S'(t)\,\mathrm{d}t=S(t)\Big|_{a}^{x}=S(x)-S(a) $，故 $ S(x)=\int_{a}^{x}S'(t)\,\mathrm{d}t+S(a) $

又由于当 a 为中心点时， $ \left\{\begin{aligned}&\sum_{n=0}^{\infty}a_{n}x^{n}\xlongequal{x=0}a_{0},\\&\sum_{n=0}^{\infty}a_{n}(x-x_{0})^{n}\xlongequal{x=x_{0}}a_{0}\end{aligned}\right. $ 都收敛，故下限通常取中心点.

(3) 在解题过程中始终不要忘记标注收敛域。

(4) 建议大家记住由这两个例题所得到的结果.

 $$ \sum_{n=1}^{\infty}nx^{n}=\frac{x}{(1-x)^{2}},-1<x<1 $$ 

 $$ \sum_{n=1}^{\infty}\frac{x^{n}}{n}=-\ln(1-x),-1\leqslant x<1;\sum_{n=1}^{\infty}nx^{n-1}=\frac{1}{(1-x)^{2}},-1<x<1. $$ 

利用这两个公式可直接得到如下常数项级数的和.

 $$ \sum_{n=1}^{\infty}\frac{1}{n\cdot2^{n}}=\sum_{n=1}^{\infty}\frac{1}{n}\cdot\left(\frac{1}{2}\right)^{n}=-\ln\left(1-\frac{1}{2}\right)=\ln2, $$ 

 $$ \sum_{n=1}^{\infty}\frac{n}{2^{n}}=\frac{1}{2}\sum_{n=1}^{\infty}n\left(\frac{1}{2}\right)^{n-1}=\frac{1}{2}\times\frac{1}{\left(1-\frac{1}{2}\right)^{2}}=2\ . $$ 

(5) 当  $ |x|<1 $ 时，

 $$ \frac{1}{1-x}=\sum_{n=0}^{\infty}x^{n}\stackrel{ 苗项为 n=0}{\longrightarrow} $$ 

 $$ \Rightarrow\frac{1}{(1-x)^{2}}=\sum_{n=0}^{\infty}nx^{n-1}\left(\frac{x}{(1-x)^{2}}=\sum_{n=0}^{\infty}nx^{n}\right) $$ 

 $$ \rightarrow 实际为 n=1, 常数求导为 0 $$ 

 $$ \Rightarrow\frac{2}{(1-x)^{3}}=\sum_{n=0}^{\infty}n(n-1)x^{n-2} $$ 

 $$ \Rightarrow\frac{6}{(1-x)^{4}}=\sum_{n=3}^{\infty}n(n-1)(n-2)x^{n-3}. $$ 

对于一个幂级数，它的系数为 n 的 3 次幂，可通过①②③④的线性组合求得。