9.10 解

 $$ \begin{aligned}\int\frac{1}{1+\cos^{2}x}\mathrm{d}x=&\int\frac{\sec^{2}x}{2+\tan^{2}x}\mathrm{d}x=\int\frac{\sqrt{2}\mathrm{d}\left(\frac{\tan x}{\sqrt{2}}\right)}{2\left[1+\left(\frac{\tan x}{\sqrt{2}}\right)^{2}\right]}\\=&\frac{1}{\sqrt{2}}\arctan\frac{\tan x}{\sqrt{2}}+\dot{C},\end{aligned} $$ 

取 C=0 即得  $ \frac{1}{1+\cos^{2}x} $ 的一个原函数

 $$ F(x)=\frac{1}{\sqrt{2}}\arctan\frac{\tan x}{\sqrt{2}}, $$ 

于是 $ \int_{0}^{\frac{3}{4}\pi}\frac{1}{1+\cos^{2}x}dx=\frac{1}{\sqrt{2}}\arctan\frac{\tan x}{\sqrt{2}}\bigg|_{0}^{\frac{3}{4}\pi}=\frac{1}{\sqrt{2}}\arctan\frac{-1}{\sqrt{2}} $，根据积分的保号性，这显然是错误的结果，错误的根源在于误用牛顿－莱布尼茨公式，这里 $ F(x)=\frac{1}{\sqrt{2}}\arctan\frac{\tan x}{\sqrt{2}} $并不是 $ \frac{1}{1+\cos^{2}x} $在 $ \left[0,\frac{3}{4}\pi\right] $上的原函数 $ (F(x) $在 $ x=\frac{\pi}{2} $处无意义)，应该分区间使用牛顿－莱布尼茨公式.于是

 $$ \begin{aligned}\int_{0}^{\frac{3}{4}}\frac{1}{1+\cos^{2}x}\mathrm{d}x&=\int_{0}^{\frac{1}{2}\pi}\frac{1}{1+\cos^{2}x}\mathrm{d}x+\int_{\frac{3}{2}\pi}^{\frac{3}{4}\pi}\frac{1}{1+\cos^{2}x}\mathrm{d}x\\&=\lim_{x\to\left(\frac{\pi}{2}\right)^{-}}F(x)-F(0)+F\left(\frac{3}{4}\pi\right)-\lim_{x\to\left(\frac{\pi}{2}\right)^{+}}F(x)\\&=\frac{1}{\sqrt{2}}\cdot\frac{\pi}{2}-0+\frac{1}{\sqrt{2}}\arctan\frac{-1}{\sqrt{2}}-\frac{1}{\sqrt{2}}\cdot\left(-\frac{\pi}{2}\right)\\&=-\frac{\pi}{\sqrt{2}}-\frac{1}{\sqrt{2}}\arctan\frac{1}{\sqrt{2}}.\end{aligned} $$ 

9.11 解

 $$ \begin{aligned}\int_{\frac{\pi}{4}}^{\frac{\pi}{4}}\mathrm{e}^{\frac{x}{2}}\frac{\cos x-\sin x}{\sqrt{\cos x}}\mathrm{d}x&=\int_{\frac{\pi}{4}}^{\frac{\pi}{4}}\mathrm{e}^{\frac{x}{2}\sqrt{\cos x}}\mathrm{d}x-\int_{\frac{\pi}{4}}^{\frac{\pi}{4}}\mathrm{e}^{\frac{x}{2}}\frac{\sin x}{\sqrt{\cos x}}\mathrm{d}x\\&=\int_{\frac{\pi}{4}}^{\frac{\pi}{4}}\mathrm{e}^{\frac{x}{2}\sqrt{\cos x}}\mathrm{d}x+2\int_{\frac{\pi}{4}}^{\frac{\pi}{4}}\mathrm{e}^{\frac{x}{2}}\mathrm{d}(\sqrt{\cos x})\\&=\left.\int_{\frac{\pi}{4}}^{\frac{\pi}{4}}\mathrm{e}^{\frac{x}{2}\sqrt{\cos x}}\mathrm{d}x+2\mathrm{e}^{\frac{x}{2}\sqrt{\cos x}}\right|_{\frac{\pi}{4}}^{\frac{\pi}{4}}-\int_{\frac{\pi}{4}}^{\frac{\pi}{4}}\mathrm{e}^{\frac{x}{2}\sqrt{\cos x}}\mathrm{d}x\\&=\sqrt[4]{8}(\mathrm{e}^{\frac{\pi}{8}}-\mathrm{e}^{\frac{\pi}{8}}).\end{aligned} $$ 

积分过程中， $ \int_{-\frac{\pi}{4}}^{\frac{\pi}{4}}e^{\frac{x}{2}}\sqrt{\cos x}dx $ 被相互抵消，这是分部积分法的一种特殊类型，与循环积分类似。

9.12 解 令  $ x = \pi - t $，则