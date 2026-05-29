注 此题的被积函数被命制成具体函数，但  $ \iint\limits_{D(t)} f(x, y) \, d\sigma $ 难以计算，故考虑利用二重积分的中值定理来处理。同理，若被积函数被命制成抽象函数，也可以考虑利用二重积分中值定理来处理，如：设  $ f(x, y) $ 具有二阶连续偏导数，

 $$ D(t)=\{(x,\ y)\big|0\leqslant x\leqslant t,\ 0\leqslant y\leqslant t\}\ , $$ 

令  $  F(t) = \iint_{D(t)} f_{xy}''(x, y) \, dx \, dy  $，求  $  F_{+}'(0)  $

解

 $$ \begin{aligned}F_{+}^{\prime}(0)&=\lim_{t\rightarrow0^{+}}\frac{F(t)-F(0)}{t-0}=\lim_{t\rightarrow0^{+}}\frac{\iint\limits_{D(t)}f_{xy}^{\prime \prime}(x,y)\mathrm{d}x\mathrm{d}y}{t-0}\\&\xlongequal{ 二重积分的中值定理 }\lim_{t\rightarrow0^{+}}\frac{f_{xy}^{\prime \prime}(\xi,\eta)\cdot t^{2}}{t}=\lim_{t\rightarrow0^{+}}\overset{0}{\underset{t\rightarrow0^{+}}{\rightarrow}}t\cdot f_{xy}^{\prime \prime}(\xi,\eta)=0.\end{aligned} $$ 

方法总结 当  $ \iint_{D}f(x,y)d\sigma $ 难计算或者  $ f(x,y) $ 为抽象型时，可考虑利用二重积分的中值定理来处理.

∂公式  $ \iint_{D}f(x,y)\mathrm{d}\sigma=f(\xi,\eta)\cdot S_{D},(\xi,\eta)\in D $ ，其中 $ S_{D} $ 为D的面积.

3 普通对称性与轮换对称性必考题！

(1) 普通对称性.

设区域D关于y轴对称，如图14-4所示，取对称的两块小面积dσ，对称点分别为$(x,y)$与$(-x,y)$，则对称点处的高分别为$f(x,y)$与$f(-x,y)$。依据定义，对称位置的两个“小竖条”的体积分别为$f(x,y)d\sigma$与$f(-x,y)d\sigma$。因为$d\sigma$一样，所以，当$f(x,y)=f(-x,y)$时，$f(x,y)d\sigma=f(-x,y)d\sigma$，体积相同，此时只需计算对称区域的一半，然后乘以2即可得到整个积分值；而当$f(x,y)=-f(-x,y)$时，$f(x,y)d\sigma=-f(-x,y)d\sigma$，对称区域的体积正好相反，这样累加起来的总体积自然就是0。于是，我们有

<div style="text-align: center;"><img src="imgs/img_in_image_box_729_804_943_1021.jpg" alt="Image" width="20%" /></div>


<div style="text-align: center;">图 14-4</div>


 $$ \iint\limits_{D}f(x,y)\mathrm{d}x\mathrm{d}y=\left\{\begin{aligned}&2\iint\limits_{D_{1}}f(x,y)\mathrm{d}x\mathrm{d}y,&f(x,y)=f(-x,y),\\ &0,&f(x,y)=-f(-x,y),\end{aligned}\right. $$ 

☑把对称点代入，函数值相同，即2倍；函数值相反，即为0（偶倍奇零）

其中 $ D_{1} $是D在y轴右侧的部分.

你看，用这种基于概念的分析方法，不用死记硬背，而且真正理解了性质的本质。现将二重积分有关的对称性全面总结如下。

①若D关于y轴对称，则

<div style="text-align: center;"><img src="imgs/img_in_image_box_790_1299_945_1404.jpg" alt="Image" width="15%" /></div>
