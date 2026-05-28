<div style="text-align: center;"><img src="imgs/img_in_image_box_288_134_789_333.jpg" alt="Image" width="48%" /></div>


考研复习的方法很重要，如基础阶段只做“1+1=2”这肯定是不行的。必须在基础阶段，扎扎实实地落实到考研数学的命题当中，掌握他们喜欢考的这些表达式，这个是很重要的。

例1.25 求极限  $ I=\lim_{x\to\infty}\frac{a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0}{b_mx^m+b_{m-1}x^{m-1}+\cdots+b_1x+b_0} $，其中  $ a_n(\neq0) $， $ b_m(\neq0) $ 为常数。纸老虎

☑ 分析 有理函数的极限问题，抓主要矛盾。找“带头大哥”，若“带头大哥”次数一致，结果就是系数比，就能很快速地把问题解决了。

解 若 n=m，则

 $$ I\xlongequal{ 上下都除以 x^{n}}\lim_{x\to\infty}\frac{a_{n}+\frac{a_{n-1}}{x}+\cdots+\frac{a_{1}}{x^{n-1}}+\frac{a_{0}}{x^{n}}}{b_{m}+\frac{b_{m-1}}{x}+\cdots+\frac{b_{1}}{x^{n-1}}+\frac{b_{0}}{x^{n}}} $$ 

 $$ \begin{aligned}\xlongequal{ 四则运算法则 }\frac{\lim\limits_{x\rightarrow\infty}\left(a_{n}+\frac{a_{n-1}}{x}+\cdots+\frac{a_{1}}{x^{n-1}}+\frac{a_{0}}{x^{n}}\right)}{\lim\limits_{x\rightarrow\infty}\left(b_{m}+\frac{b_{m-1}}{x}+\cdots+\frac{b_{1}}{x^{n-1}}+\frac{b_{0}}{x^{n}}\right)}=\frac{a_{n}}{b_{m}};\end{aligned} $$ 

若n>m，则 $ I=\lim_{x\to\infty}\frac{x^{n-m}\left(a_{n}x^{m}+a_{n-1}x^{m-1}+\cdots+a_{1}x^{m-n+1}+a_{0}x^{m-n}\right)}{b_{m}x^{m}+b_{m-1}x^{m-1}+\cdots+b_{1}x+b_{0}}=\lim_{x\to\infty}x^{n-m}\cdot\frac{a_{n}}{b_{m}}=\infty; $

超实数，特殊的不存在

这两种情况出现概率很小

若 n < m，则  $ I = \lim_{x \to \infty} \frac{a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0}{x^{m-n} \left( b_m x^n + b_{m-1} x^{n-1} + \cdots + b_1 x^{n-m+1} + b_0 x^{n-m} \right)} = \lim_{x \to \infty} \frac{1}{x^{m-n}} \cdot \frac{a_n}{b_m} = 0 $.

综上， $ \lim_{x\to\infty}\frac{a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots+a_{1}x+a_{0}}{b_{m}x^{m}+b_{m-1}x^{m-1}+\cdots+b_{1}x+b_{0}}=\left\{\begin{array}{ll}\frac{a_{n}}{b_{m}},&n=m,\\ \infty,&n>m,\\ 0,&n<m.\end{array}\right. $

☐ 方法总结 抓大头.

 $ \lim_{x\to\infty}\frac{x^{3}+x^{2}-1}{0\cdot x^{3}+2x^{2}+2}=\infty,\quad\lim_{x\to\infty}\frac{0\cdot x^{3}-x^{2}+2}{1\cdot x^{3}-x+1}=0 $ 补一个“带头大哥”（但不要写卷子上）

公式  $ \lim_{x\to\infty}\frac{a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots+a_{1}x+a_{0}}{b_{m}x^{m}+b_{m-1}x^{m-1}+\cdots+b_{1}x+b_{0}}=\left\{\begin{aligned}&\frac{a_{n}}{b_{m}},&n=m,\\&\infty,&n>m,\\&0,&n<m.\end{aligned}\right. $