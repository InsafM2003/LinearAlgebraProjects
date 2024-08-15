import numpy as np

def rotation_matrix(angle, axis):
    cos_theta = np.cos(angle) 
    sin_theta = np.sin(angle)

    if axis == 'x':
        R = np.array([[1, 0, 0, 0],
                         [0, cos_theta, -sin_theta, 0],
                         [0, sin_theta, cos_theta, 0],
                         [0, 0, 0, 1]])
    elif axis == 'y':
        R = np.array([[cos_theta, 0, sin_theta, 0],
                         [0, 1, 0, 0],
                         [-sin_theta, 0, cos_theta, 0],
                         [0, 0, 0, 1]])
    elif axis == 'z':
        R = np.array([[cos_theta, -sin_theta, 0, 0],
                         [sin_theta, cos_theta, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    return R

def transform_points(T, point):
    point_homogeneous = np.append(point, 1)
    transformed_point = T @ point_homogeneous
    
    return transformed_point[:3]


center = np.array([1, -2, 2])

center_1 = np.array([[1, 0, 0, -center[0]],
                          [0, 1, 0, -center[1]],
                          [0, 0, 1, -center[2]],
                          [0, 0, 0, 1]])

center_2 = np.array([[1, 0, 0, center[0]],
                          [0, 1, 0, center[1]],
                          [0, 0, 1, center[2]],
                          [0, 0, 0, 1]])

rotation_angle = np.radians(30)
rotation_matrix = rotation_matrix(rotation_angle, 'x')

point_to_project = np.array([1, 2, 1])
transformation_matrix = center_2 @ rotation_matrix @ center_1
transformed_point = transform_points(transformation_matrix, point_to_project)

print("Transformation Result:", transformed_point)
