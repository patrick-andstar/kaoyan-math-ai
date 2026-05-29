 $ \underline{\text{注}}  $这个题目还是蛮难的，从考试的角度看，还是要把这个取整函数搞明白，以前的数学一，大题中考过取整函数，现在就是考的频率不高了，但是一旦出现，都是很有区分度的。命题老师对这种题也是很青睐的。有了这种具体问题，大家才知道这些公式怎么用，对于这些抽象性的，或者是比较困难的理论和方法，一定要有实际的例子作为支撑，把抽象和具体紧密地结合起来，这样对知识的把握会更加的扎实和可靠。

(2) $ “\infty-\infty” $

对于“ $ \infty-\infty $”型未定式，一般有两种思路．

①如果函数中有分母，则通分，将加减法变形为乘除法，以便于使用其他计算工具（比如洛必达法则），见例1.30.

②如果函数中没有分母，则可以通过提取公因式或者作倒代换，出现分母后，再利用通分等恒等变形的方法，将加减法变形为乘除法，见例 1.31.

例1.30 极限  $ \lim_{x\to0}\left[\frac{1}{\ln(1+x)}-\frac{1}{x}\right]= $（ ）.

(A)2 (B) $ \frac{3}{2} $ (C)1 (D) $ \frac{1}{2} $

分析“ $ \infty-\infty $”常见考题： $ \lim_{x\to0}\left(\frac{1}{x}-\frac{1}{0}\right) $.简洁美，统一美.

解 应选(D).

所给极限为“ $ \infty-\infty $”型，先变形，化为“ $ \frac{0}{0} $”型.

方法一 洛必达法则.

 $$ \begin{aligned}&\lim_{x\rightarrow0}\left[\frac{1}{\ln\left(1+x\right)}-\frac{1}{x}\right]=\lim_{x\rightarrow0}\frac{x-\ln\left(1+x\right)}{x\ln\left(1+x\right)}\\=&\lim_{x\rightarrow0}\frac{x-\ln\left(1+x\right)}{x^{2}}=\lim_{x\rightarrow0}\frac{1-\frac{1}{1+x}}{2x}\\=&\lim_{x\rightarrow0}\frac{x}{2x\left(1+x\right)}=\lim_{x\rightarrow0}\frac{1}{2\left(1+x\right)}=\frac{1}{2}.\end{aligned} $$ 

方法二 泰勒公式.

 $$ \begin{aligned} 原式 &=\lim_{x\to0}\frac{x-\ln(1+x)}{x\ln(1+x)}\\&=\lim_{x\to0}\frac{\frac{1}{2}x^{2}}{x^{2}}=\frac{1}{2}\ .\end{aligned} $$ 

故选(D).

方法总结 对于“ $ \infty-\infty $”型的题目，如带分母，常常可以考虑通分。越是复杂和困难的情形，泰勒公式越