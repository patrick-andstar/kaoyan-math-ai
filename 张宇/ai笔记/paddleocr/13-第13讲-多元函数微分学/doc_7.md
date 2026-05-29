 $ \rightarrow $è§†yä¸ºå¸¸æ•°

 $$ \frac{\partial F}{\partial x}=\int_{0}^{x-y}f(t)\mathrm{d}t+x f(x-y)-y f(x-y)-(x-y)f(x-y)=\int_{0}^{x-y}f(t)\mathrm{d}t, $$ 

 $$ \frac{\partial^{2}F}{\partial x^{2}}=f(x-y), $$ 

è§†xä¸ºå¸¸æ•°

 $$ \frac{\partial F}{\partial y}=-x f(x-y)-\int_{0}^{x-y}f(t)\mathrm{d}t+y f(x-y)+(x-y)f(x-y)=-\int_{0}^{x-y}f(t)\mathrm{d}t, $$ 

 $$ \frac{\partial^{2}F}{\partial y^{2}}=f(x-y), $$ 

æ‰€ä»¥ $ \frac{\partial F}{\partial x}=-\frac{\partial F}{\partial y},\frac{\partial^{2}F}{\partial x^{2}}=\frac{\partial^{2}F}{\partial y^{2}} $

ä¸�å�¯æ‹†åˆ†ï¼Œæ�¢å…ƒæ±‚å¯¼å�‹

ä¾‹ 13.5 è®¾å‡½æ•°  $ f(x, y) = \int_0^{xy} e^{-xt^2} \, dt $ï¼Œåˆ™  $ f_x'(1, +\infty) = $ ___.

è§£ åº”å¡« $ -\frac{\sqrt{\pi}}{4} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_698_616_913_694.jpg" alt="Image" width="20%" /></div>


å½“x>0æ—¶ï¼Œ

 $ \int_{0}^{+\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2} $.

 $$ f(x,y)=\int_{0}^{xy}\mathrm{e}^{-xt^{2}}\mathrm{d}t\xlongequal[u=\sqrt{xt}]{ ä»¤ \frac{u}{\sqrt{x}}=t}\frac{1}{\sqrt{x}}\int_{0}^{x^{\frac{3}{2}}y}\mathrm{e}^{-u^{2}}\mathrm{d}u, $$ 

äº�æ˜¯ $ f(x,+\infty)=\lim_{y\to+\infty}f(x,y)=\frac{1}{\sqrt{x}}\int_{0}^{+\infty}\mathrm{e}^{-u^{2}}\mathrm{d}u=\frac{\sqrt{\pi}}{2}\cdot\frac{1}{\sqrt{x}} $ï¼Œæ•…

 $$ f_{x}^{\prime}(1,+\infty)=\frac{\sqrt{\pi}}{2}\left(\frac{1}{\sqrt{x}}\right)^{\prime}\bigg|_{x=1}=\frac{\sqrt{\pi}}{2}\left(-\frac{1}{2}\right)\frac{1}{x^{\frac{3}{2}}}\bigg|_{x=1}=-\frac{\sqrt{\pi}}{4}. $$ 

æ³¨ æ­¤é¢˜å…ˆè®¡ç®— $ f(x, +\infty) $ï¼Œå†�è®¡ç®— $ f_{x}^{\prime}(1, +\infty) $æ˜¯ç®€ä¾¿çš„ã€‚

è‹¥å…ˆè®¡ç®— $ f_{x}^{\prime}(x,y) $ï¼Œå†�ä»£å…¥ $ (1,+\infty) $ï¼Œè¿‡ç¨‹å¦‚ä¸‹ï¼š

å°†yå½“ä½œå¸¸æ•°

 $$ f_{x}^{\prime}(x,y)=-\frac{1}{2}x^{-\frac{3}{2}}\cdot\int_{0}^{x^{\frac{3}{2}}y}e^{-u^{2}}du+\frac{1}{\sqrt{x}}e^{-x^{3}y^{2}}\cdot\frac{3}{2}\sqrt{xy} $$ 

å‰�é�¢æ±‚å¯¼ï¼Œå��é�¢ä¸�åŠ¨+

å‰�é�¢ä¸�åŠ¨ï¼Œå��é�¢æ±‚å¯¼

äº�æ˜¯ $ f_{x}^{\prime}(1,+\infty)=-\frac{1}{2}\int_{0}^{+\infty}e^{-u^{2}}du=-\frac{\sqrt{\pi}}{4} $ï¼�ç•¥å¤�æ�‚ï¼�

ä¸¤ç§�æ–¹å¼�è®¡ç®— $ f_{x}^{\prime}(x_{0},y_{0}) $ï¼Œå¾— $ f_{x}^{\prime}(x_{0},y_{0})=\left\{\begin{aligned}f_{x}^{\prime}(x,y_{0})\Big|_{x=x_{0}},\\ f_{x}^{\prime}(x,y)\Big|_{y=y_{0}}\end{aligned}\right. $ï¼Œå…ˆæ±‚å¯¼å†�æ±‚å¯¼