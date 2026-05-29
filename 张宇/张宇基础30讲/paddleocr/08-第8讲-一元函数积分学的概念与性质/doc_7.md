个变化而已（也许以后你们还会接触到分数阶导数甚至更为精细的刻画变化率的工具）.

(3) 若  $ f(x) $ 可导，则  $ f'(x) $ 可能连续，也可能含有振荡间断点。

连续不难理解，那么振荡间断点是什么样子？它是真的断了吗？在现代数学提出了超实数理论后，我们已经知道了，事实上，没有什么线是连着的，只是点与点近不近，有多近的问题罢了。

①设 $ f_{1}(x)=\sin x $， $ \lim_{x\to+\infty}\sin x $振荡不存在，其大致图形为

<div style="text-align: center;"><img src="imgs/img_in_image_box_575_305_846_383.jpg" alt="Image" width="26%" /></div>


②设

 $$ f_{2}(x)=\begin{cases}\sin\frac{1}{x},&x\neq0,\\0,&x=0,\end{cases} $$ 

可以看出， $ \sin\frac{1}{x} $ 由  $ \sin u $ 和  $ u = \frac{1}{x} $ 复合而成。当  $ x \to 0^{+} $ 时， $ u \to +\infty $，故  $ \lim_{x \to 0^{+}} \sin\frac{1}{x} $ 依然是振荡不存在。

但这里有一个关键问题：这里的振荡是在 $ x\rightarrow0^{+} $时发生的，也就是x与0充分靠近、无限靠近时

发生的，于是可以看作将①中的

<div style="text-align: center;"><img src="imgs/img_in_image_box_349_604_816_723.jpg" alt="Image" width="45%" /></div>


将  $ x \rightarrow 0^{-} $也画出来，则大致图形为  $ \begin{array}{c} \uparrow \\ \downarrow \\ \downarrow \\ \downarrow \end{array} \quad \begin{array}{c} \uparrow \\ \downarrow \\ \downarrow \\ \downarrow \end{array} \quad \begin{array}{c} \uparrow \\ \downarrow \\ \downarrow \\ \downarrow \end{array} \quad \begin





<div style="text-align: center;"><img src="imgs/img_in_image_box_405_739_610_859.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_545_913_720_1008.jpg" alt="Image" width="16%" /></div>


大无穷倍吗？显然不能，故我们是看不到实际图形的，好在人类有思考能力可以想象到。

c. 振荡间断点露出了本来的面目，放大无穷倍后，即 $ \xrightarrow{\uparrow} $，还原成原来的样子，

<div style="text-align: center;"><img src="imgs/img_in_image_box_561_1059_730_1147.jpg" alt="Image" width="16%" /></div>


它是这样的：

<div style="text-align: center;"><img src="imgs/img_in_image_box_185_1159_392_1269.jpg" alt="Image" width="20%" /></div>


至此，我们明白了：