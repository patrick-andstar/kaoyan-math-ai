②套公式： $ S=\int_{0}^{+\infty}\frac{e^{-x}\left|\sin x\right|dx} $

保持非负（对应图形在x轴下方的部分向上翻折）

③做计算（难度在于处理绝对值）：

 $$ S=\int_{0}^{\pi}\mathbf{e}^{-x}\sin x\mathrm{d}x+\int_{\pi}^{2\pi}(-\mathbf{e}^{-x}\sin x)\mathrm{d}x+\int_{2\pi}^{3\pi}\mathbf{e}^{-x}\sin x\mathrm{d}x+\cdots=\lim_{n\rightarrow\infty}\sum_{k=0}^{n}\left|\int_{k\pi}^{(k+1)\pi}\mathbf{e}^{-x}\sin x\mathrm{d}x\right|. $$ 

解  $ S=\int_{0}^{+\infty}e^{-x}\left|\sin x\right|dx=\lim_{n\to\infty}\sum_{k=0}^{n}\left|\int_{k\pi}^{(k+1)\pi}e^{-x}\sin xdx\right| $，其中

 $$ \begin{aligned}&\int_{k\pi}^{(k+1)\pi}\mathrm{e}^{-x}\sin x\mathrm{d}x=\frac{1}{2}\left|\begin{matrix}(\mathrm{e}^{-x})^{\prime}&(\sin x)^{\prime}\\ \mathrm{e}^{-x}&\sin x\end{matrix}\right|_{k\pi}^{(k+1)\pi}\\ &=-\frac{1}{2}\mathrm{e}^{-x}(\cos x+\sin x)\Bigg|_{k\pi}^{(k+1)\pi}\\ &=-\frac{1}{2}\mathrm{e}^{-(k+1)\pi}\bullet(-1)^{k+1}+\frac{1}{2}\mathrm{e}^{-k\pi}\bullet(-1)^{k}\\ &=\frac{(-1)^{k}}{2}\mathrm{e}^{-k\pi}(\mathrm{e}^{-\pi}+1)\ ,\\ \end{aligned} 套公式 , 计算量大 , 重视计算 $$ 

故

 $$ S=\frac{\mathrm{e}^{-\pi}+1}{2}\lim_{n\rightarrow\infty}\sum_{k=0}^{n}\left(\mathrm{e}^{-\pi}\right)^{k}=\frac{\mathrm{e}^{-\pi}+1}{2}\bullet\frac{1}{1-\mathrm{e}^{-\pi}}=\frac{\mathrm{e}^{-\pi}+1}{2(1-\mathrm{e}^{-\pi})} $$ 

## 2 用定积分表达和计算旋转体的体积

→套公式

(1) 曲线  $ y = y(x) $ 与  $ x = a $,  $ x = b (a < b) $ 及 x 轴围成的曲边梯形绕 x 轴旋转一周所得到的旋转体的体积为

 $$ V_{x}=\int_{a}^{b}\pi y^{2}(x)\mathrm{d}x $$ 

这是怎么推导出来的呢？

<div style="text-align: center;"><img src="imgs/img_in_image_box_447_875_885_1054.jpg" alt="Image" width="42%" /></div>


 $$ \textcircled{2}\Delta V=\pi y^{2}(x)\mathrm{d}x\;. $$ 

③积分： $ V_{x}=\int_{a}^{b}\pi y^{2}(x)dx $。

例 10.5 求曲线  $ y = e^{-\frac{x}{2}} \sqrt{\sin x} $ 在  $ [0, 2\pi] $ 部分与 x 轴围成的平面图形绕 x 轴旋转一周所成的旋转体的体积.

分析 ①确定 x 的取值范围： $ \sqrt{\sin x} \Rightarrow \sin x \geqslant 0 \Rightarrow x \in [0, \pi] $.

②套公式： $ V_{x}=\int_{0}^{\pi}\pi(e^{-\frac{x}{2}}\sqrt{\sin x})^{2}dx $

解  $ y = e^{-\frac{x}{2}} \sqrt{\sin x} $ 在  $ [0, \pi] $ 上存在，在  $ (\pi, 2\pi) $ 内不存在，故