## è€ƒç ”ä¸­å¸¸è§�è€ƒé¢˜

ä¾‹ 13.19 å·²çŸ¥å‡½æ•°  $ z = z(x, y) $ ç”±æ–¹ç¨‹  $ (x^2 + y^2)z + \ln z + 2(x + y + 1) = 0 $ ç¡®å®šï¼Œæ±‚  $ z(x, y) $ çš„æ��å€¼.

è§£ åœ¨  $ (x^{2}+y^{2})z+\ln z+2(x+y+1)=0 $ ä¸¤ç«¯åˆ†åˆ«å¯¹ x å’Œ y æ±‚å��å¯¼æ•°ï¼Œå¾—

 $$ \begin{cases}2xz+(x^{2}+y^{2})\frac{\partial z}{\partial x}+\frac{1}{z}\frac{\partial z}{\partial x}+2=0,\\2yz+(x^{2}+y^{2})\frac{\partial z}{\partial y}+\frac{1}{z}\frac{\partial z}{\partial y}+2=0,\end{cases} $$ 

ä»¤ $ \frac{\partial z}{\partial x}=0,\frac{\partial z}{\partial y}=0 $ï¼Œå¾— $ \left\{\begin{aligned}x&=-\frac{1}{z},\\ y&=-\frac{1}{z}.\end{aligned}\right. $

å°† $ \begin{cases} x = -\frac{1}{z}, \\ y = -\frac{1}{z} \end{cases} $ä»£å…¥æ–¹ç¨‹ $ (x^2 + y^2)z + \ln z + 2(x + y + 1) = 0 $ï¼Œå¾— $ \ln z - \frac{2}{z} + 2 = 0 $ï¼Œå�¯çŸ¥z = 1ï¼Œä»�è€Œ $ \begin{cases} x = -1, \\ y = -1. \end{cases} $

æ–¹ç¨‹ç»„ $ (*) $ä¸­ä¸¤å¼�çš„ä¸¤ç«¯åˆ†åˆ«å†�å¯¹xã€�yæ±‚å��å¯¼æ•°ï¼Œå¾—

æ–¹ç¨‹ç»„ $ (*) $ä¸­ä¸¤å¼�çš„ä¸¤ç«¯åˆ†åˆ«å†�å¯¹x,yæ±‚å��å¯¼æ•°ï¼Œå¾—

 $$ \begin{cases}2z+4x\frac{\partial z}{\partial x}+(x^{2}+y^{2})\frac{\partial^{2}z}{\partial x^{2}}-\frac{1}{z^{2}}\bigg(\frac{\partial z}{\partial x}\bigg)^{2}+\frac{1}{z}\frac{\partial^{2}z}{\partial x^{2}}=0,\\2x\frac{\partial z}{\partial y}+2y\frac{\partial z}{\partial x}+(x^{2}+y^{2})\frac{\partial^{2}z}{\partial x\partial y}-\frac{1}{z^{2}}\frac{\partial z}{\partial x}\frac{\partial z}{\partial y}+\frac{1}{z}\frac{\partial^{2}z}{\partial x\partial y}=0,\\2z+4y\frac{\partial z}{\partial y}+(x^{2}+y^{2})\frac{\partial^{2}z}{\partial y^{2}}-\frac{1}{z^{2}}\bigg(\frac{\partial z}{\partial y}\bigg)^{2}+\frac{1}{z}\frac{\partial^{2}z}{\partial y^{2}}=0,\end{cases} $$ 

ä»�è€Œå¾—  $ A=\frac{\partial^{2}z}{\partial x^{2}}\bigg|_{(-1,-1)}=-\frac{2}{3} $ï¼Œ $ B=\frac{\partial^{2}z}{\partial x\partial y}\bigg|_{(-1,-1)}=0 $ï¼Œ $ C=\frac{\partial^{2}z}{\partial y^{2}}\bigg|_{(-1,-1)}=-\frac{2}{3} $ã€‚

ç”±äº� $ AC-B^{2}>0,\quad A<0 $ï¼Œå› æ­¤ $ z(-1,-1)=1 $æ˜¯ $ z(x,y) $çš„æ��å¤§å€¼.

## 3 æ�¡ä»¶æœ€å€¼ä¸�æ‹‰æ ¼æœ—æ—¥ä¹˜æ•°æ³•

æ±‚ç›®æ ‡å‡½æ•°  $ u = f(x, y, z) $ åœ¨çº¦æ�Ÿæ�¡ä»¶  $ \left\{\begin{aligned}\varphi(x, y, z) &= 0, \\ \psi(x, y, z) &= 0\end{aligned}\right. $ ä¸‹çš„æœ€å€¼ï¼Œåˆ™

â‘ æ�„é€ è¾…åŠ©å‡½æ•°  $ F(x, y, z, \lambda, \mu) = f(x, y, z) + \lambda \varphi(x, y, z) + \mu \psi(x, y, z) $;

ç¬¬1ä¸ªçº¦æ�Ÿ ç¬¬2ä¸ªçº¦æ�Ÿ

â‘¡ä»¤è‡ªå�˜é‡�ä¸ªæ•°=ç›®æ ‡å‡½æ•°è‡ªå�˜é‡�ä¸ªæ•°+çº¦æ�Ÿä¸ªæ•°

 $$ \begin{cases}F_{x}^{\prime}=f_{x}^{\prime}+\lambda\varphi_{x}^{\prime}+\mu\psi_{x}^{\prime}=0,\\F_{y}^{\prime}=f_{y}^{\prime}+\lambda\varphi_{y}^{\prime}+\mu\psi_{y}^{\prime}=0,\\F_{z}^{\prime}=f_{z}^{\prime}+\lambda\varphi_{z}^{\prime}+\mu\psi_{z}^{\prime}=0,\\F_{\lambda}^{\prime}=\varphi(x,y,z)=0,\\F_{\mu}^{\prime}=\psi(x,y,z)=0;\end{cases} $$ 

â‘¢è§£ä¸Šè¿°æ–¹ç¨‹ç»„å¾—å¤‡é€‰ç‚¹  $ P_{i}, i=1,2,3,\cdots,n $ï¼Œå¹¶æ±‚  $ f(P_{i}) $ï¼Œå�–å…¶æœ€å¤§å€¼ä¸º  $ u_{\max} $ï¼Œæœ€å°�å€¼ä¸º  $ u_{\min} $ï¼›