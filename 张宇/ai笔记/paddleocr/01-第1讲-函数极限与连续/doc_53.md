(7)夹逼准则.适当放缩已知不等式.题设条件

如果函数 $ f(x) $， $ g(x) $及 $ h(x) $满足下列条件：

①  $ h(x) \leqslant f(x) \leqslant g(x) $;

\[\textcircled{2}\lim g(x)=A,\lim h(x)=A\xrightarrow{}\begin{array}{c}\rightarrow h(x)\leqslant f(x)\leqslant g(x)\\ \downarrow\quad\downarrow\quad\downarrow\\ \downarrow\quad\downarrow\quad\downarrow\quad\downarrow\quad\downarrow

 $$ A\Rightarrow A\Leftrightarrow A $$ 

则  $ \lim f(x) $ 存在，且  $ \lim f(x) = A $。 $ \quad +\infty \Rightarrow +\infty \Leftarrow +\infty $

夹逼准则，说成两边夹，三明治定理都不太准确，没有突出“逼”，叫“迫敛定理”是可以的。

注 常见的一个问题：设任意的 x，总有  $ h(x) \leqslant f(x) \leqslant g(x) $，且  $ \lim[g(x) - h(x)] = 0 $，则  $ \lim f(x) $ 是否一定存在？答案是否定的。 $ \lim[g(x) - h(x)] $ 存在并不能说明  $ \lim g(x) $， $ \lim h(x) $ 都存在，从而也不能保证  $ \lim f(x) $ 存在。

例如，当 x > 0 时，取  $ h(x) = x + \frac{1}{x+1} $， $ f(x) = x + \frac{2}{x+1} $， $ g(x) = x + \frac{3}{x+1} $，则  $ h(x) < f(x) < g(x) $，且  $ \lim_{x \to +\infty} [g(x) - h(x)] = 0 $，但  $ \lim_{x \to +\infty} f(x) $ 不存在。

## 2 七种未定式的计算

七种未定式中，都是超实数的状态，我们算过七种超实数是否有一个标准实数部分。

考研的函数极限计算题一般归纳为七种未定式： $ \rightarrow $“未定”是由你来定，有可能存在有可能不存在

<div style="text-align: center;"><img src="imgs/img_in_image_box_253_814_809_915.jpg" alt="Image" width="53%" /></div>


★★★题型：直接计算、反求参数、已知某一极限求另一极限、无穷小的比阶等。

在表达式中，有一些未知参数，已知这些超实数的极限值，来求这些未知参数，这是一种常考的反问题

解题思路如下.

已知一个超实数的极限值，给出另外一个超实数，另外一个超实数跟这个超实数有联系，有区别，需要找到它们的联系和区别，从而用已知来求解未知

在考研数学中，可能无穷小比阶的考题考的是最多的

①化简先行.

拿到极限计算的问题，不要直接开始就洛必达法则，泰勒展开等等。实际上，先做一些化简，有的时候化简完了，这个题目就非常简单了，在考研中是专门出过这种题的，比如说2023年有道大题就是，第一步要化简，如果不知道化简的话，那个题太复杂了。有哪些化简办法呢？

 $$ \lim_{x\to0}\cos x\cdot(\cdots)\mathrm{e}^{x} $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_559_1290_931_1359.jpg" alt="Image" width="36%" /></div>


a. 提出极限不为 0 的因式；b. 等价无穷小代换；c. 恒等变形（基本的恒等变形法如提公因式、拆项、