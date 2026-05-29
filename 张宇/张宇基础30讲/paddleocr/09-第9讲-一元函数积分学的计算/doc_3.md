③由于  $ \frac{dx}{\sqrt{x}} = 2\mathrm{d}(\sqrt{x}) $，故  $ \int\frac{f(\sqrt{x})}{\sqrt{x}}\mathrm{d}x = 2\int f(\sqrt{x})\mathrm{d}(\sqrt{x}) = 2\int f(u)\mathrm{d}u $。

④由于 $ \frac{dx}{x^2}=d\left(-\frac{1}{x}\right) $，故 $ \int\frac{f\left(-\frac{1}{x}\right)}{x^2}dx=\int f\left(-\frac{1}{x}\right)d\left(-\frac{1}{x}\right)=\int f(u)du $。

⑤由于当x>0时， $ \frac{1}{x}dx=d(\ln x) $，故 $ \int\frac{f(\ln x)}{x}dx=\int f(\ln x)d(\ln x)=\int f(u)du $。

⑥由于  $ \mathbf{e}^x \mathrm{d}x = \mathrm{d}(\mathrm{e}^x) $，故  $ \int \mathrm{e}^x f(\mathrm{e}^x) \mathrm{d}x = \int f(\mathrm{e}^x) \mathrm{d}(\mathrm{e}^x) = \int f(u) \mathrm{d}u $。

⑦由于  $ a^{x} \, \mathrm{d}x = \frac{1}{\ln a} \, \mathrm{d}(a^{x}) $,  $ a > 0 $,  $ a \neq 1 $，故  $ \int a^{x} f(a^{x}) \, \mathrm{d}x = \frac{1}{\ln a} \int f(a^{x}) \, \mathrm{d}(a^{x}) = \frac{1}{\ln a} \int f(u) \, \mathrm{d}u $.

⑧由于  $ \sin x \, dx = d(-\cos x) $，故  $ \int \sin x \cdot f(-\cos x) \, dx = \int f(-\cos x) \, d(-\cos x) = \int f(u) \, du $

⑨由于  $ \cos x \, dx = d(\sin x) $，故  $ \int \cos x \cdot f(\sin x) \, dx = \int f(\sin x) \, d(\sin x) = \int f(u) \, du $

⑩ 由于  $ \frac{dx}{\cos^{2}x} = \sec^{2}x dx = \mathrm{d}(\tan x) $，故  $ \int \frac{f(\tan x)}{\cos^{2}x} dx = \int f(\tan x) \mathrm{d}(\tan x) = \int f(u) \mathrm{d}u $

⑪由于  $ \frac{dx}{\sin^2 x} = \csc^2 x dx = d(-\cot x) $，故  $ \int \frac{f(-\cot x)}{\sin^2 x} dx = \int f(-\cot x) d(-\cot x) = \int f(u) du $。

⑫由于  $ \frac{1}{1+x^2}dx = d(\arctan x) $，故  $ \int\frac{f(\arctan x)}{1+x^2}dx = \int f(\arctan x)d(\arctan x) = \int f(u)du $。

⑬由于  $ \frac{1}{\sqrt{1-x^{2}}}dx=d(\arcsin x) $，故  $ \int\frac{f(\arcsin x)}{\sqrt{1-x^{2}}}dx=\int f(\arcsin x)d(\arcsin x)=\int f(u)du $

 $ \lim_{x\to0}\int\frac{(\arcsin x)^{2}}{\sqrt{1-x^{2}}}dx=\int(\arcsin x)^{2}d(\arcsin x)\xlongequal{\arcsin x=u}\int u^{2}du=\frac{1}{3}u^{3}+C=\frac{1}{3}\arcsin^{3}x+C $

选择复杂部分求导  $ \frac{(\arcsin x)^{2}}{\sqrt{1-x^{2}}} $

例 9.1 求不定积分  $ \int \frac{\sqrt{x}}{\sqrt{4-x^{3}}} \, dx $.

解

 $$ \int\frac{\sqrt{x}}{\sqrt{4-x^{3}}}\mathrm{d}x=\frac{2}{3}\int\frac{\mathrm{d}(x^{\frac{3}{2}})}{\sqrt{4-(x^{\frac{3}{2}})^{2}}}=\frac{2}{3}\int\frac{\mathrm{d}(x^{\frac{3}{2}})}{2\sqrt{1-\left(\frac{1}{2}x^{\frac{3}{2}}\right)^{2}}} $$ 