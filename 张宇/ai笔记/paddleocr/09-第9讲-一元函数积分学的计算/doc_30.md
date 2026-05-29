 $$ \begin{aligned}&I=\int_{0}^{\pi}\frac{x\sin x}{1+\cos^{2}x}\mathrm{d}x=\int_{\pi}^{0}\frac{(\pi-t)\sin(\pi-t)}{1+\cos^{2}(\pi-t)}(-\mathrm{d}t)=\int_{0}^{\pi}\frac{(\pi-t)\sin t}{1+\cos^{2}t}\mathrm{d}t\\ &\\ &=\pi\int_{0}^{\pi}\frac{\sin t}{1+\cos^{2}t}\mathrm{d}t-\int_{0}^{\pi}\frac{t\sin t}{1+\cos^{2}t}\mathrm{d}t=\pi\int_{0}^{\pi}\frac{\sin t}{1+\cos^{2}t}\mathrm{d}t-I,\\ \end{aligned} $$ 

于是

 $$ \frac{\pi}{2}\int_{0}^{\pi}\frac{\sin t}{1+\cos^{2}t}\mathrm{d}t=-\frac{\pi}{2}\int_{0}^{\pi}\frac{1}{1+\cos^{2}t}\mathrm{d}(\cos t)=-\frac{\pi}{2}\cdot\arctan(\cos t)\bigg|_{0}^{\pi}=\frac{\pi^{2}}{4} $$ 

9.13 解 如果作变换  $ \sqrt[3]{x^2} = t $，则  $ x = \pm \sqrt{t^3} $。在  $ x $ 的区间  $ [-1, 1] $ 上的积分，应分两段  $ [-1, 0] $ 与  $ [0, 1] $ 来处理（即相应地，在前一段上取  $ x = -\sqrt{t^3} $；在后一段上取  $ x = \sqrt{t^3} $）。如果作变换  $ \sqrt[3]{x} = t $，则  $ x = t^3 $。虽然不必将区间  $ [-1, 1] $ 分两段处理，但也不是最好的办法。经仔细审题发现

 $$ \int_{-1}^{1}\frac{x+1}{1+\sqrt[3]{x^{2}}}\mathrm{d}x=\int_{-1}^{1}\frac{x}{1+\sqrt[3]{x^{2}}}\mathrm{d}x+\int_{-1}^{1}\frac{1}{1+\sqrt[3]{x^{2}}}\mathrm{d}x=0+2\int_{0}^{1}\frac{1}{1+\sqrt[3]{x^{2}}}\mathrm{d}x, $$ 

其中前一项因为被积函数是奇函数，故在对称区间上的积分应为 0；后一项因为被积函数在对称区间上是偶函数．

再作积分变量代换，令 $ \sqrt[3]{x^2}=t $，有 $ x=\sqrt{t^3} $， $ dx=\frac{3}{2}\sqrt{t}dt $。当x=0时，t=0；当x=1时，t=1。于是

 $$ 3\int_{0}^{1}\frac{\sqrt{t}}{1+t}\mathrm{d}t\xlongequal{\sqrt{t}=u}6\int_{0}^{1}\frac{u^{2}}{1+u^{2}}\mathrm{d}u=6-6\arctan1=6-\frac{3}{2}\pi $$ 

注 可见仔细审题，利用积分性质，会给解题带来方便。

9.14 解

 $$ \int_{-1}^{\frac{\pi}{4}}f(x)\mathrm{d}x=\int_{-1}^{0}f(x)\mathrm{d}x+\int_{0}^{\frac{\pi}{4}}f(x)\mathrm{d}x=\int_{-1}^{0}\frac{\mathrm{d}x}{1+\mathrm{e}^{x}}+\int_{0}^{\frac{\pi}{4}}\frac{\mathrm{d}x}{1+\sin x}, $$ 

 $$ \int_{-1}^{0}\frac{\mathrm{d}x}{1+\mathrm{e}^{x}}\xlongequal{\mathrm{e}^{x}=t}\int_{\mathrm{e}^{-1}}^{1}\frac{1}{1+t}\cdot\frac{1}{t}\mathrm{d}t=\int_{\mathrm{e}^{-1}}^{1}\left(\frac{1}{t}-\frac{1}{1+t}\right)\mathrm{d}t=\ln\frac{t}{1+t}\bigg|_{\mathrm{e}^{-1}}^{1}=-\ln2+\ln(1+\mathrm{e}), $$ 

 $$ \begin{aligned}\int_{0}^{\frac{\pi}{4}}\frac{\mathrm{d}x}{1+\sin x}&=\int_{0}^{\frac{\pi}{4}}\frac{1-\sin x}{\cos^{2}x}\mathrm{d}x=\int_{0}^{\frac{\pi}{4}}\sec^{2}x\mathrm{d}x-\int_{0}^{\frac{\pi}{4}}\frac{\sin x}{\cos^{2}x}\mathrm{d}x\\&=\tan x\bigg|_{0}^{\frac{\pi}{4}}-\frac{1}{\cos x}\bigg|_{0}^{\frac{\pi}{4}}=1-(\sqrt{2}-1)=2-\sqrt{2},\end{aligned} $$ 

从而

 $$ \int_{-1}^{\frac{\pi}{4}}f(x)\mathrm{d}x=-\ln2+\ln(1+\mathrm{e})+2-\sqrt{2} $$ 

9.15 解 当  $ -1 \leq x < 0 $ 时，

 $$ \begin{aligned} 原式 =\int_{-1}^{x}(1+t)dt=\frac{1}{2}(1+t)^{2}\bigg|_{-1}^{x}=\frac{1}{2}(1+x)^{2}\end{aligned}； $$ 

当 $ x\geq0 $时，

 $$ \int_{0}^{0}(1+t)dt+\int_{0}^{x}(1-t)dt=1-\frac{1}{2}(1-x)^{2} $$ 