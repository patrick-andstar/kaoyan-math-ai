移到 1，即将收敛区间平移到  $ (-1, 3) $，得  $ \sum_{n=1}^{\infty} a_{n}(x-1)^{n} $，收敛半径不变；

根据 “三、4.(2) 注 3(1)，(2) 和 (3)”，对  $ \sum_{n=1}^{\infty}a_{n}(x-1)^{n} $ 逐项求导，得  $ \sum_{n=1}^{\infty}na_{n}(x-1)^{n-1} $，再乘以  $ (x-1) $ 得  $ \sum_{n=1}^{\infty}na_{n}(x-1)^{n} $，收敛半径不变．

故  $ \sum_{n=1}^{\infty}na_{n}(x-1)^{n} $ 的收敛区间为  $ (-1,3) $，因为 x=2 在收敛区间内部，所以在该点处级数绝对收敛，故选择 (A).

例 16.27 幂级数  $ \sum_{n=2}^{\infty}\left(\frac{1}{n\ln n}+\frac{1}{2^{n}}\right)x^{n} $ 的收敛域为 ___.

分析 思路  $ \left\{\begin{array}{l}\text { ①能拆开则拆开； } \\ \text { ②不能拆开找子列。 }\end{array}\right. $

解 应填  $ [-1, 1) $.

对于 $ \sum_{n=2}^{\infty}\frac{1}{n\ln n}x^{n},\frac{1}{R_{1}}=\lim_{n\to\infty}\frac{n\ln n}{(n+1)\ln(n+1)}=1 $

当x=1时， $ \sum_{n=2}^{\infty}\frac{1}{n\ln n} $发散；当x=-1时，由莱布尼茨判别法， $ \sum_{n=2}^{\infty}\frac{(-1)^{n}}{n\ln n} $收敛，所以其收敛域为 $ [-1,1) $.

对于 $ \sum_{n=2}^{\infty}\frac{1}{2^{n}}x^{n} $， $ R_{2}=\lim_{n\to\infty}\frac{\frac{1}{2^{n}}}{\frac{1}{2^{n+1}}}=2 $

当x=2时， $ \sum_{n=2}^{\infty}1 $发散；当x=-2时， $ \sum_{n=2}^{\infty}\frac{1}{2^{n}}\cdot(-2)^{n}=\sum_{n=2}^{\infty}(-1)^{n} $发散，所以其收敛域为 $ (-2,2) $.

综上所述，原级数的收敛域为 $ [-1,1) $.

四 幂级数求和函数（解答题/客观题）

<div style="text-align: center;"><img src="imgs/img_in_image_box_840_1050_943_1157.jpg" alt="Image" width="9%" /></div>


## 概念

在收敛域上，记  $ S(x)=\sum_{n=1}^{\infty}u_{n}(x) $，并称  $ S(x) $ 为  $ \sum_{n=1}^{\infty}u_{n}(x) $ 的和函数.

如 $ \left|x\right|<1 $时， $ \sum_{n=1}^{\infty}x^{n}=\frac{x}{1-x}=S(x) $.

①（前提）求收敛域：②求和函数