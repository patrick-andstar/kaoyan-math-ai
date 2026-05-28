## 四 计算

在学习了极限的定义和性质，尤其是了解了超实数的理论后，我们对于极限的计算方法有了一个完整、全面和深刻的认识。更为重要的是，今后在计算极限时，就不会再犯错误，什么位置该替换，什么位置不能替换，就能从一个新的角度，更加全面地去分析。

## 1 方法

(1) 极限四则运算规则.

若  $ \lim f(x)=A,\ \lim g(x)=B $ ，那么

①  $ \lim[kf(x)\pm lg(x)]=k\lim f(x)\pm l\lim g(x)=kA\pm lB $，其中k，l为常数.

②  $ \lim[f(x)\cdot g(x)]=\lim f(x)\cdot\lim g(x)=A\cdot B $ 。特别地，若  $ \lim f(x) $ 存在，n 为正整数，则

 $$ \lim\left[f(x)\right]^{n}=\lim_{n\to\infty}\underbrace{f(x)\cdots\cdots\cdots\cdots f(x)}_{n 个 }=\left[\lim f(x)\right]^{n}. $$ 

③  $ \lim_{x\to0}\frac{f(x)}{g(x)}=\frac{\lim_{x\to0}f(x)}{\lim_{x\to0}g(x)}=\frac{A}{B}(B\neq0) $

上面定理可以用一句话概括：当 $ f(x) $与 $ g(x) $极限都存在时，函数的加减乘除的极限分别等于极限的加减乘除（除要求分母的极限不为零）.

★例1.20 证明：(1) 若  $ \lim_{x\to0}\frac{f(x)}{g(x)}=A $，且  $ \lim_{x\to0}g(x)=0 $，则  $ \lim_{x\to0}f(x)=0 $；

(2) 若  $ \lim_{x\to0}\frac{f(x)}{g(x)}=A\neq0 $ ，且  $ \lim_{x\to0}f(x)=0 $ ，则  $ \lim_{x\to0}g(x)=0 $ .

☐ 分析 恒等变形.

证 (1) 由于  $ f(x)=\frac{f(x)}{g(x)}\cdot g(x) $，则

 $$ \lim f(x)=\lim\frac{f(x)}{g(x)}\cdot g(x)\xlongequal{ 四则运算法则 }\lim\frac{f(x)}{g(x)}\cdot\lim g(x)=A\cdot0=0 $$ 

(2) 由于  $  g(x) = \frac{f(x)}{g(x)}  $，则  $ \lim_{x \to 0} g(x) = \lim_{x \to 0} \frac{f(x)}{\frac{f(x)}{g(x)}} = \lim_{x \to 0} \frac{f(x)}{\lim_{x \to 0} \frac{f(x)}{g(x)}} = \frac{0}{A} = 0 $.

注 以上结论非常重要，以后在有关定参数的题目中可直接使用，如下例.

例1.21 设  $ \lim_{x\to0}\frac{\sin x}{e^x-a}(\cos x-b)=5 $，则  $ b= $（ ）.

(A) -4 (B) -3 (C) -2 (D) -1