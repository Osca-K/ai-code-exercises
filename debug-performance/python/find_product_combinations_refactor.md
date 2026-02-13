# AI-Assisted Refactoring: find_product_combinations

## 1. Code Readability Improvement (Prompt 1)

### Issues Identified
- The function is long and has deeply nested loops and conditionals.
- Variable names are mostly clear, but the logic for duplicate checking is hard to follow.
- The print statement for progress is mixed into the main logic.
- The generator expression for duplicate checking is complex and impacts readability.

### Suggestions
- Extract duplicate checking into a helper function.
- Move progress printing outside the main logic (or make it optional).
- Use more descriptive variable names where possible.
- Add comments to clarify each step.

## 2. Function Refactoring (Prompt 2)

### Responsibilities Identified
- Iterating over all product pairs
- Checking if a pair is valid (not the same product, within price range, not a duplicate)
- Creating the result dictionary for each valid pair
- Sorting the results
- Printing progress

### Refactoring Suggestions
- Split into smaller functions:
  - `is_valid_pair(product1, product2, target_price, price_margin, seen_pairs)`
  - `add_pair_to_results(product1, product2, ...)`
- Use a set to track seen pairs for duplicate detection.
- Optionally, add a progress callback or flag.

## 3. Code Duplication Detection (Prompt 3)

- The duplicate check logic is repeated for each pair.
- The process of creating the result dictionary is repeated.
- Both can be consolidated into helper functions.

## 4. Refactored Code Example
```python
def find_product_combinations(products, target_price, price_margin=10, show_progress=False):
    """
    Find all unique pairs of products where the combined price is within the target range.
    """
    results = []
    seen_pairs = set()
    n = len(products)
    for i in range(n):
        if show_progress and i % 100 == 0:
            print(f"Processing product {i+1} of {n}")
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

## 5. Key Learnings
- Breaking down complex functions improves readability and maintainability.
- Using sets for duplicate detection is more efficient and clearer than generator expressions.
- Optional progress reporting can be separated from core logic.
- Helper functions and clear variable names make code easier to review and extend.
