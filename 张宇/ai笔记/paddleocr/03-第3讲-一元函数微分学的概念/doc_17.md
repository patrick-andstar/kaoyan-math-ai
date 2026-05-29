 $$ \lim_{x\to0}\frac{\ln(1-2x)+2xf(x)}{x^{2}}=0, $$ 

证明： $ f(x) $ 在 x=0 处可导，并求  $ f'(0) $

## 解答

3.1 (D) 解

 $$ f_{+}^{\prime}(0)=\lim_{x\to0^{+}}\frac{f(x)-f(0)}{x}=\lim_{x\to0^{+}}\frac{1-\cos x}{x^{\frac{3}{2}}}=0 $$ 

 $$ f_{-}^{\prime}(0)=\lim_{x\to0^{-}}\frac{x^{2}g(x)}{x}=\lim_{x\to0^{-}}x g(x)=0 $$ 

第二个等式利用了  $ g(x) $ 是有界函数这一条件，有界函数乘以无穷小量仍是无穷小量。由于  $ f(x) $ 在点 x=0 处的左导数等于右导数，因而  $ f(x) $ 在 x=0 处可导。

3.2 (A) 解 由  $ \varphi(1)=0 $ 可知

 $$ f_{+}^{\prime}(1)=\lim_{x\to1^{+}}\frac{f(x)-f(1)}{x-1}=\lim_{x\to1^{+}}\frac{\left|x^{3}-1\right|\varphi(x)}{x-1}=\lim_{x\to1^{+}}(x^{2}+x+1)\varphi(x)=0, $$ 

 $$ f_{-}^{\prime}(1)=\lim_{x\to1^{-}}\frac{f(x)-f(1)}{x-1}=\lim_{x\to1^{-}}\frac{\left|x^{3}-1\right|\varphi(x)}{x-1}=-\lim_{x\to1^{-}}\left(x^{2}+x+1\right)\varphi(x)=0, $$ 

即 $ f_{+}^{\prime}(1)=f_{-}^{\prime}(1)=0 $，所以 $ f^{\prime}(1)=0 $

设 $ f(x) $在x=1处可导，因为 $ f(1)=0 $，所以

 $$ f_{+}^{\prime}(1)=\lim_{x\to1^{+}}\frac{f(x)-f(1)}{x-1}=\lim_{x\to1^{+}}\frac{\left|x^{3}-1\right|\varphi(x)}{x-1}=\lim_{x\to1^{+}}(x^{2}+x+1)\varphi(x)=3\varphi(1), $$ 

 $$ f_{-}^{\prime}(1)=\lim_{x\to1^{-}}\frac{f(x)-f(1)}{x-1}=\lim_{x\to1^{-}}\frac{\left|x^{3}-1\right|\varphi(x)}{x-1}=-\lim_{x\to1^{-}}\left(x^{2}+x+1\right)\varphi(x)=-3\varphi(1). $$ 

由 $ f_{+}^{\prime}(1)=f_{-}^{\prime}(1) $可得， $ 3\varphi(1)=-3\varphi(1) $，故 $ \varphi(1)=0 $，应选(A).

3.3 (B) 解 由题设可知  $ f'(x_0) = 1 $ 。而  $ \left. \mathrm{d}y \right|_{x=x_0} = f'(x_0) \Delta x = \Delta x $ ，因而  $ \lim_{\Delta x \to 0} \frac{\mathrm{d}y}{\Delta x} = 1 $ ，即当  $ \Delta x \to 0 $ 时，该函数在  $ x = x_0 $ 处  $ dy $ 与  $ \Delta x $ 是等价无穷小，故选 (B).

3.4 (A) 解 题目给出  $ f(x) $ 在  $ x_{0} $ 处可导，考查  $ \lim_{\Delta x \to 0} \frac{\Delta y - dy}{dy} $，注意，如果  $ f(x) $ 在  $ x_{0} $ 处可导，则必定可微分，因此可以由微分的性质入手.

由微分的定义可知  $ \Delta y - dy = o(\Delta x) $，而  $ dy = y'dx $， $ dy\big|_{x=x_0} = f'(x_0)\Delta x $。

由题设知 $ f'(x_{0})\neq0 $，可得