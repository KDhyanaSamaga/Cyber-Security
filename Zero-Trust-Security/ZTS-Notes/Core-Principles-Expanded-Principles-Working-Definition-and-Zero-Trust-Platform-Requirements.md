## 1. Core Principles

Foundational and essential principles based on Forrester's "No More Chewy Centers" paper and NIST Zero Trust Architecture:

1. **Ensure all resources are accessed securely, regardless of location:**
* Includes all resources in the scope of Zero Trust, breaking down historical IT and security silos.
* Secures access for all identities (human and machine) to all resources (data, applications, servers), dissolving the traditional corporate perimeter.
* Mandates network traffic encryption and strict policy-enforced access controls.


2. **Adopt a least privilege strategy and strictly enforce access control:**
* Consistently manages least privilege across locations and resource types at both network and application layers using identity and security context.
* Treats the ability to send network packets to a system as a privilege; unauthorized users must be blocked at the network layer from connecting to services.


3. **Inspect and log all traffic:**
* Examines and logs network traffic metadata enriched with identity and device context (and selectively inspects content due to storage/processing costs).
* Feeds this data into Next-Generation Firewalls, network monitoring tools, and SIEMs to enhance detection, alerting, and incident response.



---

## 2. Expanded Principles

Three additional principles necessary for an enterprise-class Zero Trust environment:

1. **Ensure all components support APIs for event and data exchange:**
* Integrates previously siloed security products, infrastructure, and business systems to enable a holistic security context.
* Facilitates initiating events, responding to threats, and exchanging logs and data. Un-integrated components add friction and diminish security effectiveness.


2. **Automate actions across environments and systems, driven by context and events:**
* Enables dynamic access control rules that adjust automatically based on identity, device, network, and system context via a logical control channel connecting the Policy Decision Point (PDP) and Policy Enforcement Points (PEPs).
* Note: Automation does not mean "automatic" without oversight; manual steps (like managerial approvals) can be embedded within an automated workflow.


3. **Deliver tactical and strategic value:**
* Ties Zero Trust initiatives directly to business drivers and strategic business value.
* Relies on early, incremental tactical wins within the strategic architecture to build internal momentum, simplify the deployment journey, and gain organizational support.



---

## 3. Working Definition

> *"Zero Trust is a holistic security framework that leverages information from identity, security and IT Infrastructure, and risk and analytics tools to inform and enable the dynamic enforcement of security policies uniformly across the enterprise. Zero Trust shifts security from an ineffective perimeter-centric model to a resource and identity-centric model. As a result, organizations can continuously adapt access controls to a changing environment, obtaining improved security, reduced risk, simplified and resilient operations, and increased business agility."*

---

## 4. Zero Trust Platform Requirements

Baseline technical and operational platform requirements derived from the Zero Trust principles:

1. **Encrypted Data Plane:** Data plane communications must be encrypted (with deliberate exceptions like DNS).
2. **Contextual Access Control:** The system must enforce identity-centric and contextual access controls for all resource types.
3. **Data Protection:** Data resource protections must utilize identity and contextual policies to manage access.
4. **Universal Location Support:** Policy models and controls must secure all users in all locations consistently (remote vs. on-premises).
5. **Posture Inspection:** Devices must undergo initial and periodic security posture and configuration inspections before access is granted.
6. **BYOD Differentiation:** The platform must distinguish BYOD from corporate-managed devices and adjust access levels accordingly.
7. **Explicit Granting:** Access to any network resource must be explicitly granted by policy—no user/device inherently gets broad network access.
8. **Service-Level Granularity:** Access controls must differentiate between different services on the same resource (e.g., separating HTTPS from SSH access).
9. **Data Element Classification:** Access to specific data elements inside applications/containers with different classifications must follow business policies.
10. **Enriched Metadata Logging:** Network traffic metadata must be logged and enriched with identity context.
11. **Traffic Content Inspection:** Network traffic must be capable of examination for security and data loss prevention (DLP) purposes.
12. **Cloud-Native Parity:** Workloads transferred to the cloud must carry the same access control policies as defined on-premises.
13. **Contextual Incident Response:** Automation must incorporate identity-centric details for efficient and effective incident response.
14. **Analytics Integration:** Logs must be integrated into analytics tools to inform and drive dynamic policy enforcement.
