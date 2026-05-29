性质 3(积分的可加性) 当  $ \widehat{AC} = \widehat{AB} + \widehat{BC} $ 时， $ \int_{\widehat{AC}} F \cdot ds = \int_{\widehat{AB}} F \cdot ds + \int_{\widehat{BC}} F \cdot ds $

→物理背景下

## 注 第二型曲线积分的“对称性”

若 $L$ 为从起点 $A$ 到终点 $B$ 的有向曲线，如图 18-14(a) 所示。由于 $L$ 是有向曲线，故它并不关于 $y$ 轴对称。如图 18-14(a) 中的点 $(x, y)$ 处的 $\mathrm{d}s$ 与点 $(-x, y)$ 处的 $\mathrm{d}s$ 并不对称。细致看来，将两处的 $\mathrm{d}s$ 作水平、垂直分解，就会发现，两处的 $\mathrm{d}x$ 同向，均为 $\mathrm{d}x i$；$\mathrm{d}y$ 反向，分别为 $\mathrm{d}y j$ 与 $-\mathrm{d}y j$。此时，若有力 $F = x^2 y j$ 沿 $L$ 做功，则两处的功的微元分别为 $x^2 y \mathrm{d}y$ 与 $-x^2 y \mathrm{d}y$，加起来即为零，故 $\int_L x^2 y \mathrm{d}y = 0$。这与数量积分（如第一型曲线积分）完全不同。因为若 $f(x, y) = x^2 y$，$L$ 是如图 18-14(b) 所示的关于 $y$ 轴对称的曲线，则 $\int_L f(x, y) \mathrm{d}s = \int_L x^2 y \mathrm{d}s = 2 \int_L x^2 y \mathrm{d}s$。究其原因，数量积分的对称性是基于几何背景的，而向量积分（第二型曲线、曲面积分）没有几何背景，它们是物理问题的数学表达，多了“方向”这个重要因素。所以严格来讲，第二型曲线、曲面积分没有几何上的对称性，而是“在物理概念的基础上，得出数学表达式并确定好方向后，在数量大小上看是否相等”。记住上面这段话，就可以很好地解决问题了。

<div style="text-align: center;"><img src="imgs/img_in_image_box_312_677_487_832.jpg" alt="Image" width="16%" /></div>


<div style="text-align: center;">图 18-14</div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_676_687_861_824.jpg" alt="Image" width="17%" /></div>


<div style="text-align: center;"><img src="imgs/img_in_image_box_160_839_585_953.jpg" alt="Image" width="41%" /></div>


<div style="text-align: center;">第一型曲线积分 可讨论对称性</div>


① dx 方向上，在有物理背景情况下，有向曲线在空间位置（或平面位置）上对称的点处，两段水平位移是一致的，都是 dxi；

AC段：方向朝下↓，且位移为 $ dy(-j) $

② dy 方向上，

CB 段：方向朝上↑，且位移为 dy·j



## ④ 计算

(1) 基本方法——化为定积分。（仅多了一个有向性）

如果平面有向曲线 $L$ 由参数方程 $\begin{cases} x = x(t), \\ y = y(t) \end{cases}$ ($t: \alpha \to \beta$) 给出，其中 $t = \alpha$ 对应着起点 $A, t = \beta$ 对应着终点 $B$，则可以将平面第二型曲线积分化为定积分。如