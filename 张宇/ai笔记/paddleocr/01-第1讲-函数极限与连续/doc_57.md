方法一 脱帽法.

 $$ \lim_{x\to0}\frac{\tan2x+xf(x)}{\sin x^{3}}\xrightarrow{=}0\ , $$ 

则 $ \frac{\tan 2x + xf(x)}{x^{3}} = \alpha(x) $，其中 $ \alpha(x) $为 $ x \to 0 $时的无穷小。因此

 $$ f(x)=\frac{x^{3}\cdot\alpha(x)-\tan2x}{x} $$ 

 $$ \lim_{x\to0}\frac{2+f(x)}{x^{2}}=\lim_{x\to0}\frac{2+\frac{x^{3}\cdot\alpha(x)-\tan2x}{x}}{x^{2}} $$ 

故

 $$ \begin{aligned}&\xlongequal{ 通分 }\lim_{x\to0}\frac{2x-\tan2x+x^{3}\alpha(x)}{x^{3}}\\ &=\lim_{x\to0}\frac{2x-\left[2x+\frac{1}{3}(2x)^{3}+o(x^{3})\right]+x^{3}\alpha(x)}{x^{3}}\xrightarrow{0}=-\frac{8}{3}.\\ \end{aligned} $$ 

方法二 泰勒展开.

由  $ \lim_{x\to0}\frac{\tan2x+xf(x)}{\sin x^{3}}=0 $ ，得

 $$ \lim_{x\to0}\frac{2x+\frac{1}{3}(2x)^{3}+o(x^{3})+xf(x)}{x^{3}}=0, $$ 

故

 $$ \lim_{x\to0}\frac{2+f(x)}{x^{2}}=-\frac{8}{3} $$ 

☐ 方法总结 ①用好泰勒公式.

②已知极限，用脱帽法可解出 $ f(x) $

公式 当狗→0时，狗−tan狗~− $ \frac{1}{3} $狗 $ ^{3} $.

脱帽法：若  $ \lim_{x\to0}f(x)=A $，则  $ f(x)=\boxed{A}+\alpha(x)\left(\lim_{x\to0}\alpha(x)=0\right) $。

例 1.28 求极限  $ \lim_{x \to 1^-} \ln x \ln (1 - x) $.  $ 0 \cdot \infty $ 型

 $ \lim_{x\to0^{+}}x\ln x $

 $$ \text{“}0\bullet\infty\text{”} $$ 

\[\begin{aligned}\textcircled{7}\begin{aligned}\lim_{x\rightarrow0^{+}}\frac{x}{\frac{1}{\ln x}}\end{aligned}\quad\text{}\quad\

 $$ 0\bullet\infty\underbrace{\stackrel{0}{\underset{\infty}{\frac{1}{\infty}}}}_{\substack{\frac{1}{0}}}=\frac{\infty}{\infty} $$ 

把谁放在分母，是有讲究的。设置分母有原则，简单因式才下放。

简单因式有 $ x^{\alpha} $， $ e^{\beta x} $， $ \sin r x $等.

 $$ \begin{aligned}&\begin{aligned}\\ &\overset{ 洛必达法则 }{=}\lim_{x\rightarrow0^{+}}\frac{1}{-\frac{1}{\ln^{2}x}\cdot\frac{1}{x}}\\&=-\lim_{x\rightarrow0^{+}}x\ln^{2}x\\&\overset{ \textcircled{2} }{=}\lim_{x\rightarrow0^{+}}\frac{\ln x}{\frac{1}{x}}\\&\overset{ 洛必达法则 }{=}\lim_{x\rightarrow0^{+}}\frac{\frac{1}{x}}{-\frac{1}{x^{2}}}=-\lim_{x\rightarrow0^{+}}x=0\\ &\end{aligned}\\ \end{aligned} $$ 

复杂因式有  $ \arctan x $， $ \arcsin x $， $ \ln x $ 等。