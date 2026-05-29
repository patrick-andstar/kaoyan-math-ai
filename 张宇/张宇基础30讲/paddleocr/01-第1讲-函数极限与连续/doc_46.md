(♂分析) 先利用例 1.20 的结果求出 a 的值，再用等价无穷小的代换求 b 的值.

## 解 应选(A)

 $ \lim_{x\to0}\frac{\sin x}{e^x-a}(\cos x-b)=5\neq0 $，由例1.20的(2)知， $ \lim_{x\to0}(e^x-a)=0 $，故a=1，此时原极限变为 $ \lim_{x\to0}\frac{\sin x}{e^x-1}(\cos x-b)=\lim_{x\to0}(\cos x-b)=1-b $，故b=-4。

方法总结 若  $ \lim_{x\to0}\frac{f(x)}{g(x)}=A\neq0 $，且  $ \lim_{x\to0}f(x)=0 $，则  $ \lim_{x\to0}g(x)=0 $。

∅公式 当 $ x \to 0 $时， $ e^x - 1 \sim x \sim \sin x $。

例 1.20 的两个结论，是用四则运算规则证明的，所以可以把刚才的解题方法归结为极限的四则运算规则：加减乘除的极限只要存在，就等于极限的加减乘除。考生们在刚开始复习要记住它，不要认为它简单就轻视，前面用超实数分析了“不存在 + 不存在”为什么可能存在，这部分内容不是那么容易理解的，不是听一遍就能完全搞懂，需要不断地、反复地思考和实践。

后面我们会遇到复杂的极限情况，那么怎么处理这些复杂情况呢？需要请两个了不起的数学人物“登场”，他们是洛必达和伯努利。

(2) 洛必达法则.

法则一 设①当 $ x \to a $（或 $ x \to \infty $）时，函数 $ f(x) $及 $ F(x) $都趋于零；

② $ f'(x) $及 $ F'(x) $在点a的某去心邻域内（或当 $ |x|>X $，此时X为充分大的正数）存在，且 $ F'(x)\neq0 $；

<div style="text-align: center;"><img src="imgs/img_in_image_box_830_658_958_834.jpg" alt="Image" width="12%" /></div>


③ $ \lim_{x\to a}\frac{f'(x)}{F'(x)} $（或 $ \lim_{x\to\infty}\frac{f'(x)}{F'(x)} $）存在或为无穷大，则

洛必达

(1661—1704)

 $$ \lim_{x\to a}\frac{f(x)}{F(x)}=\lim_{x\to a}\frac{f^{\prime}(x)}{F^{\prime}(x)}( 或 \lim_{x\to\infty}\frac{f(x)}{F(x)}=\lim_{x\to\infty}\frac{f^{\prime}(x)}{F^{\prime}(x)}). $$ 

法则二 设①当 $ x\to a $（或 $ x\to\infty $）时，函数 $ f(x) $及 $ F(x) $都趋于无穷大；

② $ f'(x) $及 $ F'(x) $在点a的某去心邻域内（或当 $ |x|>X $，此时X为充分大的正数）存在，且 $ F'(x)\neq0 $；

③ $ \lim_{x\to a}\frac{f'(x)}{F'(x)} $（或 $ \lim_{x\to\infty}\frac{f'(x)}{F'(x)} $）存在或为无穷大，则

 $$ \lim_{x\to a}\frac{f(x)}{F(x)}=\lim_{x\to a}\frac{f^{\prime}(x)}{F^{\prime}(x)}( 或 \lim_{x\to\infty}\frac{f(x)}{F(x)}=\lim_{x\to\infty}\frac{f^{\prime}(x)}{F^{\prime}(x)}). $$ 

这两个是用柯西中值定理证明的。

后面讲了柯西中值定理，再回头证明这个洛必达法则