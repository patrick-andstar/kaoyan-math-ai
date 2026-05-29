注 (1) 初等函数的定义域可以是一个区间，也可以是几个区间的并集，甚至可以是一些孤立的点。例如， $ y = \sqrt{\cos \pi x - 1} $ 的定义域是  $ \{x \mid x = 0, \pm 2, \pm 4, \cdots\} $。

★ (2) 幂指函数  $ u(x)^{\nu(x)} = e^{\nu(x)\ln u(x)} $ 也是初等函数，如 x > 0 时， $ f(x) = x^x = e^{x\ln x} $ 是初等函数，其图形如图 1-17 所示。具体作图过程见例 5.12。

<div style="text-align: center;"><img src="imgs/img_in_image_box_811_131_931_258.jpg" alt="Image" width="11%" /></div>


等到学完工具后再画图，如 $ x^{2} $， $ x^{2x} $， $ x^{3x} $的图像都类似。

<div style="text-align: center;">图 1-17</div>


## 2 分段函数  $ \rightarrow $ 有别于初等函数的另一种重要的函数

在自变量的不同变化范围中，对应法则用不同式子来表示的函数称为分段函数。需要强调一句，分段函数是用几个式子来表示的一个（不是几个）函数。一般来说，它不是初等函数。分段函数的典型形式如下：

 $$ f(x)=\begin{cases}\varphi_{1}(x),&x>x_{0},\\a,&x=x_{0},\\ \varphi_{2}(x),&x<x_{0}\end{cases} 或 f(x)=\begin{cases}\varphi(x),&x\neq x_{0},\\a,&x=x_{0}.\end{cases} $$ 

分段函数很重要，原因在于其形式的复杂性所带来的命题的丰富性。后面会看到，不论是求极限、求导数，还是求积分，出现最多的研究对象之一便是分段函数。

 $$ 分段函数是非常重要的一个命题素材。\angle $$ 

下面列出三个重要的分段函数.

① $ y=|x|=\begin{cases}x,&x\geqslant0,\\-x,&x<0\end{cases} $称为绝对值函数，如图1-18(a)所示.

|x|既然是分段函数，那它是不是初等函数呢？是，因为 $ |x|=\sqrt{x^2} $，一般来讲，分段函数不是初等函数，但 $ |x| $是一个特例。

② $ y=\mathrm{sgn}x=\begin{cases}1,&x>0,\\0,&x=0,\\-1,&x<0\end{cases} $，称为符号函数，如图1-18(b)所示。对于任意实数x，有 $ x=|x| $

<div style="text-align: center;"><img src="imgs/img_in_image_box_301_975_503_1120.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_534_978_736_1122.jpg" alt="Image" width="19%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 1-18</div>


③ $ y=[x] $称为取整函数.先给出定义:设x为任一实数,不超过x的最大整数称为x的整数部分,记作 $ [x] $.如

 $$ \left[0.99\right]=0,\left[\pi\right]=3,\left[-1\right]=-1,\left[-1.99\right]=-2. $$ 

因此，取整函数  $ y = [x] $ 的定义域为  $ \mathbb{R} $，值域为  $ \mathbb{Z} $。它的图形如图 1-19 所示，在  $ x $ 为整数值处图形发生跳跃。