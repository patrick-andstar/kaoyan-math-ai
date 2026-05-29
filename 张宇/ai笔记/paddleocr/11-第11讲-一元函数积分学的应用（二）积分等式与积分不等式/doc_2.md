注 (1) 由于  $ \xi \in (a, b) \subset [a, b] $，故闭区间上结论亦成立，即设  $ f(x) $， $ g(x) $ 在  $ [a, b] $ 上连续且  $ g(x) $ 不变号，则至少存在一点  $ \xi \in [a, b] $，使得  $ \int_{a}^{b} f(x) g(x) dx = f(\xi) \int_{a}^{b} g(x) dx $.

(2) 对于  $ \int_{1}^{2} f(x) e^{-x^2} \, dx $，虽然上下限为常数，但被积函数  $ f(x) e^{-x^2} $ 与  $ n $ 有关，故中值  $ \xi_n $ 与  $ n $ 有关。同理，对于  $ \int_{1}^{2} e^{-x^2} \, dx $，若写成  $ \int_{1}^{2} e^{-x^2} \, dx = e^{-\eta_n^n} $， $ \eta_n \in (1, 2) $， $ \eta_n $ 亦与  $ n $ 有关，考生需注意，此时不能用  $ \lim_{n \to \infty} e^{-\eta_n^n} = 0 $。

拓展：对于 $ \int_{a}^{b}f(x)\mathrm{d}x=f(\xi)(b-a) $，当改变区间 $ [a,b]\to[a,x] $时， $ \xi=\xi(x) $

当改变微积函数 $ f(x) \to f(x, n) $或 $ f_{n}(x) $（函数组）时， $ \xi = \xi(n) $.

★ ★ ☐ 例 11.2 设  $ f(x) $ 在  $ \left[0, \frac{\pi}{2}\right] $ 上有二阶导数，且  $ f(0) = 2 $， $ f\left(\frac{\pi}{2}\right) = 1 $， $ \int_{0}^{\frac{\pi}{2}} f(x) e^{\sin x} \cos x \, dx = 2(e-1) $。证明：存在  $ \xi \in \left(0, \frac{\pi}{2}\right) $，使  $ f''(\xi) < 0 $。

证 由推广的积分中值定理知，存在  $ \eta \in \left(0, \frac{\pi}{2}\right) $，使得  $ f(\eta) \int_{0}^{\frac{\pi}{2}} e^{\sin x} \cos x \, dx = 2(e-1) $.

又  $ \int_{0}^{\frac{\pi}{2}} e^{\sin x} \cos x dx = e^{\sin x} \bigg|_{0}^{\frac{\pi}{2}} = e - 1 $，于是  $ f(\eta) \cdot (e - 1) = 2 (e - 1) $，即存在  $ \eta \in \left(0, \frac{\pi}{2}\right) $，使得  $ f(\eta) = 2 $。

因 $ f(0)=f(\eta)=2 $．由罗尔定理知，存在 $ \xi_{1}\in(0,\eta) $，使得 $ f'(\xi_{1})=0 $．又因为 $ f\left(\frac{\pi}{2}\right)=1 $， $ f(\eta)\neq f\left(\frac{\pi}{2}\right) $，

由拉格朗日中值定理知，存在  $ \xi_{2} \in \left( \eta, \frac{\pi}{2} \right) $，使得  $ \frac{\pi}{2} = \frac{\pi}{2} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_510_889_670_973.jpg" alt="Image" width="15%" /></div>


拓展：若 $ f(a)=f(b)=f(c) $，用三次罗尔定理

 $$ f^{\prime}(\xi_{2})=\frac{f\left(\frac{\pi}{2}\right)-f(\eta)}{\frac{\pi}{2}-\eta}=\frac{1-2}{\frac{\pi}{2}-\eta}<0, $$ 

 $$ f^{\prime}(\xi_{1})=f^{\prime}(\xi_{2})=0\ . $$ 

若 $ f(a)\neq f(b)\neq f(c) $，用三次拉格朗日中值定理，

由 $ f'(\xi_{1})<0,\ f'(\xi_{2})>0 $．由 $ f'(\xi_{1})>0,\ f'(\xi_{2})<0 $．得 $ f''(\xi)>0 $得 $ f''(\xi)<0 $（习题11.1）

再由拉格朗日中值定理知，存在  $ \xi\in(\xi_{1},\xi_{2})\subset\left(0,\frac{\pi}{2}\right) $，使得  $ f^{\prime\prime}(\xi)=\frac{f^{\prime}(\xi_{2})-f^{\prime}(\xi_{1})}{\xi_{2}-\xi_{1}}<0 $

<div style="text-align: center;"><img src="imgs/img_in_image_box_442_1295_587_1369.jpg" alt="Image" width="14%" /></div>
