from collections.abc import Mapping, Sequence
from typing import Annotated, Literal

from msgspec import Meta, Struct

from pyoci.common import IDMapping
from pyoci.filesystem import FilePath
from pyoci.int_types import Int64, Uint32, Uint64
from pyoci.platform.linux.devices import BlockIO, Device, DeviceCgroup
from pyoci.platform.linux.seccomp import Seccomp
from pyoci.process.main import Pids


class TimeOffsets(Struct, omit_defaults=True):
    secs: Int64 | None = None
    nanosecs: Uint32 | None = None


class PlatformTimeOffsets(Struct, omit_defaults=True):
    boottime: TimeOffsets | None = None
    monotonic: TimeOffsets | None = None


class IntelRdt(Struct, omit_defaults=True):
    closID: str | None = None
    l3CacheSchema: str | None = None
    memBwSchema: Annotated[str, Meta(pattern="^MB:[^\\n]*$")] | None = None
    enableCMT: bool | None = None
    enableMBM: bool | None = None


class NetworkInterfacePriority(Struct, omit_defaults=True):
    name: str
    priority: Uint32


class Network(Struct, omit_defaults=True):
    classID: Uint32 | None = None
    priorities: Sequence[NetworkInterfacePriority] | None = None


class Memory(Struct, omit_defaults=True):
    kernel: Int64 | None = None
    kernelTCP: Int64 | None = None
    limit: Int64 | None = None
    reservation: Int64 | None = None
    swap: Int64 | None = None
    swappiness: Uint64 | None = None
    disableOOMKiller: bool | None = None
    useHierarchy: bool | None = None
    checkBeforeUpdate: bool | None = None


class HugepageLimit(Struct, omit_defaults=True):
    pageSize: Annotated[str, Meta(pattern="^[1-9][0-9]*[KMG]B$")]
    limit: Uint64


class Cpu(Struct, omit_defaults=True):
    cpus: str | None = None
    mems: str | None = None
    period: Uint64 | None = None
    quota: Int64 | None = None
    burst: Uint64 | None = None
    realtimePeriod: Uint64 | None = None
    realtimeRuntime: Int64 | None = None
    shares: Uint64 | None = None
    idle: Int64 | None = None


class Rdma(Struct, omit_defaults=True):
    hcaHandles: Uint32 | None = None
    hcaObjects: Uint32 | None = None


class Resources(Struct, omit_defaults=True):
    unified: Mapping[str, str] | None = None
    devices: Sequence[DeviceCgroup] | None = None
    pids: Pids | None = None
    blockIO: BlockIO | None = None
    cpu: Cpu | None = None
    hugepageLimits: Sequence[HugepageLimit] | None = None
    memory: Memory | None = None
    network: Network | None = None
    rdma: Mapping[str, Rdma] | None = None


NamespaceType = Literal["mount", "pid", "network", "uts", "ipc", "user", "cgroup", "time"]


class NamespaceReference(Struct, omit_defaults=True):
    type: NamespaceType
    path: FilePath | None = None


RootfsPropagation = Literal["private", "shared", "slave", "unbindable"]


class Personality(Struct, omit_defaults=True):
    domain: Literal["LINUX", "LINUX32"] | None = None
    flags: Sequence[str] | None = None


class Linux(Struct, omit_defaults=True):
    """
    Linux platform-specific configurations
    """

    devices: Sequence[Device] | None = None
    uidMappings: Sequence[IDMapping] | None = None
    gidMappings: Sequence[IDMapping] | None = None
    namespaces: Sequence[NamespaceReference] | None = None
    resources: Resources | None = None
    cgroupsPath: str | None = None
    rootfsPropagation: RootfsPropagation | None = None
    seccomp: Seccomp | None = None
    sysctl: Mapping[str, str] | None = None
    maskedPaths: Sequence[str] | None = None
    readonlyPaths: Sequence[str] | None = None
    mountLabel: str | None = None
    intelRdt: IntelRdt | None = None
    personality: Personality | None = None
    timeOffsets: PlatformTimeOffsets | None = None
