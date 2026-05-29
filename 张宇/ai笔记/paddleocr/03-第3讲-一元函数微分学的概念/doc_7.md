(C)  $ n_{3} < n_{2} < n_{1} $

(D)

 $$ n_{2}<n_{3}<n_{1} $$ 

☐ 分析 该题是例 3.5 结论的具体应用.

解 应选(A).

由例 3.5 可知，若  $ \varphi(x) $ 在  $ x=x_{0} $ 处连续，则  $ f(x)=\left|x-x_{0}\right|\varphi(x) $ 在点  $ x_{0} $ 处可导的充分必要条件是

 $ \varphi(x_0) = 0 $

因式分解：

 $$ \begin{aligned}\left|x^{3}+x^{2}-2x-2\right|\\=\left|x^{2}(x+1)-2(x+1)\right|\\=\left|(x^{2}-2)(x+1)\right|\\=\left|x+1\right|\left|x+\sqrt{2}\right|\left|x-\sqrt{2}\right|\end{aligned} $$ 

 $$ \begin{aligned}f_{1}(x)&=(x^{2}-1)\underline{\left|x^{3}+x^{2}-2x-2\right|}=(x+1)(x-1)\Big|(x+\sqrt{2})(x-\sqrt{2})(x+1)\Big|\\&=(x+1)(x-1)\Big|x+\sqrt{2}\Big|\Big|x-\sqrt{2}\Big|\Big|x+1\Big|.\end{aligned} $$ 

当 $ f_{1}(x)=\left|x+\sqrt{2}\right|\left[(x+1)(x-1)\left|x-\sqrt{2}\right|\left|x+1\right|\right]=\left|x+\sqrt{2}\right|Q_{1}(x) $时， $ Q_{1}(-\sqrt{2})\neq0 $，故 $ x=-\sqrt{2} $是 $ f_{1}(x) $的不可导点.

当 $ f_{1}(x)=\left|x-\sqrt{2}\right|\left[(x+1)(x-1)\left|x+\sqrt{2}\right|\left|x+1\right|\right]=\left|x-\sqrt{2}\right|Q_{2}(x) $时， $ Q_{2}(\sqrt{2})\neq0 $，故 $ x=\sqrt{2} $是 $ f_{1}(x) $的不可

导点.

因式分解：

 $$ \begin{aligned}f_{2}(x)&=(x^{2}-1)\underline{\left|x^{3}-2x^{2}-x+2\right|}=(x+1)(x-1)\left|(x+1)(x-1)(x-2)\right|\\&=(x+1)(x-1)\left|x-2\right|\left|x-1\right|\left|x+1\right|.\end{aligned} $$ 

 $$ \begin{aligned}&\left|x^{3}-2x^{2}-x+2\right|\\=&\left|x^{2}(x-2)-(x-2)\right|\\=&\left|(x-2)(x^{2}-1)\right|\\=&\left|(x-2)(x-1)(x+1)\right|\end{aligned} $$ 

当 $ f_{2}(x)=|x-2|\left[(x+1)(x-1)|x-1||x+1|\right]=\left|x-2\right|Q_{3}(x) $时， $ Q_{3}(2)\neq0 $，故x=2是 $ f_{2}(x) $的不可导点。

 $$ \begin{aligned}f_{3}(x)&=(x^{2}-1)\underline{\left|x^{3}+3x^{2}-2x-6\right|}=(x+1)(x-1)\left|(x+\sqrt{2})(x-\sqrt{2})(x+3)\right|\\&=(x+1)(x-1)\left|x-\sqrt{2}\right|\left|x+\sqrt{2}\right|\left|x+3\right|.\end{aligned} $$ 

因式分解：

当 $ f_{3}(x)=\left|x+\sqrt{2}\right|\left[(x+1)(x-1)\left|x-\sqrt{2}\right|\left|x+3\right|\right]=\left|x+\sqrt{2}\right|Q_{4}(x) $时， $ Q_{4}(-\sqrt{2})\neq0 $

 $$ \begin{aligned}&\left|x^{3}+3x^{2}-2x-6\right|\\=&\left|x^{2}(x+3)-2(x+3)\right|\\=&\left|(x^{2}-2)(x+3)\right|\end{aligned} $$ 

 $$ =\left|(x-\sqrt{2})(x+\sqrt{2})(x+3)\right| $$ 

故  $ x = -\sqrt{2} $ 是  $ f_{3}(x) $ 的不可导点.

当  $ f_{3}(x)=\left|x-\sqrt{2}\right|\left[(x+1)(x-1)\left|x+\sqrt{2}\right|\left|x+3\right|\right]=\left|x-\sqrt{2}\right|Q_{5}(x) $ 时， $ Q_{5}(\sqrt{2})\neq0 $，故  $ x=\sqrt{2} $ 是  $ f_{3}(x) $ 的不可导点.

当 $ f_{3}(x)=\left|x+3\right|\left[(x+1)(x-1)\left|x-\sqrt{2}\right|\left|x+\sqrt{2}\right|\right]=\left|x+3\right|Q_{6}(x) $时， $ Q_{6}(-3)\neq0 $，故x=-3是 $ f_{3}(x) $的不可导点.

所以 $ f_{1}(x) $有两个不可导点 $ x=-\sqrt{2} $， $ x=\sqrt{2} $； $ f_{2}(x) $有一个不可导点 $ x=2 $； $ f_{3}(x) $有三个不可导点 $ x=-\sqrt{2} $， $ x=\sqrt{2} $， $ x=-3 $。于是， $ n_{2}<n_{1}<n_{3} $，应选(A).