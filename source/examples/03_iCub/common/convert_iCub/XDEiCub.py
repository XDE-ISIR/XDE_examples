
"""
This file has been automatically generated to convert iCub model
from arboris-python into XDE.
"""

import lgsm

def get_bodies_data():
    """ Get bodies mass, inertia and displacement from parent frame.
        
    Returns a dictionnary {'body name': (mass, moments_of_inertia, H_parent_body)}.
    """
    return {
            'neck_2': (0.1, [1.47e-05, 1.47e-05, 1.125e-05], lgsm.Displacement([0.0, 0.033, 0.0, 0.5, 0.5, 0.5, 0.5])),
            'l_hip_1': (0.32708, [0.0001226823, 0.0001226823, 0.0002361518], lgsm.Displacement([-0.006, -0.0306, -0.0199, 0.7071067812, -0.7071067812, 0.0, 0.0])),
            'l_hip_2': (1.5304, [0.0010850536, 0.0010850536, 0.0007353572], lgsm.Displacement([0.0, 0.0, -0.0375, 0.5, -0.5, -0.5, 0.5])),
            'neck_1': (0.28252, [0.0001554802, 0.0001554802, 3.17835e-05], lgsm.Displacement([-0.00231, -0.0838517963, 0.0, -0.0, 0.0, 0.0, 1.0])),
            'l_shank': (0.95262, [0.0038379274, 0.0004726186, 0.0038379274], lgsm.Displacement([0.0, -0.1799031226, 0.0, -0.0, 0.0, 1.0, 0.0])),
            'r_hip_2': (1.5304, [0.0010850536, 0.0010850536, 0.0007353572], lgsm.Displacement([0.0, 0.0, 0.0375, 0.5, 0.5, 0.5, 0.5])),
            'r_elbow_1': (0.050798, [2.0319e-06, 2.0319e-06, 2.0319e-06], lgsm.Displacement([-0.0, 0.0, -0.07428, -0.4304593346, 0.4304593346, -0.5609855268, 0.5609855268])),
            'l_arm': (1.1584, [0.0025450048, 0.0025450048, 0.0003915392], lgsm.Displacement([-0.078, 0.0, 0.0, 0.5, 0.5, -0.5, -0.5])),
            'l_ankle_1': (0.14801, [7.11651e-05, 7.11651e-05, 4.44215e-05], lgsm.Displacement([-0.0, -0.1065, 0.0, 0.0, 0.7071067812, 0.7071067812, 0.0])),
            'l_foot': (0.6747, [0.0008119371, 0.0003360683, 0.0007317417], lgsm.Displacement([-0.0047312139, 0.0151082333, 0.0, 0.7049876859, -0.0547024933, 0.7049876859, 0.0547024933])),
            'l_hand': (0.19099, [7.64119e-05, 8.49428e-05, 0.0001430197], lgsm.Displacement([0.0, 0.0345, 0.0, 0.5, 0.5, 0.5, 0.5])),
            'r_hand': (0.19099, [7.64119e-05, 8.49428e-05, 0.0001430197], lgsm.Displacement([0.0, -0.0345, 0.0, 0.5, 0.5, 0.5, 0.5])),
            'chest': (4.12925, [0.0116382114, 0.0089010137, 0.0101058082], lgsm.Displacement([0.1094482037, 0.0, -0.008, 0.5, 0.5, -0.5, 0.5])),
            'r_wrist_1': (0.05, [7.9167e-06, 7.9167e-06, 2.5e-06], lgsm.Displacement([0.0, -0.0, -0.0673, 0.5, 0.5, -0.5, -0.5])),
            'l_shoulder_2': (0.20779, [0.0001070292, 0.0001070292, 9.35055e-05], lgsm.Displacement([0.0, 0.0, 0.0355, 0.5, -0.5, -0.5, 0.5])),
            'l_shoulder_1': (0.48278, [0.0001208559, 0.0001208559, 0.0002319758], lgsm.Displacement([0.0038714793, -0.0338517963, -0.075825711, -0.0, 0.9914448614, 0.0, -0.1305261922])),
            'l_forearm': (0.48774, [0.000845416, 0.000845416, 9.7548e-05], lgsm.Displacement([-0.015, -0.07, 0.0, 0.7071067812, 0.7071067812, -0.0, -0.0])),
            'r_thigh': (2.32246, [0.0139763503, 0.0014723952, 0.013781487], lgsm.Displacement([0.1501968774, 0.0, 0.0, -0.5, 0.5, 0.5, 0.5])),
            'head': (0.78, [0.0019968, 0.0019968, 0.0019968], lgsm.Displacement([0.0825, 0.0, 0.001, 0.5, -0.5, 0.5, -0.5])),
            'r_hip_1': (0.32708, [0.0001226823, 0.0001226823, 0.0002361518], lgsm.Displacement([-0.006, 0.0306, -0.0199, 0.7071067812, -0.7071067812, 0.0, 0.0])),
            'r_foot': (0.6747, [0.0008119371, 0.0003360683, 0.0007317417], lgsm.Displacement([-0.0047312139, 0.0151082333, 0.0, -0.0547024933, 0.7049876859, 0.0547024933, 0.7049876859])),
            'r_ankle_1': (0.14801, [7.11651e-05, 7.11651e-05, 4.44215e-05], lgsm.Displacement([-0.0, -0.1065, -0.0, 0.0, 0.7071067812, 0.7071067812, 0.0])),
            'l_thigh': (2.32246, [0.0139763503, 0.0014723952, 0.013781487], lgsm.Displacement([0.1501968774, -0.0, -0.0, 0.5, -0.5, 0.5, 0.5])),
            'l_elbow_1': (0.050798, [2.0319e-06, 2.0319e-06, 2.0319e-06], lgsm.Displacement([0.0, 0.0, 0.07428, 0.5609855268, -0.5609855268, -0.4304593346, 0.4304593346])),
            'r_shank': (0.95262, [0.0038379274, 0.0004726186, 0.0038379274], lgsm.Displacement([0.0, 0.1799031226, 0.0, 0.0, 0.0, 0.0, 1.0])),
            'waist': (0.20297, [0.0002588413, 0.0002907583, 0.0001066438], lgsm.Displacement([0.006, 0.0, -0.1, 1.0, 0.0, 0.0, 0.0])),
            'lap_belt_2': (0.91179, [0.0009339769, 0.0009339769, 0.0004381151], lgsm.Displacement([0.0431335137, 0.0562856998, 0.0, 0.6532814824, 0.6532814824, 0.2705980501, 0.2705980501])),
            'r_forearm': (0.48774, [0.000845416, 0.000845416, 9.7548e-05], lgsm.Displacement([0.015, 0.07, 0.0, 0.7071067812, 0.7071067812, 0.0, -0.0])),
            'l_wrist_1': (0.05, [7.9167e-06, 7.9167e-06, 2.5e-06], lgsm.Displacement([0.0, 0.0, 0.0673, 0.5, 0.5, -0.5, -0.5])),
            'r_arm': (1.1584, [0.0025450048, 0.0025450048, 0.0003915392], lgsm.Displacement([-0.078, 0.0, -0.0, 0.5, -0.5, 0.5, -0.5])),
            'r_shoulder_1': (0.48278, [0.0001208559, 0.0001208559, 0.0002319758], lgsm.Displacement([0.0038714793, -0.0338517963, 0.075825711, 0.1305261922, -0.0, 0.9914448614, 0.0])),
            'r_shoulder_2': (0.20779, [0.0001070292, 0.0001070292, 9.35055e-05], lgsm.Displacement([0.0, 0.0, -0.0355, 0.5, 0.5, -0.5, -0.5])),
            'lap_belt_1': (3.623, [0.0142217846, 0.0105504779, 0.0060679212], lgsm.Displacement([0.0113, -0.0, 0.0617, 0.6532814824, 0.6532814824, -0.2705980501, 0.2705980501])),
            }


