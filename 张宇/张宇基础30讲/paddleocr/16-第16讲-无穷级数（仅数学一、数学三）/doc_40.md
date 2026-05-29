由华里士公式，知 $ b_{n+2}=\frac{n+1}{n+2}b_{n} $，故 $ a_{n}=b_{n}-\frac{n+1}{n+2}b_{n}=\frac{1}{n+2}b_{n} $。于是

 $$ \sum_{n=1}^{\infty}(-1)^{n}\frac{a_{n}}{b_{n}}=\sum_{n=1}^{\infty}(-1)^{n}\bullet\frac{1}{n+2}. $$ 

当 $ |x|<1 $时，令 $ S(x)=\sum_{n=1}^{\infty}(-1)^{n}\frac{x^{n+2}}{n+2} $，则

 $$ \begin{aligned}S^{\prime}(x)&=\sum_{n=1}^{\infty}(-1)^{n}\bullet x^{n+1}=x\sum_{n=1}^{\infty}(-x)^{n}\\&=x\bullet\frac{-x}{1+x}=-\frac{x^{2}}{1+x}.\end{aligned} $$ 

于是

有理函数的积分

 $$ \begin{aligned}S(x)&=S(0)+\int_{0}^{x}\underline{\left(-\frac{t^{2}}{1+t}\right)}\mathrm{d}t=\int_{0}^{x}\frac{1-t^{2}-1}{1+t}\mathrm{d}t\\&=\int_{0}^{x}(1-t)\mathrm{d}t-\int_{0}^{x}\frac{1}{1+t}\mathrm{d}t\\&=x-\frac{x^{2}}{2}-\ln(1+x)\enspace.\\ \end{aligned} $$ 

当x=1时，根据莱布尼茨判别法，知 $ \sum_{n=1}^{\infty}(-1)^{n}\cdot\frac{1}{n+2} $收敛，故

 $$ \sum_{n=1}^{\infty}(-1)^{n}\frac{a_{n}}{b_{n}}=\lim_{x\to1^{-}}S(x)=\frac{1}{2}-\ln2\quad. $$ 

☑ 方法总结 ①看到  $ \int\sqrt{1-x^{2}}dx $ 考虑三角换元；

②见到 $ \int_{0}^{\frac{\pi}{2}}\sin^{n}t dt $，用华里士公式分析积分与积分之间的关系，即确定 $ a_{n} $与 $ b_{n} $的关系，得 $ \frac{a_{n}}{b_{n}} $的关系式.

公式  $ \int_{0}^{\frac{\pi}{2}}\sin^{n}t\mathrm{d}t=\frac{n-1}{n}\int_{0}^{\frac{\pi}{2}}\sin^{n-2}t\mathrm{d}t $

## 五 函数展开成幂级数

 $$ \sum_{n=0}^{n}x^{n}=\frac{1}{1-x},\ -1<x<1 $$ 

从左到右是求和函数  

从右到左是展开

<div style="text-align: center;"><img src="imgs/img_in_image_box_847_1056_951_1162.jpg" alt="Image" width="10%" /></div>


## 概念

如果函数 $ f(x) $在点 $ x=x_{0} $处存在任意阶导数，则称

 $$ f(x_{0})+f^{\prime}(x_{0})(x-x_{0})+\frac{f^{\prime \prime}(x_{0})}{2!}(x-x_{0})^{2}+\cdots+\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n}+\cdots $$ 