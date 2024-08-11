from robotkinematicscatalogue.source import *
from robotkinematicscatalogue.forwardKinematics import *
from robotkinematicscatalogue.trajectoryGeneration import *
from robotkinematicscatalogue.angleSetConventions import *

"""from robotkinematicscatalogue.inversekinematics.__4DOF.deltaRobot3D import *
from robotkinematicscatalogue.inversekinematics.__4DOF.palletizingRobot import *
from robotkinematicscatalogue.inversekinematics.__4DOF.SCARARobot import *
from robotkinematicscatalogue.inversekinematics.__6DOF.sixDOF import *
from robotkinematicscatalogue.inversekinematics.__6DOF.collaborativeRobot import *
from robotkinematicscatalogue.inversekinematics.__6DOF.industrialRobot import *"""

from robotkinematicscatalogue.inversekinematics.ABB import *
from robotkinematicscatalogue.inversekinematics.KUKA import *
from robotkinematicscatalogue.inversekinematics.palletizing import *
from robotkinematicscatalogue.inversekinematics.SCARA import *
from robotkinematicscatalogue.inversekinematics.UniversalRobots import *
from robotkinematicscatalogue.inversekinematics.YASKAWA import *

def printMatrix(TBW, digits=5):
    """
    # Prints array or matrix in a readable format
    """

    # Rounding "ridiculous" near-zero number up to float
    TBW = sym.Matrix(TBW)
    for a in sym.preorder_traversal(TBW):
        if isinstance(a, sym.Float):
            TBW = TBW.subs(a, round(a,digits))

    sym.pprint(TBW)