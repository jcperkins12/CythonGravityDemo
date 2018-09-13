from PurePython import gravity
from Cy0_CompiledPython import gravity_cy0
from Cy1_RestrictTypes import gravity_cy1
from Cy2_RestrictClassVariables import gravity_cy2
from Cy3_cdefFunctions import gravity_cy3
from Cy4_Cdivision import gravity_cy4
from Cy5_NoGIL import gravity_cy5


@profile
def run_python(time_span, n_steps):
    p = gravity.Planet()
    gravity.step_time(p, time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]


print(run_python(100000, 10000000))

@profile
def run_compiled_cython(time_span, n_steps):
    p = gravity_cy0.Planet()
    gravity_cy0.step_time(p, time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]

print(run_compiled_cython(100000, 10000000))

@profile
def run_add_restricted_types(time_span, n_steps):
    p = gravity_cy1.Planet()
    gravity_cy1.step_time(p, time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]

print(run_add_restricted_types(100000, 10000000))

@profile
def run_add_class_restrictions(time_span, n_steps):
    p = gravity_cy2.Planet()
    gravity_cy2.step_time(p, time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]

print(run_add_class_restrictions(100000, 10000000))

@profile
def run_add_function_restrictions(time_span, n_steps):
    p = gravity_cy3.Planet()
    gravity_cy3.step_time(p, time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]

print(run_add_function_restrictions(100000, 10000000))

@profile
def run_add_Cdivision(time_span, n_steps):
    p = gravity_cy4.Planet()
    gravity_cy4.step_time(p, time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]

print(run_add_Cdivision(100000, 10000000))

@profile
def run_nogil(time_span, n_steps):
    p = gravity_cy5.Planet()
    gravity_cy5.step_time(p, time_span, n_steps)
    return [(p.x, p.y, p.z), (p.vx, p.vy, p.vz)]

print(run_nogil(100000, 10000000))
