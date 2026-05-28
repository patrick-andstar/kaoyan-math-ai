 $$ \lim_{x\to0}\frac{f(x)}{1-\cos x}=\lim_{x\to0}\frac{2f(x)}{x^{2}}=-1 $$ 

故  $ \lim_{x\to0}\frac{f(x)}{x^{2}}=-\frac{1}{2}<0 $ ，由极限的局部保号性可知，在 x=0 的某去心邻域内有  $ \frac{f(x)}{x^{2}}<0 $ ，即  $ f(x)<0 $ ，从而选 (D).

☑ 方法总结 见到  $ \lim_{x\to0}f(x)=A<0 $，则利用保号性：当  $ x\in\dot{U}(x_{0},\delta) $，有  $ f(x)<0 $。

公式  $ 1-\cos x \geq 0 $

## 5 无穷小的定义

如果当  $ x \to x_0 $（或  $ x \to \infty $）时，函数  $ f(x) $ 的极限为零，那么称函数  $ f(x) $ 为当  $ x \to x_0 $（或  $ x \to \infty $）时的无穷小，记为  $ \begin{cases} \text{本身就是 } 0 \to \text{是一个常数，唯一一个常数的无穷小（0是最高阶的无穷小）} \\ \text{本身不是 } 0 \text{，是趋于 } 0 \text{ 的 } f(x) \text{ 或 } \{x_n\} \to \text{是一个极限过程} \end{cases} $

 $$ \lim_{x\to x_{0}}f(x)=0( 或 \lim_{x\to\infty}f(x)=0). $$ 

注（脱帽法） $ \lim_{x\to\infty}f(x)=A\Leftrightarrow f(x)=A+\alpha $，这里 $ \lim_{x\to\infty}\alpha=0 $，即 $ \alpha $是 $ x\to\bullet $时的无穷小。

<div style="text-align: center;"><img src="imgs/img_in_image_box_484_716_660_779.jpg" alt="Image" width="17%" /></div>


把 A 换成 0，为什么要单独讲这个定义呢？因为它有特殊的、重要的地位和意义。

从牛顿、莱布尼茨开始，无穷小一直是一个无法解释的、必须回避的话题，包括第二次数学危机的产生，为什么大主教批判牛顿，牛顿都不敢讲话呢？因为对于无穷小是什么，他讲不出来，他一会儿让无穷小为零，一会儿让无穷小又不能为零，当无穷小在分母上，它就不能为零。然后，牛顿算出一个结果，加上一个无穷小，他就把无穷小扔掉了，无法解释！所以到了后来，才出现了魏尔斯特拉斯的 $ \varepsilon-\delta $语言。在前面讲极限时，讲过超实数系，这里来简单复习下，从数学上来讲，

 $$  有理数 \xrightarrow{\quad\sqrt{2}\quad} 实数 \xrightarrow{\quad\sqrt{-1}\quad} 复数 . $$ 

现在又遇到问题了，这个无穷小怎么表示呢？牛顿、莱布尼茨没有想到，这是因为历史局限性．即便后来的柯西和魏尔斯特拉斯给出了数学分析中的标准极限定义，他们也没有想到，把实数系再扩展成超实数系．

<div style="text-align: center;"><img src="imgs/img_in_image_box_384_1163_658_1230.jpg" alt="Image" width="26%" /></div>


超实数系里面是什么呢？首先是我们所学到的实数，除了这些实数之外，还引入了无穷小量和无穷大量的概念．一旦无穷小量、无穷大量进来了，这个实数系就变成了超实数系．我用最通俗的语言讲给大家，不过也不要深究，因为这需要强大的数理逻辑的底子．

超实数系告诉我们，任何一个实数 $ x_{0} $，自带光环，边上有无限个以它作为极限的超实数。

<div style="text-align: center;"><img src="imgs/img_in_image_box_454_1388_755_1426.jpg" alt="Image" width="29%" /></div>
