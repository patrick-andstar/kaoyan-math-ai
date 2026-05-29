⑧当  $ 0 < x < \frac{\pi}{2} $ 时， $ \sin x > \frac{2}{\pi}x $ 。证明见例 6.19.

⑨  $ \arctan x \leqslant x \leqslant \arcsin x (0 \leqslant x \leqslant 1) $

<div style="text-align: center;"><img src="imgs/img_in_image_box_569_139_772_281.jpg" alt="Image" width="19%" /></div>


可考：当  $ x_{n}>0 $ 时， $ x_{n+1}=\arctan x_{n}<x_{n} $，故  $ \left\{x_{n}\right\} $ 单调减少。

<div style="text-align: center;"><img src="imgs/img_in_image_box_790_179_932_307.jpg" alt="Image" width="13%" /></div>


 $ 10\,e^x \geq x + 1 $ (任意  $ x $)

可考：当  $ x_{n+1} = e^{x_n} - 1 $ 时，由  $ e^{x_n} - 1 \geq x_n $，得  $ x_{n+1} \geq x_n $，即  $ \{x_n\} $ 单调不减。

⑪  $ x - 1 \geq \ln x (x > 0) $。

可考：当  $ x_n > 0 $ 时，若  $ x_{n+1} = \ln x_n + 1 $，由  $ \ln x_n + 1 \leq x_n $，得  $ x_{n+1} \leq x_n $，即  $ \{x_n\} $ 单调不增。

⑫  $ \frac{1}{1 + x} < \ln \left(1 + \frac{1}{x}\right) < \frac{1}{x} (x > 0) $ 或  $ \frac{x}{1 + x} < \ln (1 + x) < x (x > 0) $。



<div style="text-align: center;"><img src="imgs/img_in_image_box_744_324_939_468.jpg" alt="Image" width="18%" /></div>


(3) 利用闭区间上连续函数必有最大值与最小值.

(4) 利用压缩映射原理。（简化版）

原理一 对数列  $ \{x_n\} $，若存在常数  $ k $ ( $ 0 < k < 1 $)，使得  $ |x_{n+1} - a| \leq k|x_n - a| $， $ n = 1, 2, \cdots $，则  $ \{x_n\} $ 收敛于  $ a $。

证  $ 0 \leqslant |x_{n+1} - a| \leqslant k |x_n - a| \leqslant k^2 |x_{n-1} - a| \leqslant \cdots \leqslant k^n |x_1 - a| $，由于  $ \lim_{n \to \infty} k^n = 0 $，根据夹逼准则，有  $ \lim_{n \to \infty} |x_{n+1} - a| = 0 $，即  $ \{x_n\} $ 收敛于  $ a $。

原理二 对数列  $ \{x_n\} $，若  $ x_{n+1} = f(x_n) $， $ n=1,2,\cdots $， $ f(x) $ 可导， $ a $ 是  $ f(x) = x $ 的唯一解，且对任意  $ x \in \mathbb{R} $，有  $ |f'(x)| \leq k < 1 $，则  $ \{x_n\} $ 收敛于  $ a $。

证  $ \left|x_{n+1}-a\right|=\left|f(x_{n})-f(a)\right| $ 

拉格朗日中值定理  $ \left|f'(\xi)\right|\left|x_{n}-a\right|\leqslant k\left|x_{n}-a\right| $，其中  $ \xi $ 介于  $ a $ 与  $ x_{n} $ 之间，

由原理一，有  $ \{x_{n}\} $ 收敛于 a .

以上原理一、二是特殊的压缩映射过程，考生在使用它们时，要写出证明过程。如例 2.15。

(5) 利用题设条件来推证（这往往是解答题的第 1 问）.  $ \longrightarrow $ 例2.11

例 2.9  $ \lim_{n\to\infty}\left(\frac{1}{n^{2}+n+1}+\frac{2}{n^{2}+n+2}+\cdots+\frac{n}{n^{2}+n+n}\right)= $ ___.

分析分母不一样不能相加减，通分又太复杂，故可以利用放缩将分母化成相同的.需要注意：分母越大，分数越小.

把分母写成一样的： $ 小 \leq \sum_{i=1}^{n} \frac{i}{n^{2} + n + i} \leq $ 大.

解 应填 $ \frac{1}{2} $