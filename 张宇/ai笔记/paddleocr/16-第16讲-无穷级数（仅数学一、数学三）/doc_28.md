为什么要单独讨论两个端点呢？

比值判别法里面，有

 $ \lim_{n\to\infty}\frac{a_{n+1}}{a_n}\begin{cases}<1, 收敛 ,\\=1, 判别法失效 ,\\>1, 发散 .\end{cases} $

极限比出来是1，那有可能大于1，也有可能小于1，故可以找到 $ \frac{3}{2} $，也可以找到 $ \frac{1}{2} $。显然，有 $ \frac{1}{2}<\frac{a_{n+1}}{a_n}<\frac{3}{2}\Rightarrow\frac{1}{2}a_n<a_{n+1}<\frac{3}{2}a_n $。

这种推导，我们就没有办法找到 $ a_{n+1}<ka_n $， $ 0<k<1 $。根据极限的保号性，无法与一个收敛的等比级数作大小比较，所以这个方法失效。

所以阿贝尔定理中没有两个端点，绝不是因为我没有给那两块钱。

注2 上述(1)，(2)的方法只是充分的，即当  $ \sum_{n=0}^{\infty}a_{n}x^{n} $ 的收敛半径存在时，极限  $ \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| $ 或  $ \lim_{n\to\infty}\sqrt[n]{|a_n|} $ 可能不存在.

 $ \Rightarrow $ 分成  $ a_{2k} $ 与  $ a_{2k+1} $ 两种情况讨论

如  $ \sum_{n=1}^{\infty}\frac{\left[3+\left(-1\right)\right]^{n}}{n}x^{n} $，记  $ a_{n}=\frac{\left[3+\left(-1\right)\right]^{n}}{n} $，则  $ \lim_{n\to\infty}\sqrt[n]{|a_n|}=\lim_{n\to\infty}\frac{3+\left(-1\right)^{n}}{\sqrt[n]{n}} $ 不存在， $ \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim_{n\to\infty}\frac{\left[3+\left(-1\right)^{n+1}\right]^{n+1}}{[3+\left(-1\right)^{n}]^{n}} $ 亦不存在，但是此级数的收敛半径是存在的，怎么求呢？见习题 16.12.

抽象型幂级数的收敛域

注3 已知  $ \sum a_{n}(x-x_{1})^{n} $ 的敛散性，讨论  $ \sum b_{n}(x-x_{2})^{m} $ 的敛散性.

 $$  令 x-x_{0}=t $$ 

(1)  $ (x-x_{1})^{n} $ 与  $ (x-x_{2})^{m} $ 的转化一般通过初等变形来完成，包括①“平移”收敛区间；②提出或者乘以因式  $ (x-x_{0})^{k} $ 等.

(2)  $ a_{n} $ 与  $ b_{n} $ 的转化一般通过微积分变形来完成，包括①对级数逐项求导；②对级数逐项积分等.

(3)以下三种情况，级数的收敛半径不变，收敛域要具体问题具体分析.

①对级数提出或者乘以因式 $ (x-x_{0})^{k} $，或者作平移等，收敛半径不变。

②对级数逐项求导，收敛半径不变，收敛域可能缩小.

③对级数逐项积分，收敛半径不变，收敛域可能扩大.

并非“一定”，端点处的

敛散性可能会发生改变



例 16.22 设  $ a_n = \sum_{k=1}^n \frac{1}{k} $，则级数  $ \sum_{n=1}^{\infty} a_n x^n $ 的收敛半径为 ___.

分析  $ \sum_{n=1}^{\infty}\left(1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}\right)x^{n} $，则  $ 1<1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}<1+1+1+\cdots+1=n $，故  $ \sqrt[n]{1}<\sqrt[n]{a_{n}}<\sqrt[n]{n} $

解 应填 1.