from enum import Enum
from typing import TypeVar, Callable, Union, Generic, List, Optional

T = TypeVar('T')
K = TypeVar('K')

class ActionType(Enum):
    MAP = 1
    FILTER = 2
    REMOVE = 3
    FOREACH = 4
    REDUCE = 5
    FIND = 6
    COLLECT = 7

ArrayTransformer = Callable[[T], K]
FilterTransformer = Callable[[T], bool]
ForEachTransformer = Callable[[T], None]
ReduceTransformer = Callable[[K, T], K]
Condition = Union[Callable[[T], bool], T]

class StreamInterrupt:
    def __init__(self):
        self.interrupted = False

class Action(Generic[T, K]):
    def __init__(self, type: ActionType, transformer: Union[ArrayTransformer[T, K], FilterTransformer[T], ForEachTransformer[T], ReduceTransformer[K, T], None]):
        self.type = type
        self.transformer = transformer

class __Arachnea(Generic[T]):
    def __init__(self, lst: List[T]):
        self.lst = lst
        self.action_stack: List[Action] = []

    def map(self, transformer: ArrayTransformer[T, K]) -> '__Arachnea[K]':
        self.action_stack.append(Action(ActionType.MAP, transformer))
        return self  # type: ignore

    def filter(self, transformer: FilterTransformer[T]) -> '__Arachnea[T]':
        self.action_stack.append(Action(ActionType.FILTER, transformer))
        return self

    def forEach(self, transformer: ForEachTransformer[T]) -> '__Arachnea[T]':
        self.action_stack.append(Action(ActionType.FOREACH, transformer))
        return self

    def remove(self, condition: Condition) -> '__Arachnea[T]':
        def condition_to_array_transformer(ele: T) -> bool:
            if callable(condition):
                return condition(ele)
            else:
                return ele == condition

        self.action_stack.append(Action(ActionType.REMOVE, condition_to_array_transformer))
        return self

    def action_loop(self, operation: Callable[[T], None], interrupt: StreamInterrupt = StreamInterrupt()):
        index = 0

        while index < len(self.lst):
            if interrupt.interrupted:
                break

            ele = self.lst[index]
            exclude = False

            for action in self.action_stack:
                if action.type == ActionType.MAP:
                    ele = action.transformer(ele)  # type: ignore
                elif action.type == ActionType.FOREACH:
                    action.transformer(ele)  # type: ignore
                elif action.type == ActionType.FILTER:
                    exclude = not action.transformer(ele)  # type: ignore
                elif action.type == ActionType.REMOVE:
                    exclude = action.transformer(ele)  # type: ignore

                    if exclude:
                        self.action_stack.remove(action)
                        break

                if exclude:
                    break

            if not exclude:
                operation(ele)

            index += 1

    def reduce(self, transformer: ReduceTransformer[K, T], initial_value: K) -> K:
        accumulator = initial_value

        def operation(ele: T):
            nonlocal accumulator
            accumulator = transformer(accumulator, ele)

        self.action_loop(operation)
        return accumulator

    def find(self, condition: Condition) -> Optional[T]:
        def condition_to_array_transformer(ele: T) -> bool:
            if callable(condition):
                return condition(ele)
            else:
                return ele == condition

        result = None
        interrupt = StreamInterrupt()

        def operation(ele: T):
            nonlocal result
            if condition_to_array_transformer(ele):
                result = ele
                interrupt.interrupted = True

        self.action_loop(operation, interrupt)
        return result

    def collect(self) -> List[T]:
        result: List[T] = []

        def operation(ele: T):
            result.append(ele)

        self.action_loop(operation)
        return result

def arachnea(lst: List[T]) -> __Arachnea[T]:
    return __Arachnea(lst)
