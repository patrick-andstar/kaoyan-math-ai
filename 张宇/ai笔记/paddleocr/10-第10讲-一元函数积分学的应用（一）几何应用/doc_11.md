 $$ \begin{aligned}&\begin{aligned}\\ &s=\int_{0}^{\frac{1}{2}}\sqrt{1+(y^{\prime})^{2}}\mathrm{d}x=\int_{0}^{\frac{1}{2}}\sqrt{1+\left(\frac{-2x}{1-x^{2}}\right)^{2}}\mathrm{d}x=\int_{0}^{\frac{1}{2}}\frac{1+x^{2}}{1-x^{2}}\mathrm{d}x\\&=\int_{0}^{\frac{1}{2}}\frac{x^{2}-1+2}{1-x^{2}}\mathrm{d}x=\int_{0}^{\frac{1}{2}}\left(\frac{2}{1-x^{2}}-1\right)\mathrm{d}x\\&=\int_{0}^{\frac{1}{2}}\left(\frac{1}{1+x}+\frac{1}{1-x}-1\right)\mathrm{d}x=\ln3-\frac{1}{2}.\\ &\end{aligned}\\ \end{aligned} $$ 

例 10.11 阿基米德螺线  $ r = \theta $ 上相应于  $ \theta $ 从 0 到  $ 2\pi $ 一段的弧长为 ___.

☐ 分析 套极坐标求弧长的公式.

解 应填  $ \pi\sqrt{1+4\pi^{2}}+\frac{1}{2}\ln\left(2\pi+\sqrt{1+4\pi^{2}}\right) $

阿基米德螺线的图形如图 10-10 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_708_438_927_583.jpg" alt="Image" width="21%" /></div>


由题意，所求弧长为

<div style="text-align: center;">图 10-10</div>


 $$ \begin{aligned}&s=\int_{0}^{2\pi}\sqrt{[r(\theta)]^{2}+[r^{\prime}(\theta)]^{2}}\mathrm{d}\theta\\ &=\int_{0}^{2\pi}\sqrt{\theta^{2}+1^{2}}\mathrm{d}\theta\\ &=\int_{0}^{2\pi}\sqrt{1+\theta^{2}}\mathrm{d}\theta\\ &=\left[\frac{\theta}{2}\sqrt{1+\theta^{2}}+\frac{1}{2}\ln\left(\theta+\sqrt{1+\theta^{2}}\right)\right]_{0}^{2\pi}\\ &=\pi\sqrt{1+4\pi^{2}}+\frac{1}{2}\ln\left(2\pi+\sqrt{1+4\pi^{2}}\right).\\ \end{aligned}\\ \begin{aligned}&\theta=\tan t\\ &\frac{\theta-\tan t}{\sqrt{1+\theta^{2}}}\mathrm{d}\theta=\frac{\int\left[\sec^{3}t\mathrm{d}t-\int\left[\sec^{2}t\cdot\mathrm{d}(\tan t)\right]=\sec t\cdot\tan t-\int\tan^{2}t\sec t\mathrm{d}t\right]}{\sec t\cdot\tan t-\int(\sec^{2}t-1)\sec t\mathrm{d}t}\\ &=\frac{\sec t\cdot\tan t-\sqrt{\sec^{3}t}\mathrm{d}t+\int\sec t\mathrm{d}t}{\frac{1}{2}\sec t\cdot\tan t+\frac{1}{2}\ln(\sec t+\tan t)+C}\\ &=\frac{1}{2}\cdot\sqrt{1+\theta^{2}}\cdot\theta+\frac{1}{2}\ln\left(\sqrt{\theta^{2}+1}+\theta\right)+C\\ \end{aligned} $$ 

(3)旋转曲面的面积（侧面积）. $ \rightarrow $ 在弧长公式基础上多乘了 $ 2\pi|y(x)| $.

①曲线  $ L: y = f(x) (a \leqslant x \leqslant b) $ 绕 x 轴旋转一周所得旋转曲面的面积

 $$ S=2\pi\int_{a}^{b}\left|y\right|\sqrt{1+\left(y_{x}^{\prime}\right)^{2}}\mathrm{d}x\quad. $$ 

②曲线  $ L:\left\{\begin{aligned}x=x(t),\\ y=y(t)\end{aligned}\right. $( $ \alpha\leq t\leq\beta $,  $ x'(t)\neq0 $) 绕 x 轴旋转一周所得旋转曲面的面积

<div style="text-align: center;"><img src="imgs/img_in_image_box_760_1049_917_1174.jpg" alt="Image" width="15%" /></div>


 $$ S=2\pi\int_{\alpha}^{\beta}\left|y(t)\right|\sqrt{\left(x_{t}^{\prime}\right)^{2}+\left(y_{t}^{\prime}\right)^{2}}\mathrm{d}t. $$ 

算体积用 dx，算侧面积用 ds

 $ S=\int_{a}^{b}2\pi\left|f(x)\right|\frac{ds}{\downarrow} $

孤微分

③曲线  $ L: r = r(\theta)(\alpha \leq \theta \leq \beta) $ 绕 x 轴旋转一周所得旋转曲面的面积

 $$ S=2\pi\int_{\alpha}^{\beta}\left|r(\theta)\sin\theta\right|\sqrt{\left[r(\theta)\right]^{2}+\left[r^{\prime}(\theta)\right]^{2}}\mathrm{d}\theta. $$ 

例 10.12 曲线  $ y = \sqrt{x - 1} (1 \leq x \leq 2) $ 绕 x 轴旋转一周所得到的旋转体的表面积为 ___.