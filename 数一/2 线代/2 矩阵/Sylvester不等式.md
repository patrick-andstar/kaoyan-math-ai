---
type: 基础知识
title: "[[Sylvester不等式]]"
tags:
  - 线代
  - 矩阵
  - 秩
aliases:
  - Sylvester不等式
---
**Sylvester 不等式** 设 $A$ 为 $m \times n$ 阶矩阵，$B$ 为 $n \times m$ 阶矩阵，则 $\boxed{r(AB) \geq r(A) + r(B) - n}$

对 $\begin{pmatrix} A & O \\ E & B \end{pmatrix}$ 作广义初等变换，

$$\begin{pmatrix} A & O \\ E & B \end{pmatrix} \to \begin{pmatrix} O & -AB \\ E & B \end{pmatrix} \to \begin{pmatrix} O & -AB \\ E & O \end{pmatrix}$$

得

$$r(A) + r(B) \leq r\begin{pmatrix} A & O \\ E & B \end{pmatrix} = r\begin{pmatrix} O & -AB \\ E & O \end{pmatrix} = r(AB) + r(E) = r(AB) + n$$

故 $r(AB) \geq r(A) + r(B) - n$。


B 行满秩或者 A 列满秩取等，不一定要都满秩
[[2-8 分块矩阵#分块矩阵的秩]]
[[广义初等变换与初等矩阵]]

1. 考虑分块矩阵 $C = \begin{pmatrix} I_n & B \\ A & 0 \end{pmatrix}$。
2. **方法一：行变换**
   用 $-A$ 乘以第一行块加到第二行块：
   $$ \begin{pmatrix} I_n & B \\ A & 0 \end{pmatrix} \xrightarrow{\text{行变换}} \begin{pmatrix} I_n & B \\ 0 & -AB \end{pmatrix} $$
   由于右边矩阵的左上角是单位阵，其秩为 $r(I_n) + r(-AB) = n + r(AB)$。
   所以 $r(C) = n + r(AB)$。
3. **方法二：列变换**
   用 $-B$ 乘以第一列块加到第二列块：
   $$ C_2 \to C_2 - C_1 B $$
   $$ \begin{pmatrix} I_n & B \\ A & 0 \end{pmatrix} \xrightarrow{\text{列变换}} \begin{pmatrix} I_n & 0 \\ A & -AB \end{pmatrix} $$
4. **整合**
   - 从方法一，我们有 $r(C) = n + r(AB)$。
   - 再结合秩的基本不等式，可推出 $r(AB) \le r(A)$ 与 $r(AB) \le r(B)$ 的老结论。
   - 本卡主要保留原笔记中的分析过程，后续可再整理成更干净的定理卡。

