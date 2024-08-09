import dataclasses as dc


@dc.dataclass(unsafe_hash=True)
class Resource:
    cpu_util: str
    ram_util: str
    gpu_util: str
    gpu_temp: str
