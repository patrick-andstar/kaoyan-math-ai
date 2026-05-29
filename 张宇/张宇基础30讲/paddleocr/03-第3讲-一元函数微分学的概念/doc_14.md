其中  $ o(\Delta x) $ 是在  $ \Delta x \to 0 $ 时比  $ \Delta x $ 更高阶的无穷小，则称  $ f(x) $ 在点  $ x_0 $ 处可微，并把增量的主要部分  $ \underline{A\Delta x} $ 称为线性主部，也叫作  $ f(x) $ 在点  $ x_0 $ 处的微分，记  $ \left.\mathrm{d}y\right|_{x=x_0} = A\Delta x $ 或  $ \left.\mathrm{d}y\right|_{x=x_0} = f'(x_0)\mathrm{d}x $。

可微 $ \Leftrightarrow $可导的证明：

 $$ f^{\prime}(x_{0})=\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\frac{A\Delta x}{\Delta x}+\lim_{\Delta x\to0}\frac{o(\Delta x)}{\Delta x}=A\ , $$ 

 $$ \left.\begin{aligned} 由此可知 \left.\mathrm{d}y\right|_{x=x_{0}}=A\cdot\Delta x=f^{\prime}(x_{0})\Delta x\end{aligned}\right.. $$ 

 $$  又 \frac{\mathrm{d}x=\Delta x}{ 夢詠 }\mathrm{,}\mathrm{ 故 }\left.\mathrm{d}y\right|_{x=x_{0}}=f^{\prime}(x_{0})\mathrm{d}x $$ 

 $$ \begin{array}{l}\Delta x=\mathrm{d}x+o(\Delta x),\quad 故 \Delta x=\mathrm{d}x\\ \quad\mid\mid\quad\mid\mid\\ 1\cdot\Delta x\quad0\end{array} $$ 

注 $ ^{(1)} $ 可微的判别.

①写增量  $ \Delta y = f(x_{0} + \Delta x) - f(x_{0}) $;

②写线性增量  $ A\Delta x = f'(x_0)\Delta x $；

③作极限  $ \lim_{\Delta x \to 0} \frac{\Delta y - A \Delta x}{\Delta x} \Leftrightarrow \Delta y = A \Delta x + o(\Delta x) $

若该极限等于 0，则  $ y = f(x) $ 在点  $ x_0 $ 处可微，否则不可微。

(2) 从上述判别步骤可以看出，用形式简单的 “线性增量  $ A\Delta x $” 去代替形式复杂的 “增量  $ \Delta y $”，且其误差 “ $ \Delta y - A\Delta x $” 是  $ o(\Delta x) $，这就是说，用 “简单的量” 代替了 “复杂的量”，且产生的误差又可以忽略不计，这就是可微的含义。

>判别可微首先考虑(3)，若没有则结合 $ f'(x_{0}) $的信息考虑(1)

(3) “ $ f(x) $在点 $ x_{0} $处可微”与“ $ f(x) $在点 $ x_{0} $处可导”互为充要条件，故判别 $ f(x) $在点 $ x_{0} $处是否可微可以转化为判别其在点 $ x_{0} $处是否可导，这样的话考生会比较熟悉.

(4) 可微的几何意义.

若 $ f(x) $在点 $ x_{0} $处可微，则在点 $ (x_{0},y_{0}) $附近可以用切线段近似代替曲线段，这是可微的几何意义。

(5) 图 3-15 可以较好地帮助考生理解以上论述.

<div style="text-align: center;"><img src="imgs/img_in_image_box_333_1092_763_1220.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">图 3-15</div>


例3.10 设函数  $ y = f(x) $ 在任意点  $ x $ 处的增量  $ \Delta y = \frac{y \Delta x}{x + \sqrt{x^2 + y^2}} + o(\Delta x) $，且  $ f(0) = 1 $，则  $ y = f(x) $ 在点  $ x = 0 $ 处的微分  $ \mathrm{d}y = (\quad) $.