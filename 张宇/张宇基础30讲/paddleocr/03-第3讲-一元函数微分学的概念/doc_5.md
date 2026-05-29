又  $ f'\left(\frac{1}{2}\right)>0 $，由例 3.1(C) 选项的结论，知  $ f'(x) $ 也是以 2 为周期的周期函数，则  $ f'\left(\frac{3}{2}\right)= $

 $ f'\left(\frac{3}{2}-2\right)=f'\left(-\frac{1}{2}\right)=f'\left(\frac{1}{2}\right)>0 $，故 $ f\left(-\frac{1}{2}\right)<f^{\prime\prime}(0)<f'\left(\frac{3}{2}\right) $，即M<K<N，应选(C).

例 3.3 设  $ f(x) $ 在  $ x=0 $ 的某邻域内有定义，并且  $ |f(x)| \leq 1 - \cos x $，则  $ f(x) $ 在  $ x=0 $ 处（）.

(A) 极限存在但不连续

(B) 连续但不可导

(C) 可导且  $ f'(0) = 0 $

(D) 可导且  $ f'(0) \neq 0 $

解 应选(C).

可分为三个层次去做题。

第一层次：夹逼准则找极限.

因为  $ 0 \leqslant |f(x)| \leqslant 1 - \cos x $，且  $ \lim_{x \to 0} (1 - \cos x) = 0 $，所以由夹逼准则知  $ \lim_{x \to 0} |f(x)| = 0 $，故  $ \lim_{x \to 0} f(x) = 0 $

第二层次：特殊点找函数值.

将 x=0 代入所给不等式，有  $ |f(0)| \leqslant 1 - \cos 0 = 0 $，所以  $ f(0) = 0 $，故  $ \lim_{x \to 0} f(x) = f(0) $，得  $ f(x) $ 在 x = 0 处连续，且

 $$ \left|f(x)-f(0)\right|=\left|f(x)-0\right|=\left|f(x)\right|\leqslant1-\cos x. $$ 

第三层次：夹逼准则找极限，此时极限是导数的定义。

 $$ 0\leqslant\left|\frac{f(x)-f(0)}{x-0}\right|\leqslant\frac{1-\cos x}{\left|x\right|}. $$ 

因为 $ \lim_{x\to0}\frac{1-\cos x}{|x|}=\lim_{x\to0}\frac{\frac{1}{2}x^{2}}{|x|}=0 $，再次使用夹逼准则，有 $ \lim_{x\to0}\left|\frac{f(x)-f(0)}{x-0}\right|=0 $，也即 $ \lim_{x\to0}\frac{f(x)-f(0)}{x-0}=0 $，故 $ f'(0)=0 $，应选(C).

方法总结  $ f(x) $ 是抽象函数，利用抽象函数和具体函数的关系式，通过具体函数的信息去求抽象函数的点信息.

例 3.4 设函数  $ f(x) = (\mathrm{e}^{x} - 1)(\mathrm{e}^{2x} - 2)\cdots(\mathrm{e}^{nx} - n) $，其中  $ n $ 为正整数，则  $ f'(0) = (\quad) $.

(A)  $ (-1)^{n-1}(n-1)! $

(B)  $ (-1)^n(n-1)! $

(C)  $ (-1)^{n-1}n! $

(D)  $ (-1)^n n! $

解 应选(A).

方法一 利用导数的定义，有

 $$ \begin{aligned}f^{\prime}(0)&=\lim_{x\rightarrow0}\frac{f(x)-f(0)}{x-0}=\lim_{x\rightarrow0}\frac{(\mathrm{e}^{x}-1)(\mathrm{e}^{2x}-2)\cdots(\mathrm{e}^{nx}-n)-0}{x}\\&=\lim_{x\rightarrow0}\frac{\mathrm{e}^{x}-1}{x}\cdot\lim_{x\rightarrow0}\left[(\mathrm{e}^{2x}-2)\cdots(\mathrm{e}^{nx}-n)\right]=(-1)^{n-1}(n-1)!\end{aligned} $$ 

方法二 公式法.

 $$ f^{\prime}(x)=(\mathrm{e}^{x}-1)^{\prime}(\mathrm{e}^{2x}-2)\cdots(\mathrm{e}^{nx}-n)+(\mathrm{e}^{x}-1)(\mathrm{e}^{2x}-2)^{\prime}\cdots(\mathrm{e}^{nx}-n)+\cdots+(\mathrm{e}^{x}-1)(\mathrm{e}^{2x}-2)\cdots(\mathrm{e}^{nx}-n)^{\prime}, $$ 

<div style="text-align: center;"><img src="imgs/img_in_image_box_39_1423_435_1498.jpg" alt="Image" width="38%" /></div>
