# NeetCode Learnings Notes

## Data Structures & Algortithms

**Problem:** anagram-groups

**Pattern:** Canonical Representation

**Key Insight:** By converting each word into a unique signature (e.g., sorted characters or a character frequency count), all anagrams map to the same key and can be grouped directly using a hash map.

**Recognition Signal:** Different inputs should be considered identical after normalization.

---

**Problem:** remove-element

**Pattern:** Two Pointers (Read / Write)

**Key Insight:**  Avoid deleting or shifting elements repeatedly. Instead, use a **write pointer** to overwrite elements that should be kept.

**Recognition Signal:** Filter elements in-place while preserving the remaining values.

---

**Problem:** majority-element

**Pattern:** Boyer–Moore majority vote algorithm

**Key Insight:** If an element appears more than half of times, then it cannot be completely canceled out by all the other elements combined.

**Recognition Signal:** Looking for an element occurring more than half of the time.

