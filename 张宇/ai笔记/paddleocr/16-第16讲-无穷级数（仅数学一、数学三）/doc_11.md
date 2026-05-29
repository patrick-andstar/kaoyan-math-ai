(2)由例2.11可知 $ \lim_{n\to\infty}\frac{\frac{a_n}{b_n}}{b_n}=\frac{1}{2} $，又级数 $ \sum_{n=1}^{\infty}b_n $收敛，所以级数 $ \sum_{n=1}^{\infty}\frac{a_n}{b_n} $收敛.

(4) 比值判别法（也叫达朗贝尔判别法）.

给出一正项级数  $ \sum_{n=1}^{\infty}u_{n} $，如果  $ \lim_{n\to\infty}\frac{u_{n+1}}{u_{n}}=\rho $，那么

①若  $ \rho<1 $ ，则  $ \sum_{n=1}^{\infty}u_{n} $ 收敛；

②若  $ \rho > 1 $，则  $ \sum_{n=1}^{\infty} u_{n} $ 发散.

<div style="text-align: center;"><img src="imgs/img_in_image_box_803_301_920_477.jpg" alt="Image" width="11%" /></div>


达朗贝尔

(1717—1783)

注 (1) 需要指出，若  $ \rho=1 $，无法用此法判定  $ \sum_{n=1}^{\infty}u_{n} $ 的敛散性。比如对于  $ \sum_{n=1}^{\infty}\frac{1}{n}, u_{n}=\frac{1}{n} $，则  $ \lim_{n\to\infty}\frac{u_{n+1}}{u_{n}}=\lim_{n\to\infty}\frac{\frac{1}{n+1}}{\frac{1}{n}}=\lim_{n\to\infty}\frac{n}{n+1}=1 $；对于  $ \sum_{n=1}^{\infty}\frac{1}{n^{2}}, u_{n}=\frac{1}{n^{2}} $，则  $ \lim_{n\to\infty}\frac{u_{n+1}}{u_{n}}=\lim_{n\to\infty}\frac{\frac{1}{(n+1)^{2}}}{\frac{1}{n^{2}}}=\lim_{n\to\infty}\left(\frac{n}{n+1}\right)^{2}=1 $。你看，前者发散，后者收敛，但都有  $ \rho=1 $。

(2) 由 (1)，若  $ \rho $ 不存在或  $ \rho = 1 $，无法用比值判别法。但若  $ \frac{u_{n+1}}{u_n} < \frac{\rho+1}{2} = k < 1 $，存在  $ N > 0 $，当  $ n > N $ 时， $ u_{n+1} < \frac{\rho+1}{2}u_n = ku_n < k^2u_{n-1} < \cdots < k^{n-N}u_{N+1} = k^nA $，由于  $ \sum_{n=N}^{\infty}k^{n-N}u_{N+1} $ 收敛，则  $ \sum_{n=1}^{\infty}u_n $ 收敛。若  $ \frac{u_{n+1}}{u_n} \geq 1(n > N > 0) $，则  $ \lim_{n \to \infty} u_n $ 不等于 0，不必取极限，就可推知  $ \sum_{n=1}^{\infty}u_n $ 发散。

 $ u_{n+1} \geqslant u_n $，即  $ \{u_n\} $ 为单调不减的正项数列，故  $ \lim_{n \to \infty} u_n \neq 0 $。

例 16.11 设  $ a > 0 $，则下列对级数  $ \sum_{n=1}^{\infty} \frac{a^n n!}{n^n} $ 的敛散性说法正确的是（）.

(A) 当 0 < a < e 时，原级数收敛；当  $ a \geq e $ 时，原级数发散

(B) 当 0 < a < e 时，原级数发散；当  $ a \geq e $ 时，原级数收敛

(C) 当 0 < a < e 时，原级数收敛；当  $ a \geq e $ 时，原级数收敛

①当  $ 0 < a \leq e $ 时，原级数收敛；当 a > e 时，原级数发散.



题目改进方法：

(D) 当 0 < a < e 时，原级数发散；当  $ a \geq e $ 时，原级数发散

②当 0 < a < e 时，原级数收敛；当  $ a \geq e $ 时，原级数发散。



若设计如上两个选项，则在计算过程中，就不得不验证a=e时，级数的敛散性

解 应选(A).