This diagram illustrates a **traditional, legacy perimeter-based enterprise architecture** transitioning into or incorporating security controls that support a **Zero Trust Architecture (ZTA)**.

In a pure **Zero Trust Architecture**, the fundamental philosophy is **"Never Trust, Always Verify."** Network location alone (being inside the internal network) does not grant trust. Every user, device, and request must be explicitly authenticated, authorized, continuously validated, and granted least-privileged access before accessing resources.

Below is a detailed breakdown of every component in the diagram, explaining **what it is**, **why it is used**, and **what it does**, structured through the lens of Zero Trust.

---

## 1. Users & External Entities

* **Employee**:
* **What it is:** Internal workforce users requesting access to enterprise data and workloads.


* **Why it is used:** Represents the human identity initiating operations.


* **Zero Trust Context:** Zero Trust treats employees as untrusted regardless of whether they are remote or inside the office network. Their identity, context (device posture, location, time), and actions are strictly evaluated on every access request.




* **Customer**:
* **What it is:** External users accessing public-facing enterprise services.


* **Why it is used:** Represents external traffic that must be strictly isolated from core enterprise workloads.


* **Zero Trust Context:** Customers are granted minimal access, restricted strictly to public web interfaces via strict access rules and Web Application Firewalls (WAF).




* **Customer System**:
* **What it is:** External device or system managed by a customer.


* **Why it is used:** Represents third-party managed endpoint infrastructure interacting with enterprise SaaS or web systems.


* **Zero Trust Context:** Considered entirely unmanaged and untrusted; access is conditioned through Cloud Access Security Brokers (CASB) or secure web gateways.





---

## 2. Perimeter & Border Protection

* **VPN Client & VPN Entry Point**:
* **What it is:** Virtual Private Network infrastructure providing remote encrypted network tunnels.


* **Why it is used:** Traditionally grants remote employees access to the internal network.


* **Zero Trust Context:** VPNs represent a **legacy approach** that Zero Trust seeks to replace or refine. Standard VPNs grant broad network-level access once authenticated ("castle-and-moat"). In Zero Trust, VPNs are replaced or paired with **Zero Trust Network Access (ZTNA)**, which grants application-level access instead of network-level access.




* **DMZ (Demilitarized Zone)**:
* **What it is:** A perimeter network segment separating the public internet from the private enterprise network.


* **Why it is used:** Houses public-facing services (e.g., VPN gateways, web servers) so external traffic doesn't hit the internal network directly.


* **Zero Trust Context:** Zero Trust shifts focus from perimeter-based zoning (DMZ) to micro-segmentation around individual workloads, neutralizing the concept of a "safe" inner zone.




* **Web Server + WAF (Web Application Firewall)**:
* **What it is:** Web application hosting coupled with a layer-7 security firewall.


* **Why it is used:** Inspects incoming HTTP/HTTPS traffic for web application attacks (SQL injection, XSS, DDoS) before it hits applications.


* **Zero Trust Context:** Functions as an inline Policy Enforcement Point (PEP) ensuring incoming application traffic complies with security standards.





---

## 3. Network Security & Control Controls

* **NGFW / IDS / IPS (Next-Generation Firewall / Intrusion Detection & Prevention System)**:
* **What it is:** Advanced deep-packet inspection network security systems.


* **Why it is used:** Monitors, filters, and blocks malicious traffic crossing network boundaries or moving laterally.


* **Zero Trust Context:** Enforces network segmentation policies, performs continuous threat detection, and inspects traffic in real-time.




* **NAC (Network Access Control)**:
* **What it is:** Security solution that enforces access policy on devices attempting to connect to a network.


* **Why it is used:** Ensures only compliant, authenticated devices can connect to the internal network.


* **Zero Trust Context:** Acts as a gatekeeper verifying device posture (antivirus up-to-date, proper OS patch level) before granting network admission.





---

## 4. Workload Access & Control Point Components

* **Jump Box**:
* **What it is:** A hardened server used as an intermediary system to access administrative interfaces of critical resources.


* **Why it is used:** Minimizes exposure of backend servers by restricting direct SSH/RDP access.


* **Zero Trust Context:** Enforces gateway-level isolation and monitoring for administrative sessions.




* **Load Balancer**:
* **What it is:** Device or software distribution system for network/application traffic across multiple back-end servers.


* **Why it is used:** Ensures high availability, scalability, and performance for applications.


* **Zero Trust Context:** Can terminate TLS encryption for inspection and act as a control point for routing authenticated traffic to micro-segmented workloads.




