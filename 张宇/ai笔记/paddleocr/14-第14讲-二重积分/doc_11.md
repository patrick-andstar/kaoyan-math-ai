解 应选(B).

根据所给二次积分得到积分区域为 D： $ \left\{\begin{aligned}&\sin x<y<1,\\&\frac{\pi}{2}<x<\pi,\end{aligned}\right. $ 如图 14-7 所示，则

<div style="text-align: center;"><img src="imgs/img_in_image_box_732_128_942_268.jpg" alt="Image" width="20%" /></div>


 $$ \int_{\frac{\pi}{2}}^{\pi}\mathrm{d}x\int_{\sin x}^{1}f(x,y)\mathrm{d}y=\int_{0}^{1}\mathrm{d}y\int_{\frac{\pi-\arcsin y}{\sqrt{x-x_{0}}}}^{\pi}f(x,y)\mathrm{d}x. $$ 

<div style="text-align: center;">图 14-7</div>


↘ 由例1.12得，当  $ \frac{\pi}{2} < x \leqslant \frac{3}{2}\pi $ 时， $ x = \pi - \arcsin y $

☑ 方法总结 交换积分顺序的题目，应先确定积分区域，然后交换积分顺序写成相应的累次积分.

 $$ \begin{aligned}&\begin{aligned}\\ &\int_{\frac{\pi}{2}}^{\pi}\mathrm{d}x\int_{1}^{\sin x}f(x,y)\mathrm{d}y\quad\sin x<1( 不是二重积分 , 仅是累次积分形式 )\\&\quad\\ &=-\int_{\frac{\pi}{2}}^{\pi}\mathrm{d}x\int_{\sin x}^{1}f(x,y)\mathrm{d}y\quad. 二重积分 \\ &\end{aligned}\\ \end{aligned} $$ 

例 14.6 当  $ x \to 0^{+} $ 时， $ f(x) = \int_{0}^{x^{2}} \mathrm{d}y \int_{x}^{\sqrt{y}} \sin \frac{y}{t} \mathrm{d}t $ 与  $ g(x) = ax^{b} $ 是等价无穷小量，则  $ ab = $ ___.

分析  $ \sin\frac{y}{x} $ 若对 x 积分，则没有初等函数形式的原函数表达，若对 y 积分，可用初等函数形式表示，所以先积 y 后积 x，本题属于交换积分顺序的题目.

又因为  $ 0 \leqslant y \leqslant x^{2} $，所以  $ \sqrt{y} \leqslant x $，故  $ \int_{0}^{x^{2}} dy \int_{x}^{\sqrt{y}} \sin \frac{y}{t} dt $ 先添一个负号变为  $ -\int_{0}^{x^{2}} dy \int_{\sqrt{y}}^{x} \sin \frac{y}{t} dt $，变为二重积分后，画出积分区域图，再交换积分顺序。

解 应填  $ -\frac{1}{2} $

交换上下限，保证上限大于等于下限

 $$ \begin{aligned}f(x)&=\int_{0}^{x^{2}}\mathrm{d}y\int_{\frac{y}{x}}^{\sqrt{y}}\sin\frac{y}{t}\mathrm{d}t=-\int_{0}^{x^{2}}\mathrm{d}y\int_{\frac{y}{x}}^{\sqrt{y}}\sin\frac{y}{t}\mathrm{d}t\\&=-\iint_{D}\sin\frac{y}{t}\mathrm{d}\sigma=-\int_{0}^{x}\mathrm{d}t\int_{0}^{t^{2}}\sin\frac{y}{t}\mathrm{d}y\\&=\int_{0}^{x}t\cdot\left(\cos\frac{y}{t}\right)\Bigg|_{y=0}^{y=t^{2}}\mathrm{d}t\end{aligned} 注意给哪个变量代上下限 . $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_716_830_911_1011.jpg" alt="Image" width="18%" /></div>


 $$ \sim-\frac{1}{2}x^{2} $$ 

于是  $ \lim_{x\to0^{+}}\frac{f(x)}{g(x)}=\lim_{x\to0^{+}}\frac{x(\cos x-1)}{abx^{b-1}}=\lim_{x\to0^{+}}\frac{-\frac{1}{2}x^{3}}{abx^{b-1}}=1 $ ，故  $ ab=-\frac{1}{2} $

注 (1)  $ \frac{\sin x}{x}, \frac{\cos x}{x}, \frac{\ln(1+x)}{x}, \frac{1}{\ln x}, \sin x^2, \cos x^2, \sin \frac{1}{x}, \cos \frac{1}{x}, \frac{\tan x}{x}, \frac{e^x}{x}, \tan x^2, e^{ax^2 + bx + c} (a \neq 0) $

均没有初等函数形式的原函数，见到它们，一般都要交换积分次序，避免先对x求积分。

(2)事实上， $ a=-\frac{1}{8} $，b=4.