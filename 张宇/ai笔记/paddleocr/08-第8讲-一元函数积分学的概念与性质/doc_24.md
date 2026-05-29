使 $ f(x) $在 $ x_{0} $的邻域内无界的点即为瑕点。

如  $ \lim_{x\to0}\frac{1}{x}=\infty,\quad x=0 $ 为瑕点；

(2) 无界函数的反常积分的概念与敛散性.

再如  $ \lim_{x\to0}\frac{1}{x}\sin\frac{1}{x}= $ 无界振荡，x=0 为瑕点.

定义 2 设  $ F(x) $ 是  $ f(x) $ 在相应区间上的一个原函数， $ x_{0} $ 为  $ f(x) $

①若 x=a 是唯一瑕点，则



 $$ \int_{a}^{b}f(x)\mathrm{d}x=F(b)-\lim_{x\to a^{+}}F(x) $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_669_318_827_439.jpg" alt="Image" width="15%" /></div>


若上述极限存在，则称反常积分收敛，否则称发散。

②若x=b是唯一瑕点，则

 $$ \int_{a}^{b}f(x)\mathrm{d}x=\lim_{x\to b^{-}}F(x)-F(a) $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_378_446_825_571.jpg" alt="Image" width="43%" /></div>


若上述极限存在，则称反常积分收敛，否则称发散。

③若 $ x=c\in(a,b) $是唯一瑕点，则

<div style="text-align: center;"><img src="imgs/img_in_image_box_357_573_903_748.jpg" alt="Image" width="52%" /></div>


只要等号右边有一个发散，左边即发散，不存在“发散+发散=收敛”的情形，如 $ \int_{-\infty}^{+\infty}x^3dx=\int_{-\infty}^{0}x^3dx+\int_0^{+\infty}x^3dx $，由于 $ \int_{-\infty}^{0}x^3dx=-\infty $，发散，故 $ \int_{-\infty}^{+\infty}x^3dx $发散，而不是 $ \int_{-\infty}^{+\infty}x^3dx=0 $， $ \int_{-\infty}^{+\infty}x^3dx\neq\lim_{R\to+\infty}\int_{-R}^{R}x^3dx $，只有当反常积分收敛时， $ \int_{-\infty}^{+\infty}f(x)dx=\lim_{R\to+\infty}\int_{-R}^{R}f(x)dx $才成立。

若右端两个积分都收敛，则称反常积分收敛，否则称发散。

注1 在反常积分中，一般把“∞”和瑕点统称为奇点．→判别前提

在判别积分敛散性时， $ \underline{\text{一个积分中只能有一个奇点，若出现两个及以上奇点，需拆分。}} $

注2 请看 (2) 的①，当 x = a 为  $ f(x) $ 的瑕点时， $ f(x) $ 便是一个无界函数了，积分  $ \int_{a}^{b} f(x) \, dx $ 也可能存在。细心的考生可能会联想到，前面我们不是说 “ $ \int_{a}^{b} f(x) \, dx $ 存在的必要条件是  $ f(x) $ 有界” 吗？这不是矛盾了吗？事实上，前面所说的  $ \int_{a}^{b} f(x) \, dx $ 是定积分（黎曼积分），而这里的  $ \int_{a}^{b} f(x) \, dx $ 是反常积分，它们并不是一个概念，所以没有任何矛盾。只是当考生读完这一段，最好今后在提到积分存在时，特别强调一下，是定积分存在（黎曼可积，常义可积），还是反常积分存在（广义可积）。