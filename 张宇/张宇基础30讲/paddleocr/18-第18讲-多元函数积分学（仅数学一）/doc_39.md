D是单连通区域，且P，Q具有一阶连续偏导数，则以下6个命题等价.

① $ \frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y} $（旋度为零的等式）在D内处处成立；绝大多数的题都用它

②沿 D 内任意分段光滑闭曲线 L 都有  $ \oint_{L} Pdx + Qdy = 0 $；

③ $ \int_{L_{1}}P\mathrm{d}x+Q\mathrm{d}y=\int_{L_{2}}P\mathrm{d}x+Q\mathrm{d}y $（积分与路径无关）；

④ du = Pdx + Qdy (Pdx + Qdy 为某二元函数 u(x, y) 的全微分);

⑤ $ Pdx+Qdy=0 $ 是全微分方程；

⑥ $ (P, Q) $ 是某二元函数 u 的梯度.

③计算.

a. 按折线  $ (x_0, y_0) \to (x, y_0) \to (x, y) $ [见图 18-20(a)] 或按折线  $ (x_0, y_0) \to (x_0, y) \to (x, y) $ [见图 18-20(b)] 计算  $ u $. 计算公式分别为  $ \int_{0}^{(x, y)} du = \int_{(x, y)}^{(x, y)} Pdx + Qdy $.

 $$ \begin{aligned}&0(b)] 计算 u．计算公式分别为 \\ &\begin{aligned}\\ &u(x,\ y)=\int_{x_{0}}^{x}P(x,\ y_{0})\mathrm{d}x+\int_{y_{0}}^{y}Q(x,\ y)\mathrm{d}y\\ &\end{aligned}\quad\begin{aligned}\\ &\int_{x_{0}}^{x,\ y_{0}}\mathrm{d}u=\int_{\left(x_{0},\ y_{0}\right)}^{x,\ y_{0}}P\mathrm{d}x+Q\mathrm{d}y\\ &\Rightarrow u(x,\ y)-u(x_{0},\ y_{0})=\int_{x_{0}}^{x}P(x,\ y_{0})\mathrm{d}x+\int_{y_{0}}^{y}Q(x,\ y)\mathrm{d}y\\ &\Rightarrow u(x,\ y)=\int_{x_{0}}^{x}P(x,\ y_{0})\mathrm{d}x+\int_{y_{0}}^{y}Q(x,\ y)\mathrm{d}y\quad( 其中 1 个原函数 )\\ &\end{aligned}\\ \end{aligned} $$ 

或

 $$ u(x,y)=\int_{x_{0}}^{x}P(x,y)\mathrm{d}x+\int_{y_{0}}^{y}Q(x_{0},y)\mathrm{d}y. $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_375_802_512_936.jpg" alt="Image" width="13%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_541_800_692_942.jpg" alt="Image" width="14%" /></div>


<div style="text-align: center;">图 18-20</div>


这里要求折线的路径应在 $D$ 内。以上公式得出的 $u(x, y)$ 再加任意常数 $C$ 就得到了所有原函数。

b. 按折线或用 $u$（终点） $-u$（起点）计算积分 $\int P \, dx + Q \, dy$。

比如： $ u(1,1)-u(0,0)=\int_{(0,0)}^{(1,1)}P\,dx+Q\,dy $

例18.20 若曲线积分  $ \int_{L}\frac{x\mathrm{d}x-ay\mathrm{d}y}{x^{2}+y^{2}-1} $ 在区域  $ D=\left\{(x,y)\mid x^{2}+y^{2}<1\right\} $ 内与路径无关，则  $ a= $ ___.

分析 D 为单连通区域，且 P，Q 一阶偏导连续，则在 D 内曲线积分与路径无关  $ \Leftrightarrow \frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y} \Rightarrow $ 解出参数 a。

解 应填 -1.

由题设知

 $$ P=\frac{x}{x^{2}+y^{2}-1},Q=\frac{-ay}{x^{2}+y^{2}-1}, $$ 