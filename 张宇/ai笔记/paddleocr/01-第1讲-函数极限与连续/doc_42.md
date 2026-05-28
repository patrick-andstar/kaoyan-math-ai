③有限个无穷小的乘积是无穷小.

 $$ \alpha_{2}\rightarrow0\Rightarrow|\alpha_{2}|<1\xrightarrow{ 常用 } $$ 

 $$ 0\leqslant\left|\alpha_{1}\alpha_{2}\right|<\left|\alpha_{1}\right|\bullet1\rightarrow0. $$ 

如

夹逼到0

## 无穷小的比阶

在讲极限概念时，柯西也好，魏尔斯特拉斯也好，比牛顿和莱布尼茨的进步只是用了一个不等式，可是他们也没有讲  $ \alpha $ 到 0 的距离到底有多少， $ \beta $ 到 0 的距离是多少？不过我们可以尝试从  $ \alpha $， $ \beta $ 的阶数比入手。

<div style="text-align: center;"><img src="imgs/img_in_image_box_723_324_969_457.jpg" alt="Image" width="23%" /></div>


设在自变量的同一变化过程中， $ \lim\alpha(x)=0 $， $ \lim\beta(x)=0 $，且 $ \beta(x)\neq0 $，则

①若  $ \lim_{\sqrt{\frac{\alpha(x)}{\beta(x)}}} $ = 0，则称  $ \alpha(x) $ 是比  $ \beta(x) $ 高阶的无穷小，记为  $ \alpha(x) = o(\beta(x)) $；

 $ \alpha(x) \rightarrow 0 $ 的速度比  $ \beta(x) \rightarrow 0 $ 的速度快

②若  $ \lim_{\beta(x)} \frac{\alpha(x)}{\beta(x)} = \infty $，则称  $ \alpha(x) $ 是比  $ \beta(x) $ 低阶的无穷小；

★③若  $ \lim\frac{\alpha(x)}{\beta(x)}=c\neq0 $ ，则称  $ \alpha(x) $ 与  $ \beta(x) $ 是同阶无穷小；

最重要的是③与④

★④若  $ \lim_{\beta(x)} \frac{\alpha(x)}{\beta(x)} = 1 $，则称  $ \alpha(x) $ 与  $ \beta(x) $ 是等价无穷小，记为  $ \alpha(x) \sim \beta(x) $；

“等价”不是相等，如  $ \lim_{x\to0}\frac{\sin x}{x}=1\neq0 $，而  $ \lim_{x\to0}\frac{x-\sin x}{x^{3}}=\frac{1}{6} $.

 $$  是它的标准实数部分 \mathrm{std}\left(\frac{\sin x}{x}\right)=1 $$ 

⑤若  $ \lim_{x\to0}\frac{\alpha(x)}{\left[\beta(x)\right]^{k}}=c\neq0,k>0 $ ，则称  $ \alpha(x) $ 是  $ \beta(x) $ 的 k 阶无穷小 .

并不是任意两个无穷小都可进行比阶的。例如，当  $ x \to 0 $ 时， $ x\sin\frac{1}{x} $ 与  $ x^2 $ 虽然都是无穷小，但是却不可以比阶，也就是说既无高低阶之分，也无同阶可言，因为  $ \lim_{x \to 0} \frac{x\sin\frac{1}{x}}{x^2} = \lim_{x \to 0} \frac{1}{x\sin\frac{1}{x}} $ 不存在。

 $$ \lim_{x\to0}\frac{x\sin\frac{1}{x}}{x^{2}}=\lim_{x\to0}\frac{1}{x}\sin\frac{1}{x}\xrightarrow{ 极限不存在，一会儿跑到无穷大，一会跑到 0, 所以这种不专一的超实数定义为  无界变量 } $$ 