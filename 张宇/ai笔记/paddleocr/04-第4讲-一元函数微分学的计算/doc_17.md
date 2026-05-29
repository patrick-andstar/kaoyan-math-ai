在x=0处的n阶导数 $ f^{(n)}(0)(n\geqslant3) $

## 解答

4.1 (C) 解  $ h'(x)=\mathrm{e}^{1+g(x)}\cdot g'(x) $. 因  $ h'(1)=1 $,  $ g'(1)=2 $, 故

 $$ g(1)=\ln\frac{h^{\prime}(1)}{g^{\prime}(1)}-1=\ln\frac{1}{2}-1=-\ln2-1\quad. $$ 

4.2  $ (1+2x)e^{2x} $ 解  $ f(x)=\lim_{t\to0}x(1-2t)^{-\frac{x}{t}}=x\lim_{t\to0}\left[(1-2t)^{-\frac{1}{2t}}\right]^{2x}=xe^{2x} $，因此

 $$ f^{\prime}(x)=(x\mathrm{e}^{2x})^{\prime}=\mathrm{e}^{2x}+x\mathrm{e}^{2x}\bullet2=(1+2x)\mathrm{e}^{2x}. $$ 

4.3  $ -\frac{1}{A^{2}e^{2x}} $ 解 设  $ y = f(x) $，则

 $$ \frac{\mathrm{d}x}{\mathrm{d}y}=\frac{1}{\frac{\mathrm{d}y}{\mathrm{d}x}}=\frac{1}{f^{\prime}(x)}, $$ 

 $$ \begin{aligned}\mathrm{d}^{2}x&=\frac{\mathrm{d}\left(\frac{\mathrm{d}x}{\mathrm{d}y}\right)}{\mathrm{d}y}=\frac{\mathrm{d}\left[\frac{1}{f^{\prime}(x)}\right]}{\mathrm{d}x}\bullet\frac{\mathrm{d}x}{\mathrm{d}y}=-\frac{f^{\prime \prime}(x)}{\left[f^{\prime}(x)\right]^{2}}\bullet\frac{1}{f^{\prime}(x)}\\&=-\frac{f^{\prime \prime}(x)}{\left[f^{\prime}(x)\right]^{3}}=-\frac{A\mathrm{e}^{x}}{\left(A\mathrm{e}^{x}\right)^{3}}=-\frac{1}{A^{2}\mathrm{e}^{2x}}\quad.\end{aligned} $$ 

 $$ -\frac{(1+2t)(1+t^{2})}{2t} $$ 

 $$ \begin{aligned}\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}&=\frac{\frac{\mathrm{d}x}{\mathrm{d}t}\bullet\frac{\mathrm{d}^{2}y}{\mathrm{d}t^{2}}-\frac{\mathrm{d}^{2}x}{\mathrm{d}t^{2}}\bullet\frac{\mathrm{d}y}{\mathrm{d}t}}{\left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^{3}}\\&=\frac{\frac{2t}{1+t^{2}}\bullet\left[-\frac{4t}{(1+t^{2})^{2}}-2\right]-\frac{2-2t^{2}}{(1+t^{2})^{2}}\bullet\left[\frac{2}{1+t^{2}}-2(t+1)\right]}{\frac{8t^{3}}{(1+t^{2})^{3}}}\\&=-\frac{(1+2t)(1+t^{2})}{2t},\end{aligned} $$ 

或

 $$ \frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\frac{\mathrm{d}y}{\mathrm{d}t}}{\frac{\mathrm{d}x}{\mathrm{d}t}}=\frac{\frac{2}{1+t^{2}}-2(t+1)}{\frac{2t}{1+t^{2}}}=-(t^{2}+t+1), $$ 

 $$ \frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}=\frac{\mathrm{d}}{\mathrm{d}t}\left[-(t^{2}+t+1)\right]\bullet\frac{\mathrm{d}t}{\mathrm{d}x}=\frac{\frac{\mathrm{d}}{\mathrm{d}t}\left[-(t^{2}+t+1)\right]}{\frac{\mathrm{d}x}{\mathrm{d}t}}=-\frac{(1+2t)(1+t^{2})}{2t}. $$ 