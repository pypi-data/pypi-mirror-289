from jnius import PythonJavaClass, java_method

__all__ = ("FutureCallback",)


class FutureCallback(PythonJavaClass):
    __javainterfaces__ = ["com/google/common/util/concurrent/FutureCallback"]
    __javacontext__ = "app"

    def __init__(self, callback: dict):
        self.callback = callback

    def _callback(self, name, *args):
        func = self.callback.get(name)
        if func:
            return func(*args)

    @java_method("(Ljava/lang/Object;)V")
    def onSuccess(self, obj):
        self._callback("on_success", obj)

    @java_method("(Ljava/lang/Throwable;)V")
    def onFailure(self, throwable):
        self._callback("on_failure", throwable)
