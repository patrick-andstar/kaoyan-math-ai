 $$ \begin{aligned}&\lim_{x\rightarrow+\infty}\frac{\frac{1}{x}+\ln(1+\mathrm{e}^{x})}{x}=\lim_{x\rightarrow+\infty}\left[\frac{1}{x^{2}}+\frac{x+\ln(1+\mathrm{e}^{-x})}{x}\right]=1,\\&\lim\left[\frac{1}{1}+\ln(1+\mathrm{e}^{x})-x\right]=\lim\left[\frac{1}{1}+\ln(1+\mathrm{e}^{-x})\right]=0.\end{aligned}\Rightarrow\begin{aligned}&\ln(1+\mathrm{e}^{x})-x\\=&\ln(1+\mathrm{e}^{x})-\ln\mathrm{e}^{x}\\=&\ln\frac{1+\mathrm{e}^{x}}{\mathrm{e}^{x}}\\=&\ln(1+\mathrm{e}^{-x})\end{aligned} $$ 

且

 $$ \lim_{x\to+\infty}\left[\frac{1}{x}+\ln(1+\mathrm{e}^{x})-x\right]=\lim_{x\to+\infty}\left[\frac{1}{x}+\ln(1+\mathrm{e}^{-x})\right]=0, $$ 

所以直线 y = x 是曲线  $ y = \frac{1}{x} + \ln(1 + e^x) $ 在  $ x \to +\infty $ 时的一条斜渐近线，其大致图形如图 5-6 所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_415_405_615_604.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">图 5-6</div>


注 渐近线的求解是对考生的极限计算能力的考查.

## 七 最值或取值范围

<div style="text-align: center;"><img src="imgs/img_in_image_box_833_737_936_846.jpg" alt="Image" width="9%" /></div>


最值的定义 → 整体概念，有别于极值

定义 3 设  $ x_{0} $ 为  $ f(x) $ 定义域内一点，若对于  $ f(x) $ 的定义域内任意一点 x，均有

 $$ f(x)\leqslant f(x_{0})\ ( 或 f(x)\geqslant f(x_{0})\ ) $$ 

成立，则称 $ f(x_{0}) $为 $ f(x) $的最大值（或最小值）.

注 极值和最值是什么关系？我们通过两个例子来看。

①设 $ f(x)=\mathrm{e}^{x},x\in[0,+\infty) $，则 $ f(0)=\mathrm{e}^{0}=1 $为 $ f(x) $在 $ [0,+\infty) $内的最小值，即 $ f(x)\geq f(0) $。但 $ f(x) $在 $ [0,+\infty) $内没有极值。细致说来，首先，x=0是区间左端点，不存在双侧邻域 $ U(0) $，使 $ x\in U(0) $时， $ f(x)\geq f(0) $，故不存在极值。其次，对于 $ (0,+\infty) $内的任意一点 $ x_{0} $



不论  $ U(x_0) $ 取得多么小，对于  $ x \in U(x_0) $，并不总有  $ f(x) \geq f(x_0) $，所以  $ f(x) $ 在  $ [0, +\infty) $ 内无极小值，易见也无极大值。所以  $ f(x) $ 在  $ [0, +\infty) $ 内无极值。

<div style="text-align: center;"><img src="imgs/img_in_image_box_777_1210_919_1307.jpg" alt="Image" width="13%" /></div>


②设 $ f(x)=3x-x^{3} $，有

 $$ f^{\prime}(x)=3(1-x^{2}),f^{\prime \prime}(x)=-6x,f^{\prime}(\pm1)=0,f^{\prime \prime}(\pm1)=\mp6, $$ 