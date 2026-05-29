注 事实上，设 $ f(x) $是 $ [a,b] $上非负的连续函数，只要 $ f(x) $不恒等于零，则必有

 $$ \int_{a}^{b}f(x)\mathrm{d}x>0\quad. $$ 

在有些积分不等式的证明与定积分值的估计中，要求获得严格的不等式结果，便需要用到这个结论，其证明见例 8.7.

极限戴帽法： $ f(x) > 0 $，则 $ \lim_{x \to x_0} f(x) \geq 0 $

极限脱帽法： $ \lim_{x\to0}f(x)>0 $，则 $ f(x)>0 $

积分： $ f(x)-g(x)\leq0 $， $ a<b $，则 $ \int_{a}^{b}[f(x)-g(x)]\,dx\leq0 $

若有条件 $ f(x)-g(x) $连续，且不恒为0，则 $ \int_{a}^{b}[f(x)-g(x)]\,dx<0 $。

性质 5(估值定理) 设 M, m 分别是  $ f(x) $ 在  $ [a, b] $ 上的最大值和最小值，L 为区间  $ [a, b] $ 的长度，则有

 $$ mL\leqslant\int_{a}^{b}f(x)\mathrm{d}x\leqslant ML\quad. $$ 

注 证  $ \int_{a}^{b} m dx \leqslant \int_{a}^{b} f(x) dx \leqslant \int_{a}^{b} M dx $，有  $ mL \leqslant \int_{a}^{b} f(x) dx \leqslant ML $。 $ \rightarrow m \leqslant f(x) \leqslant M $

★★★性质 6(中值定理) 设  $ f(x) $ 在区间  $ [a, b] $ 上连续，则在  $ [a, b] $ 上至少存在一点  $ \xi $，使得

 $$ \int_{a}^{b}f(x)\mathrm{d}x=f(\xi)(b-a)\enspace. $$ 

### 例 8.3 在区间  $ [-1, 2] $ 上，以下四个结论：

① $ f(x)=\begin{cases}2,&x>0,\\1,&x=0,\\-1,&x<0\end{cases} $有原函数，但其定积分不存在；→

② $ f(x)=\begin{cases}2x\sin\frac{1}{x^{2}}-\frac{2}{x}\cos\frac{1}{x^{2}},&x\neq0,\\0,&x=0\end{cases} $有原函数，其定积分也存在；

③ $ f(x)=\begin{cases}\frac{1}{x},&x\neq0,\\0,&x=0\end{cases} $没有原函数，其定积分也不存在；





<div style="text-align: center;"><img src="imgs/img_in_image_box_603_931_760_1061.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_642_1132_787_1259.jpg" alt="Image" width="14%" /></div>


④ $ f(x)=\left\{\begin{aligned}&2x\cos\frac{1}{x}+\sin\frac{1}{x},&x\neq0,\\ &0,&x=0.\end{aligned}\right. $，有原函数，其定积分也存在.

x=0 是无穷间断点

正确结论的个数为（）.

(A)1          (B)2          (C)3          (D)4