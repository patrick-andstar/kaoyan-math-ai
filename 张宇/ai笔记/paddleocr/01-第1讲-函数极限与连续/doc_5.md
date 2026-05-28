解 直接由  $ y = \ln\left(x + \sqrt{x^2 + 1}\right) $ 解出  $ x = f^{-1}(y) $ 会很麻烦，现采用下述方法。

 $$ -y=-\ln\left(x+\sqrt{x^{2}+1}\right)=\ln\frac{1}{x+\sqrt{x^{2}+1}} $$ 

 $$ \frac{ 分母有理化 }{\ln\frac{\sqrt{x^{2}+1}-x}{\left(\sqrt{x^{2}+1}+x\right)\left(\sqrt{x^{2}+1}-x\right)}}=\ln\left(\sqrt{x^{2}+1}-x\right) $$ 

所以

 $$ \mathbf{e}^{-y}=\sqrt{x^{2}+1}-x, $$ 

再由  $ y = f(x) $ 的表达式有

 $$ \mathrm{e}^{\gamma}=\sqrt{x^{2}+1}+x, $$ 

②-①，得

 $$ x=\frac{1}{2}\big(\mathbf{e}^{y}-\mathbf{e}^{-y}\big), $$ 

交换上式中x, y的位置后就是 $ y = f(x) $的反函数，即

 $$ y=f^{-1}(x)=\frac{1}{2}\left(\mathrm{e}^{x}-\mathrm{e}^{-x}\right),-\infty<x<+\infty. $$ 

☑ 方法总结 利用对数的性质，巧妙地反解 x。

公式  $ \ln(x+\sqrt{x^{2}+1}) $ 是常见的奇函数.

注 (1) 函数  $ y = \ln\left(x + \sqrt{x^2 + 1}\right) $ 叫作反双曲正弦函数，其图像如图 1-3(a) 所示。函数  $ y = \frac{e^x - e^{-x}}{2} $ 叫作双曲正弦函数，其图像如图 1-3(b) 所示。考生应记住这两个函数的图像。

<div style="text-align: center;"><img src="imgs/img_in_image_box_407_908_525_1032.jpg" alt="Image" width="11%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_544_909_666_1022.jpg" alt="Image" width="11%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 1-3</div>


(2)  $ y = \frac{e^{x} + e^{-x}}{2} $ 叫作双曲余弦函数，其图像如图 1-4 所示，它是偶函数，是一种特殊的悬链线。达·芬

奇在画《抱银貂的女子》时，曾仔细思索过女子的脖子上戴的项链的形状是什么函数，可惜他一生都未能明白，在他去世近200年后，约翰·伯努利解决了这个问题。那不是抛物线  $ y = x^2 $，而是悬链线  $ y = \frac{a}{2} \left( e^{\frac{x}{a}} + e^{-\frac{x}{a}} \right) $，取  $ a = 1 $，便是  $ y = \frac{e^x + e^{-x}}{2} $。

<div style="text-align: center;"><img src="imgs/img_in_image_box_700_1162_849_1278.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;">图 1-4</div>


这个函数没有反函数