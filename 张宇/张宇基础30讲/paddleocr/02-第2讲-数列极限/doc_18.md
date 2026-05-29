其中  $ \xi $ 介于  $ a $ 与  $ x_n $ 之间，当  $ n \to \infty $ 时， $ \left(\frac{\sqrt{3}}{2}\right)^n |x_1 - a| \to 0 $，故由夹逼准则，有  $ x_{n+1} \to a $，即  $ \lim_{n \to \infty} x_n = a $。

注 考生可画出如图 2-5 所示的情形，加深理解。

<div style="text-align: center;"><img src="imgs/img_in_image_box_373_282_697_520.jpg" alt="Image" width="31%" /></div>


<div style="text-align: center;">图 2-5</div>


## 8 $ \{x_{n}\} $ 收敛于 a 的速度问题

设数列  $ \{x_n\} $， $ \{y_n\} $ 在  $ n \to \infty $ 的过程中同时趋于 a，记  $ u_n = |x_n - a| $， $ v_n = |y_n - a| $， $ I = \lim_{n \to \infty} \frac{u_n}{v_n} $，且当  $ n \to \infty $ 时， $ u_n $ 和  $ v_n $ 都是无穷小量，则有

若 I=0 ，则说明  $ x_{n} $ 的收敛速度比  $ y_{n} $ 的收敛速度快；（高阶）

若 I = b （b 为大于零的常数），则说明  $ x_{n} $ 的收敛速度是  $ y_{n} $ 的  $ \frac{1}{b} $ 倍；（同阶）

若  $ I = \infty $，则说明  $ x_{n} $ 的收敛速度比  $ y_{n} $ 的收敛速度慢。（低阶）

如： $ x_{n}=\frac{1}{n},y_{n}=\frac{1}{\sqrt{n}},\lim_{n\to\infty}x_{n}=\lim_{n\to\infty}y_{n}=0 $，故 $ I=\lim_{n\to\infty}\frac{\left|\frac{1}{n}-0\right|}{\left|\frac{1}{\sqrt{n}}-0\right|}=0 $，于是 $ x_{n} $比 $ y_{n} $收敛于0的速度快.

而数列极限定义为  $ \lim_{n\to\infty}x_n=a\Leftrightarrow $ 任意  $ \varepsilon>0 $ ，存在  $ N>0 $ ，当  $ n>N $ 时，恒有  $ \left|x_n-a\right|<\varepsilon $ 。此定义中不体现收敛速度，这是命制选择题的理论依据。

“对任意给定的  $ k \in \mathbb{N} $，总存在正整数 N，当  $ n > N $ 时，恒有  $ |x_n - a| \leq \frac{1}{2^k} $”是数列  $ \{x_n\} $ 收敛于  $ a $ 的（ ）。

(A) 充分不必要条件

(B) 必要不充分条件

(C) 充分必要条件

(D) 既不充分也不必要条件

解 应选 (C).