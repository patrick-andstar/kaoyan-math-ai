(C) N < M < 1

(D)  $ 1 < M < N $

♀分析 考查复合函数 $ f[g(x)] $

涉及知识点： $ \int_{0}^{\frac{\pi}{2}}f(\sin x)dx=\int_{0}^{\frac{\pi}{2}}f(\cos x)dx $

令  $ x = \frac{\pi}{2} - t $，则有  $ \int_{0}^{\frac{\pi}{2}} f(\sin x) \, dx = \int_{0}^{\frac{\pi}{2}} f(\cos t) \, dt $。

 $$  积分与字母无关 \quad\int_{0}^{\frac{\pi}{2}}f(\cos x)dx $$ 

## 解 应选(A)

 $ \sin(\sin x), \cos(\cos x) $ 均在  $ \left[0, \frac{\pi}{2}\right] $ 上连续，由  $ \sin x \leqslant x $ 知  $ \sin(\sin x) \leqslant \sin x $，且  $ \sin(\sin x) \neq \sin x $  $ \left(x \in \left[0, \frac{\pi}{2}\right]\right) $，故

 $ \int_{0}^{\frac{\pi}{2}}\sin(\sin x)dx<\int_{0}^{\frac{\pi}{2}}\sin xdx=1 $，即M<1。

又

 $ \int_{0}^{\frac{\pi}{2}}\cos(\cos x)dx $ 令  $ x=\frac{\pi}{2}-t $

 $ \int_{0}^{\frac{\pi}{2}}\cos(\sin t)dt>\int_{0}^{\frac{\pi}{2}}\cos tdt=1 $ ，即 N>1 ，



因此选(A).

→本质是一个由定积分定义的函数.

## 三 变限积分

<div style="text-align: center;"><img src="imgs/img_in_image_box_827_721_931_828.jpg" alt="Image" width="10%" /></div>


## 1 概念

当x在 $ [a,b] $上变动时，对应于每一个x值，积分 $ \int_{a}^{x}f(t)dt $都有一个确定的值，因此 $ \int_{a}^{x}f(t)dt $是一个关于x的函数，记作

 $$ F(x)=\int_{a}^{x}f(t)\mathrm{d}t(a\leqslant x\leqslant b), $$ 

称函数  $ F(x) $ 为变上限的定积分。同理可以定义变下限的定积分和  $ \underline{\text{上、下限都变化的定积分}} $，这些都称为变限积分。事实上，变限积分就是定积分的推广。

 $$  如 \int_{x^{2}}^{e^{x}}f(t)\mathrm{d}t $$ 

## 2 性质

(1) 函数  $ f(x) $ 在  $ I $ 上可积，则函数  $ F(x) = \int_a^x f(t) \, dt $ 在  $ I $ 上连续。 $ f(x) $ 可导  $ \Rightarrow $ 连续  $ \Rightarrow $ 可积  $ \Rightarrow $ 有界

 $ F(x) $ 若存在，则其一定连续．与  $ f(x) $ 作区分： $ f(x) $ 存在但其并不一定连续．