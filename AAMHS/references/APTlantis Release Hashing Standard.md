# APTlantis Release Hashing Standard

Purpose: Every APTlantis release artifact SHALL be accompanied by multiple cryptographic hashes. The purpose of these hashes is to provide integrity verification, long-term archival confidence, and independence from any single cryptographic algorithm or vendor ecosystem.
The APTlantis project views software releases as artifacts worthy of preservation. Verification information should remain useful and trustworthy for years or decades after publication.

Required Hash Algorithms

All release artifacts MUST include the following hashes:
• SHA256
• BLAKE3
• KangarooTwelve (K12)

Rationale
SHA256: Universal Compatibility
SHA256 remains the most widely recognized and supported cryptographic hash algorithm in software distribution.
Benefits include:
• Native support across Windows, Linux, and macOS
• Compatibility with security scanners and CI/CD systems
• Broad recognition by users and organizations
• Long-established industry adoption
SHA256 serves as the baseline verification method that virtually every user can validate without installing additional tooling.

BLAKE3: High-Performance Modern Hashing
BLAKE3 represents the current state of the art in practical hashing performance.
Benefits include:
• Extremely high throughput
• Parallel processing support
• Excellent performance on modern CPUs
• Strong cryptographic design
• Growing ecosystem adoption
BLAKE3 is particularly valuable when verifying large artifacts such as ISO images, archives, datasets, virtual machine images, and software collections.

KangarooTwelve: Independent Cryptographic Lineage
KangarooTwelve is a high-performance derivative of the Keccak family, the basis of SHA-3.
Benefits include:
• Distinct design lineage from SHA-2 and BLAKE families
• Excellent performance characteristics
• Strong security margins
• Modern sponge-based construction
• Long-term cryptographic diversity

KangarooTwelve provides algorithmic independence, reducing reliance on any single family of cryptographic designs.
Defense Through Diversity
The selected algorithms intentionally originate from different cryptographic families:

Algorithm
Family

SHA256
SHA-2

BLAKE3
BLAKE

KangarooTwelve
Keccak / SHA-3


This approach improves long-term resilience by avoiding dependence on a single algorithm family.
The goal is not merely redundancy, but cryptographic diversity.
Post-Quantum Considerations
Current research indicates that cryptographic hash functions remain significantly more resistant to quantum attacks than traditional public-key cryptography.
The selected algorithms provide strong security margins while maintaining practical performance. APTlantis considers SHA256, BLAKE3, and KangarooTwelve an appropriate balance between compatibility, performance, and future resilience.
Future Direction
APTlantis may supplement release hashes with cryptographic signatures, including post-quantum signature schemes, as tooling and ecosystem support mature.
Hashes verify that a file has not changed.
Signatures verify who published it.
Both play an important role in long-term software preservation and provenance.