"""
Test for Python-CSP's builtin functions (processes/threads).

Most if not all of the builtins accept two channel arguments: One to
receive the input from, and one to write the output to. After the
writing for an input value is done, the builtin `yield`s and continues
to run.
"""

import unittest

# Make shortcuts. Don't use `from ... import *`, so we can still
#  access both the process and the threading variety
import csp.cspprocess
import csp.cspthread
import csp.builtins as builtins


class TestBuiltinsWithProcesses(unittest.TestCase):
    csp_process = csp.cspprocess

    def setUp(self):
        csp = self.csp_process
        # Get us some channels for later use
        self.spare_channels = [csp.Channel() for i in xrange(3)]

    def tearDown(self):
        # Ignore result
        [channel.poison() for channel in self.spare_channels]

    def producer(self):
        @self.csp_process.process
        def _producer(channel, values):
            for value in values:
                channel.write(value)
        return _producer

    def consumer(self):
        @self.csp_process.process
        def _consumer(channel, reads, result_channel):
            result = []
            for i in xrange(reads):
                result.append(channel.read())
            result_channel.write(result)
        return _consumer

    def feedBuiltin(self, in_data, builtin, args=None, excess_reads=0):
        """Feed the data from `in_data` into the builtin CSPProcess
        (process/thread) and return a sequence of the corresponding
        output values. If `args` isn't `None`, use this tuple as the
        positional arguments to the builtin. If `excess_reads` is
        greater than 0, read this many values after reading output
        values corresponding to the input and include them in the
        returned output data.
        """
        csp = self.csp_process
        in_channel, out_channel, result_channel = self.spare_channels[:3]
        # Use positional arguments if requested
        if args is None:
            called_builtin = builtin(in_channel, out_channel)
        else:
            called_builtin = builtin(in_channel, out_channel, *args)
        parallel_processes = csp.Par(
          called_builtin,
          self.producer()(in_channel, in_data),
          self.consumer()(out_channel, reads=len(in_data)+excess_reads,
                          result_channel=result_channel)
          )
        parallel_processes.start()
        # Collect output data from builtin
#         out_data = []
#         for data_item in in_data:
#             in_channel.write(data_item)
#             out_data.append(out_channel.read())
#         for i in xrange(excess_reads):
#             out_data.append(out_channel.read())
        #return out_data

    def assertListsAlmostEqual(self, list1, list2, msg=None):
        """Compare corresponding list elements with
        `self.assertAlmostEqual` and fail with message `msg` if
        a comparison fails.
        """
        for item1, item2 in zip(list1, list2):
            self.assertAlmostEqual(item1, item2)

    def feedUnaryFloatOperation(self, in_data, expected_out_data, builtin):
        """Test an unary floating point operation `builtin`, for
        example `builtins.Sin`. Check if items in the sequence
        `in_data` have corresponding results in `expected_out_data`.
        """
        out_data = self.feedBuiltin(in_data, builtin)
        self.assertListsAlmostEqual(out_data, expected_out_data)

    def testSin(self):
        in_data = [0.0, 1.0, 4.0, -1.0, -4.0, 10.0]
        expected_data = [0.0, 0.841470984808, -0.756802495308,
                         -0.841470984808, 0.756802495308, -0.544021110889]
        self.feedBuiltin(in_data, builtins.Sin)
        #self.feedUnaryFloatOperation(in_data, expected_data, builtins.Sin)

    def testCos(self):
        in_data = [0.0, 1.0, 4.0, -1.0, -4.0]
        expected_data = [1.0, 0.540302305868, -0.653643620864,
                         0.540302305868, -0.653643620864, -0.839071529076,]
        self.feedUnaryFloatOperation(in_data, expected_data, builtins.Cos)

    def testSucc(self):
        in_data = [0.0, 1.1, 99.123, 1e4, -1.0]
        expected_data = [1.0, 2.1, 100.123, 1e4+1.0, 0.0]
        self.feedUnaryFloatOperation(in_data, expected_data, builtins.Succ)

    def testPred(self):
        in_data = [1.0, 2.1, 100.123, 1e4+1.0, 0.0]
        expected_data = [0.0, 1.1, 99.123, 1e4, -1.0]
        self.feedUnaryFloatOperation(in_data, expected_data, builtins.Pred)

    #XXX Something like this is defined in Python 2.7
    def assertListsEqual(self, list1, list2, msg=None):
        """See `assertListsAlmostEqual`, but compare exactly."""
        for item1, item2 in zip(list1, list2):
            self.assertAlmostEqual(item1, item2)

    def feedUnaryOperation(self, in_data, expected_out_data, builtin,
                           args=None):
        """Test an unary floating point operation `builtin`, for
        example `builtins.Sin`. Check if items in the sequence
        `in_data` have corresponding results in `expected_out_data`.
        If `args` is given and not `None`, use the tuple as the
        positional arguments in the call of `builtin`.
        """
        # `args` is handled appropriately by `feedBuiltin`
        out_data = self.feedBuiltin(in_data, builtin, args)
        self.assertListsEqual(out_data, expected_out_data)

    def testPrefix(self):
        in_data = [1, 2, -3, "a", u"abc", ()]
        expected_data = [7] + in_data
        out_data = self.feedBuiltin(in_data, builtins.Prefix, args=(7,),
                                    excess_reads=1)
        print out_data
        #self.feedUnaryOperation(in_data, expected_data, builtins.Prefix, (7,))



# class TestBuiltinsWithThreads(TestBuiltinsWithProcesses):
#     csp_process = csp.cspthread


if __name__ == '__main__':
    unittest.main(TestBuiltinsWithProcesses, 'testSin')
