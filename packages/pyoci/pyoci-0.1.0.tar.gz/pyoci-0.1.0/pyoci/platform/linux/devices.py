from collections.abc import Sequence
from typing import Annotated

from msgspec import Meta, Struct

from pyoci.common import GID, UID
from pyoci.filesystem import FilePath
from pyoci.int_types import Int64, Uint16, Uint64

Major = Annotated[Int64, Meta(description="major device number")]
Minor = Annotated[Int64, Meta(description="minor device number")]

FileMode = Annotated[
    int,
    Meta(description="File permissions mode (typically an octal value)", ge=0, le=512),
]

FileType = Annotated[
    str,
    Meta(description="Type of a block or special character device", pattern="^[cbup]$"),
]


class Device(Struct, omit_defaults=True):
    type: FileType
    path: FilePath
    fileMode: FileMode | None = None
    major: Major | None = None
    minor: Minor | None = None
    uid: UID | None = None
    gid: GID | None = None


class DeviceCgroup(Struct, omit_defaults=True):
    allow: bool
    type: str | None = None
    major: Major | None = None
    minor: Minor | None = None
    access: str | None = None


class BlockIODevice(Struct, omit_defaults=True):
    major: Major
    minor: Minor


class BlockIODeviceThrottle(BlockIODevice):
    rate: Uint64 | None = None


Weight = Uint16


class BlockIODeviceWeight(BlockIODevice):
    weight: Weight | None = None
    leafWeight: Weight | None = None


class BlockIO(Struct, omit_defaults=True):
    weight: Weight | None = None
    leafWeight: Weight | None = None
    throttleReadBpsDevice: Sequence[BlockIODeviceThrottle] | None = None
    throttleWriteBpsDevice: Sequence[BlockIODeviceThrottle] | None = None
    throttleReadIOPSDevice: Sequence[BlockIODeviceThrottle] | None = None
    throttleWriteIOPSDevice: Sequence[BlockIODeviceThrottle] | None = None
    weightDevice: Sequence[BlockIODeviceWeight] | None = None
