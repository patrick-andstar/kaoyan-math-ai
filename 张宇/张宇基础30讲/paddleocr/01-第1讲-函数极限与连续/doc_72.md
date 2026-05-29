故在 $ \left[-\frac{\pi}{2},\frac{3}{2}\pi\right) $上， $ f(x)=\left\{\begin{aligned}&x,&x\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right),\\&\pi-x,&x\in\left[\frac{\pi}{2},\frac{3}{2}\pi\right),\end{aligned}\right. $于是在 $ (-∞,+∞) $上，

 $$ f(x)=\arcsin(\sin x)=\begin{cases}x-2k\pi,&x\in\left[-\frac{\pi}{2}+2k\pi,\frac{\pi}{2}+2k\pi\right),\ $ 2k+1)\pi-x,&x\in\left[\frac{\pi}{2}+2k\pi,\frac{3}{2}\pi+2k\pi\right),\end{cases}k 为整数 . $$ 

其图形如图 1-29 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_404_446_628_544.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 1-29</div>


1.12 解 利用等价无穷小量代换， $ e^{x}-1\sim x(x\rightarrow0) $，则

 $$ \begin{aligned}\lim_{x\rightarrow0}\left(\frac{\mathrm{e}^{x}+x\mathrm{e}^{x}}{\mathrm{e}^{x}-1}-\frac{1}{x}\right)&=\lim_{x\rightarrow0}\frac{x\mathrm{e}^{x}(1+x)+1-\mathrm{e}^{x}}{x(\mathrm{e}^{x}-1)}=\lim_{x\rightarrow0}\frac{x\mathrm{e}^{x}(1+x)+1-\mathrm{e}^{x}}{x^{2}}\\&=\lim_{x\rightarrow0}\frac{3x\mathrm{e}^{x}+x^{2}\mathrm{e}^{x}}{2x}=\lim_{x\rightarrow0}\frac{3\mathrm{e}^{x}+x\mathrm{e}^{x}}{2}=\frac{3}{2}\ .\end{aligned} $$ 

注 下面的做法是错误的：

 $$ \begin{aligned}\lim_{x\to0}\left(\frac{\mathbf{e}^{x}+x\mathbf{e}^{x}}{\mathbf{e}^{x}-1}-\frac{1}{x}\right)&=\lim_{x\to0}\left(\frac{\mathbf{e}^{x}+x\mathbf{e}^{x}}{x}-\frac{1}{x}\right)\\&=\lim_{x\to0}\frac{\mathbf{e}^{x}+x\mathbf{e}^{x}-1}{x}=\lim_{x\to0}(2\mathbf{e}^{x}+x\mathbf{e}^{x})=2\end{aligned} $$ 

1.13 解 因为  $ \lim_{x\to0}a_{i}^{x}=1 $ ，所以原极限为 “ $ 1^{\infty} $” 型未定式.

方法一 使用洛必达法则求极限.

 $$ \begin{aligned}\lim_{x\to0}\left(\frac{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}}{n}\right)^{\frac{n}{x}}&=\exp\left\{\lim_{x\to0}\frac{n}{x}\left(\frac{a_{1}^{x}+a_{2}^{x}+\cdots+a_{n}^{x}}{n}-1\right)\right\}\\&=\exp\left\{\lim_{x\to0}\frac{a_{1}^{x}-1}{x}+\lim_{x\to0}\frac{a_{2}^{x}-1}{x}+\cdots+\lim_{x\to0}\frac{a_{n}^{x}-1}{x}\right\}\\&=\exp\{\lim_{x\to0}(a_{1}^{x}\ln a_{1}+a_{2}^{x}\ln a_{2}+\cdots+a_{n}^{x}\ln a_{n})\}=a_{1}a_{2}\cdots a_{n}.\end{aligned} $$ 

方法二 凑成第二个重要极限（“1 $ ^{\circ} $”型未定式都可以凑成第二个重要极限），在计算过程中使用洛必达法则.