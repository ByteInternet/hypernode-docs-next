---
myst:
  html_meta:
    description: Learn about how Hypernode calculates the pricing for Horizontal autoscaling
    title: Pricing for Horizontal Autoscaling | Hypernode
---

# Horizontal Autoscaling Pricing

Horizontal autoscaling pricing has two parts.
1. Fixed license for 25 euros per month.
2. Variable price based on the autoscaling usage.


## Fixed license

The fixed license costs 25 euros per month and is added to your normal Hypernode subscription when you enable Horizontal autoscaling. If you enable it in the middle of the month, you will only pay for the remaining days of that month accordingly.

## Variable Pricing Table

| Autoscaled Server plan | Cost per minute |
| ----------- | ----------- |
| Falcon M    | €0.15       |
| Falcon L    | €0.25       |
| Falcon XL   | €0.45       |
| Falcon 2XL  | €0.69       |
| Falcon 3XL  | €1.02       |
| Falcon 4XL  | €1.5        |
| Falcon 5XL  | €2.2        |

Please note that even though the costs are listed per minute, all the charges are applied on an hourly basis.

So, if you had an extra server when you were autoscaled (due to high load) for 45 minutes, you will be charged for an hour. So the cost will be `60 * cost per minute`.
