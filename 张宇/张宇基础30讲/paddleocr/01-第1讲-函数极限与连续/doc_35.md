c.  $ \lim_{x\to x_0}\frac{f(x)}{g(x)}=\lim_{x\to x_0}f(x)\cdot\frac{1}{g(x)} $

讨论与b. 类似.

综上所述，可列表如下：


<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>条件</td><td style='text-align: center; word-wrap: break-word;'>结论</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ f(x) $， $ g(x) $均存在核值</td><td style='text-align: center; word-wrap: break-word;'>$ f(x) \pm g(x) $， $ f(x) \cdot g(x) $， $ \frac{f(x)}{g(x)} $（ $ g(x) $核值不为0）均存在核值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ f(x) $， $ g(x) $中恰有一个不存在核值</td><td style='text-align: center; word-wrap: break-word;'>$ f(x) \pm g(x) $不存在核值； $ f(x) \cdot g(x) $可能存在核值，也可能不存在核值； $ \frac{f(x)}{g(x)} $可能存在核值，也可能不存在核值</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ f(x) $， $ g(x) $均不存在核值</td><td style='text-align: center; word-wrap: break-word;'>$ f(x) \pm g(x) $， $ f(x) \cdot g(x) $， $ \frac{f(x)}{g(x)} $均可能存在核值，也可能不存在核值</td></tr></table>

## 4 函数极限的性质

(1) 唯一性.

如果极限  $ \lim_{x\to x_0}f(x) $ 存在，那么极限唯一。任何一个实数，周围有无数个光环。

<div style="text-align: center;"><img src="imgs/img_in_image_box_421_783_611_948.jpg" alt="Image" width="18%" /></div>


前面表中的24种情况

## 注 (1) 函数极限存在的充要条件

与 $ f(x_{0}) $天生没关系

表示左右趋近都是  $ A \leftarrow \begin{cases} \lim\limits_{x \to x_0} f(x) = A \Leftrightarrow \lim\limits_{x \to x_0} f(x) = A \text{且} \lim\limits_{x \to x_0} f(x) = A, \\ \lim\limits_{x \to x_0} f(x) = A \Leftrightarrow f(x) = A + \alpha(x), \lim\limits_{x \to x_0} \alpha(x) = 0 \end{cases} $

趋实数  $ f(x) = A \Leftrightarrow f(x) = \begin{cases} \lim\limits_{x \to x_0} f(x) = A \Leftrightarrow f(x) = A + \alpha(x), \lim\limits_{x \to x_0} \alpha(x) = 0 \end{cases} $

<div style="text-align: center;"><img src="imgs/img_in_image_box_740_1049_903_1203.jpg" alt="Image" width="15%" /></div>


 $$  一个超实数 = 实数 + 超实数 $$ 

①对于 $ x\to\infty $，意味着 $ x\to+\infty $且 $ x\to-\infty $；两个方向

②对于 $ x \to x_{0} $，意味着 $ x \to x_{0}^{+} $且 $ x \to x_{0}^{-} $。

我们称这个细节的问题为自变量取值的“双向性(有正有负)”，基于此，我们看几个重要的函数极限问题.