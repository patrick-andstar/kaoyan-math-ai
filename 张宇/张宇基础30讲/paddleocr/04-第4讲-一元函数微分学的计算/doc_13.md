(2) 莱布尼茨公式 → 主要考乘积形式

设 $ u=u(x) $， $ v=v(x) $均n阶可导，则

 $$ \begin{aligned}&(u\pm\nu)^{(n)}=u^{(n)}\pm\nu^{(n)},\ $ uv)^{(n)}=u^{(n)}\nu+C_{n}^{1}u^{(n-1)}\nu^{\prime}+C_{n}^{2}u^{(n-2)}\nu^{\prime \prime}+\cdots+C_{n}^{k}u^{(n-k)}\nu^{(k)}+\cdots+C_{n}^{n-1}u^{\prime}\nu^{(n-1)}+u\nu^{(n)}\  共 n+1 项 \\&=\sum_{k=0}^{n}C_{n}^{k}u^{(n-k)}\nu^{(k)}.\\ \end{aligned} $$ 

考研中往往给出的是低次幂的幂函数作为 $ u(x) $或 $ v(x) $.

例如，给出的 $ u(x) $或 $ v(x) $为 $ x^{2} $，其三阶导数为0，则 $ u(x)\cdot v(x) $的n阶导数只有3项

(*)式，就是求函数乘积的高阶导数的莱布尼茨公式，其中 $ u^{(0)}=u,v^{(0)}=v. $

注 (1) 见到求两个函数乘积的高阶导数，一般用莱布尼茨公式即可，有时要结合“(1)归纳法”中的通式；当一个函数求高阶导数较困难时，若能转化成两个函数的乘积形式，亦可用莱布尼茨公式.

(2) 若 n 不太大，其系数  $ C_{n}^{0} $， $ C_{n}^{1} $， $ C_{n}^{2} $， $ \cdots $， $ C_{n}^{n-1} $， $ C_{n}^{n} $ 的记忆方法可按下述 “三角形”：

 $  \phi  $ ( $ \arcsin x $)' =  $ \frac{1}{\sqrt{1-x^2}} $ 。则 ( $ \arcsin x $)' *  $ \sqrt{1-x^2} $ = 1 。

令  $ u = (\arcsin x)' $， $ v = \sqrt{1 - x^2} $，故  $ u \cdot v = 1 $，所  $ \therefore \frac{1}{2}(u \cdot v)^{(n-1)} = 1^{(n-1)} = 0 $

 $$ C_{n-1}^{0}(\arcsin x)^{(n)}\sqrt{1-x^{2}}+\cdots+C_{n-1}^{n-1}(\arcsin x)^{\prime}\left(\sqrt{1-x^{2}}\right)^{(n-1)}=0 $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_635_630_848_798.jpg" alt="Image" width="20%" /></div>


例4.17 设 $ f(x)=xe^{x} $，则 $ f^{(n)}(x)= $___。

♣分析 本题是两类不同函数乘积的 n 阶导数，且其中  $ u(x)=x $ 是低次幂函数，可以考虑莱布尼茨公式，最后只有 2 项！

解 应填 $ (n+x)e^{x} $

 $$ f^{(n)}(x)=(x\mathrm{e}^{x})^{(n)}=(e^{x})^{(n)}x+C_{n}^{1}(\mathrm{e}^{x})^{(n-1)}\bullet1=x\mathrm{e}^{x}+n\mathrm{e}^{x}=(n+x)\mathrm{e}^{x}. $$ 

方法总结 求两类不同函数乘积的 n 阶导数，用莱布尼茨公式.

 $$ (uv)^{(n)}=u^{(n)}v+C_{n}^{1}u^{(n-1)}v^{\prime}+C_{n}^{2}u^{(n-2)}v^{\prime\prime}+\cdots+C_{n}^{k}u^{(n-k)}v^{(k)}+\cdots+C_{n}^{n-1}u^{\prime}v^{(n-1)}+uv^{(n)}=\sum_{k=0}^{n}C_{n}^{k}u^{(n-k)}v^{(k)} $$ 

(3)泰勒展开式.  $ \rightarrow $也称任意阶可导.

①任何一个无穷阶可导的函数都可写成

抽象展开

 $$ y=f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n}, $$ 

或者

 $$ y=f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^{n} $$ 

具体展开

②题目给出一个具体的无穷阶可导函数 $ y=f(x) $，可以通过已知公式展开成幂级数。这些已知公式为