## 2 敛散性的判别法

(1)无穷区间．

比较判别法 设函数 $ f(x) $， $ g(x) $在区间 $ [a, +\infty) $上连续，并且 $ 0 \leqslant f(x) \leqslant g(x) $（ $ a \leqslant x < +\infty $），则

①当 $ \int_{a}^{+\infty} g(x)dx $收敛时， $ \int_{a}^{+\infty} f(x)dx $收敛；



②当 $ \int_{a}^{+\infty}f(x)dx $发散时， $ \int_{a}^{+\infty}g(x)dx $发散.

<div style="text-align: center;"><img src="imgs/img_in_image_box_574_260_759_378.jpg" alt="Image" width="17%" /></div>


★比较判别法的极限形式 设函数 $ f(x) $， $ g(x) $在区间 $ [a, +\infty) $上连续，且 $ f(x) \geq 0 $， $ g(x) > 0 $， $ \lim_{x \to +\infty} \frac{f(x)}{g(x)} = \lambda $有限或 $ \infty $，则  $ \rightarrow $ 说明 $ f(x) $， $ g(x) $是同阶无穷小。

①当 $ \lambda\neq0 $且 $ \lambda\neq\infty $时， $ \int_{a}^{+\infty}f(x)dx $与 $ \int_{a}^{+\infty}g(x)dx $有相同的敛散性；

②当 $ \lambda=0 $时，若 $ \int_{a}^{+\infty}g(x)dx $收敛，则 $ \int_{a}^{+\infty}f(x)dx $也收敛；

③当 $ \lambda=\infty $时，若 $ \int_{a}^{+\infty}g(x)dx $发散，则 $ \int_{a}^{+\infty}f(x)dx $也发散。

(2) 无界函数.

比较判别法 设  $ f(x) $,  $ g(x) $ 在  $ (a, b] $ 上连续，瑕点同为 x = a，并且  $ 0 \leqslant f(x) \leqslant g(x) (a < x \leqslant b) $，则

①当 $ \int_{a}^{b}g(x)dx $收敛时， $ \int_{a}^{b}f(x)dx $收敛；



②当 $ \int_{a}^{b}f(x)dx $发散时， $ \int_{a}^{b}g(x)dx $发散.

<div style="text-align: center;"><img src="imgs/img_in_image_box_614_797_780_925.jpg" alt="Image" width="16%" /></div>


比较判别法的极限形式 设  $ f(x) $,  $ g(x) $ 在  $ (a, b] $ 上连续，瑕点同为  $ x = a $，并且  $ f(x) \geq 0 $,  $ g(x) > 0 $ ( $ a < x \leq b $),  $ \lim_{x \to a^+} \frac{f(x)}{g(x)} = \lambda $（有限或  $ \infty $），则  $ \rightarrow $ 计算极限

 $$ f(x),g(x) $$ 

①当 $ \lambda\neq0 $且 $ \lambda\neq\infty $时， $ \int_{a}^{b}f(x)dx $和 $ \int_{a}^{b}g(x)dx $有相同的敛散性；

 $ g(x) $ 趋于  $ \infty $ 的速度比  $ f(x) $ 更快

②当 $ \lambda=0 $时，若 $ \int_{a}^{b}g(x)dx $收敛，则 $ \int_{a}^{b}f(x)dx $也收敛；

③当 $ \lambda=\infty $时，若 $ \int_{a}^{b}g(x)dx $发散，则 $ \int_{a}^{b}f(x)dx $也发散.

## 注 两个重要结论