注 这个级数的和是著名的欧拉数 e. 可在  $ e^{x} = \sum_{n=0}^{\infty} \frac{x^{n}}{n!} $ 中，令 x = 1，则有  $ \sum_{n=0}^{\infty} \frac{1}{n!} = e $

(2) 比较判别法.

给出两个正项级数  $ \sum_{n=1}^{\infty}u_{n} $ 和  $ \sum_{n=1}^{\infty}v_{n} $，如果从某项起有  $ u_{n} \leqslant v_{n} $ 成立，则

①若 $ \sum_{n=1}^{\infty}v_{n} $收敛，则 $ \sum_{n=1}^{\infty}u_{n} $也收敛；

②若 $ \sum_{n=1}^{\infty}u_{n} $发散，则 $ \sum_{n=1}^{\infty}v_{n} $也发散.

## 有人通俗地念成：两个正项级数，若大的收敛，则小的必收敛；若小的发散，则大的必发散。对于记忆来讲，这种念法未尝不可。

例 16.4 以下结论，正确的是（）.

(A)  $ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right) $ 收敛， $ \sum_{n=1}^{\infty}\frac{1}{n} $ 收敛

(B)  $ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right) $ 收敛， $ \sum_{n=1}^{\infty}\frac{1}{n} $ 发散

(C)  $ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right) $ 发散， $ \sum_{n=1}^{\infty}\frac{1}{n} $ 收敛

(D)  $ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right) $ 发散， $ \sum_{n=1}^{\infty}\frac{1}{n} $ 发散

解 应选(D).

方法一 当  $ x > 0 $ 时，有  $ x > \ln(1 + x) > 0 $，所以对任意的正整数  $ n $，显然也有  $ \frac{1}{n} > \ln\left(1 + \frac{1}{n}\right) $。我们可

以先研究  $ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right) $ 的敛散性，若发散，可用比较判别法得出结论。

 $$ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right)=\sum_{n=1}^{\infty}\ln\frac{n+1}{n}, $$ 

其部分和

 $$ S_{n}=\ln\frac{2}{1}+\ln\frac{3}{2}+\cdots+\ln\frac{n+1}{n}=(\ln2-\ln1)+(\ln3-\ln2)+\cdots+[\ln(n+1)-\ln n]=\ln(n+1) $$ 

因为  $ \lim_{n\to\infty}S_n=\lim_{n\to\infty}\ln(n+1)=+\infty $，所以  $ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right) $ 发散，根据正项级数的比较判别法，有  $ \sum_{n=1}^{\infty}\frac{1}{n} $ 发散。选 (D).

方法二  $ \sum_{n=1}^{\infty}\ln\left(1+\frac{1}{n}\right) $ 发散，证明方法见例 16.1 的应用.

注1  $ \sum_{n=1}^{\infty}\frac{1}{n}=1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}+\cdots $，这个级数从第二项起，每项都是其左右两个相邻项的调和平均数。所谓数c是数a与数b的调和平均数就是指它们之间满足下面这个式子：