def get_joints_data():
    """ Get joints data.
           
    Returns a dictionnary {'joints name': ('parent body name',
                                           'child body name',
                                           Hinge_center_in_parent_frame,
                                           Hinge_axis_in_parent_frame,
                                           q_min,
                                           q_max,
                                           tau_max)}.
    """
    return {
            'r_wrist_roll': ('r_forearm', 'r_wrist_1', [0.0, 0.0, -0.0673], [-1.0, -0.0, 0.0], -1.1344640138, 0.1745329252, 0.65),
            'r_elbow_yaw': ('r_elbow_1', 'r_forearm', [0.015, 0.0, 0.0], [0.0, -1.0, 0.0], -0.872664626, 0.872664626, 0.45),
            'l_elbow_pitch': ('l_arm', 'l_elbow_1', [0.0, 0.0, 0.07428], [-0.9659258263, 0.2588190451, 0.0], 0.0959931089, 1.8500490071, 20.0),
            'l_elbow_yaw': ('l_elbow_1', 'l_forearm', [-0.015, 0.0, 0.0], [0.0, -1.0, 0.0], -0.872664626, 0.872664626, 0.45),
            'l_shoulder_roll': ('l_shoulder_1', 'l_shoulder_2', [0.0, 0.0, 0.0355], [-1.0, 0.0, 0.0], 0.0, 2.8064894372, 84.0),
            'r_ankle_pitch': ('r_shank', 'r_ankle_1', [-0.0, -0.1065, 0.0], [0.0, 0.0, -1.0], -0.7330382858, 0.3665191429, 24.0),
            'l_hip_pitch': ('waist', 'l_hip_1', [-0.006, -0.0681, -0.0199], [0.0, 1.0, 0.0], -0.7679448709, 2.3038346126, 84.0),
            'l_knee': ('l_thigh', 'l_shank', [0.0, -0.0734031226, 0.0], [-0.0, 0.0, -1.0], -2.181661565, 0.401425728, 30.0),
            'torso_pitch': ('waist', 'lap_belt_1', [-0.006, 0.0, 0.1], [-0.0, -1.0, 0.0], -0.3839724354, 1.4660765717, 36.0),
            'head_yaw': ('neck_2', 'head', [0.0, 0.0, 0.001], [1.0, 0.0, 0.0], -0.9599310886, 0.9599310886, 20.0),
            'l_shoulder_yaw': ('l_shoulder_2', 'l_arm', [0.0, 0.0, 0.0], [-1.0, -0.0, 0.0], -0.6457718232, 1.745329252, 34.0),
            'r_ankle_roll': ('r_ankle_1', 'r_foot', [0.0, 0.0, 0.0], [0.0, -1.0, 0.0], -0.4188790205, 0.4188790205, 11.0),
            'torso_yaw': ('lap_belt_2', 'chest', [0.0, 0.0, -0.008], [-1.0, -0.0, 0.0], -1.0297442587, 1.0297442587, 80.0),
            'l_ankle_roll': ('l_ankle_1', 'l_foot', [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], -0.4188790205, 0.4188790205, 11.0),
            'r_hip_roll': ('r_hip_1', 'r_hip_2', [0.0, 0.0, 0.0375], [1.0, -0.0, 0.0], -2.0769418099, 0.2967059728, 84.0),
            'l_wrist_roll': ('l_forearm', 'l_wrist_1', [0.0, 0.0, 0.0673], [-1.0, -0.0, 0.0], -1.1344640138, 0.1745329252, 0.65),
            'l_hip_yaw': ('l_hip_2', 'l_thigh', [0.0, 0.0, 0.0], [-1.0, 0.0, 0.0], -1.3788101091, 1.3788101091, 40.0),
            'r_wrist_pitch': ('r_wrist_1', 'r_hand', [0.0, 0.0, 0.0], [1.0, -0.0, 0.0], -0.436332313, 0.436332313, 0.65),
            'r_hip_pitch': ('waist', 'r_hip_1', [-0.006, 0.0681, -0.0199], [0.0, 1.0, 0.0], -0.7679448709, 2.3038346126, 84.0),
            'l_ankle_pitch': ('l_shank', 'l_ankle_1', [-0.0, -0.1065, 0.0], [0.0, 0.0, -1.0], -0.7330382858, 0.3665191429, 24.0),
            'r_shoulder_yaw': ('r_shoulder_2', 'r_arm', [0.0, 0.0, 0.0], [1.0, 0.0, 0.0], -0.6457718232, 1.745329252, 34.0),
            'l_hip_roll': ('l_hip_1', 'l_hip_2', [0.0, 0.0, -0.0375], [-1.0, 0.0, 0.0], -2.0769418099, 0.2967059728, 84.0),
            'torso_roll': ('lap_belt_1', 'lap_belt_2', [0.0374766594, 0.061942554, 0.0], [0.7071067812, -0.7071067812, 0.0], -0.6806784083, 0.6806784083, 80.0),
            'r_elbow_pitch': ('r_arm', 'r_elbow_1', [0.0, 0.0, -0.07428], [0.9659258263, -0.2588190451, 0.0], 0.0959931089, 1.8500490071, 20.0),
            'head_roll': ('neck_1', 'neck_2', [0.0, 0.033, 0.0], [1.0, -0.0, 0.0], -1.2217304764, 1.0471975512, 20.0),
            'l_wrist_pitch': ('l_wrist_1', 'l_hand', [0.0, 0.0, 0.0], [1.0, -0.0, 0.0], -0.436332313, 0.436332313, 0.65),
            'r_shoulder_pitch': ('chest', 'r_shoulder_1', [0.0225685672, -0.0338517963, 0.0060472293], [0.2588190451, 0.0, -0.9659258263], -1.6580627894, 0.0872664626, 84.0),
            'r_shoulder_roll': ('r_shoulder_1', 'r_shoulder_2', [0.0, 0.0, -0.0355], [-1.0, -0.0, 0.0], 0.0, 2.8064894372, 84.0),
            'l_shoulder_pitch': ('chest', 'l_shoulder_1', [0.0225685672, -0.0338517963, -0.0060472293], [-0.2588190451, 0.0, -0.9659258263], -1.6580627894, 0.0872664626, 84.0),
            'r_hip_yaw': ('r_hip_2', 'r_thigh', [0.0, 0.0, 0.0], [1.0, -0.0, 0.0], -1.3788101091, 1.3788101091, 40.0),
            'head_pitch': ('chest', 'neck_1', [-0.00231, -0.0838517963, 0.0], [0.0, 0.0, 1.0], -0.6981317008, 0.5235987756, 20.0),
            'r_knee': ('r_thigh', 'r_shank', [0.0, 0.0734031226, 0.0], [0.0, 0.0, 1.0], -2.181661565, 0.401425728, 30.0),
            }


