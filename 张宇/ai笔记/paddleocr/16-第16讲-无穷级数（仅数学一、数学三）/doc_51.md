掌握一般项  $ u_{n}=\ln\left[1+\frac{(-1)^{n}}{\sqrt{n}}\right] $ 的阶数，需使用泰勒公式.

解 由泰勒公式得，

 $$ \ln\left[1+\frac{(-1)^{n}}{\sqrt{n}}\right]=\frac{(-1)^{n}}{\sqrt{n}}-\frac{1}{2n}+o\left(\frac{1}{n}\right), $$ 

由比较判别法， $ \lim_{n\to\infty}\frac{\frac{1}{2n}-o\left(\frac{1}{n}\right)}{\frac{1}{n}}=\frac{1}{2} $，而级数 $ \sum_{n=2}^{\infty}\frac{(-1)^{n}}{\sqrt{n}} $是（条件）收敛的，故原级数发散.

16.12 分析  $ \lim_{n\to\infty}\sqrt[n]{|a_n|}=\lim_{n\to\infty}\frac{3+(-1)^n}{\sqrt[n]{n}} $ 不存在.

 $ \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=\lim_{n\to\infty}\frac{\left[3+(-1)^{n+1}\right]^{n+1}}{n+1}\cdot\frac{n}{\left[3+(-1)^n\right]^n}=\lim_{n\to\infty}\frac{\left[3+(-1)^{n+1}\right]^n}{\left[3+(-1)^n\right]^n}\cdot\left[3+(-1)^{n+1}\right]\cdot\frac{n}{n+1} $ 不存在（因为当  $ n $ 为

奇数，且  $ n \to \infty $ 时， $ \frac{n}{n+1} \to 1 $， $ \frac{\left[3+(-1)^{n+1}\right]^n}{\left[3+(-1)^n\right]^n} \to +\infty $， $ 3+(-1)^{n+1} \to 4 $）.

但  $ \lim_{n\to\infty}\sqrt[n]{|a_n|} $ 及  $ \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| $ 都不存在，并不能判定原级数的收敛半径一定不存在.

解 现考虑原级数的奇、偶项级数.

由于  $ a_{n}=\frac{\left[3+(-1)^{n}\right]^{n}}{n}=\begin{cases}\frac{4^{n}}{n}, & n \text{ 为偶数}, \\ \frac{2^{n}}{n}, & n \text{ 为奇数},\end{cases} $ 故原级数的奇、偶项级数分别为  $ \sum_{k=1}^{\infty}\frac{2^{2k-1}}{2k-1}\cdot x^{2k-1} $ 与  $ \sum_{k=1}^{\infty}\frac{4^{2k}}{2k}\cdot x^{2k} $.

①由比值判别法求出级数 $ \sum_{k=1}^{\infty}\frac{2^{2k-1}}{2k-1}\cdot x^{2k-1} $的收敛半径 $ R_{1}=\frac{1}{2} $，级数 $ \sum_{k=1}^{\infty}\frac{4^{2k}}{2k}\cdot x^{2k} $的收敛半径 $ R_{2}=\frac{1}{4} $，则原级数的收敛半径 $ R=\min\{R_{1},R_{2}\}=\frac{1}{4} $。

②当  $ x=\frac{1}{4} $ 时，原级数化为  $ \sum_{n=1}^{\infty}\frac{\left[3+(-1)^{n}\right]^{n}}{n}\cdot\frac{1}{4^{n}} $，且  $ \frac{\left[3+(-1)^{n}\right]^{n}}{n}\cdot\frac{1}{4^{n}}=\begin{cases}\frac{1}{(2k-1)\cdot2^{2k-1}},&n=2k-1,\\\frac{1}{2k},&n=2k.\end{cases} $

由于 $ \sum_{k=1}^{\infty}\frac{1}{(2k-1)\cdot2^{2k-1}} $收敛， $ \sum_{k=1}^{\infty}\frac{1}{2k} $发散，因此 $ \sum_{n=1}^{\infty}\frac{\left[3+(-1)^{n}\right]^{n}}{n}\cdot\frac{1}{4^{n}} $发散.

③当 $ x=-\frac{1}{4} $时，原级数为 $ \sum_{n=1}^{\infty}\frac{\left[3+(-1)^{n}\right]^{n}}{n}\cdot\frac{(-1)^{n}}{4^{n}} $，且