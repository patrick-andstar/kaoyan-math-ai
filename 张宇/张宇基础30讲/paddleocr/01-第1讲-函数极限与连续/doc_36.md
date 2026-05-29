①  $ \lim_{x\to\infty}e^x $ 不存在，因为  $ \lim_{x\to+\infty}e^x = +\infty $， $ \lim_{x\to-\infty}e^x = 0 $，根据 “极限若存在，必唯一”，得原极限不存在。

<div style="text-align: center;"><img src="imgs/img_in_image_box_462_213_626_388.jpg" alt="Image" width="15%" /></div>


② $ \lim_{x\to0}\frac{\sin x}{|x|} $不存在，因为 $ \lim_{x\to0^{+}}\frac{\sin x}{|x|}=\lim_{x\to0^{+}}\frac{\sin x}{x}=1,\quad\lim_{x\to0^{-}}\frac{\sin x}{|x|}=\lim_{x\to0^{-}}\frac{\sin x}{-x}=-1 $

③  $ \lim_{x\to\infty}\arctan x $ 不存在，因为  $ \lim_{x\to+\infty}\arctan x=\frac{\pi}{2} $， $ \lim_{x\to-\infty}\arctan x=-\frac{\pi}{2} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_776_413_937_546.jpg" alt="Image" width="15%" /></div>


④ $ \lim_{x\to0}[x] $不存在，因为 $ \lim_{x\to0^{+}}[x]=0,\lim_{x\to0^{-}}[x]=-1 $

[x]为不超过x的最大整数，也就是x的整数部分.

⑤分段函数分段点两侧表达式不同，需分别求左、右极限。

<div style="text-align: center;"><img src="imgs/img_in_image_box_799_558_937_665.jpg" alt="Image" width="13%" /></div>


在实际考试中，主要是这些函数：一个是指数函数，一个是带绝对值的函数，也就是分段函数。如果分段函数在分段点处两端的解析式不同，是需要分别求左、右极限的，这个考点在研究生考试中几乎是必考的。所以考生不仅要知道这些唯一性，而且研究生考试中更会通过这些具体的例子去考查考生对唯一性的认识。

例1.15 当  $ x \to 1 $ 时，函数  $ \frac{e^{\frac{1}{x-1}} \ln |1 + x|}{e^x - 1(x - 2)} $ 的极限（）.

(A) 等于 1 (B) 等于 0 (C) 为  $ \infty $ (D) 不存在且不为  $ \infty $

 $ \rho $ 分析  $ x \to 1 $，关键看  $ \frac{1}{e^{-1}} $



<div style="text-align: center;"><img src="imgs/img_in_image_box_833_851_954_912.jpg" alt="Image" width="11%" /></div>


 $ x \rightarrow 1^{+}, x - 1 \rightarrow 0^{+}, \frac{1}{\sqrt{x-1}} \rightarrow +\infty; $ 你不能用一个非常非常小的正数去代替，后面会专门提无穷小的概念，它不是一个很小很小的数，而是无限趋于零的变量

 $ \boxed{x \to 1^-}, x - 1 \to 0^-, \frac{1}{x - 1} \to -\infty. $

x无限趋于1，但比1小

解 应选(D).

函数  $ \frac{\mathrm{e}^{\frac{1}{x-1}}\ln|1+x|}{(\mathrm{e}^{x}-1)(x-2)} $ 在 x=1 处没有定义，在 x=1 的两侧表达式虽然相同，但是注意到当  $ x \to 1 $ 时， $ \frac{1}{x-1} $ 左、右极限不相等，因此应该考虑单侧极限。