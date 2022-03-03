from collections import OrderedDict
from argparse import Namespace
from .namespace import namespace_to_dict


class DataClass(OrderedDict):
  """
  @flax.struct.dataclass
  class DiffusionOutput(DataClass):
    x_t: jnp.ndarray = None
  """
    def __getitem__(self, key):
        return self.__getattribute__(key)


class ModelConfig(Namespace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def items(self):
        return namespace_to_dict(self).items()

    def __getitem__(self, key):
        return self.__getattribute__(key)
