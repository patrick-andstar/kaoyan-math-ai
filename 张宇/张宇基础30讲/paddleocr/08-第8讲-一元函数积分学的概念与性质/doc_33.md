于是，先对 $ \sum_{i=1}^{n}\frac{\sin\frac{i\pi}{n}}{n+\frac{1}{i}} $进行放缩，有

 $$ \sum_{i=1}^{n}\frac{\sin\frac{i\pi}{n}}{n+1}\leqslant\sum_{i=1}^{n}\frac{\sin\frac{i\pi}{n}}{n+\frac{1}{i}}\leqslant\sum_{i=1}^{n}\frac{\sin\frac{i\pi}{n}}{n}, $$ 

由于

 $$ \lim_{n\to\infty}\sum_{i=1}^{n}\frac{\sin\frac{i\pi}{n}}{n}=\lim_{n\to\infty}\frac{1}{n}\sum_{i=1}^{n}\sin\frac{i}{n}\pi=\int_{0}^{1}\sin\pi x dx=\frac{2}{\pi}, $$ 

 $$ \lim_{n\to\infty}\sum_{i=1}^{n}\frac{\sin\frac{i\pi}{n}}{n+1}=\lim_{n\to\infty}\frac{n}{n+1}\cdot\frac{1}{n}\sum_{i=1}^{n}\sin\frac{i}{n}\pi=1\cdot\int_{0}^{1}\sin\pi x dx=\frac{2}{\pi}, $$ 

因此，由夹逼准则得

 $$ \lim_{n\to\infty}\sum_{i=1}^{n}\frac{\sin\frac{i\pi}{n}}{n+\frac{1}{i}}=\frac{2}{\pi}\quad. $$ 

8.61 解 设  $ f(x)=x-[x] $，其图形如图 8-7 所示.

<div style="text-align: center;"><img src="imgs/img_in_image_box_404_780_640_905.jpg" alt="Image" width="22%" /></div>


<div style="text-align: center;">图 8-7</div>


方法一 因为 x=1 是  $ y=f(x) $ 的跳跃间断点，所以

 $$ F_{-}^{\prime}(1)=\lim_{x\to1^{-}}f(x)=1,\;F_{+}^{\prime}(1)=\lim_{x\to1^{+}}f(x)=0, $$ 

故 $ F_{-}^{\prime}(1)+F_{+}^{\prime}(1)=1 $

方法二

 $$ F_{-}^{\prime}(1)=\lim_{x\to1^{-}}\frac{F(x)-F(1)}{x-1}=\lim_{x\to1^{-}}\frac{\int_{0}^{x}t\mathrm{d}t-\frac{1}{2}}{x-1}=\lim_{x\to1^{-}}\frac{x}{1}=1, $$ 

 $$ \begin{aligned}F_{+}^{\prime}(1)&=\lim_{x\to1^{+}}\frac{F(x)-F(1)}{x-1}=\lim_{x\to1^{+}}\frac{\int_{0}^{1}t\mathrm{d}t+\int_{1}^{x}(t-1)\mathrm{d}t-\frac{1}{2}}{x-1}\\&=\lim_{x\to1^{+}}\frac{\int_{1}^{x}(t-1)\mathrm{d}t}{x-1}=\lim_{x\to1^{+}}\frac{x-1}{1}=0,\end{aligned} $$ 

故 $ F_{-}^{\prime}(1)+F_{+}^{\prime}(1)=1 $

8.7 分析 本题考查反常积分敛散性的判别法（通过计算结果来判别是否收敛），是历届考生复习