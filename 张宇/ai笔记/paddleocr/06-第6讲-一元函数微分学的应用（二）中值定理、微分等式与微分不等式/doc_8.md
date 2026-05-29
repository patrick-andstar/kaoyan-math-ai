(A)  $ xf(x) > af(a) $ (B)  $ bf(b) > xf(x) $ (C)  $ xf(a) > af(x) $ (D)  $ xf(b) > BF(x) $

解 应选(D).

令  $ g(x)=xf(x) $，x>0，则  $ g'(x)=f(x)+xf'(x)<0 $， $ g(x) $ 单调减少，故当 0<a<x<b 时， $ g(b)<g(x)<g(a) $，即  $ bf(b)<xf(x)<af(a) $，选项 (A)，(B) 错误。

再令  $ h(x)=\frac{f(x)}{x} $，x>0，则

 $$ \begin{aligned}h^{\prime}(x)&=\frac{xf^{\prime}(x)-f(x)}{x^{2}}\quad\begin{aligned}& 判断不出 f,xf^{\prime} 的关系 .\\& 想到拉格朗日中值定理 \end{aligned}\\ &=\frac{xf^{\prime}(x)-\left[f(x)-f(0)\right]}{x^{2}}=\frac{xf^{\prime}(x)-f^{\prime}(\xi)\cdot x}{x^{2}}\\ &=\frac{f^{\prime}(x)-f^{\prime}(\xi)>0}{x},\\ \end{aligned} $$ 

其中  $ 0 < \xi < x $ 。由  $ f''(x) > 0 $ ，知  $ f'(x) $ 单调增加， $ f'(x) > f'(\xi) $ ，则  $ h'(x) > 0, h(x) $ 单调增加，故当 0 < a < x < b 时， $ h(a) < h(x) < h(b) $ ，即  $ \frac{f(a)}{a} < \frac{f(x)}{x} < \frac{f(b)}{b} $ ，也即  $ af(x) > xf(a), xf(b) > bf(x) $ ，选项 (C) 错误，选 (D).

定理 8（柯西中值定理）用参数方程来表达

①在 $ [a,b] $上连续，

设 $ f(x) $， $ g(x) $满足

②在 $ (a,b) $内可导，则存在 $ \xi\in(a,b) $，使得

③ $ g'(x)\neq0 $，

法国科学院院长拉格朗日（欧拉姆学生）的学生，微积分收官人之一。

数学故事：拉格朗日让其父亲答应柯西15岁前

不学数学，15岁后拉格朗日亲自来教





<div style="text-align: center;"><img src="imgs/img_in_image_box_829_674_920_848.jpg" alt="Image" width="8%" /></div>


<div style="text-align: center;">柯西</div>


★往往考查一个具体函数，一个抽象函数

 $$ \frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f^{\prime}(\xi)}{g^{\prime}(\xi)}\xrightarrow{同} $$ 

(1789—1857)

“参数方程  $ \begin{cases} x = g(t), \\ y = f(t) \end{cases} $ 求导而来”

例 6.11 设  $ f(x) $ 在  $ [a, b] $ 上连续，在  $ (a, b) $ 内可导， $ 0 < a < b $，证明：至少存在一点  $ \xi \in (a, b) $，使得  $ f(b) - f(a) = \xi \ln \frac{b}{a} f'(\xi) $。

证 因为  $ f(x) $ 与  $ g(x)=\ln x $ 在  $ [a,b] $ 上连续，在  $ (a,b) $ 内可导，且  $ g'(x)=\frac{1}{x}\neq0(0<a<x<b) $，即  $ f(x) $ 与  $ g(x)=\ln x $ 在  $ [a,b] $ 上满足柯西中值定理的条件，则至少存在一点  $ \xi\in(a,b) $，使得

 $$ \frac{f(b)-f(a)}{\ln b-\ln a}=\frac{f^{\prime}(\xi)}{\frac{1}{\xi}}, $$ 

即

 $$ f(b)-f(a)=\xi\ln\frac{b}{a}f^{\prime}(\xi)\ . $$ 