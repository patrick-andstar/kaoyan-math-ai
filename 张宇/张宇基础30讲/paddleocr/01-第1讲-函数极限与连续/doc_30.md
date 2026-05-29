在实数轴上任取一点 $ x_{0} $，称为核.

 $ x_{0}+x^{*} $ 是以  $ x_{0} $ 为核的有限超实数，称为核  $ x_{0} $ 的光环，由于  $ x^{*} $ 是任意一个非零无穷小，故  $ x_{0} $ 的光环有无穷多个.

为方便，记  $ X^* = x_0 + x^* = \text{std}(X^*) + [X^* - \text{std}(X^*)] $， $ x_0 = \text{std}(X^*) $ 也称为超实数  $ X^* $ 的标准实数部分， $ x^* = X^* - \text{std}(X^*) $ 即为非零无穷小量。

如  $ x_0 = 0 $， $ x_1^* = \sin x(x \to 0) $，则  $ X_1^* = x_0 + x_1^* = \sin x(x \to 0) $ 是

以 0 为核，以  $ \sin x $ 为无穷小量的超实数。



<div style="text-align: center;"><img src="imgs/img_in_image_box_658_346_954_426.jpg" alt="Image" width="28%" /></div>


如 $ x_{0}=0 $， $ x_{2}^{*}=2x(x\rightarrow0) $，则 $ X_{2}^{*}=x_{0}+x_{2}^{*}=2x(x\rightarrow0) $是以0为核，以2x为无穷小量的超实数.

如  $ x_{0}=0,\quad x_{3}^{*}=\frac{1}{x}(x\rightarrow0) $，则  $ X_{3}^{*}=x_{0}+x_{3}^{*}=\frac{1}{x}(x\rightarrow0) $ 是以 0 为核，以  $ \frac{1}{x} $ 为无穷大量的超实数.

如  $ x_{0}=0,\quad x_{4}^{*}=\frac{1}{x^{2}}(x\rightarrow0) $，则  $ X_{4}^{*}=x_{0}+x_{4}^{*}=\frac{1}{x^{2}}(x\rightarrow0) $ 是以 0 为核，以  $ \frac{1}{x^{2}} $ 为无穷大量的超实数.

显然，上述 4 个超实数到它们的核的距离  $ |\sin x| $， $ |2x| $， $ \left|\frac{1}{x}\right| $， $ \left|\frac{1}{x^2}\right| $ ( $ x \to 0 $) 均不是实数， $ |\sin x| $， $ |2x| $ ( $ x \to 0 $) 是比任何正实数都小的量， $ \left|\frac{1}{x}\right| $， $ \left|\frac{1}{x^2}\right| $ ( $ x \to 0 $) 是比任何正实数都大的量。

(3) 超实数与极限的关系与运算.

先举个例子.如

 $$ \lim_{x\to0}\frac{\sin x}{x}=1, $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_736_834_953_907.jpg" alt="Image" width="21%" /></div>


其中，① $ \frac{\sin x}{x} $ 在未作极限运算时，为 $ \underline{\text{实数运算}} $.

② $ \lim_{x\to0}\frac{\sin x}{x} $称为 $ \underline{\text{趋核运算}} $，此时的 $ \frac{\sin x}{x} $称为 $ \underline{\text{超实数}} $， $ \lim_{x\to0}\frac{\sin x}{x} $的结果为 $ \underline{\text{其核值1}} $。于是★设 $ \lim_{x\to x_0}f(x)=A $，其运算（及其运算顺序）为

a.  $ f(x) $ 为实数运算.

b.  $ \lim_{x\to x_0}f(x) $ 为趋核运算，A 为核值，当 A 唯一时，称趋核运算存在， $ \lim_{x\to x_0}f(x) $ 存在；否则称趋核运算不存在， $ \lim_{x\to x_0}f(x) $ 不存在.

如  $ \lim_{x\to0}\frac{(x-x)}{x}=\lim_{x\to0}0=0 $

实数运算  $ \frac{x-0}{x} $ 趋核运算 = 核值 0

再如， $ \lim_{x\to0}(x-\sin x)\stackrel{\circ}{=}0\lim_{x\to0}(x-x)=0 $，当然不等， $ \lim_{x\to0}(x-\sin x) $首先要作实数运算.由于 $ \sin x\neq x $， $ \underline{\text{x-\sin x\neq x-x}} $，故趋核运算便无从谈起了.