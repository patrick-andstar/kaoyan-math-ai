例 9.6 设  $ f(\ln x) = \frac{\ln(1+x)}{x} $，计算  $ \int f(x) \, dx $。

☑分析 首先，本题要求出 $ f(x) $的表达式，一般方法是令 $ t=\ln x $。其次，计算具体积分，或先凑微分再分部积分，或换元再分部积分。

解 设  $ \ln x = t $，则  $ x = e^{t} $， $ f(t) = \frac{\ln(1 + e^{t})}{e^{t}} $，故

 $$ \begin{aligned}\int f(x)\mathrm{d}x=&\int\frac{\ln(1+\mathrm{e}^{x})}{\mathrm{e}^{x}}\mathrm{d}x=-\int\ln(1+\mathrm{e}^{x})\mathrm{d}(\mathrm{e}^{-x})\\=&-\mathrm{e}^{-x}\ln(1+\mathrm{e}^{x})+\int\frac{1}{1+\mathrm{e}^{x}}\mathrm{d}x\\=&-\mathrm{e}^{-x}\ln(1+\mathrm{e}^{x})+\int\left(1-\frac{\mathrm{e}^{x}}{1+\mathrm{e}^{x}}\right)\mathrm{d}x\\=&-\mathrm{e}^{-x}\ln(1+\mathrm{e}^{x})+x-\ln(1+\mathrm{e}^{x})+C\\=&x-(1+\mathrm{e}^{-x})\ln(1+\mathrm{e}^{x})+C.\end{aligned} $$ 

例 9.7 计算不定积分  $ \int e^{2x}(\tan x+1)^{2}dx $

☑ 分析 展开平方，利用三角函数公式化简.

解

 $$ \begin{aligned}\int\mathrm{e}^{2x}(\tan x+1)^{2}\mathrm{d}x&=\int\mathrm{e}^{2x}(\sec^{2}x+2\tan x)\mathrm{d}x\\&=\int\mathrm{e}^{2x}\sec^{2}x\mathrm{d}x+2\int\mathrm{e}^{2x}\tan x\mathrm{d}x\\&=\int\mathrm{e}^{2x}\mathrm{d}(\tan x)+2\int\mathrm{e}^{2x}\tan x\mathrm{d}x\\&=\mathrm{e}^{2x}\tan x-\boxed{2\int\mathrm{e}^{2x}\tan x\mathrm{d}x+2\int\mathrm{e}^{2x}\tan x\mathrm{d}x}\xrightarrow{ 通过分部积分，出现正负相反的积分 }\\&=\mathrm{e}^{2x}\tan x+C\;.\end{aligned} $$ 

## 4 有理函数的积分

(1) 定义.

形如 $ \int\frac{P_{n}(x)}{Q_{m}(x)}\mathrm{d}x(n<m) $的积分称为有理函数的积分，其中 $ P_{n}(x) $， $ Q_{m}(x) $分别是x的n次多项式和m次多项式.

 $ \rightarrow\frac{P_{n}(x)}{Q_{m}(x)}\left\{\begin{array}{l}n<m 真分式, \\ n\geq m 假分式 = 多项式 + 真分式. 比如: \frac{x^{2}}{x+1}=\frac{x^{2}-1+1}{x+1}=x-1+\frac{1}{x+1}.\end{array}\right. $

(2) 思想.

若  $ Q_{m}(x) $ 在实数域内可因式分解，则因式分解后再把  $ \frac{P_{n}(x)}{Q_{m}(x)} $ 拆成若干项最简有理分式之和.

有理式=最简有理分式之和，其中最简有理分式分为 $ \frac{A}{ax+b} $， $ \frac{A_k}{(ax+b)^k} $， $ \frac{Ax+B}{px^2+qx+r} $， $ \frac{A_k x+B_k}{(px^2+qx+r)^k} $

 $ (k=2,3,\cdots) $.