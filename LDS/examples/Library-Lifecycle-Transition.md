# LDS Library Lifecycle Transition Example

## Purpose

This example shows a library moving through LDS stability states.

## Library

- Library: `ManifestQuery.Core`
- Governing standard: LDS
- Companion command: `manifest-query-cli`, governed by CTS

## Experimental

The library begins as `experimental` while public names, return shapes, and error contracts are still changing.

Required evidence:

- rough public surface summary;
- known gaps;
- no stability claims for automation consumers.

## Interface-Stable

The library moves to `interface-stable` when:

- public functions and types are named;
- extension contracts are documented;
- at least one consumer can build against the interface;
- known breaking risks are recorded.

## Versioned

The library moves to `versioned` when:

- semver policy is documented;
- changelog location is known;
- breaking-change procedure exists;
- MSRV or runtime minimum is recorded.

## Reference

The library moves to `reference` when:

- two or more real consumers are tracked;
- at least one breaking-change cycle has been handled;
- migration notes exist;
- validator evidence is part of release review.
