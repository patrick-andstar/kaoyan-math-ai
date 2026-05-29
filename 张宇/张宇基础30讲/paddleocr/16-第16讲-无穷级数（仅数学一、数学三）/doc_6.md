分析  $ \lim_{n\to\infty}S_n=S\Leftrightarrow\sum_{n=1}^{\infty}u_n=S,\quad\lim_{n\to\infty}S_{2n}=S\Rightarrow\sum_{n=1}^{\infty}u_n=S $

证 由于  $ \lim_{n\to\infty}u_{n}=0 $ ，因此  $ \lim_{n\to\infty}u_{2n+1}=0 $ 。结合  $ \lim_{n\to\infty}S_{2n}=S $ ，有

 $$ \lim_{n\to\infty}S_{2n+1}=\lim_{n\to\infty}(S_{2n}+u_{2n+1})=\lim_{n\to\infty}S_{2n}+\lim_{n\to\infty}u_{2n+1}=S+0=S $$ 

故  $ \lim_{n\to\infty}S_{2n}=\lim_{n\to\infty}S_{2n+1}=S $ 。所以  $ \lim_{n\to\infty}S_{n}=S $ ，即  $ \sum_{n=1}^{\infty}u_{n}=S $ 。

## 级数敛散性的判别方法

<div style="text-align: center;"><img src="imgs/img_in_image_box_840_407_944_515.jpg" alt="Image" width="10%" /></div>


## 正项级数及其敛散性判别

 $$ \{S_{*}\} $$ 

若通项 $ u_{n}\geq0,n=1,2,\cdots $，则称 $ \sum_{n=1}^{\infty}u_{n} $为正项级数.

(1) 收敛原则.

正项级数  $ \sum_{n=1}^{\infty}u_{n} $ 收敛的

注 由于  $ \left\{S_{n}\right\} $ 单调不减，故  $ \lim_{n\to\infty}S_{n} $ 只有两种可能的结果：若  $ \left\{S_{n}\right\} $ 有界，则  $ \lim_{n\to\infty}S_{n}=S $（有限正数）；若  $ \left\{S_{n}\right\} $ 无界，则  $ \lim_{n\to\infty}S_{n}=+\infty $ 。除此之外，再无其他结果。

例 16.3 判别级数  $ \sum_{n=0}^{\infty}\frac{1}{n!} $ 的敛散性.

分析当 $ S_{2n} $， $ S_{2n-1} $均不好算时，可以考虑找 $ S_{n} $的上界.

解 其部分和  $ S_{n+1} $ 满足

 $$ \begin{aligned}0<S_{n+1}&=1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots+\frac{1}{n!}\\&\leq1+1+\frac{1}{1\times2}+\frac{1}{2\times3}+\cdots+\frac{1}{(n-1)n}\\&=1+1+\left(1-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{3}\right)+\cdots+\left(\frac{1}{n-1}-\frac{1}{n}\right)=3-\frac{1}{n}<3,\end{aligned} $$ 

即  $ \left\{S_{n+1}\right\} $ 有界，由收敛原则，有  $ \sum_{n=0}^{\infty}\frac{1}{n!} $ 收敛.