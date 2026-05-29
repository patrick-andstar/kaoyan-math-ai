解

 $$ \begin{aligned} 原式 =&\int_{3}^{+\infty}\frac{\mathrm{d}x}{(x-1)^{4}\sqrt{(x-1)^{2}-1}}\xlongequal{x-1=\sec\theta}\int_{\frac{\pi}{3}}^{\frac{\pi}{2}}\frac{\sec\theta\tan\theta}{\sec^{4}\theta\tan\theta}\mathrm{d}\theta\\=&\int_{\frac{\pi}{3}}^{\frac{\pi}{2}}(1-\sin^{2}\theta)\cos\theta\mathrm{d}\theta=\frac{2}{3}-\frac{3\sqrt{3}}{8}\ .\end{aligned} $$ 

注 在收敛的条件下，通过换元可能实现反常积分与定积分的相互转化.

★★★例9.28 计算 $ I_{n}=\int_{0}^{+\infty}x^{n}e^{-x}dx $（n为非负整数）.

分析 分部积分法可能会建立递推式  $ I_{n}=f(I_{n-1}) $

解 由分部积分法，得

 $$ I_{n}=-\int_{0}^{+\infty}x^{n}\mathrm{d}(\mathrm{e}^{-x})=(-x^{n}\mathrm{e}^{-x})\bigg|_{0}^{+\infty}+n\int_{0}^{+\infty}x^{n-1}\mathrm{e}^{-x}\mathrm{d}x=nI_{n-1},\;n=1,\;2,\cdots, $$ 

其中  $ \lim_{x\to+\infty}x^{n}e^{-x}=0 $ 。又因为

 $$ I_{0}=\int_{0}^{+\infty}\mathrm{e}^{-x}\mathrm{d}x=-\mathrm{e}^{-x}\bigg|_{0}^{+\infty}=1, $$ 

所以

 $$ \int_{0}^{+\infty}x^{3}\mathrm{e}^{-x}\mathrm{d}x=I_{3}=3!=6 $$ 

 $$ I_{n}=nI_{n-1}=n(n-1)I_{n-2}=\cdots=n(n-1)\cdots1\bullet I_{0}=n!. $$ 

注 计算积分时，若能用上“Γ函数”的知识，会既快速又准确.

(1) 定义： $ \Gamma(\alpha)=\int_{0}^{+\infty}x^{\alpha-1}\mathrm{e}^{-x}\mathrm{d}x\xlongequal{x=t^{2}}2\int_{0}^{+\infty}t^{2\alpha-1}\mathrm{e}^{-t^{2}}\mathrm{d}t(x,t>0) $

(2) 递推式： $ \Gamma(\alpha+1)=\int_{0}^{+\infty}x^{\alpha}\mathrm{e}^{-x}\mathrm{d}x=-\int_{0}^{+\infty}x^{\alpha}\mathrm{d}(\mathrm{e}^{-x})=-x^{\alpha}\mathrm{e}^{-x}\bigg|_{0}^{+\infty}+\int_{0}^{+\infty}\mathrm{e}^{-x}\alpha x^{\alpha-1}\mathrm{d}x=\alpha\Gamma(\alpha) $

其中  $ \Gamma(1)=1 $,  $ \Gamma\left(\frac{1}{2}\right)=\sqrt{\pi} $, 故  $ \Gamma(n+1)=n! $,  $ \Gamma(2)=1 $,  $ \Gamma\left(\frac{5}{2}\right)=\frac{3}{2}\cdot\frac{1}{2}\cdot\Gamma\left(\frac{1}{2}\right)=\frac{3}{4}\sqrt{\pi} $.

 $$ \Gamma(1)=\int_{0}^{+\infty}\mathrm{e}^{-x}\mathrm{d}x=1 $$ 

 $$ \Rightarrow\Gamma\left(\frac{1}{2}\right)=2\int_{0}^{+\infty}\mathrm{e}^{-t^{2}}\mathrm{d}t=\sqrt{\pi} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_95_1088_340_1260.jpg" alt="Image" width="23%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_373_1093_688_1238.jpg" alt="Image" width="30%" /></div>


诺贝尔物理学奖得主费曼喜欢“在积分号下求导”这种被数学家认为不严谨甚至“荒唐”的方法，如已知 $ \int_{0}^{+\infty}e^{-x}dx=1 $，简单推广为 $ \int_{0}^{+\infty}e^{-x}dx=\frac{1}{a},a>0 $。一个有意思的现象是：视 $ a $为变量，等式两边对 $ a $求导，注意左边是在积分号下对 $ a $求导，有 $ \int_{0}^{+\infty}(e^{-x})_{0}^{x}dx=\left(\frac{1}{a}\right)_{0}^{x} $，即 $ -\int_{0}^{+\infty}x\cdot e^{-x}dx=-\frac{1}{a} $，重复上述工作，直到 $ (-1)^{n}\int_{0}^{+\infty}x^{n}e^{-x}dx=(-1)^{n}\left(\frac{n}{a^{n+1}}\right)^{n+1} $，再令 $ a=1 $，得 $ x^{n}e^{-x}dx=n! $，费曼对自己的这个“战法”非常得意，他说：“无论用什么方法，即便是戏法，只有答案对了，才是唯一重要的。”