 $$ \left[u(x)^{\nu(x)}\right]^{\prime}=\left[\mathrm{e}^{\nu(x)\ln u(x)}\right]^{\prime}=u(x)^{\nu(x)}\left[\nu^{\prime}(x)\ln u(x)+\nu(x)\bullet\frac{u^{\prime}(x)}{u(x)}\right].\  公式不要记 , 直接求导 . $$ 

例 4.12 求函数  $ y = x^x $ ( $ x > 0 $) 的导数.

分析  $ x^{x} $ 是典型的幂指函数，将  $ x^{x} $ 化为  $ e^{x\ln x} $，再去求导。

解

 $$ \begin{aligned}y^{\prime}&=(x^{x})^{\prime}=(\mathrm{e}^{x\ln x})^{\prime}\\&=\mathrm{e}^{x\ln x}(x\ln x)^{\prime}\\&=x^{x}(1+\ln x)(x>0)\end{aligned} $$ 

方法总结 遇到幂指函数，先化成指数函数，转化为简单的复合函数再去求导。

∅公式  $ (x\ln x)'=\ln x+1 $

例4.13 求函数  $ y = x^{\frac{1}{x}} $ (x > 0) 的导数.

分析  $ x^{\frac{1}{x}} $ 是幂指函数，将  $ x^{\frac{1}{x}} $ 化为  $ e^{\frac{1}{x}\ln x} $，再去求导。

解

 $$ \begin{aligned}&y^{\prime}=\left(x^{\frac{1}{x}}\right)^{\prime}=\left(e^{\frac{1}{x}\ln x}\right)^{\prime}\\ &\begin{aligned}\\ &=e^{\frac{1}{x}\ln x}\left(-\frac{1}{x^{2}}\bullet\ln x+\frac{1}{x}\bullet\frac{1}{x}\right)\\&=x^{\frac{1}{x}-2}(1-\ln x)(x>0).\\ &\end{aligned}\\ \end{aligned} $$ 

☑ 方法总结 遇到幂指函数，先化成指数函数，转化为简单的复合函数再去求导.

公式  $ \left(\frac{1}{x}\ln x\right)^{\prime}=-\frac{1}{x^{2}}\ln x+\frac{1}{x^{2}} $

★★★10 高阶导数 是考研数学中一个区分度较高的题型

求高阶导数主要有 $ \underline{\text{三种方法}} $.→不同问题选择不同的方法，题型具有灵活性！

(1) 归纳法.

逐次求导，探索规律，得出通式.

例4.14 求  $ y = \sin x $ 的  $ n $ 阶导数.

☑ 分析 当不知道高阶求导公式时，只能逐阶求导，本题还需要借助于三角函数的诱导公式，写成同名下的三角函数形式，再去探索规律.

解

 $$ y^{\prime}=(\sin x)^{\prime}=\cos x, $$ 

 $$ y^{\prime \prime}=(\cos x)^{\prime}=-\sin x, $$ 

 $$ y^{m}=(-\sin x)^{\prime}=-\cos x, $$ 