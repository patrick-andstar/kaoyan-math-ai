☑ 方法总结 当累次积分无法积分，即没有初等函数形式的原函数表达式时，可考虑交换积分顺序.

公式  $ \int\sin\frac{y}{t}dy=-t\cos\frac{y}{t}+C $

当  $ x \to 0^{+} $ 时， $ f(x) \sim g(x) $，则  $ \int_{0}^{x} f(t) dt \sim \int_{0}^{x} g(t) dt $。（可用洛必达法则证明）

例 14.7 计算  $ \int_{0}^{1} dy \int_{y}^{1} \arcsin \sqrt{4x - 4x^{2}} dx $.

♡分析 被积函数只含有x，而且先对x积分较困难，所以考虑交换积分顺序.

解 先对 x 积分较困难，交换积分次序.

 $$ \begin{aligned} 原式 =&\int_{0}^{1}\mathrm{d}x\int_{0}^{x}\arcsin\sqrt{4x-4x^{2}}\mathrm{d}y\\=&\int_{0}^{1}x\arcsin\sqrt{4x-4x^{2}}\mathrm{d}x=\frac{1}{2}\end{aligned}\xrightarrow{ 由例 9.15 知 } $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_810_412_945_541.jpg" alt="Image" width="13%" /></div>


方法总结  $ \int_{c}^{d}dy\int_{x_{1}(y)}^{x_{2}(y)}f(x)dx $ 对 x 积分比较困难时，可转化为先积 y，即  $ \int_{a}^{b}dx\int_{y_{1}(x)}^{y_{2}(x)}f(x)dy $

公式  $ \int_{0}^{1}\arcsin\sqrt{1-x^{2}}dx=1,\quad\int_{0}^{1}x\arcsin\sqrt{4x-4x^{2}}dx=\frac{1}{2} $

## 极坐标系下的计算方法

因为是中心对称图像，一般先积r，后积θ

极坐标系：与中心对称图像有关!

直角坐标与极坐标关系 $ \begin{cases} x=r\cos\theta, \\ y=r\sin\theta. \end{cases} $→转换桥梁

 $$ r=r_{0},\quad\theta=\theta_{0} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_592_725_825_914.jpg" alt="Image" width="22%" /></div>


则有  $ \mathrm{d}\sigma = \mathrm{d}r \cdot r \mathrm{d}\theta = r \mathrm{d}r \mathrm{d}\theta $ 近似看成矩形。

<div style="text-align: center;"> $ (r, \theta) $</div>


在极坐标系下，按照积分区域与极点位置关系的不同，一般将二重积分的计算分为三种情况，如图 14-8 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_242_1010_402_1108.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_454_999_623_1113.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_669_1003_786_1123.jpg" alt="Image" width="11%" /></div>


<div style="text-align: center;">(c)</div>


<div style="text-align: center;">图 14-8</div>


从 Ox 轴逆时针出发，先碰到积分区域时，记  $ \theta = \alpha $，后离开区域时，记  $ \theta = \beta $，所以  $ \theta $ 的下限为  $ \alpha $，上限为  $ \beta $，然后限内画条线，先交内曲线记  $ r = r_{1}(\theta) $，然后交外曲线  $ r = r_{2}(\theta) $

(1)  $ \iint_{D}f(x,y)\mathrm{d}\sigma=\int_{\alpha}^{\beta}\mathrm{d}\theta\int_{\eta_{1}(\theta)}^{\eta_{2}(\theta)}f(r\cos\theta,r\sin\theta)r\mathrm{d}r $ （极点 O 在区域 D 外部）；

(2)  $ \iint_{D}f(x,y)\mathrm{d}\sigma=\int_{\alpha}^{\beta}\mathrm{d}\theta\int_{0}^{r(\theta)}f(r\cos\theta,r\sin\theta)r\mathrm{d}r $（极点 O 在区域 D 边界上）；