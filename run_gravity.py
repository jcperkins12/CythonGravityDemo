from PurePython import gravity
from Cy0_CompiledPython import gravity_cy0


@profile
def run_python(time_span, n_steps):
    p = gravity.Planet()
    gravity.step_time(gravity.Planet(), time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]


print(run_python(100, 1000))

@profile
def run_cython_0(time_span, n_steps):
    p = gravity_cy0.Planet()
    gravity_cy0.step_time(gravity.Planet(), time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]

print(run_cython_0(100, 1000))
