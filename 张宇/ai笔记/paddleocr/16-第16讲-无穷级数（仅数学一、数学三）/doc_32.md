## 2 运算法则

若幂级数  $ \sum_{n=0}^{\infty}a_{n}x^{n} $ 与  $ \sum_{n=0}^{\infty}b_{n}x^{n} $ 的收敛半径分别为  $ R_{a} $ 和  $ R_{b}(R_{a} \neq R_{b}) $，则有

① $ k\sum_{n=0}^{\infty}a_{n}x^{n}=\sum_{n=0}^{\infty}ka_{n}x^{n},\left|x\right|<R_{a} $，k为常数；

 $$ \sum_{n=0}^{\infty}a_{n}x^{n}\pm\sum_{n=0}^{\infty}b_{n}x^{n}=\sum_{n=0}^{\infty}(a_{n}\pm b_{n})x^{n},\left|x\right|<R=\min\left\{R_{a},R_{b}\right\} $$ 

注 当  $ R_a = R_b $ 时， $ \sum_{n=0}^{\infty} a_n x^n \pm \sum_{n=0}^{\infty} b_n x^n $ 的收敛半径  $ R \geq \min\{R_a, R_b\} $。即当  $ R_a = R_b $ 时， $ R $ 可能会变大。例如，对于  $ \sum_{n=0}^{\infty} (1 + 2^n) x^n $， $ \sum_{n=0}^{\infty} (1 - 2^n) x^n $，可求得

 $$ R_{a}=\lim_{n\to\infty}\frac{1+2^{n}}{1+2^{n+1}}=\frac{1}{2},\quad R_{b}=\lim_{n\to\infty}\left|\frac{1-2^{n}}{1-2^{n+1}}\right|=\frac{1}{2}, $$ 

而  $ \sum_{n=0}^{\infty}[(1+2^{n})x^{n}+(1-2^{n})x^{n}]=2\sum_{n=0}^{\infty}x^{n} $ 的收敛半径 R=1 ，即

其中  $ 2^{n}x^{n} $ 使得收敛半径相对于  $ x^{n} $ 变小，去掉  $ 2^{n}x^{n} $，则收敛半径变大

 $ R > \min\left\{\frac{1}{2}, \frac{1}{2}\right\} $，由此可见，发散级数 + 发散级数是有可能收敛的

③  $ \sum_{n=0}^{\infty}a_{n}x^{n}\cdot\sum_{n=0}^{\infty}b_{n}x^{n}=\sum_{n=0}^{\infty}\left(\sum_{i=0}^{n}a_{i}b_{n-i}\right)x^{n} $

柯西划线法：

<div style="text-align: center;"><img src="imgs/img_in_image_box_194_904_634_1172.jpg" alt="Image" width="42%" /></div>


如何理解并记住此公式呢？由

 $$ (a_{0}+a_{1}x+a_{2}x^{2})(b_{0}+b_{1}x+b_{2}x^{2})=a_{0}b_{0}+(a_{0}b_{1}+a_{1}b_{0})x+(a_{0}b_{2}+a_{1}b_{1}+a_{2}b_{0})x^{2}+(a_{1}b_{2}+a_{2}b_{1})x^{3}+a_{2}b_{2}x^{4}, $$ 

根据归纳法，可知

 $$ \sum_{n=0}^{\infty}a_{n}x^{n}\bullet\sum_{n=0}^{\infty}b_{n}x^{n}=\sum_{n=0}^{\infty}\left(\sum_{i=0}^{n}a_{i}b_{n-i}\right)x^{n}\ . $$ 

收敛半径 $ R=\min\{R_{a},R_{b}\} $

 $$ \begin{aligned}&\rightarrow 即 (a_{0}b_{n}+a_{1}b_{n-1}+\cdots+a_{n}b_{0})x^{n}\end{aligned} $$ 