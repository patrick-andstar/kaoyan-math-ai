<div style="text-align: center;"><img src="imgs/img_in_image_box_98_128_166_199.jpg" alt="Image" width="6%" /></div>


## 基础内容精讲

## 基本求导公式

<div style="text-align: center;"><img src="imgs/img_in_image_box_845_218_947_325.jpg" alt="Image" width="9%" /></div>


以下公式要熟记.

 $ (x^{\circ})^{\prime}=\alpha x^{\alpha-1} $ ( $ \alpha $ 为常数)， $ \frac{(a^{x})^{\prime}=a^{x}\ln a(a>0,a\neq1)} $， $ \left(\mathrm{e}^{x}\right)^{\prime}=\mathrm{e}^{x} $， $ \left(\log_{a}x\right)^{\prime}=\frac{1}{x\ln a} $ ( $ a>0,a\neq1 $)， $ \frac{\sqrt{(a^{x})^{\prime\prime}=(a^{x}\ln a)^{\prime}=a^{x}(\ln a)^{2}} $，根据规律得： $ (a^{x})^{(n)}=a^{x}(\ln a)^{n} $， $ \left(\mathrm{e}^{x}\right)^{(n)}=\mathrm{e}^{x} $



(类似地，后面的高阶导数也可以用归纳法去推导)

 $ \left(\ln|x|\right)^{\prime}=\left\{\begin{aligned}&(\ln x)^{\prime},&x>0,\\&[\ln(-x)]^{\prime}=-\frac{1}{x}\cdot(-1),&x<0\end{aligned}\right. $  $ \frac{1}{x}=-\frac{1}{x}(x\neq0) $，视绝对值符号而不见！ $ \left[\ln|u(x)|\right]^{\prime}=\left\{\begin{aligned}&[\ln u(x)]^{\prime}=\frac{1}{u(x)}\cdot u^{\prime}(x),\\&[\ln(-u(x))]^{\prime}=-\frac{1}{u(x)}[-u^{\prime}(x)]=\frac{u^{\prime}(x)}{u(x)}\end{aligned}\right. $

复合函数

 $$ \left(\ln|x|\right)^{\prime}=\frac{1}{x},\left[\left(\sin x\right)^{\prime}=\cos x,\left(\cos x\right)^{\prime}=-\sin x,\left(\arcsin x\right)^{\prime}=\frac{1}{\sqrt{1-x^{2}}}\right. $$ 

 $$ \left(\arccos x\right)^{\prime}=-\frac{1}{\sqrt{1-x^{2}}}\ ,\left(\tan x\right)^{\prime}=\sec^{2}x,\left(\cot x\right)^{\prime}=-\csc^{2}x,\left(\arctan x\right)^{\prime}=\frac{1}{1+x^{2}}, $$ 

 $$ \left(\operatorname{arccot} x\right)^{\prime}=-\frac{1}{1+x^{2}},\left(\sec x\right)^{\prime}=\sec x\tan x,\left(\csc x\right)^{\prime}=-\csc x\cot x,\left\lbrack 三角函数求导公式 \right. $$ 

 $$ \left[\ln(x+\sqrt{x^{2}+1})\right]^{\prime}=\frac{1}{\sqrt{x^{2}+1}},\left[\ln(x+\sqrt{x^{2}-1})\right]^{\prime}=\frac{1}{\sqrt{x^{2}-1}}. $$ 

## 2 四则运算

若以下函数均可导，则

 $$ -\frac{d}{dx} $$ 

和、差的导数（微分） $ [u(x) \pm v(x)]' = u'(x) \pm v'(x) $， $ \mathrm{d}[u(x) \pm v(x)] = \mathrm{d}[u(x)] \pm \mathrm{d}[v(x)] $。

积的导数 (微分)  $ [u(x)v(x)]' = u'(x)v(x) + u(x)v'(x), d[u(x)v(x)] = u(x)d[v(x)] + v(x)d[u(x)]. $

注 (1) 函数乘积求导公式的证明，设  $ f(x) = u(x)v(x) $. (2015 年考研考过)

 $$ \begin{aligned}f^{\prime}(x_{0})&=\lim_{x\to x_{0}}\frac{f(x)-f(x_{0})}{x-x_{0}}\\&=\lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x)-f(x_{0})}{\Delta x}\end{aligned} $$ 

 $$ f^{\prime}(x)=\left[u(x)v(x)\right]^{\prime}=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}\xrightarrow{\text{泛指点}} 接受义写 $$ 