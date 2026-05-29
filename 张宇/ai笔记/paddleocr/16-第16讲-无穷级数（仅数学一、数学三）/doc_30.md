 $$ \lim_{n\to\infty}\left|\frac{b_{n+1}}{b_{n}}\right|=\lim_{n\to\infty}\frac{n+1}{n+2}=1, $$ 

所以收敛半径  $ \tilde{R}=1 $ 。当 x=1 时，级数  $ \sum_{n=0}^{\infty}\frac{1}{n+1} $ 发散；当 x=-1 时，级数  $ \sum_{n=0}^{\infty}\frac{1}{n+1}(-1)^{n+1} $ 收敛，故收敛域为  $ [-1,1) $ 。

综上，选(B).

例 16.25 已知  $ \sum_{n=1}^{\infty}\frac{n!}{n^n}e^{-nx} $ 的收敛域为  $ (a, +\infty) $，则  $ a = $ ___.

解 应填 -1 .

因为

 $$ \lim_{n\to\infty}\left|\frac{(n+1)!}{(n+1)^{n+1}}\mathrm{e}^{-(n+1)x}\bullet\frac{n^{n}}{n!}\mathrm{e}^{nx}\right|=\lim_{n\to\infty}\left|\left(\frac{n}{n+1}\right)^{n}\mathrm{e}^{-x}\right|=\mathrm{e}^{-x-1}, $$ 

所以当  $ e^{-x-1} < 1 $，即 x > -1 时，级数收敛，当  $ e^{-x-1} > 1 $，即 x < -1 时级数发散，所以 a = -1。

注 (1) 当  $ x = -1 $ 时， $ \frac{u_{n+1}}{u_n} = \frac{e}{\left(1 + \frac{1}{n}\right)^n} $，分母单调增加，且  $ \left(1 + \frac{1}{n}\right)^n \to e(n \to \infty) $，故  $ \left(1 + \frac{1}{n}\right)^n < e $，故  $ \frac{u_{n+1}}{u_n} > 1 $，且  $ u_n > 0 $，故  $ \lim_{n \to \infty} u_n \neq 0 $，即当  $ x = -1 $ 时级数发散。

 $ u_{n} $ 单调增加，且是正项级数，所以一定发散

→包含非幂级数，如指数级数、对数级数

<div style="text-align: center;"><img src="imgs/img_in_image_box_695_816_917_893.jpg" alt="Image" width="21%" /></div>


(2)对于一般函数项级数的收敛域，可以不是对称区间，也没有“收敛半径”这一概念.

例 16.26 设  $ \sum_{n=1}^{\infty}a_{n}(x+1)^{n} $ 在点 x=1 处条件收敛，则幂级数  $ \sum_{n=1}^{\infty}na_{n}(x-1)^{n} $ 在点 x=2 处（）.

(A) 绝对收敛 (B) 条件收敛 (C) 发散 (D) 敛散性不确定

♡分析 思路： $ a_{n}(x+1)^{n}\xrightarrow{\text{平移}}a_{n}(x-1)^{n}\xrightarrow{\text{求导}}na_{n}(x-1)^{n-1}\xrightarrow{\text{乘}(x-1)}na_{n}(x-1)^{n} $

解 应选(A).

根据 “三、3. 注 (3)”，由  $ \sum_{n=1}^{\infty}a_{n}(x+1)^{n} $ 在点 x=1 处条件收敛，知

 $$ R=\left|x_{1}-x_{0}\right|=\left|1-(-1)\right|=2, $$ 

且收敛区间为 $ (-3,1) $;

根据 “三、4.(2) 注 3(1) 和 (3)”，将  $ (x+1)^n $  $ \xrightarrow{(x+1)^n} $  $ \xrightarrow{(-3)} $  $ \xrightarrow{(-1)} $ 平移  $ \xrightarrow{1} $

转化为 $ (x-1)^n $，也就是把级数的中心点由-1转 $ \xrightarrow{(x-1)^n} $  $ \xrightarrow{(-1)} $  $ \xrightarrow{1} $  $ \xrightarrow{3} $