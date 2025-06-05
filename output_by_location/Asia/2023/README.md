# Asia 2023
---
## 🧠 Tools by Category
### Web/AppSec or Red Teaming

<details><summary><strong>[APKHunt | OWASP MASVS Static Analyzer](https://github.com/Cyber-Buddy/APKHunt)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Sumit Kalaria](https://img.shields.io/badge/Sumit%20Kalaria-informational) ![Mrunal Chawda](https://img.shields.io/badge/Mrunal%20Chawda-informational)

                APKHunt is a comprehensive static code analysis tool for Android apps that is based on the OWASP MASVAS framework. The OWASP MASVS (Mobile Application Security Verification Standard) is the industry standard for mobile app security. APKHunt is intended primarily for mobile app developers and security testers, but it can be used by anyone to identify and address potential security vulnerabilities in their code.

With APKHunt, mobile software architects or developers can conduct thorough code reviews to ensure the security and integrity of their mobile applications, while security testers can use the tool to confirm the completeness and consistency of their test results. Whether you're a developer looking to build secure apps or an infosec tester charged with ensuring their security, APKHunt can be an invaluable resource for your work.

Key features of APKHunt:
- Scan coverage: Covers most of the SAST (Static Application Security Testing) related test cases of the OWASP MASVS framework.
- Optimised scanning: Specific rules are designed to check for particular security sinks, resulting in an almost accurate scanning process.
- Low false-positive rate: Designed to pinpoint and highlight the exact location of potential vulnerabilities in the source code.
- Output format: Results are provided in a TXT file format for easy readability for end-users.

Current Limitation:
- Supporting OS/Language: Capable of scanning the source code of an android APK file and is only supported on Linux environments.

Upcoming Features:
- Scanning of multiple APK files at the same time
- More output format such as HTML
- Integration with third-party tools

                </details>
                

### Web/AppSec

<details><summary><strong>[Build Your Own Reconnaissance System with Osmedeus Workflow Engine](https://github.com/j3ssie/osmedeus)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Ai Ho](https://img.shields.io/badge/Ai%20Ho-informational)

                Osmedeus is a is a workflow framework designed to perform reconnaissance, with a focus on identifying the attack surface and conducting security testing on the specified target, including vulnerability scanning, port scanning, and content discovery

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[CANalyse 2.0 : A Vehicle Network Analysis and Attack Tool](https://github.com/canalyse/CANalyse-2.0)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Kartheek Lade](https://img.shields.io/badge/Kartheek%20Lade-informational)

                CANalyse is a software tool built to analyse the log files in a creative powerful way to find out unique data sets automatically and inject the refined payload back into vehicle network. It can also connect to simple interfaces such as Telegram for remote control. Basically, while using this tool you can provide your bot-ID and be able to use the tool's inbuilt IDE over the internet through telegram.

CANalyse uses python-can library to sniff vehicle network packets and analyse the gathered information and uses the analysed information to command & control certain functions of the vehicle. CANalyse can be installed inside a raspberry-PI, to exploit the vehicle through a telegram bot by recording and analysing the vehicle network.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[eBPFShield: Advanced IP-Intelligence & DNS Monitoring using eBPF](https://github.com/sagarbhure/eBPFShield)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Sagar Bhure](https://img.shields.io/badge/Sagar%20Bhure-informational)

                eBPFShield is a powerful security tool that utilizes eBPF and Python to provide real-time IP-Intelligence and DNS monitoring. By executing in kernel space, eBPFShield avoids costly context switches, making it a high-performance solution for detecting and preventing malicious behavior on your network. The tool offers efficient monitoring of outbound connections and comparison with threat intelligence feeds, making it an effective solution for identifying and mitigating potential threats. The tool includes features such as DNS monitoring, IP-Intelligence, and the ability to pull down public threat feeds.

Additionally, it includes a roadmap for future developments such as support for IPv6, automated IP reputation analysis using Machine Learning algorithms, and integration with popular SIEM systems for centralized monitoring and alerting.

eBPFShield is especially useful for companies and organizations that handle sensitive information and need to ensure the security of their networks. It's an efficient solution to monitor and protect servers from potential threats and it can help to prevent data breaches and other cyber attacks.

                </details>
                
<details><summary><strong>[StegoWiper+: A Powerful and Flexible Active Attack for Disrupting Stegomalware and Advanced Stegography](https://github.com/mindcrypt/stegowiper)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Alfonso Muñoz](https://img.shields.io/badge/Alfonso%20Muñoz-informational) ![Manuel Urueña](https://img.shields.io/badge/Manuel%20Urueña-informational)

                Over the last 10 years, many threat groups have employed stegomalware or other steganography-based techniques to attack organizations from all sectors and in all regions of the world. Some examples are: APT15/Vixen Panda, APT23/Tropic Trooper, APT29/Cozy Bear, APT32/OceanLotus, APT34/OilRig, APT37/ScarCruft, APT38/Lazarus Group, Duqu Group, Turla, Vawtrack, Powload, Lokibot, Ursnif, IceID, etc.Our research shows that most groups are employing very simple techniques (at least from an academic perspective) and known tools to circumvent perimeter defenses, although more advanced groups are also using steganography to hide C&C communication and data exfiltration. We argue that this lack of sophistication is not due to the lack of knowledge in steganography (some APTs have already experimented with advanced algorithms) but simply because organizations are not able to defend themselves, even against the simplest steganography techniques.

During the demonstration we will show the practical limitations of applying existing automated steganalysis techniques for companies that want to prevent infections or information theft by these threat actors. For this reason, we have created stegoWiper, a tool to blindly disrupt any image-based stegomalware, attacking the weakest point of all steganography algorithms: their robustness. We'll show that it is capable of disrupting all steganography techniques and tools (Invoke-PSImage, F5, Steghide, openstego, ...) employed nowadays. In fact, the more sophisticated a steganography technique is, the more disruption stegoWiper produces. Moreover, our active attack allows us to disrupt any steganography payload from all the images exchanged by an organization by means of a web proxy ICAP (Internet Content Adaptation Protocol) service, in real time and without having to identify which images contain hidden data first.

After our presentation at BlackHat USA 2022 Arsenal we have been working on supporting, disrupting, state-of-the-art advanced algorithms available in the academic literature, based on matrix encryption, wet-papers, etc. (e.g. Hill, J-Uniward, Hugo). Especially we have paid attention to the YASS algorithm (https://pboueke.github.io/CryptoStego/) resistant to numerous active attacks and commercial CDR-type software. Finally our tool is able to defeat them.

                </details>
                
<details><summary><strong>[Unprotect Project: Malware Evasion Techniques](https://github.com/fr0gger)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Thomas Roccia](https://img.shields.io/badge/Thomas%20Roccia-informational)

                Malware evasion consists of techniques used by malware to bypass security in place, circumvent automated and static analysis as well as avoiding detection and harden reverse engineering. There is a broad specter of techniques that can be used. In this talk we will review the history of malware evasion techniques, understand the latest trends currently used by threat actors and bolster your security analysis skills by getting more knowledge about evasion mechanisms.

We will present the latest major update of the Unprotect Project an open-source documentation about malware evasion techniques. The goal will be to present the project and see how we can leverage it for use cases, including threat intelligence, malware analysis, strengthen security, train people, and extend the Mitre ATT&CK matrix. Over the years it has become a well renowned place for security researchers. During this talk we will review some of the most important update.

This presentation can benefit both Blue and Red Team as it will provide knowledge and information on how malware can bypass your security in place and stay under the radar. You will learn about the intrinsic mechanisms used by attackers to compromise you without you even realizing it!

                </details>
                
<details><summary><strong>[White Phoenix - Beating Intermittent Encryption](https://github.com/mittidesai/Stock-Market-Prediction/blob/master/120_clusters)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Ari Novick](https://img.shields.io/badge/Ari%20Novick-informational) ![Amir Landau](https://img.shields.io/badge/Amir%20Landau-informational)

                Intermittent Encryption (aka Partial Encryption) is a new trend in the world of ransomware. It's been adopted by many notorious groups such as BlackCat Ransomware, Play Ransomware and more. Altogether, the groups using intermittent encryption have successfully targeted hundreds of organizations in 2022 alone. However, even though intermittent encryption has its advantages, it leaves much of the content of targeted files unencrypted. In this talk, we will demonstrate a tool that uses this limitation to recover valuable data, such as text and images from documents encrypted by these groups, allowing the victims to recover some of their lost data.

                </details>
                

### Red Teaming

<details><summary><strong>[Interactive Kubernetes Security Learning Playground - Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Madhu Akula](https://img.shields.io/badge/Madhu%20Akula-informational)

                Kubernetes Goat is an interactive Kubernetes security learning playground. It has intentionally vulnerable by design scenarios to showcase the common misconfigurations, real-world vulnerabilities, and security issues in Kubernetes clusters, containers, and cloud native environments.

It's tough to learn and understand Kubernetes security safely, practically, and efficiently. So here we come to solve this problem not only for security researchers but also to showcase how we can leverage it for attackers, defenders, developers, DevOps teams, and anyone interested in learning Kubernetes security. We are also helping products & vendors to showcase their product or tool's effectiveness by using these playground scenarios and also help them to use this to educate their customers and organizations. This project is a place to share knowledge with the community in well-documented quality content in hands-on scenario approaches.

                </details>
                
<details><summary><strong>[KernelGoat](https://github.com/Rnalter/KernelGoat)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Shivankar Madaan](https://img.shields.io/badge/Shivankar%20Madaan-informational)

                "KernelGoat is a 'Vulnerable by Design' Linux kernel environment to learn and practice Kernel security issues"

                </details>
                
<details><summary><strong>[tty2web](https://github.com/kost/tty2web/blob/master/LICENSE)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Vlatko Kosturjak](https://img.shields.io/badge/Vlatko%20Kosturjak-informational)

                tty2web can take any console program and convert it into a web application. It provides a proper console for your shell needs directly inside your browser, which means programs like vim, mc, or any program that needs tty will work as expected by default. Features include support for both bind and reverse mode, which is useful for penetration testing and NAT traversal, bidirectional file transfer, reverse SOCKS 5 functionality by emulating the regeorg interface, and API support for executing commands (imagine having a RESTful interface to your operating system shell). It supports collaboration and sharing between teams, is multiplatform, and runs well on Unix/Linux-based OSs running container payloads. It is based on gotty but has been heavily improved for security and penetration tester needs.

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[Nightingale: Docker for Pentesters](https://github.com/RAJANAGORI/Nightingale)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Raja Nagori](https://img.shields.io/badge/Raja%20Nagori-informational)

                Have you ever been encounter where you configured the security virtual envieonment in the virtualbox and after someday the VM got crashed. All your configuration, tool setup, important information about the taget, POC's and what not, all will be gone and you can't recover the same.

With the same problem, I created the Nightingale based on the docker technology which provides you the exact security environment where you can expreicne the tools which a pentesters required at the time of pentesting. Adding to this, you no need to worry about your data, configuration and all other important. Nightingale will automatically restore the configuration once the new container will be up.

                </details>
                
