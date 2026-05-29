例 7.1 已知动点 P 在曲线  $ y = x^3 $ 上运动，记坐标原点与点 P 间的距离为 l。若点 P 的横坐标对时间的变化率为常数  $ v_0 $，则当点 P 运动到点  $ (1, 1) $ 时，l 对时间的变化率是 ___。

解 应填  $ 2\sqrt{2}v_{0} $

由题设知  $ l=\sqrt{x^{2}+y^{2}}=\sqrt{x^{2}+x^{6}} $，则

 $$ \frac{\mathrm{d}l}{\mathrm{d}t}=\frac{\mathrm{d}l}{\mathrm{d}x}\bullet\frac{\mathrm{d}x}{\mathrm{d}t}=\frac{2x+6x^{5}}{2\sqrt{x^{2}+x^{6}}}\bullet v_{0}, $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_713_250_839_349.jpg" alt="Image" width="12%" /></div>


 $$ \left.\frac{\mathrm{d}l}{\mathrm{d}t}\right|_{x=1}=\frac{8}{2\sqrt{2}}\nu_{0}=2\sqrt{2}\nu_{0}. $$ 

☑ 方法总结 涉及相关变化率问题：①建立相关变量方程；②求导找出相关变化率，进而通过已知变化率求未知变化率.

注 更为综合的物理应用会涉及微分方程，将在第 15 讲学习.

<div style="text-align: center;"><img src="imgs/img_in_image_box_95_680_128_716.jpg" alt="Image" width="3%" /></div>


## 复利与连续复利（仅数学三）

<div style="text-align: center;"><img src="imgs/img_in_image_box_842_652_945_759.jpg" alt="Image" width="9%" /></div>


复利计算公式为

 $$ A_{m}=A(1+r)^{m},\stackrel{A(1+r)(1+r)\cdots(1+r)}{\overbrace{m 个 }} $$ 

其中 A 表示一开始的本金，r 表示每一期的利率，m 表示复利的总期数， $ A_{m} $ 表示 m 期后的余额。

①如果年利率为r的利息一年支付1次，那么当初始存款为A元时，t年后余额 $ A_{t} $则为

 $$ A_{t}=A(1+r)^{t}. $$ 

②如果年利率为r的利息一年支付n次，那么当初始存款为A元时，t年后余额 $ A_{t} $则为

 $$ A_{i}=A\left(1+\frac{r}{n}\right)^{n}\overset{n}{\longrightarrow}A\overbrace{\left(1+\frac{r}{n}\right)\cdots\left(1+\frac{r}{n}\right)\left[\left(1+\frac{r}{n}\right)\cdots\left(1+\frac{r}{n}\right)\right]\cdots\left[\left(1+\frac{r}{n}\right)\cdots\left(1+\frac{r}{n}\right)\right]}^{n\uparrow}\cdots\overbrace{\left(1+\frac{r}{n}\right)\cdots\left(1+\frac{r}{n}\right)\left[\left(1+\frac{r}{n}\right)\cdots\left(1+\frac{r}{n}\right)\right]}^{n\uparrow} $$ 

 $$ A\mathbf{e}^{n}=R\Rightarrow A\xrightarrow{}\mathbf{R}\mathbf{e}^{-n} $$ 

③对于②，当 $ \underline{n\rightarrow\infty} $时， $ \lim_{n\rightarrow\infty}A_t=\lim_{n\rightarrow\infty}A\left(1+\frac{r}{n}\right)^{nt}=Ae^{rt} $，这称为连续复利→掌握至此即可，无须深入学习支付无数次

注 考试时要弄清楚①，②，③三种情况，题目会明确告知.

例 7.2 设某酒厂有一批新酿的好酒，如果现在（假定 t=0）就售出，总收入为  $ R_{0} $ 元；如果窖藏起来，待来日按陈酒价格出售，t 年末总收入为  $ R = R_{0} e^{\frac{2}{5} \sqrt{t}} $ 。假定银行的年利率 r 为 6%，并以连续复