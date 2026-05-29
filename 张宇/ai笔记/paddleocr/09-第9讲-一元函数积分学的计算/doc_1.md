## 基本积分公式

<div style="text-align: center;"><img src="imgs/img_in_image_box_862_253_966_359.jpg" alt="Image" width="10%" /></div>


以下 10 组公式，要牢记.

 $$ \begin{aligned} \textcircled{1} \int x^{k}\mathrm{d}x=\frac{1}{k+1}x^{k+1}+C,k\neq-1;\begin{cases}\displaystyle\int\frac{1}{x^{2}}\mathrm{d}x=-\frac{1}{x}+C,\\\displaystyle\int\frac{1}{\sqrt{x}}\mathrm{d}x=2\sqrt{x}+C.\end{cases}\end{aligned} $$ 

②

 $$ \int\frac{1}{x}\mathrm{d}x=\ln\left|x\right|+C\quad.\longrightarrow(\ln x)^{\prime}=\frac{1}{x} $$ 

③

 $$ \int e^{x}dx=e^{x}+C;\quad\int a^{x}dx=\frac{a^{x}}{\ln a}+C,\quad a>0\text{ 且 }a\neq1\quad\longrightarrow(a^{x})^{\prime}=a^{x}\ln a $$ 

④

 $$ \int\sin x\mathrm{d}x=-\cos x+C;\quad\int\cos x\mathrm{d}x=\sin x+C; $$ 

 $$ \int\tan xdx=-\ln\left|\cos x\right|+C;\quad\int\cot xdx=\ln\left|\sin x\right|+C; $$ 

 $$ \begin{aligned} 角度一：\left(-\ln\left|\cos x\right|\right)^{\prime}=\tan x\Rightarrow\int\tan xdx=-\ln\left|\cos x\right|+C.\end{aligned} $$ 

 $$ \begin{aligned} 角度二 ,\ \int\tan x\mathrm{d}x=&\int\frac{\sin x}{\cos x}\mathrm{d}x=-\int\frac{1}{\cos x}(\cos x)^{\prime}\mathrm{d}x\quad( 凑微分 )\\&\xlongequal{u=\cos x}-\int\frac{1}{u}\mathrm{d}u=-\ln|u|+C=-\ln\left|\cos x\right|+C.\end{aligned} $$ 

 $$ \int\frac{\mathrm{d}x}{\cos x}=\int\sec x\mathrm{d}x=\ln\left|\sec x+\tan x\right|+C\;;\;\star $$ 

 $$ \int\frac{\mathrm{d}x}{\sin x}=\int\csc x\mathrm{d}x=\ln\left|\csc x-\cot x\right|+C $$ 

 $$ \int\sec^{2}x\mathrm{d}x=\tan x+C\;;\quad\int\csc^{2}x\mathrm{d}x=-\cot x+C\;; $$ 

 $$ \int\sec x\tan x\mathrm{d}x=\sec x+C\;;\quad\int\csc x\cot x\mathrm{d}x=-\csc x+C\;. $$ 

 $$ \textcircled{5}\begin{cases}\displaystyle\int\frac{1}{1+x^{2}}\,\mathrm{d}x=\arctan x+C\,,\\\displaystyle\int\frac{1}{a^{2}+x^{2}}\,\mathrm{d}x=\frac{1}{a}\arctan\frac{x}{a}+C(a>0).\end{cases} $$ 

 $$ \textcircled{6}\begin{cases}\displaystyle\int\frac{1}{\sqrt{1-x^{2}}}\,\mathrm{d}x=\arcsin x+C\,,\\\displaystyle\int\frac{1}{\sqrt{a^{2}-x^{2}}}\,\mathrm{d}x=\arcsin\frac{x}{a}+C(a>0).\end{cases} $$ 

 $$ \begin{aligned}\frac{1}{x^{2}+a^{2}}\mathrm{d}x&=\frac{1}{a}\int\frac{1}{1+\left(\frac{x}{a}\right)^{2}}\left(\frac{x}{a}\right)^{\prime}\mathrm{d}x\\&\xlongequal{\frac{x}{a}=u}\frac{1}{a}\int\frac{1}{1+u^{2}}\mathrm{d}u=\frac{1}{a}\arctan u+C\\&=\frac{1}{a}\arctan\frac{x}{a}+C\end{aligned} $$ 