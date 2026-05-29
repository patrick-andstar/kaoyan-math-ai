由于  $ \ln\frac{1-t}{1+t}=\ln(1-t)-\ln(1+t) $ 为奇函数，故原式 =0.

例9.13 求  $ \int_{-1}^{1} x^{2} \sqrt{1-x^{2}} \, dx $.

分析  $ \sqrt{ } $ 中含平方项  $ \rightarrow $ 三角函数代换.

解 因被积函数为偶函数，故

 $$ \int_{-1}^{1}x^{2}\sqrt{1-x^{2}}\mathrm{d}x=2\int_{0}^{1}x^{2}\sqrt{1-x^{2}}\mathrm{d}x $$ 

再作三角变换，令  $ x = \sin t $，当  $ x = 0 $ 时，可取  $ t = 0 $；当  $ x = 1 $ 时，可取  $ t = \frac{\pi}{2} $，且当  $ t \in \left[0, \frac{\pi}{2}\right] $ 时， $ x = \sin t $ 不超出原上、下限的区间  $ [0, 1] $，在  $ \left[0, \frac{\pi}{2}\right] $ 上， $ x' = x'(t) = \cos t $ 连续。于是

 $$ \begin{aligned} 原式 &=2\int_{0}^{1}x^{2}\sqrt{1-x^{2}}\mathrm{d}x=2\int_{0}^{\frac{\pi}{2}}\sin^{2}t\cos^{2}t\mathrm{d}t\\&=2\left(\int_{0}^{\frac{\pi}{2}}\sin^{2}t\mathrm{d}t-\int_{0}^{\frac{\pi}{2}}\sin^{4}t\mathrm{d}t\right)\\&=2\left(\frac{1}{2}\times\frac{\pi}{2}-\frac{3}{4}\times\frac{1}{2}\times\frac{\pi}{2}\right)=\frac{\pi}{8}\ .\\ \end{aligned} $$ 

注 从原则上讲，作变换  $ x = \sin t $ 后，当  $ x = 0 $ 时，可取  $ t = 0, \pm \pi, \pm 2\pi, \cdots $；当  $ x = 1 $ 时，可取  $ t = \frac{\pi}{2}, \frac{\pi}{2} \pm 2\pi, \cdots $，上、下限有多种组合可满足定理条件。但被积函数中  $ \sqrt{1 - x^2} = \sqrt{1 - \sin^2 t} = |\cos t| $，在不同组合中，此绝对值的处理有简有繁，应引起注意，不要自找麻烦。

例9.14  $ \int_{0}^{1} \arcsin \sqrt{1 - x^{2}} \, dx = \_\_\_\_\_\_ . $

分析 ①  $ \int \arcsin \sqrt{1 - x^2} \, dx \to \int u \, dv $ （难算）=  $ uv - \int v \, du $ （易算）.

② $ \sqrt{ } $中含平方项→三角函数代换.

解 应填 1.

方法一 分部积分法.

 $$ \begin{aligned}&\int_{0}^{1}\arcsin\sqrt{1-x^{2}}\mathrm{d}x=x\arcsin\sqrt{1-x^{2}}\bigg|_{0}^{1}-\int_{0}^{1}x\mathrm{d}(\arcsin\sqrt{1-x^{2}})\\ &=-\int_{0}^{1}x\mathrm{d}(\arcsin\sqrt{1-x^{2}})=\int_{0}^{1}x\frac{1}{\sqrt{1-x^{2}}}\mathrm{d}x=-\frac{1}{2}\int_{0}^{1}\frac{\mathrm{d}(1-x^{2})}{\sqrt{1-x^{2}}}\\ &=-\sqrt{1-x^{2}}\bigg|_{0}^{1}=1\ .\\ \end{aligned} $$ 

方法二 换元法.