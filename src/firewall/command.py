from typing import Dict, Tuple

_command_handler: Dict[str, callable] = {}


def command(name: str) -> callable:
    # 데코레이터 일급 함수
    # -------------
    def decorator(func: callable) -> callable:
        if _command_handler.get(name):
            raise Exception(
                f"The @command decorator should not be applied multiple times."
            )
        # 파라미터로 받은 이름을 키로 사용한다.
        _command_handler[name] = func
        return func

    # -------------
    return decorator


def get_command_handler(cmd: str) -> Tuple[callable, str] | None:
    for prefix in _command_handler:
        if not cmd.startswith(prefix):
            continue
        return _command_handler[prefix], cmd[len(prefix) :].strip()

    return None


async def executeCommand(cmd: str, contoller):
    handler_entry = get_command_handler(cmd)

    if handler_entry is None:
        return None
    command_func, arg = handler_entry
    exec_result = command_func()
    return exec_result
