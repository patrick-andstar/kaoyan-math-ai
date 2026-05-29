 $$ \begin{aligned}&(1+x^{2})y^{2}=x^{2}\\ \Rightarrow&y^{2}+x^{2}y^{2}-x^{2}=0\\ \Rightarrow&x^{2}(y^{2}-1)=-y^{2}\\ \Rightarrow&x=\frac{y}{\sqrt{1-y^{2}}}\end{aligned} $$ 

 $$ f(x)=\frac{x}{\sqrt{1+x^{2}}}(x>0)\ . $$ 

由  $ y=\frac{x}{\sqrt{1+x^{2}}} $ 得  $ x=\frac{y}{\sqrt{1-y^{2}}} $ (0 < y < 1)，从而  $ y=f(x) $， $ y=\frac{1}{2} $， $ y=\frac{\sqrt{3}}{2} $ 及 y 轴所围图形绕 x 轴旋转一周所成旋转体的体积为

 $$ x=\varphi(y) $$ 

 $$ \begin{aligned}&V=2\pi\int_{\frac{1}{2}}^{\frac{\sqrt{3}}{2}}x y\mathrm{d}y=2\pi\int_{\frac{1}{2}}^{\frac{\sqrt{3}}{2}}\frac{y^{2}}{\sqrt{1-y^{2}}}\mathrm{d}y\\ &\begin{aligned}\\ &\xlongequal{ 令 y=\sin t}2\pi\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}\sin^{2}t\mathrm{d}t=2\pi\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}\frac{1-\cos2t}{2}\mathrm{d}t\\&=\frac{\pi^{2}}{6}.\\ &\end{aligned}\\ \end{aligned} $$ 

☑ 方法总结 学会利用反函数，将绕 x 轴旋转用  $ V_{y} $ 的体积公式表示出来.

注 此题增加了2个综合性考查： $ \begin{cases} ①\text{要把}f(x)\text{求出来}. \\ ②x,\ y\text{地位交换，先反解，再套公式计算}. \end{cases} $

(3)平面曲线绕定直线旋转. 套公式 若出现2个及以上的交点，则不适用，如平面曲线L:  $ y=f(x) $， $ a\leq x\leq b $，且 $ f(x) $可导.

<div style="text-align: center;"><img src="imgs/img_in_image_box_814_775_965_867.jpg" alt="Image" width="14%" /></div>


定直线  $ L_{0} $ ： $ Ax + By + C = 0 $ ，且过  $ L_{0} $ 的任一条垂线与 L 至多有一个交点，如图 10-6 所示，则 L 绕  $ L_{0} $ 旋转一周所得旋转体的体积为

 $$ \star V=\frac{\pi}{\left(A^{2}+B^{2}\right)^{\frac{3}{2}}}\int_{a}^{b}\left[Ax+Bf(x)+C\right]^{2}\left|Af^{\prime}(x)-B\right|\mathrm{d}x. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_444_1043_627_1180.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">图 10-6</div>


特别地，若 A = C = 0,  $ B \neq 0 $，则  $ L_{0} $ 为 y = 0 (x 轴)，如图 10-7 所示，L 绕  $ L_{0} $ 旋转一周所得旋转体的体积为

 $$ \begin{aligned}V=\pi\int_{a}^{b}f^{2}(x)\mathrm{d}x&\xrightarrow{}\boldsymbol{V}=\frac{\pi}{\left(B^{2}\right)^{\frac{3}{2}}}\int_{a}^{b}\left[B f(x)\right]^{2}\left|-B\right|\mathrm{d}x\\&=\frac{\pi}{\left|B\right|^{3}}\int_{a}^{b}B^{2}\left|B\right|f^{2}(x)\mathrm{d}x=\pi\int_{a}^{b}f^{2}(x)\mathrm{d}x\end{aligned} $$ 