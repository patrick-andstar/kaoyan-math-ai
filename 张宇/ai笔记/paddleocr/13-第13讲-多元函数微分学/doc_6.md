(A)  $ \left.\frac{\partial f}{\partial x}\right|_{(0,1)} $ ä¸�å­˜åœ¨ï¼Œ $ \left.\frac{\partial f}{\partial y}\right|_{(0,1)} $ å­˜åœ¨

(B)  $ \left.\frac{\partial f}{\partial x}\right|_{(0,1)} $ å­˜åœ¨ï¼Œ $ \left.\frac{\partial f}{\partial y}\right|_{(0,1)} $ ä¸�å­˜åœ¨

(C) $ \left.\frac{\partial f}{\partial x}\right|_{(0,1)} $ï¼Œ $ \left.\frac{\partial f}{\partial y}\right|_{(0,1)} $å�‡å­˜åœ¨

(D) $ \left.\frac{\partial f}{\partial x}\right|_{(0,1)} $ï¼Œ $ \left.\frac{\partial f}{\partial y}\right|_{(0,1)} $å�‡ä¸�å­˜åœ¨

(2) åˆ†æ��  $ \left.\frac{\partial f}{\partial x}\right|_{(0,1)}=\lim_{\Delta x\to0}\frac{f(0+\Delta x,1)-f(0,1)}{\Delta x}=\lim_{\Delta x\to0}\frac{\ln(1+\sqrt{\Delta x\cdot\sin1})-0}{\Delta x} $ åˆ©ç”¨å½“  $ x\to0 $ æ—¶ï¼Œ $ \ln(1+x)\sim x $

 $ \left.\frac{\partial f}{\partial y}\right|_{(0,1)}=\lim_{\Delta y\to0}\frac{f(0,1+\Delta y)-f(0,1)}{\Delta y}=\lim_{\Delta y\to0}\frac{\ln(1+\Delta y)-0}{\Delta y} $

## è§£ åº”é€‰(A)

å› ä¸º $ f(x,y)=\ln\left(y+\left|x\sin y\right|\right) $ï¼Œæ‰€ä»¥

 $$ f(0,1)=\ln(1+0)=0,\;f(x,1)=\ln\left(1+\left|x\sin1\right|\right),\;f(0,\;y)=\ln(y+0)=\ln y, $$ 

å› æ­¤

 $$ \left.\frac{\partial f}{\partial x}\right|_{(0,1)}=\lim_{x\to0}\frac{f(x,1)-f(0,1)}{x-0}=\lim_{x\to0}\frac{\ln(1+\left|x\sin1\right|)}{x}=\lim_{x\to0}\frac{\left|x\sin1\right|}{x}, $$ 

 $$ \left.\frac{\partial f}{\partial y}\right|_{(0,1)}=\lim_{y\to1}\frac{f(0,y)-f(0,1)}{y-1}=\lim_{y\to1}\frac{\ln y}{y-1}=\lim_{y\to1}\frac{1}{y}=1, $$ 

æ‰€ä»¥ $ \left.\frac{\partial f}{\partial x}\right|_{(0,1)} $ ä¸�å­˜åœ¨ï¼Œ $ \left.\frac{\partial f}{\partial y}\right|_{(0,1)} $ å­˜åœ¨.

æ³¨  $ f_{x}^{\prime}(x_{0},y_{0})=\lim_{\Delta x\to0}\frac{f(x_{0}+\Delta x,y_{0})-f(x_{0},y_{0})}{\Delta x} $  $ \lim_{x\to x_{0}}\frac{f(x,y_{0})-f(x_{0},y_{0})}{x-x_{0}} $  $ \rightarrow $ å‡½æ•°å·®å€¼å¼�

å�Œç�†ï¼Œ $ f_{y}^{\prime}(x_{0},y_{0})=\lim_{\Delta y\to0}\frac{f(x_{0},y_{0}+\Delta y)-f(x_{0},y_{0})}{\Delta y}\xlongequal{y_{0}+\Delta y=y}\lim_{y\to y_{0}}\frac{f(x_{0},y)-f(x_{0},y_{0})}{y-y_{0}} $

ä¾‹ 13.4 è®¾å‡½æ•°  $  f(t)  $ è¿�ç»­ï¼Œä»¤  $  F(x, y) = \int_{0}^{x-y} (x-y-t) f(t) \, dt  $ï¼Œåˆ™ï¼ˆï¼‰.

(A)  $ \frac{\partial F}{\partial x} = \frac{\partial F}{\partial y}, \frac{\partial^{2}F}{\partial x^{2}} = \frac{\partial^{2}F}{\partial y^{2}} $

(B)  $ \frac{\partial F}{\partial x} = \frac{\partial F}{\partial y}, \frac{\partial^{2}F}{\partial x^{2}} = -\frac{\partial^{2}F}{\partial y^{2}} $

(C)  $ \frac{\partial F}{\partial x} = -\frac{\partial F}{\partial y}, \frac{\partial^{2}F}{\partial x^{2}} = \frac{\partial^{2}F}{\partial y^{2}} $

(D)  $ \frac{\partial F}{\partial x} = -\frac{\partial F}{\partial y}, \frac{\partial^{2}F}{\partial x^{2}} = -\frac{\partial^{2}F}{\partial y^{2}} $

## è§£ åº”é€‰(C)

ç”±é¢˜çŸ¥ï¼Œ $ F(x,y)=x\int_{0}^{x-y}f(t)dt-y\int_{0}^{x-y}f(t)dt-\int_{0}^{x-y}tf(t)dt $ï¼Œåˆ™