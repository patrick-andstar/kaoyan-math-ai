故选(A).

方法二 由题设可得在 x=0 处

 $$ \sin x=(1+x^{2})(ax+bx^{2}+cx^{3}+\cdots), $$ 

所以

 $$ \lim_{x\to0}\frac{\sin x}{x}=\lim_{x\to0}(1+x^{2})(a+bx+cx^{2}+\cdots)=a, $$ 

故a=1

又因为  $ \sin x $ 为奇函数，所以 b = 0，从而可得

 $$ \sin x=(1+x^{2})(x+cx^{3}+\cdots), $$ 

故

 $$ c=\lim_{x\to0}\frac{\sin x-(1+x^{2})x}{x^{3}}=\lim_{x\to0}\frac{\sin x-x}{x^{3}}-1=\lim_{x\to0}\frac{\cos x-1}{3x^{2}}-1=-\frac{7}{6} $$ 

故选(A).

注 此题 $ f(x) $是奇函数，既然写“=”，则两边性质是一样的，相同的函数，即左边是奇函数，所以右边不能有偶次方，故 $ b=0 $，(C)，(D)排除.

<div style="text-align: center;"><img src="imgs/img_in_image_box_78_693_673_771.jpg" alt="Image" width="57%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_822_696_925_803.jpg" alt="Image" width="9%" /></div>


## 连续点的定义

设函数 $ f(x) $在点 $ x_{0} $的某一邻域内有定义，且有 $ \lim_{x\to x_{0}}f(x)=f(x_{0}) $，则称函数 $ f(x) $在点 $ x_{0} $处连续.

什么叫函数连续？先说什么叫函数存在.存在是说，给了一个x，就有一个y对应在那里(见图1-27)，它附近的点X们所对应的Y们也是如此，它们只是在那里，无牵无挂；连续是说，Y们充分靠近y（见图1-28），它们彼此的距离小到无法用任何小的正实数表达，只能用超实数“无穷小”来衡量，它们并不只是在那里，它们相依相偎.

<div style="text-align: center;"><img src="imgs/img_in_image_box_281_1064_723_1196.jpg" alt="Image" width="42%" /></div>


<div style="text-align: center;">图1-27</div>


<div style="text-align: center;">图1-28</div>


所以，函数存在，是 y 和 Y 们都无非无挂地待在那里；函数连续，是 y 和 Y 们都无非无挂地待在那里；函数连续，是 y 和 Y 都没有。连续并不是真的连着，连续只是 Y 彼此充分靠近而已，也可以说，连续就是一种离散，连续曲线不是曲线不断开，恰恰相反，它每一个位置都是断开的。我们对于客观事物的刻画，严格说来，都是一种近似，只是看这种近似的代价是不是可以被接受。