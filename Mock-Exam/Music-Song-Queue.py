class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Song:
    def __init__(self, name: str, genre: str, duration: int):
        self.name = name
        self.genre = genre
        self.duration = duration

    def showinfo(self):
        return f"{self.name} <|> {self.genre} <|> {self.duration // 60}.{self.duration % 60:02}"

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def is_empty(self):
        return self.top is None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.undo_stack = LinkedListStack()

    def enqueue(self, song: Song):
        temp = self.head
        state = LinkedListStack()
        while temp:
            state.push(temp.data)
            temp = temp.next
        self.undo_stack.push(state)
        new_node = Node(song)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        temp = self.head
        state = LinkedListStack()
        while temp:
            state.push(temp.data)
            temp = temp.next
        self.undo_stack.push(state)
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return temp.data

    def isEmpty(self):
        return self.head is None

    def peek(self):
        return None if self.isEmpty() else self.head.data

    def show_Queue(self):
        temp = self.head
        index = 1
        while temp:
            duration = f"{temp.data.duration // 60}.{temp.data.duration % 60:02}"
            print(f"Queue#{index} {temp.data.name} <|> {temp.data.genre} <|> {duration}")
            temp = temp.next
            index += 1

    def groupSong(self):
        temp = self.head
        genre = {}
        while temp:
            genre.setdefault(temp.data.genre, []).append(temp.data.name)
            temp = temp.next
        for key, names in genre.items():
            print(f"{key}: {' | '.join(names)}")

    def rev_queue(self):
        temp = self.head
        state = LinkedListStack()
        while temp:
            state.push(temp.data)
            temp = temp.next
        self.undo_stack.push(state)

        temp = self.head
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        self.head, self.tail = self.tail, self.head

    def removeSong(self, name: str):
        temp = self.head
        state = LinkedListStack()
        while temp:
            state.push(temp.data)
            temp = temp.next
        self.undo_stack.push(state)

        temp = self.head
        while temp:
            if temp.data.name == name:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev
                return
            temp = temp.next
        if self.head is None:
            print("Queue is empty!")
        else:
            print(f"Can not Delete! {name} is not exist")

    def undo(self):
        if self.undo_stack.is_empty():
            print("No undo available.")
            return

        state = self.undo_stack.pop()
        self.head = self.tail = None
        while not state.is_empty():
            song = state.pop()
            self.enqueue(song)

def main():
    music_queue = Queue()
    while True:
        command = input()
        if command.startswith("enqueue:"):
            _, details = command.split(":", 1)
            name, genre, duration = details.split("|")
            music_queue.enqueue(Song(name.strip(), genre.strip(), int(duration.strip())))
        elif command.startswith("dequeue:"):
            song = music_queue.dequeue()
            if song:
                duration = f"{song.duration // 60}.{song.duration % 60:02}"
                print(f"Dequeue item: {song.name} <|> {song.genre} <|> {duration}")
        elif command.startswith("showQueue:"):
            temp = music_queue.head
            index = 1
            while temp:
                duration = f"{temp.data.duration // 60}.{temp.data.duration % 60:02}"
                print(f"Queue#{index} {temp.data.name} <|> {temp.data.genre} <|> {duration}")
                temp = temp.next
                index += 1
        elif command.startswith("groupSong:"):
            music_queue.groupSong()
        elif command.startswith("reverseQueue:"):
            music_queue.rev_queue()
        elif command.startswith("removeSong:"):
            _, name = command.split(":", 1)
            music_queue.removeSong(name.strip())
        elif command.startswith("undo:"):
            music_queue.undo()
        elif command == "End":
            break
        else:
            print("Invalid command")

main()