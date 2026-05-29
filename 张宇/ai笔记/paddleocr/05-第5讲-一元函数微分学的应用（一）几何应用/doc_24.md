5.7  $ y=2x+1 $ 解

 $$ a=\lim_{x\to\infty}\frac{y}{x}=\lim_{x\to\infty}\left(2-\frac{1}{x}\right)\mathrm{e}^{\frac{1}{x}}=2 $$ 

 $$ b=\lim_{x\to\infty}(y-ax)=\lim_{x\to\infty}[2x(\mathrm{e}^{\frac{1}{x}}-1)-\mathrm{e}^{\frac{1}{x}}]=\lim_{x\to\infty}\left[\frac{2(\mathrm{e}^{\frac{1}{x}}-1)}{\frac{1}{x}}-\mathrm{e}^{\frac{1}{x}}\right]=1, $$ 

所以斜渐近线方程为 $ y=2x+1 $。

5.8  $ (-1,0) $ 解 将  $ y' = 2x + 1 $,  $ y'' = 2 $ 代入曲率公式  $ k = \frac{|y''|}{[1 + (y')^2]^{\frac{3}{2}}} $，得  $ \frac{2}{[1 + (2x + 1)^2]^{\frac{3}{2}}} = \frac{\sqrt{2}}{2} $，整理后有  $ x^2 + x = 0 $，由于 x < 0，因此得 x = -1，又有  $ y|_{\perp} = 0 $，故所求点的坐标为  $ (-1,0) $。

5.9 解 方程两边对 x 求导可得

 $$ 3y^{2}y^{\prime}-2yy^{\prime}+xy^{\prime}+y-x=0, $$ 

令 $ y^{\prime}=0 $，由 $ \left(*\right) $得y=x，将其代入原方程有

 $$ 2x^{3}-x^{2}-1=0, $$ 

从而可得唯一驻点 $ x=1 $.(*)式两边再对x求导，得

 $$ (3y^{2}-2y+x)y^{\prime \prime}+2(3y-1)(y^{\prime})^{2}+2y^{\prime}-1=0, $$ 

因此 $ y''|_{x=1}=\frac{1}{2}>0 $，故x=1是 $ y=y(x) $的极小值点.