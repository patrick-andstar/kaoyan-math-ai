 $$ \begin{aligned}&=\lim_{\Delta x\rightarrow0}\frac{u(x+\Delta x)v(x+\Delta x)-u(x)v(x+\Delta x)+u(x)v(x+\Delta x)-u(x)v(x)}{\Delta x}\\&=\lim_{\Delta x\rightarrow0}\frac{u(x+\Delta x)-u(x)}{\Delta x}\cdot v(x+\Delta x)+\lim_{\Delta x\rightarrow0}\frac{v(x+\Delta x)-v(x)}{\Delta x}\cdot u(x)\\&=u^{\prime}(x)\cdot v(x)+u(x)\cdot v^{\prime}(x).\end{aligned} $$ 

(2)  $ \underline{\text{[u(x)v(x)w(x)]' = u'(x)v(x)w(x) + u(x)v'(x)w(x) + u(x)v(x)w'(x))}} $，如果遇到因式超过三个的式子，一般不要直接求导，而要另谋他法。公式巧记：3个人排一排，第一个人一巴掌加中间人一巴掌再加最后一人一巴掌。

商的导数（微分）

 $$ \left[\frac{u(x)}{v(x)}\right]^{\prime}=\frac{u^{\prime}(x)v(x)-u(x)v^{\prime}(x)}{\left[v(x)\right]^{2}},\ v(x)\neq0, $$ 

巩固：

 $$ (u\pm v)^{\prime}=u^{\prime}\pm v^{\prime}\ , $$ 

 $$ (uv)^{\prime}=u^{\prime}v+uv^{\prime} $$ 

 $$ \mathrm{d}\left[\frac{u(x)}{\nu(x)}\right]=\frac{\nu(x)\mathrm{d}[u(x)]-u(x)\mathrm{d}[\nu(x)]}{\left[\nu(x)\right]^{2}},\nu(x)\neq0. $$ 

 $$ \begin{aligned}\left(\frac{u}{v}\right)^{\prime}=&\left(u\bullet\frac{1}{v}\right)^{\prime}\\=&u^{\prime}\bullet\frac{1}{v}+u\bullet\left(-\frac{1}{v^{2}}\right)\bullet v^{\prime}\\=&\frac{u^{\prime}v-u v^{\prime}}{v^{2}}\end{aligned} $$ 

例 4.1 设  $ f(x)=\prod_{n=1}^{100}\left(\tan\frac{\pi x^{n}}{4}-n\right) $，则  $ f'(1)= $ ___.

☐ 分析 此题是 100 项相乘!

 $$ f(x)=\left(\tan\frac{\pi}{4}x-1\right)\left(\tan\frac{\pi}{4}x^{2}-2\right)\cdots\left(\tan\frac{\pi}{4}x^{100}-100\right). $$ 

若用乘法求导公式计算，计算量十分大。如果因式超过3项，不要直接求导，另寻他法。把它转化为两项相乘，往“经典形式”转化。

解 应填 $ -\frac{\pi\cdot99!}{2} $

本题的研究对象 $ f(x) $是多因式相乘，如果直接对其使用导数定义或者先求导再代值，都比较麻烦。本题希望考生发现，当把 $ x=1 $代入每个因式后，只有第一项 $ \tan\frac{\pi}{4}-1=0 $，而其余所有项都不等于0，抓住第一项这个“特立独行”的主要条件，记 $ g(x)=\prod_{n=2}^{100}\left(\tan\frac{\pi x^n}{4}-n\right) $，于是

 $$ f(x)=\underbrace{\left(\tan\frac{\pi x}{4}-1\right)}_{u}\cdot\underbrace{\frac{g(x)}{v}}_{} $$ 

故

 $$ f^{\prime}(x)=\sec^{2}\frac{\pi x}{4}\cdot\frac{\pi}{4}\cdot g(x)+\left(\tan\frac{\pi x}{4}-1\right)\cdot g^{\prime}(x) $$ 

 $$ f^{\prime}(1)=\frac{\pi}{4}\sec^{2}\frac{\pi x}{4}\bigg|_{x=1}\cdot g(1)=-\frac{\pi\cdot99!}{2} $$ 

⑨ 方法总结 多因式相乘的题目不要直接用乘法求导公式计算，而是巧妙地变化为“经典形式”再去算。

∅ 公式  $ \left(\tan x\right)'=\sec^{2}x $