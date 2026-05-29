 $$ \begin{aligned}&\textcircled{7} \begin{cases}\displaystyle\int\frac{1}{\sqrt{x^{2}+a^{2}}}\mathrm{d}x=\ln(x+\sqrt{x^{2}+a^{2}})+C( 常见 a=1),\\\displaystyle\int\frac{1}{\sqrt{x^{2}-a^{2}}}\mathrm{d}x=\ln\left|x+\sqrt{x^{2}-a^{2}}\right|+C(|x|>|a|).\end{cases}\end{aligned} $$ 

8

 $$ \int\frac{1}{x^{2}-a^{2}}\mathrm{d}x=\frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right|+C\left(\int\frac{1}{a^{2}-x^{2}}\mathrm{d}x=\frac{1}{2a}\ln\left|\frac{x+a}{x-a}\right|+C\right) $$ 

 $$ \Rightarrow\int\frac{1}{a^{2}-x^{2}}\mathrm{d}x=-\int\frac{1}{x^{2}-a^{2}}\mathrm{d}x=-\frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right|+C $$ 

 $$ \int\sqrt{a^{2}-x^{2}}\mathrm{d}x=\frac{a^{2}}{2}\arcsin\frac{x}{a}+\frac{x}{2}\sqrt{a^{2}-x^{2}}+C(a>|x|\geq0) $$ 

 $$ =\frac{1}{2a}\ln\left|\frac{x+a}{x-a}\right|+C. $$ 

⑩ $ \int\sin^{2}xdx=\frac{x}{2}-\frac{\sin2x}{4}+C\left(\sin^{2}x=\frac{1-\cos2x}{2}\right) $;——记住2次方即可，3次方不用再记

 $$ \int\cos^{2}x dx=\frac{x}{2}+\frac{\sin2x}{4}+C\left(\cos^{2}x=\frac{1+\cos2x}{2}\right); $$ 

 $$ \int\tan^{2}x\mathrm{d}x=\tan x-x+C(\tan^{2}x=\sec^{2}x-1); $$ 

 $$ \int\cot^{2}x\mathrm{d}x=-\cot x-x+C(\cot^{2}x=\csc^{2}x-1). $$ 

## 不定积分的积分法

<div style="text-align: center;"><img src="imgs/img_in_image_box_814_656_917_763.jpg" alt="Image" width="9%" /></div>


## 凑微分法

 $$  令 g(x)=u $$ 

 $$ \int f[g(x)]g^{\prime}(x)\mathrm{d}x=\int f[g(x)]\mathrm{d}[g(x)]=\int f(u)\mathrm{d}u\xrightarrow{}\longrightarrow 若可以代入基本积分公式 , 则结束 $$ 

注1 当被积函数比较复杂时，拿出一部分放到 d 后面去，若能凑成  $ \int f(u)du $ 的形式，则凑微分成功。比如，

 $$ \int\frac{\ln^{5}x}{x}\mathrm{d}x=\int\ln^{5}x\cdot\frac{1}{x}\mathrm{d}x=\int\ln^{5}x\mathrm{d}(\ln x)=\frac{\ln^{6}x}{6}+C. $$ 

 $$ \int\ln^{5}x\cdot(\ln x)^{\prime}dx $$ 

 $$ f[g(x)]\quad g^{\prime}(x) $$ 

## 放入d后面要熟练

##  $ ^{*} $注2 常用的凑微分公式：

①由于  $ x \, \mathrm{d}x = \frac{1}{2} \mathrm{d}(x^{2}) $，故  $ \int x f(x^{2}) \, \mathrm{d}x = \frac{1}{2} \int f(x^{2}) \, \mathrm{d}(x^{2}) = \frac{1}{2} \int f(u) \, \mathrm{d}u $

②由于  $ \sqrt{x} \, \mathrm{d}x = \frac{2}{3} \mathrm{d}\left(x^{\frac{3}{2}}\right) $，故  $ \int \sqrt{x} f\left(x^{\frac{3}{2}}\right) \, \mathrm{d}x = \frac{2}{3} \int f\left(x^{\frac{3}{2}}\right) \, \mathrm{d}\left(x^{\frac{3}{2}}\right) = \frac{2}{3} \int f(u) \, \mathrm{d}u $