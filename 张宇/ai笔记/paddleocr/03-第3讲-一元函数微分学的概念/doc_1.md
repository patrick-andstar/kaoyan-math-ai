①  $ I_{1} $ :  $ \lim_{\Delta t \to 0} \frac{f(t + \Delta t) - f(t)}{\Delta t} \xlongequal{\text{存在}} a $. 注意：a是瞬时变化率，不是平均变化率， $ \rightarrow $线性函数变化率不变

②  $ I_{2} $ :  $ \lim_{\Delta t \to 0} \frac{f(t + \Delta t) - f(t)}{\Delta t} = \lim_{\Delta t \to 0} \frac{0}{\Delta t} = 0 $.



<div style="text-align: center;"><img src="imgs/img_in_image_box_169_138_305_224.jpg" alt="Image" width="13%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_239_306_309.jpg" alt="Image" width="13%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_162_325_316_404.jpg" alt="Image" width="14%" /></div>


 $ \lim_{\Delta t \to 0} \frac{f(t + \Delta t) - f(t)}{\Delta t} = $定值.

极限是研究函数变化趋势的，导数是研究变化快慢趋势的。

<div style="text-align: center;"><img src="imgs/img_in_image_box_107_504_170_573.jpg" alt="Image" width="6%" /></div>


## 基础内容精讲

## 1 导数

 $$ \Delta x\rightarrow0^{+},\quad\Delta x\rightarrow0^{-} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_849_589_952_695.jpg" alt="Image" width="9%" /></div>


设  $ y = f(x) $ 定义在区间 I 上，让自变量在  $ x = x_0 $ 处加一个增量  $ \Delta x $（可正可负），其中  $ x_0 \in I $， $ x_0 + \Delta x \in I $，则可得函数的增量  $ \Delta y = f(x_0 + \Delta x) - f(x_0) $。若函数增量  $ \Delta y $ 与自变量增量  $ \Delta x $ 的比值在  $ \Delta x \to 0 $ 时的极限存在，即  $ \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} $ 存在，则称函数  $ y = f(x) $ 在点  $ x_0 $ 处可导，并称这个极限为  $ y = f(x) $ 在点  $ x_0 $ 处的导数，记作  $ f'(x_0) $，即

变化率

 $$ f^{\prime}(x_{0})=\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x)-f(x_{0})}{\Delta x}. $$ 

当然， $ \left.\frac{dy}{dx}\right|_{x=x_0} $， $ \left.\frac{d[f(x)]}{dx}\right|_{x=x_0} $， $ y'(x_0) $ 或  $ y'\big|_{x=x_0} $ 这些符号记法与  $ f'(x_0) $ 等价。顺便交代一下，“导数”这个名词被认为是拉格朗日最先使用的，记号  $ f'(x_0) $， $ y'\big|_{x=x_0} $ 多次出现在拉格朗日的文章中，而莱布尼茨则喜欢写作  $ \left.\frac{dy}{dx}\right|_{x=x_0} $， $ \left.\frac{d[f(x)]}{dx}\right|_{x=x_0} $。 $ \left.\frac{\left(\frac{\frac{dy}{dx}}{dx}\right)^2}{dx}\right|_{x=x_0} $ 的形式，也叫微商；考研只用拉格朗日和莱布尼茨写法。莱布尼茨所用的符号  $ d $ 具有普适意义：如果要求  $ A $ 对  $ B $ 的变化率，就把  $ A $， $ B $ 填进  $ \left.\frac{d\Delta}{d\Omega}\right. $，得  $ \left.\frac{dA}{dB}\right. $，它可表示几乎所有你想研究的变化率问题，而不仅仅是位移  $ s $ 对时间  $ t $ 的变化率—— $ \frac{ds}{dt} $ 等于速度  $ v $。

比如： $ \left.\frac{d(兴趣)}{d(时间)}\right. $，它往往小于零，你同意吗？再比如： $ \left.\frac{d(利润)}{d(价格)}\right. $，若  $ \left.\frac{d(利润)}{d(价格)}\right. $ > 0，也就是涨价可以增加利润，此时定价低了；若  $ \left.\frac{d(利润)}{d(价格)}\right. $ < 0，也就是降价可以增加利润，此时定价高了。综上，当  $ \left.\frac{d(利润)}{d(价格)}\right. $ = 0 时，利润最大，也就是说导数为零时的价格应是商品标签上的数字。懂得了这些道理后，请问，当  $ \left.\frac{d(成绩)}{d(努力)}\right. $ > 0 时，说明什么？