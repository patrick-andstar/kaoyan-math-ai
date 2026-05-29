现在可以准确回答这个问题了——振荡间断点是什么样子？它是真的断了吗？设

 $$ f(x)=\begin{cases}x^{2}\cos\frac{1}{x},&x\neq0,\\0,&x=0,\end{cases} $$ 

其在 $ (-∞,+∞) $上处处可导，且其导函数为

 $$ f^{\prime}(x)=\begin{cases}2x\cos\frac{1}{x}+\sin\frac{1}{x},&x\neq0,\\0,&x=0.\end{cases} $$ 

显然，

 $$ \lim_{x\to0}f^{\prime}(x)\xlongequal{(*)}\lim_{x\to0}2x\cos\frac{1}{x}+\lim_{x\to0}\sin\frac{1}{x}=\lim_{x\to0}\sin\frac{1}{x} $$ 

极限振荡不存在。请原谅我在 $ (*) $处鲁莽地拆开了，那只是为了让各位更清楚地看到 $ \lim_{x\to0}\sin\frac{1}{x} $。如前所述，函数 $ \begin{cases}\sin\frac{1}{x}, & x\neq0,\\0,& x=0\end{cases} $，放大无穷倍后的样子为：



<div style="text-align: center;"><img src="imgs/img_in_image_box_495_649_713_756.jpg" alt="Image" width="21%" /></div>


导函数的值不会突变，我们可以放心了。

以上我们讨论了函数真实存在的样子，事实上，微积分就是在研究函数微观上的样子，当你懂得了这些，就会逐渐发现它们的威力，并拥有了揭示真实的力量。

<div style="text-align: center;"><img src="imgs/img_in_image_box_75_942_111_983.jpg" alt="Image" width="3%" /></div>


## 定积分

<div style="text-align: center;"><img src="imgs/img_in_image_box_113_1042_144_1070.jpg" alt="Image" width="3%" /></div>


## 1 定义

<div style="text-align: center;"><img src="imgs/img_in_image_box_239_1048_317_1090.jpg" alt="Image" width="7%" /></div>


①分割(分割方法不唯一，只要分成n份即可)；②近似；③求和；④取极限.

<div style="text-align: center;"><img src="imgs/img_in_image_box_820_948_922_1054.jpg" alt="Image" width="9%" /></div>


(1) 定积分的概念.

若函数 $ f(x) $在区间 $ [a,b] $上有界，在 $ (a,b) $上任取 $ n-1 $个分点 $ x_i(i=1,2,3,\cdots,n-1) $，定义 $ x_0=a $和 $ x_n=b $，且 $ a=x_0<x_1<x_2<x_3<\cdots<x_{n-1}<x_n=b $，记 $ \Delta x_k=x_k-x_{k-1},k=1,2,3,\cdots,n $。并任取一点 $ \xi_k\in[x_{k-1},x_k] $，记 $ \lambda=\max_{1\leq k\leq n}\left\{\Delta x_k\right\} $，若当 $ \lambda\to0 $时，极限 $ \lim_{\lambda\to0}\sum_{k=1}^{n}f(\xi_k)\Delta x_k $存在且与分点 $ x_i $及点 $ \xi_k $的取法