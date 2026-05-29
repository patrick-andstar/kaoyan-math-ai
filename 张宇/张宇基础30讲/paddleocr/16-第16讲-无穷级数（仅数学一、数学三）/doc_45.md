总结： $ S(x) $ 收敛于点的  $ \frac{\text{左极限} + \text{右极限}}{2} $.

## 3 正弦级数和余弦级数

①当 $ f(x) $为奇函数时，其展开式是正弦级数

 $$ f(x)\sim\sum_{n=1}^{\infty}b_{n}\sin\frac{n\pi x}{l},b_{n}=\frac{2}{l}\int_{0}^{l}f(x)\sin\frac{n\pi x}{l}\mathrm{d}x,n=1,2,\cdots. $$ 

②当 $ f(x) $为偶函数时，其展开式是余弦级数

 $$ f(x)\sim\frac{a_{0}}{2}+\sum_{n=1}^{\infty}a_{n}\cos\frac{n\pi x}{l}, $$ 

 $$ a_{0}=\frac{2}{l}\int_{0}^{l}f(x)\mathrm{d}x,\ a_{n}=\frac{2}{l}\int_{0}^{l}f(x)\cos\frac{n\pi x}{l}\mathrm{d}x,\ n=1,\ 2,\cdots. $$ 

## 4 只在  $ [0, \eta] $ 上有定义的函数的正弦级数和余弦级数展开

若 $ f(x) $是定义在 $ [0,l] $上的函数，首先用周期延拓，使其扩展为定义在 $ (-\infty,+\infty) $上的周期函数 $ F(x) $。在得到 $ F(x) $的傅里叶展开式后，再将其自变量限制在 $ [0,l] $上，就得到 $ f(x) $在 $ [0,l] $上的傅里叶级数展开式。《全国硕士研究生招生考试数学考试大纲》中只要求周期奇延拓和周期偶延拓。

(1) 周期奇延拓与正弦级数展开.

①周期奇延拓.

 $$ F(x)=\begin{cases}f(x),&0<x\leq l,\\-f(-x),&-l\leq x<0,\\0,&x=0,\end{cases} $$ 

设 $ f(x) $定义在 $ [0,l] $上，令

<div style="text-align: center;"><img src="imgs/img_in_image_box_699_854_938_972.jpg" alt="Image" width="23%" /></div>


再令  $ F(x) $ 为以 2l 为周期的周期函数.

②正弦级数展开.

 $$ f(x)\sim\sum_{n=1}^{\infty}b_{n}\sin\frac{n\pi}{l}x,\;x\in[0,\;l], $$ 

 $$ b_{_{n}}=\frac{2}{l}\int_{0}^{l}f(x)\sin\frac{n\pi}{l}x\mathrm{d}x(n=1,2,3,\cdots). $$ 

(2) 周期偶延拓与余弦级数展开.

①周期偶延拓.

设 $ f(x) $定义在 $ [0,l] $上，令

<div style="text-align: center;"><img src="imgs/img_in_image_box_586_1183_939_1281.jpg" alt="Image" width="34%" /></div>


周期偶延拓

 $$ F(x)=\begin{cases}f(x),&0\leq x\leq l,\\f(-x),&-l\leq x<0,\end{cases} $$ 

再令  $ F(x) $ 为以 2l 为周期的周期函数.