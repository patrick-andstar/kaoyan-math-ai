考研中，对于无穷级数的敛散性判别，要求掌握的内容比反常积分多

定义 1 设  $ \sum_{n=1}^{\infty}u_{n} $ 为任意项级数，若  $ \sum_{n=1}^{\infty}|u_{n}| $ 收敛，则称  $ \sum_{n=1}^{\infty}u_{n} $ 绝对收敛.

定义 2 设  $ \sum_{n=1}^{\infty}u_{n} $ 为任意项级数，若  $ \sum_{n=1}^{\infty}u_{n} $ 收敛，但  $ \sum_{n=1}^{\infty}|u_{n}| $ 发散，则称  $ \sum_{n=1}^{\infty}u_{n} $ 条件收敛。为收敛程度没那么

注1 再次考查级数  $ \sum_{n=1}^{\infty}(-1)^{n-1}\cdot\frac{1}{n} $，它是条件收敛还是绝对收敛？

解  $ \left|(-1)^{n-1} \cdot \frac{1}{n}\right| = \frac{1}{n} $，且  $ \sum_{n=1}^{\infty} \frac{1}{n} $ 是发散的；而由例 16.14 可知， $ \sum_{n=1}^{\infty} (-1)^{n-1} \cdot \frac{1}{n} $ 是收敛的。故此级数条件收敛。

注2 (1) 若  $ \sum_{n=1}^{\infty}|u_{n}| $ 收敛（即任意项级数  $ \sum_{n=1}^{\infty}u_{n} $ 绝对收敛），则  $ \sum_{n=1}^{\infty}u_{n} $ 必收敛。

引入级数  $ \sum_{n=1}^{\infty}v_{n} $，其一般项  $ \rightarrow $ 挑正项的方法

 $$ \nu_{n}=\frac{1}{2}\frac{(u_{n}+|u_{n}|)}{}=\begin{cases}u_{n},&u_{n}>0,\\ 0,&u_{n}\leqslant0.\end{cases} $$ 

可见级数  $ \sum_{n=1}^{\infty}v_{n} $ 是把级数  $ \sum_{n=1}^{\infty}u_{n} $ 中的负项换成 0 而得到的，也就是级数  $ \sum_{n=1}^{\infty}u_{n} $ 中的全体正项所构成的级数，类似地，令

 $$ w_{n}=\frac{1}{2}(|u_{n}|-u_{n})=\begin{cases}-u_{n},&u_{n}<0,\\0,&u_{n}\geqslant0\end{cases}=\begin{cases}|u_{n}|,&u_{n}<0,\\0,&u_{n}\geqslant0,\end{cases} $$ 

即使不加负的，也收敛

则  $ \sum_{n=1}^{\infty} w_n $ 为级数  $ \sum_{n=1}^{\infty} u_n $ 中全体负项的绝对值所构成的级数。如果级数  $ \sum_{n=1}^{\infty} u_n $ 绝对收敛，那么级数  $ \sum_{n=1}^{\infty} v_n $ 与  $ \sum_{n=1}^{\infty} w_n $ 都收敛；如果级数  $ \sum_{n=1}^{\infty} u_n $ 条件收敛（即  $ \sum_{n=1}^{\infty} u_n $ 收敛，而  $ \sum_{n=1}^{\infty} |u_n| $ 发散），那么级数  $ \sum_{n=1}^{\infty} v_n $ 与  $ \sum_{n=1}^{\infty} w_n $ 都发散。

证明：因  $ 0 \leq \sum_{n=1}^{\infty} v_{n} \leq \sum_{n=1}^{\infty} |u_{n}| $，由  $ \sum_{n=1}^{\infty} |u_{n}| $ 收敛，得  $ \sum_{n=1}^{\infty} v_{n} $ 收敛。

又  $ \sum_{n=1}^{\infty}w_{n}=\sum_{n=1}^{\infty}|u_{n}|-\sum_{n=1}^{\infty}v_{n} $，故  $ \sum_{n=1}^{\infty}w_{n} $ 收敛

因为收敛-收敛=收敛

 $$ \sum_{n=1}^{\infty}v_{n} $$ 

由  $ \sum_{n=1}^{\infty}u_{n}-\sum_{n=1}^{\infty}v_{n}=-\sum_{n=1}^{\infty}w_{n} $，得  $ \sum_{n=1}^{\infty}w_{n} $ 收敛，而  $ \sum_{n=1}^{\infty}|u_{n}|=\sum_{n=1}^{\infty}|v_{n}-w_{n}|=\sum_{n=1}^{\infty}v_{n}+\sum_{n=1}^{\infty}w_{n} $，故  $ \sum_{n=1}^{\infty}|u_{n}| $ 收敛，与题干矛盾，故  $ \sum_{n=1}^{\infty}v_{n} $ 发散再由收敛一发散 = 发散，得  $ \sum_{n=1}^{\infty}w_{n} $ 发散

条件收敛的项和

负项分别拿出来均发

散，条件收敛是由于正

项和负项的相互牵扯才

收敛的，而绝对收敛不

受影响

