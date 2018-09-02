#!/usr/bin/env python3


class ClosedHash:
    empty = "          "

    def __init__(self, buckets):
        self.B = buckets
        self.dictionary = []
        self.MAKENULL()
        self.probes = []

    def h(self, x):
        return hash(x) % self.B

    def MAKENULL(self):
        """
        Empties the dictionary
        """
        self.dictionary = []
        for i in range(self.B):
            self.dictionary.append(None)

    def locate(self, x):
        """
        Scans dictionary until either x is found, an empty bucket is found, or has scanned
        the entire table
        :param x: value to search for
        """
        initial = self.h(x)

        # buckets scanned
        scanned = 0

        while (scanned < self.B) and (self.dictionary[(initial + scanned) % self.B] != x) and (
                self.dictionary[(initial + scanned) % self.B]):
            scanned += 1

        self.probes.append(scanned + 1)

        return (initial + scanned) % self.B

    def locate1(self, x):
        """
        Same as locate but stops at deleted
        :param x: value to search for
        """
        initial = self.h(x)

        # buckets scanned
        scanned = 0

        while (scanned < self.B) and (self.dictionary[(initial + scanned) % self.B] != "**********") and (
                self.dictionary[(initial + scanned) % self.B] != x) and (self.dictionary[(initial + scanned) % self.B]):
            scanned += 1

        self.probes.append(scanned + 1)
        return (initial + scanned) % self.B

    def INSERT(self, x):
        """
        Inserts into the dictionary
        :param x: item to insert
        """
        if self.dictionary[self.locate(x)] == x:
            return

        bucket = self.locate1(x)

        if not self.dictionary[bucket] or self.dictionary[bucket] == "**********":
            self.dictionary[bucket] = x

    def DELETE(self, x):
        """
        Deletes item from dictionary
        :param x: Item to delete
        """
        bucket = self.locate(x)

        if self.dictionary[bucket] == x:
            self.dictionary[bucket] = '**********'


def count_probes(probes):
    """
    Counts the amount of probes in probes array
    :param probes: array of probes
    :return: float count
    """
    count = 0
    for n in probes:
        count += n

    return float(count)


if __name__ == "__main__":

    test = []
    for i in range(20):
        test.append(str(i*i))

    print("\n-------- ClosedHash Testing --------\n")

    insert = []
    insertProbes = []

    delete = []
    deleteProbes = []

    bucketCount = []

    for buckets in range(0, 55, 5):
        if buckets == 0:
            buckets += 1

        A = ClosedHash(buckets)

        # Insert
        A.probes = []
        for num in test:
            A.INSERT(num)

        c = count_probes(A.probes)
        insertProbes.append(c)
        insert.append(c / len(A.probes))

        # Delete
        A.probes = []
        for num in test:
            A.DELETE(num)

        c = count_probes(A.probes)
        deleteProbes.append(c)
        delete.append(float(c) / len(A.probes))

        bucketCount.append(buckets)

    print("Test Array")
    print(test)
    print("\nProbes for insert")
    print(insertProbes)
    print("\nProbes for Delete")
    print(deleteProbes)
    print("\nTotal Buckets")
    print(bucketCount)
    print("\nAverage probes for insert")
    print(insert)
    print("\nAverage probes for delete")
    print(delete)

    print("\n-------- Complete --------\n")
