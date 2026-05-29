14.11 解 积分区域 D 为图 14-17 中阴影部分，转换成直角坐标系进行计算.

 $$ I=\iint_{D}x\mathrm{e}^{-y^{2}}\mathrm{d}x\mathrm{d}y=\int_{0}^{+\infty}\mathrm{e}^{-y^{2}}\mathrm{d}y\int_{0}^{y}x\mathrm{d}x=\frac{1}{2}\int_{0}^{+\infty}y^{2}\mathrm{e}^{-y^{2}}\mathrm{d}y\xlongequal{ 由例 14.12}\frac{\sqrt{\pi}}{8} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_825_127_947_226.jpg" alt="Image" width="11%" /></div>


<div style="text-align: center;">图 14-17</div>


14.12 解 (1) 由二重积分的性质可知，当积分区域 D 包含了所有使被积函数  $ 1 - 2x^2 - y^2 $ 大于等于零的区域，而不包含使被积函数  $ 1 - 2x^2 - y^2 $ 小于零的区域，即当 D 是椭圆  $ 2x^2 + y^2 = 1 $ 所围的平面闭区域时，此二重积分的值达到最大.

(2) 由 (1) 知  $ D=\left\{(x,y)\mid2x^{2}+y^{2}\leq1\right\} $，此时令  $ \left\{\begin{aligned}x=\frac{1}{\sqrt{2}}r\cos\theta,\\ y=r\sin\theta,\end{aligned}\right. $ 则

 $$ \begin{aligned}\iint\limits_{D}(1-2x^{2}-y^{2})\mathrm{d}\sigma=&\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}(1-r^{2}\cos^{2}\theta-r^{2}\sin^{2}\theta)\bullet\left|\begin{matrix}\frac{\partial x}{\partial r}&\frac{\partial x}{\partial\theta}\\ \frac{\partial y}{\partial r}&\frac{\partial y}{\partial\theta}\end{matrix}\right|\mathrm{d}r\\=&\int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{1}(1-r^{2})\frac{1}{\sqrt{2}}r\mathrm{d}r\\=&2\pi\bullet\frac{1}{\sqrt{2}}\int_{0}^{1}(r-r^{3})\mathrm{d}r\\=&\sqrt{2}\pi\left(\frac{1}{2}r^{2}-\frac{1}{4}r^{4}\right)\bigg|_{0}^{1}=\frac{\sqrt{2}\pi}{4}.\end{aligned} $$ 