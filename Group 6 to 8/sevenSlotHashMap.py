class sevenSlotHashMap:
    def __init__(self):
        self._arr = [[] for _ in range(7)]
        
    def hash_key(key: str) -> int:
        return sum(ord(char) for char in key) % 7

    def put(self, key: str, value):
        idx = sevenSlotHashMap.hash_key(key)
        for i, kvPair in enumerate(self._arr[idx]):
            if kvPair[0] == key:
                self._arr[idx][i] = (key, value)
                return
        self._arr[idx].append((key, value))

    def get(self, key: str):
        idx = sevenSlotHashMap.hash_key(key)
        for kvPair in self._arr[idx]:
            if kvPair[0] == key:
                return kvPair[1]
        return None

    def delete(self, key):
        idx = sevenSlotHashMap.hash_key(key)
        for i, kvPair in enumerate(self._arr[idx]):
            if kvPair[0] == key:
                del self._arr[idx][i]
                return True
        return False

if __name__ == "__main__":
    sshm = sevenSlotHashMap()
    sshm.put("cat", 3)
    sshm.put("act", 4)
    sshm.put("dog", 7)
    sshm.put("god", 0)
    # sshm.put("cat", 6)
    # print(sshm.get("cat"))
    # sshm.delete("act")
    print(*sshm._arr, sep="\n")