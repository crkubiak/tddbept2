from wasRun import WasRun
from testCaseTest import TestCaseTest
from testCase import TestCase
# test = TestCase()
# test.run()
print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCase("tearDown").run())
