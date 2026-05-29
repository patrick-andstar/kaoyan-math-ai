注 (1)  $ f(x) $ 与  $ |f(x)| $ 连续、可导的关系总结.

①设 $ f(x) $在 $ x_{0} $处连续，则 $ |f(x)| $在 $ x_{0} $处连续；反之不真。

②设 $ f(x) $在 $ x_{0} $处可导，则

a.  $ f(x_0) \neq 0 \Rightarrow |f(x)| $ 在  $ x_0 $ 处可导且  $ \left[\left|f(x)\right|\right]'\bigg|_{x=x_0} = \begin{cases} f'(x_0), & f(x_0) > 0, \\ -f'(x_0), & f(x_0) < 0. \end{cases} $

b.  $ f(x_{0})=0 $，且  $ \left\{\begin{aligned}f'(x_{0})&=0\Rightarrow\left|f(x)\right|\text{在}x_{0}\text{处可导且}\left[\left|f(x)\right|\right]^{\prime}\right|_{x=x_{0}}=0,\\ f'(x_{0})&\neq0\Rightarrow\left|f(x)\right|\text{在}x_{0}\text{处不可导}\end{aligned}\right. $

(2)  $ f(x) $ 在  $ x_{0} $ 处连续  $ \Leftrightarrow |f(x)| $ 在  $ x_{0} $ 处必连续，为什么？

因为在 $ x_{0} $处， $ f(x) $的微观性态图（放大足够多倍）如图3-5(a)~(c)所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_226_550_408_683.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_460_551_655_684.jpg" alt="Image" width="18%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_693_552_873_685.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">图 3-5</div>


<div style="text-align: center;">(c)</div>


而  $ |f(x)| $ 如图 3-6(a)~(c) 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_226_817_409_952.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_459_819_644_952.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_691_818_872_952.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">图 3-6</div>


<div style="text-align: center;">(c)</div>


点点相依相偎的图 3-5(a)~(c)，加上绝对值后依然相依相偎成为图 3-6(a)~(c)，故成立（无论是  $ \rightarrow $ 还是  $ \rightarrow $ ，只要相依相偎即可）。为什么反过来不对？很简单，你看  $ |f(x)| $ 相依相偎，连续 [见图 3-7(b)]，可  $ f(x) $ 却相距甚远，自然不连续 [见图 3-7(a)]。

<div style="text-align: center;"><img src="imgs/img_in_image_box_361_1166_527_1311.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_572_1166_734_1310.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 3-7</div>
