## 考研数学基础30讲·高等数学分册

★★★(3)局部保号性。（这个太重要了，极限的3个性质中最重要的一个）

如果  $  f(x) \to A(x \to x_0)  $ 且  $  A > 0  $ （或  $  A < 0  $），那么存在常数  $  \delta > 0  $，使得当  $  0 < |x - x_0| < \delta  $ 时，有  $  \begin{cases} \text{超实数} < \\ f(x) > 0 \end{cases}  $ （或  $  f(x) < 0  $）。如果在  $  x_0  $ 的某去心邻域内  $  f(x) \geq 0  $ （或  $  f(x) \leq 0  $）且  $  \lim_{x \to 0} f(x) = A  $，则  $  A \geq 0  $ （或  $  A \leq 0  $）。

 $  \lim_{x \to 0} f > 0 \Rightarrow f > 0  $

 $  \lim_{x \to 0} f < 0 \Rightarrow f < 0  $

（脱帽严格不等）牢记

 $  f \geq 0 \Rightarrow \lim_{x \to 0} f \geq 0  $

 $  f \leq 0 \Rightarrow \lim_{x \to 0} f \leq 0  $

（戴帽非严格不等）



取  $ \varepsilon = 2A $ ，则  $ -A < f(x) < 3A $ ，此范围不够精确，不能用于证明此结论

lim我=你：即使给我整个世界，我也只在你身边



<div style="text-align: center;"><img src="imgs/img_in_image_box_588_345_708_405.jpg" alt="Image" width="11%" /></div>


注证  $ \lim_{x\to x_0}f(x)=A(A>0) $，即对任意  $ \varepsilon>0 $，存在  $ \delta>0 $，使得当  $ 0<|x-x_0|<\delta $ 时，有  $ |f(x)-A|<\varepsilon $。取  $ \varepsilon=\frac{A}{2}>0 $，即有  $ |f(x)-A|<\frac{A}{2} $，所以  $ f(x)>\frac{A}{2}>0 $，证毕。

<div style="text-align: center;"><img src="imgs/img_in_image_box_245_594_471_674.jpg" alt="Image" width="21%" /></div>


四面八方均可到来，以A为核心，A自带光环

问题：超实数的标准实数部分都大于零，那这些超实数都怎么样呢？

答：它们与 A 的距离无限小，从而它们一定大于零。

注 只要核心大于零，它的所有光晕都大于零.

如  $ \lim_{x\to+\infty}\frac{1}{x}\rightarrow0 $ 为它的标准实数部分

 $ \rightarrow $ 0 作为它的标准实数部分

 $ \rightarrow $ 0 为它的标准实数部分

即使 $ f(x)>0 $，它的极限也有可能等于零，即存在 $ f(x)>0 $，使 $ \mathrm{std}[f(x)]=0 $。对于大于零的超实数，它的标准实数部分有可能是零。0的右边是有光晕的

<div style="text-align: center;"><img src="imgs/img_in_image_box_759_953_929_1017.jpg" alt="Image" width="16%" /></div>


例 1.18 已知  $ f(x) $ 在 x=0 的某个邻域内连续，且  $ \lim_{x\to0}\frac{f(x)}{1-\cos x}=-1 $，则存在  $ \delta>0 $，（）.

(A) 当  $ x \in (-\delta, 0) $ 时， $ f(x) > 0 $；当  $ x \in (0, \delta) $ 时， $ f(x) < 0 $

(B) 当  $ x \in (-\delta, 0) $ 时， $ f(x) < 0 $；当  $ x \in (0, \delta) $ 时， $ f(x) > 0 $

(C) 当  $ x \in (-\delta, 0) $ 时， $ f(x) > 0 $；当  $ x \in (0, \delta) $ 时， $ f(x) > 0 $

(D) 当  $ x \in (-\delta, 0) $ 时， $ f(x) < 0 $；当  $ x \in (0, \delta) $ 时， $ f(x) < 0 $

♡分析 本题考查保号性，在考研中经常出类似的题，本题关键在于极限是负数.

解 应选(D).

由于