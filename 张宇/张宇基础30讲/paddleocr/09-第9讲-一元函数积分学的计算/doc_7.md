(2) 分部积分法的推广公式与  $ \int P_{n}(x)e^{kx}dx $， $ \int P_{n}(x)\sin axdx $， $ \int P_{n}(x)\cos bxdx $。

设函数  $ u = u(x) $ 与  $ v = v(x) $ 具有直到第  $ n+1 $ 阶的连续导数，并根据分部积分公式

 $$ \int u\mathrm{d}\nu=u\nu-\int\nu\mathrm{d}u, $$ 

则有

 $$ \int u v^{(n+1)}\mathrm{d}x=u v^{(n)}-u^{\prime}v^{(n-1)}+u^{\prime \prime}v^{(n-2)}-\cdots+(-1)^{n}u^{(n)}v+(-1)^{n+1}\int u^{(n+1)}v\mathrm{d}x $$ 

注 证明 n=3 时，如下：

 $$ \int u v^{(4)}\mathrm{d}x=u v^{(3)}-u^{\prime}v^{\prime \prime}+u^{\prime \prime}v^{\prime}-u^{(3)}v+\int u^{(4)}v\mathrm{d}x\ . $$ 

证

 $$ \int u\nu^{(4)}\mathrm{d}x=\int u\mathrm{d}[\nu^{(3)}]=u\nu^{(3)}-\int u^{\prime}\nu^{(3)}\mathrm{d}x\;, $$ 

 $$ \int u^{\prime}v^{(3)}\mathrm{d}x=\int u^{\prime}\mathrm{d}(v^{\prime \prime})=u^{\prime}v^{\prime \prime}-\int u^{\prime \prime}v^{\prime \prime}\mathrm{d}x~, $$ 

 $$ \int u^{\prime \prime}v^{\prime \prime}\mathrm{d}x=\int u^{\prime \prime}\mathrm{d}(v^{\prime})=u^{\prime \prime}v^{\prime}-\int u^{(3)}v^{\prime}\mathrm{d}x~, $$ 

 $$ \int u^{(3)}\nu^{\prime}\mathrm{d}x=\int u^{(3)}\mathrm{d}\nu=u^{(3)}\nu-\int u^{(4)}\nu\mathrm{d}x\quad. $$ 

联立以上式子，得

 $$ \int u v^{(4)}\mathrm{d}x=u v^{(3)}-u^{\prime}v^{\prime \prime}+u^{\prime \prime}v^{\prime}-u^{(3)}v+\int u^{(4)}v\mathrm{d}x\quad. $$ 

事实上，可写成如下表格：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>u的各阶导数</td><td style='text-align: center; word-wrap: break-word;'>u</td><td style='text-align: center; word-wrap: break-word;'>u&#x27;</td><td style='text-align: center; word-wrap: break-word;'>u&#x27;&#x27;</td><td style='text-align: center; word-wrap: break-word;'>u^{(3)}</td><td style='text-align: center; word-wrap: break-word;'>u^{(4)}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v^{(4)} 的各阶原函数</td><td style='text-align: center; word-wrap: break-word;'>v^{(4)}</td><td style='text-align: center; word-wrap: break-word;'>v^{(3)}</td><td style='text-align: center; word-wrap: break-word;'>v&#x27;&#x27;</td><td style='text-align: center; word-wrap: break-word;'>v&#x27;</td><td style='text-align: center; word-wrap: break-word;'>v</td></tr></table>

计算方法：以u作起点左上、右下错位相乘，各项符号“+”“-”相间，最后一项为 $ \int u^{(4)}vdx $比如，求不定积分 $ \int(x^{3}+2x+6)e^{2x}dx $，则


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>u</td><td style='text-align: center; word-wrap: break-word;'>$ x^{3}+2x+6 $</td><td style='text-align: center; word-wrap: break-word;'>$ 3x^{2}+2 $</td><td style='text-align: center; word-wrap: break-word;'>6x</td><td style='text-align: center; word-wrap: break-word;'>6</td><td style='text-align: center; word-wrap: break-word;'>0</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>v(4)</td><td style='text-align: center; word-wrap: break-word;'>e^{2x}</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{2}e^{2x} $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{4}e^{2x} $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{8}e^{2x} $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{16}e^{2x} $</td></tr></table>

利用上述表格，可得

 $$ \begin{aligned} 原式 &=(x^{3}+2x+6)\left(\frac{1}{2}\mathrm{e}^{2x}\right)-(3x^{2}+2)\left(\frac{1}{4}\mathrm{e}^{2x}\right)+6x\left(\frac{1}{8}\mathrm{e}^{2x}\right)-6\left(\frac{1}{16}\mathrm{e}^{2x}\right)+\int0\bullet\left(\frac{1}{16}\mathrm{e}^{2x}\right)\mathrm{d}x\\&=\left(\frac{1}{2}x^{3}-\frac{3}{4}x^{2}+\frac{7}{4}x+\frac{17}{8}\right)\mathrm{e}^{2x}+C\ .\end{aligned} $$ 