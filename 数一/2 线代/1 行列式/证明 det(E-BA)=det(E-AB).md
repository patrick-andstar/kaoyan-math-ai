---
type: 基础知识
title: "[[证明 det(E-BA)=det(E-AB)]]"
tags:
  - 线代
  - 行列式
  - 证明
aliases:
  - det(E-BA)=det(E-AB)
---

## 证明 $\det(E - AB) = \det(E - BA)$

要证明 $n$ 阶矩阵满足 $\det(E - AB) = \det(E - BA)$，可以通过 **分块矩阵的行列式变换** 或 **特征值关系** 分析，以下是两种核心方法：

### 方法一：分块矩阵的初等变换（最直接）

构造 **分块矩阵**：
$$
M = \begin{pmatrix} E & A \\ B & E \end{pmatrix}
$$

#### 步骤 1：左乘初等分块矩阵，化简下块
左乘初等分块矩阵 $\begin{pmatrix} E & 0 \\ -B & E \end{pmatrix}$（行列式为 $1$，可逆，属于“行初等变换”）：
$$
\begin{pmatrix} E & 0 \\ -B & E \end{pmatrix} M = \begin{pmatrix} E & A \\ 0 & E - BA \end{pmatrix}
$$
该矩阵是 **下三角分块矩阵**，其行列式为对角线分块的行列式乘积：
$$
\det\left(\begin{pmatrix} E & A \\ 0 & E - BA \end{pmatrix}\right) = \det(E) \cdot \det(E - BA) = \det(E - BA)
$$

#### 步骤 2：右乘初等分块矩阵，化简上块
右乘初等分块矩阵 $\begin{pmatrix} E & -A \\ 0 & E \end{pmatrix}$（行列式为 $1$，可逆，属于“列初等变换”）：
$$
M \begin{pmatrix} E & -A \\ 0 & E \end{pmatrix} = \begin{pmatrix} E & 0 \\ B & E - AB \end{pmatrix}
$$
该矩阵是 **上三角分块矩阵**，其行列式为：
$$
\det\left(\begin{pmatrix} E & 0 \\ B & E - AB \end{pmatrix}\right) = \det(E) \cdot \det(E - AB) = \det(E - AB)
$$

#### 步骤 3：行列式相等性
由于 **左乘/右乘行列式为 1 的矩阵不改变原矩阵的行列式**，故：
$$
\det(M) = \det(E - BA) \quad \text{且} \quad \det(M) = \det(E - AB)
$$
因此：
$$
\det(E - AB) = \det(E - BA)
$$

---

### 方法二：特征值的关联（补充理解）
矩阵的行列式是 **所有特征值的乘积**（计重数）。对于 $AB$ 和 $BA$：

1. **非零特征值的一致性**：
   若 $\lambda \neq 0$ 是 $AB$ 的特征值（对应特征向量 $x \neq 0$，即 $ABx = \lambda x$），则令 $y = Bx$，可得 $BAy = B(ABx) = B(\lambda x) = \lambda(Bx) = \lambda y$，故 $\lambda$ 也是 $BA$ 的特征值（对应特征向量 $y = Bx \neq 0$，否则 $ABx = 0 \implies \lambda = 0$，矛盾）。

   反之，$BA$ 的非零特征值也必是 $AB$ 的非零特征值，且重数相同。

2. **零特征值的个数**：
   矩阵的 **秩** 满足 $\text{rank}(AB)$ 和 $\text{rank}(BA)$ 可能不同，但它们的零空间维度满足一定关系，最终可以证明 $AB$ 和 $BA$ 的 **零特征值个数** 相等。一个更直接的结论是，它们的特征多项式满足 $\lambda^n \det(\lambda E - AB) = \lambda^n \det(\lambda E - BA)$，这保证了它们的特征值集合（含重数）是一致的。

3. **行列式的计算**：
   $E - AB$ 的特征值为 $1 - \lambda_i$（$\lambda_i$ 是 $AB$ 的特征值），$E - BA$ 的特征值为 $1 - \mu_j$（$\mu_j$ 是 $BA$ 的特征值）。
   由于 $\lambda_i$ 和 $\mu_j$ 的集合（计重数）完全相同，故 $1 - \lambda_i$ 和 $1 - \mu_j$ 作为集合（计重数）也完全相同，因此它们的乘积相等：
   $$
   \det(E - AB) = \prod (1 - \lambda_i) = \prod (1 - \mu_j) = \det(E - BA)
   $$

---

### 总结
> [!summary]
> - **分块矩阵法** 利用初等变换的行列式不变性，通过构造对称的分块矩阵，将 $\det(E-AB)$ 和 $\det(E-BA)$ 关联到同一矩阵的行列式，简洁明了。
> - **特征值法** 从矩阵特征值的内在关联出发，解释了行列式相等的本质（特征值集合的一致性）。

两种方法均证明：
$$
\boldsymbol{\det(E - AB) = \det(E - BA)}
$$

