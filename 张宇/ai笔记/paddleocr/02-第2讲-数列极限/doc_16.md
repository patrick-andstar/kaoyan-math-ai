又  $ F(0)=0,\quad F(1)=1-2\ln2<0,\quad F(+\infty)=\lim_{x\to+\infty}\left[x-2\ln(1+x)\right]=+\infty>0 $

如图 2-2 所示，故  $ F(x) $ 在  $ (0,1) $ 内无零点，在  $ (1,+\infty) $ 上有唯一零点，因此原方程在  $ (0,+\infty) $ 内有唯一实根  $ \xi $。

(2)由(1)得 $ \xi=2\ln(1+\xi) $， $ \xi>0 $．令 $ x_{n+1}=f(x_{n}) $， $ f(x)=2\ln(1+x) $

①验： $ x_{1}>x_{2}>\xi $

<div style="text-align: center;"><img src="imgs/img_in_image_box_721_137_946_369.jpg" alt="Image" width="21%" /></div>


 $$ x_{2}=2\ln(1+x_{1}),\ 2\ln(1+\xi)=\xi, $$ 

<div style="text-align: center;">图 2-2</div>


因为 $ x_{1}-2\ln(1+x_{1})>0 $，故 $ x_{1}>2\ln(1+x_{1})=x_{2}>2\ln(1+\xi)=\xi $。

②设： $ x_{k-1}>x_k>\xi $。

③证： $ x_{k}>x_{k+1}>\xi $

由 $ ^{②} $知，

 $$ x_{k+1}=2\ln(1+x_{k})>2\ln(1+\xi)=\xi, $$ 

 $$ \begin{array}{c} x_{k}=\frac{2\ln(1+x_{k-1})>2\ln(1+x_{k})}{\downarrow}=x_{k+1}, \\ \ln(1+x) 为增函数 \end{array} $$ 

故得证 $ x_{k}>x_{k+1}>\xi $。

综上， $ \{x_{n}\} $ 单调递减有下界，于是

 $$ \lim_{n\to\infty}x_{n}\xlongequal{ 存在 }a. $$ 

在 $ x_{n+1}=2\ln(1+x_{n}) $两边取极限，有 $ a=2\ln(1+a) $

又由(1)知， $ \xi $是 $ x=2\ln(1+x) $在 $ (0,+\infty) $内的唯一实根，故 $ a=\xi $

注 题目解答过程需要背诵。考生可画出如图 2-3 所示的情形，加深理解。

<div style="text-align: center;"><img src="imgs/img_in_chart_box_406_1027_669_1196.jpg" alt="Image" width="25%" /></div>


<div style="text-align: center;">图 2-3</div>


引申：若题目改为  $ x_1 < \xi $，则如图 2-4 所示。