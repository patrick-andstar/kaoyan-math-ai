## 2 用常数变量化证明不等式

如果欲证的不等式中都是 $ \underline{\text{常数}} $，则可以将其中一个或者几个常数变量化，再利用上面所述的导数工具去证明. 常数不可直接求导

## 3 用中值定理证明不等式

主要用拉格朗日中值定理或者泰勒公式.

利用中值定理： $ \frac{\ln b-\ln a}{b-a}=\frac{1}{\xi} $，其中

例6.21 设 0 < a < b，证明不等式

 $ 0 < a < \xi < b $，即  $ 0 < \frac{1}{b} < \frac{1}{\xi} < \frac{1}{a} $

 $$ a^{2}+b^{2}\geqslant2ab\quad\frac{2a}{a^{2}+b^{2}}<\frac{\ln b-\ln a}{b-a}<\frac{1}{\sqrt{ab}} $$ 

证 先证右边的不等式.

设

构造辅助函数  $ \varphi(x)=\ln x-\ln a-\frac{x-a}{\sqrt{ax}}(x>a>0) $，

因为

 $$ \varphi^{\prime}(x)=\frac{1}{x}-\frac{1}{\sqrt{a}}\left(\frac{1}{2\sqrt{x}}+\frac{a}{2x\sqrt{x}}\right)=\frac{2\sqrt{ax}-x-a}{2x\sqrt{ax}}=-\frac{\left(\sqrt{x}-\sqrt{a}\right)^{2}}{2x\sqrt{ax}}<0 $$ 

故当x>a时， $ \varphi(x) $单调减少，又 $ \varphi(a)=0 $，所以当x>a时， $ \varphi(x)<\varphi(a)=0 $，即

 $$ \ln x-\ln a<\frac{x-a}{\sqrt{ax}}, $$ 

特别地，当 $ x=b>a $时，便有

常数变量化

 $$ \ln b-\ln a<\frac{b-a}{\sqrt{ab}}, $$ 

即

 $$ \frac{\ln b-\ln a}{b-a}<\frac{1}{\sqrt{ab}}. $$ 

再证左边的不等式.

设

 $$ f(x)=\ln x(x>a>0), $$ 

由拉格朗日中值定理知，至少存在一点  $ \xi \in (a, b) $，使

 $$ \frac{\ln b-\ln a}{b-a}=(\ln x)^{\prime}\Big|_{x=\xi}=\frac{1}{\xi}. $$ 

由于 $ 0<a<\xi<b $，且 $ a^{2}+b^{2}>2ab $，所以 $ \frac{1}{\xi}>\frac{1}{b}>\frac{2a}{a^{2}+b^{2}} $，从而有

 $$ \frac{\ln b-\ln a}{b-a}=\frac{1}{\xi}>\frac{2a}{a^{2}+b^{2}}. $$ 

综上，不等式 $ \frac{2a}{a^{2}+b^{2}}<\frac{\ln b-\ln a}{b-a}<\frac{1}{\sqrt{ab}} $成立.