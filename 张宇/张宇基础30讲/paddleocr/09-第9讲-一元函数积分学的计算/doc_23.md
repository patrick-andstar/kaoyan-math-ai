 $ \int_{0}^{T}f(t)\mathrm{d}t=0 $，即 $ \int_{0}^{T}f(x)\mathrm{d}x=0 $时， $ F(x) $以T为周期.

(2) 记

 $$ \varphi(x)=F(x)-\frac{\int_{0}^{T}f(x)\mathrm{d}x}{T}x=\int_{a}^{x}f(t)\mathrm{d}t-\frac{\int_{0}^{T}f(x)\mathrm{d}x}{T}x, $$ 

于是

 $$ \begin{align*}\varphi(x+T)-\varphi(x)=&\int_{a}^{x+T}f(t)\mathrm{d}t-\frac{\int_{0}^{T}f(x)\mathrm{d}x}{T}(x+T)-\left[\int_{a}^{x}f(t)\mathrm{d}t-\frac{\int_{0}^{T}f(x)\mathrm{d}x}{T}x\right]\\=&\int_{x}^{x+T}f(t)\mathrm{d}t-\frac{\int_{0}^{T}f(x)\mathrm{d}x}{T}\bullet T=\int_{0}^{T}f(t)\mathrm{d}t-\int_{0}^{T}f(x)\mathrm{d}x=0,\end{align*} $$ 

故  $ \varphi(x)=F(x)-\frac{\int_{0}^{T}f(x)dx}{T}x $ 以 T 为周期.

## 五 反常积分的计算  $ \rightarrow $ 往往是在收敛的条件下

在计算反常积分时，注意识别奇点（端点、内部）。

<div style="text-align: center;"><img src="imgs/img_in_image_box_839_546_943_653.jpg" alt="Image" width="10%" /></div>


例9.26 计算反常积分  $ \int_{\frac{1}{2}}^{\frac{3}{2}}\frac{dx}{\sqrt{|x-x^{2}|}} $

分析 注意内部的点 x=1 为瑕点， $ \lim_{x\to1}\frac{1}{\sqrt{|x-x^2|}}=\infty\Rightarrow $ 反常积分拆区间去绝对值.

解 注意到被积函数含有绝对值符号且 x=1 是其无穷间断点，故

 $$ \int_{\frac{1}{2}}^{1}\frac{\mathrm{d}x}{\sqrt{x-x^{2}}}+\int_{1}^{\frac{3}{2}}\frac{\mathrm{d}x}{\sqrt{x^{2}-x}} $$ 

而

 $$ \int_{\frac{1}{2}}^{1}\frac{\mathrm{d}x}{\sqrt{x-x^{2}}}=\int_{\frac{1}{2}}^{1}\frac{\mathrm{d}x}{\sqrt{\frac{1}{4}-\left(x-\frac{1}{2}\right)^{2}}}=\arcsin\left(2x-1\right)\bigg|_{\frac{1}{2}}^{1}=\arcsin1=\frac{\pi}{2} $$ 

 $$ \begin{aligned}\int_{1}^{\frac{3}{2}}\frac{\mathrm{d}x}{\sqrt{x^{2}-x}}&=\int_{1}^{\frac{3}{2}}\frac{\mathrm{d}x}{\sqrt{\left(x-\frac{1}{2}\right)^{2}-\frac{1}{4}}}=\ln\left[\left(x-\frac{1}{2}\right)+\sqrt{\left(x-\frac{1}{2}\right)^{2}-\frac{1}{4}}\right]\Bigg|_{1}^{\frac{3}{2}}\\&=\ln(2+\sqrt{3}),\end{aligned} $$ 

因此

 $$ \int_{\frac{1}{2}}^{\frac{3}{2}}\frac{\mathrm{d}x}{\sqrt{\left|x-x^{2}\right|}}=\frac{\pi}{2}+\ln(2+\sqrt{3}). $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_122_1369_233_1400.jpg" alt="Image" width="10%" /></div>


例9.27 求  $ \int_{3}^{+\infty}\frac{dx}{(x-1)^{4}\sqrt{x^{2}-2x}} $