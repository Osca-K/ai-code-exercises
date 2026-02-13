# Performance Optimization: Python Product Combination Finder

## 1. Performance Issue Description

The function `find_product_combinations` finds all pairs of products whose combined price is within a target range. With 5,000+ products, the function takes 20–30 seconds to run, which is too slow for a user-facing web application.

## 2. Bottleneck Analysis

- The function uses two nested loops over the product list, resulting in O(n^2) time complexity.
- For each pair, it checks for duplicates by scanning the `results` list with a generator expression, which is O(n) per check.
- For 5,000 products, this results in ~25 million iterations and many duplicate checks.

## 3. Suggested Optimizations

### A. Avoid Duplicate Pairs Efficiently
- Use a set to track seen product ID pairs (e.g., frozenset of IDs) instead of scanning the results list.

### B. Reduce Redundant Comparisons
- Only consider each unique pair once by iterating `j` from `i+1` instead of all `j`.

### C. Use List Comprehensions and Built-in Functions
- Use more efficient data structures and comprehensions where possible.

### D. Example Optimized Code
```python
def find_product_combinations_optimized(products, target_price, price_margin=10):
    results = []
    seen_pairs = set()
    n = len(products)
    for i in range(n):
        for j in range(i + 1, n):  # Only unique pairs
            product1 = products[i]
            product2 = products[j]
            combined_price = product1['price'] + product2['price']
            if (target_price - price_margin) <= combined_price <= (target_price + price_margin):
                pair_ids = frozenset([product1['id'], product2['id']])
                if pair_ids not in seen_pairs:
                    results.append({
                        'product1': product1,
                        'product2': product2,
                        'combined_price': combined_price,
                        'price_difference': abs(target_price - combined_price)
                    })
                    seen_pairs.add(pair_ids)
    results.sort(key=lambda x: x['price_difference'])
    return results
```

## 4. Expected Results
- Time complexity reduced from O(n^2 * n) to O(n^2) with much less overhead per pair.
- For 5,000 products, this should reduce execution time from 20–30 seconds to under 2 seconds (depending on hardware).

## 5. Key Learnings
- Always avoid unnecessary nested loops and repeated work in performance-critical code.
- Use sets or dictionaries for fast membership checks instead of scanning lists.
- Consider algorithmic improvements (unique pairs, early exits) before micro-optimizations.
- Profile code to identify true bottlenecks before optimizing.

---

**Context:** This optimization is for a product recommendation feature in an e-commerce app, where user experience depends on fast response times.
