<div style="text-align: center;"><img src="imgs/img_in_image_box_384_157_696_366.jpg" alt="Image" width="30%" /></div>


<div style="text-align: center;">图 2-4</div>


例 2.15 (1) 证明方程  $ x = \cos x $ 在  $ \left(0, \frac{\pi}{3}\right) $ 内有唯一实根 a；

(2) 设  $ -1 \leqslant x_1 \leqslant 1 $，定义  $ x_{n+1} = \cos x_n $， $ n = 1, 2, \cdots $，证明  $ \lim_{n \to \infty} x_n $ 存在，且极限值就是 (1) 中的 a

证 (1) 令  $ F(x) = \cos x - x $， $ x \in \left(0, \frac{\pi}{3}\right) $，则

 $$ F(0)=1>0,\ F\left(\frac{\pi}{3}\right)=\frac{1}{2}-\frac{\pi}{3}<0, $$ 

且  $ F'(x) = -\sin x - 1 < 0 $，故  $ F(x) $ 单调递减，于是存在唯一的  $ a \in \left(0, \frac{\pi}{3}\right) $，使得  $ F(a) = 0 $，即  $ a = \cos a $，方程在  $ \left(0, \frac{\pi}{3}\right) $ 内有唯一实根 a。

(2)由题知， $ x_{n+1}=\cos x_{n} $，由于 $ -1\leqslant x_{1}\leqslant1 $，则 $ x_{n+1}=\cos x_{n}\leqslant1 $，且 $ x_{n+1}=\cos x_{n}>0 $，故 $ 0<x_{n}\leqslant1<\frac{\pi}{3} $，n>1.

令 $ f(x)=\cos x $，显然 $ f(x) $在 $ \left(0,\frac{\pi}{3}\right) $内单调减少，于是 $ \{x_{n}\} $不单调，下面直接考虑 $ \left|x_{n+1}-a\right| $

 $$ \begin{aligned}x_{n+1}-a|&=|\cos x_{n}-\cos a|\\&\xlongequal{=}|-\sin\xi|\bullet|x_{n}-a|\xrightarrow{ 拉格朗日中值定理 }\\&\leqslant\frac{\sqrt{3}}{2}\bullet|x_{n}-a|\quad\sin\frac{\pi}{3}\\&\leqslant\left(\frac{\sqrt{3}}{2}\right)^{2}|x_{n-1}-a|\\&\quad\vdots\longrightarrow 压缩映射 \\&\leqslant\left(\frac{\sqrt{3}}{2}\right)^{n}|x_{1}-a|,\end{aligned} $$ 