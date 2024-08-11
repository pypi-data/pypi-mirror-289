from robotkinematicscatalogue.synthesize import *
from robotkinematicscatalogue.inversekinematics.__6DOF.industrialRobot import *

class ABB_IRB_1300_11(industrialRobot):
    
    def __init__(self, gripper=np.diag([-1, -1, 1, 1])):
        
        # Modified Denavit-Hartenberg parameters (DHM)
        DHM = np.array([[   0,          0,          544,        0           ],
                        [   -np.pi/2,   50,         0,          -np.pi/2    ],
                        [   0,          425,        0,          0           ],
                        [   -np.pi/2,   40,         425,        0           ],
                        [   np.pi/2,    0,          0,          0           ],
                        [   -np.pi/2,   0,          90,         np.pi       ]])

        self.alpha = DHM[:,0]
        self.a = DHM[:,1]
        self.d = DHM[:,2]
        self.theta = DHM[:,3]
                                
        # Joint limits provided in degrees and/or millimeters (mm)
        self.jointMax = [180, 130, 65, 230, 130, 242]
        self.jointMin = [-180, -100, -210, -230, -130, -242]

        # Identify inverted joints - joints that rotate counterclockwise in local z-axis frame
        self.inv_joint = [1] * 6
                
        # Identify nullified joints - prior joints that cancel out at specified self.null_joint element
        self.null_joint = [0, 0, 0, 0, 0, 0]

        # Predefined transform matrices used for inverse kinematics
        self.TB0 = np.eye(4)
        self.TB0[2, 3] = self.d[0]
        self.T6W = gripper
        self.T6W[2, 3] = self.d[5]