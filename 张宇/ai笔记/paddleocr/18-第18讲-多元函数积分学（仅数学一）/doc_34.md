 $$ \begin{aligned}&=-6\int_{0}^{\frac{\pi}{2}}\sin^{4}t(1-\sin^{2}t)dt\\ &\\&=-6\times\left(\frac{3}{4}\times\frac{1}{2}\times\frac{\pi}{2}-\frac{5}{6}\times\frac{3}{4}\times\frac{1}{2}\times\frac{\pi}{2}\right)=-\frac{3}{16}\pi.\\ \end{aligned} $$ 

例18.16 在过点  $ O(0,0) $ 和  $ A(\pi,0) $ 的曲线族  $ y=a\sin x(a>0) $ 中，求一条曲线 L，使沿该曲线

从 O 到 A 的积分  $ \int_{L}(1+y^{3})\,\mathrm{d}x+(2x+y)\,\mathrm{d}y $ 的值最小.

<div style="text-align: center;"><img src="imgs/img_in_image_box_744_321_922_400.jpg" alt="Image" width="17%" /></div>


(2) 先将 a 当作常数代入积分中，利用参数法，令  $ \begin{cases} x = x, \\ v = a \sin x. \end{cases} $ 再将 a 当作变量，利用导数为零求得 a.

 $$ \mathrm{d}y=a\cos x\mathrm{d}x $$ 

解

 $$ I(a)=\int_{0}^{\pi}\left[1+a^{3}\sin^{3}x+(2x+a\sin x)a\cos x\right]\mathrm{d}x=\pi-4a+\frac{4}{3}a^{3} $$ 

令 $ I'(a)=4(a^2-1)=0 $，得 $ a=1(a=-1 $舍去 $ ) $，且 $ a=1 $是 $ I(a) $在 $ (0,+\infty) $内的唯一驻点。

又因为 $ I''(1)=8>0 $，所以 $ I(a) $在a=1处取到最小值。因此所求曲线是

验证

 $$ y=\sin x(0\leqslant x\leqslant\pi) $$ 

注 本题是一道小的综合题，主要考查平面第二型曲线积分的基本方法(化为定积分)及一元函数的最值.

总结 从近几年考查的题型来看，例 18.15 这种类型的题目比较容易出解答题，且具有一定区分度；例 18.16 这类综合题反而不是很难，更可能出选择题。

第二型曲线积分（边界）

★★★ (2) 格林公式.  $ \rightarrow $ 化为  $ \rightarrow $ 二重积分（内部）

理论意义：类似  $ \int_{a}^{b} f(x) \, dx = F(x) $  $ {}^{b} $，把一个区间内部要解决的问题转换到端点上去.



设平面有界闭区域D由分段光滑曲线L围成， $ \underline{\text{P(x, y), Q(x, y)}} $在D上具有一阶连续偏导数， $ \underline{\text{L取正向，则}} $①曲线封闭②

 $$ \begin{aligned}&\oint_{L}P(x,y)\mathrm{d}x+Q(x,y)\mathrm{d}y=\iint_{D}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathrm{d}\sigma．\\ &\quad\begin{aligned}\\ &\downarrow& 内部和边界连接 \\&\downarrow&L 必为封闭正向曲线 \\ &\end{aligned}\\ \end{aligned} $$ 

伟大的数学家格林花了七天七夜闭关修炼，创立了格林公式，他出关的时候他的朋友挖苦他：你这个书呆子，七天七夜不和人讲话，你怎么耐得住寂寞？格林轻轻回了一句：我根本没有寂寞，何来寂寞可耐？

这个故事送给各位考研的同学，考研需要闭关修炼，闭关修炼的时候你怎么耐得住寂寞？以伟大的数学家格林为榜样——我没有寂寞，何来寂寞可耐！

注 所谓 L 取正向，是指当一个人沿着 L 的这个方向前进时，左手始终在 L 所围成的区域 D 内，如图 18-16 所示。试想一下：假如你在学校的环形操场上跑步，你的左手始终在草坪中，说明你跑的方向是正向。