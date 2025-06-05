# USA 2018
---
## 🧠 Tools by Category
### Web/AppSec

<details><summary><strong>[A Look at ModSec 3.0 for NGINX: A Software Web Application Firewall](https://github.com/cranelab/webapp-tech)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Kevin Jones](https://img.shields.io/badge/Kevin%20Jones-informational)

                Today more and more websites are becoming subject to the constant and malevolent barrage coming from malicious hackers. A websites name can be tarnished quickly by a simple breach of their application stack. Web application security is becoming more and more a crucial part of the IT infrastructure, but what exactly does a WAF do and why do you need it? In this talk we will answer those questions.

We will first take a look at how the popular and highly adopted open source proxy server known as NGINX can be combined with the long respected open source web application firewall known as ModSecurity to achieve an effective and highly secure layer for your web application stack. We will explain the detailed benefits that NGINX and ModSecurity can provide, including protection from layer 7 attacks such as XSS, SQLi and LFI. We will showcase how the combination of these technologies can automatically block traffic from known malicious IP addresses. We will cover the visibility and auditing ModSecurity can provide from its detailed log files.

Lastly, we will walk through the setup process and configurations so that after attending this session you can easily and quickly setup NGINX and ModSecurity as a effective and highly secure web application firewall.

                </details>
                
<details><summary><strong>[Astra: Automated Security Testing For REST APIs](https://github.com/Surya443/NIT-Hackathon2023/blob/main/Indian%20Startup.csv)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Ankur Bhargava](https://img.shields.io/badge/Ankur%20Bhargava-informational) ![Prajal Kulkarni](https://img.shields.io/badge/Prajal%20Kulkarni-informational) ![Sagar Popat](https://img.shields.io/badge/Sagar%20Popat-informational)

                REST API penetration testing is complex due to continuous changes in existing APIs and addition of new APIs. Astra (Sanskrit: अस्त्र) can be used by security engineers or developers as an integral part of their process, so they can detect and patch vulnerabilities in the initial phase of the development cycle. Astra can automatically detect and test login & logout (Authentication API), which makes it easy for anyone to integrate this into CICD pipeline. Astra can take API collection as an input so this can also be used for testing APIs in stand-alone mode.

                </details>
                
<details><summary><strong>[Burp Replicator: Automate Reproduction of Complex Vulnerabilities](https://github.com/rajendrac3/Machine-Learning/blob/master/Apply%20Naive%20Bayes%20on%20Amazon%20reviews/Naive%20Bayes.ipynb)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Paul Johnston](https://img.shields.io/badge/Paul%20Johnston-informational)

                Developers often struggle to reproduce vulnerabilities discovered during pen tests. This is especially true for complex issues that need to bypass JavaScript validation, work with multi-step forms, handle dynamic CSRF tokens and more. This does not fit well with agile development where the ability to quickly reproduce problems enables efficient test driven development. Replicator solves this issue by allowing a pen tester to create a reproduction script that a developer can use on their system. Complex vulnerabilities can be confirmed with a single click, allowing the developer to stay in their productive coding flow. The tool is fully integrated with Burp Suite, making the script greatly easier to produce than a shell script, and keeping the tester in productive flow.

                </details>
                
<details><summary><strong>[OWASP Offensive Web Testing Framework](https://github.com/owtf/owtf/blob/develop/SECURITY.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Viyat Bhalodia](https://img.shields.io/badge/Viyat%20Bhalodia-informational)

                OWASP OWTF is a project focused on penetration testing efficiency and alignment of security tests to security standards like the OWASP Testing Guide (v3 and v4), the OWASP Top 10, PTES and NIST so that pentesters will have more time to

See the big picture and think out of the box
More efficiently find, verify and combine vulnerabilities
Have time to investigate complex vulnerabilities like business logic/architectural flaws
Perform more tactical/targeted fuzzing on seemingly risky areas
Demonstrate true impact despite the short timeframes we are typically given to test

OWTF is highly configurable and anybody can trivially create simple plugins or add new tests in the configuration files without having any development experience.

                </details>
                

### Red Teaming

<details><summary><strong>[ADRecon: Active Directory Recon](https://github.com/adrecon/ADRecon)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Prashant Mahajan](https://img.shields.io/badge/Prashant%20Mahajan-informational)

                ADRecon is a tool which extracts various artifacts (as highlighted below) out of an AD environment in a specially formatted Microsoft Excel report that includes summary views with metrics to facilitate analysis. The report can provide a holistic picture of the current state of the target AD environment. The tool is useful to various classes of security professionals like system administrators, security professionals, DFIR, etc. It can also be an invaluable post-exploitation tool for a penetration tester. It can be run from any workstation that is connected to the environment, even hosts that are not domain members. Furthermore, the tool can be executed in the context of a non-privileged (i.e. standard domain user) accounts. Fine Grained Password Policy, LAPS and BitLocker may require Privileged user accounts. The tool will use Microsoft Remote Server Administration Tools (RSAT) if available, otherwise it will communicate with the Domain Controller using LDAP.

The following information is gathered by the tool: Forest; Domain; Trusts; Sites; Subnets; Default Password Policy; Fine Grained Password Policy (if implemented); Domain Controllers, SMB versions, whether SMB Signing is supported and FSMO roles; Users and their attributes; Service Principal Names (SPNs); Groups and memberships; Organizational Units (OUs); ACLs for the Domain, OUs, Root Containers and GroupPolicy objects; Group Policy Object details; DNS Zones and Records; Printers; Computers and their attributes; LAPS passwords (if implemented); BitLocker Recovery Keys (if implemented); and GPOReport (requires RSAT).

Available at https://github.com/sense-of-security/ADRecon

                </details>
                
<details><summary><strong>[Armory](https://github.com/depthsecurity/armory-docker/blob/master/launch_api.sh)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Daniel Lawson](https://img.shields.io/badge/Daniel%20Lawson-informational)

                Armory is a tool designed to run various existing tools, collating all of the output into a local database, and using that information for further attacks. It is extremely modular, and it is pretty easy to create custom modules and reports. Armory's purpose is to streamline client discovery and external penetration tests.

                </details>
                
<details><summary><strong>[BloodHound 1.5](https://github.com/chryzsh/awesome-bloodhound)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Andy Robbins](https://img.shields.io/badge/Andy%20Robbins-informational) ![Rohan Vazarkar](https://img.shields.io/badge/Rohan%20Vazarkar-informational) ![Will Schroeder](https://img.shields.io/badge/Will%20Schroeder-informational)

                BloodHound is a single page Javascript web application, built on top of Linkurious, compiled with Electron, with a Neo4j database fed by a PowerShell ingestor. BloodHound uses graph theory to reveal the hidden and often unintended relationships within an Active Directory environment. Attackers can use BloodHound to easily identify highly complex attack paths that would otherwise be impossible to quickly identify. Defenders can use BloodHound to identify and eliminate those same attack paths. Both blue and red teams can use BloodHound to easily gain a deeper understanding of privilege relationships in an Active Directory environment. BloodHound is developed by @_wald0, @CptJesus, and @harmj0y.

                </details>
                
<details><summary><strong>[Chiron: An Advanced IPv6 Security Assessment and Penetration Testing Framework](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Network_Attacks.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Antonios Atlasis](https://img.shields.io/badge/Antonios%20Atlasis-informational)

                Chiron is an IPv6 Security Assessment Framework, written in Python and employing Scapy. It is comprised of the following modules:

• IPv6 Scanner
• IPv6 Local Link
• IPv4-to-IPv6 Proxy
• IPv6 Attack Module
• IPv6 Proxy
All the above modules are supported by a common library that allows the creation of completely arbitrary IPv6 header chains, fragmented or not. Suggested host OS: Linux (*BSD may also work).

Source Code: https://github.com/aatlasis/Chiron﻿

                </details>
                
<details><summary><strong>[CoffeeShot: Avoid Detection with Memory Injection](https://github.com/MinervaLabsResearch/CoffeeShot)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Asaf Aprozper](https://img.shields.io/badge/Asaf%20Aprozper-informational)

                For the first time ever, we are introducing a framework that utilizes the usage of Java Native Access with Java. How did we take advantage of that? Well, we used this to call to interesting Windows API's directly from Java. CoffeeShot is a framework that was designed for creating Java-based malware which bypasses most of the anti-virus vendors. CoffeeShot utilizes the features of JNA to look for a victim process, once it finds it - a shellcode will be injected directly from the Java Archive file (JAR).

Java malware like "Jrat" and "Adwind" are used by malicious adversaries day by day, more and more. Their main reason for writing malware in Java is to be evasive and avoid security products – including those that use advanced features like machine learning. To overcome the above, blue-teamers can use this framework and thereby understand their status of anti-malware weakness against Java-based malware.

On the other hand, CoffeeShot can be applied by penetration testers as well. The framework provides red-teamers a friendly toolset by allowing them to embed any shellcode in a JAR file, assisting them to avoid detection with memory injection and to PWN the target!

                </details>
                
<details><summary><strong>[DELTA: SDN Security Evaluation Framework](https://github.com/seungsoo-lee/DELTA)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Jinwoo Kim](https://img.shields.io/badge/Jinwoo%20Kim-informational) ![Seungsoo Lee](https://img.shields.io/badge/Seungsoo%20Lee-informational) ![Seungwon Shin](https://img.shields.io/badge/Seungwon%20Shin-informational) ![Seungwon Woo](https://img.shields.io/badge/Seungwon%20Woo-informational)

                Software-Defined Networking (SDN) allows network operators to manage the entire network in a centralized manner by separating the vendor specific control plane from legacy routers/switches. Thus, this concept provides an intelligent way to design novel network functions. However, although SDN offers significant advantages over the traditional networking, the security of SDN has not been sufficiently verified. So, here, we introduce an open source tool for systematically assessing the security of SDN called DELTA.

DELTA is a first SDN security evaluation framework, which has two primary functions; (1) It can automatically instantiate known attack cases against SDN elements across diverse environments, and (2) it can assist in uncovering unknown security problems within an SDN deployment. For replaying attack cases, our framework has a number of test cases against open source SDN controllers and all SDN-enabled switch devices (software and hardware). Also, our framework provides a protocol-aware fuzzer for OpenFlow, which is a de-facto standard protocol of SDN, in order to find new vulnerabilities.

DELTA has following main features:

Fully automatically reproduce 40 published exploits against all SDN components composed of SDN controllers, a control channel, and OpenFlow-enabled switches.
Provide a blackbox fuzzing module that randomizes OpenFlow messages.
Support for both VM-based all-in-one single machine and hardware-based environments.
Fully compatible with promising SDN controllers (ONOS, OpenDaylight, Floodlight, and Ryu).
[NEW] Support additional 7 new attacks against SDN switches (i.e., OVS, HP, and Pica8), which are discovered from DELTA fuzzing module.
[NEW] Support DISTRIBUTED controller testing and related attack cases.
[NEW] Provide a new fuzzing module that discovers security problems of REST-API implementations in SDN controllers and related attack cases.

                </details>
                
<details><summary><strong>[DSP: Docker Security Playground](https://github.com/DockerSecurityPlayground/DSP)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Simon Pietro Romano](https://img.shields.io/badge/Simon%20Pietro%20Romano-informational)

                This presentation covers the design and implementation of the Docker Security Playground (DSP), an architecture leveraging a microservices-based approach in order to build complex network infrastructures specifically tailored to the study of network security. DSP has been conceived at the outset as a tool for learning network security with a hands-on approach. A number of security labs have been already realized and made available in a public repository. The talk discusses how such labs can be fruitfully exploited by students, as well as presents the Application Programming Interface offered to programmers interested in the implementation of new labs.

                </details>
                
<details><summary><strong>[Foxtrot C2: A Journey of Payload Delivery](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/RT.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Dimitry Snezhkov](https://img.shields.io/badge/Dimitry%20Snezhkov-informational)

                Execution of an offensive payload may begin with a safe delivery of the payload to the endpoint itself. When secure connections in the enterprise are inspected, reliance only on transmission level security may not be enough to accomplish that goal. Foxtrot C2 serves one goal: safe last mile delivery of payloads and commands between the external network and the internal point of presence, traversing intercepting proxies, with the end-to-end application level encryption.

While the idea of end-to-end application encryption is certainly not new, the exact mechanism of Foxtrot's delivery implementation has advantages to Red Teams as it relies on a well known third party site, enjoying elevated ranking and above average domain fronting features. Payload delivery involves several OpSec defenses: sensible protection from direct attribution, active link expiration to evade consistent interception, inspection, tracking and replay activities by the defenders. Asymmetric communication channels are also planned.

And if your standalone Foxtrot agent is caught, the delivery mechanism may live on, you could still manually bring the agent back into the environment via the browser. A concept tool built on these ideas will be presented and released. It will be used as basis for our discussion.

                </details>
                
<details><summary><strong>[Humble Chameleon: Eating 2FA for Breakfast](https://github.com/claissg/humble_chameleon)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Forrest Kasler](https://img.shields.io/badge/Forrest%20Kasler-informational)

                By creating a simple tool that performs a man-in-the-middle attack against the HTTP protocol, we can eliminate the need to manually create phishing sites. In addition, this same tool can be used to harvest session cookies from applications that require 2FA, disallow victims from logging out and killing our stolen cookies, hide phishing domains behind legitimate content, categorize phishing domains, serve malware alongside legitimate content, only serve payloads in response to whitelisted requests, and target multiple services at the same time, all without SSL warnings. *Note: This is not just a tool, but a release of a new attack methodology.

                </details>
                
<details><summary><strong>[Mallet: An Intercepting Proxy for Arbitrary Protocols](https://github.com/sensepost/mallet)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Rogan Dawes](https://img.shields.io/badge/Rogan%20Dawes-informational)

                This prsentation will focus on a new open-source intercepting proxy named Mallet, based on the mature and high-performance Netty framework, that wraps it with a drag and drop graph-based graphical user interface and a datastore. In doing so, we gain access to an existing library of protocol implementations, including TLS (and SNI), various compression algorithms, HTTP, HTTP/2, MQTT, REDIS, and many others, and most important, an existing community of developers creating new protocol decoders and encoders, and the associated body of knowledge in this area.

The Mallet user interface closely follows the Netty model, making it simple to construct a pipeline of encoders and decoders by dragging existing codecs, or adding your own codecs or script blocks to a palette, taking the researcher from a simple TCP intercept-and-forward proxy, to a full-blown protocol stack with scriptable processing, with every change being recorded for review and replay in a subsequent connection. As Netty supports a variety of transports, from the common TCP and UDP to SCTP, Serial Port and File, as well as native kqueue and epoll transports, Mallet can be used to intercept all sorts of data, however you may find it.

Source Code: https://github.com/SensePost/Mallet

                </details>
                
<details><summary><strong>[PowerUpSQL: A PowerShell Toolkit for Attacking SQL Serversin Enterprise Environments](https://github.com/NetSPI/PowerUpSQL)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Antti Rantasaari](https://img.shields.io/badge/Antti%20Rantasaari-informational) ![Scott Sutherland](https://img.shields.io/badge/Scott%20Sutherland-informational)

                PowerUpSQL includes functions that support SQL Server discovery, weak configuration auditing, privilege escalation on scale, and post exploitation actions such as OS command execution. It is intended to be used during internal penetration tests and red team engagements. However, PowerUpSQL also includes many functions that can be used by administrators to quickly inventory the SQL Servers in their ADS domain and perform common threat hunting tasks related to SQL Server. This should be interesting to red, blue, and purple teams interested in automating day to day tasks involving SQL Server.

Source Code: https://github.com/netspi/powerupsql
Slides: https://bit.ly/2OxbGYy﻿
Video: https://youtu.be/UX_tBJQtqW0

                </details>
                
<details><summary><strong>[RID Hijacking: Maintaining Access on Windows Machines](https://github.com/ustayready/tradecraft/blob/master/offensive-security/persistence/rid-hijacking.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Sebastián Castro](https://img.shields.io/badge/Sebastián%20Castro-informational)

                The art of persistence is (and will be...) a matter of concern when successfully exploitation is achieved. Sometimes it is pretty tricky to maintain access on certain environments, especially when it is not possible to execute common vectors like creating or adding users to privileged groups, dumping credentials or hashes, deploying a persistent shell, or anything that could trigger an alert on the victim. This statement ratifies why it's necessary to use discrete and stealthy techniques to keep an open door right after obtaining a high privilege access on the target.

What could be more convenient that only use OS resources in order to persist an access? This presentation will provide a new post-exploitation hook applicable to all Windows versions called RID Hijacking, which allows setting desired privileges to an existent account in a stealthy manner by modifying some security attributes. To show its effectiveness, the attack will be demonstrated by using a module which was recently added by Rapid7 to their Metasploit Framework, and developed by the security researcher Sebastián Castro.

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[Adversarial Robustness Toolbox for Machine Learning Models - ARSENAL THEATER DEMO](https://gist.github.com/standardgalactic/7f03809c56f4b098b95a50ada32cd02c)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Irina Nicolae](https://img.shields.io/badge/Irina%20Nicolae-informational)

                Adversarial attacks of machine learning systems have become an undisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (so-called poisoning attacks), or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (so-called evasion attacks). Adversarial attacks have been demonstrated in a number of different application domains, including malware detection, spam filtering, visual recognition, speech-to-text conversion, and natural language understanding. Devising comprehensive defences against poisoning and evasion attacks by adaptive adversaries is still an open challenge.

We will present the Adversarial Robustness Toolbox (ART), a library which allows rapid crafting and analysis of both attacks and defence methods for machine learning models. It provides an implementation for many state-of-the-art methods for attacking and defending machine learning. Through ART, the attendees will (re)discover how to attack and defend machine learning systems.

                </details>
                
<details><summary><strong>[Archery: Open Source Vulnerability Assessment and Management - ARSENAL THEATER DEMO](https://github.com/google-research-datasets/gap-coreference/blob/master/gap-test.tsv)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Anand Tiwari](https://img.shields.io/badge/Anand%20Tiwari-informational)

                Archery is an open-source vulnerability assessment and management tool that helps developers and pentesters to perform scans and manage vulnerabilities. Archery uses popular open-source tools to perform comprehensive scanning for web application and network. It also performs web application dynamic authenticated scanning and covers the whole applications by using selenium. The developers can also utilize the tool for implementation of their DevOps CI/CD environment.

The main capabilities of our Archery include:

Perform Web and Network Vulnerability Scanning using vulnerability scanner tools
Correlates and Collaborate all raw scans data, show them in a consolidated manner
Perform authenticated web scanning
Perform web application scanning using selenium
Automate your scanners
Vulnerability Management including Web, Network and Mobile Applications
Enable REST API's for developers to perform scanning and Vulnerability Management
Useful for DevOps teams for Vulnerability Management

                </details>
                
<details><summary><strong>[boofuzz](https://github.com/jtpereyda)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Joshua Pereyda](https://img.shields.io/badge/Joshua%20Pereyda-informational)

                boofuzz is an open-source network protocol fuzzing framework, competing with closed source commercial products like Defensics and Peach. Inheriting from the open source tools Spike and Sulley, boofuzz improves on a long line of block-based fuzzing frameworks.

The fuzzing framework allows hackers to specify protocol formats, and boofuzz does the heavy lifting of generating mutations specific to the format. boofuzz makes developing protocol-specific "smart" fuzzers relatively easy. Make no mistake, designing a smart network protocol fuzzer is no trivial task, but boofuzz provides a solid foundation for producing quality fuzzers.

Written in Python, boofuzz builds on its predecessor, Sulley, with key features including:

Online documentation
More extensibility including support for arbitrary communications mediums
Built-in support for serial fuzzing, ethernet- and IP-layer, UDP broadcast
Much easier install experience!
Far fewer bugs

Source Code: https://github.com/jtpereyda/boofuzz

                </details>
                
<details><summary><strong>[BTA](https://github.com/atktgs/BlackHat2015Arsenal)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Joffrey CZARNY](https://img.shields.io/badge/Joffrey%20CZARNY-informational)

                When it comes to the security of the information system, Active Directory domain controllers are, or should be, at the center of concerns, which are (normally) to ensure compliance with best practices, and during a compromise proved to explore the possibility of cleaning the information system without having to rebuild Active Directory. However, few tools implement this process; there are more and more offensive tools to target Active Directory and several ways exist to backdoor Active Directory.

We propose to present some possible backdoors which could be set by an intruder in Active Directory to keep administration rights. For example, how to modify the AdminSDHolder container in order to reapply rights after administrator actions. Moreover, backdoors can be implemented in Active Directory to help an intruder to gain back his privileges. Then, we will present the last features in BTA, which help to detected all mis-configurations that can be abused to bypass Administrative Forest Design Approach "ESAE", as DCsync rights, Exchange privileges...

The presentation will be organized as follows:

We begin by demonstrating some backdoors in order to keep admins rights or to help an intruder to quickly recover admins rights.
We will continue by describing all mis-configurations that can be abused to bypass ESAE design, as DCsync rights, Exchange privileges...
We conclude with a feedback on real world usage of BTA.

More information can be found on the Bitbucket repository: https://github.com/airbus-seclab/bta

                </details>
                
<details><summary><strong>[Deep Exploit](https://github.com/TheDreamPort/deep_exploit)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Isao Takaesu](https://img.shields.io/badge/Isao%20Takaesu-informational)

                DeepExploit is fully automated penetration tool linked with Metasploit. It identifies the status of all opened ports on the target server and executes the exploit at pinpoint using Machine Learning.

Deep Exploit's key features are the following:

Self-learning: DeepExploit can learn how to exploitation by itself (uses reinforcement learning). It is not necessary for humans to prepare learning data.
Efficiently execute exploit: DeepExploit can execute exploits at pinpoint (minimum 1 attempt) using self-learned data.
Deep penetration: If DeepExploit succeeds the exploit to the target server, it further executes the exploit to other internal servers.
Operation is very easy: Your only operation is to input one command. It is very easy!
Learning time is very fast: DeepExploit uses distributed learning by multi agents. So, we adopted an advanced machine learning model called A3C.

Current Deep Exploit's version is a beta, but it can fully automatically execute following actions:

Intelligence gathering
Threat modeling
Vulnerability analysis
Exploitation
Post-Exploitation
Reporting

By using our DeepExploit, you will benefit from the following:

For pentesters: (a) They can greatly improve the test efficiency; (b) The more pentesters use DeepExploit, DeepExploit learns how to method of exploitation using machine learning. As a result, accuracy of test can be improve.
For Information Security Officers: (c) They can quickly identify vulnerabilities of own servers. As a result, prevent that attackers attack to your servers using vulnerabilities, and protect your reputation by avoiding the negative media coverage after breach.

Because attack methods to servers are evolving day by day, there is no guarantee that yesterday's security countermeasures are safety today. It is necessary to quickly find vulnerabilities and take countermeasures. Our DeepExploit will contribute greatly to keep your safety.

Source Code:
https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/DeepExploit

Document:
https://github.com/13o-bbr-bbq/machine_learning_security/blob/master/DeepExploit/doc/BHUSA2018Arsenal_20180802.pdf﻿

                </details>
                
<details><summary><strong>[Halcyon IDE: For Nmap Script Developers](https://github.com/s4n7h0/Halcyon-IDE)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Sanoop Thomas](https://img.shields.io/badge/Sanoop%20Thomas-informational)

                Halcyon IDE lets you quickly and easily develop Nmap scripts for performing advanced scans on applications and infrastructures with a wide range capabilities from recon to exploitation. It is the first IDE released exclusively for Nmap script development. Halcyon IDE is free and open source project (always will be) released under MIT license to provide an easier development interface for rapidly growing information security community around the world. The project was initially started as an evening free time "coffee shop" project and has taken a serious step for its developer/contributors to spend dedicated time for its improvements very actively.

Source Code: https://halcyon-ide.org﻿

                </details>
                
<details><summary><strong>[SimpleRisk: ARSENAL THEATER DEMO](https://gist.github.com/williballenthin/28c73da6cbf5e76e137a9100ab45697f)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Josh Sokol](https://img.shields.io/badge/Josh%20Sokol-informational)

                As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk, via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform risk management activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to submit risks, plan mitigations, facilitate management reviews, prioritize for project planning, and track regular reviews. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.

Source Code: https://github.com/simplerisk

                </details>
                
<details><summary><strong>[V2X Validation Tool](https://github.com/ryanbgriffiths/IROS2023PaperList/blob/main/README.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Jonathan Petit](https://img.shields.io/badge/Jonathan%20Petit-informational) ![Raashid Ansari](https://img.shields.io/badge/Raashid%20Ansari-informational)

                The V2X Validation Tool (called dsrcvt because focused on DSRC technology) facilitates penetration testing on automotive On-Board Units (OBUs) used for Vehicle-to-X communication. Currently, dsrcvt is capable of sending unsigned or signed Basic Safety Messages (BSMs) by re-signing a recorded BSM sent for automotive onboard units. Using these BSMs it tries to cause a surge in an OBU's processing power. It also attempts to bypass the security checks posed by the IEEE 1609.2 security layer. An enhanced version of dsrcvt (dsrcvt-crafter) facilitates crafting entirely custom BSMs from scratch, conforming to the IEEE 1609 standards family. dsrcvt also comes as an OBU fuzzer that can fuzz user-selected fields of a BSM to pen-test OBU implementations.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[Art of Dancing with Shackles: Best Practice of App Store Malware Automatic Hunting System](https://github.com/lilang-wu/iOS-AppStore-Malware-Automatic-Hunting-System)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Ju Zhu](https://img.shields.io/badge/Ju%20Zhu-informational) ![Lilang Wu](https://img.shields.io/badge/Lilang%20Wu-informational) ![Moony Li](https://img.shields.io/badge/Moony%20Li-informational)

                We all know the iOS system from Apple to be one of the most secure among all popular operating systems. From a technical view, the protection feature of sandbox gardened application, runtime code signing check, hardware level application code packing protection and so forth, and Apple Store security check policy is extremely strict - before any application is released on Apple Store.

However, this is bad news for security vendors, for the defense protection solution has no chance being granted sufficient privilege to detect and defeat attacks in deep level, when end user suffered real APT attack such as PEGASUS. Our tools is aimed at introducing the tricks and lessons of Apple Store apps automatic crawling and security sandbox automatic analysis systems for security researchers and security vendors in the world.

Source Code: https://github.com/dongyangwu/iOS-AppStore-Malware-Automatic-Hunting-System

                </details>
                
<details><summary><strong>[Bro: Do You Bro? Beginner to Expert](https://github.com/bro/broctl/blob/master/CHANGES)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Seth Hall](https://img.shields.io/badge/Seth%20Hall-informational)

                The Bro Network Security Monitor is an open-source framework that gives total visibility over network traffic in real-time. Since most cyber attacks cross the network (and hosts themselves can be compromised), threat hunters and incident responders typically rely on network data as a vital source of truth, to reconstruct what really happened (or is happening now) in their environment. Bro is perhaps the best and most widely used tool for network traffic analysis. Join us to learn more about Bro with Seth Hall, longtime Bro developer, and see a demo where he will provide a comprehensive overview of Bro, from introduction to advanced custom scripting.

                </details>
                
<details><summary><strong>[CyBot: Open-Source Threat Intelligence Chat Bot (Full Circle)](https://github.com/avinashshenoy97/awesome-python-1/blob/master/README.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Tony Lee](https://img.shields.io/badge/Tony%20Lee-informational)

                Threat intelligence chat bots are useful friends. They perform research for you and can even be note takers or central aggregators of information. However, it seems like most organizations want to design their own bot in isolation and keep it internal. To counter this trend, our goal was to create a repeatable process using a completely free open source framework, an inexpensive Raspberry Pi (or even virtual machine), and host a community-driven plugin framework to open up the world of threat intel chat bots to everyone from the average home user to the largest security operations center.

We were thrilled to debut the end result of our research (a chat bot that we affectionately call CyBot) at Black Hat Arsenal Vegas 2017. To build on that momentum we also brought CyBot to Black Hat Europe and Asia to gather more great feedback and ideas from an enthusiastic international crowd. This year's Black Hat Vegas will allow us to share new features that stemmed from Black Hat Asia feedback as well as lessons learned from the global collaboration effort.

Best of all, if you know even a little bit of Python, you can help our collaboration efforts by writing plugins and sharing them with the community. If you want to build your own CyBot, the instructions in this project will let you do so with about an hour of invested time and anywhere from $0-$35 in expenses. Come make your own threat intelligence chat bot today!

                </details>
                
<details><summary><strong>[DeepViolet: SSL/TLS Scanning API & Tools](https://github.com/spoofzu/DeepViolet/blob/master/src/main/java/com/mps/deepviolet/api/CipherSuiteUtil.java)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Milton Smith](https://img.shields.io/badge/Milton%20Smith-informational)

                DeepViolet TLS/SSL scanner is an information gathering tool to test TLS/SSL configuration on secure web servers. DeepViolet is an API written in Java. Two proof of concept tools implement the API to demonstrate DeepViolet running from the command line or alternatively from a desktop application. Features of DeepViolet include enumeration of web server cipher suites, display X.509 certificate metadata, examine X.509 certificate trust chains, user configurable ciphersuite naming conventions and more. DeepViolet is an OWASP open source project written to help educate the technical community around TLS/SSL and strengthen knowledge of security protocols while strengthen security of web applications. DeepViolet project is always looking for volunteers.

Source Code: https://github.com/spoofzu/DeepViolet

                </details>
                
<details><summary><strong>[DejaVu: An Open Source Deception Framework](https://github.com/bhdresh/Dejavu)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Bhadreshkumar Patel](https://img.shields.io/badge/Bhadreshkumar%20Patel-informational) ![Harish Ramadoss](https://img.shields.io/badge/Harish%20Ramadoss-informational)

                Deception techniques - if deployed well - can be very effective for organizations to improve network defense and can be a useful arsenal for blue teams to detect attacks at very early stage of cyber kill chain. But the challenge we have seen is deploying, managing and administering decoys across large networks is still not easy and becomes complex for defenders to manage this over time. Although there are a lot of commercial tools in this space, we haven't come across open source tools which can achieve this.

With this in mind, we have developed DejaVu which is an open source deception framework which can be used to deploy across the infrastructure. This could be used by the defender to deploy multiple interactive decoys (HTTP Servers, SQL, SMB, FTP, SSH, client side – NBNS) strategically across their network on different VLAN's. To ease the management of decoys, we have built a web-based platform which can be used to deploy, administer and configure all the decoys effectively from a centralized console. Logging and alerting dashboard displays detailed information about the alerts generated and can be further configured on how these alerts should be handled. If certain IP's like in-house vulnerability scanner, SCCM etc. needs to be whitelisted, this can be configured which effectively would mean very few false positives.

Alerts only occur when an adversary is engaged with the decoy, so now when the attacker touches the decoy during reconnaissance or performs authentication attempts this raises a high accuracy alert which should be investigated by the defense. Decoys can also be placed on the client VLAN's to detect client side attacks such as responder/LLMNR attacks using client side decoys. Additionally, common attacks which the adversary uses to compromise such as abusing Tomcat/SQL server for initial foothold can be deployed as decoys, luring the attacker and enabling detection.

                </details>
                
<details><summary><strong>[Firmware Audit: Platform Firmware Security Automation for Blue Teams and DFIR](https://github.com/viktorbezdek/awesome-github-projects)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Lee Fisher](https://img.shields.io/badge/Lee%20Fisher-informational) ![Paul English](https://img.shields.io/badge/Paul%20English-informational)

                The first major release of our platform firmware security automation tool, Firmware Audit, aka: fwaudit. fwaudit automates the running and forensic hashing of output and firmware blobs for a variety of platform firmwares and across a variety of FOSS tools. fwaudit provides a pre-composed profiles for defense, exploration and forensics, to reduce the risk of bricking and maximize operational uptime.

                </details>
                
<details><summary><strong>[Kemon: An Open-Source Pre and Post Callback-Based Framework for macOS Kernel Monitoring](https://github.com/karteum/starred)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Yu Wang](https://img.shields.io/badge/Yu%20Wang-informational)

                If third-party vendors want to add new features to the macOS kernel, such as antivirus capabilities, ransomware blocking, data breach auditing, behavior monitoring and so on, they usually need the support of the system's exported interfaces. At present, only two known official interfaces are available, they are Kernel Authorization subsystem and Mandatory Access Control framework. Unfortunately, neither of them are suitable for today's kernel development tasks. The Kernel Authorization KPIs was designed thirteen years ago and it is clear that it lacks the necessary maintenance and upgrades. For example, there are only seven file operation related notification callbacks available, which are obviously not enough. For each notification callback (KAUTH_SCOPE_FILEOP), we cannot modify the return results. For some specific callback functions, the input parameters lack critical context information. As for the Mandatory Access Control framework, Apple directly claims that third parties should not use these private interfaces, this mechanism is not part of the KPI.

In order to bring about some changes, I'd like to introduce you to Kemon, an open source Pre and Post-operation based kernel callback framework. With the power of Kemon, we can easily implement LPC communication monitoring, MAC policy filtering, kernel driver firewall, etc. In general, from an attacker's perspective, this framework can help achieve more powerful Rootkit. From the perspective of defense, Kemon can help construct more granular monitoring capabilities. I also implemented a kernel fuzzer through this framework, which helped me find many vulnerabilities, such as: CVE-2017-7155, CVE-2017-7163, CVE-2017-13883, etc.

Source Code: https://github.com/didi/kemon
Documentation: https://github.com/didi/kemon/blob/master/doc/Kemon

                </details>
                
<details><summary><strong>[Learn How to Build Your Own Utility to Monitor Malicious Behaviors of Malware on macOS](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/L-SM-TH.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Kai Lu](https://img.shields.io/badge/Kai%20Lu-informational)

                The landscape of macOS malware has changed dramatically in the past couple of years. Threats are becoming more complex, more varied, and more numerous. As a malware analyst or security researcher, having a powerful dynamic analysis utility is vital to be effective and efficient. This utility can enable us to understand malware capabilities and quickly analyze the malicious behaviors of malware.

Want to know how to build your own arsenal? I will detail the implementation to monitor kinds of malicious behaviors of malware on macOS. The capabilities of the utility cover monitoring process execution with command line arguments, file system events (including all common file operations, such as open, read, write, delete, rename operations), dylib loading event, network activities (including UDP, TCP, ICMP, DNS query and response).

The Mandatory Access Control Framework is the substrate on top of which all of Apple's securities, both macOS and iOS, are implemented. I will discuss how to monitor process execution, file system events, and dylib loading events using MACF on macOS. Next, I'll provide the details for monitoring network activities using Socket Filters. The utility can also record some basic info including process name, parent process name, pid, ppid, uid besides the specific details for each event. For DNS response, this utility can parse the data of DNS response and record the IP:URL mappings.

The utility consists of two parts, one is the KEXT(core component) in kernel, the other one is a client program in user space, which involves the communication between kernel space and user space. After discussing some communication mechanisms, I'll choose the kernel control API, which is a socket-based API that allows you to communicate with and receive broadcast notifications from the KEXT. The client program is intended to receive the data from the KEXT and display it to users.

In this presentation, I provide an advanced solution to monitor kinds of malicious behaviors of malware in kernel on macOS. I will also provide all involved key technical details for the implementation of monitoring all common malicious behaviors of malware on macOS. This utility is designed to dynamically analyze the malicious behaviors of malware on macOS, helping analysts or security researchers more efficiently analyze malware. You can build your own utility for fun!

Source Code: https://fortinetweb.s3.amazonaws.com/fortiguard/research/fortiappmonitor_1.0.0_release.pkg

Presentation:

https://fortinetweb.s3.amazonaws.com/fortiguard/research/Learn_How_to_Build_Your_Own_Utility_to_Monitor_Malicious_Behaviors_of_Malware_on%20macOS_KaiLu.pdf

                </details>
                
<details><summary><strong>[LogonTracer](https://github.com/t-tani)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Shusei Tomonaga](https://img.shields.io/badge/Shusei%20Tomonaga-informational) ![Tomoaki Tani](https://img.shields.io/badge/Tomoaki%20Tani-informational)

                LogonTracer is a tool to investigate malicious logon by visualizing and analyzing Windows Active Directory event logs. Event log analysis is a key element in DFIR. In the lateral movement phase of APT incidents, analysis Windows Active Directory event logs is crucial since it is one of the few ways to identify compromised hosts. At the same time, examining the logs is usually a painful task because Windows Event Viewer is not a best tool. Analysts often end up exporting entire logs into text format, then feeding them to other tools such as SIEM. However, SIEM is neither a perfect solution to handle the increasing amount of logs.

We would like to introduce a more specialized event log analysis tool for incident responders. It visualizes event logs using network analysis and machine learning so as to show the correlation of accounts and hosts. Proven with our on the ground response experience, most importantly it is an open source tool.

                </details>
                
<details><summary><strong>[MaliceIO](https://github.com/gunguy831/malice-1)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Josh Maine](https://img.shields.io/badge/Josh%20Maine-informational)

                Malice's mission is to be a free open source version of VirusTotal that anyone can use at any scale from an independent researcher to a fortune 500 company.

Source Code: https://github.com/maliceio/malice

                </details>
                
<details><summary><strong>[Memhunter: A Live Alternative to Volatility Memory Forensic Plugins](https://github.com/marcosd4h/memhunter)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Marcos Oviedo](https://img.shields.io/badge/Marcos%20Oviedo-informational)

                Memhunter automates the hunting of memory resident malware, improving the threat hunter analysis process and remediation times. The tool detects and reports memory-resident malware living on endpoint processes. Memhunter only works on Windows at the moment, and it detects known malicious memory injection techniques. The detection process is performed through live analysis and without needing memory dumps. The tool was designed as a replacement of memory forensic volatility plugins such as malfind and hollowfind. The idea of not requiring memory dumps helps on performing the memory resident malware threat hunting at scale, without manual analysis, and without the complex infrastructure needed to move dumps to forensic environments.

In order to find footprints left by malware code injection techniques, memhunter relies on a set of memory inspection heuristics and ETW trace collection. Once a suspicious process gets identified, the tool filters out false-positives through Yara Rules analysis and VirusTotal queries. This down-selection process helps the tool to reduce the number of false positives, leaving only known-bad processes. The tool then gets forensic information on the remaining set of suspicious findings and report them back to the analyst for remediation steps.

The tool itself is a self-contained binary which can be run on the endpoint to conduct the memory hunting. The idea of a self-contained binary helps on reducing the footprint, the dependencies needed, and improving the deployability of the tool. The binary contains a set of embedded "hunters" plugins, each one in charge of performing a specific heuristic detection. It also contains the ability to register the binary as an ETW collection service, which will augment the findings of next runs by providing contextual information on the attack. The down-selection is performed through libyara and VirusTotal client functionality.

Source Code: https://github.com/marcosd4h/memhunter

                </details>
                
<details><summary><strong>[MLPdf: An Effective Machine Learning Based Approach for PDF Malware Detection](https://github.com/emintham/Papers)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Jason Zhang](https://img.shields.io/badge/Jason%20Zhang-informational)

                Due to the popularity of portable document format (PDF) and increasing number of vulnerabilities in major PDF viewer applications, malware writers continue to use it to deliver malware via web downloads, email attachments and other methods in both targeted and non-targeted attacks. The topic on how to effectively block malicious PDF documents has received huge research interests in both cyber security industry and academia with no sign of slowing down.

In this work, we propose and demonstrate a novel approach based on a multilayer perceptron (MLP) neural network model, termed MLPdf, for the detection of PDF based malware. More specifically, the MLPdf model uses a backpropagation algorithm with stochastic gradient decent search for model update. A group of high quality features are extracted from two real-world datasets which comprise around 105000 benign and malicious PDF documents. Evaluation results indicate that the proposed MLPdf approach exhibits excellent performance which significantly outperforms all evaluated eight well known commercial anti-virus scanners with a much higher true positive rate (TPR) of 95.12% achieved while maintaining a very low false positive rate of 0.08%. Of the evaluated commercial AV scanners, the best scanner only has a TPR of 84.53%, which is over 10% lower than the proposed MLPdf model. In the demonstration, we will first manually analyze a malicious PDF document , then show how it can be automatically detected by the proposed ML approach.

Presentation: https://github.com/cyberML/MLPdf/blob/master/BlackHatUSA2018_MLPdf_slides.pdf
Paper: https://arxiv.org/abs/1808.06991

                </details>
                
<details><summary><strong>[Objective-See's MacOS Security Tools](https://github.com/objective-see/FileMonitor)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Patrick Wardle](https://img.shields.io/badge/Patrick%20Wardle-informational)

                Patrick drank the Apple juice; to say he loves his Mac is an understatement. However, he is bothered by the increasing prevalence of macOS malware and how both Apple & 3rd-party security tools can be easily bypassed. Instead of just complaining about this fact, he decided to do something about it. To help secure his personal computer, he's written various macOS security tools that he now shares online (always free!), via objective-see.com.

Come watch as DoNotDisturb detects physical access attacks, LuLu blocks malware attempting to communicate with C&C servers, OverSight detect webcam spying, and much more. Our Macs will remain secure!

                </details>
                
<details><summary><strong>[PA Toolkit: Wireshark Plugins for Pentesters](https://github.com/pentesteracademy/patoolkit)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Jeswin Mathai](https://img.shields.io/badge/Jeswin%20Mathai-informational) ![Nishant Sharma](https://img.shields.io/badge/Nishant%20Sharma-informational)

                Wireshark is the most basic tool that anyone thinks of when network traffic analysis is mentioned. Wireshark is beyond doubt, a wonderful tool which is available free of cost to the community and is well maintained. It is also modular and allows the user to add more functionality in form of C/Lua plugins. There are some good dissectors and plugins available for Wireshark which make user's life easy but when we talk the plugins related to attack detection or macro analysis from the security point of view, there is not much available. Our PA Toolkit is such an attempt to extend the functionality of Wireshark from a micro-analysis tool and protocol dissector to the macro analyzer and threat hunter.

PA toolkit is a collection of Wireshark plugins which enables a pentester to get insights for multiple network protocols like WiFi, VoIP, ARP, DNS, DHCP, SSL etc. This eliminates the need for a separate software/framework to detect basic attacks. The plugins are easy to add and are platform independent.

                </details>
                
<details><summary><strong>[Performing Live Forensics Without Killing Your Evidence](https://github.com/muellerzr/Practical-Deep-Learning-For-Coders/blob/master/05a_NLP.ipynb)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![John Moran](https://img.shields.io/badge/John%20Moran-informational)

                In a threat landscape characterized by targeted attacks, file-less malware and other advanced hacking techniques, the days of relying solely on traditional "dead box" forensics for investigations are, well… dead. Live forensics, a practice considered a dangerous and dark art just a decade ago, has now become the de-facto standard. However, many CSIRT teams still struggle with this type of threat hunting.

This session will discuss the benefits, pitfalls to avoid and best practices for performing live box forensics as a threat hunting tool. The presenter will also introduce a free and publicly available command line tool for Windows that automates the execution and data acquisition from other live forensics tools in a more secure, easier to maintain manner.

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[BLE CTF Project](https://github.com/hackgnar/ble_ctf)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Ryan Holeman](https://img.shields.io/badge/Ryan%20Holeman-informational)

                The purpose of BLE CTF is to teach the core concepts of Bluetooth low energy client and server interactions. While it has also been built to be fun, it was built with the intent to teach and reinforce core concepts that are needed to plunge into the world of Bluetooth hacking. After completing this CTF, you should have everything you need to start fiddling with any BLE GATT device you can find. Built to run on the esp32 microcontroller, the BLE CTF is a fully functional BLE GATT server which challenges users to utilize fundamental bluetooth communication methods. Focusing on fun and education, the CTF is the first of its kind to help teach hackers how to dive into the world of Bluetooth.

Source Code: https://github.com/hackgnar/ble_ctf

                </details>
                
<details><summary><strong>[BLEMystique: Affordable Custom BLE Target](https://github.com/pentesteracademy/blemystique)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Jeswin Mathai](https://img.shields.io/badge/Jeswin%20Mathai-informational) ![Nishant Sharma](https://img.shields.io/badge/Nishant%20Sharma-informational)

                BLEMystique is an ESP32 based custom BLE target which can be configured by the user to behave like one of the multiple BLE devices i.e. Heart rate monitor, Smart Lock, Smart Bottle, Smart band, Smartwatch etc. BLEMystique allows a pentester to play with BLE side of different Smart devices with a single piece of affordable ESP32 chip.

                </details>
                
<details><summary><strong>[Expl-iot: IoT Security Testing and Exploitation Framework](https://github.com/kzwkt/iot-exploit/blob/master/setup.py)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Aseem Jakhar](https://img.shields.io/badge/Aseem%20Jakhar-informational)

                Expl-iot is an open source flexible and extendable framework for IoT Security Testing and exploitation. It will provide the building blocks for writing exploits and other IoT security assessment test cases with ease. Expliot will support most IoT communication protocols, firmware analysis, hardware interfacing functionality and test cases that can be used from within the framework to quickly map and exploit an IoT product or IoT Infrastructure. It will help the security community in writing quick IoT test cases and exploits. The objectives of the framework are:

Easy of use
Extendable
Support for hardware, radio and IoT protocol analysis

We are currently working on the python3 version and will release it in a month. The new Alpha release is envisioned to have support for UART(serial), ZigBee, BLE, MQTT, CoAP (next version will have support for JTAG, I2C and SPI) and few miscellaneous test cases.

Source Code: https://gitlab.com/expliot_framework/expliot

                </details>
                
<details><summary><strong>[GRFICS: A Graphical Realism Framework for Industrial Control Simulations - ARSENAL THEATER DEMO](https://github.com/facebookresearch/colorlessgreenRNNs/blob/main/data/linzen_testset/subj_agr_filtered.text)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![David Formby](https://img.shields.io/badge/David%20Formby-informational)

                GRFICS is a graphical realism framework for industrial control simulations designed to lower the barrier to entry for learning about ICS security. This initial version of GRFICS provides a virtual chemical process control network including everything from the plant operator's human machine interface, to a vulnerable programmable logic controller, down to a realistic chemical process simulation being visualized in the Unity 3D game engine. With GRFICS, beginners in ICS security can practice exploiting common ICS vulnerabilities and vividly see the impact of their attacks on the virtual chemical reactor.

                </details>
                
<details><summary><strong>[WHID Injector and WHID Elite: A New Generation of HID Offensive Devices](https://github.com/xairy/usb-hacking)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Luca Bongiorni](https://img.shields.io/badge/Luca%20Bongiorni-informational)

                WHID Injector was born from the need for cheap and dedicated hardware that could be remotely controlled in order to conduct HID attacks. WHID stands for WiFi HID injector. It is a cheap but reliable piece of hardware designed to fulfill Pentesters needs related to HID Attacks, during their engagements. The core of WHID Injector is mainly an Atmega 32u4 (commonly used in many Arduino boards) and an ESP-12s (which provides the WiFi capabilities and is commonly used in IoT projects). However, during the last months, a new hardware was under R&D (i.e. WHID Elite). It replaces the Wi-Fi capabilities with a 2G baseband. Which extends its wireless capabilities to (potentially) an unlimited working range.

This cute piece of hardware is perfect to be concealed into USB gadgets and used during engagements to get remote shell over an air-gapped environment. In practice, is the dream of any Red Teamer out there. During the Arsenal presentation we will see in depth how WHID Injector and WHID Elite were designed and their functionalities. We will also look which tools and techniques Blue Teams can use to detect and mitigate this kind of attacks.

                </details>
                
<details><summary><strong>[ZigDiggity: ZigBee Pentest Toolkit](https://github.com/BishopFox/zigdiggity)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Francis Brown](https://img.shields.io/badge/Francis%20Brown-informational) ![Matthew Gleason](https://img.shields.io/badge/Matthew%20Gleason-informational)

                Introducing ZigDiggity, an entire suite of new ZigBee penetration testing tools to be released by Francis Brown and Matthew Gleason exclusively at Black Hat USA – Arsenal 2018. We'll be publicly releasing a FREE set of ZigBee hacking tools designed specifically for use by security professionals. We will showcase the best-of-breed in both hacking hardware and software (ZigDiggity) that you'll need to build a complete ZigBee penetration toolkit. Each of the key concepts/tools will be accompanied with live hacking demonstrations that will be both exciting as well as educational, including:

ZigBee – disabling home security system door/window alarms via ZigBee DoS attacks
Scaling this same home ZigBee attack to an entire neighborhood by equipping Bishop Fox's DangerDrone with the ZigBee Hacking gear and new ZigDiggity toolset.

We'll also be giving away a fully functional Danger Drone to one lucky audience member, fully equipped and loaded with ZigDiggity hacking capabilities – guaranteed to leave your friends feeling peanut butter and jealous!

                </details>
                

### Web/AppSec or Red Teaming

<details><summary><strong>[OWASP Dependency-Check](https://github.com/jeremylong/DependencyCheck)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Jeremy Long](https://img.shields.io/badge/Jeremy%20Long-informational)

                With the number of critical vulnerabilities in FOSS libraries that have affected so many applications over the last few years - Software Composition Analysis is a critical component to maintaining the security of your custom application. From Struts to Spring to jackson-databind, etc. the list of libraries that have had vulnerabilities that lead to remote code execution in the applications using the libraries goes on and on. As does the list of sites that have been compromised by these vulnerabilities. OWASP dependency-check is an open source Software Composition Analysis tool that provides a solution the `OWASP Top 10 2017: A9 - Using Components with Known Vulnerabilities`.

                </details>
                
<details><summary><strong>[Puma Scan](https://github.com/pumasecurity/puma-scan)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Eric Johnson](https://img.shields.io/badge/Eric%20Johnson-informational) ![Eric Mead](https://img.shields.io/badge/Eric%20Mead-informational)

                Puma Scan provides real-time, continuous source code analysis for .NET applications with over 50 security-focused rules targeting insecure deserialization, injection, weak cryptography, cross-site request forgery, misconfiguration, and many more insecure coding patterns. Puma Scan displays vulnerabilities in Visual Studio as spell check errors and compiler warnings to prevent engineers from committing vulnerabilities into code repositories.

DevSecOps teams can use Puma Scan's command line interface to enable security scanning in continuous integration pipelines (e.g. Jenkins, TFS), monitor code for security issues, and verify security thresholds are met during each build.
Come see live demonstrations of the Puma hunting source code for vulnerabilities and walk away with an open-source (MPL v2.0) static analysis engine to help secure your .NET applications.

                </details>
                

### Reverse Engineering

<details><summary><strong>[Snake: The Malware Storage Zoo](https://github.com/WithSecureLabs/snake)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Alex Kornitzer](https://img.shields.io/badge/Alex%20Kornitzer-informational)

                Snake is a malware storage zoo that was built out of the need for a centralized and unified storage solution for malicious samples that could seamlessly integrate into the investigation pipeline. Snake utilizes a plugin system to provide extensive static analysis capability along with interface capability to allow interaction with 3rd party platforms, such as Cuckoo. Snake adheres to the RESTful API philosophy and as a result allows for seamless interaction with 3rd party tools from within a single UI. It provides enough information to allow analysts to quickly and efficiently pivot to the most suitable tools for the task at hand.

                </details>
                

### OSINT

<details><summary><strong>[Social Mapper: Social Media Correlation Through Facial Recognition](https://github.com/Greenwolf/social_mapper)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Jacob Wilkin](https://img.shields.io/badge/Jacob%20Wilkin-informational)

                Social Mapper is a Open Source Intelligence Tool that uses facial recognition to correlate social media profiles across different sites on a mass scale. It takes an automated approach to searching popular social media sites for targets names and pictures to accurately detect and group a person's presence, outputting the results into report that a human operator can quickly review. Social Mapper has a variety of uses in the security industry, for example the automated gathering of large amounts of social media profiles for use on targeted phishing campaigns. Facial recognition aids this process by removing false positives in the search results, so that reviewing this data is quicker for a human operator.

Social Mapper supports the following social media platforms:

LinkedIn
Facebook
Twitter
GooglePlus
Instagram
VKontakte
Weibo
Douban

Social Mapper takes a variety of input types such as:

An organization's name
A folder full of named images
A CSV file with names and url's to images online

                </details>
                
