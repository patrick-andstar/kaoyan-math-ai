(C)拐点是 $ (0,0) $

(D) 在 $ (0,0) $处既非极值点也非拐点

♡分析 ①对于 $ f(x^{2}-t^{2}) $，令 $ x^{2}-t^{2}=u\Rightarrow f(u) $;

②换元后对x求导，利用极值充分判别法.

## 解 应选(A)

令 $ x^{2}-t^{2}=u $，则

 $$ F(x)=\frac{1}{2}\int_{0}^{x^{2}}f(u)\mathrm{d}u, $$ 

于是

 $$ F^{\prime}(x)=\frac{1}{2}\bullet2xf(x^{2})=xf(x^{2}), $$ 

 $$ F^{\prime \prime}(x)=f(x^{2})+2x^{2}f^{\prime}(x^{2})\enspace. $$ 

因为 $ f(x)<-2xf'(x) $，所以 $ f(x^{2})+2x^{2}f'(x^{2})<0 $，即 $ F''(x)<0 $，另外， $ F(0)=F'(0)=0 $，故由判别极值的第二充分条件， $ F(x) $在x=0处取极大值，选(A).

## 2 重要结论

(1)  $  f(x)  $ 为可积的奇函数  $ \Rightarrow \left\{ \begin{aligned} \int_{0}^{x} f(t) dt \text{为偶函数}, \\ \int_{a}^{x} f(t) dt \text{为偶函数} (a \neq 0) \end{aligned} \right. $.

注 (1) 若  $ f(x) $ 为连续的奇函数，则  $ \int_{a}^{x} f(t) dt + C $ 也是偶函数，故  $ f(x) $ 的全体原函数均为偶函数。

(2) 只需要被积函数可积，即可有变限积分的相关性质，只有被积函数连续时，才能谈原函数的相关性质，以下同。

(2)  $  f(x)  $ 为可积的偶函数  $ \Rightarrow \left\{ \begin{aligned} & \int_{0}^{x} f(t) dt \text{为奇函数}, \\ & \int_{a}^{x} f(t) dt (a \neq 0) \end{aligned} \right. $

若  $ \int_{a}^{x} f(t) dt = \int_{0}^{x} f(t) dt $，为奇函数，

 $  f'(x)  $ 奇

注 若  $ f(x) $ 为连续的偶函数，则  $ f(x) $ 的全体原函数中，只有  $ \int_{0}^{x} f(t) dt $ 是奇函数.

(3)  $ f(x) $ 是可积的且以  $ T $ 为周期的周期函数，则  $ \int_0^x f(t) \, dt $ 是以  $ T $ 为周期的周期函数  $ \Leftrightarrow \int_0^T f(x) \, dx = 0 $。 $ \rightarrow f'(x) $ 也  $ \therefore T $ 为周期

注  $ \int_{a}^{x}f(t)dt=\int_{a}^{0}f(t)dt+\int_{0}^{x}f(t)dt $ 亦是以 T 为周期的周期函数  $ (a\neq0) $. 常数 周期函数