 $ \frac{dy}{dx}=\frac{dy/dt}{dx/dt}=\frac{\psi'(t)}{\varphi'(t)} $

## 注 由参数方程确定的函数的二阶导数。（不要背）

设函数  $ y = y(x) $ 由参数方程  $ \begin{cases} x = \varphi(t), \\ y = \psi(t) \end{cases} $ 确定，其中  $ t $ 是参数，且  $ \varphi(t), \psi(t) $ 均二阶可导， $ \varphi'(t) \neq 0 $，则  $ \rightarrow $ 若  $ \frac{dy}{dx} = w(t) $，则

 $$ \frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}=\frac{\mathrm{d}(\mathrm{d}y/\mathrm{d}x)}{\mathrm{d}x}=\frac{\mathrm{d}\left[w(t)\right]/\mathrm{d}t}{\mathrm{d}x/\mathrm{d}t}=\frac{w^{\prime}(t)}{\varphi^{\prime}(t)} $$ 

 $$ \frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\mathrm{d}y/\mathrm{d}t}{\mathrm{d}x/\mathrm{d}t}=\frac{\psi^{\prime}(t)}{\varphi^{\prime}(t)},\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}=\frac{\mathrm{d}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)}{\mathrm{d}x}=\frac{\mathrm{d}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)/\mathrm{d}t}{\mathrm{d}x/\mathrm{d}t}=\frac{\psi^{\prime \prime}(t)\varphi^{\prime}(t)-\psi^{\prime}(t)\varphi^{\prime \prime}(t)}{\left[\varphi^{\prime}(t)\right]^{3}} $$ 

例 4.9 设  $ y = y(x) $ 由参数方程  $ \begin{cases} x = \sin t, \\ y = t \sin t + \cos t \end{cases} $ 确定，则  $ \left. \frac{d^2 y}{dx^2} \right|_{t=\frac{\pi}{4}} = $ ___.

分析 本题是参数方程求导，将  $ \frac{dy}{dx} $ 转化为  $ \frac{dy/dt}{dx/dt}=t $，二阶导  $ \frac{d^{2}y}{dx^{2}}=\frac{d\left(\frac{dy}{dx}\right)}{dx}=\frac{d\left(\frac{dy}{dx}\right)}{dx}\cdot\frac{dt}{dx} $

解 应填 $ \sqrt{2} $

因为

 $$ \frac{\mathrm{d}y}{\mathrm{d}x}=\frac{\mathrm{d}y/\mathrm{d}t}{\mathrm{d}x/\mathrm{d}t}=t, $$ 

 $$ \frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}=\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)=\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\mathrm{d}y}{\mathrm{d}x}\right)\bullet\frac{\mathrm{d}t}{\mathrm{d}x}=\frac{1}{\cos t} $$ 

所以

 $$ \left.\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}\right|_{t=\frac{\pi}{4}}=\frac{1}{\cos\frac{\pi}{4}}=\sqrt{2} $$ 

∅公式  $ (\sin t)' = \cos t, (\cos t)' = -\sin t $

例4.10 设函数  $ y = y(x) $ 由  $ \begin{cases} x = \arctan t, \\ 2y - ty^2 + e' = 5 \end{cases} $ 所确定，则  $ \frac{dy}{dx} = $ ___.

(2)分析 本题是参数方程的求导，第二个方程  $ 2y - ty^{2} + e^{t} = 5 $ 是 y 关于 t 的隐函数，直接两端对 t 求导得 dy / dt，然后利用参数方程的求导公式  $ \frac{dy}{dx} = \frac{dy}{dx} / dt $.

解 应填 $ \frac{(y^{2}-e^{t})(1+t^{2})}{2(1-ty)} $

 $$ \frac{\mathrm{d}x}{\mathrm{d}t}=\frac{1}{1+t^{2}}, $$ 

由  $ 2\frac{dy}{dt}-y^{2}-2ty\frac{dy}{dt}+e^{t}=0 $ ，得  $ \frac{dy}{dt}=\frac{y^{2}-e^{t}}{2(1-ty)} $ ，因而