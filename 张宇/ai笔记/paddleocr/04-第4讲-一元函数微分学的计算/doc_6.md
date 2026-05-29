解 y 的表达式含有绝对值符号，可知其为分段函数，x=0 为其分段点，则

 $$ y=\left|x\mathbf{e}^{-x}\right|=\begin{cases}-x\mathbf{e}^{-x},&x<0,\\x\mathbf{e}^{-x},&x\geqslant0,\end{cases} $$ 

所以

→非分段点处用导数公式求导

 $$ y^{\prime}=\begin{cases}\mathrm{e}^{-x}(x-1),&x<0,\\\mathrm{e}^{-x}(1-x),&x>0.\end{cases} $$ 

而

 $$ \frac{y_{-}^{\prime}(0)=\lim_{x\to0^{-}}\frac{y(x)-y(0)}{x}=\lim_{x\to0^{-}}\frac{-x\mathrm{e}^{-x}}{x}=-1} $$ 

分段点处用导数定义求导

 $$ \underline{y^{\prime}}_{+}(0)=\lim_{x\to0^{+}}\frac{y(x)-y(0)}{x}=\lim_{x\to0^{+}}\frac{x\mathrm{e}^{-x}}{x}=1 $$ 

可知y在x=0处不可导.所以

 $$ \begin{aligned}\downarrow\\  因为 y_{-}^{\prime}(0)\neq y_{+}^{\prime}(0)\end{aligned} $$ 

 $$ y^{\prime \prime}=\begin{cases}\mathrm{e}^{-x}(2-x),&x<0,\\\mathrm{e}^{-x}(x-2),&x>0.\end{cases} $$ 

## 5 反函数的导数

设 $ y = f(x) $为单调、可导函数，且 $ f'(x) \neq 0 $，则存在反函数 $ x = \varphi(y) $，且 $ \frac{dx}{dy} = \frac{1}{\frac{dy}{dx}} $，即 $ \varphi'(y) = \frac{1}{f'(x)} $。

注 (1) 设  $ y = \arcsin x $, -1 < x < 1.

由  $ y = \arcsin x $，得反函数  $ x = \sin y $， $ y \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right) $。根据反函数求导公式，得

 $$ \left(\arcsin x\right)^{\prime}=\frac{1}{\left(\sin y\right)^{\prime}}=\frac{1}{\cos y}=\frac{1}{\sqrt{1-\sin^{2}y}}=\frac{1}{\sqrt{1-x^{2}}}\left(-1<x<1\right). $$ 

(2) 反函数的二阶导数.  $ \rightarrow $ 重要

在  $ y = f(x) $ 单调，且二阶可导的情况下，若  $ f'(x) \neq 0 $，则存在反函数  $ x = \varphi(y) $，记  $ f'(x) = y_x' $， $ \varphi'(y) = x_y' $，则有

 $$ y_{x}^{\prime}=\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{1}{\frac{\mathrm{d}x}{\mathrm{d}y}}=\frac{1}{x_{y}^{\prime}}, $$ 

 $$ y_{xx}^{\prime \prime}=\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}=\frac{\mathrm{d}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)}{\mathrm{d}x}=\frac{\mathrm{d}\left(\frac{1}{x_{y}^{\prime}}\right)}{\mathrm{d}x}=\frac{\mathrm{d}\left(\frac{1}{x_{y}^{\prime}}\right)}{\mathrm{d}y}\cdot\frac{1}{\left[x_{y}^{\prime}\right]^{2}}=-\frac{1}{\left(x_{y}^{\prime}\right)^{2}}\cdot\left(x_{y}^{\prime}\right)_{y}^{\prime}\cdot\frac{1}{x_{y}^{\prime}}=-\frac{x_{yy}^{\prime\prime}}{\left(x_{y}^{\prime}\right)^{2}}\cdot\frac{1}{x_{y}^{\prime}}=-\frac{x_{yy}^{\prime\prime}}{\left(x_{y}^{\prime}\right)^{2}}. $$ 

反过来，则有

 $$ x_{y}^{\prime}=\frac{1}{y_{x}^{\prime}},x_{yy}^{\prime\prime}=-\frac{y_{xx}^{\prime\prime}}{\left(y_{x}^{\prime}\right)^{3}}. $$ 