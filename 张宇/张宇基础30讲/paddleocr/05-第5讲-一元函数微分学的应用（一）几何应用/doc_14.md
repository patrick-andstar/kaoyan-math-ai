<div style="text-align: center;"><img src="imgs/img_in_image_box_101_137_950_483.jpg" alt="Image" width="82%" /></div>


注 $ ^{4} $ ①求斜渐近线时，a与b均应求出来才可以，仅求出a不能确定有斜渐近线.

如  $ y = x + \sin x $， $ a = \lim_{x \to \infty} \frac{y}{x} = 1 $，而  $ b = \lim_{x \to \infty} (y - 1 \cdot x) = \lim_{x \to \infty} \sin x $ 不存在。

所以  $ y = x + \sin x $ 无斜渐近线.

②曲线与渐近线可能会有交点，如 $ y=\frac{\sin x}{x} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_392_751_695_886.jpg" alt="Image" width="29%" /></div>


例 5.9 求曲线  $ y = \frac{1}{x} + \ln(1 + e^x) $ 的渐近线.

☐分析 按铅直、水平与斜渐近线的顺序依次去找，注意极限的计算.

解 因为

 $$ \lim_{x\to0}\left[\frac{1}{x}+\ln(1+\mathrm{e}^{x})\right]=\infty, $$ 

所以直线 x=0 是曲线  $ y=\frac{1}{x}+\ln(1+e^{x}) $ 的一条铅直渐近线.

因为

 $$ \lim_{x\to-\infty}\left[\frac{1}{x}+\ln(1+\mathrm{e}^{x})\right]=0, $$ 

所以直线 y=0 是曲线  $ y=\frac{1}{x}+\ln(1+e^{x}) $ 在  $ x\to-\infty $ 时的一条水平渐近线.

因为