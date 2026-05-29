注 $ ^{(1)} $当需要讨论左、右极限时，用以下结论：

 $ \lim_{x\to x_0^+}f(x)=\lim_{x\to x_0^-}f(x)=f(x_0)\Leftrightarrow f(x) $ 在点  $ x_0 $ 处连续．

(2) 连续性运算法则.

①(连续性的四则运算法则)设 $ f(x) $与 $ g(x) $都在点 $ x=x_{0} $处连续，则 $ f(x)\pm g(x) $与 $ f(x)g(x) $在点 $ x=x_{0} $处连续，当 $ g(x_{0})\neq0 $时， $ f(x)/g(x) $在点 $ x=x_{0} $处也连续.

两个函数如果在同一个点 $ x_{0} $处连续，则它们的和差积商在这点也是连续的

②(复合函数的连续性)设  $ u = \varphi(x) $ 在点  $ x = x_0 $ 处连续， $ y = f(u) $ 在点  $ u = u_0 $ 处连续，且  $ u_0 = \varphi(x_0) $，则  $ f[\varphi(x)] $ 在点  $ x = x_0 $ 处连续。

容易理解，不做证明，有些不需要证明，有些可能是超纲的

③(反函数的连续性)设 $ y=f(x) $在区间 $ I_x $上单调且连续，则反函数 $ x=\varphi(y) $在对应的区间 $ I_y=\{y\mid y=f(x),x\in I_x\} $上连续且有相同的单调性.

★ (3) 设  $ f(x) $ 在点  $ x = x_0 $ 处连续，且  $ f(x_0) > 0 $ （或  $ f(x_0) < 0 $），则存在  $ \delta > 0 $，使得当  $ |x - x_0| < \delta $ 时， $ f(x) > 0 $（或  $ f(x) < 0 $）。这句话非常重要！

<div style="text-align: center;"><img src="imgs/img_in_image_box_478_681_629_751.jpg" alt="Image" width="14%" /></div>


## 2 间断点的定义与分类

以下设函数 $ f(x) $在点 $ x_{0} $的某去心邻域内有定义.

讨论间断点只看无定义点和分段点，一个初等函数在其定义区间内都是连续的.

<div style="text-align: center;"><img src="imgs/img_in_image_box_712_871_964_968.jpg" alt="Image" width="24%" /></div>


区间  $ [a, b] $ 上连续，是指 a 处（左端点）右连续，b 处（右端点）左连续。

间断点中，无单侧间断的概念(考研数学中).区间端点是不考虑间断的.

<div style="text-align: center;"><img src="imgs/img_in_image_box_404_1048_659_1133.jpg" alt="Image" width="24%" /></div>


(1) 可去间断点.

若  $ \lim_{x\to x_0}f(x)=A\neq f(x_0)(f(x_0) $ 甚至可以无定义），则  $ x=x_0 $ 称为可去间断点。（可补间断点）

<div style="text-align: center;"><img src="imgs/img_in_image_box_135_1237_309_1348.jpg" alt="Image" width="16%" /></div>


 $ f(x)=\left\{\begin{aligned}&\frac{\sin x}{x},&x\neq0,\\&1,&x=0,\end{aligned}\right. $ 则  $ f(x) $ 在 x=0 处就连续