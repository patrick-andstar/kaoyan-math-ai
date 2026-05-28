---
type: 基础知识
title: "[[AB=O的思考]]"
tags:
  - 线代
  - 矩阵
  - 秩
aliases:
  - AB=O的思考
---

A - $m \times n$, B - $n \times s$, 如 $AB=O$，则 $r(A)+r(B) \le n$ ^1

另外理解：
1. B 的列向量是 $AX=O$ 的解，[[4-4 基础解系|基础解系]]证明
2. 矩阵 $B$ 的每一列 (非零向量) 均为 $A$ 的属于 $\lambda=0$ 的特征向量.
3. A 的列向量线性相关
4. A 为方阵时，$|A|=0$
5. A 有 0 特征值
6. [[Sylvester不等式|Sylvester不等式]]



**证：**

1. $Ax = 0$ : $n-r(A)$ 个无关的解向量, $\{\beta_1, \beta_2, \ldots, \beta_s\} \subset \{AX = 0 \text{ 解向量}\}$

$$r(\beta_1, \beta_2, \ldots, \beta_s) \leq n-r(A), \quad \therefore \quad r(A) + r(B) \leq n$$

---

**伴随矩阵秩的讨论：**

① 若 $r(A) = n$，则 $|A| \neq 0$，$|A^*| = |A|^{n-1} \neq 0$，$\Rightarrow r(A^*) = n$

② 若 $r(A) = n-1$，由 $AA^* = A^*A = |A|E = O$

③ 若 $r(A) < n-1$，则 $A^* = O$，$r(A^*) = 0$

---

由 ②：$r(A) + r(A^*) \leq n$，即 $(n-1) + r(A^*) \leq n$，故 $r(A^*) \leq 1$

又（因为 $A$ 有 $n-1$ 阶子式不为零）$r(A^*) \geq 1$

因此 $r(A^*) = 1$