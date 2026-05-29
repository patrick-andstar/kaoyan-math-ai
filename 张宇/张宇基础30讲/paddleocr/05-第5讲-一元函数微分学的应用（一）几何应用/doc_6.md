令 $ f^{(n+1)}(x)=(n+1+x)e^{x}=0 $，得函数 $ f^{(n)}(x)=(n+x)e^{x} $的驻点 $ x=-(n+1) $。又

 $$ f^{(n+2)}[-(n+1)]=\mathbf{e}^{-n-1}>0, $$ 

所以  $ x = -(n+1) $ 是函数  $ f^{(n)}(x) = (n+x)e^{x} $ 的极小值点，极小值为

 $$ f^{(n)}\bigl[-(n+1)\bigr]=-\mathbf{e}^{-(n+1)}\;. $$ 

方法总结 先求出表达式  $ f^{(n)}(x) $，再求出此函数的驻点，然后代入  $ f^{(n+2)}(x) $ 验证即可。求极小值时将驻点代入  $ f^{(n)}(x) $ 而非  $ f(x) $。

## 凹凸性与拐点的概念

<div style="text-align: center;"><img src="imgs/img_in_image_box_858_417_962_525.jpg" alt="Image" width="10%" /></div>


## 凹凸性的定义

《全国硕士研究生招生考试数学考试大纲》规定如下：

定义 1 设函数  $ f(x) $ 在区间 I 上连续. 如果对 I 上任意不同两点  $ x_{1}, x_{2} $，恒有

横坐标中点的函数值在曲线上  $ \left\langle f\left(\frac{x_{1}+x_{2}}{2}\right)<\frac{f(x_{1})+f(x_{2})}{2},\right. $  $ \rightarrow $ 函数值的中点在弦上

则称  $ y = f(x) $ 在 I 上的图形是凹的（或凹弧），如图 5-2(a) 所示；如果恒有

 $$ f\left(\frac{x_{1}+x_{2}}{2}\right)>\frac{f(x_{1})+f(x_{2})}{2}, $$ 

则称  $ y = f(x) $ 在 I 上的图形是凸的（或凸弧），如图 5-2(b) 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_273_910_488_1091.jpg" alt="Image" width="20%" /></div>


 $$ \frac{f(x_{1})+f(x_{2})}{2}>f\left(\frac{x_{1}+x_{2}}{2}\right) $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_577_896_795_1090.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">(a)</div>


 $$ \frac{f(x_{1})+f(x_{2})}{2}<f\left(\frac{x_{1}+x_{2}}{2}\right) $$ 

<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 5-2</div>


注 事实上，当图形为凹时，可以将 $ f\left(\frac{1}{2}x_{1}+\frac{1}{2}x_{2}\right)<\frac{1}{2}f(x_{1})+\frac{1}{2}f(x_{2}) $更一般地写为

 $$ f(\lambda_{1}x_{1}+\lambda_{2}x_{2})<\lambda_{1}f(x_{1})+\lambda_{2}f(x_{2}), $$ 

广义化的凹凸性定义