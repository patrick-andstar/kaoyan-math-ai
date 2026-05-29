合并、分子分母同除变量的最高次幂等， $ \underline{\text{高级的恒等变形法如变量代换，也叫换元法等）}} $.需要强调的是，很多问题如果不化简就计算，可能计算会很复杂，甚至可能计算不出结果． $ \underline{\text{如负代换，倒代换}} $

如： $ \lim_{x\to0}\left(\frac{1+\sin x}{x}-\frac{1}{\mathrm{e}^x-1}\right)=\lim_{x\to0}\left(\frac{1}{x}-\frac{1}{\mathrm{e}^x-1}\right)+\lim_{x\to0}\frac{\sin x}{x} $ 解题的方法，我们不能蛮干，一定要注意这些细节，细节决定成败。

②判断类型（运算类型）.

用在函数中，难度就很高了，对于这种问题呢，《考研数学基础30讲》里面也会提及，我会给大家一个完整的全面的归纳

③选择方法（洛必达法则、 $ \underline{\text{泰勒公式}} $、 $ \underline{\text{夹逼准则等}} $）

→太重要了，“火眼金睛”泰勒

(1) “ $ \frac{0}{0} $” “ $ \frac{\infty}{\infty} $” “ $ 0 \cdot \infty $”.

例1.24  $ \lim_{x\to0^{+}}\frac{(1+x)^{\frac{1}{x}}-e}{x}= $ ___.这是考研中喜欢出的一种类型（提前告诉存在了，实际上问是几）

♡分析 “ $ \frac{0}{0} $”，先做恒等变形， $ u(x)^{v(x)} = e^{v(x)\ln u(x)} $。碰到幂指函数，一定用 e 抬起来。

解 应填  $ -\frac{e}{2} $

 $$ \begin{aligned}& 原极限 =\lim_{x\to0^{+}}\frac{\mathrm{e}^{\frac{1}{x}\ln(1+x)}-\mathrm{e}}{\ x\ }=\mathrm{e}\lim_{x\to0^{+}}\frac{\mathrm{e}^{\frac{1}{x}\ln(1+x)-1}}{\ x\ }-\frac{1}{\mathrm{e}}\overset{ 痢 -1\sim 痢 ( 狥 \to0)}{\lim_{x\to0^{+}}}\frac{\frac{1}{x}\ln(1+x)-1}{\ x\ }\\&\xlongequal{ 通分 }\mathrm{e}\lim_{x\to0^{+}}\frac{\ln(1+x)-x}{\ x^{2}}\xlongequal{=\mathrm{e}\lim_{x\to0^{+}}\frac{-\frac{1}{2}x^{2}}{x^{2}}=-\frac{1}{2}\mathrm{e}\ }\cdot\lim_{x\to0^{+}}\frac{\ln(1+x)-x}{\ x^{2}}\xlongequal{ 溏必法法则 }\lim_{x\to0^{+}}\frac{\frac{1}{1+x}-1}{\ 2x}\\ \end{aligned} $$ 

方法总结 碰到幂指函数，用 e 括起来， $ u(x)^{\nu(x)} = e^{\nu(x)\ln u(x)} $

公式 当  $ x \to 0 $ 时， $ \ln(1+x)-x \sim -\frac{1}{2}x^{2} $

注  $ f(x)=(1+x)^{\frac{1}{x}} $ 在 x>0 时有以下性质：

① $ f(x) $单调减少；② $ \lim_{x\to0^{+}}f(x)=e $；

 $$ \lim_{x\to0}(1+x)^{\frac{1}{x}}=e\quad\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^{x}=e $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_367_1129_529_1253.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_538_1130_709_1256.jpg" alt="Image" width="16%" /></div>


★③ $ (1+x)^{\frac{1}{x}} - e \sim -\frac{e}{2} x (x \to 0^{+}) $．刚才的例1.24

这个结论太重要了，0 是一个重要的实数。