<div style="text-align: center;"><img src="imgs/img_in_image_box_72_127_140_198.jpg" alt="Image" width="6%" /></div>


## 基础内容精讲

## 向量代数

<div style="text-align: center;"><img src="imgs/img_in_image_box_820_245_923_352.jpg" alt="Image" width="9%" /></div>


## 向量及其表达形式

既有大小又有方向的量称为向量.

注 两个向量，只要它们的大小相等、方向相同，它们就是相等的向量，与它们在空间中的位置无关（这也称为向量的自由性）.

向量的表达形式为

 $$ \boxed{a}=(a_{x},a_{y},a_{z})=a_{x}i+a_{y}j+a_{z}k $$ 

高等数学中手写要打箭头：a

## 2 向量的运算及其应用

线性代数中不需要， $ a=\begin{bmatrix}1\\ 1\\ 2\end{bmatrix} $

设  $ \boldsymbol{a} = (a_{x}, a_{y}, a_{z}) $,  $ \boldsymbol{b} = (b_{x}, b_{y}, b_{z}) $,  $ \boldsymbol{c} = (c_{x}, c_{y}, c_{z}) $,  $ \boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c} $ 均是非零向量.

(1) 数量积（内积、点积）及其应用.

结果是数

①  $ a \cdot b = (a_x, a_y, a_z) \cdot (b_x, b_y, b_z) = a_x b_x + a_y b_y + a_z b_z $.

② $ a\cdot b=|a||b|\cos\theta $，则 $ \cos\theta=\frac{a\cdot b}{|a||b|}=\frac{a_{x}b_{x}+a_{y}b_{y}+a_{z}b_{z}}{\sqrt{a_{x}^{2}+a_{y}^{2}+a_{z}^{2}}\cdot\sqrt{b_{x}^{2}+b_{y}^{2}+b_{z}^{2}}} $，其中 $ \theta $为a，b的夹角.

③  $ a \perp b \Leftrightarrow \theta = \frac{\pi}{2} \Leftrightarrow a \cdot b = |a||b| \cos \theta = 0 \Leftrightarrow a_x b_x + a_y b_y + a_z b_z = 0 $ 。垂直方程最常用

例：若 $ (1,2,1) $与 $ (a,1,-1) $垂直，则 $ a+2-1=0 $，即a=-1

 $$ =|\boldsymbol{a}|\cos\theta $$ 

④  $ \underline{\text{Prij\_a}} = \frac{a \cdot b}{|b|} = \frac{a_x b_x + a_y b_y + a_z b_z}{\sqrt{b_x^2 + b_y^2 + b_z^2}} $，称为 a 在 b 上的投影。

(2) 向量积（外积、叉积）及其应用。

①  $ a \times b = \begin{vmatrix} i & j & k \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix} $，其中  $ |a \times b| = |a||b|\sin\theta $，用右手规则确定方向（转向角不超过  $ \pi $）， $ \theta $ 为 a, b





<div style="text-align: center;"><img src="imgs/img_in_image_box_556_1117_715_1181.jpg" alt="Image" width="15%" /></div>


的夹角.

②  $ a \parallel b \Leftrightarrow \theta = 0 $ 或  $ \pi \Leftrightarrow \frac{a_x}{b_x} = \frac{a_y}{b_y} = \frac{a_z}{b_z} $.

<div style="text-align: center;"><img src="imgs/img_in_image_box_519_1255_822_1374.jpg" alt="Image" width="29%" /></div>


(3) 混合积及其应用.