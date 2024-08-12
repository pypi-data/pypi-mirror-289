from jnius import JavaClass, MetaJavaClass, JavaMultipleMethod, JavaStaticMethod


class Futures(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = 'com/google/common/util/concurrent/Futures'

    immediateFuture = JavaStaticMethod(
        '(Ljava/lang/Object;)'
        'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    immediateVoidFuture = JavaStaticMethod(
        '()Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    immediateFailedFuture = JavaMultipleMethod(
        '(Ljava/lang/Throwable;)'
        'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    immediateCancelledFuture = JavaMultipleMethod(
        '()Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    submit = JavaMultipleMethod([
        (
            '(Ljava/util/concurrent/Callable;'
            'Ljava/util/concurrent/Executor;)'
            'Lcom/google/common/util/concurrent/ListenableFuture;',
            True, False
        ),
        (
            '(Ljava/lang/Runnable;'
            'Ljava/util/concurrent/Executor;)'
            'Lcom/google/common/util/concurrent/ListenableFuture;',
            True, False
        )
    ])

    submitAsync = JavaStaticMethod(
        '(Lcom/google/common/util/concurrent/AsyncCallable;'
        'Ljava/util/concurrent/Executor;)'
        'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    scheduleAsync = JavaStaticMethod(
        '(Lcom/google/common/util/concurrent/AsyncCallable;'
        'JLjava/util/concurrent/TimeUnit;'
        'Ljava/util/concurrent/ScheduledExecutorService;)'
        'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    catching = JavaStaticMethod(
        '(Lcom/google/common/util/concurrent/ListenableFuture;'
        'Ljava/lang/Class;Lcom/google/common/base/Function;'
        'Ljava/util/concurrent/Executor;)'
        'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    catchingAsync = JavaMultipleMethod(
        '(Lcom/google/common/util/concurrent/ListenableFuture;'
        'Ljava/lang/Class;'
        'Lcom/google/common/util/concurrent/AsyncFunction;'
        'Ljava/util/concurrent/Executor;)'
        'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    withTimeout = JavaStaticMethod(
        '(Lcom/google/common/util/concurrent/ListenableFuture;'
        'JLjava/util/concurrent/TimeUnit;'
        'Ljava/util/concurrent/ScheduledExecutorService;)'
        'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    transformAsync = JavaStaticMethod(
        '(Lcom/google/common/util/concurrent/ListenableFuture;'
        'Lcom/google/common/util/concurrent/AsyncFunction;'
        'Ljava/util/concurrent/Executor;)'
        'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    transform = JavaMultipleMethod(
        '(Lcom/google/common/util/concurrent/ListenableFuture;'
        'Lcom/google/common/base/Function;'
        'Ljava/util/concurrent/Executor;)'
        'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    lazyTransform = JavaStaticMethod(
        '(Ljava/util/concurrent/Future;'
        'Lcom/google/common/base/Function;)'
        'Ljava/util/concurrent/Future;'
    )

    allAsList = JavaMultipleMethod([
        (
            '([Lcom/google/common/util/concurrent/ListenableFuture;)'
            'Lcom/google/common/util/concurrent/ListenableFuture;',
            True, False
        ),
        (
            '(Ljava/lang/Iterable;)'
            'Lcom/google/common/util/concurrent/ListenableFuture;',
            True, False
        )
    ])

    whenAllComplete = JavaMultipleMethod([
        (
            '([Lcom/google/common/util/concurrent/ListenableFuture;)'
            'Lcom/google/common/util/concurrent/Futures$FutureCombiner;',
            True, False
        ),
        (
            '(Ljava/lang/Iterable;)'
            'Lcom/google/common/util/concurrent/Futures$FutureCombiner;',
            True, False
        )
    ])

    whenAllSucceed = JavaMultipleMethod([
        (
            '([Lcom/google/common/util/concurrent/ListenableFuture;)'
            'Lcom/google/common/util/concurrent/Futures$FutureCombiner;',
            True, False
        ),
        (
            '(Ljava/lang/Iterable;)'
            'Lcom/google/common/util/concurrent/Futures$FutureCombiner;',
            True, False
        )
    ])

    nonCancellationPropagating = JavaStaticMethod(
            '(Lcom/google/common/util/concurrent/ListenableFuture;)'
            'Lcom/google/common/util/concurrent/ListenableFuture;'
    )

    successfulAsList = JavaMultipleMethod([
        (
            '([Lcom/google/common/util/concurrent/ListenableFuture;)'
            'Lcom/google/common/util/concurrent/ListenableFuture;',
            True, False
        ),
        (
            '(Ljava/lang/Iterable;)'
            'Lcom/google/common/util/concurrent/ListenableFuture;',
            True, False
        )
    ])

    inCompletionOrder = JavaStaticMethod(
        '(Ljava/lang/Iterable;)'
        'Lcom/google/common/collect/ImmutableList;'
    )

    addCallback = JavaStaticMethod(
        '(Lcom/google/common/util/concurrent/ListenableFuture;'
        'Lcom/google/common/util/concurrent/FutureCallback;'
        'Ljava/util/concurrent/Executor;)V'
    )

    getDone = JavaStaticMethod(
        '(Ljava/util/concurrent/Future;)'
        'Ljava/lang/Object;'
     )

    getChecked = JavaMultipleMethod([
        (
            '(Ljava/util/concurrent/Future;'
            'Ljava/lang/Class;)Ljava/lang/Object;',
            True, False
        ),
        (
            '(Ljava/util/concurrent/Future;'
            'Ljava/lang/Class;JLjava/util/concurrent/TimeUnit;)'
            'Ljava/lang/Object;',
            True, False
        )
    ])

    getUnchecked = JavaStaticMethod(
        '(Ljava/util/concurrent/Future;)'
        'Ljava/lang/Object;'
    )
