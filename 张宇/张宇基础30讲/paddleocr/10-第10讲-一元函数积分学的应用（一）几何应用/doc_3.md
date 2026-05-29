## 考研数学基础30讲·高等数学分册

♡分析 ①画出摆线（考试不会给出图！！！）.

②按照直角坐标系去理解参数方程，套直角坐标系下的面积公式进行计算。

 $$ \begin{cases}x=x(t),\\y=y(t)\stackrel{}{\underset{}{\downarrow}{\rightarrow}}y=f(x)=f[x(t)]=y(t)\end{cases}. $$ 

比如： $ \left\{\begin{aligned}x=2t,\\ y=t^{2}\end{aligned}\right.\Rightarrow y=\frac{1}{4}x^{2}=f(x)=f[x(t)]=\frac{1}{4}(2t)^{2}=t^{2}=y(t) $

 $$ S=\int_{a}^{b}f(x)\mathrm{d}x\xlongequal{x=x(t)}\int_{x^{-1}(a)}^{x^{-1}(b)}f[x(t)]\mathrm{d}[x(t)]=\int_{\alpha}^{\beta}y(t)x^{\prime}(t)\mathrm{d}t. $$ 

解 当 t=0 或  $ t=2\pi $ 时，y=0 。故当 t 由 0 变到  $ 2\pi $ 时，曲线正好成一拱，所以

 $$ \begin{aligned}S&=\int_{0}^{2\pi}y(x)\mathrm{d}x\xlongequal{x=a(t-\sin t)}\int_{0}^{2\pi}a(1-\cos t)[a(t-\sin t)]^{^{\prime}}\mathrm{d}t\\&=\int_{0}^{2\pi}a^{2}(1-\cos t)^{2}\mathrm{d}t=a^{2}\int_{0}^{2\pi}(1-2\cos t+\cos^{2}t)\mathrm{d}t\\&=a^{2}\int_{0}^{2\pi}\mathrm{d}t-2a^{2}\int_{0}^{2\pi}\cos t\mathrm{d}t+a^{2}\int_{0}^{2\pi}\cos^{2}t\mathrm{d}t\\&=2a^{2}\pi+4a^{2}\int_{0}^{\frac{\pi}{2}}\cos^{2}t\mathrm{d}t=3a^{2}\pi.\end{aligned} $$ 

☑ 方法总结 参数方程下面积公式的本质：直角坐标系下的面积公式的换元法形式.

例 10.3 伯努利双纽线  $ r^2 = a^2 \cos 2\theta $ 围成的图形的面积为 ___.

分析 ①画图。②套公式，做计算（借助对称性简化计算）.

解 应填 $ a^{2} $

如图 10-3 所示，利用对称性，所求图形面积是阴影部分面积的 4 倍。

阴影部分的图形由射线  $ \theta = 0, \theta = \frac{\pi}{4} $ 与伯努利双纽线  $ r^{2} = a^{2} \cos 2\theta $ 围成，于是所求的平面图形面积为

<div style="text-align: center;"><img src="imgs/img_in_image_box_718_961_925_1118.jpg" alt="Image" width="20%" /></div>


 $$ S=4\int_{0}^{\frac{\pi}{4}}\frac{1}{2}a^{2}\cos2\theta\mathrm{d}\theta=a^{2}\sin2\theta\Big|_{0}^{\frac{\pi}{4}}=a^{2}. $$ 

<div style="text-align: center;">图 10-3</div>


例 10.4 求曲线  $ y = e^{-x} \sin x (x \geq 0) $ 与 x 轴所围平面图形的面积.

♡分析 ①画图：如图 10-4 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_330_1264_675_1356.jpg" alt="Image" width="33%" /></div>


<div style="text-align: center;">图 10-4</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_686_1286_804_1343.jpg" alt="Image" width="11%" /></div>
