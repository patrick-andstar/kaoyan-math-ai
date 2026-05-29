a. “振荡” 是它的左右函数值的特征，即  $ \rightarrow $  $ \rightarrow $  $ \rightarrow $  $ \rightarrow $ 密集地像矩形块一样无限靠近 y 轴.

<div style="text-align: center;"><img src="imgs/img_in_image_box_505_147_676_274.jpg" alt="Image" width="16%" /></div>


b. “间断”只是在描述上述特征，即 $ \lim_{x\to0}\sin\frac{1}{x} $不存在.

谁叫连续的定义是  $ \lim_{x\to x_0}f(x)=f(x_0) $ 呢，就因为  $ \lim_{x\to0}\sin\frac{1}{x}\neq\sin\frac{1}{x}\bigg|_{x=0} $ （无定义），于是只能叫间断．

即使定义成  $ \begin{cases}\sin\frac{1}{x},&x\neq0,\\0,&x=0,\end{cases} $ 依然是  $ \lim_{x\to0}\sin\frac{1}{x}\neq0 $ ，也只能叫间断．

不过，对于 $ \begin{cases}\sin\frac{1}{x}, & x\neq0,\\0,& x=0\end{cases} $这样的振荡间断点，我们可以说，曲线上的点均是相依相偎的，它

<div style="text-align: center;"><img src="imgs/img_in_image_box_115_675_948_828.jpg" alt="Image" width="80%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_117_838_504_967.jpg" alt="Image" width="37%" /></div>


总之，形如  $ f(x)=\begin{cases}\sin\frac{1}{x}, & x\neq0,\\0, & x=0\end{cases} $ 这样的振荡间断点，没有实际上的“断开”，它们是点点相依相偎的。只是它有一个独特的地方，即无限次振荡，故只能称间断，曰：(无限次) 振荡使得极限不存在而不得不称为间断的点。

还记得“连续函数”必有原函数吗？原函数当然是可导函数。也就是说，一个“点点相依相偎”（连续）的函数，一定有（是）一个“点点相依相偎更近”（可导）的函数求导而得到的。反过来说，一个“点点相依相偎更近”（可导）的函数，求导后，会得到一个“点点相依相偎”（可以理解为靠近程度降低）的函数。于是，不只是连续函数“点点相依相偎”，我们研究得如此细致的“振荡间断函数”也可以“点点相依相偎”啊！故可导函数求导后，可能得到连续函数，也可能得到含振荡间断点的函数，只要这些函数“点点相依相偎”（足够近）就行。

于是，若 $ f(x) $可导，则 $ f'(x) $可能连续，也可能含有振荡间断点。