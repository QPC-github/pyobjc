
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIPlugIn (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(CIPlugIn.loadPlugIn_allowNonExecutable_, 1)

if __name__ == "__main__":
    main()
