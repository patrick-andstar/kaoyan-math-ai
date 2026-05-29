 $$ =\int_{a}^{b}f(a+b-t)\mathrm{d}t=\int_{a}^{b}f(a+b-x)\mathrm{d}x, $$ 

证毕。

注 $ ^{(1)} $此结论的证明过程比较简单，但其用处很大.

(2) 若  $ f(x) $ 复杂， $ f(x) + f(a + b - x) $ 简单，则考虑  $ \int_{a}^{b} f(x) \, dx = \int_{a}^{b} \frac{f(x) + f(a + b - x)}{2} \, dx $ 比如

 $$ \begin{aligned}\int_{0}^{\frac{\pi}{4}}\ln(1+\tan x)\mathrm{d}x=&\int_{0}^{\frac{\pi}{4}}\ln\left[1+\tan\left(\frac{\pi}{4}-x\right)\right]\mathrm{d}x=\int_{0}^{\frac{\pi}{4}}\ln\frac{2}{1+\tan x}\mathrm{d}x\\=&\int_{0}^{\frac{\pi}{4}}\frac{\ln(1+\tan x)+\ln\frac{2}{1+\tan x}}{2}\mathrm{d}x=\frac{\pi}{8}\ln2.\end{aligned} $$ 

例 9.18 设  $ f(x) $ 在  $ [0,1] $ 上连续，证明  $ \int_{0}^{\pi} x f(\sin x) dx = \frac{\pi}{2} \int_{0}^{\pi} f(\sin x) dx $，并计算  $ \int_{0}^{\pi} x \sin^9 x dx $。

分析  $ \int_{0}^{\pi} x f(\sin x) dx \xrightarrow{\text{难算}} \text{区间再现} $。

解 令  $ x = \pi - t $，作区间再现换元，有

 $$ \begin{aligned}\int_{0}^{\pi}x f(\sin x)\mathrm{d}x&=\int_{\pi}^{0}(\pi-t)f[\sin(\pi-t)](-\mathrm{d}t)\\&=\int_{0}^{\pi}(\pi-t)f(\sin t)\mathrm{d}t=\int_{0}^{\pi}(\pi-x)f(\sin x)\mathrm{d}x\\&=\pi\int_{0}^{\pi}f(\sin x)\mathrm{d}x-\int_{0}^{\pi}x f(\sin x)\mathrm{d}x\ ,\end{aligned} $$ 

故

 $$ \int_{0}^{\pi}x f(\sin x)\mathrm{d}x=\frac{\pi}{2}\int_{0}^{\pi}f(\sin x)\mathrm{d}x\quad. $$ 

 $$ \int_{0}^{\pi}x\sin^{9}x\mathrm{d}x=\frac{\pi}{2}\int_{0}^{\pi}\sin^{9}x\mathrm{d}x=\pi\times\frac{8}{9}\times\frac{6}{7}\times\frac{4}{5}\times\frac{2}{3}=\frac{128\pi}{315}. $$ 

★例9.19 设 $ f(x)=\int_{1}^{x}e^{-t^{2}}dt $，则 $ \int_{0}^{1}xf(x)dx= $（）.

(A)  $ \frac{1}{4}(e^{-1}+1) $ (B)  $ \frac{1}{4}(e^{-1}-1) $ (C)  $ \frac{1}{4}(e+1) $ (D)  $ \frac{1}{4}(e-1) $

分析 ① 可积不可求积函数见例 14.6 的注；

②变限积分求导公式见“四、变限积分的计算”；

③ $ \int u\,dv = uv - \int v\,du $（不可求积先求导）.

解 应选(B).

由于 $ f(x)=\int_{1}^{x^{2}}e^{-t^{2}}dt $不能积出来，故由分部积分公式有 $ \int_{0}^{1}xf(x)dx=\frac{x^{2}}{2}f(x)\bigg|_{0}^{1}-\int_{0}^{1}\frac{x^{2}}{2}\cdot f'(x)dx $，可见，