* **PAM (Privileged Access Management)**:
* **What it is:** Cyber-security strategy and tools designed to secure, manage, and monitor privileged elevated access accounts.


* **Why it is used:** Prevents credential theft and abuse by granting temporary, monitored, highly elevated access to administrative users.


* **Zero Trust Context:** Core Zero Trust component enforcing the **Principle of Least Privilege (PoLP)** and Just-In-Time (JIT) access.




* **R (Resources / Workloads being accessed)**:
* **What it is:** The actual data, applications, services, or databases.


* **Why it is used:** The core assets that business operations rely on.


* **Zero Trust Context:** The primary targets to protect. Each resource is isolated using micro-segmentation so compromise of one resource does not allow lateral movement to another.





---

## 5. Enterprise Management & Governance (Top Banner)

These centralized management plane components serve as the **Policy Decision Points (PDP)** and context engines in a Zero Trust Architecture:

* **IAM (Identity and Access Management)**:
* **What it is:** Management framework of policies and technologies for ensuring appropriate users have appropriate access.


* **Why it is used:** Authenticates identities (using MFA, SSO) and manages user entitlements.


* **Zero Trust Role:** The fundamental pillar of Zero Trust identity-based access control.




* **GRC (Governance, Risk, and Compliance)**:
* **What it is:** Structured framework aligning IT strategy with business goals while managing risk and meeting regulatory requirements.


* **Why it is used:** Defines organizational access policies, compliance baselines, and risk tolerances.


* **Zero Trust Role:** Outlines the security policies that Zero Trust engines enforce programmatically.




* **PKI (Public Key Infrastructure)**:
* **What it is:** System of digital certificates, Certificate Authorities (CA), and encryption management.


* **Why it is used:** Authenticates devices and encrypts communications via TLS/mTLS.


* **Zero Trust Role:** Guarantees cryptographically secure, end-to-end encrypted communications and Mutual TLS (mTLS) device authentication.




* **MDM (Mobile Device Management)**:
* **What it is:** Software used to monitor, manage, and secure employee laptops, mobile devices, and endpoints.


* **Why it is used:** Ensures endpoint compliance with corporate security standards.


* **Zero Trust Role:** Feeds device health and compliance state into the Zero Trust Policy Engine before access is approved.




* **SIEM (Security Information and Event Management)**:
* **What it is:** Security management system that aggregates log data from across the enterprise network.


* **Why it is used:** Performs real-time security monitoring, event correlation, and incident analysis.


* **Zero Trust Role:** Provides continuous visibility, logging, and automated threat response.





---

## 6. Cloud & External Infrastructure Extensions

* **CASB (Cloud Access Security Broker)**:
* **What it is:** Security enforcement point placed between cloud service users and cloud applications.


* **Why it is used:** Extends enterprise security policies to external SaaS platforms.


* **Zero Trust Context:** Enforces DLP (Data Loss Prevention), threat protection, and access policies for cloud-hosted applications.




* **SaaS (Software as a Service)**:
* **What it is:** Cloud-hosted software applications (e.g., Microsoft 365, Salesforce).


* **Why it is used:** Delivers software functionality over the internet without local hosting.


* **Zero Trust Context:** Secured directly via identity providers (IAM) and CASB without relying on internal corporate network connectivity.




* **IaaS (Infrastructure as a Service)**:
* **What it is:** Cloud-hosted computing infrastructure (e.g., AWS EC2, Azure VMs).


* **Why it is used:** Scalable infrastructure hosting cloud workloads.


* **Zero Trust Context:** Connected via encrypted **Private Links** and restricted using cloud-native **Security Groups** (micro-segmentation).




* **Security Group**:
* **What it is:** Virtual stateful firewall controlling inbound/outbound cloud instance traffic.


* **Why it is used:** Restricts traffic at the cloud network interface level.


* **Zero Trust Context:** Enforces micro-segmentation at the individual cloud workload level.




* **Private Link**:
* **What it is:** Dedicated, private cryptographic connection linking cloud IaaS to the enterprise network without exposing traffic to the public internet.


* **Why it is used:** Ensures secure, low-latency cross-environment connectivity.


* **Zero Trust Context:** Secures transport layer communications between on-premise and cloud ecosystems.




* **Branch Offices & WAN (e.g., MPLS)**:
* **What it is:** Remote physical office sites connected through wide-area networks or firewalls.


* **Why it is used:** Connects distributed physical branch locations back to core enterprise applications.


* **Zero Trust Context:** Branch office networks are treated as untrusted networks (similar to public Wi-Fi), requiring local firewall enforcement and explicit verification for every outbound request.
