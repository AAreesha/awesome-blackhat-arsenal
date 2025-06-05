# Europe 2018
---
## 🧠 Tools by Category
### Red Teaming / AppSec

<details><summary><strong>[ART: Adversarial Robustness Toolbox for Machine Learning Models](https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/Contributing)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Irina Nicolae](https://img.shields.io/badge/Irina%20Nicolae-informational)

                Adversarial attacks of machine learning systems have become an indisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (so-called poisoning attacks) or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (so-called evasion attacks). Adversarial attacks have been demonstrated in a number of different application domains, including malware detection, spam filtering, visual recognition, speech-to-text conversion, and natural language understanding. Devising comprehensive defences against poisoning and evasion attacks by adaptive adversaries is still an open challenge.

We will present the Adversarial Robustness Toolbox (ART), a library which allows rapid crafting and analysis of both attacks and defense methods for machine learning models. It provides an implementation for many state-of-the-art methods for attacking and defending machine learning. Through ART, the attendees will (re)discover how to attack and defend machine learning systems.

                </details>
                
<details><summary><strong>[Deep Exploit: Fully Automatic Penetration Test Tool Using Machine Learning](https://github.com/TheDreamPort/deep_exploit)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Isao Takaesu](https://img.shields.io/badge/Isao%20Takaesu-informational)

                DeepExploit is fully automated penetration tool linked with Metasploit. It identifies the status of all opened ports on the target server and executes the exploit at pinpoint using Machine Learning.

Deep Exploit's key features are the following:

Efficiently execute exploit: DeepExploit can execute exploits at pinpoint (minimum 1 attempt) using self-learned data.
Deep penetration: If DeepExploit succeeds the exploit to the target server, then it further executes the exploit to other internal servers.
Self-learning: DeepExploit can learn how to exploitation by itself (uses reinforcement learning). It is not necessary for humans to prepare learning data.
Powerful intelligence gathering. To gather the information of software operated on the target server is very important for successful the exploitation. DeepExploit can identify product name and version using following methods.
+ Port scanning; Machine Learning (Analyze HTTP responses gathered by Web crawling); Google Hacking

Current Deep Exploit's version is a beta, but it can fully automatically execute following actions:

Intelligence gathering
Threat modeling
Vulnerability analysis
Exploitation
Post-Exploitation
Reporting

By using our DeepExploit, you will benefit from the following:

For pentesters:
(a) They can greatly improve the test efficiency; (b) The more pentesters use DeepExploit, DeepExploit learns how to method of exploitation using machine learning. As a result, accuracy of test can be improve.


For Information Security Officers:
(c) They can quickly identify vulnerabilities of own servers. As a result, prevent that attackers attack to your servers using vulnerabilities, and protect your reputation by avoiding the negative media coverage after breach.

Because attack methods to servers are evolving day by day, there is no guarantee that yesterday's security countermeasures are safety today. It is necessary to quickly find vulnerabilities and take countermeasures. Our DeepExploit will contribute greatly to maintaining your safety.

Presentation: https://www.slideshare.net/babaroa/deep-exploitblack-hat-europe-2018-arsenal
Source Code:: https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/DeepExploit

                </details>
                
<details><summary><strong>[Lucky CAT: A Distributed Fuzzing Management Framework](https://github.com/fkie-cad/LuckyCAT)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Thomas Barabosch](https://img.shields.io/badge/Thomas%20Barabosch-informational)

                Lucky CAT (Crash All the Things!) is a distributed fuzzing framework with an easy to use web interface. It allows management of fuzzing jobs on several remote machines concurrently. Lucky CAT aims to be easily usable, scaleable, extensible, and fun. To achieve this, it is built using several micro services and it relies on many open source projects. Furthermore, it offers a RESTful API to automate it or to integrate it with other tools.

Lucky CAT comes with several plugins for mutation engines (e.g. /dev/urandom, radamsa), fuzzers (afl, qemu_fuzzer, a minimalistic file fuzzer) and verifiers (local gdb exploitable, remote gdb exploitable). There are templates (in Python and C) that allow to quickly integrate, for example, new fuzzers and verifiers. Fuzzers can rely on their own mutation engine (e.g. afl) but Lucky CAT can also generate test cases for a fuzzer. This is handy when writing a fuzzer for an embedded device with limited computational resources or a small one-shot fuzzer for a custom protocol.

Its origin is the Nightmare Fuzzing Project. However, Lucky CAT goes beyond its ancestor. It is more 2018-ish using latest technologies such as RabbitMQ, Flask, MongoDB, and Python3. Lucky CAT's main objective is to automate the fuzzing process as far as possible so as to security researchers can focus on what they can best: identifying attack surfaces or writing custom fuzzers.
Therefore, future releases will focus on, amongst others, automatic deployment of fuzzers, crash notification and job summaries via email and instant messaging, and kernel core dump analysis.

Presentation: https://net.cs.uni-bonn.de/fileadmin/ag/martini/Staff/thomas_barabosch/blackhat-eu18-arsenal.pdf
Source Code: https://github.com/fkie-cad/LuckyCAT

                </details>
                
<details><summary><strong>[PingCastle: An Active Directory Security Tool](https://github.com/netwrix/pingcastle)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Vincent Le Toux](https://img.shields.io/badge/Vincent%20Le%20Toux-informational)

                So many tools that exist to assess Active Directory security, and yet, it is impossible to have an overview of all. PingCastle has been designed to tackle these difficulties and get results fast and without any requirements. Healthcheck mode is the most well-known mode that gives vulnerability reports in minutes regarding major AD vulnerabilities. But what if the most important point was to convince the management that AD security is not that simple? PingCastle is more than a vulnerability scanner. This demo will include scanners, cartography and secret tricks.

                </details>
                
<details><summary><strong>[Prowler: Cloud Security Assessment, Auditing, Hardening, Compliance and Forensics Readiness Tool](https://github.com/prowler-cloud/prowler)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Toni de la Fuente](https://img.shields.io/badge/Toni%20de%20la%20Fuente-informational)

                Prowler helps to assess, audit and harden your AWS account configuration and resources. It also helps to check your configuration with CIS recommendations, and check if your cloud infrastructure is GDPR compliance or if you are ready for a proper forensic investigation. It is a command line tool that provides direct and clear information about configuration status related to security of a given AWS account, it performs more than 80 checks.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[ATT&CK Framework: Endpoint Detection Super Powers on the Cheap with Sysmon and Splunk](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/L-SM-TH.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Olaf Hartong](https://img.shields.io/badge/Olaf%20Hartong-informational)

                By using the ATT&CK framework as a basis for hunting the likelihood of catching at least part of the attackers trail is significantly increased. To make use of this rich data source I will demonstrate a Threat Hunting application which will guide your investigation along all covered ATT&CK techniques.

I will release the (Mandatory Manual Learning) ThreatHunting Splunk app I've developed, which at the time of writing contains over 80 (multi)searches and over 10 dashboards leveraging summary indexes, custom visualisations and a rich set of workflow actions.
These dashboards contain overviews, threat indicators and facilitate consecutive drilldown workflows to help the analyst determine whether this is a threat or not and also provides a whitelisting option for false positives.

Knowledge is power; the workflow has been intentionally built on generic searches to cover all attack variations, in the beginning this will generate quite some false positives. It might not appear so but this is a great thing, it will teach the hunters a great deal about their environment and therefore over time they'll be more efficient in detecting malicious behavior.

                </details>
                
<details><summary><strong>[Real-Time AD Attack Detection: Detect Attacks Leveraging Domain Administrator Privilege](https://github.com/0xe7/WonkaVision)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Wataru Matsuda](https://img.shields.io/badge/Wataru%20Matsuda-informational) ![Mariko Fujimoto](https://img.shields.io/badge/Mariko%20Fujimoto-informational) ![Takuho Mitsunaga](https://img.shields.io/badge/Takuho%20Mitsunaga-informational)

                In Advanced Persistent Threat (APT) attacks, attackers tend to attack the Active Directory to expand infections. Attackers try to take over Domain Administrator privileges and create a backdoor called the "Golden Ticket". Attackers leverage this Golden Ticket to disguise themselves as legitimate accounts and obtain long-term administrator privilege. However, detecting attacks that use this method is quite difficult because the attackers' use of legitimate accounts and commands are not identified as anomalies.

We introduce a real-time detection tool that uses Domain Controller Event logs for detecting attack activities leveraging Domain Administrator privileges. Our tool can minimize the damages these types of attacks can cause even if the attackers maliciously take advantage of the Golden Ticket.

Our tool consists of the following steps to reduce false detection rate and support immediate incident response.

Step1 (Signature based detection): Analyze Event logs focusing on the characteristics of the attack activities.
Step2 (Machine Learning): Use unsupervised machine learning and anomaly detection in order to detect suspicious commands that attackers tend to use as outliers.
Step3 (Real-time alert): Raise real-time alerts using Elastic Stack if attack activities are detected.

We will publish our tool on GitHub and show specific algorithms that we have implemented so that visitors can customize or develop their own system. Our tool is all open sourced, enabling immediate and efficient incident responses against attacks at a reasonable cost.

Presentation: ﻿https://github.com/sisoc-tokyo/Real-timeDetectionAD/blob/master/Arsenal_eu-18-Real-time-Detection-of-Attacks-Leveraging-Domain-Administrator-Privilege.pdf

                </details>
                
<details><summary><strong>[SNDBOX: The Artificial Intelligence Malware Research Platform](https://github.com/FOSDEM/video-meta/blob/master/fosdem2017/released.yml)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Ran Dubin](https://img.shields.io/badge/Ran%20Dubin-informational) ![Ariel Koren](https://img.shields.io/badge/Ariel%20Koren-informational)

                SNDBOX is the world's first Artificial Intelligence (AI) malware research platform designed to scale up research time. Developed by researchers for researchers, SNDBOX offers never-seen-before malware analysis visibility powered by kernel mode next generation sandbox. Multiple AI detection vectors work alongside our big data malware similarity engine to reduce false positive classification errors. Behavioral signatures, multi-vector deep learning classifiers and multiple AI similarity search engines seamlessly work together to provide high visibility and data-driven explanations to scale malware research capabilities and reduce research time. Furthermore, with full access to our data, all levels of your team can leverage information necessary for complete malware remediation and new research possibilities, while sharing insights, public samples and IOC's through our community platform.

                </details>
                

### Red Teaming

<details><summary><strong>[CoffeeShot: Memory Injection to Avoid Detection](https://github.com/MinervaLabsResearch/CoffeeShot)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Asaf Aprozper](https://img.shields.io/badge/Asaf%20Aprozper-informational)

                CoffeeShot is an evasion framework that designed for creating Java-based malware which bypasses most of the anti-virus vendors. The framework utilizes JNA (Java Native Access) to look for a victim process, once it finds it - a shellcode will be injected directly from the Java Archive file (JAR).

Java malware like "Jrat" and "Adwind" are used by malicious adversaries' day by day, more and more. Their main reason to write malware in Java is to be evasive and avoid security products - including those that use advanced features like machine learning. To overcome the above, blue-team members can use this framework in assessing the effectiveness of their anti-malware measures against malicious software written in Java.

On the other hand, CoffeeShot can be applied by penetration testers as well. The framework provides red-teamers a friendly toolset by allowing them to embed any shellcode in a JAR file, assisting them to avoid detection with memory injection and to PWN the target!

                </details>
                
<details><summary><strong>[iBombShell: Dynamic Remote Shell](https://github.com/Matir/jspassphrase/blob/master/wordlist.json)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Pablo Gonzalez Perez](https://img.shields.io/badge/Pablo%20Gonzalez%20Perez-informational) ![Álvaro Nuñez-Romero](https://img.shields.io/badge/Álvaro%20Nuñez-Romero-informational)

                The emergence of PowerShell within pentesting post-exploitation is important. Its flexibility, possibilities and power make this Microsoft´s command line an efficient post-exploitation tool. In scenarios where we cannot use neither install pentesting techniques this tool acquires special relevance. iBombShell gives access to a pentesting repository where the pentester could use any function oriented to the post-exploitation phase and, in some cases, exploit vulnerabilities. iBombShell is a remote pentesting Shell that loads itself automatically in memory offering unlimited tools for the pentester.

iBombShell is a tool written in PowerShell that allows post-exploitation functionalities in a shell or a prompt, anytime and in any operating system. Moreover, it allows, in some cases, the execution of vulnerability exploitation features. These features are loaded dynamically, depending on when they are needed, from a GitHub repository.

The shell is downloaded directly to memory giving access to many pentesting features and functionalities, avoiding any hard drive access. These functionalities downloaded to memory are in PowerShell function format. This execution strategy is called EveryWhere.

In addition, iBombShell allows a second way of execution called Silently. Using this execution way, an iBombShell instance (called warrior) can be launched. When the Warrior is executed over a compromised machine, it will connect to a C2 through the http protocol. From the C2, written in Python, a warrior can be controlled to dynamically load functions to the memory and to offer pentesting remote execution functionalities. All those steps are part of the post-exploitation phase.

                </details>
                
<details><summary><strong>[SCAVENGER: A Post-Exploitation Scanning/Mapping Tool](https://github.com/brianckeegan/Trailers/blob/master/joined_data.csv)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Philip Pieterse](https://img.shields.io/badge/Philip%20Pieterse-informational)

                SCAVENGER is a multi-threaded post-exploitation scanning tool for mapping systems and finding "interesting" and most frequently used files, folders and services. Once credentials are gained, it can scan remote systems (Linux, Windows and OSX) via services like SMB and SSH to scrape that system looking for "interesting" things and then cache the result. SCAVENGER has the ability to find the newest files that have been accessed/modified/created and keep the result in an ordered database. Then, after time has passed, hours or days later the systems can be scanned again. SCAVENGER can then compare the previous list of "newest files" to the latest list of "newest files." This gives the user the ability to find the "interesting" and most frequently files used on that system, for example password files being accessed by an administrator or heavily used credit card database files.

Whilst looking for "interesting" files, folder and services, SCAVENGER scans these filenames and their content for various "interesting" phrases, for example "password" or "secret." Once detected SCAVENGER then downloads the "interesting" file to the local system. At the same time SCAVENGER also scans for Card Holder Data and also downloads the file if Card Holder Data is found.

Future features will be the addition of services like NFS, FTP and database connections. Also adding more capability of retrieving passwords from remote Linux or Windows systems, without touching to the disk of the remote system. And without reinventing the wheel using SCAVENGER as a wrapper to use on Windows systems performing more post-exploitation techniques.

Source Code: https://github.com/SpiderLabs/scavenger﻿

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[RPL Attacks Framework: Attacking RPL in WSNs](https://github.com/wannadie/mendeley-parser/blob/master/output/electrical-and-electronic-engineering/electrical-and-electronic-engineering-p.csv)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Alexandre D'Hondt](https://img.shields.io/badge/Alexandre%20D'Hondt-informational)

                This tool is a framework for attacking the Routing Protocol for Low power and lossy networks (RPL) implementation of Contiki for Wireless Sensor Networks (WSN).

Presentation: https://github.com/dhondta/rpl-attacks/raw/master/doc/bheu18-arsenal-presentation.pdf

                </details>
                
<details><summary><strong>[Universal Radio Hacker v2: Simulate Wireless Devices with Software Defined Radio](https://github.com/jopohl/urh)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Johannes Pohl](https://img.shields.io/badge/Johannes%20Pohl-informational)

                Wireless communication between Internet of Things (IoT) devices is, in many cases, built upon proprietary protocols designed under size and energy constraints. Vulnerabilties in such protocols are critical, e.g. an attacker breaks into a house by hacking a wireless door lock. Software Defined Radios (SDR) offer a generic way to investigate such protocols, but require software support when it comes to demodulating and decoding messages. The Universal Radio Hacker (URH) is an open source tool to support researchers when operating with SDRs by abstracting most of the required HF basics needed for demodulation. Furthermore, it assists reverse engineering the protocol format. While this works well for stateless and undirectional protocols, there are more sophisticated protocols on the market that can not be handled without state machine.

Version 2.0 of the Universal Radio Hacker introduces a Simulation tab that allows to specify a complete HF protocol with several states and participants. It is called Simulation because URH has the ability to play the protocol from the perspective of one or more participants, i.e. URH evaluates all messages towards the simulated participant and dynamically crafts responses depending on the state and previous information. The simulation advancement complies to the easy-to-use philosophy that we also use for the basic URH. Users can see all messages of the analyzed protocol in a graphical flow graph and add new messages, edit or move them around at convenience. Message field values are dynamically derived with access to all previously sent and received information or even by using external programs, e.g. for AES encryption. Conditions, jump and pause elements in the graphical user interface allow generating complex state machines. In our presentation, we demonstrate a practical attack that shows how the simulation component of URH opens a sophisticated wireless door lock (AES encryption) with SDRs.

                </details>
                

### Web/AppSec

<details><summary><strong>[XSSER: From XSS to RCE 3.0](https://github.com/Varbaek/xsser)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Hans-Michael Varbaek](https://img.shields.io/badge/Hans-Michael%20Varbaek-informational)

                This presentation demonstrates how an attacker can utilize XSS to execute arbitrary code on the web server when an administrative user inadvertently triggers a hidden XSS payload. Custom tools and payloads integrated with Metasploit's Meterpreter in a highly automated approach will be demonstrated live, including post-exploitation scenarios and interesting data that can be obtained from compromised web applications. This version includes more payloads for common web apps and various other improvements too!

                </details>
                
