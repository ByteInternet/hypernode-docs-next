from unittest import TestCase, mock


class HypernodeTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super(HypernodeTestCase, self).__init__(*args, **kwargs)

    def set_up_patch(self, topatch, themock=None, **kwargs):
        """
        Patch a function or class without having to use
        class or method decorators. This is helpful when
        you want to compose a mock in the setup without
        without having to do the boilerplate of patching,
        adding cleanup and starting the patch. See
        https://docs.python.org/3/library/unittest.mock-examples.html#applying-the-same-patch-to-every-test-method
        This helper is used in most Hypernode projects.
        :param topatch: string The class to patch
        :param themock: optional object to use as mock
        :return: mocked object
        """
        if themock is None:
            themock = mock.Mock()

        if "return_value" in kwargs:
            themock.return_value = kwargs["return_value"]

        patcher = mock.patch(topatch, themock)
        self.addCleanup(patcher.stop)
        return patcher.start()

    def set_up_context_manager_patch(self, topatch, themock=None, **kwargs):
        patcher = self.set_up_patch(topatch, themock=themock, **kwargs)
        patcher.return_value.__exit__ = lambda a, b, c, d: None
        patcher.return_value.__enter__ = lambda x: None
        return patcher
