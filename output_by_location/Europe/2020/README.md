# Europe 2020
---
## 🧠 Tools by Category
### Blue Team & Detection

<details><summary><strong>[0365Squatting](https://github.com/O365Squad/O365-Squatting)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![J Francisco Bolivar](https://img.shields.io/badge/J%20Francisco%20Bolivar-informational) ![Jose Miguel Gomez](https://img.shields.io/badge/Jose%20Miguel%20Gomez-informational)

                One of the main benefits of cloud technology is to deploy quickly services, with minimum interaction from the administrator side, this is an advantage exploited by cyber criminals too. Nowadays the main threats all size companies are facing is phishing, every day cybercriminals are creating more sophisticated techniques to cheat users and make more difficult the job of blue teams. The most common technique used is typo squatting.

Part of the Blue team mission is to detect phishing, typo squatters, and attack domains before the phishing campaign begins, there is outside plenty of tools trying to detect that domains based on DNS, however none of them are focus into the cloud.
0365Squatting is a python tool created to identify that domains before the attack start. The tool can create a list of typo squatted domains based on the domain provided by the user and check all the domains against O365 infrastructure, (these domains will not appear on a DNS request).

At the same time, this tool can also be used by red teams and bug bunters, one of the classic attacks is the domain takeover so, the second option of this too is to check if the domain is registered in O365 in order to launch a domain takeover attack.

                </details>
                
<details><summary><strong>[HosTaGe: mobile honeypots for rapid deployment](https://github.com/aau-network-security/HosTaGe)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Emmanouil Vasilomanolakis](https://img.shields.io/badge/Emmanouil%20Vasilomanolakis-informational) ![Shreyas Srinivasa](https://img.shields.io/badge/Shreyas%20Srinivasa-informational) ![Eirini Lygerou](https://img.shields.io/badge/Eirini%20Lygerou-informational)

                HosTaGe is a lightweight, low-interaction, and portable honeypot for mobile devices that aims on the detection of malicious network environments. As most malware propagate over the network via specific protocols, a low-interaction honeypot located at a mobile device can check wireless networks for actively propagating malware. HosTaGe supports many commonly used protocols (e.g. HTTP, TELNET, SSH) along with many IoT/ICS specific ones (e.g. MQTT, S7COMM, MODBUS). We envision such honeypots running on all kinds of mobile devices to provide a quick assessment on the potential security state of a network.

                </details>
                
<details><summary><strong>[NEW TSURUGI LINUX ACQUIRE & DIGITAL FORENSIC ACQUISITIONS](https://github.com/drego85/HackInBo)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Giovanni Rattaro](https://img.shields.io/badge/Giovanni%20Rattaro-informational) ![Marco Giorgi](https://img.shields.io/badge/Marco%20Giorgi-informational)

                Tsurugi ACQUIRE is a dedicated Linux OS to perform DIGITAL FORENSIC acquisition before to start post mortem DFIR investigations.

                </details>
                
<details><summary><strong>[Strafer: A Tool to Detect Infections in Elasticsearch Instances](https://github.com/adityaks/strafer)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Aditya K Sood](https://img.shields.io/badge/Aditya%20K%20Sood-informational) ![Rohit Bansal](https://img.shields.io/badge/Rohit%20Bansal-informational)

                Elasticsearch infections are rising exponentially. The adversaries are exploiting open and exposed Elasticsearch interfaces to trigger infections in the cloud and non-cloud deployments. During this talk, we will release a tool named "STRAFER" to detect potential infections in the Elasticsearch instances. The tool allows security researchers, penetration testers, and threat intelligence experts to detect compromised and infected Elasticsearch instances running malicious code. The tool also enables you to conduct efficient research in the field of malware targeting cloud databases.




In this version of the tool, the following modules are supported:

Elasticsearch instance information gathering and reconnaissance
Elasticsearch instance exposure on the Internet
Detecting potential ransomware infections in the Elasticsearch instances
Detecting potential botnet infections such as meow botnet.
Detecting infected indices in the Elasticsearch instances

Note: This is the first release of the tool and we expect to add more modules in the nearby future.

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[ArcherySec 2.0 - Open Source Vulnerability Assessment and Management](https://github.com/archerysec/archerysec)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Anand Tiwari](https://img.shields.io/badge/Anand%20Tiwari-informational)

                ArcherySec is an opensource vulnerability assessment and management tool which helps developers and pentesters to perform scans and manage vulnerabilities. ArcherySec uses popular opensource tools to perform comprehensive scanning for web applications and networks. It also supports multiple continuous integrations and continuous delivery software. The developers could utilize this tool for the implementation of vulnerability management in the DevOps CI/CD environment.

- Perform Web and Network Vulnerability Scanning using opensource tools.
- Correlates and Collaborate all raw scans data, shows them in a consolidated manner.
- Perform authenticated web scanning.
- Vulnerability Management.
- Enable REST API's for developers to perform scanning and Vulnerability Management.
- JIRA Ticketing System.
- Sub domain discovery and scanning.
- Periodic scans.
- Concurrent scans.
- Integrate with CI/CD software.

                </details>
                

### Red Teaming

<details><summary><strong>[Batea: Digging for gold in network data](https://github.com/yarkable/Awesome-Computer-Vision-Paper-List/blob/main/NeurIPS/nips2019.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Serge-Olivier Paquette](https://img.shields.io/badge/Serge-Olivier%20Paquette-informational)

                Batea is a simple tool that showcases how basic machine learning can help security analysts in their day-to-day operations. It is a context-driven network device ranking framework based on the anomaly detection family of machine learning algorithms. The goal of Batea is to allow security teams to automatically filter interesting network devices in large networks using nmap scan reports. We call those Gold Nuggets. Batea outputs the gold nuggets in order of interest for an attacker given the context of the network.

The human challenge is, on the one hand, that a typical enterprise network will host thousands of endpoints, far too many for a few security team members to constantly track and evaluate for their "attractiveness" to a potential intruder. On the other hand, the notion of interest is highly context-sensitive.

Batea works by constructing a numerical representation of all devices from your nmap reports (XML) and then applying the Isolation Forest algorithm to uncover the gold nuggets. It is easily extendable by adding specific "features", or interesting characteristics, to the numerical representation of the network elements.

The features act as elements of intuition, and the unsupervised anomaly detection methods allow the context of the device, along with the total description of the network, to be used as the central building block of the ranking algorithm.

Given that we have taken meaningful elements of intuition all at once, the fact that the Isolation Forest algorithm always takes the whole dataset into consideration ensures that the network context is embedded in the ranking used to predict Gold Nuggets.

Pen testers can train the Batea machine learning model from scratch on new network data, or use a model that has been pre-trained on various networks.

                </details>
                
<details><summary><strong>[C2 Matrix](https://github.com/CyberSecurityUP/C2Matrix-Automation)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Jorge Orchilles](https://img.shields.io/badge/Jorge%20Orchilles-informational) ![Bryson Bort](https://img.shields.io/badge/Bryson%20Bort-informational)

                Command and Control is one of the most important tactics in the MITRE ATT&CK matrix as it allows the attacker to interact with the target system and realize their objectives. Organizations leverage Cyber Threat Intelligence to understand their threat model and adversaries that have the intent, opportunity, and capability to attack. Red Team, Blue Team, and virtual Purple Teams work together to understand the adversary Tactics, ﻿Techniques, and Procedures to perform adversary emulations and improve detective and preventive controls.

The C2 Matrix was created to aggregate all the Command and Control frameworks publicly available (open-source and commercial) in a single resource to assist teams in testing their own controls through adversary emulations (Red Team or Purple Team Exercises). Phase 1 lists all the Command and Control features such as the coding language used, channels (HTTP, TCP, ﻿DNS, SMB, etc.), agents, key exchange, and other operational security features and capabilities.﻿﻿ This allows more efficient decisions making when called upon to emulate and adversary TTPs.

It is the golden age of Command and Control (C2) frameworks. Learn how these C2 frameworks work and start testing against your organization to improve detective and preventive controls.

                </details>
                
<details><summary><strong>[git-wild-hunt: Pwn API and leaked secrets](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/RT.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Rod Soto](https://img.shields.io/badge/Rod%20Soto-informational) ![Jose Hernandez](https://img.shields.io/badge/Jose%20Hernandez-informational)

                Git Wild Hunt is a tool that allows researchers and security operators to find leaked credentials and secrets in Github covering over 30 types of credentials. This tool is great for cloud security/DevOps security awareness or for cloud security pentesters and red teamers. We will show how deep into an organization or even personal sensitive information can be found by simply starting from leaked credentials in a GitHub project.

                </details>
                
<details><summary><strong>[Powerglot: Encoding offensive scripts using polyglots for stego-malware, privilege escalation & lateral movement](https://github.com/mindcrypt/powerglot)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Dr. Alfonso Muñoz](https://img.shields.io/badge/Dr.%20Alfonso%20Muñoz-informational)

                In red-team exercises or offensive tasks, masking of payloads is usually done by using steganography, especially to avoid network level protections, being one of the most common payloads scripts developed in powershell. Recent malware and APTs make use of some of these capabilities: APT32, APT37, Ursnif, Powload, LightNeuron/Turla, Platinum APT, Waterbug/Turla, Lokibot, The dukes (operation Ghost), Titanium, etc. But offensive tools based on steganography need a loader to run the payload. Powerglot tries to reduce this exposition using polyglots in several scenarios.

Powerglot is a multifunctional and multi-platform attack and defense tool based on polyglots. Powerglot allows to mask a script (powershell, shellscripting, php, ...) mainly in a digital image, although other file formats are in progress. Unlike the usual offensive tools or malware, Powerglot does not need any loader to execute the "information hidden", minimizing the noise on the target system.

PowerGlot has a clear utility in offensive tasks but it is also defined as a discovery and blue team tool. To our knowledge, it is the first general and complete open-source tool that allows to search for the presence of masked information with polyglots, information that could be useful to achieve persistence in a system or to hide malware (stego-malware, privilege escalation, lateral movement, reverse shell, etc.)

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[BLE hardware-less hackme](https://github.com/smartlockpicking/BLE_HackMe)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Slawomir Jasek](https://img.shields.io/badge/Slawomir%20Jasek-informational)

                The new, free tool aims to help getting familiar with the very basics of ubiquitous Bluetooth Low Energy technology and its (in)security - without the need of any dedicated hardware. It is based on a specially designed software (running on a typical Windows 10 laptop) - which simulates a BLE device, on the radio layer working exactly the same as a real one. The simulated device contains several "hackme" challenges of increasing level: starting with simple communication protocol introduction up to unlocking smart locks. Most of these challenges can be solved using nothing more than just a free mobile application, which connects via Bluetooth to the laptop running simulated device. This unique approach makes the fun available for everyone who would like to start the journey into fascinating vulnerabilities of BLE devices, but is afraid of gearing up with special hardware or steep learning curve for advanced tools. The basics possible to grasp using the introduced hackme can however be easily applicable to take control of surprisingly lot of real devices surrounding us.

                </details>
                

### OSINT

<details><summary><strong>[kubeletctl: A Kubelet Client to Attack Kubernetes](https://github.com/cyberark/kubeletctl)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Eviatar Gerzi](https://img.shields.io/badge/Eviatar%20Gerzi-informational)

                kubeletctl is a CLI client for kubelet - the remote agent of Kubernetes on the nodes. It implements all the documented and undocumented API of kubelet but it also includes offensive capabilities:
- Scan for vulnerable nodes
- Scan for containers with RCE
- Run command on multiple containers

                </details>
                

### Web/AppSec

<details><summary><strong>[SnitchDNS](https://github.com/sadreck)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Pavel Tsakalidis](https://img.shields.io/badge/Pavel%20Tsakalidis-informational)

                "It's always DNS". SnitchDNS is database driven (basic) DNS server built using Twisted, with a fancy web interface to go with it. Ideal for Red Team infrastructure, bug bounties, ad-blocking, DNS tunnels, and more.

As it's database driven, any changes are reflected immediately, match wildcard subdomains, source IP restrictions, conditional responses (great for SSRF), Slack/Teams/Email/Push notifications, logging, Swagger 2.0 API, full CLI interface, and more!

Ideal use cases are as a DNS Tunnel, DNS forwarding server, red teams, canary tokens, LetsEncrypt DNS challenge, and even ad-blocking.

                </details>
                
<details><summary><strong>[Threagile: Agile Threat Modeling Toolkit](https://github.com/cschneider4711)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Christian Schneider](https://img.shields.io/badge/Christian%20Schneider-informational)

                If we can build software in a reliable, reproducible and quick way at any time using Pipeline-as-Code and have also automated security scans as part of it, how can we quickly capture the risk landscape of agile projects to ensure we didn't miss an important thing? Traditionally, this happens in workshops with lots of discussion and model work on the whiteboard. It's just a pity that it often stops then: Instead of a living model, a slowly but surely eroding artifact is created, while the agile project evolves at a faster pace.

In order to counteract this process of decay, something has to be done continuously, something like "Threat-Model-as-Code" in the DevSecOps sense. The open-source tool Threagile implements the ideas behind this approach: Agile developer-friendly threat modeling right from within the IDE. Models editable in developer IDEs and diffable in Git, which automatically derive risks including graphical diagram and report generation with recommended mitigation actions.

The open-source Threagile toolkit runs either as a command line tool or a full-fledged server with a REST-API: Given information about your data assets, technical assets, communication links, and trust boundaries as input in a simple to maintain YAML file, it executes a set of over 40 built-in risk rules (and optionally your custom risk rules) against the processed model. The resulting artifacts are diagrams, JSON, Excel, and PDF reports about the identified risks, their rating, and the mitigation steps as well as risk tracking state.

Agile development teams can easily integrate threat modeling into their process by maintaining a simple YAML input file about their architecture and the open-source Threagile toolkits handles the risk evaluation.

                </details>
                
