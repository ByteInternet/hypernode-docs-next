---
myst:
  html_meta:
    description: 'Struggling with the “Front Controller Reached 100 Router Match Iterations”
      error? Our expert guides will help you diagnose, troubleshoot and solve this
      issue. '
    title: Solve “Front Controller Reached 100 Router Match Iterations”
redirect_from:
  - /en/troubleshooting/performance/how-to-solve-the-front-controller-reached-100-router-match-iterations-error/
---

<!-- source: https://support.hypernode.com/en/troubleshooting/performance/how-to-solve-the-front-controller-reached-100-router-match-iterations-error/ -->

# How to solve the “Front Controller Reached 100 Router Match Iterations” Error

This error appears when a corruption in the cache arises, caused by a bug in Magento.

We see this error mostly on shops that experience high traffic, causing a rare condition in the caching mechanism.

The developers from Convenient and AmpersandHQ fully debugged this issue and came up with a patch that should solve this issue once and for all.

You can find [detailed information](https://github.com/convenient/magento-ce-ee-config-corruption-bug#the-fix)about how to solve this issue on the GitHub page of Convenient.

This issue is as far as we know a Magento 1 only issue, although a very small group of developers working on Magento 2 have notified us of having the same issue appear in Magento 2.

**Update:** So it seems it could help [changing the permissions on certain a PHP file](https://stackoverflow.com/questions/6262129/magento-front-controller-reached-100-router-match-iterations-error/33684913#33684913)if the convenient patch does not fix this issue.

**Update 2:** Adding other suggestions to fix this issue from [Magento explorer](https://magentoexplorer.com/how-to-debug-and-fix-front-controller-reached-100-router-match-iterations-in-magento).
