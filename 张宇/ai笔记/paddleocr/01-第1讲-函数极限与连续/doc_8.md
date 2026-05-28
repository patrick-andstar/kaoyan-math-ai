注 考研试题中常出现这种问题，考生要重视.

隐函数问题先给大家提到这里，与之相关的隐函数存在定理，以及隐函数存在定理所推出的公式法等，我们到后面再去讲。

★★★5 函数的四种特性→考研中怎么去使用这些特性呢？微积分是利用极限这个工具研究函数、函数的导数及积分的四种特性

(1)有界性.

设 $ f(x) $的定义域为 $ D $， $ \underline{\text{数集}} $  $ I\subset D $。如果存在某个正数 $ M $，使对任一 $ x\in I $，有 $ |f(x)|\leq M $，则称 $ f(x) $在 $ I $上有界；如果这样的 $ M $不存在，则称 $ f(x) $在 $ I $上无界。

注 (1) 从几何上看，如果在给定的区间，函数  $ y = f(x) $ 的图形能够被直线  $ y = -M $ 和  $ y = M $ “完全包起来”，则为有界；从解析上说，如果找到某个正数  $ M $，使得  $ |f(x)| \leq M $，则为有界。

<div style="text-align: center;"><img src="imgs/img_in_image_box_444_592_661_709.jpg" alt="Image" width="21%" /></div>


<div style="text-align: center;">区间I</div>


能画圆则画圆，不易画圆，我们就用解析法，去找正数M.

(2)有界还是无界的讨论首先需指明区间I，不知区间，无法谈论有界性.比如 $ y=\frac{1}{x} $在 $ (2,+\infty) $内有界，但在 $ (0,2) $内无界.

<div style="text-align: center;"><img src="imgs/img_in_image_box_442_831_664_988.jpg" alt="Image" width="21%" /></div>


(3)事实上，只要在区间I上或其端点处存在点 $ x_{0} $，使得 $ \lim_{x\to x_{0}}f(x) $的值为无穷大，则没有任何两条直线y=-M和y=M可以把I上的 $ f(x) $“包起来”，这就叫无界.考研中常出这样的题目，比如例1.17.

例 1.6 证明函数  $ f(x)=\frac{x}{1+x^{2}} $ 在  $ (-∞,+∞) $ 内有界.

补充： $ x^{2}=\left|x^{2}\right|=\left|x\right|^{2} $



 $$ \begin{aligned}&x^{3}\neq\left|x^{3}\right|=\left|x\right|^{3},\\&\left|x\right|=\sqrt{x^{2}}.\\ \end{aligned} $$ 

分析 当  $ x \neq 0 $ 时， $ \left|f(x)\right| = \frac{|x|}{1 + x^2} \xlongequal{\text{分子分母同除}} \frac{1}{\frac{1}{|x|} + |x|} $ 或者用  $ \left|x\right| = \sqrt{x^2} $

若求  $ \left[\left|f(x)\right|\right]' $ 呢；



证 方法一 当 $ x\neq0 $时，

 $$ \left|f(x)\right|=\frac{\left|x\right|}{1+x^{2}}=\frac{1}{\frac{1}{\left|x\right|}+\left|x\right|}, $$ 

 $$ \begin{aligned}\left[\mid f(x)\mid\right]^{\prime}=&\left[\sqrt{f^{2}(x)}\right]^{\prime}\\ =&\frac{2f(x)f^{\prime}(x)}{2\sqrt{f^{2}(x)}}=\frac{f(x)f^{\prime}(x)}{\mid f(x)\mid}.\end{aligned} $$ 

 $$ \begin{aligned} 再如：f(x)&=2x+\sqrt{x^{2}+2x+1}\\&=2x+\sqrt{(x+1)^{2}}\\&=2x+\left|x+1\right|.\end{aligned} $$ 