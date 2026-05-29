②速度对时间的变化率（加速度）；

③牛顿第二定律 $ (F=ma) $

力 质量 加速度

已知质点运动的位移 s 关于时间 t 的函数为  $ s = s(t) $，称它为质点的运动方程（位移方程），则其速度为

 $$ \nu(t)=\lim_{\Delta t\to0}\frac{\Delta s}{\Delta t}=s^{\prime}(t),\quad\Rightarrow\nu(t)=\frac{\mathrm{d}s}{\mathrm{d}t} $$ 

其加速度为

 $$ a(t)=\frac{\mathrm{d}v}{\mathrm{d}t}=\frac{\mathrm{d}v}{\mathrm{d}s}\bullet\frac{\mathrm{d}s}{\mathrm{d}t}\left(\mathrm{ 或 }a(t)=\frac{\mathrm{d}\left(\frac{\mathrm{d}s}{\mathrm{d}t}\right)}{\mathrm{d}t}=\frac{\mathrm{d}^{2}s}{\mathrm{d}t^{2}}\right)\stackrel{\sim}{a}(t)=\lim_{\Delta t\rightarrow0}\frac{\Delta v}{\Delta t}=v^{\prime}(t)=s^{\prime \prime}(t)\;. $$ 

 $ \frac{dv}{ds} \cdot v $（更利于解决含s，v不涉及t的相关微分方程问题，第15讲再学习）

这就是导数的物理意义。

## 2 相关变化率

研究 $ \frac{\mathrm{d}A}{\mathrm{d}B}=\frac{\mathrm{d}A}{\mathrm{d}C}\cdot\frac{\mathrm{d}C}{\mathrm{d}B} $

①若已知 $ \frac{dA}{dB} $， $ \frac{dC}{dB} $，则 $ \frac{dA}{dC}=\frac{\frac{dA}{dB}}{\frac{dC}{dB}} $（通过已知求未知）；

②该等式建立了  $ \frac{dA}{dB} $ 与  $ \frac{dC}{dB} $ 的关系，A，B，C 可以扩展为很多实际的量，比如某冰块质量（m）对温度（c）随时间（t）的变化率

 $$ \frac{\mathrm{d}m}{\mathrm{d}t}=\frac{\mathrm{d}m}{\mathrm{d}c}\bullet\frac{\mathrm{d}c}{\mathrm{d}t}\Longrightarrow\frac{\mathrm{d}m}{\mathrm{d}c}=\frac{\frac{\mathrm{d}m}{\mathrm{d}t}}{\frac{\mathrm{d}c}{\mathrm{d}t}}\ . $$ 

微分学中经济应用较多，积分学中物理应用较多.

 $ f'(x) $ 已知，若告知  $ \frac{dx}{dt} $，则  $ \frac{dy}{dt} $ 便可求.

若函数  $ y = f(x) $ 由参数方程  $ \left\{\begin{aligned} x &= x(t), \\ y &= y(t) \end{aligned}\right. $ 确定且可导，则  $ \frac{dy}{dt} = \frac{dy}{dx} \cdot \frac{dx}{dt} = f'(x) \frac{dx}{dt} $，上式中， $ \frac{dy}{dt} $ 与  $ \frac{dx}{dt} $ 由  $ f'(x) $ 联系在一起，这种相互关联的变化率称为相关变化率。

注 单独出题不难，常见的是速度、位移、加速度与相关变化率的综合题，难度在于和微分方程相结合.