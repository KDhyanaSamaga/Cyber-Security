### **1. Forrester’s Zero Trust eXtended (ZTX) Model**

Forrester introduced the initial Zero Trust model in 2010 and later updated it to the **Zero Trust eXtended (ZTX)** model. The ZTX model places **Data (or "Value")** at its very center. This reflects Forrester’s view that the data explosion across on-premises and cloud environments represents the core asset that must be protected, while the surrounding elements act as conduits to that data.

The ZTX model consists of **five core pillars surrounding data**, along with **two foundational operational capabilities**:

#### **Core Pillars surrounding Data**

* **Data / Value (Center):** Includes data classification, data protection, and Data Loss Prevention (DLP) integrated into the policy model to enforce contextual access controls.
* **Networks:** Focuses primarily on user and server network segmentation based on identity-centric attributes. It incorporates traditional network security components such as Next-Generation Firewalls (NGFWs), Web Application Firewalls (WAF), Network Access Control (NAC), and Intrusion Prevention Systems (IPS).
* **People:** Centers on Identity and Access Management (IAM), leveraging Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), Multi-Factor Authentication (MFA), and Single Sign-On (SSO) using modern standards like OAuth and SAML.
* **Workloads:** Encompasses the logical functions driving business (containers, applications, infrastructure, processes, etc.) across hybrid environments using metadata-driven access controls.
* **Devices:** Focuses on the identity, inventory, security, isolation, and control of devices, relying on user agents/clients running on end-user devices.

#### **Foundational Capabilities**

* **Visibility and Analytics:** Consolidates data across disparate sources across the enterprise to support informed, contextual security decisions.
* **Automation and Orchestration:** Automates manual processes and ties them directly to security policies and dynamic responses across the enterprise ecosystem.

---

### **2. Gartner’s Approach to Zero Trust**

Gartner approaches Zero Trust primarily through a conceptual model called **CARTA** (**Continuous Adaptive Risk and Trust Assessment**).

#### **Core Principles of Gartner's Approach**

* **CARTA Framework:** Focuses on maintaining a continuous assessment of risk and trust regarding users, devices, applications, data, and workloads.
* **Operational Cycle:** Built around a continuous four-phase loop: **Predict, Prevent, Detect, and Respond**.
* **Continuous Adjustment:** Follows a core process of:
1. *Implement* a security posture.
2. *Monitor* the posture continuously.
3. *Adjust* the security posture across different security planes.



#### **Gartner's Zero Trust Terminology**

Gartner views Zero Trust slightly more narrowly through specific technical categories:

* **Zero Trust Network Access (ZTNA):** Applied specifically to **user-to-server** security.
* **Zero Trust Network Segmentation (ZTNS):** Applied to **server-to-server** security and microsegmentation.
