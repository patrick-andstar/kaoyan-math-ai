定理 6(罗尔定理)

①在 $ [a,b] $上连续，

三个条件同时满足才可以

设 $ f(x) $满足

②在 $ (a,b) $内可导，则存在 $ \xi\in(a,b) $，使得 $ f'(\xi)=0 $。

③ $ f(a)=f(b) $,

<div style="text-align: center;"><img src="imgs/img_in_image_box_800_124_898_277.jpg" alt="Image" width="9%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_304_310_465_378.jpg" alt="Image" width="15%" /></div>


 $ f(a) = f(b) $;

②  $ \lim_{x\to a^{+}}f(x)=\lim_{x\to b^{-}}f(x) $

(1652—1719)

 $$ \textcircled{3}\lim_{x\to a^{+}}f(x)=+\infty,\ \lim_{x\to b^{-}}f(x)=+\infty. $$ 

 $$ >f^{\prime}(\xi)=0 $$ 

注 $ ^{1} $ 推广的罗尔定理.

设 $ f(x) $在 $ (a,b) $内可导， $ \lim_{x\to a^{-}}f(x)=\lim_{x\to b^{-}}f(x)=A $，则在 $ (a,b) $内至少存在一点 $ \xi $，使 $ f'(\xi)=0 $，其中区间 $ (a,b) $可以是有限区间也可以是无穷区间，A可以是有限数也可以是无穷大。

注2 罗尔定理的使用往往需要构造辅助函数，其方法总结如下.

(1) 简单情形：题设  $ f(x) $ 即为辅助函数（研究对象）.

(2) 复杂情形.  $ \rightarrow $ 一般不用f，而用一个神秘的“F”——辅助函数.

①乘积求导公式 $ (uv)' = u'v + uv' $的逆用.

 $$ \left[f(x)f(x)\right]^{\prime}=\left[f^{2}(x)\right]^{\prime}=2f(x)\cdot f^{\prime}(x) $$ 

见到 $ f(x)f'(x) $，令 $ F(x)=f^{2}(x) $。逆运算

b.  $ [f(x) \cdot f'(x)]' = [f'(x)]^2 + f(x)f''(x) $

见到  $ [f'(x)]^2 + f(x)f''(x) $，令  $ F(x) = f(x)f'(x) $

 $$ \left[f(x)\mathrm{e}^{\varphi(x)}\right]^{\prime}=f^{\prime}(x)\mathrm{e}^{\varphi(x)}+f(x)\mathrm{e}^{\varphi(x)}\cdot\varphi^{\prime}(x)=\left[f^{\prime}(x)+f(x)\varphi^{\prime}(x)\right]\mathrm{e}^{\varphi(x)} $$ 

见到 $ f'(x)+f(x)\varphi'(x) $，令 $ F(x)=f(x)\mathrm{e}^{\varphi(x)} $

常考以下情形.

 $ \varphi(x)=x\Rightarrow $ 见到  $ f'(x)+f(x) $，令  $ F(x)=f(x)\mathrm{e}^x $

 $ \varphi(x) = -x \Rightarrow $ 见到  $ f'(x) - f(x) $，令  $ F(x) = f(x)e^{-x} $

 $ \varphi(x)=kx \Rightarrow $ 见到  $ f'(x)+kf(x) $，令  $ F(x)=f(x)e^{kx} $

 $ (uv)'' = u''v + 2u'v' + uv'' $ 亦有可能考到.

②商的求导公式 $ \left(\frac{u}{v}\right)^{\prime}=\frac{u^{\prime}v-uv^{\prime}}{v^{2}} $的逆用.

 $$ \left[\frac{f(x)}{x}\right]^{\prime}=\frac{f^{\prime}(x)x-f(x)}{x^{2}} $$ 