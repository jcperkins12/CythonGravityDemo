from PurePython import gravity
from Cy0_CompiledPython import gravity_cy0
from Cy1_RestrictTypes import gravity_cy1


@profile
def run_python(time_span, n_steps):
    p = gravity.Planet()
    gravity.step_time(gravity.Planet(), time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]


print(run_python(100000, 10000000))

@profile
def run_cython_0(time_span, n_steps):
    p = gravity_cy0.Planet()
    gravity_cy0.step_time(gravity_cy0.Planet(), time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]

print(run_cython_0(100000, 10000000))

@profile
def run_cython_1(time_span, n_steps):
    p = gravity_cy1.Planet()
    gravity_cy1.step_time(gravity_cy1.Planet(), time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]

print(run_cython_1(100000, 10000000))
