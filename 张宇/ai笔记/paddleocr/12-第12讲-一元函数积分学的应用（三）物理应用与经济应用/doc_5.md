 $$ \Delta m_{i}=\rho(\xi_{i})\Delta s_{i},\Delta M_{i l_{0}}=r_{i}\rho(\xi_{i})\Delta s_{i}, $$ 

故总力矩为

 $$ \begin{align*}M_{L_{0}}=&\lim_{n\to\infty}\sum_{i=1}^{n}\Delta M_{iL_{0}}=\lim_{n\to\infty}\sum_{i=1}^{n}r_{i}\rho(\xi_{i})\Delta s_{i}=\int_{a}^{b}\frac{\left|ax+by+c\right|}{\sqrt{a^{2}+b^{2}}}\rho(x)\mathrm{d}s\\=&\int_{a}^{b}\frac{\left|ax+by+c\right|}{\sqrt{a^{2}+b^{2}}}\rho(x)\sqrt{1+\left[f^{\prime}(x)\right]^{2}}\mathrm{d}x.\end{align*} $$ 

当 $ \rho= $常数时，则有

 $$ r(\overline{x},\overline{y})=\frac{M_{L_{0}}}{M}=\frac{\int_{a}^{b}\frac{\left|ax+by+c\right|}{\sqrt{a^{2}+b^{2}}}\sqrt{1+\left[f^{\prime}(x)\right]^{2}}\mathrm{d}x}{\int_{a}^{b}\sqrt{1+\left[f^{\prime}(x)\right]^{2}}\mathrm{d}x}, $$ 

其中  $ r(\overline{x}, \overline{y}) $ 指形心  $ (\overline{x}, \overline{y}) $ 到直线  $ L_{0} $ 的距离.

<div style="text-align: center;"><img src="imgs/img_in_image_box_289_618_523_796.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_532_568_764_791.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 12-8</div>


## 3 古鲁金第一定理

如图 12-9 所示，将曲线段  $ L $ 任意切分成  $ n $ 段， $ \Delta s_i (i=1,2,\cdots,n) $ 为每一小段的长度，在  $ \Delta s_i $ 上任取一点  $ (\xi, \eta_i) $，记  $ \lambda = \max_{i} \{\Delta s_i\} $，则  $ \Delta s_i $ 绕直线  $ L_0 $ 旋转一周的侧面积为

 $$ \Delta A_{i}=2\pi r_{i}\Delta s_{i}=2\pi\bullet\frac{\left|a\xi_{i}+b\eta_{i}+c\right|}{\sqrt{a^{2}+b^{2}}}\Delta s_{i}, $$ 

故曲线段 L 绕直线  $ L_{0} $ 旋转一周的侧面积为

 $$ \begin{aligned}A=&\lim_{\lambda\rightarrow0}\sum_{i=1}^{n}\Delta A_{i}=\lim_{\lambda\rightarrow0}2\pi\bullet\frac{\left|a\xi_{i}+b\eta_{i}+c\right|}{\sqrt{a^{2}+b^{2}}}\Delta s_{i}\\=&\int_{a}^{b}2\pi\bullet\frac{\left|a x+b y+c\right|}{\sqrt{a^{2}+b^{2}}}\sqrt{1+\left[f^{\prime}(x)\right]^{2}}\mathrm{d}x.\end{aligned} $$ 

与公式 $  (12-2)  $比较，得

 $$ r(\overline{x},\overline{y})=\frac{M_{L_{0}}}{M}=\frac{2\pi M_{L_{0}}}{2\pi M}=\frac{A}{2\pi\bullet l}, $$ 