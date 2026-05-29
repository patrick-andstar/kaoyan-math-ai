证 因为  $ x = x_{0} \in I $ 是  $ f(x) $ 唯一的间断点，所以  $ x \neq x_{0} $ 时， $ f(x) $ 连续，此时  $ F(x) = \int_{a}^{x} f(t) \, dt $ 可导，且  $ F'(x) = f(x) $，而  $ F'(x_{0}) = \lim_{x \to x_{0}} \frac{F(x) - F(x_{0})}{x - x_{0}} $。

这两个等号使用洛必达法则

若  $ x_{0} \in I $ 是  $ f(x) $ 的跳跃间断点，则  $ F'_{-}(x_{0}) = \lim_{x \to x_{0}} f(x) $， $ F'_{+}(x_{0}) = \lim_{x \to x_{0}} f(x) $，因为  $ \lim_{x \to x_{0}} f(x) \neq \lim_{x \to x_{0}} f(x) $，所以此时  $ F'_{-}(x_{0}) \neq F'_{+}(x_{0}) $，即  $ F(x) = \int_{a}^{x} f(t) \, dt $ 在  $ x_{0} $ 处不可导。

若  $ x_{0} \in I $ 是  $ f(x) $ 的可去间断点，则  $ \lim_{x \to x_{0}} f(x) $ 存在，于是  $ F'(x_{0}) = \lim_{x \to x_{0}} f(x) $ 存在。

例 8.11 设函数  $ y = f(x) $ 在区间  $ [-1, 3] $ 上的图形如图 8-6 所示，则函数  $ F(x) = \int_0^x f(t) \, dt $ 的图形为（ ）.

<div style="text-align: center;"><img src="imgs/img_in_image_box_404_569_630_752.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 8-6</div>


<div style="text-align: center;">(A)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_797_406_995.jpg" alt="Image" width="23%" /></div>


<div style="text-align: center;">(B)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_561_798_806_995.jpg" alt="Image" width="23%" /></div>


<div style="text-align: center;">(C)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_163_1006_429_1201.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">(D)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_565_1008_806_1205.jpg" alt="Image" width="23%" /></div>


## 解 应选(D)

本题有三个要点：第一，变限积分只要存在就必连续，故排除(B); 第二，由 $ f(x) $有两个跳跃间断点可知， $ F(x) $应有两个不可导点，排除(A); 第三， $ F(0)=\int_{0}^{0}f(t)dt=0 $，所以 $ F(x) $的图像过原点，排除(C). 故答案选择(D).