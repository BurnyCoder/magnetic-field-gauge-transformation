# Gauge transformation showcase

Different vector potentials can describe the same magnetic field. This showcase
makes that freedom visible: the potential arrows change as a gauge is selected,
while their curl and the magnetic field remain fixed.

The [reference passages](reference-text.md) contain the quoted text. The
step-by-step derivation below is added explanation, cross-checked against
[MIT's gauge-transformation and circulation derivation, page 6](https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf).

## 1. What the arrows represent

For a constant, signed parameter \(b\), consider two **vector potentials**:

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
out of the page, in the positive z direction. The magnetic-field magnitude is
\(|b|\); \(b\) is its signed z component. Negative \(b\) reverses all
directions; crosses then represent \(-z\). At \(b=0\), all three plotted
planar fields and the magnetic field vanish.

## 2. Take the curl of each potential

The x and y components of both curls vanish because \(A_z=0\) and nothing
depends on \(z\). Only the z component can survive:

\[
(\nabla\times\mathbf A)_z
=\frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}.
\]

For the first potential,

\[
(\nabla\times\mathbf A)_z
=\frac{\partial(bx)}{\partial x}-\frac{\partial 0}{\partial y}
=b.
\]

For the second potential,

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

To write \(\mathbf A'=\mathbf A+\nabla s\), subtract in that order:

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
The third plot shows this connecting gradient over scalar contours. For
\(b\ne0\) and the displayed choice \(C=0\), the exact \(s=0\) contour
is the pair of coordinate axes. At \(b=0\), the scalar is constant,
\(s=C\); it is zero throughout the plane only for the displayed choice \(C=0\).

## 4. Why straight arrows can have curl

The z component of curl is **counterclockwise circulation per unit area** in
the limit of a shrinking xy-plane loop, viewed from positive z. It does not
require the drawn arrows or their field lines to form circles.

Consider either orange square, centered at the origin with sides parallel to
the axes and side length \(L\). Traverse it counterclockwise as viewed from
positive z. For the first potential, the right side has \(A_y=bL/2\) and is
traversed upward, contributing \(bL^2/2\). On the left side both \(A_y\) and
the direction of travel reverse, giving another \(bL^2/2\). The horizontal
sides contribute zero. For the second potential, the bottom side has
\(A'_x=bL/2\) and is traversed rightward; the top side has
\(A'_x=-bL/2\) and is traversed leftward. Each contributes \(bL^2/2\), while
the vertical sides contribute zero. Consequently

\[
\oint\mathbf A\cdot d\boldsymbol\ell
=\oint\mathbf A'\cdot d\boldsymbol\ell
=bL^2=\int\mathbf B\cdot d\mathbf S.
\]

Dividing by the square's area gives \(b\) for both. Here the curl is constant,
so this is exact at any square size. Moving the square can change the individual
side contributions, but the total remains \(bL^2\). The gradient adds zero
closed-loop circulation: \(\oint\nabla s\cdot d\boldsymbol\ell=0\), because
the loop returns to the same value of the single-valued function \(s\).

## 5. What the slider means

The slider chooses a dimensionless number \(\lambda\) between 0 and 1:

\[
\mathbf A_\lambda=\mathbf A+\lambda\nabla s
=(-\lambda by,(1-\lambda)bx,0).
\]

At 0 it is the first potential; at 1 it is the second. At 1/2 it becomes
\(\frac12(-by,bx,0)=\frac12\mathbf B\times\mathbf r\), where
\(\mathbf r=(x,y,z)\). This is the [symmetric gauge](https://www.damtp.cam.ac.uk/user/tong/aqm/solid1.pdf),
which is rotationally symmetric about the z axis through the origin.
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

The curl of the gradient vanishes because the mixed second derivatives of
\(s\) agree. These particular functions are smooth and single-valued on all
of space, and we have constructed their connecting scalar explicitly.

This is gauge invariance: the chosen potential changes while the magnetic
field, and hence the magnetic force \(q\mathbf v\times\mathbf B\) on a
particle with the same charge and velocity, remain the same.

The scalar \(s\) is a **gauge function**, not the electric scalar potential
\(\phi\). This showcase is static and uses time-independent \(s\). In SI
conventions, the [general electromagnetic transformation](https://web.mit.edu/8.286/www/quiz22/q3sols-euf22.pdf)
is \(\mathbf A'=\mathbf A+\nabla s\) together with
\(\phi'=\phi-\partial s/\partial t\), preserving both electric and magnetic
fields. Here \(\partial s/\partial t=0\), so \(\phi\) remains unchanged.
The magnetic field alone does not determine the electric field, even in a
static situation: \(\mathbf E=-\nabla\phi\) can differ if \(\phi\) is
changed independently. In this showcase, \(\phi\) is held fixed and every
potential is time-independent, so the gauge change preserves both fields.

## Reading the figures honestly

Coordinates, field strength, and vector-potential magnitudes use illustrative
units; the default is \(b=1\), \(z=0\), and \(x,y\in[-2,2]\). The three planar
fields share one arrow scale within each figure and throughout slider motion;
arrows are not normalized individually. The perpendicular B symbols represent
direction and uniformity, and their sizes do not encode magnitude. If length
has unit \(L_0\) and magnetic field has unit \(B_0\), vector potential has
unit \(B_0L_0\) and the gauge function has unit \(B_0L_0^2\).
Changing \(b\) and regenerating may change the common arrow scale; use the
labels when comparing separate runs. Numerical checks support the implementation;
the exact derivative calculations above establish the mathematical identity.
