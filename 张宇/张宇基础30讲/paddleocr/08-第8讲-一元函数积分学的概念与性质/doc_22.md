注 本题是考研真题，如果考生能够熟练掌握一元函数积分学的有关概念和性质，便可轻松解决这个问题，而无须进行烦琐的计算，从这个角度说，本题是概念题.

例8.12 设函数 $ f(x)=\begin{cases}\cos x,&0\leq x<π,\\1,&\pi\leq x\leq2π,\end{cases} $， $ F(x)=\int_{0}^{x}f(t)dt $，则（）.

(A)  $ x = \pi $ 是函数  $ F(x) $ 的跳跃间断点

(B)  $ x = \pi $ 是函数  $ F(x) $ 的可去间断点

(C)  $ F(x) $ 在  $ x=\pi $ 处连续但不可导

(D)  $ F(x) $ 在  $ x=\pi $ 处可导

解 应选(C).

 $$ \begin{aligned}\lim_{x\to\pi}\cos x=-1,\quad\lim_{x\to\pi}1=1\end{aligned} $$ 

方法一 由于  $ x = \pi $ 为  $ f(x) $ 的跳跃间断点，因此  $ F(x) = \int_{0}^{x} f(t) \, dt $ 在  $ x = \pi $ 处连续但不可导，故选 (C).

方法二  $ F(x)=\int_{0}^{x}f(t)dt=\left\{\begin{aligned}&\int_{0}^{x}\cos tdt,&0\leqslant x<\pi,\\&\int_{0}^{\pi}\cos tdt+\int_{\pi}^{x}1dt,& \pi\leqslant x\leqslant2\pi.\end{aligned}\right. $  $ =\left\{\begin{aligned}&\sin x,&0\leqslant x<\pi,\\&x-\pi,&\pi\leqslant x\leqslant2\pi.\end{aligned}\right. $

因为  $ \lim_{x\to\pi^{+}}F(x)=\lim_{x\to\pi^{-}}F(x)=F(\pi)=0 $ ，所以  $ F(x) $ 在  $ x=\pi $ 处连续．而

 $$ F_{-}^{\prime}(\pi)=\lim_{x\to\pi^{-}}\frac{F(x)-F(\pi)}{x-\pi}=\lim_{x\to\pi^{-}}\frac{\sin x-0}{x-\pi}=\lim_{x\to\pi^{-}}\frac{\cos x}{1}=-1 $$ 

 $$ F_{+}^{\prime}(\pi)=\lim_{x\to\pi^{+}}\frac{F(x)-F(\pi)}{x-\pi}=\lim_{x\to\pi^{+}}\frac{x-\pi-0}{x-\pi}=1 $$ 

因此  $ F_{-}^{\prime}(\pi) \neq F_{+}^{\prime}(\pi) $，即  $ F(x) $ 在  $ x = \pi $ 处不可导。

例8.13 设 $ f(x)=\begin{cases}e^{x^2}+x^2,&x\neq0,\\a,&x=0,\end{cases} $，其中 $ a $为常数，令 $ F(x)=\int_{-1}^{x}f(t)dt $，则以下命题：

①当a=1时， $ F(x) $在x=0处可导；

②当 $ a\neq1 $时， $ F(x) $在x=0处可导；

③当a=1时， $ F(x) $在x=0处不可导；

当 $ a\neq1 $时， $ F(x) $在x=0处不可导.

所有真命题的序号为（）.

(A) ①④ (B) ①② (C) ③④ (D) ②③

解 应选(B).

若 a=1，则  $ f(x) $ 在 x=0 处连续，此时  $ F(x) $ 在 x=0 处可导，且  $ F'(0)=f(0)=1 $。

若  $ a \neq 1 $，则 x = 0 是  $ f(x) $ 的可去间断点，此时

 $$ \lim_{x\to0}\frac{\int_{-1}^{x}(e^{t^{2}}+t^{2})dt-\int_{-1}^{0}(e^{t^{2}}+t^{2})dt}{x-0}\xlongequal{洛必达法则}\lim_{x\to0}(e^{x^{2}}+x^{2})=1 $$ 

于是  $ F'(0) $ 存在，即  $ F(x) $ 在 x=0 处仍可导，故选 (B).

或用 “三、2.(3)” 的结论，直接有  $ F(x) $ 在 x=0 处可导.