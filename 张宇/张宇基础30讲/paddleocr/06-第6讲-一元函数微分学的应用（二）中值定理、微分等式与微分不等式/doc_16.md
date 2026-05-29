所以曲线 $ f(x)=\sin x-\frac{2x}{\pi} $在 $ \left(0,\frac{\pi}{2}\right) $内是凸的，又 $ f(0)=f\left(\frac{\pi}{2}\right)=0 $，所以 $ f(x)=\sin x-\frac{2x}{\pi}>0 $，即

 $$ \sin x>\frac{2x}{\pi},\;x\in\left(0,\;\frac{\pi}{2}\right). $$ 

例6.20 证明： $ \left(\ln\frac{1+x}{x}-\frac{1}{1+x}\right)^{2}<\frac{1}{x\left(1+x\right)^{2}}(x>0) $

证 只要证明当x>0时， $ \left|\ln\frac{1+x}{x}-\frac{1}{1+x}\right|-\frac{1}{\sqrt{x}(1+x)}<0 $即可.

带绝对值无法求导



<div style="text-align: center;"><img src="imgs/img_in_image_box_753_193_913_314.jpg" alt="Image" width="15%" /></div>


令

 $$ f(x)=\ln\frac{1+x}{x}-\frac{1}{1+x}=\ln(1+x)-\ln x-\frac{1}{1+x} $$ 

则

补充中值定理结论：

 $$ \begin{aligned}f^{\prime}(x)&=\frac{1}{1+x}-\frac{1}{x}+\frac{1}{(1+x)^{2}}\\&=\frac{(1+x)x-(1+x)^{2}+x}{x(1+x)^{2}}\\&=\frac{-1}{x(1+x)^{2}}<0,\end{aligned} $$ 

令 $ f(t)=\ln t $，则存在 $ \xi\in(x,x+1) $使得 $ \ln(1+x)-\ln x=\frac{1}{\xi}\cdot1 $。

又因为 $ \frac{1}{1+x}<\frac{1}{\xi}<\frac{1}{x} $。

所以 $ \frac{1}{1+x}<\ln\left(1+\frac{1}{x}\right)<\frac{1}{x} $。记住！！

又  $ \lim_{x\to+\infty}f(x)=0 $ ，所以  $ f(x)>0 $

令

 $$ g(x)=\ln\frac{1+x}{x}-\frac{1}{1+x}-\frac{1}{\sqrt{x}(1+x)}, $$ 

则

 $$ \begin{aligned}&g^{\prime}(x)=\frac{1}{1+x}-\frac{1}{x}+\frac{1}{(1+x)^{2}}+\frac{\frac{1}{2\sqrt{x}}\cdot(1+x)+\sqrt{x}}{x(1+x)^{2}}\\ &\\ &\quad=\frac{-2\sqrt{x}+1+x+2x}{2x^{\frac{3}{2}}(1+x)^{2}}=\frac{1+3x-2\sqrt{x}}{2x^{\frac{3}{2}}(1+x)^{2}}\quad 分母 >0\\ \end{aligned} $$ 

为  $ h(x) $ 的驻点，

①当 $ x>\frac{1}{9} $时， $ h'(x)>0 $

②当 $ x<\frac{1}{9} $时， $ h'(x)<0 $

唯一的小值为最小值

再令  $ h(x)=1+3x-2\sqrt{x} $，则  $ h'(x)=3-\frac{1}{\sqrt{x}}\xlongequal{\text{令}}0 $，得  $ x=\frac{1}{9} $，为唯一极小值点，也即最小值点，且  $ h_{\min}=\frac{2}{3}>0 $，故  $ h(x)>0 $，于是  $ g'(x)>0 $，即  $ g(x) $ 在  $ (0,+\infty) $ 上单调增加，且  $ \lim_{x\to+\infty}g(x)=0 $，所以  $ g(x)<0 $，证毕。