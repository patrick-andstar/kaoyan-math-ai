 $ f(x)=f(1)+f'(1)(x-1)+\frac{f''(\xi)}{2}(x-1)^2 $（ $ \xi $是介于x，1之间的关于x的函数），

 $$ \int_{0}^{2}f(x)\mathrm{d}x=f^{\prime}(1)\int_{0}^{2}(x-1)\mathrm{d}x+\int_{0}^{2}\frac{f^{\prime \prime}(\xi)}{2}(x-1)^{2}\mathrm{d}x=\frac{1}{2}\int_{0}^{2}f^{\prime \prime}(\xi)(x-1)^{2}\mathrm{d}x $$ 

利用第8讲“二、3”的性质4

 $$ \int_{0}^{2x_{0}}(x-x_{0})\mathrm{d}x=0 $$ 

 $$ \left|\int_{0}^{2}f(x)\mathrm{d}x\right|\leqslant\frac{1}{2}\int_{0}^{2}\left|f^{\prime\prime}(\xi)\right|(x-1)^{2}\mathrm{d}x\leqslant\frac{1}{2}M\int_{0}^{2}(x-1)^{2}\mathrm{d}x=\frac{1}{3}M $$ 

故得证.

## 4 用积分法

→即 $ f'(x) $连续

例 11.10 设  $ f(x) $ 在  $ [0, 2\pi] $ 上具有一阶连续导数，且  $ f'(x) \geq 0 $，证明：对任意正整数  $ n $ 有

 $$ \left|\int_{0}^{2\pi}f(x)\sin n x\mathrm{d}x\right|\leqslant\frac{2}{n}[f(2\pi)-f(0)]\ . $$ 

☐分析 被积函数是两项相乘的形式，故用分部积分法去做.

 $$ \begin{aligned} 证 \quad\left|\int_{0}^{2\pi}f(x)\sin n x\mathrm{d}x\right|&=\left|\frac{1}{n}\int_{0}^{2\pi}f(x)\mathrm{d}(\cos nx)\right|=\left|\frac{1}{n}f(x)\cos nx\right|_{0}^{2\pi}-\frac{1}{n}\int_{0}^{2\pi}f^{\prime}(x)\cos n x\mathrm{d}x\\&\leqslant\left|\frac{1}{n}f(x)\cos nx\right|_{0}^{2\pi}+\left|\frac{1}{n}\int_{0}^{2\pi}f^{\prime}(x)\cos n x\mathrm{d}x\right|\\&\leqslant\frac{1}{n}[f(2\pi)-f(0)]+\frac{1}{n}\int_{0}^{2\pi}\left|f^{\prime}(x)\cos nx\right|\mathrm{d}x\\ 由于 f^{\prime}(x)\geqslant0, 故 f(2\pi)\geqslant f(0)\\f(2\pi)-f(0)\geqslant0&\xleftarrow{}\\\leqslant&\frac{1}{n}[f(2\pi)-f(0)]+\frac{1}{n}\int_{0}^{2\pi}f^{\prime}(x)\mathrm{d}x\\&=\frac{2}{n}[f(2\pi)-f(0)]．\end{aligned} 可得 .\\  \begin{aligned}&\leqslant\left|uv\right|_{u}^{b}+\left|\int_{a}^{b}v\mathrm{d}u\right|\\&\leqslant\left|uv\right|_{u}^{b}+\left|\int_{a}^{b}v\mathrm{d}u\right|\\&\quad 可得 .\end{aligned} $$ 

## 5 用牛顿－莱布尼茨公式

例 11.11 设  $ f'(x) $ 在  $ [a, b] $ 上连续，且  $ f(a) = f(b) = 0 $ 。证明：

 $$ \left|f(x)\right|\leqslant\frac{1}{2}\int_{a}^{b}\left|f^{\prime}(x)\right|\mathrm{d}x\quad. $$ 

♡分析 证明 $ f(x) $与 $ \int_{a}^{b}f'(x)dx $的关系用牛顿-莱布尼茨公式.

<div style="text-align: center;"><img src="imgs/img_in_image_box_128_1220_163_1254.jpg" alt="Image" width="3%" /></div>


证 由  $ f(x)=f(x)-f(a)=\int_{a}^{x}f'(t)dt $，得

 $$ 3^{-} $$ 

 $$ \left|f(x)\right|=\left|\int_{a}^{x}f^{\prime}(t)dt\right|\leqslant\int_{a}^{x}\left|f^{\prime}(t)\right|dt $$ 

由 $ f(x)=f(x)-f(b)=\int_{b}^{x}f'(t)dt $，得