def get_meshes_data():
    """ Get meshes data.
           
    Returns a dictionnary {'body name': [('submesh1 name', H_body_submesh1), ...]}.
    """
    return {
            'neck_2': [
                      ('neck_2_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_forearm': [
                      ('r_forearm_mesh', lgsm.Displacement([0.0, 0.0, 0.074, 0.7071067812, -0.7071067812, 0.0, 0.0])),
                      ('r_forearm_cyl_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'head': [
                      ('head_mesh', lgsm.Displacement([0.0, 0.0, -0.1375, 0.7071067812, 0.0, 0.0, 0.7071067812])),
                      ('head_sphere_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'neck_1': [
                      ('neck_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_shank': [
                      ('l_lowerleg_mesh', lgsm.Displacement([0.0, 0.1065, 0.0, 0.0, 0.0, 0.7071067812, 0.7071067812])),
                      ('l_shank_cyl_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 0.7071067812, 0.7071067812, 0.0, 0.0])),
                         ],
            'l_hip_1': [
                      ('l_hip_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_hip_1': [
                      ('r_hip_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_elbow_1': [
                      ('r_elbow_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_hip_2': [
                      ('l_hip_2_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_arm': [
                      ('l_upperarm_mesh', lgsm.Displacement([0.0, 0.01, 0.062, 0.5, -0.5, 0.5, -0.5])),
                      ('l_arm_cyl_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_ankle_1': [
                      ('r_ankle_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_arm': [
                      ('r_upperarm_mesh', lgsm.Displacement([0.0, 0.01, -0.062, 0.5, -0.5, 0.5, -0.5])),
                      ('r_arm_cyl_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_thigh': [
                      ('l_upperleg_mesh', lgsm.Displacement([0.0, 0.1001968774, 0.0, 0.7071067812, -0.7071067812, -0.0, -0.0])),
                      ('l_thigh_cyl1_mesh', lgsm.Displacement([0.0, 0.0381968774, 0.0, -0.5, 0.5, 0.5, 0.5])),
                      ('l_thigh_cyl2_mesh', lgsm.Displacement([0.0, -0.0738031226, 0.0, 0.7071067812, -0.0, -0.0, -0.7071067812])),
                         ],
            'l_elbow_1': [
                      ('l_elbow_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_ankle_1': [
                      ('l_ankle_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_foot': [
                      ('l_foot_mesh', lgsm.Displacement([0.0, -0.0389735499, -0.0427929897, 0.7049876859, 0.0547024933, 0.0547024933, -0.7049876859])),
                      ('l_foot_cyl_mesh', lgsm.Displacement([0.0, -0.0033068434, 0.0042722421, 0.5371820773, -0.4598210694, -0.4598210694, -0.5371820773])),
                         ],
            'r_shank': [
                      ('r_lowerleg_mesh', lgsm.Displacement([0.0, 0.1065, 0.0, 0.0, 0.0, 0.7071067812, 0.7071067812])),
                      ('r_shank_cyl_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 0.7071067812, 0.7071067812, 0.0, 0.0])),
                         ],
            'waist': [
                      ('waist_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_wrist_1': [
                      ('l_wrist_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_foot': [
                      ('r_foot_mesh', lgsm.Displacement([0.0, 0.0389735499, -0.0427929897, 0.7049876859, -0.0547024933, 0.0547024933, 0.7049876859])),
                      ('r_foot_cyl_mesh', lgsm.Displacement([0.0, 0.0033068434, 0.0042722421, -0.4598210694, 0.5371820773, 0.5371820773, 0.4598210694])),
                         ],
            'l_hand': [
                      ('l_hand_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_hand': [
                      ('r_hand_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_hip_2': [
                      ('r_hip_2_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'chest': [
                      ('torso_mesh', lgsm.Displacement([0.024, -0.0345517963, 0.0, 0.7071067812, 0.7071067812, 0.0, -0.0])),
                      ('chest_cylinder_mesh', lgsm.Displacement([-0.0, 0.0647482037, 0.0, -0.5, 0.5, 0.5, 0.5])),
                         ],
            'r_wrist_1': [
                      ('r_wrist_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_shoulder_2': [
                      ('l_shoulder_2_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_shoulder_1': [
                      ('l_shoulder_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'l_forearm': [
                      ('l_forearm_mesh', lgsm.Displacement([0.0, 0.0, -0.074, 0.0, -0.0, -0.7071067812, 0.7071067812])),
                      ('l_forearm_cyl_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_thigh': [
                      ('r_upperleg_mesh', lgsm.Displacement([0.0, -0.1001968774, 0.0, 0.7071067812, 0.7071067812, -0.0, -0.0])),
                      ('r_thigh_cyl1_mesh', lgsm.Displacement([0.0, -0.0381968774, 0.0, -0.5, 0.5, 0.5, 0.5])),
                      ('r_thigh_cyl2_mesh', lgsm.Displacement([0.0, 0.0738031226, 0.0, 0.7071067812, -0.0, -0.0, -0.7071067812])),
                         ],
            'lap_belt_2': [
                         ],
            'r_shoulder_1': [
                      ('r_shoulder_1_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'r_shoulder_2': [
                      ('r_shoulder_2_mesh', lgsm.Displacement([0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])),
                         ],
            'lap_belt_1': [
                      ('pelvis_mesh', lgsm.Displacement([0.0084852814, 0.0895197185, 0.0, 0.6532814824, -0.6532814824, 0.2705980501, -0.2705980501])),
                         ],
            }


def get_kinematic_tree(joint_damping=1.):
    """ Get kinematic tree as defined in the desc module of XDE.
    """

    bodies_data = get_bodies_data()
    joints_data = get_joints_data()
    
    nodes = {}
    for b, val  in bodies_data.items():
        mass, inertias, H_parent_body = val
        nodes[b] = [b, mass, H_parent_body, [], []]
    
    for j, val in joints_data.items():
        p_name, c_name, V_p_hinge, hinge_axis_in_p, qmin, qmax, tau_max = val
        nodes[c_name][3].append(['hinge', V_p_hinge, hinge_axis_in_p, joint_damping, qmin, qmax, 0])
        nodes[p_name][4].append(nodes[c_name])
    
    return nodes['waist']

