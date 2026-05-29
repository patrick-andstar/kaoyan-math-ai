方法二 可用常数 k 来证明  $ \int_{a}^{b} f(x) \, dx = f(\xi)(b - a) $.

令  $ k=\frac{\int_{a}^{b}f(x)dx}{b-a} $，设  $ F(x)=\int_{a}^{x}f(t)dt-k(x-a) $，则  $ F(b)=F(a)=0 $，故由罗尔定理知，存在  $ \xi\in(a,b) $，使  $ F'(\xi)=0 $，故  $ \int_{a}^{b}f(x)dx=f(\xi)(b-a) $.

考研真题中已经考过，可直接在大题中使用，不必证明。

例 8.9 设  $ I_{1}=\int_{0}^{\frac{\pi}{4}}\frac{\tan x}{x}dx $,  $ I_{2}=\int_{0}^{\frac{\pi}{4}}\frac{x}{\tan x}dx $，则（）.

(A)  $ I_{1}>I_{2}>1 $

(B)  $ 1>I_{1}>I_{2} $

(C)  $ I_{2}>I_{1}>1 $

(D)  $ 1>I_{2}>I_{1} $

解 应选(B).

方法一 当  $ x \in \left(0, \frac{\pi}{4}\right) $ 时， $ 0 < \sin x < x < \tan x $，故  $ \frac{\tan x}{x} > \frac{x}{\tan x} $，则

 $$ I_{1}=\int_{0}^{\frac{\pi}{4}}\frac{\tan x}{x}\mathrm{d}x>\int_{0}^{\frac{\pi}{4}}\frac{x}{\tan x}\mathrm{d}x=I_{2}. $$ 

这便排除了选项(C)和(D).

由第2讲“6. 注(2)⑦”重要不等式可知，当  $ 0 < x < \frac{\pi}{4} $ 时， $ \frac{\tan x}{x} < \frac{4}{\pi} $，则有  $ I_{1} = \int_{0}^{\frac{\pi}{4}} \frac{\tan x}{x} \, dx < \frac{4}{\pi} \int_{0}^{\frac{\pi}{4}} dx = 1 $。故(B)正确。

方法二

 $$ I_{2}-I_{1}=\int_{0}^{\frac{\pi}{4}}\frac{x}{\tan x}-\frac{\tan x}{x}\mathrm{d}x=\int_{0}^{\frac{\pi}{4}}\frac{(x+\tan x)(x-\tan x)}{x\tan x}\mathrm{d}x $$ 

由积分的保号性，可知当 $ x\in\left(0,\frac{\pi}{4}\right) $时， $ x-\tan x<0 $，故 $ I_{2}-I_{1}<0 $，即 $ I_{2}<I_{1} $。

令 $ g(x)=\frac{\tan x}{x} $，则 $ g'(x)=\frac{x\sec^{2}x-\tan x}{x^{2}}=\frac{x-\sin x\cdot\cos x}{x^{2}\cos^{2}x} $

当 $ x\in\left(0,\frac{\pi}{4}\right) $时， $ g'(x)>0 $，故 $ g(x) $单调递增，则

 $$ g(x)<g\left(\frac{\pi}{4}\right)=\frac{4}{\pi}, $$ 

即 $ I_{1}<1 $，故 $ I_{2}<I_{1}<1 $。因此选(B)。

例8.10 设  $ M = \int_{0}^{\frac{\pi}{2}} \sin(\sin x) \, dx $,  $ N = \int_{0}^{\frac{\pi}{2}} \cos(\cos x) \, dx $，则（）.

(A) M < 1 < N

(B) M < N < 1