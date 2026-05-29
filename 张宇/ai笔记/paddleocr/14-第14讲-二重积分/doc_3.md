设平面闭区域 $ D_{i}(i=1,2,3,4) $分别是由

 $$ L_{1}:\ x^{2}+y^{2}=1,\ L_{2}:\ x^{2}+y^{2}=2, $$ 

 $$ L_{3}:\ x^{2}+2y^{2}=2,\ L_{4}:\ 2x^{2}+y^{2}=2 $$ 

围成的平面区域，记

则  $ \max\{I_{1}, I_{2}, I_{3}, I_{4}\} = (\quad) $.

(A)  $ I_{1} $ (B)  $ I_{2} $ (C)  $ I_{3} $ (D)  $ I_{4} $

(2)分析 此题是同一个函数在不同区域的积分比大小的问题，不需要计算二重积分，应研究在不同积分区域下，被积函数的正负情形。被积函数  $ 1 - x^{2} - \frac{1}{2}y^{2} \geq 0 $ 正好对应的区域为  $ D_{4} $，而  $ D_{1} < D_{4} $，故  $ I_{1} < I_{4} $， $ D_{4} < D_{2} $，在  $ D_{2} - D_{4} $ 区域，被积函数值为负，所以  $ I_{2} < I_{4} $，同理  $ I_{3} < I_{4} $。

解 应选(D).

曲线  $ L_{i}(i=1,2,3,4) $ 如图 14-2 所示. 记被积函数为  $ f(x,y)= $  $ 1-\left(x^{2}+\frac{1}{2}y^{2}\right) $，由于  $ L_{4}:2x^{2}+y^{2}=2 $，则  $ D_{4} $ 内部为  $ x^{2}+\frac{y^{2}}{2}<1 $，于是在  $ D_{4} $ 内部有  $ f(x,y)>0 $，而在  $ D_{4} $ 外部有  $ f(x,y)<0 $.

①比较 $ I_{1} $与 $ I_{4} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_681_665_959_886.jpg" alt="Image" width="26%" /></div>


<div style="text-align: center;">图 14-2</div>


 $$ \begin{aligned}I_{4}=&\iint\limits_{D_{4}}f(x,y)\mathrm{d}x\mathrm{d}y=\iint\limits_{D_{1}}f(x,y)\mathrm{d}x\mathrm{d}y+\iint\limits_{D_{4}-D_{1}}f(x,y)\mathrm{d}x\mathrm{d}y\\=&I_{1}+\iint\limits_{\substack{D_{4}-D_{1}\\}}\ f(x,y)\mathrm{d}x\mathrm{d}y>I_{1}.\\& 与 I_{4}.\end{aligned} $$ 

②比较 $ I_{2} $与 $ I_{4} $

 $$ \begin{aligned}I_{2}=&\iint\limits_{D_{2}}f(x,y)\mathrm{d}x\mathrm{d}y=\iint\limits_{D_{4}}f(x,y)\mathrm{d}x\mathrm{d}y+\iint\limits_{D_{2}-D_{4}}f(x,y)\mathrm{d}x\mathrm{d}y\\=&I_{4}+\iint\limits_{\underbrace{D_{2}-D_{4}}_{}}f(x,y)\mathrm{d}x\mathrm{d}y<I_{4}.\end{aligned} $$ 

③比较 $ I_{3} $与 $ I_{4} $.如图14-3所示，将 $ D_{3} $， $ D_{4} $中互不重合的部分分别记为 $ D_{31} $， $ D_{32} $， $ D_{41} $， $ D_{42} $，则

 $$ I_{3}=\iint\limits_{\overbrace{D_{31}\atop}\rightarrow}f(x,\ y)\mathrm{d}x\mathrm{d}y+\iint\limits_{\overbrace{D_{32}\atop}\rightarrow}f(x,\ y)\mathrm{d}x\mathrm{d}y+\iint\limits_{D_{3}\cap D_{4}}f(x,\ y)\mathrm{d}x\mathrm{d}y $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_732_1170_958_1384.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">图 14-3</div>
