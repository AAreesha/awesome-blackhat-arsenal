# USA 2020
---
## 🧠 Tools by Category
### Social Engineering / General

<details><summary><strong>[A DECEPTICON and AUTOBOT walk into a bar: A NEW Python tool for enhanced OPSEC](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/AnonOpSecPrivacy.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Social Engineering / General](https://img.shields.io/badge/Category:%20Social%20Engineering%20/%20General-pink) ![Joe Gray](https://img.shields.io/badge/Joe%20Gray-informational)

                When we see the terms Natural Language Processing (NLP) or Machine Learning (ML), often, our guts are correct, and it is vendor marketing material, frequently containing FUD. After tinkering with various libraries in Python and R with the use of some OSINT and SOCMINT techniques, I have found a use for NLP and ML that is 100% FUD free in the form of a brand new, Python-based tool.

In this presentation, which goes further than the previous DECEPTICON presentation, we address topics that I have frequently spoken about in past years is disinformation, deception, OSINT, and OPSEC. When working through learning NLP and ML in Python, it dawned on me: marry these technologies with DECEPTICON for good. Enter the DECEPTICON bot. The DECEPTICON bot is a python* based tool that connects to social media via APIs to read posts/tweets to determine patterns of posting intervals and content then takes over to autonomously post for the user. What is the application you ask: people who are trying to enhance their OPSEC and abandon social media accounts that have been targeted without setting off alarms to their adversaries. Use case scenarios include public figures, executives, and, most importantly – domestic violence and trafficking victims.

                </details>
                

### Red Teaming

<details><summary><strong>[AutoRDPwn: The Shadow Attack Framework](https://github.com/JoelGMSec/AutoRDPwn)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Joel Gámez](https://img.shields.io/badge/Joel%20Gámez-informational)

                AutoRDPwn is a post-exploitation framework created in Powershell, designed primarily to automate the Shadow attack on Microsoft Windows computers. This vulnerability (catalogued as a feature by Microsoft) allows a remote attacker to view the desktop of his victim without his consent, and even control it on demand, using native tools of the operating system itself.

Thanks to the additional modules, it is possible to obtain a remote shell through Netcat, dump system hashes with Mimikatz, load a remote keylogger and much more. All this, through a totally intiutive menu in seven different languages.

In this talk, we will briefly review the most common remote desktop attacks and the big difference the Shadow attack makes to them. Afterwards, we will make different live demonstrations, in which all the functionalities of the tool will be put into practice. Some of them are the following:

- UAC, AMSI and Windows Defender Bypass
- Remote Shell using native system and third party tools
- Obtaining hashes and pass the hash
- Remote execution without credentials via SMB, WMI and WinRM
- Shadow attack on different operating systems (both desktop and server versions)
- Miscellaneous (remote keylogger, one-line execution, pivoting and more)

                </details>
                
<details><summary><strong>[C2 Matrix: Comparison of Command and Control Frameworks](https://github.com/jesusgavancho/TryHackMe_and_HackTheBox/blob/master/Intro%20to%20C2.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Jorge Orchilles](https://img.shields.io/badge/Jorge%20Orchilles-informational) ![Bryson Bort](https://img.shields.io/badge/Bryson%20Bort-informational)

                Command and Control is one of the most important tactics in the MITRE ATT&CK matrix as it allows the attacker to interact with the target system and realize their objectives. Organizations leverage Cyber Threat Intelligence to understand their threat model and adversaries that have the intent, opportunity, and capability to attack. Red Team, Blue Team, and virtual Purple Teams work together to understand the adversary Tactics, Techniques, and Procedures to perform adversary emulations and improve detective and preventive controls.

The C2 Matrix was created to aggregate all the Command and Control frameworks publicly available (open-source and commercial) in a single resource to assist teams in testing their own controls through adversary emulations (Red Team or Purple Team Exercises). Phase 1 lists all the Command and Control features such as the coding language used, channels (HTTP, TCP, DNS, SMB, etc.), agents, key exchange, and other operational security features and capabilities. This allows more efficient decisions making when called upon to emulate and adversary TTPs.

It is the golden age of Command and Control (C2) frameworks. Learn how these C2 frameworks work and start testing against your organization to improve detective and preventive controls.

The C2 Matrix currently has 41 command and control frameworks documented in a Google Sheet, web site, and questionnaire format.

For Blackhat, C2 Matrix will release phase 2 of the project which involves mapping each C2 to MITRE ATT&CK and correlate with known adversaries. This will allow much quicker selection of which C2s to use for a given adversary or threat scenarios.

                </details>
                
<details><summary><strong>[Covenant: .NET Command and Control](https://github.com/cobbr/Covenant)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Ryan Cobb](https://img.shields.io/badge/Ryan%20Cobb-informational)

                Covenant is a .NET command and control platform and web application that aims to highlight the attack surface of the .NET Framework and .NET Core, make the use of offensive .NET tradecraft easier, and serve as a collaborative platform for red teamers.

Covenant is multi-platform, multi-user, provides an intuitive web application interface, and is extendible through an API.

Covenant includes multiple built-in implants that utilize the traditional .NET Framework and .NET Core, which gives Covenant multi-platform implants that run on Windows, Linux, and MacOS. Additionally, Covenant allows operators to edit and add additional custom implants.

Covenant includes built-in support for custom and complex command and control routing. The platform includes built-in outbound listeners, including an HTTP and TCP listener, and peer-to-peer SMB communications over named pipes, which allows for complex implant networking. The platform also includes a protocol for adding new, custom communication protocols that gives the operator complete control over how the command and control traffic appears on the wire.

Covenant includes tons of built-in tasks based on libraries such as SharpSploit and GhostPack, and uses dynamic C# compilation and ConfuserEx obfuscation on tasks and payloads.

Covenant also has an emphasis on implant and network communication security to protect the data accessed by implants. Covenant implements an Encrypted Key Exchange protocol between implants and listeners to achieve forward secrecy for new implants and enforces SSL certificate pinning for implants.

In the age of EDR and threat hunting, red teamers need flexible, robust, and intuitive command and control platforms. Red teamers need the ability to collaborate with teammates, customize implant behavior and command and control traffic, track artifacts, and quickly adapt for defensive technologies. In this demo, you'll be shown how to accomplish this with Covenant.

                </details>
                
<details><summary><strong>[DeepSea Phishing Gear](https://github.com/dsnezhkov)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Dimitry Snezhkov](https://img.shields.io/badge/Dimitry%20Snezhkov-informational)

                Introducing DeepSea, the phishing gear you will want to take with you on your next offensive expedition. 

It is designed to help Red Team operators and teams with the tactical delivery of opsec-tight, flexible email phishing campaigns carried out in a portable manner on the outside as well as on the inside 
of a perimeter. 

Have you ever wanted to seamlessly operate with external and internal email providers; quickly re-target connectivity parameters per campaign; flexibly add headers, targets, attachments, correctly format and inline email templates, images and multipart messages; use content templates for personalization; clearly separate artifacts and content delivery for multiple (parallel or sequential) phishing campaigns; get actionable context help and deploy with minimal dependencies? 

In this session, we will show how you can do this and more in a portable, one binary cross platform setup, with less than 50 lines in a configuration file. 

With DeepSea, you will be able to keep campaign persistence with DNS tricks and an embedded email server used for running advanced two-way threaded campaigns you have always wanted. Catch and respond to those often missed inquiry emails, solidifying pretext and pacifying your marks.

Whether you plan on executing phishing campaigns deep on the inside of the perimeter, or bounce across multiple email providers for an external stealthy campaign delivery, DeepSea is very likely able to help.

                </details>
                
<details><summary><strong>[Starkiller: Threat Emulation Platform for Red Teams and Penetration Testers](https://github.com/sponsors/BC-SECURITY)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Anthony Rose](https://img.shields.io/badge/Anthony%20Rose-informational)

                The ultimate goal for any security team is to increase resiliency within an organization and adapt to the modern threat. Starkiller aims to provide red teams with a platform to emulate Advanced Persistent Threat (APT) tactics. Starkiller is a frontend for the post-exploitation framework, PowerShell Empire, which incorporates a multi-user GUI application that interfaces with a remote Command and Control (C2) server. Empire is powered by Python 3 and PowerShell and includes many widely used offensive security tools for Windows, Linux, and macOS exploitation. The framework's flexibility to easily incorporate new modules allows for a single solution for red team operations. Both red and blue teams can utilize Starkiller to emulate and defend against the most used APT attack vectors.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[capa: Automatically Identify Malware Capabilities](https://github.com/mandiant/capa/releases/)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Moritz Raabe](https://img.shields.io/badge/Moritz%20Raabe-informational) ![William Ballenthin](https://img.shields.io/badge/William%20Ballenthin-informational)

                capa is an open-source tool that detects capabilities in programs to reduce the time-to-triage and make malware analysis more accessible. Anyone dealing with potentially malicious programs and especially forensic, intelligence, and malware analysts can use capa to understand a sample's capabilities, role (downloader, backdoor, etc.), and any suspicious or unique functionality.
capa takes automated malware triage to the next level going from simply saying "this is probably bad" to providing a concise description of what a program actually does. This report provides critical, decision-making information to anyone dealing with malware.

capa uses a new algorithm that reasons over the features found in a file to identify its capabilities. The lowest level features range from disassembly tricks to coding constructs, while intermediate features include references to recognized strings or API calls. Users compose rules that train capa how to reason about features – and even the significance of other rules. This makes it easy for the community to extend the tool's abilities.

We will describe how and why our tool works. We will also show to use it to enhance every malware analysis workflow. Furthermore, you will learn how to develop capability detections that extend capa.

                </details>
                
<details><summary><strong>[ioc2rpz: Where Threat Intelligence Meets DNS](https://github.com/Homas/ioc2rpz)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Vadim Pavlov](https://img.shields.io/badge/Vadim%20Pavlov-informational)

                DNS is the control plane of the Internet with unprecedented detailed views on applications, devices and even transferred data going in and out of a network. 80% of malware uses DNS to communicate with Command & Control for DNS data exfiltration/infiltration and phishing attacks using lookalike domains. Response Policy Zones or DNS Firewall is a feature which allows us to apply security policies on DNS. Commercial DNS Firewall feeds providers usually do not allow users to generate their own feeds. Cloud only DNS service providers do not provide feeds for on-prem DNS.

ioc2rpz is a DNS server which automatically creates, maintains and distributes DNS Firewall feeds from various local (files, DB) and remote (http, ftp, rpz) sources. This enables easy integrations with Threat Intel providers and Threat Intelligence Platforms. The feeds can be distributed to any open source and commercial DNS servers which support RPZ, e.g. ISC BIND, PowerDNS, Infoblox, BlueCat, Efficient IP etc. With ioc2rpz you can create your own feeds, actions and prevent undesired communications before they happen.

https://ioc2rpz.net is a community portal which is powered by ioc2rpz where you can try several free DNS Firewall feeds.

RpiDNS is a new feature integrated into ioc2rpz.gui which includes an installation script and a web interface to monitor and manage local secure DNS services.

                </details>
                
<details><summary><strong>[JVMXRay](https://github.com/spoofzu/jvmxray)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Milton Smith](https://img.shields.io/badge/Milton%20Smith-informational)

                JVMXRay is technology for monitoring access to system resources within the Java Virtual Machine at runtime. Since JVMXRay integrates with virtual machine, no code changes to the application are required for operation. An ancillary benefit of no code required is that the technology provides insight into 3rd party libraries used by your application and commercial software where no source code is available. JVMXRay is designed with application security emphasis but it's beneficial for other areas like software quality processes and diagnostics. JVMXRay may be extended to work with many technologies like OWASP Dependency Check and other tools.

                </details>
                
<details><summary><strong>[PurpleSharp: Adversary Simulation for the Blue Team](https://github.com/mvelazc0/PurpleSharp)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Mauricio Velazco](https://img.shields.io/badge/Mauricio%20Velazco-informational)

                Defending enterprise networks against attackers continues to present a difficult challenge for blue teams. Prevention has fallen short; improving detection & response capabilities has proven to be a step in the right direction. However, without the telemetry produced by adversary behavior, building and testing detection capabilities will be a challenging task. Executing adversary simulations in monitored environments produces the telemetry that allows security teams to identify gaps in visibility as well as build, test and enhance detection analytics

PurpleSharp is an open source adversary simulation tool written in C# that executes adversary techniques against Windows Active Directory environments. The resulting telemetry can be leveraged to measure and improve the efficacy of a detection engineering program. PurpleSharp executes different behavior across the attack lifecycle following the MITRE ATT&CK Framework's tactics: execution, persistence, privilege escalation, credential access, lateral movement, etc.

PurpleSharp executes simulations on remote hosts by leveraging administrative credentials and native Windows services/features such as Server Message Block (SMB), Windows Management Instrumentation (WMI), Remote Procedure Call (RPC) and Named Pipes.

PurpleSharp can assist blue teams in the following use cases:

- Verify prevention controls ( are Lsass dumps being blocked ? )
- Build new detection controls ( build a detection rule for T1117)
- Test/verify existing detection controls (are we really detecting process injection ?)
- dentify gaps with existing detection analytics ( broken logic, lack of coverage, etc. )
- Identify gaps in visibility ( broken agents, broken event pipelines, etc. )
- Train the SOC with credible simulations

                </details>
                
<details><summary><strong>[ROADtools and ROADrecon](https://github.com/dirkjanm/ROADtools)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Dirk-jan Mollema](https://img.shields.io/badge/Dirk-jan%20Mollema-informational)

                ROADtools is a framework to interact with Azure AD. It currently consists of a library (roadlib) and the ROADrecon Azure AD exploration tool.

ROADlib is a library that can be used to authenticate with Azure AD or to build tools that integrate with a database containing ROADrecon data. The database model in ROADlib is automatically generated based on the metadata definition of the Azure AD internal API.

ROADrecon is a tool for exploring information in Azure AD from both a Red Team and Blue Team perspective. In short, this is what it does:

- Uses an automatically generated metadata model to create an SQLAlchemy backed database on disk.
- Use asynchronous HTTP calls in Python to dump all available information in the Azure AD graph to this database.
- Provide plugins to query this database and output it to a useful format.
- Provide an extensive interface built in Angular that queries the offline database directly for its analysis.

ROADrecon also provides a built-in plugin to export it's data to a custom version of BloodHound with Azure AD capabilities.

Both ROADtools and ROADrecon are completely free and open source software.

                </details>
                
<details><summary><strong>[soc-faker: A python package for use in generating fake data for SOC and security automation](https://github.com/swimlane/soc-faker)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Josh Rickard](https://img.shields.io/badge/Josh%20Rickard-informational)

                soc-faker is used to generate fake data for use by Security Operation Centers, Information security professionals, product teams, and many more.

                </details>
                
<details><summary><strong>[vPrioritizer: Learn to say NO to almost every vulnerability (art of risk prioritisation…)](https://github.com/varchashva)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Pramod Rana](https://img.shields.io/badge/Pramod%20Rana-informational)

                As suggested by vulndb and cve, on a daily basis, approximately 50 new vulnerabilities become known to industry and even if an organization considers the impact rate of 10%, it’s still very challenging to manage it effectively and it’s safe to assume that count is going to increase furthermore. So with this amount organization is focusing (or should focus) on reducing the risk rather than eliminating it.

In current era, vulnerability management is (almost) equal to risk prioritisation because

- Resources (skillset and time) is limited in every organisation
- Environment is changing too fast and too frequently (ROI is less in analysis and remediation of a vulnerability if affected asset is not going to be live for a longer time - small attack surface)
- Attack surface is increasing exponentially in diversity (which again comes down to prioritisation)
- Remember the 80/20 rule - 20% of vulnerabilities bring 80% of risk

So what is risk? How do we calculate it? What are the factors contributing to risk?

1. CVSS (historically used) - No
2. Asset Criticality - No
3. Asset Accessibility - No
4. Exploit Applicability - No
5. Exploit Availability - No
6. Ease of Exploitation - No
7. Attack Surface - No
8. All of the Above - Yes

Theoretically, the above approach looks appropriate to adopt but practically it’s not possible to do it manually for every vulnerability affecting every asset by every organisation.

To overcome the above challenges I have prepared an open-source framework, vPrioritizer, which gives us ability to assess the risk on different layers such as (and hence comprehensive control on granularity of each component of risk):

- We can assign significance on per asset basis
- We can assess severity on per vulnerability basis
- At the same time, we can adjust both factors at asset & vulnerability relationship level
- On top of that, community analytics provides insights as suggested risk

This framework enables us to understand the contextualized risk pertaining to each asset by each vulnerability across the organization. It’s community based analytics provides a suggested risk for each vulnerability identified by vulnerability scanners and further strengthens risk prioritization process. So at any point of time teams can make an effective and more informed decision, based on unified and standardized data, about what (vulnerability/ties) they should remediate (or can afford not to) on which (asset/s).

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[Carnivore: Microsoft External Attack Tool](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Active_Directory.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Chris Nevin](https://img.shields.io/badge/Chris%20Nevin-informational)

                Carnivore is a username enumeration and password spraying tool for Microsoft services (Skype for Business, ADFS, RDWeb, Exchange and O365). It includes new post compromise functionality for Skype for Business (pulling the internal address list and user presence), and a new method for smart detection of the username format. Carnivore originally began as an on-premises Skype for Business enumeration/spray tool as, these days, organizations have often locked down their implementations of Exchange, however, Skype for Business has been left externally accessible, and does not seem to have received as much attention from penetration tests.

                </details>
                
<details><summary><strong>[FuzzCube](https://github.com/antojoseph/fc)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Anto Joseph](https://img.shields.io/badge/Anto%20Joseph-informational)

                Fuzzing over the ages has improved in tooling, logic, and process, but is still a number-crunching problem! You are improving your odds by throwing more CPU power at it.

How do we make it happen without hacking through custom solutions that cannot be reused? Enter FuzzCube - Batteries Included! FuzzCube comes with State Sharing Features, Mutation Engines and Crash Verification tools that you could leverage in your projects. It leverages Kubernetes for its infrastructure orchestration capabilities. Using Kubernetes operators, we abstract the complexity of deploying a fuzzing infrastructure with distributed high throughput workloads, fault tolerance, storage orchestration, and high scalability. We will practise distributed fuzzing in the era of Cloud Native Computing and use our new skills to find some 0days ;)

                </details>
                
<details><summary><strong>[macOS Bluetooth Analysis Suite (mBAS)](https://github.com/mathew-fleisch/def-con-schedule/blob/master/docs/conference.json)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Yu Wang](https://img.shields.io/badge/Yu%20Wang-informational)

                mBAS is a set of Bluetooth tools for macOS platforms, including Bluetooth HCI request sniffer, fuzzer and Broadcom firmware SoC tools, etc. Among them, the HCI fuzzer helped me discover many Bluetooth kernel vulnerabilities, such as CVE-2020-3892, CVE-2020-3893, CVE-2020-3905, CVE-2020-3907, CVE-2020-3908 and CVE-2020-3912. With these tools, we can better understand the design and implementation of Bluetooth subsystem of macOS and other platforms.

                </details>
                

### OSINT

<details><summary><strong>[KubiScan: Searching for Risky Pods and Permissions in Kubernetes Cluster](https://github.com/cyberark/KubiScan)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Eviatar Gerzi](https://img.shields.io/badge/Eviatar%20Gerzi-informational)

                KubiScan is a tool that was created to search for risky Pods which contain a privileged service account tokens that can be used for privilege escalation or even compromising the cluster. It can also show you all the risky roles, rolebindings, users and privileged pods in the Kubernetes Cluster and other cool stuff.

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[MUD-Visualizer](https://github.com/iot-onboarding/mud-visualizer)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Vafa Andalibi](https://img.shields.io/badge/Vafa%20Andalibi-informational)

                Manufacturer Usage Description (MUD) is a recently introduced IETF standard designed to protect IoT devices and networks by isolating IoT device based on the information that define the behavior of that device. The standard defines a straight-forward method to implement a defensive mechanism based on the rules that are introduced by manufacturer of the device. MUD-Files are the core component of the MUD standard and contain the access control information of IoT devices. However, MUD-Files may contain possibly hundreds of access control rules. As a result, reading and validating these files is a challenge; and determining how multiple IoT devices interact is difficult for the developer and infeasible for the consumer. MUD-Visualizer is a tool that provides a visualization of any number of MUD-Files and is designed to enable developers to produce correct MUD-Files by providing format corrections, integrating them with other MUD-Files, and identifying conflicts through visualization. MUD-Visualizer is scalable and its core task is to merge and illustrate ACEs for multiple devices; both within and beyond the local area network.

                </details>
                
