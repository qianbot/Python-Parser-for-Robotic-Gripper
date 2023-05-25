# load conda env with open3d >=0.17.0

import open3d as o3d
import numpy as np

NUM_POINTS = 2048

hithand_np = np.load('hithand_pc.npy')
hithand_pcd = o3d.geometry.PointCloud()
hithand_pcd.points = o3d.utility.Vector3dVector(hithand_np)

ds_pcd = hithand_pcd.farthest_point_down_sample(NUM_POINTS)

o3d.visualization.draw_geometries([ds_pcd])
o3d.io.write_point_cloud('ds_hithand.pcd',ds_pcd)