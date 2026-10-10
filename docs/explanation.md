# Exercise 3, worked through

The [transcription](source-extract.md) preserves the exercise and its surrounding
explanation. The derivation below is additional explanation, cross-checked
against [MIT's gauge-transformation and circulation derivation, page 6](https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf).

## 1. What the arrows represent

Equations (8) and (9) describe two **vector potentials**:

\[
\mathbf A=(0,bx,0),\qquad \mathbf A'=(-by,0,0).
\]

For the illustrated choice \(b=1\), the first plot's arrows point upward when
\(x>0\), downward when \(x<0\), and vanish along \(x=0\). Their lengths grow
with \(|x|\). The second plot's arrows point left when \(y>0\), right when
\(y<0\), and vanish along \(y=0\); lengths grow with \(|y|\).

Both fields are independent of \(z\), and their z components vanish. A slice
at \(z=0\) therefore displays all their spatial variation. The final panel
shows the magnetic field separately: circles with dots mean vectors pointing
out of the page, in the positive z direction. Their magnitude is constant.
Negative \(b\) reverses all directions; crosses then represent \(-z\).

## 2. Take the curl of each potential

The x and y components of both curls vanish because \(A_z=0\) and nothing
depends on \(z\). Only the z component can survive:

\[
(\nabla\times\mathbf A)_z
=\frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}.
\]

For Equation (8),

\[
(\nabla\times\mathbf A)_z
=\frac{\partial(bx)}{\partial x}-\frac{\partial 0}{\partial y}
=b.
\]

For Equation (9),

\[
(\nabla\times\mathbf A')_z
=\frac{\partial 0}{\partial x}-\frac{\partial(-by)}{\partial y}
=0-(-b)=b.
\]

Thus, everywhere,

\[
\boxed{\nabla\times\mathbf A=\nabla\times\mathbf A'=(0,0,b).}
\]

## 3. Find the scalar that connects them

The exercise asks for \(\mathbf A'=\mathbf A+\nabla s\), so subtract in that order:

\[
\nabla s=\mathbf A'-\mathbf A=(-by,-bx,0).
\]

Integrating \(\partial s/\partial x=-by\) with respect to \(x\) gives
\(s=-bxy+f(y,z)\). Matching the y component requires
\(\partial f/\partial y=0\), and matching the z component requires
\(\partial f/\partial z=0\). Therefore

\[
\boxed{s(x,y,z)=-bxy+C.}
\]

Checking directly, \(\nabla(-bxy+C)=(-by,-bx,0)\), so adding this gradient to
\((0,bx,0)\) gives \((-by,0,0)\). The arbitrary constant contributes no gradient.
The third plot shows this connecting gradient over scalar contours; the axes
are the exact \(s=0\) contour for the displayed choice \(C=0\).

## 4. Why straight arrows can have curl

Curl measures **local circulation per unit area**. It does not require the
drawn arrows or their field lines to form circles.

Consider either orange square, traversed counterclockwise, with side length
\(L\). In the first potential, its vertical sides each contribute
\(bL^2/2\) to \(\oint\mathbf A\cdot d\boldsymbol\ell\); horizontal sides
contribute zero. In the second potential, the horizontal sides each contribute
\(bL^2/2\); vertical sides contribute zero. Consequently

\[
\oint\mathbf A\cdot d\boldsymbol\ell
=\oint\mathbf A'\cdot d\boldsymbol\ell
=bL^2=\int\mathbf B\cdot d\mathbf S.
\]

Dividing by the square's area gives \(b\) for both. The gradient adds zero
closed-loop circulation: \(\oint\nabla s\cdot d\boldsymbol\ell=0\).

## 5. What the slider means

The slider chooses a dimensionless number \(\lambda\) between 0 and 1:

\[
\mathbf A_\lambda=\mathbf A+\lambda\nabla s
=(-\lambda by,(1-\lambda)bx,0).
\]

At 0 it is Equation (8); at 1 it is Equation (9). At 1/2 it becomes
\(\frac12(-by,bx,0)=\frac12\mathbf B\times\mathbf r\), the symmetric gauge.
For every slider position,

\[
(\nabla\times\mathbf A_\lambda)_z=(1-\lambda)b+\lambda b=b.
\]

The screen changes the mathematical description of the same magnetic field.
Here \(\lambda\) selects a gauge and is spatially constant; it is not a time
coordinate or a simulated physical change. Because the added field is a
gradient,

\[
\nabla\times(\mathbf A+\nabla s)
=\nabla\times\mathbf A+\underbrace{\nabla\times\nabla s}_{0}
=\mathbf B.
\]

This is the screenshot's gauge invariance: the chosen potential changes while
the magnetic field, and hence the magnetic force \(q\mathbf v\times\mathbf B\),
remain the same. These particular functions are smooth on all of space.

The scalar \(s\) is a **gauge function**, not the electric scalar potential
\(\phi\). This example is static and uses time-independent \(s\). The
[general electromagnetic transformation](https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf)
also transforms \(\phi\) by \(-\partial s/\partial t\); that term is zero here.

## Reading the figures honestly

Coordinates, field strength, and vector-potential magnitudes use illustrative
units because the screenshot supplies no numerical scale. The three planar
fields share one arrow scale within each figure and throughout slider motion;
arrows are not normalized individually. The perpendicular B symbols represent
direction and uniformity, and their physical units differ from those of A.
Changing \(b\) and regenerating may change the common arrow scale; use the
labels when comparing separate runs. Numerical checks support the implementation;
the exact derivative calculations above establish the mathematical identity.
