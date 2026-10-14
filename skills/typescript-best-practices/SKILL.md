---
name: typescript-best-practices
description: "Shape or review TypeScript code and types. Use when reading or editing TypeScript, adapting guidance to the project's actual version and schemas."
---

# TypeScript Best Practices

Read {{RUNTIME_GUIDE}} before choosing tools or optional workflows. Fit type guidance to the project's TypeScript version, runtime schemas, and existing conventions.

Model meaningful variants with discriminated unions and check exhaustiveness where adding a variant should surface work for callers. Treat untrusted external values as unknown and validate them at the boundary; make type guards verify what they claim. Derive types from authoritative schemas and existing contracts when that keeps them aligned.

Use branded primitives, object-shaped arguments, satisfies, and helper types when they clarify a real invariant or call site. Prefer narrowing and validation over unchecked casts, but do not treat every cast, positional argument, optional property, or unbranded string as a defect. Avoid introducing abstractions or dependencies for style alone.

The goal is types that make important states and boundaries clear while fitting the code that consumes them.
