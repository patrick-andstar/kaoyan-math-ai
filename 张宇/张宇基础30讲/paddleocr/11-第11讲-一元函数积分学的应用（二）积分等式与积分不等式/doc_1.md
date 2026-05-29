证明，可用函数的单调性（见例 11.7）、拉格朗日中值定理（见例 11.8）、泰勒公式（见例 11.9）、积分法（见例 11.10）与牛顿－莱布尼茨公式（见例 11.11）来解决。

## 积分等式

<div style="text-align: center;"><img src="imgs/img_in_image_box_835_211_939_318.jpg" alt="Image" width="10%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_122_338_156_367.jpg" alt="Image" width="3%" /></div>


## 用中值定理

 $ g(x) $ 恒正，恒负或恒为0

例 11.1 (1) 设  $ f(x) $,  $ g(x) $ 在  $ [a, b] $ 上连续，且  $ g(x) $ 在  $ [a, b] $ 上不变号，证明：存在  $ \xi \in (a, b) $，使得

 $ \int_{a}^{b}f(x)g(x)\mathrm{d}x=f(\xi)\int_{a}^{b}g(x)\mathrm{d}x; $ 推广的积分中值定理（考试可直接使用）

当  $ g(x)=1>0 $ 时，即  $ \int_{a}^{b}f(x)dx=f(\xi)(b-a) $， $ \xi\in[a,b] $（积分中值定理）

★★★★(2)设 $ f(x) $在 $ [1,2] $上连续，计算 $ \lim_{n\to\infty}\int_{1}^{2}f(x)e^{-x^n}dx $。 $ \lim_{n\to\infty}\int_{1}^{2}\neq\int_{a}^{b}\lim_{n\to\infty} $

(1) 证 若  $ g(x)=0 $，结论显然成立；

若  $ g(x) \neq 0 $，由于不变号，不妨设  $ g(x) > 0 $ 。令

 $$ F(x)=\int_{a}^{x}f(t)g(t)\mathrm{d}t,\quad G(x)=\int_{a}^{x}g(t)\mathrm{d}t, $$ 

在  $ [a, b] $ 上应用柯西中值定理，有  $ \frac{F(b) - F(a)}{G(b) - G(a)} = \frac{F'(\xi)}{G'(\xi)} $，即

 $$ \frac{\int_{a}^{b}f(x)g(x)\mathrm{d}x-0}{\int_{a}^{b}g(x)\mathrm{d}x-0}=\frac{f(\xi)g(\xi)}{g(\xi)}=f(\xi), $$ 

 $$ \int_{a}^{b}f(x)g(x)\mathrm{d}x=f(\xi)\int_{a}^{b}g(x)\mathrm{d}x,\xi\in(a,b), $$ 

其中 $ \int_{a}^{b}g(x)dx>0 $．同理可得 $ g(x)<0 $时成立．得证．

利用积分保号性  $ g(x)>0 $ 见注(2)

(2) 解 由 (1) 知， $ \int_{1}^{2}f(x)\mathrm{e}^{\frac{1}{x}}dx=f(\xi_{n})\int_{1}^{2}\mathrm{e}^{-x^{n}}dx $， $ 1<\xi_{n}<2 $。因  $ f(x) $ 在  $ [1,2] $ 上连续，则  $ f(\xi_{n}) $ 有界；又在  $ (1,2) $ 内， $ \underline{e}^{x^{n}}>x^{n}+1>0 $，即  $ \frac{1}{x^{n}}<\frac{1}{x^{n}+1}<\frac{1}{x^{n}} $。

于是

 $$ 0<\int_{1}^{2}\mathrm{e}^{-x^{n}}\mathrm{d}x<\int_{1}^{2}x^{-n}\mathrm{d}x=\frac{1}{1-n}x^{1-n}\bigg|_{1}^{2}=\frac{1}{1-n}(2^{1-n}-1)\Rightarrow 积分保号性 $$ 

 $$ \lim_{n\to\infty}\frac{1}{1-n}(2^{1-n}-1)=0 $$ 

由夹逼准则得  $ \lim_{n\to\infty}\int_{1}^{2}e^{-x^n}dx=0 $ 。故  $ \lim_{n\to\infty}\int_{1}^{2}f(x)e^{-x^n}dx=\lim_{n\to\infty}f(\xi_n)\lim_{n\to\infty}\int_{1}^{2}e^{-x^n}dx=0 $ 。有界 × 无穷小量