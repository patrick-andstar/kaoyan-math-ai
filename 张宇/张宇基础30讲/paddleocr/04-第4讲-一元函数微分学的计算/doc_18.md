4.5  $ (n-1)!\mathrm{e}^{n} $ 解 对  $ f'(x)=\mathrm{e}^{f(x)} $ 两边关于 x 求导，得

 $$ f^{\prime \prime}(x)=\mathrm{e}^{f(x)}\bullet f^{\prime}(x)=\mathrm{e}^{2f(x)}, $$ 

两边再对x求导，得

 $$ f^{m}(x)=\mathrm{e}^{2f(x)}\bullet2f^{\prime}(x)=2!\mathrm{e}^{3f(x)}, $$ 

两边再对x求导，得

 $$ f^{(4)}(x)=2\mathrm{e}^{3f(x)}\bullet3f^{\prime}(x)=3!\mathrm{e}^{4f(x)}, $$ 

由以上导数规律可得

 $$ f^{(n)}(x)=(n-1)!\mathbf{e}^{n f(x)}, $$ 

所以 $ f^{(n)}(2)=(n-1)!\mathrm{e}^{n} $

4.6 解 在方程中令 x=0 可得  $ 0=\ln\frac{e}{y(0)}+1 $ ，故  $ y(0)=e^{2} $ 。将方程两边对 x 求导，得

 $$ \cos(xy)(y+xy^{\prime})=\frac{1}{x+e}-\frac{y^{\prime}}{y} $$ 

将x=0， $ y(0)=\mathrm{e}^{2} $代入，有 $ e^{2}=\frac{1}{\mathrm{e}}-\frac{y^{\prime}(0)}{\mathrm{e}^{2}} $，即 $ y^{\prime}(0)=\mathrm{e}-\mathrm{e}^{4} $

### 4.7 证明 根据导数定义，有

 $$ f^{\prime}(0)=\lim_{x\to0}\frac{\frac{g(x)}{x}-0}{x-0}=\lim_{x\to0}\frac{g(x)}{x^{2}}=\lim_{x\to0}\frac{g^{\prime}(x)}{2x}=\frac{1}{2}\lim_{x\to0}\frac{g^{\prime}(x)-g^{\prime}(0)}{x-0}=\frac{1}{2}g^{\prime\prime}(0) $$ 

当 $ x\neq0 $时， $ f'(x)=\frac{xg'(x)-g(x)}{x^{2}} $，则

 $$ \begin{aligned}\lim_{x\to0}f^{\prime}(x)&=\lim_{x\to0}\frac{xg^{\prime}(x)-g(x)}{x^{2}}=\lim_{x\to0}\frac{g^{\prime}(x)}{x}-\lim_{x\to0}\frac{g(x)}{x^{2}}\\&=g^{\prime \prime}(0)-\frac{1}{2}g^{\prime \prime}(0)=\frac{1}{2}g^{\prime \prime}(0)=f^{\prime}(0),\end{aligned} $$ 

所以 $ f(x) $的导函数在x=0处连续.

4.8 解 方法一 由莱布尼茨公式

 $$ (u v)^{(n)}=u^{(n)}v+C_{n}^{1}u^{(n-1)}v^{\prime}+C_{n}^{2}u^{(n-2)}v^{\prime \prime}+\cdots+u v^{(n)}, $$ 

及

 $$ \left[\ln(1+x)\right]^{(k)}=\frac{(-1)^{k-1}(k-1)!}{(1+x)^{k}}\quad(k 为正整数 ), $$ 

得当 $ n \geqslant 3 $时，

 $$ f^{(n)}(x)=x^{2}\frac{(-1)^{n-1}(n-1)!}{(1+x)^{n}}+2nx\frac{(-1)^{n-2}(n-2)!}{(1+x)^{n-1}}+n(n-1)\cdot\frac{(-1)^{n-3}(n-3)!}{(1+x)^{n-2}}, $$ 

所以