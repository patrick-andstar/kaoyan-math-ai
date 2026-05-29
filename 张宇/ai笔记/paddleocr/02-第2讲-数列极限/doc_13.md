 $$  联想到 1-\cos x\sim\frac{1}{2}x^{2}(x\rightarrow0) $$ 

 $$ \lim_{n\to\infty}\frac{a_{n}}{b_{n}^{2}}=\lim_{n\to\infty}\frac{\sqrt{1-\cos b_{n}}}{b_{n}^{2}}\cdot\frac{a_{n}}{1-\cos b_{n}}=\frac{1}{2}\lim_{n\to\infty}\frac{a_{n}}{1-\cos a_{n}+a_{n}}=\frac{1}{2}\lim_{n\to\infty}\frac{1}{\frac{1-\cos a_{n}}{a_{n}}+1}=\frac{1}{2} $$ 

单调有界准则  $ \rightarrow $ 单调有界准则是讨论数列极限存在的两个最重要的准则之一，另外一个是夹逼准则

单调有界数列必有极限，即若数列  $ \{x_{n}\} $ 单调增加（减少）且有上界（下界），则  $ \lim_{n\to\infty}x_{n} $ 存在。

不等关系

单调有界准则其实包含两种情况（涉及不等关系，是数学中的难点），第1种情况数列单调增加并且有上界；第2种情况，数列单调减少并且有下界。在这两种情况下数列极限都是存在的，使用的时候需要注意，当证明出来数列单调增加时，只需要再去证明数列有上界即可，无须再去证明有下界，同样如果证明出来数列有上界，则只需要再去证明数列单调增加即可，第二种情况同理。

记： $ x_{n} \leqslant x_{n+1} \leqslant a $，则  $ \lim_{n \to \infty} x_{n} $ 存在.

<div style="text-align: center;"><img src="imgs/img_in_image_box_116_589_363_816.jpg" alt="Image" width="23%" /></div>


学会用结论即可。不必去证明准则本身

<div style="text-align: center;"><img src="imgs/img_in_image_box_394_604_631_769.jpg" alt="Image" width="22%" /></div>


 $ a \leqslant x_{n+1} \leqslant x_n $，则  $ \lim_{n \to \infty} x_n $ 存在。

<div style="text-align: center;"><img src="imgs/img_in_image_box_405_834_622_995.jpg" alt="Image" width="21%" /></div>


证明数列 $ \{x_{n}\} $单调性的常用方法：

★ a.  $ \underline{x_{n+1}-x_{n}}> $ 0 或  $ \frac{x_{n+1}}{x_{n}}> $ 1（同号）.

作差法用得较多.

★ b. 利用数学归纳法.

一题一练 设  $ c = 2 \ln(1 + b) $,  $ b > a > 0 $，且  $ a $ 是方程  $ x - 2 \ln(1 + x) = 0 $ 的唯一非零解，证明  $ c > a $

♡分析 由题知， $ c=2\ln(1+b) $， $ a=2\ln(1+a) $。

令 $ f(x)=2\ln(1+x) $， $ f'(x)=\frac{2}{1+x} $，则当x>0时， $ f(x) $单调递增.

由 b > a > 0 ，得  $ 2 \ln(1 + b) > 2 \ln(1 + a) $，故 c > a

<div style="text-align: center;"><img src="imgs/img_in_image_box_711_1241_942_1360.jpg" alt="Image" width="22%" /></div>


题一练 设单调递减数列  $ \{x_n\} $ 满足  $ x_{n+1} = 2\ln(1 + x_n) $， $ n=1,2,\cdots $， $ x_1 > a > 0 $，且  $ a $ 是  $ x - 2\ln(1 + x) = 0 $ 的唯一