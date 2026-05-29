(3)  $ f(x) $ 在  $ x_{0} $ 处可导  $ \neq $  $ |f(x)| $ 在  $ x_{0} $ 处可导 .

比如， $ f(x) $ 在  $ x_0 $ 点处的微观性态图如图 3-8（a）所示（放大足够多倍），其在  $ x_0 $ 处可导，则  $ \left|f(x)\right| $ 如图 3-8（b）所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_274_298_452_440.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_579_310_746_441.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">图 3-8</div>


<div style="text-align: center;">(b)</div>


如果说连续， $ f(x) $ 在  $ x_0 $ 处连续  $ \Rightarrow |f(x)| $ 在  $ x_0 $ 处连续，是的，点与点就是相依相偎在一起的，正如 (2) 所述。但说可导，不仅要相依相偎，而且要  $ \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} $ 存在（唯一的数），也就是  $ f(x) $ 相似相偎到  $ f(x_0) $ 的速度要不比  $ x \to x_0 $ 的速度慢。（①若快，则  $ \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = 0 $ ；②若同阶，则  $ \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = A \neq 0 $。）

请看图 3-8(a) 和图 3-8(b)，对于  $ \left|f(x)\right| $， $ \lim_{x\to x_0}\frac{\left|f(x)\right|-\left|f(x_0)\right|}{x-x_0}<0 $（ $ \downarrow $，而  $ \lim_{x\to x_0}\frac{\left|f(x)\right|-\left|f(x_0)\right|}{x-x_0}>0 $）

( )，故  $ \lim_{x\to x_0}\frac{\left|f(x)\right|-\left|f(x_0)\right|}{x-x_0} $ 不存在， $ \left|f(x)\right| $ 在  $ x_0 $ 处不可导，即若  $ f(x) $ 在  $ x_0 $ 处可导， $ f(x_0)=0 $， $ f'(x_0)\neq0 $，则  $ \left|f(x)\right| $ 在  $ x_0 $ 处必不可导。反例同 (2).

现在，试试看，你应该可以清楚回答了：若 $ f(x) $在 $ x_0 $处可导，且 $ f(x_0) \neq 0 $，则 $ |f(x)| $在 $ x_0 $处必可导，如图3-9(a)，图3-9(b)所示。

<div style="text-align: center;"><img src="imgs/img_in_image_box_268_1073_435_1203.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">(a)</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_562_1074_727_1203.jpg" alt="Image" width="15%" /></div>


<div style="text-align: center;">(b)</div>


<div style="text-align: center;">图 3-9</div>


提示: 对于连续或可导函数, 只要  $ f(x_0) \geq 0 $, 无论  $ f(x_0) $ 与 0 的距离有多小, 它旁边相依相偎的  $ f(x) $ 一定  $ \geq 0 $, 考研中常用这一点.