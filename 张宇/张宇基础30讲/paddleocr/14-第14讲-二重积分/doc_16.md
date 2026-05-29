☑ 方法总结 积分与字母用谁无关！

 $$ \iint\limits_{D_{x}}f(x,y)\mathrm{d}x\mathrm{d}y=\iint\limits_{D_{y}}f(y,x)\mathrm{d}y\mathrm{d}x,\quad\int_{a}^{b}f(x)\mathrm{d}x=\int_{a}^{b}f(t)\mathrm{d}t. $$ 

公式  $ \int e^{-x}dx=-e^{-x}+C $

### 例14.12 计算 $ \int_{-\infty}^{+\infty}x^{2}e^{-x^{2}}dx $

♡分析 被积函数为偶函数，因为  $ \int_{-\infty}^{+\infty} x^2 e^{-x^2} dx $ 收敛，所以可以用对称性处理，然后借助  $ \Gamma $ 函数计算结果。

解  $ \int_{-\infty}^{+\infty}x^{2}e^{-x^{2}}dx=2\int_{0}^{+\infty}x^{2}e^{-x^{2}}dx $，又由例9.28知， $ 2\int_{0}^{+\infty}x^{2}e^{-x^{2}}dx=2\int_{0}^{+\infty}x^{2}\cdot\frac{3}{2}e^{-x^{2}}dx=\Gamma\left(\frac{3}{2}\right)=\frac{1}{2}\cdot\Gamma\left(\frac{1}{2}\right)=\frac{\sqrt{\pi}}{2} $。故 $ \int_{-\infty}^{+\infty}x^{2}e^{-x^{2}}dx=\frac{\sqrt{\pi}}{2} $。

注 本题若不用Γ函数，对于 $ \int_{0}^{+\infty}x^{2}e^{-x^{2}}dx $，要这样算：

 $$ \begin{aligned}\int_{0}^{+\infty}x^{2}\mathrm{e}^{-x^{2}}\mathrm{d}x=&\int_{0}^{+\infty}\left(-\frac{1}{2}\right)x\mathrm{e}^{-x^{2}}\mathrm{d}(-x^{2})=\int_{0}^{+\infty}\left(-\frac{1}{2}\right)x\mathrm{d}(\mathrm{e}^{-x^{2}})\\=&-\frac{1}{2}x\mathrm{e}^{-x^{2}}\bigg|_{0}^{+\infty}-\int_{0}^{+\infty}\left(-\frac{1}{2}\right)\mathrm{e}^{-x^{2}}\mathrm{d}x\\=&0+\frac{1}{2}\int_{0}^{+\infty}\mathrm{e}^{-x^{2}}\mathrm{d}x=\frac{\sqrt{\pi}}{4},\end{aligned} $$ 

故 $ \int_{-\infty}^{+\infty}x^{2}e^{-x^{2}}dx=\frac{\sqrt{\pi}}{2} $，显然，这是相对麻烦的。

方法总结 Γ函数的相关结论要牢记： $ \Gamma(\alpha)=\int_{0}^{+\infty}x^{\alpha-1}e^{-x}dx $， $ \Gamma(\alpha+1)=a\Gamma(\alpha) $。

例14.13 已知  $ \lim_{x\to+\infty}\frac{\int_{0}^{x}t^{2}e^{x^{2}-t^{2}}dt+ae^{x^{2}}}{x^{b}}=-\frac{1}{2} $，求 a, b 的值.

♡分析）一开始，可能看不出是什么类型的未定式，作恒等变形(分子分母同时除以 $ e^{x^2} $)再看.

解

 $$ \lim_{x\to+\infty}\frac{\int_{0}^{x}t^{2}e^{-t^{2}}dt+a}{x^{b}e^{-x^{2}}}=-\frac{1}{2} $$ 

此时不论 b 取何值， $ \lim_{x\to+\infty}x^{b}e^{-x^{2}}=0 $，即判定为“ $ \frac{0}{0} $”型（事实上，变形前为“ $ \frac{\infty}{\infty} $”型）.

故

 $$ \lim_{x\to+\infty}\left(\int_{0}^{x}t^{2}\mathrm{e}^{-t^{2}}\mathrm{d}t+a\right)=0, $$ 

于是

 $$ a=-\int_{0}^{+\infty}t^{2}\mathrm{e}^{-t^{2}}\mathrm{d}t=-\frac{\sqrt{\pi}}{4}\xrightarrow{} $$ 