即在长度为一个周期的区间上的定积分，与该区间的起点位置无关，其证明见例 9.16.

(4) 设  $ f(x) $ 为连续函数，则

 $$ \int_{a}^{b}f(x)\mathrm{d}x=\int_{a}^{b}f(a+b-x)\mathrm{d}x, $$ 

这叫“区间再现公式”，其证明见例9.17.

 $$ \begin{aligned}&\star(5)\int_{0}^{\frac{\pi}{2}}\sin^{n}x\mathrm{d}x=\int_{0}^{\frac{\pi}{2}}\cos^{n}x\mathrm{d}x=\begin{cases}\frac{n-1}{n}\bullet\frac{n-3}{n-2}\bullet\cdots\bullet\frac{2}{3}\bullet1,\\\frac{n-1}{n}\bullet\frac{n-3}{n-2}\bullet\cdots\bullet\frac{1}{2}\bullet\frac{\pi}{2},\end{cases}\\ \end{aligned} $$ 

★(6)  $ \int_{0}^{\pi}\sin^{n}x\,dx=\begin{cases}2\cdot\frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdot\cdots\cdot\frac{2}{3}\cdot1,&n\text{为大于}1\text{的奇数},\\2\cdot\frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdot\cdots\cdot\frac{1}{2}\cdot\frac{\pi}{2},&n\text{为正偶数},\end{cases} $

 $$ \int_{0}^{\pi}\cos^{n}x\mathrm{d}x=\left\{\begin{aligned}&0,\\ &2\bullet\frac{n-1}{n}\bullet\frac{n-3}{n-2}\bullet\cdots\bullet\frac{1}{2}\bullet\frac{\pi}{2},\end{aligned}\right. $$ 

 $$ \begin{aligned}&\star(7)\int_{0}^{2\pi}\cos^{n}x\mathrm{d}x=\int_{0}^{2\pi}\sin^{n}x\mathrm{d}x=\left\{\begin{aligned}&0,&n 为正奇数 ,\\&4\cdot\frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdot\cdots\cdot\frac{1}{2}\cdot\frac{\pi}{2},&n 为正偶数 .\end{aligned}\right.\\ \end{aligned} $$ 

(5)，(6)，(7)叫华里士公式，利用华里士公式可快速计算某些特殊的定积分，如

 $$ \int_{0}^{\frac{\pi}{2}}\sin^{8}x\mathrm{d}x=\frac{7}{8}\cdot\frac{5}{6}\cdot\frac{3}{4}\cdot\frac{1}{2}\cdot\frac{\pi}{2}=\frac{35\pi}{256}, $$ 

 $$ \int_{0}^{\pi}\sin^{9}x\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sin^{9}x\mathrm{d}x=2\cdot\frac{8}{9}\cdot\frac{6}{7}\cdot\frac{4}{5}\cdot\frac{2}{3}\cdot1=\frac{256}{315}. $$ 

“点火公式”

例9.12  $ \lim_{n\to\infty}\frac{1}{n}\sum_{i=1}^{n}\left[\ln(3n-2i)-\ln(n+2i)\right]= $ ___.

分析  $ \ln(3n-2i)-\ln(n+2i)=\ln\frac{3n-2i}{n+2i}=\ln\frac{3-2\frac{i}{n}}{1+2\frac{i}{n}} $

解 应填 0.

 $$ \begin{aligned} 原式 &=\lim_{n\rightarrow\infty}\frac{1}{n}\sum_{i=1}^{n}\ln\frac{3n-2i}{n+2i}=\lim_{n\rightarrow\infty}\frac{1}{n}\sum_{i=1}^{n}\ln\frac{3-2\frac{i}{n}}{1+2\frac{i}{n}}\\&=\int_{0}^{1}\ln\frac{3-2x}{1+2x}\mathrm{d}x=\int_{0}^{1}\ln\frac{\frac{3}{2}-x}{\frac{1}{2}+x}\mathrm{d}x\xlongequal{ 令 x-\frac{1}{2}=t}\int_{\frac{1}{2}}^{\frac{1}{2}}\ln\frac{1-t}{1+t}\mathrm{d}t,\end{aligned} $$ 