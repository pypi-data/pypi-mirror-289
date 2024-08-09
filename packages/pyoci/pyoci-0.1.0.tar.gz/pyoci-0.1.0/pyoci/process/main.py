from collections.abc import Sequence
from typing import Annotated, Literal

from msgspec import Meta, Struct, field

from pyoci.common import GID, UID, Env
from pyoci.int_types import Int32, Int64, Uint32, Uint64
from pyoci.process.capabilities import Capabilities
from pyoci.process.scheduler import Scheduler

Umask = Uint32


class Rlimit(Struct):
    hard: Uint64
    soft: Uint64
    type: Annotated[str, Meta(pattern="^RLIMIT_[A-Z]+$")]


class IoPriority(Struct, omit_defaults=True):
    class_: Literal["IOPRIO_CLASS_RT", "IOPRIO_CLASS_BE", "IOPRIO_CLASS_IDLE"] = field(name="class")
    priority: Int32 | None = None


class ConsoleSize(Struct):
    height: Uint64
    width: Uint64


class ExecCPUAffinity(Struct, omit_defaults=True):
    initial: Annotated[str, Meta(pattern="^[0-9, -]*$")] | None = None
    final: Annotated[str, Meta(pattern="^[0-9, -]*$")] | None = None


class User(Struct, omit_defaults=True):
    uid: UID | None = None
    gid: GID | None = None
    umask: Umask | None = None
    additionalGids: Sequence[GID] | None = None
    username: str | None = None


class Pids(Struct):
    limit: Int64


class Process(Struct, omit_defaults=True):
    cwd: str
    args: Sequence[str] | None = None
    commandLine: str | None = None
    consoleSize: ConsoleSize | None = None
    env: Env | None = None
    terminal: bool | None = None
    user: User | None = None
    capabilities: Capabilities | None = None
    apparmorProfile: str | None = None
    oomScoreAdj: int | None = None
    selinuxLabel: str | None = None
    ioPriority: IoPriority | None = None
    noNewPrivileges: bool | None = None
    scheduler: Scheduler | None = None
    rlimits: Sequence[Rlimit] | None = None
    execCPUAffinity: ExecCPUAffinity | None = None
