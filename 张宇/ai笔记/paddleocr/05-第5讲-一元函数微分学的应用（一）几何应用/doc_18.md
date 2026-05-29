其次，用导数工具， $ y=(1-x^{2})^{\frac{3}{2}} $， $ y'=\frac{3}{2}(1-x^{2})^{\frac{1}{2}}\cdot(-2x)\xlongequal{\text{令}}0 $，当 $ x\geq0,y\geq0 $时，x=0,x=1；又 $ y''=3\cdot\frac{2x^{2}-1}{\sqrt{1-x^{2}}} $，令 $ y''=0 $，解得 $ x=\frac{\sqrt{2}}{2} $（拐点横坐标），代入得，拐点 $ \left(\frac{\sqrt{2}}{2},\left(\frac{1}{2}\right)^{\frac{3}{2}}\right) $.

列表如下.


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>x</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>$ \left(0,\frac{\sqrt{2}}{2}\right) $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{\sqrt{2}}{2} $</td><td style='text-align: center; word-wrap: break-word;'>$ \left(\frac{\sqrt{2}}{2},1\right) $</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>y&#x27;</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'></td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>y&#x27;&#x27;</td><td style='text-align: center; word-wrap: break-word;'>-3</td><td style='text-align: center; word-wrap: break-word;'>-</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>+</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>y</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>$ \searrow $</td><td style='text-align: center; word-wrap: break-word;'>拐点</td><td style='text-align: center; word-wrap: break-word;'>$ \searrow $</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr></table>

<div style="text-align: center;"><img src="imgs/img_in_image_box_740_336_946_537.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">图 5-7</div>


最后，画出图像，如图 5-7 所示.

注也可借助上表分析出由每个分段点分出的区间内函数的单调性与曲线的凹凸性.

例 5.12 画出  $ y = x^{x} $ (x > 0) 的图像.

♡分析 幂指函数求导常用公式： $ u^{v}=e^{v\ln u} $

解 当  $ x \rightarrow 0^{+} $ 时，

 $$ \begin{aligned}\lim_{x\to0^{+}}x^{x}&=\lim_{x\to0^{+}}e^{x\ln x}=e^{\lim\limits_{x\to0^{+}}x\ln x}=e^{\lim\limits_{x\to0^{+}}\frac{\ln x}{\frac{1}{x}}}\\&=e^{\lim\limits_{x\to0^{+}}\frac{\frac{1}{x}}{\frac{1}{x^{2}}}}=e^{\lim\limits_{x\to0^{+}}(-x)}=e^{0}=1\end{aligned} $$ 

令 $ y=f(x) $，则

 $$ f^{\prime}(x)=(x^{x})^{\prime}=(e^{x\ln x})^{\prime}=x^{x}(1+\ln x)\ ,\longrightarrow 求驻点 $$ 

 $$ \begin{aligned}f^{\prime \prime}(x)&=\left[f^{\prime}(x)\right]^{\prime}=\left[(1+\ln x)f(x)\right]^{\prime}\\&=(1+\ln x)f^{\prime}(x)+\frac{1}{x}f(x)\\&=x^{x}\left[(1+\ln x)^{2}+\frac{1}{x}\right].\\ \end{aligned} $$ 

由x>0，得 $ x^x>0 $，故 $ f(x)>0 $， $ f''(x)>0 $。 $ \rightarrow $无拐点

令 $ f'(x)=0 $，解得 $ x=\frac{1}{e} $。因此 $ f(x) $在 $ x=\frac{1}{e} $处取得极小值，故函数图像如图5-8所示。

 $$ \left(0,\frac{1}{e}\right)\text{上},\quad f^{\prime}(x)<0\text{；在 }\left(\frac{1}{e},+\infty\right)\text{上},\quad f^{\prime}(x)>0. $$ 