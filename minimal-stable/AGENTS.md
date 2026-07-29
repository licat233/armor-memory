# ARMOR Minimal Stable Development Rules

This directory implements deterministic document routing.

- Do not add natural-language keyword inference.
- Do not call an LLM from the router.
- Do not scan the Vault from the router.
- Do not add implicit Inbox fallbacks.
- Do not silently accept unknown values.
- Every new enum or route requires documentation and tests.
- Run: `python3 -m pytest minimal-stable/tests -v`
- Do not modify V7.2 while working in this directory.

