正实数表达，只能用超实数“无穷小”来衡量，它们并不只是在那里，它们相依相偎；可导是说，它们不仅依偎在一起，而且Y们靠近y的速度不会比X们靠近x的速度慢，也就是速度一样或者速度更快(见图3-4)。

<div style="text-align: center;"><img src="imgs/img_in_image_box_187_223_897_358.jpg" alt="Image" width="68%" /></div>


<div style="text-align: center;">图 3-2</div>


<div style="text-align: center;">图 3-3</div>


<div style="text-align: center;">图3-4</div>


所以，函数存在是y和Y们无牵无挂地待在那里；函数连续是y和Y们充分靠近；导函数存在是y和Y们不仅充分靠近，且靠近的速度更快。连续曲线不是曲线不断开，恰恰相反，它每一个位置都是断开的。就算Y们靠得更近，比如可导，也只是靠得更近而已，依然是断开的。

例 3.1 以下命题，错误的是（）.

(A) 若  $ f(x) $ 是可导的偶函数，则  $ f'(x) $ 是奇函数

导数的性质，选项当结论记住，会应用即可



(B) 若  $ f(x) $ 是可导的奇函数，则  $ f'(x) $ 是偶函数

(C) 若  $ f(x) $ 是可导的周期为 T 的周期函数，则  $ f'(x) $ 也是以 T 为周期的周期函数

(D) 若  $ f(x) $ 是可导的有界函数，则  $ f'(x) $ 是有界函数

解 应选(D).

对于选项 $ (\mathrm{A}) $，由导数定义，得

 $$ \begin{aligned}f^{\prime}(-x)&=\lim_{\Delta x\to0}\frac{f(-x+\Delta x)-f(-x)}{\Delta x}=\lim_{\Delta x\to0}\frac{f(x-\Delta x)-f(x)}{\Delta x}\\&=(-1)\lim_{\frac{-\Delta x\to0}{ 狥 }}\frac{f(x-\Delta x)-f(x)}{-\Delta x}=-f^{\prime}(x),\\ \end{aligned} $$ 

故 $ f'(x) $是奇函数.

对于选项 $ (\mathrm{B}) $，由导数定义，得

 $$ \begin{aligned}f^{\prime}(-x)&=\lim_{\Delta x\to0}\frac{f(-x+\Delta x)-f(-x)}{\Delta x}\\&=\lim_{\Delta x\to0}\frac{-f(x-\Delta x)+f(x)}{\Delta x}\\&=\lim_{-\Delta x\to0}\frac{f(x-\Delta x)-f(x)}{-\Delta x}\\&=f^{\prime}(x),\end{aligned} $$ 

故 $ f'(x) $是偶函数.

对于选项 $ (\mathrm{C}) $，由导数定义，得

 $$ f^{\prime}(x+T)=\lim_{\Delta x\to0}\frac{f(x+T+\Delta x)-f(x+T)}{\Delta x} $$ 