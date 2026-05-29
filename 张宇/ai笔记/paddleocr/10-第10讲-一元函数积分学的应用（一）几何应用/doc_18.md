所以

 $$ \int_{0}^{2\pi}(t-\sin t)^{2}\sin t\mathrm{d}t=-4\pi^{2}-2\pi^{2}=-6\pi^{2} $$ 

则

 $$ V_{_{y}}=-\pi a^{3}\bullet\left(-6\pi^{2}\right)=6\pi^{3}a^{3}. $$ 

方法二 平面图形绕y轴旋转一周所得旋转体的体积为

 $$ \begin{aligned}V_{_{y}}&=2\pi\int_{0}^{2\pi}xy(x)\mathrm{d}x&\\&=2\pi\int_{0}^{2\pi}a(t-\sin t)a(1-\cos t)a(1-\cos t)\mathrm{d}t\\ &\\&=2\pi a^{3}\int_{0}^{2\pi}(t-2t\cos t+t\cos^{2}t-\sin t+2\sin t\cos t-\sin t\cos^{2}t)\mathrm{d}t\\ &\\&=6\pi^{3}a^{3}.\\ \end{aligned} $$ 

10.9 解 作出图形，如图 10-18 所示.

 $ \widehat{AB} $ 的方程为  $ y = x^2 + 2(0 \leq x \leq 1) $， $ \widehat{BC} $ 的方程为  $ y = 4 - x^2 (1 \leq x \leq 2) $

<div style="text-align: center;"><img src="imgs/img_in_image_box_367_590_657_798.jpg" alt="Image" width="28%" /></div>


<div style="text-align: center;">图 10-18</div>


设旋转体在区间  $ [0,1] $ 上的体积为  $ V_{1} $，在区间  $ [1,2] $ 上的体积为  $ V_{2} $，则它们的体积微元分别为

 $$ \mathrm{d}V_{1}=\pi\{3^{2}-[3-(x^{2}+2)]^{2}\}\mathrm{d}x=\pi(8+2x^{2}-x^{4})\mathrm{d}x, $$ 

 $$ \mathrm{d}V_{2}=\pi\{3^{2}-[3-(4-x^{2})]^{2}\}\mathrm{d}x=\pi(8+2x^{2}-x^{4})\mathrm{d}x. $$ 

由对称性得

 $$ \begin{aligned}V&=2(V_{1}+V_{2})=2\pi\int_{0}^{1}(8+2x^{2}-x^{4})\mathrm{d}x+2\pi\int_{1}^{2}(8+2x^{2}-x^{4})\mathrm{d}x\\&=2\pi\int_{0}^{2}(8+2x^{2}-x^{4})\mathrm{d}x=\frac{448}{15}\pi.\end{aligned} $$ 