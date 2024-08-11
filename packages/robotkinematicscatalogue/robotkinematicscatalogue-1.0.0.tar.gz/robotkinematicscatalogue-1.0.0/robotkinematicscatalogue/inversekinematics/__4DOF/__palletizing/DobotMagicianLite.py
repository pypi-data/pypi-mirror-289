from robotkinematicscatalogue.synthesize import *
from robotkinematicscatalogue.inversekinematics.__4DOF.palletizingRobot import *

class DobotMagicianLite(palletizingRobot):

    def __init__(self, gripper=np.eye(4)):

        # Modified Denavit-Hartenberg parameters (DHM)
        DHM = np.array([[   0,          0,          107,        0           ],
                        [   -np.pi/2,   20,         0,          -np.pi/2    ],
                        [   0,          150,        0,          np.pi/2     ],
                        [   0,          150,        0,          0           ],
                        [   -np.pi/2,   34.720,     15,         np.pi       ]])
        
        self.alpha = DHM[:,0]
        self.a = DHM[:,1]
        self.d = DHM[:,2]
        self.theta = DHM[:,3]

        # Joint limits provided in degrees and/or millimeters (mm)
        self.jointMax = [135, 80, 85, 145]
        self.jointMin = [-135, -5, -10, -145]
                        
        # Identify inverted joints - joints that rotate counterclockwise in local z-axis frame
        self.inv_joint = inv_joint_DEFAULT
        
        # Identify nullified joints - prior joints that cancel out at specified self.null_joint element
        self.null_joint = [0, 0, 1, 1, 0, 0]

        # Predefined transform matrices used for inverse kinematics
        self.TB0 = np.eye(4)
        self.TB0[2, 3] = self.d[0]
        self.T6W = gripper