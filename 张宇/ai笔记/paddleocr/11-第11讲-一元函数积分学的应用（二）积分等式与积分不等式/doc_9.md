 $$ \int_{2}^{3}\varphi(x)\mathrm{d}x=\varphi(\eta)(3-2)=\varphi(\eta). $$ 

对  $ \varphi(x) $ 在  $ [1, 2] $ 和  $ [2, \eta] $ 上分别应用拉格朗日中值定理，并注意到  $ \varphi(1) < \varphi(2) $， $ \varphi(\eta) < \varphi(2) $，得

 $$ \varphi^{\prime}(\xi_{1})=\frac{\varphi(2)-\varphi(1)}{2-1}>0,1<\xi_{1}<2, $$ 

 $$ \varphi^{\prime}(\xi_{2})=\frac{\varphi(\eta)-\varphi(2)}{\eta-2}<0,\;2<\xi_{2}<\eta\leq3\;. $$ 

在  $ [\xi_{1}, \xi_{2}] $ 上对导函数  $ \varphi'(x) $ 应用拉格朗日中值定理，有

 $$ \varphi^{\prime \prime}(\xi)=\frac{\varphi^{\prime}(\xi_{2})-\varphi^{\prime}(\xi_{1})}{\xi_{2}-\xi_{1}}<0,\xi\in(\xi_{1},\xi_{2})\subset(1,3). $$ 

11.2 证明 要证原不等式成立，只需证  $ \int_{0}^{\frac{\pi}{2}}\frac{\cos x-\sin x}{1+x^{2}}dx\geqslant0 $

方法一  $ \int_{0}^{\frac{\pi}{2}}\frac{\cos x-\sin x}{1+x^{2}}dx=\int_{0}^{\frac{\pi}{4}}\frac{\cos x-\sin x}{1+x^{2}}dx+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\frac{\cos x-\sin x}{1+x^{2}}dx $

在上式右边第二项积分中，令 $ x=\frac{\pi}{2}-t $，得

 $$ \begin{aligned}\int_{0}^{\frac{\pi}{2}}\frac{\cos x-\sin x}{1+x^{2}}\mathrm{d}x=&\int_{0}^{\frac{\pi}{4}}\frac{\cos x-\sin x}{1+x^{2}}\mathrm{d}x+\int_{0}^{\frac{\pi}{4}}\frac{\sin t-\cos t}{1+\left(\frac{\pi}{2}-t\right)^{2}}\mathrm{d}t\\=&\int_{0}^{\frac{\pi}{4}}\left(\cos x-\sin x\right)\left[\frac{1}{1+x^{2}}-\frac{1}{1+\left(\frac{\pi}{2}-x\right)^{2}}\right]\mathrm{d}x\geq0,\end{aligned} $$ 

故原式得证.

方法二

 $$ \begin{aligned}&\int_{0}^{\frac{\pi}{2}}\frac{\cos x-\sin x}{1+x^{2}}\mathrm{d}x\\=&\int_{0}^{\frac{\pi}{4}}\frac{\cos x-\sin x}{1+x^{2}}\mathrm{d}x+\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}\frac{\cos x-\sin x}{1+x^{2}}\mathrm{d}x\\=&\frac{1}{1+\xi^{2}}\int_{0}^{\frac{\pi}{4}}(\cos x-\sin x)\mathrm{d}x+\frac{1}{1+\eta^{2}}\int_{\frac{\pi}{4}}^{\frac{\pi}{2}}(\cos x-\sin x)\mathrm{d}x\\=&(\sqrt{2}-1)\left(\frac{1}{1+\xi^{2}}-\frac{1}{1+\eta^{2}}\right),\end{aligned} $$ 

其中  $ 0 \leqslant \xi \leqslant \frac{\pi}{4} $， $ \frac{\pi}{4} \leqslant \eta \leqslant \frac{\pi}{2} $，从而有

 $$ \int_{0}^{\frac{\pi}{2}}\frac{\cos x-\sin x}{1+x^{2}}\mathrm{d}x\geqslant0, $$ 