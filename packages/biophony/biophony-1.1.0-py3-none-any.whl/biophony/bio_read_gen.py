# pylint: disable=missing-module-docstring
# pylint: disable=duplicate-code
import collections.abc
import random
import typing

from .bio_seq import BioSeq
from .bio_read import BioRead
from .elem_seq_gen import ElemSeqGen
from .elements import Elements

class BioReadGen(collections.abc.Iterator[BioRead]):
    """Generator of BioRead objects.

    Generates a series of random BioRead objects.

    Args:
        elements: The set of elements to use.
        quality: The range of characters to use for the quality.
        seqlen: The length of the generated sequence.
        seqid: Sequence ID.
        prefix_id: The prefix to use when generating the ID.
        desc: The description.
        count: The number of BioSeq objects to generate.
    """

    # pylint: disable-next=too-many-arguments
    def __init__(self, elements: Elements | None = None,
                 quality: tuple[str, str] = ("!", "~"),
                 seqlen: int = 1000, prefix_id: str = "chr",
                 desc: str = "", count: int = 1) -> None:
        self._elements = Elements() if elements is None else elements
        self._quality = quality
        self._seqlen = seqlen
        self._prefix_id = prefix_id
        self._desc = desc
        self._count = count

        self._n: int = 0 # Current count

    def __iter__(self) -> typing.Self:
        """Gets the iterator on the reads.

        Returns:
            Itself as an iterator.
        """
        return self

    def _gen_qual(self) -> str:
        return ''.join([chr(random.randint(ord(self._quality[0]),
                                           ord(self._quality[1])))
                        for i in range(self._seqlen)])

    def __next__(self) -> BioRead:
        """Generates the next read.

        Returns:
            A BioRead object.
        """

        if self._n < self._count:
            self._n += 1
            gen = ElemSeqGen(seq_len = self._seqlen, elements = self._elements)
            return BioRead(seq = BioSeq(seqid = f"{self._prefix_id}{self._n}",
                           desc = self._desc, seq = next(gen)),
                           qual = self._gen_qual())

        raise StopIteration
