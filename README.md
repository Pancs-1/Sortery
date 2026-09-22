# Sortery 🌌

An ultra-optimized, hybrid data structure library written in Python that merges a **Doubly Linked List** with a **Hash-Mapped Lookup Table** and a **Binary Search Engine**. 

Sortery is designed to ingest highly fragmented, out-of-order data streaming with massive numeric gaps and organize it into a continuous sequential chain in real-time, executing over large volumes without standard brute-force performance bottlenecks.

## 🛠️ The Architecture

Standard sorting algorithms often require sorting the entire dataset from scratch or scanning linearly to position incoming elements. Sortery utilizes a multi-layered approach to handle dynamic data insertion efficiently:

1. **The Presentation Layer (Doubly Linked Nodes):** Data elements exist as discrete node objects scattered in memory, communicating strictly through bidirectional pointers (`.next` and `.prev`). This eliminates the array-shifting overhead during splicing operations.
2. **The Instant-Lookup Table (Hash Map):** A dictionary registers every node upon arrival, mapping raw values to their exact object locations in memory for instantaneous O(1) reference routing.
3. **The Algorithmic Navigator (Binary Search):** To bridge structural gaps between non-consecutive integers without resorting to linear scanning, Sortery triggers an internal binary-splitting search pattern (the classic number-guessing algorithm). This optimizes neighbor identification to logarithmic time scales.

## ⚡ Performance Metric

Sortery eliminates the worst-case scenario O(N²) brute-force lookup loop and maintains stability at scale:

* **Time Complexity (Insertion):** \(O(\log N)\) average case for boundary detection.
* **Extraction Complexity:** O(N) linear step to materialize sequential pointer links.
* **Stress Test Benchmarks:**
  * **1,000 randomized elements:** ~0.0018 seconds
  * **20,000 randomized elements:** ~0.0240 seconds
  * **100,000 highly chaotic elements:** **0.6030 seconds** 🚀

## 💻 Quick Start & Usage

Drop `sortery.py` directly into your workspace and initialize the execution engine:

```python
from sortery import SmartSorter

# Initialize Sortery
sorter = SmartSorter()

# Feed unorganized, fragmented data
messy_stream = [12, 1, 994, 5, 2, 995, 13]
sorter.feed_unorganized_list(messy_stream)

# Extract perfectly ordered chain sequence
clean_output = sorter.get_sorted_list()
print(clean_output) 
# Output: [1, 2, 5, 12, 13, 994, 995]
```

