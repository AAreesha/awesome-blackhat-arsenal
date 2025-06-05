# USA 2023
---
## 🧠 Tools by Category
### Red Teaming

<details><summary><strong>[Abusing Microsoft SQL Server with SQLRecon](https://github.com/Tw1sm/PySQLRecon)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Sanjiv Kawa](https://img.shields.io/badge/Sanjiv%20Kawa-informational)

                In November 2022, Kaspersky Lab publicly released research which outlined that reoccurring attacks against Microsoft SQL Server rose by 56% (https://usa.kaspersky.com/about/press-releases/2022_kaspersky-finds-reoccurring-attacks-using-microsoft-sql-server-rise-by-56-in-2022).

I'd like to share a tool I wrote called SQLRecon, which will demonstrate how adversaries are leveraging Microsoft SQL services to facilitate with furthering their presence within enterprise networks through privilege escalation and lateral movement. I will also share defensive considerations which organizations can practically implement to mitigate attacks. I feel that this will add a fresh perspective on the various ancillary services within enterprise Windows networks which are under less scrutiny, however still ripe for abuse.

For red team operators, SQLRecon helps address the post-exploitation tooling gap by modernizing the approach operators can take when attacking SQL Servers. The tool is written in C#, rather than long-standing existing tools that use PowerShell or Python. SQLRecon has been designed with operational security and detection avoidance in mind – with a special focus on stealth, reconnaissance, lateral movement, and privilege escalation. The tool was designed to be modular, allowing for ease of extensibility from the hacker community. SQLRecon is compatible stand-alone or within a diverse set of command and control (C2) frameworks (Cobalt Strike, Nighthawk, Mythic, PoshC2, Sliver, Havoc, etc). When using the latter, SQLRecon can be executed either in-process, or through traditional fork and run.

Furthermore, I will be releasing a new version, one that is currently only used internally on advanced red team engagements by IBM X-Force Red's Adversary Services team.

                </details>
                
<details><summary><strong>[BloodHound 5.0](https://github.com/ly4k/BloodHound)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Andy Robbins](https://img.shields.io/badge/Andy%20Robbins-informational) ![Rohan Vazarkar](https://img.shields.io/badge/Rohan%20Vazarkar-informational)

                BloodHound 5.0 is faster, more powerful, and easier to deploy and use than any previous version. With this major update, we are completely overhauling BloodHound's code and bringing many features from the commercial versions of BloodHound to the free and open source version. That convergence means we can release features much faster, and that the application is much faster than it ever has been. It also means the deployment model is fundamentally changing.


Come see our Arsenal presentation to see how to set up and use BloodHound 5.0, including attack path analysis and execution demonstrations covering on-prem Active Directory and Azure.

                </details>
                
<details><summary><strong>[Commando VM and FLARE VM: Enhanced Toolsets for Penetration Testing and Windows-Based Malware Analysis](https://github.com/mandiant/commando-vm)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![George Litvinov](https://img.shields.io/badge/George%20Litvinov-informational) ![Alex Tselevich](https://img.shields.io/badge/Alex%20Tselevich-informational) ![Jake Barteaux](https://img.shields.io/badge/Jake%20Barteaux-informational) ![Dennis Tran](https://img.shields.io/badge/Dennis%20Tran-informational) ![Joseph Clay](https://img.shields.io/badge/Joseph%20Clay-informational)

                We are excited to release the latest version of Commando VM and showcase recent advancements of FLARE VM at the Black Hat Arsenal. Commando VM is a virtual machine distribution focused on penetration testing and red teaming. FLARE VM is tailored for malware analysis and reverse engineering. Both Windows-based tools have undergone significant enhancements to improve their usability, functionality, and efficiency. The projects now open source all packages, allowing the community to add and improve tools. Additionally, we have implemented a new GUI installation process to streamline the setup and configuration experience for both new and experienced users.

The latest iteration boasts new profiles for Commando VM, enabling users to tailor their environment to specific penetration testing and red teaming scenarios. Whether the user focuses on Cloud, Web App, or Internal testing, Commando VM has a ready-to-use profile for them with all relevant configurations and toolkit. In addition to that, the user can also create and save their own custom profile, allowing them to easily automate future VM deployments.

Furthermore, we have made substantial quality of life improvements, including debloating and performance optimization, resulting in faster, leaner, and more efficient virtual machines. Users will benefit from these enhancements as they navigate through the intricacies of malware analysis, reverse engineering, and penetration testing with the updated Commando VM and FLARE VM toolsets.

Join us at the Black Hat Arsenal to discover the power and flexibility of the next generation of Commando VM and FLARE VM. We will share how the updated tools can support your workflows in malware analysis, reverse engineering, and penetration testing. Additionally, you will learn how to contribute new tool and code updates benefiting thousands of analysts around the world.

                </details>
                
<details><summary><strong>[EvilnoVNC: Next-Gen Spear Phishing Attacks](https://github.com/JoelGMSec/EvilnoVNC)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Joel Gámez Molina](https://img.shields.io/badge/Joel%20Gámez%20Molina-informational)

                One of the main attack vectors in Red Team exercises, and possible entry points for an attacker, are phishing campaigns.

Currently, there are all kinds of tools and countermeasures to perform or defend against them, with a very high level of maturity and fully consolidated by the industry for many years.

On the other hand, there are hardly any tools oriented to Spear Phishing or any other type of more sophisticated attack, regardless of whether you are part of the Red Team or the Blue Team.

In this presentation, and from a totally offensive approach, we will explain how it has been possible to develop a new tool aimed at Spear Phishing, which will use techniques never seen before for this purpose, allowing us to see what the victim is doing in real time, intercept keystrokes with a keylogger, obtain and decrypt cookies, among many other things.

                </details>
                
<details><summary><strong>[Faraday: Open Source Vulnerability Manager](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/vulnerability_assessment/faraday.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Federico Kirschbaum](https://img.shields.io/badge/Federico%20Kirschbaum-informational)

                Faraday is a powerful and versatile security tool designed to help cybersecurity professionals perform effective and efficient penetration testing. It is an open-source framework that enables security testers to manage and track their penetration testing activities, from initial reconnaissance to final reporting.

With Faraday, users can integrate multiple tools and methodologies, including vulnerability scanning, exploitation, and post-exploitation techniques. It supports a wide range of tools, such as Metasploit, Nmap, and Burp Suite, and provides a central console to manage all the testing activities.

                </details>
                
<details><summary><strong>[Modern Active Directory Attacks with the Metasploit Framework](https://github.com/SP2-MC2/Readability-Resources/blob/master/cyberDictionary.txt)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Spencer McIntyre](https://img.shields.io/badge/Spencer%20McIntyre-informational)

                Active Directory is the foundation of the infrastructure for many organizations. As of 2023, Metasploit has added a wide range of new capabilities and attack workflows to support Active Directory exploitation. This Arsenal demonstration will cover new ways to enumerate information from LDAP, attacking Active Directory Certificate Services (AD CS), leveraging Role Based Constrained Delegation, and using Kerberos authentication.

The Kerberos features added in Metasploit 6.3 will be a focal point. The audience will learn how to execute multiple attack techniques, including Pass-The-Ticket (PTT), forging Golden/Silver Tickets, and authenticating with AD CS certificates. Finally, users will see how these attack primitives can be combined within Metasploit to streamline attack workflows with integrated ticket management. The demonstration will also highlight inspection capabilities that are useful for decrypting traffic and tickets for debugging and research purposes.

                </details>
                
<details><summary><strong>[SharpSCCM 2.0 - Abusing Microsoft's C2 Framework](https://github.com/subat0mik/Misconfiguration-Manager/blob/main/RESOURCES.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Chris Thompson](https://img.shields.io/badge/Chris%20Thompson-informational) ![Diego Lomellini](https://img.shields.io/badge/Diego%20Lomellini-informational)

                SharpSCCM 2.0 - Abusing Microsoft's C2 Framework

SharpSCCM is a post-exploitation tool designed to leverage Microsoft Endpoint Configuration Manager (a.k.a. ConfigMgr, formerly SCCM) for credential gathering and lateral movement without requiring access to the SCCM administration console GUI (e.g., from a C2 agent).

The release of SharpSCCM 2.0 includes new functionality to execute arbitrary commands on groups of devices, coerce NTLM authentication from remote SCCM clients that belong to specific users, dump and decrypt additional credentials from an SCCM client or by requesting them from a management point, and triage of local client files for software distribution point locations.

This session will include demonstrations of multiple techniques that can be used to take over an SCCM site, dump credentials from an SCCM client, execute arbitrary commands on remote SCCM clients, and coerce NTLM authentication from remote SCCM clients and servers.

Each demo will be followed by practical recommendations for mitigating these attacks and Q&A.

                </details>
                

### Web/AppSec

<details><summary><strong>[BlueMap - An Interactive Tool for Azure Exploitation](https://github.com/SikretaLabs/BlueMap)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Maor Tal](https://img.shields.io/badge/Maor%20Tal-informational)

                As demonstrated in BlackHat UK & Asia - BlueMap helps cloud red teamers and security researchers identify IAM misconfigurations, information gathering, and abuse of managed identities in interactive mode without ANY third-party dependencies. No more painful installations on the customer's environment, and No more need to custom the script to avoid SIEM detection!

The tool leaves minimum traffic in the network logs to help during red team engagements from on-prem to the cloud. Developed in Python and implemented all Azure integrations from scratch with zero dependencies on Powershell stuff. The idea behind the tool is to let security researchers and red team members have the ability to focus on more Opsec rather than DevOps stuff.

                </details>
                
<details><summary><strong>[Cloud AuthZ Trainer (CAZT)](https://github.com/Coalfire-Research/cazt)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Rodney Beede](https://img.shields.io/badge/Rodney%20Beede-informational)

                CAZT is a simulator of cloud-provider responsible REST APIs. It includes a lab manual for getting hands-on practice with how to attack authorization vulnerabilities in a cloud API.

It is different from other vulnerable cloud practice environments because it focuses on the cloud-provider shared responsibility instead of the customer. This enables pen testers to gain experience with testing the cloud vendor itself as well as an understanding of what a vulnerable cloud service will look like.

                </details>
                
<details><summary><strong>[Emulating Any HTTP Software as a Honeypot with HASH: A Deceptive Defense Against Cyberattacks](https://github.com/mmjang/AnkiIRExtension/blob/master/hwd.json)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Eslam Salem](https://img.shields.io/badge/Eslam%20Salem-informational)

                HASH (HTTP Agnostic Software Honeypot), an open-source framework for creating and launching low interaction honeypots. With simple YAML configuration files HASH can simulate any HTTP based software with built in randomization capabilities to avoid being identified.

                </details>
                
<details><summary><strong>[Nekuda: IDN-Squatting Detector](https://github.com/G4LB1T/Nekuda)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Gal Bitensky](https://img.shields.io/badge/Gal%20Bitensky-informational) ![Adi Pick](https://img.shields.io/badge/Adi%20Pick-informational)

                Put yourself in the shoes of a fraudster, you are trying to create a phishing website. Why inserting detectable unicode characters into a mostly-ASCII domain when you can register an entire domain in unicode? This is available when one uses a lesser-known feature called Internationalized Domain Name Top Level Domains (IDN TLD). Consider registering domains like google.com's lookalike in Hebrew - גוגל.קום, アマゾン.コム in Japanese instead of amazon.com or 微软.公司 which is the Chinese equivalent of microsoft.com.

Nekuda (dot in Hebrew) assists blue teamers to detect such domains. Its input is a string (e.g. the blue teamer's employer Brand name) and it emits over 150 potential IDN TLD domains and its registration status. It covers a potential gap in proactive phishing detection and prevention strategies and can be easily integrated into existing open-source tools like dnstwist.

                </details>
                
<details><summary><strong>[route-detect: Find Authentication and Authorization Security Bugs in Web Application Routes](https://github.com/mschwager)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Matt Schwager](https://img.shields.io/badge/Matt%20Schwager-informational)

                This demo introduces route-detect. route-detect is a command-line tool that seeks to aid security researchers and engineers in finding authentication (authn) and authorization (authz) security bugs in web application routes. These bugs are some of the most common security issues found today. The following industry standard resources highlight the severity of the issue:

- 2021 OWASP Top 10 #1 - Broken Access Control
- 2021 OWASP Top 10 #7 - Identification and Authentication Failures
- 2019 OWASP API Top 10 #2 - Broken User Authentication
- 2019 OWASP API Top 10 #5 - Broken Function Level Authorization

Of course, not all authn or authz bugs occur in web application routes, but route-detect seeks to confront this pervasive class of bugs.

                </details>
                

### Web/AppSec or Red Teaming

<details><summary><strong>[Build Inspector Open Source](https://github.com/vmware-archive/build-inspector)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Jeremy Banker](https://img.shields.io/badge/Jeremy%20Banker-informational)

                Build Inspector provides processing of plain-text CI/CD build and deployment logs with an eye towards identifying consumed and produced dependencies, along with identifying actions that introduce additional risk into the process. Quickly identify changes from one pipeline run to the next, and home in on spots where developers have added unnecessary risk or are performing actions that could be opportunities for a supply chain compromise.

                </details>
                
<details><summary><strong>[Daksh SCRA (Source Code Review Assist Tool)](https://github.com/coffeeandsecurity/DakshSCRA)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Debasis Mohanty](https://img.shields.io/badge/Debasis%20Mohanty-informational)

                Daksh SCRA is an open source tool that assists with manual source code review by providing helpful information to the code reviewer. This tool differs from traditional code review tools because it aims to help reviewers collect various details about the code base and identify areas of interest to review and confirm potential vulnerabilities. Even if code reviewers use automated code review tools, there are still many manual tasks they must perform to confirm findings and ensure precision in the code review process.

Although there are numerous automated code review tools available, none of them can perform a reconnaissance of the code base and provide code reviewers with useful insights. Typically, code reviewers must search for relevant information to confirm findings or ensure precision. Daksh SCRA offers valuable information such as technology and platform usage, functionalities, use cases, vulnerable patterns, and libraries used, among other data.

While most code review tools search for vulnerable patterns, they often report a high percentage of false positives. Daksh SCRA, on the other hand, is designed to be a reconnaissance tool that provides code reviewers with maximum insights about the target code base to assist with precise code review. Although Daksh SCRA is in its infancy stage, it is still a usable tool that supports a wide range of languages and platforms, and new features will be added in future releases.

                </details>
                
<details><summary><strong>[SCodeScanner - An Open-Source Source-Code Scanner](https://github.com/agrawalsmart7/scodescanner)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Utkarsh Agrawal](https://img.shields.io/badge/Utkarsh%20Agrawal-informational)

                SCodeScanner is a powerful tool for identifying vulnerabilities in source-code. It is designed to be easy to use and provides a range of features to help users quickly and accurately identify vulnerabilities with fewer false positives.

Some key features of SCodeScanner include:

- Support multiple languages: SCodeScanner is capable of scanning source code written in multiple languages such as JAVA, PHP and YAML. The most commonly used languages in web development.

- Relatively Less false positives: SCodeScanner includes flags that help to eliminate false positives and only report on vulnerabilities that are mostly confirmed to exist.

- Custom rules: SCodeScanner works with semgrep and allows users to create their own rules to scan for advanced patterns.

- Ability to track user input variables: SCodeScanner can identify instances where user input variables are defined in one file but used insecurely in another file for better coverage.

- Fast scanning: SCodeScanner's rules are designed to check for multiple vulnerabilities at once, which results in a faster scanning process.

- Integration: SCodeScanner can integrate with CI/CD pipelines and also pass results to bug-tracking services such as Jira and Slack, allowing users to easily share the results of their scans with their team.

- Scan mutltiple ways: It automatically download all git repo mentioned inside a txt file and start scan. Not only this but also support git, folder, file scans aswell.

Proof of results, SCodeScanner has already found 5 vulnerabilities in multiple Wordpress plugins and has been awarded following CVEs:

CVE-2022-1604
CVE-2022-1465
CVE-2022-1474
CVE-2022-1527
CVE-2022-1532

Overall, SCodeScanner is a valuable tool for any developer or security professional looking to identify vulnerabilities in their source-code before it is published in production. Its fast scanning, less false positives, and CI/CD pipeline integrations as well as bug-tracking services, make it a powerful tool for ensuring the security of your code.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[Defending software development ecosystems with Safe Package](https://github.com/lorin/resilience-engineering)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Mike Doyle](https://img.shields.io/badge/Mike%20Doyle-informational)

                With typosquatting, with account takeover, and with dependency hijacking attackers are using malicious packages to target our deployment pipelines. They mimic popular packages like Material Tailwind, hijack popular dependencies like event-stream, and compromise privileged accounts. This talk explains these classes of attack with examples and introduces safe-package, an open-source security wrapper for all kinds of package managers that neutralizes these attacks.

                </details>
                
<details><summary><strong>[Find Blind Spots in Your Security with Paladin Cloud](https://github.com/kagisearch/smallweb/blob/main/smallweb.txt)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![John Richards](https://img.shields.io/badge/John%20Richards-informational)

                Paladin Cloud is an extensible, Security-as-Code (SaC) platform designed to help developers and security teams reduce risks in their cloud environments. It functions as a policy management plane across multi-cloud and enterprise systems, protecting applications and data. The platform contains best practice security policies and performs continuous monitoring of cloud assets, prioritizing security violations based on severity levels to help you focus on the events that matter..

Its resource discovery capability creates an asset inventory, then evaluates security policies against each asset. Powerful visualization enables developers to quickly identify and remediate violations on a risk-adjusted basis. An auto-fix framework provides the ability to automatically respond to policy violations by taking predefined actions.

Paladin Cloud is more than a tool to manage cloud misconfiguration. It's a holistic cloud security platform that can be used for continuous monitoring and reporting across any domain.

                </details>
                
<details><summary><strong>[Grove: An Open-Source Log Collection Framework](https://gist.github.com/LisaDawn/7003846)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Peter Adkins](https://img.shields.io/badge/Peter%20Adkins-informational) ![Melissa Hardware](https://img.shields.io/badge/Melissa%20Hardware-informational)

                Grove is a log collection framework designed to support a unified way of collecting, storing, and routing logs from Software as a Service (SaaS) providers which do not natively support log streaming.

This is performed by periodically collecting logs from configured sources, and writing them to arbitrary destinations.

Grove enables teams to collect security related events from their vendors in a reliable and consistent way, while allowing this data to be stored and analyzed with existing tools.

                </details>
                
<details><summary><strong>[MELEE: A Tool to Identify Ransomware Infections in MySQL Deployments](https://github.com/adityaks/melee)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Aditya K Sood](https://img.shields.io/badge/Aditya%20K%20Sood-informational)

                Attackers are abusing MySQL instances for conducting nefarious operations on the Internet. The cybercriminals are targeting exposed MySQL instances and triggering infections at scale to exfiltrate data, destruct data, and extort money via ransom. For example one of the significant threats MySQL deployments face is ransomware. We have authored a tool named "MELEE" to detect potential infections in MySQL instances. The tool allows security researchers, penetration testers, and threat intelligence experts to detect compromised and infected MySQL instances running malicious code. The tool also enables you to conduct efficient research in the field of malware targeting cloud databases.

                </details>
                
<details><summary><strong>[Network Monitoring Tools for macOS](https://github.com/drduh/macOS-Security-and-Privacy-Guide)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Patrick Wardle](https://img.shields.io/badge/Patrick%20Wardle-informational)

                As the majority of malware contains networking capabilities, it is well understood that detecting unauthorized network access is a powerful detection heuristic. However, while the concepts of network traffic analysis and monitoring to detect malicious code are well established and widely implemented on platforms such as Windows, there remains a dearth of such capabilities on macOS.

Here, we will present various tools capable of enumerating network state, statistics, and traffic, directly on a macOS host. We will showcase open-source tools that leverage low-level APIs, private frameworks, and user-mode extensions that provide insight into all networking activity on macOS:

Specifically we'll demonstrate:

* A network monitor that allows one to explore all network sockets and connections, either via an interactive UI, or from the commandline.

* A DNS monitor that uses Apple's Network Extension Framework to monitors DNS requests and responses directly from the Terminal.

* A firewall that monitors and filters all network traffic, giving users with the ability to block unknown/unauthorized outgoing connections.

                </details>
                
<details><summary><strong>[Noriben: Quick and Easy Automated Malware Analysis Sandbox](https://github.com/Rurik/Noriben)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Brian Baskin](https://img.shields.io/badge/Brian%20Baskin-informational)

                Noriben is a Python-based tool that works Sysinternals Procmon to automatically collect, analyze, and report on runtime indicators of malware. It allows for the collection and analysis of unusual behavior on a system while attacks are being performed. The use of Noriben allows for manual analysis of malware while collecting its behavior, such as the use of command line arguments or manual debugging. With a host-based component, it can even run and collect info from thousands of malware samples automatically.

                </details>
                
<details><summary><strong>[ThreatPatrol](https://github.com/Viralmaniar)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Viral Maniar](https://img.shields.io/badge/Viral%20Maniar-informational)

                ThreatPatrol is a powerful open-source SaaS tool that offers Blue Teams a wealth of information on potential threats, allowing them to gain situational awareness and perform threat hunting. The tool's flexibility is a significant advantage, as it can be hosted on the cloud or on an internal standalone machine, providing users with the convenience and customisation options they need.

ThreatPatrol offers a comprehensive database of over 160 threat actor groups, indicators of compromise (IOCs), tactics, techniques, and procedures (TTPs), and their modus operandi out of the box. This information is regularly updated to ensure that users have access to the latest information on potential threats, providing insights into emerging threats and enabling proactive measures to prevent cyber-attacks.

Cyber Defenders can add, update, or degrade TTPs and IOCs for their network and map them to the MITRE Framework, which can be visualised on the dashboard in graph form, and generate reports for sharing with executive members. By proactively collecting and analysing data on potential threats, cyber teams can improve their situational awareness, enabling them to take appropriate action to prevent or mitigate attacks.

ThreatPatrol also provides feeds from over 100+ different sources, allowing organisations to stay up-to-date with the latest attack methods and trends, adjust their security posture, and protect themselves better against cyber threats. With improved situational awareness, organisations can respond more quickly and effectively when incidents occur, making ThreatPatrol an essential tool for protecting valuable data and avoiding the devastating consequences of a cyber-attack.

                </details>
                
<details><summary><strong>[Vovk - Advanced Dynamic Yara Rule Generator](https://github.com/ChanChiChoi/tiny-crawler/blob/master/paperMeta4arxiv_byArchive/arxiv-cs-2009.txt)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Vishal Thakur](https://img.shields.io/badge/Vishal%20Thakur-informational)

                Vovk - Debugging module for Advanced Dynamic Yara Rule Generation.
Vovk is a dynamic analysis tool that can be used as a module with the debugger (WinDBG). The tool itself is a DLL, built using both WdbgExts and DbgEng frameworks.
The way the tool works is pretty straightforward. You load Vovk into the debugger and then execute it. It runs through the malware and collects code snippets from memory and writes them to Yara file as a complete ruleset on the disk. You can then use the generated Yara ruleset to contain and neutralize malware campaigns or simply respond to security incidents that you are working on.

                </details>
                
<details><summary><strong>[YAMA: Yet Another Memory Analyzer for Malware Detection](https://github.com/t-tani)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Tomoaki Tani](https://img.shields.io/badge/Tomoaki%20Tani-informational) ![Shusei Tomonaga](https://img.shields.io/badge/Shusei%20Tomonaga-informational)

                YAMA is a system for generating tools that can inspect whether specific malware is present in memory during incident response. While numerous security countermeasure products exist for malware detection, targeted attacks utilizing malware that operates only in memory remain challenging to detect using existing products and continue to pose a threat.
Looking at existing open-source software (OSS) projects, some, such as PeSieve and Moneta, perform memory scans on live memory. However, few offer detection methods specifically tailored to particular malware for live systems. As file-less malware threats increase, having the means to verify the presence of malware in memory across multiple endpoints becomes crucial in incident response.
Using our proposed YAMA system, the scanner generated can create memory scanners tailored explicitly to any malware. The scanner generated by YAMA is a standalone executable capable of running on most 64-bit Windows OS. When infection investigation of malware present only in memory is required during incident response, executing the scanner created by YAMA on the suspected device will easily detect whether it is infected. Furthermore, in cases where a large-scale infection is suspected, the scanner can be distributed via Active Directory (AD) to clarify the infection status within the network.
YAMA is expected to be a powerful support tool for enhancing the investigative capabilities of Blue Teams, who conduct incident response daily.

                </details>
                

### Reverse Engineering

<details><summary><strong>[Glyph - An Architecture Independent Binary Analysis Tool for Fingerprinting Functions Through NLP](https://github.com/Xenios91)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Corey Hartman](https://img.shields.io/badge/Corey%20Hartman-informational)

                Reverse engineering is an important task performed by security researchers to identify vulnerable functions and malicious functions in IoT (Internet of Things) devices that are often shared across multiple devices of many system architectures. Common techniques to currently identify the reuse of these functions do not perform cross-architecture identification unless specific data such as unique strings are identified that may be of use in identifying a piece of code. Utilizing natural language processing techniques, Glyph allows you to upload an ELF binary (32 & 64 bit) for cross-architecture function fingerprinting, upon analysis, a web-based function symbol table will be created and presented to the user to aid in their analysis of binary executables/shared objects.

                </details>
                
<details><summary><strong>[SHAREM: Advanced Windows Shellcode Analysis Framework with Ghidra Plugin](https://github.com/Bw3ll/sharem)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Bramwell Brizendine](https://img.shields.io/badge/Bramwell%20Brizendine-informational) ![Jake Hince](https://img.shields.io/badge/Jake%20Hince-informational) ![Max Kersten](https://img.shields.io/badge/Max%20Kersten-informational)

                Shellcode can be cryptic, especially when encoded. Understanding its functionality is not straightforward. SHAREM is a cutting-edge Shellcode Analysis Framework, with both emulation and its own disassembler. SHAREM's unprecedented capabilities can allow us to unravel the mysteries of shellcode in new ways not seen.

Windows syscalls have become trendy in offensive security, yet SHAREM is the only tool that can emulate and log all user-mode Windows syscalls. Additionally, SHAREM also emulates and logs thousands of WinAPI functions. SHAREM is the only shellcode tool to parse and discover not only parameters, but also entire structures passed as parameters. SHAREM doesn't present parameters as hexadecimal values, but converts each to human readable format, in vivid colors.

Disassemblers like IDA Pro and Ghidra can be poor at disassembling shellcode accurately. SHAREM's disassembler is significantly more accurate with its original analysis capabilities. SHAREM additionally can uniquely integrate emulation results to provide flawless disassembly. Novel signature identifications are used to identify each function in the shellcode, and parameter values. SHAREM uses unique capabilities to accurately identify data, presenting data the correct way, not as misinterpreted instructions. SHAREM also uniquely provides complete-code coverage via emulation, capturing all functionality.

New at Arsenal, we will release a new script that allows SHAREM's output to be ingested by Ghidra. While Ghidra can handle shellcode in some cases, it simply cannot beat a framework specifically designed to handle and emulate shellcode. As such, this new release leverages SHAREM's advanced capabilities. Additionally, major updates include revamped complete-code coverage, timeless debugging of stack, nearly doubling the number of supported WinAPIs.

SHAREM provides unprecedented capabilities with encoded shellcode. Not only does it fully deobfuscate shellcode through emulation, discovering WinAPIs and syscalls, but it automatically recovers the shellcode's deobfuscated form. SHAREM presents error-free disassembly of its decoded form, with function calls and parameters labelled.

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[HIDE & SEEK: An Open Source Implant for Red Teams](https://github.com/mgeeky/ProtectMyTooling)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Jonathan Fischer](https://img.shields.io/badge/Jonathan%20Fischer-informational)

                Many Enterprises are shifting away from dedicated workstations and cubes, and moving to a more flexible workspace with thin client and desk hoteling. This creates the ideal landscape for hardware implant attacks. The current implant market, as it exists today, has not kept up with this shift. While closed source for-profit solutions exist, by their nature they lack the flexibility and customization to adapt to large scale targeted deployments. Open source projects similarly exist but focus more on individual workstations (dumb keyboards and remote terminals) relying on corporate networks for remote control and are easily detectable. Neither solution today is able to meet the needs of a modern Red Team.
This presentation introduces an open source, freely available hardware implant which adopts modern IoT technologies, leveraging non-standard communication channels to create a remotely managed mesh network of hardware implants. Attendees will learn about the new techniques and tactics that we used to create a new breed of open-source hardware implant. Topics covered in this presentation will include the scaling of implants for a stealthy enterprise takeover, creating and utilizing a flexible command and control mesh network, creating a new class of remote access shells that survive idle screen lock, and more. Attendees will leave the talk with new tactics and a new platform from which to innovate their own custom implants from. Live demos will be used to demonstrate these new tactics against real world infrastructure.
Previous hardware implant talks have covered: basic implants, their benefits, injecting keystrokes, Wi-Fi connectivity, and attack scripts. This presentation builds off of those but shows attendees how to leverage new techniques and technologies to push the innovation of hardware implants forward evolutionarily for use in today's modern Red Team operations.

                </details>
                
<details><summary><strong>[ICS Forensics Tools](https://github.com/nikhil130yadav/k-means-cluster-on-text-data/blob/master/output_30000words_3000Topics.txt)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Ori Perez](https://img.shields.io/badge/Ori%20Perez-informational) ![Maayan Shaul](https://img.shields.io/badge/Maayan%20Shaul-informational)

                open source forensic toolkit for analyzing Industrial PLC metadata and project files. ICS Forensics Tools enables investigators to identify suspicious artifacts on ICS environment for detection of compromised devices during incident response or manual check. ICS Forensics Tools is open source, which allows investigators to verify the actions of the tool or customize it to specific needs. We will be announcing two new forensics tools.These presentation will include live demonstrations, as well as a quick and easy-to-use forensics guide utilizing the tool. The tools will be available for immediate use, right before the session begins.

                </details>
                
<details><summary><strong>[Thunderstorm: Turning Off the Lights in Your Data Center](https://github.com/JoelGMSec/MyTalks)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Joel Gámez Molina](https://img.shields.io/badge/Joel%20Gámez%20Molina-informational)

                One of the main premises of any IT installation, is to protect the entire infrastructure against possible failures. In addition to firewalls and other network elements, one of the vital points is the electrical system.

Thanks to uninterruptible power supplies (UPS), it is possible to cover and manage these issues economically. The main problem, is that many of these systems inherit the same bugs as other IoT devices, which makes them vulnerable to all kinds of attacks.

In this presentation, we will explain how it has been possible to develop different zero-day vulnerabilities thanks to social engineering, some investment, and a bit of common sense. Among other things, these flaws would make it possible to compromise the electrical system of an office or even that of a Data Center.

Since these devices share common components, it would be possible to obtain remote code execution (with the highest possible privileges) and/or denial of service on more than 100 different manufacturers. Moreover, all of this has been automated in a single framework, making it possible to detect and exploit these vulnerabilities easily, simply and fully automatically.

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[SimpleRisk: Governance, Risk Management & Compliance](https://github.com/OWASP/www-chapter-austin/blob/master/pastevents.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Josh Sokol](https://img.shields.io/badge/Josh%20Sokol-informational)

                As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform organizational Governance, Risk Management, and Compliance activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to manage control frameworks, policies, and exceptions, facilitate audits, and perform risk prioritization and mitigation activities. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.

                </details>
                
