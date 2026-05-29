例 9.4 求不定积分  $ \int \frac{xe^{x}}{\sqrt{e^{x}-1}} dx $.

分析 ①  $ \int_{\triangle} dx \rightarrow \int_{\triangle} dx $ ② 带  $ \sqrt{} $ 且无平方项，整体代换令其为 u. 稳定不好求 易求

## 解 本题主要考查换元法、分部积分法

令  $ u = \sqrt{e^{x} - 1} $，则  $ x = \ln(1 + u^{2}) $， $ dx = \frac{2u}{1 + u^{2}}du $，从而

 $$ \begin{aligned}\int\frac{x\mathrm{e}^{x}}{\sqrt{\mathrm{e}^{x}-1}}\mathrm{d}x&=\int\frac{(1+u^{2})\ln(1+u^{2})}{u}\cdot\frac{2u}{1+u^{2}}\mathrm{d}u=2\int\ln(1+u^{2})\mathrm{d}u\\&=2u\ln(1+u^{2})-\int\frac{4u^{2}}{1+u^{2}}\mathrm{d}u=2u\ln(1+u^{2})-4u+4\arctan u+C\\&=2x\sqrt{\mathrm{e}^{x}-1}-4\sqrt{\mathrm{e}^{x}-1}+4\arctan\sqrt{\mathrm{e}^{x}-1}+C.\end{aligned} $$ 

例 9.5 求不定积分  $ \int\frac{xe^{\arctan x}}{(1+x^{2})^{\frac{3}{2}}}dx $

分析 带  $ \sqrt{} $ 且有平方项→三角代换  $ x=\tan t $ →消  $ \sqrt{} $

解 本题涉及换元法、分部积分法.

设 $ x=\tan t $，则

 $$ \int\frac{x\mathrm{e}^{\arctan x}}{\left(1+x^{2}\right)^{\frac{3}{2}}}\mathrm{d}x=\int\frac{\mathrm{e}^{t}\tan t}{\left(1+\tan^{2}t\right)^{\frac{3}{2}}}\sec^{2}t\mathrm{d}t=\int\mathrm{e}^{t}\sin t\mathrm{d}t, $$ 

又

 $$ \begin{aligned}\int\mathrm{e}^{t}\sin t\mathrm{d}t&\xlongequal{(*)}-\int\mathrm{e}^{t}\mathrm{d}(\cos t)=-\left(\mathrm{e}^{t}\cos t-\int\mathrm{e}^{t}\cos t\mathrm{d}t\right)\\&=-\mathrm{e}^{t}\cos t+\mathrm{e}^{t}\sin t-\int\mathrm{e}^{t}\sin t\mathrm{d}t,\end{aligned}\\\begin{aligned}\int\mathrm{e}^{t}\cos t-\int\mathrm{e}^{t}\cos t\mathrm{d}t\end{aligned}\\\begin{aligned}\frac{ 分部积分可能会建立欲求积 }{ 分的方程 }\end{aligned} $$ 

故原式= $ \int e^{t}\sin tdt=\frac{1}{2}e^{t}(\sin t-\cos t)+C=\frac{(x-1)e^{\arctan x}}{2\sqrt{1+x^{2}}}+C $

注 $ ^{*} $处亦可直接套用如下公式：

 $$ \textcircled{1}\int\mathrm{e}^{ax}\sin bx\mathrm{d}x=\frac{\begin{vmatrix}(\mathrm{e}^{ax})^{\prime}&(\sin bx)^{\prime}\\\mathrm{e}^{ax}&\sin bx\end{vmatrix}}{a^{2}+b^{2}}+C=\frac{a\mathrm{e}^{ax}\sin bx-b\mathrm{e}^{ax}\cos bx}{a^{2}+b^{2}}+C\;; $$ 

 $$ \textcircled{2}\int\mathrm{e}^{ax}\cos bx\mathrm{d}x=\frac{\left|\begin{matrix}(\mathrm{e}^{ax})^{\prime}&(\cos bx)^{\prime}\\ \mathrm{e}^{ax}&\cos bx\end{matrix}\right|}{a^{2}+b^{2}}+C=\frac{a\mathrm{e}^{ax}\cos bx+b\mathrm{e}^{ax}\sin bx}{a^{2}+b^{2}}+C. $$ 

再如， $ \int e^{-x}\sin nxdx=\frac{-e^{-x}\sin nx-ne^{-x}\cos nx}{(-1)^{2}+n^{2}}+C $