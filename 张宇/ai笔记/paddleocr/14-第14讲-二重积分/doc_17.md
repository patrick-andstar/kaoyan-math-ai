则

 $$ \begin{aligned} 原式 &=\lim_{x\to+\infty}\frac{\int_{0}^{x}t^{2}\mathrm{e}^{-t^{2}}\mathrm{d}t-\frac{\sqrt{\pi}}{4}}{x^{b}\mathrm{e}^{-x^{2}}}\xlongequal{ 洛必达法则 }\lim_{x\to+\infty}\frac{x^{2}\mathrm{e}^{-x^{2}}}{bx^{b-1}\mathrm{e}^{-x^{2}}+x^{b}\mathrm{e}^{-x^{2}}\left(-2x\right)}\\&=\lim_{x\to+\infty}\frac{x^{2}}{bx^{b-1}-2x^{b+1}}=-\frac{1}{2},\end{aligned} $$ 

故b=1

☑ 方法总结 当分母→0时，若分式的极限不为0，则可知分子→0。

 $ \lim_{x\to+\infty}e^{x^2}\left(\int_0^x t^2e^{-t^2}dt+a\right)=\infty $

无穷大 常数 常数

公式  $ \int_{0}^{+\infty}t^{2}e^{-t^{2}}dt=\frac{\sqrt{\pi}}{4} $

## 3 极坐标系与直角坐标系的互相转化

一是用好 $ \left\{\begin{aligned}x=r\cos\theta,\\ y=r\sin\theta\end{aligned}\right. $这个公式；二是画出区域D的边界图形，做好上限、下限的转化.

例14.14  $ \int_{0}^{1}dx\int_{1-x}^{\sqrt{1-x^{2}}}\frac{x+y}{x^{2}+y^{2}}dy= $ ___.

♡分析 本题乍一看，也许我们会先考虑题目是否在积分次序上设置了障碍，是否需要交换积分次序再做积分，但是，细致做来，我们会发现不管是先对x积分，还是先对y积分，都不容易计算。看来这不是积分次序上的问题，这时想想看是不是选择何种坐标系的问题呢？被积函数中含有 $ x^2 + y^2 $的形式，且积分区域是圆的一部分，如图14-9所示，显然应该优先考虑极坐标系，题目给出的却是直角坐标系，我们需要改变一下。

<div style="text-align: center;"><img src="imgs/img_in_image_box_789_778_941_912.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;">图 14-9</div>


即使发现区域D关于y=x对称，使用轮换对称性 $ f(x,y)+f(y,x) $的等式仍复杂，所以不用轮换对称性，只需要放在极坐标下计算即可。

解 应填  $ 2-\frac{\pi}{2} $

 $$ \begin{aligned} 原式 &=\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta\int_{\frac{1}{\cos\theta+\sin\theta}}^{1}\frac{r(\cos\theta+\sin\theta)}{r^{2}}r\mathrm{d}r\xrightarrow{ 由 x+y=1 得 }r=\frac{1}{\cos\theta+\sin\theta}\\&=\int_{0}^{\frac{\pi}{2}}(\cos\theta+\sin\theta)\frac{\cos\theta+\sin\theta-1}{\cos\theta+\sin\theta}\mathrm{d}\theta\\&=\int_{0}^{\frac{\pi}{2}}\cos\theta\mathrm{d}\theta+\int_{0}^{\frac{\pi}{2}}\sin\theta\mathrm{d}\theta-\int_{0}^{\frac{\pi}{2}}\mathrm{d}\theta\\&=1+1-\frac{\pi}{2}=2-\frac{\pi}{2}.\\ \end{aligned} $$ 

☑ 方法总结 当题目是累次积分时，通常考虑换积分顺序或者换坐标系。