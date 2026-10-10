# Text extracted from the supplied screenshot

Source: [the supplied image](source/exercise-3.png). The screenshot does not show
the book's title, author, or page number; no attribution beyond the image is
inferred. This is a manual transcription of the passages relevant to Exercise 3.
Mathematical typography and line wrapping have been normalized. Blockquotes are
source text; the [worked explanation](explanation.md) is newly written.

## The magnetic field and its vector potential

The screenshot's Equation (5) is

\[
\vec B=\vec\nabla\times\vec A.
\]

The component needed here, from Equation (6), is

\[
B_z=\frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}.
\]

> Suppose \(\vec B\) is given by a vector potential, as in Eq. (5). We can always
> add a gradient to \(\vec A\) to define a new vector potential without changing
> \(\vec B\). The reason is that the curl of a gradient is always zero. Thus if two
> vector potentials are related by

\[
\vec A'=\vec A+\nabla s
\]

> for some scalar \(s\), then they produce identical magnetic fields and cannot
> be distinguished by any experiment.

## The example: Equations (7), (8), and (9)

> Let's consider an example of a magnetic field and its associated vector
> potential. The simplest case is a uniform magnetic field pointing, say, along
> the z axis.

Equation (7):

\[
B_x=0,\qquad B_y=0,\qquad B_z=b,
\]

> where \(b\) is a number representing the strength of the field. Now define a
> vector potential by

Equation (8):

\[
A_x=0,\qquad A_y=bx,\qquad A_z=0.
\]

> When the curl of \(\vec A\) is computed, there is only one term, namely
> \(\partial A_y/\partial x=b\). Thus the only component of the magnetic field is
> the z component, and it has value \(b\).

> Now, there is something funny about Equations (8). The uniform magnetic field
> seems to be completely symmetric with respect to rotations in the x, y plane.
> But the vector potential has only a y component.

> However, we could have used a different vector potential \(\vec A'\)—one with
> only an x component—to generate the very same magnetic field:

Equation (9):

\[
A'_x=-by,\qquad A'_y=0,\qquad A'_z=0.
\]

## Exercise 3

> **Exercise 3: Show that the two vector potentials in Equations (8) and
> Equations (9) both give the same uniform magnetic field. This means that the
> two differ by a gradient. Find the scalar whose gradient, when added to
> Equations (8), gives Equations (9).**

## What the screenshot calls a gauge transformation

> The operation of changing from one vector potential to another to describe the
> same magnetic field has a name. It is called a *gauge transformation*. Why
> “gauge”? It's a historical glitch. At one time it was wrongly thought to reflect
> ambiguities in gauging lengths at different locations.

> If the vector potential is ambiguous but the magnetic field quite definite,
> why bother with the vector potential at all? The answer is that without it, we
> could not express the principle of stationary action, or the Lagrangian,
> Hamiltonian, and Poisson formulations of mechanics for particles in magnetic
> fields. It's a weird situation. The physical facts are *gauge invariant*, but
> the formalism requires us to choose a gauge (a particular choice of vector
> potential).
