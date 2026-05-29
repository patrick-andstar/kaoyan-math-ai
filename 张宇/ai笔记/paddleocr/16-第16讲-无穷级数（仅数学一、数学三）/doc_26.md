收敛点往外扩 $ \left\{\begin{array}{l} \text { 一定可以找到一个确定的点 } R \text { ，使得级数在 } (-R, R) \text { 内绝对收敛，在 } (-\infty, -R) \text { ，发散点往里收 } \\ (R, +\infty) \text { 上发散 } \end{array}\right. $

<div style="text-align: center;"><img src="imgs/img_in_image_box_265_253_793_344.jpg" alt="Image" width="51%" /></div>


在两个端点 R 和 -R 处的敛散性如何呢？阿贝尔没有讲就去世了。

现在明白为什么阿贝尔要 12 块钱了吧，数学家是量化好的，两个端点值两块钱。从此以后，再也没有任何方法告诉我们两个端点的敛散性情况了，只能将这两个端点代入级数中，按数项级数的方法认认真真地判断，而这两个端点是考研数学中必考无疑的，这就是我们追悔莫及的原因。

关于收敛域，我们会遇到两种题：①具体型级数的收敛域；②抽象型问题，已知一个级数的收敛域，去推导另外一个级数的收敛域，这两个级数之间是有关系的，要通过关系转化找到答案。

注 根据阿贝尔定理，已知  $ \sum_{n=0}^{\infty} a_{n}(x-x_{0})^{n} $ 在某点  $ x_{1}(x_{1} \neq x_{0}) $ 的敛散性，确定该幂级数的收敛半径可分为以下三种情况.

(1) 若在  $ x_{1} $ 处收敛，则收敛半径  $ R \geqslant |x_{1} - x_{0}| $。假设  $ R < |x_{1} - x_{0}| $，则由阿贝尔定理， $ x_{1} $ 处发散，从而  $ R \geqslant |x_{1} - x_{0}| $

(2) 若在  $ x_{1} $ 处发散，则收敛半径  $ R \leqslant |x_{1} - x_{0}| $

假设  $ R > |x_1 - x_0| $，则由阿贝尔定理， $ x_1 $ 处绝对收敛，矛盾，从而  $ R \leq |x_1 - x_0| $，能取到等号。

(3) 若在  $ x_{1} $ 处条件收敛，则  $ R = |x_{1} - x_{0}| $ 。【重要考点】

例如，对于抽象型问题，若级数  $ \sum_{n=0}^{\infty}a_{n}(x-2)^{n} $ 在 x=4 处条件收敛，则 R=2

<div style="text-align: center;"><img src="imgs/img_in_image_box_354_961_732_1001.jpg" alt="Image" width="36%" /></div>


## 4 收敛域的求法

先看具体型幂级数收敛域的问题．①找 $ R\Rightarrow $中心点在原点时，确定 $ (-R,R) $，若中心点不在原点，平移即可；

(1)对于不缺项幂级数 $ \sum_{n=0}^{\infty}a_{n}x^{n} $.

 $ \sum_{n=0}^{\infty}a_{2n}x^{2n} $只有偶次幂，就是缺项级数

①收敛半径的求法.

若  $ \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\rho $ 或  $ \lim_{n\to\infty}\sqrt[n]{|a_n|}=\rho $，则  $ \sum_{n=0}^{\infty}a_nx^n $ 的收敛半径 R 的表达式为  $ R=\begin{cases}\dfrac{1}{\rho},&\rho\neq0,\rho\neq+\infty,\\+\infty,&\rho=0,\\0,&\rho=+\infty.\end{cases} $

②收敛区间与收敛域.