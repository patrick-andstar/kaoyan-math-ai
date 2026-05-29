逆否命题

(2) 设  $ \sum_{n=1}^{\infty}|u_n| $ 收敛，则  $ \sum_{n=1}^{\infty}u_n $ 收敛；设  $ \sum_{n=1}^{\infty}u_n $ 发散，则  $ \sum_{n=1}^{\infty}|u_n| $ 发散。

(3) 设  $ \sum_{n=1}^{\infty}u_n^2 $ 收敛，则  $ \sum_{n=1}^{\infty}\frac{u_n}{n} $ 绝对收敛（提示： $ \left|\frac{u_n}{n}\right|\leqslant\frac{1}{2}\left(u_n^2+\frac{1}{n^2}\right) $）。

不可以直接用  $ \left|u_n\right|\geqslant u_n $，非项级数不能直接用比较判别法，应使用  $ 2\left|u_n\right|\geqslant u_n+\left|u_n\right|\geqslant0 $，假设  $ \sum_{n=1}^{\infty}u_n $ 收敛，则  $ \sum_{n=1}^{\infty}u_n $ 收敛，矛盾，则假设不成立，原命题成立，即



看到收敛的级数，不要想当然以为是正项的

(4) 设  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \sum_{n=1}^{\infty}|u_{n}| $ 不定（反例： $ \sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n} $ 收敛，但  $ \sum_{n=1}^{\infty}\frac{1}{n} $ 发散）。 $ \sum_{n=1}^{\infty}|u_{n}| $ 发散

(5) 设  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \sum_{n=1}^{\infty}u_{n}^{2} $ 不定（反例： $ \sum_{n=1}^{\infty}(-1)^{n}\frac{1}{\sqrt{n}} $ 收敛，但  $ \sum_{n=1}^{\infty}\frac{1}{n} $ 发散）.

(6) 设  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \sum_{n=1}^{\infty}(-1)^{n}u_{n} $ 不定（反例： $ \sum_{n=1}^{\infty}(-1)^{n}\frac{1}{n} $ 收敛，但  $ \sum_{n=1}^{\infty}\frac{1}{n} $ 发散）.

(7) 设  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \sum_{n=1}^{\infty}(-1)^{n}\frac{u_{n}}{n} $ 不定（反例： $ \sum_{n=2}^{\infty}(-1)^{n}\frac{1}{\ln n} $ 收敛，但  $ \sum_{n=2}^{\infty}\frac{1}{n\ln n} $ 发散）.

(8) 设  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \sum_{n=1}^{\infty}u_{2n} $（偶数项）， $ \sum_{n=1}^{\infty}u_{2n-1} $（奇数项）不定（反例： $ 1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\cdots=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{1}{n} $ 收敛，但是其奇数项和偶数项都发散）.

(9) 设  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \sum_{n=1}^{\infty}(u_{2n-1}+u_{2n}) $ 收敛（收敛级数任意加括号所得的新级数仍收敛，且和不变）.

(10) 设  $ \sum_{n=1}^{\infty} u_{n} $ 收敛，则  $ \sum_{n=1}^{\infty} (u_{2n-1} - u_{2n}) $ 不定（反例： $ u_{1} + u_{2} + u_{3} + u_{4} + u_{5} + u_{6} + \cdots = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \cdots $ 收敛，但  $ 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \cdots $ 发散）.

(11) 设  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \left\{\begin{aligned}&\sum_{n=1}^{\infty}(u_{n}+u_{n+1}) 收敛 \left(\sum_{n=1}^{\infty}u_{n}+\sum_{n=1}^{\infty}u_{n+1} 收敛 \right),\\&\sum_{n=1}^{\infty}(u_{n}-u_{n+1}) 收敛 \left(\sum_{n=1}^{\infty}u_{n}-\sum_{n=1}^{\infty}u_{n+1} 收敛 \right).\end{aligned}\right. $ 结论确实

(12) 设  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，则  $ \sum_{n=1}^{\infty}u_{n}u_{n+1} $ 不定（反例： $ u_{n}=(-1)^{n}\frac{1}{\sqrt{n}},u_{n}u_{n+1}=(-1)^{n}\frac{1}{\sqrt{n}}\cdot(-1)^{n+1}\frac{1}{\sqrt{n+1}}=-\frac{1}{\sqrt{n(n+1)}} $，级数发散）.