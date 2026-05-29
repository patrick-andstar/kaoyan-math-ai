 $$ \begin{aligned}&\left\{\begin{aligned}&\sqrt{a^{2}-x^{2}}\rightarrow 令 x=a\sin t,\left|t\right|<\frac{\pi}{2},\\&\sqrt{a^{2}+x^{2}}\rightarrow 令 x=a\tan t,\left|t\right|<\frac{\pi}{2},\end{aligned}\right.\end{aligned} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_648_165_801_355.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_823_168_965_353.jpg" alt="Image" width="13%" /></div>


 $$ \left\{\begin{aligned}\sqrt{x^{2}-a^{2}}&\rightarrow 令 x=a\sec t,\\ \end{aligned}\right.\left\{\begin{aligned} 若 x>0, 则 0<t<\frac{\pi}{2},\\ 若 x<0, 则 \frac{\pi}{2}<t<\pi.\end{aligned}\right. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_805_354_963_542.jpg" alt="Image" width="15%" /></div>


②恒等变形后作三角函数代换——当被积函数含有根式 $ \sqrt{ax^{2}+bx+c} $时，可先化为以下三种形式：

 $$ \sqrt{\varphi^{2}(x)+k^{2}},\sqrt{\varphi^{2}(x)-k^{2}},\sqrt{k^{2}-\varphi^{2}(x)}, $$ 

再作三角函数代换.

解题利器：“令复杂=t”

★★★③根式代换——当被积函数含有根式 $ \sqrt[n]{ax+b} $， $ \sqrt{\frac{ax+b}{cx+d}} $， $ \sqrt{ae^{bx}+c} $等时，一般令根式 $ \sqrt{*} = t $（因为事实上，很难通过根号内换元的办法凑成平方，所以根号无法去掉）。对既含有 $ \sqrt[n]{ax+b} $，也含有 $ \sqrt[m]{ax+b} $的函数，一般取 $ m, n $的最小公倍数 $ l $，令 $ \sqrt[l]{ax+b} = t $。

 $$ \begin{aligned}& 比如 ,\  含有 \sqrt[2]{ax+b},\sqrt[3]{ax+b} 的函数 ,\  令 t=\sqrt[6]{ax+b}．\end{aligned} $$ 

④倒代换——当被积函数分母的幂次比分子高两次及两次以上时，作倒代换，令 $ x=\frac{1}{t} $

 $$ \begin{aligned}\downarrow_{ 未必一定用 , 必 }\int\frac{1}{x(x^{3}+1)}\mathrm{d}x&=\int\frac{x^{2}\widehat{x}}{\overline{x^{3}(x^{3}+1)}\mathrm{d}x=\frac{1}{3}\int\frac{1}{x^{3}(x^{3}+1)}\mathrm{d}(x^{3})\\&\xlongequal{x^{3}=t}\frac{1}{3}\int\frac{1}{t(t+1)}\mathrm{d}t=\frac{1}{3}\int\left(\frac{1}{t}-\frac{1}{t+1}\right)\mathrm{d}t\\&=\frac{1}{3}(\ln|t|-\ln|t+1|)+C\\&=\frac{1}{3}\ln\left|\frac{x^{3}}{x^{3}+1}\right|+C\end{aligned} $$ 

⑤复杂函数的直接代换——当被积函数中含有  $ a^x $， $ e^x $， $ \ln x $， $ \arcsin x $， $ \arctan x $ 等时，可考虑直接令复杂函数等于  $ t $，值得指出的是，当  $ \ln x $， $ \arcsin x $， $ \arctan x $ 与  $ P_n(x) $ 或  $ e^{ax} $ 作乘法时（其中  $ P_n(x) $ 为  $ x $ 的  $ n $ 次多项式），优先考虑分部积分法。

 $$ \textcircled{11}例 9.3\quad 求不定积分 \int\sqrt{a^{2}-x^{2}}\mathrm{d}x(a>0). $$ 