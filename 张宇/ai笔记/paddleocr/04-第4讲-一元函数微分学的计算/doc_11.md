但这样算下去，很难找到规律．想到 $ \cos x=\sin\left(x+\frac{\pi}{2}\right) $，则有

 $$ y^{\prime}=(\sin x)^{\prime}=\cos x=\sin\left(x+\frac{\pi}{2}\right), $$ 

 $$ y^{\prime \prime}=\left[\sin\left(x+\frac{\pi}{2}\right)\right]^{\prime}=\cos\left(x+\frac{\pi}{2}\right)=\sin\left(x+\frac{\pi}{2}+\frac{\pi}{2}\right)=\sin\left(x+2\cdot\frac{\pi}{2}\right), $$ 

 $$ y^{m}=\left[\sin\left(x+2\bullet\frac{\pi}{2}\right)\right]^{\prime}=\cos\left(x+2\bullet\frac{\pi}{2}\right)=\sin\left(x+3\bullet\frac{\pi}{2}\right), $$ 

于是

 $$ y^{(n)}=\sin\left(x+n\bullet\frac{\pi}{2}\right), $$ 

即

 $$ \left(\sin x\right)^{\left(n\right)}=\sin\left(x+n\bullet\frac{\pi}{2}\right),n=1,2,\cdots. $$ 

☑ 方法总结 在没有相应的高阶公式情况下，可以逐阶求导，探索规律，写出通项的表达式.

∅公式  $ \left(\sin x\right)' = \cos x $， $ \left(\cos x\right)' = -\sin x $。

## 注 常用高阶导数（n为正整数）：

 $ (\mathrm{e}^{ax+b})^{(n)}=\underline{a}^{n}\mathrm{e}^{ax+b} $;

 $ (\sin(ax+b))^{(n)}=\underline{a}^{n}\sin\left(ax+b+\frac{n\pi}{2}\right) $;

 $ (\cos(ax+b))^{(n)}=\underline{a}^{n}\cos\left(ax+b+\frac{n\pi}{2}\right) $;

 $ (\frac{1}{ax+b})^{(n)}=-(-1)\frac{1}{(ax+b)^{2}}\cdot a $;

 $ (\ln(ax+b))^{(n)}=-(-1)^{n-1}\frac{(n-1)!}{(ax+b)^{n}} $;

 $ (\frac{1}{ax+b})^{(n)}=-(-1)(-2)\cdots(-n)a^{n}\cdot\frac{1}{(ax+b)^{n+1}} $

 $ (\frac{1}{ax+b})^{(n)}=-(-1)^{n}\frac{a^{n}}{(ax+b)^{n+1}} $

考生若能记住这些式子，那是最好的。若记不住，学会推导的方式，在考试中快速计算出来，也是可以的。

例4.15 设  $ y = \frac{1 - x}{1 + x} $，则  $ y^{(n)}(0) = (\quad) $.

(A) $ (-1)^{n}2\cdot n! $ (B) $ -2^{n}\cdot n! $ (C) $ 2^{n}\cdot(n-1)! $ (D) $ -2^{n}\cdot(n-1)! $

♂分析 本题不能直接用常用高阶导数公式，可考虑先转化为有常用高阶导数公式的式子．因