ä¾‹ 13.6 è®¾å‡½æ•°  $ f(x, y) $ å�¯å¾®ï¼Œ $ f(0, 0) = 0 $ï¼Œ $ \frac{\partial f}{\partial x} = -f(x, y) $ï¼Œ $ \frac{\partial f}{\partial y} = e^{-x} \cos y $ï¼Œæ±‚  $ f(x, y) $

åˆ†æ�� å��é—®é¢˜ï¼šå‘Šè¯‰ $ f_{x}^{\prime}, f_{y}^{\prime} $ï¼Œå��æ±‚ $ f(x, y) $ã€‚â†’ä¿�è¯�å��é�¢è¡¨è¾¾å¼�è¿�ç®—æœ‰æ„�ä¹‰

ä¾‹å¦‚åœ¨ä¸€å…ƒå‡½æ•°ä¸­  $ F'(x)=\frac{\mathrm{d}[F(x)]}{\mathrm{d}x}=\cos x $ï¼Œåˆ™  $ F(x)=\int\cos x\mathrm{d}x=\sin x+C $

 $ \begin{cases}\varphi'(x)=\varphi(x)\Rightarrow\varphi(x)=C\mathrm{e}^{x},\\\varphi'(x)=-\varphi(x)\Rightarrow\varphi(x)=C\mathrm{e}^{-x}.\end{cases} $ Cä¸ºä»»æ„�å¸¸æ•°

è§†ä¸ºå…³äº�yçš„å¸¸æ•°



è§£ ç”±  $ \frac{\partial f}{\partial y} = e^{-x} \cos y $ï¼Œå¾—  $ f(x, y) = e^{-x} \sin y + \underline{\phi(x)} $ï¼Œäº�æ˜¯  $ \frac{\partial f}{\partial x} = -e^{-x} \sin y + \phi'(x) $ã€‚

å�ˆ $ \frac{\partial f}{\partial x}=-f(x,y) $ï¼Œæ•…

åˆ©ç”¨å¾®åˆ†æ–¹ç¨‹ $ \frac{d[\varphi(x)]}{dx}=-\varphi(x) $ï¼Œåˆ™

 $$ -\mathrm{e}^{-x}\sin y+\varphi^{\prime}(x)=-\mathrm{e}^{-x}\sin y-\varphi(x), $$ 

äº�æ˜¯æœ‰  $ \varphi'(x) + \varphi(x) = 0 $ï¼Œè§£å¾—  $ \varphi(x) = C\mathrm{e}^{-x} $ï¼Œå�³  $ f(x, y) = \mathrm{e}^{-x} \sin y + C\mathrm{e}^{-x} $ã€‚

 $$ \int\frac{1}{\varphi(x)}\mathrm{d}[\varphi(x)]=-\int\mathrm{d}x $$ 

 $$ \Rightarrow\ln\left|\varphi(x)\right|=-x+\ln C_{0} $$ 

ç”± $ f(0,0)=0 $ï¼Œå¾—C=0ï¼Œæ‰€ä»¥ $ f(x,y)=\mathrm{e}^{-x}\sin y $ã€‚

æ³¨ æœ¬é¢˜è¿›ä¸€æ­¥å�¯æ±‚ $ \underline{f(x,x)} $åœ¨ $ [0,+\infty) $çš„éƒ¨åˆ†ä¸�xè½´å›´æˆ�çš„å›¾å½¢ç»•xè½´æ—‹è½¬ä¸€å‘¨æ‰€æˆ�çš„æ—‹è½¬ä½“ä½“ç§¯ï¼Œæ­¥éª¤å¦‚ä¸‹ï¼š

 $$ \begin{aligned}&V=\int_{0}^{+\infty}\pi[f(x,x)]^{2}\mathrm{d}x=\int_{0}^{+\infty}\pi\mathrm{e}^{-2x}\sin^{2}x\mathrm{d}x=\int_{0}^{+\infty}\pi\mathrm{e}^{-2x}\frac{1-\cos2x}{2}\mathrm{d}x\\ &\\&=\frac{\pi}{2}\int_{0}^{+\infty}\mathrm{e}^{-2x}(1-\cos2x)\mathrm{d}x=\frac{\pi}{2}\int_{0}^{+\infty}\mathrm{e}^{-2x}\mathrm{d}x-\frac{\pi}{2}\int_{0}^{+\infty}\mathrm{e}^{-2x}\cos2x\mathrm{d}x\\ &\\&\xlongequal{ ä»¤ u=2x}\frac{\pi}{4}-\frac{\pi}{4}\int_{0}^{+\infty}\mathrm{e}^{-u}\cos u\mathrm{d}u,\\ \end{aligned} $$ 

å…¶ä¸­

 $$ \begin{aligned}\int_{0}^{+\infty}\mathrm{e}^{-u}\cos u\mathrm{d}u&=\frac{\left|(\mathrm{e}^{-u})^{\prime}\quad(\cos u)^{\prime}\right|}{(\mathrm{e}^{-u}\quad\cos u)}\Bigg|_{0}^{+\infty}\\ &=\frac{1}{2}(-\mathrm{e}^{-u}\cos u+\mathrm{e}^{-u}\sin u)\Bigg|_{0}^{+\infty}\\ &=\frac{1}{2}[0-(-1)]=\frac{1}{2},\\ \end{aligned} $$ 

æ•…

 $$ V=\frac{\pi}{4}-\frac{\pi}{4}\bullet\frac{1}{2}=\frac{\pi}{8}. $$ 