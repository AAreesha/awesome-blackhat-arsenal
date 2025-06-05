# USA 2021
---
## 🧠 Tools by Category
### Red Teaming

<details><summary><strong>[Cloudtopolis: Zero Infrastructure Password Cracking](https://github.com/JoelGMSec/Cloudtopolis)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Joel Gámez](https://img.shields.io/badge/Joel%20Gámez-informational)

                Cloudtopolis is a tool that facilitates the installation and provisioning of Hashtopolis on the Google Cloud Shell platform, quickly and completely unattended (and also, free!). Together with Google Collaboratory, it allows us to break hashes without the need for dedicated hardware from any browser (even from your smartphone).

Thanks to its implementation through Docker, it can be run almost anywhere in a fast and easy way. In addition, it can be used collaboratively using different accounts, being very useful for use in CTF teams or in Red Team exercises.

As a novelty in this talk, automated clients for Windows and Linux (not disclosed yet) will be presented, being able to additionally use the user's local resources together with the graphic cards provided by Colab.

                </details>
                
<details><summary><strong>[InQL: Introspection GraphQL Scanner](https://github.com/doyensec/inql)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Andrea Brancaleoni](https://img.shields.io/badge/Andrea%20Brancaleoni-informational)

                InQL is an open-source toolbox for GraphQL. In addition to introspection and enumeration, our tool allows probing for GraphQL specific vulnerabilities. Over the course of the last few years, InQL became the go-to tool for GraphQL penetration testing thanks to its flexibility.

InQL is suited specifically for security audits and manual penetration testing with its tight integration with Burp Suite. In addition to that, InQL also provides an easily accessible API and command-line interface that can be integrated with other “shift-left” security engineering practices.

During the session, we will showcase InQL superpowers: black-box queries generation, cycles detection, CSRF helpers, and the newly integrated SQLi exploiter.

Resources:
- https://github.com/doyensec/inql
- https://blog.doyensec.com/2018/05/17/graphql-security-overview.html
- https://blog.doyensec.com/2020/03/26/graphql-scanner.html
- https://blog.doyensec.com/2021/05/20/graphql-csrf.html
- https://blog.doyensec.com/2020/11/19/inql-scanner-v3.html
- https://blog.doyensec.com/2020/06/11/inql-scanner-v2.html

                </details>
                
<details><summary><strong>[Kubestriker: A Blazing Fast Kubernetes Security Auditing Tool](https://github.com/vchinnipilli/kubestriker)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Vasant Chinnipilli](https://img.shields.io/badge/Vasant%20Chinnipilli-informational) ![Pralhad Chaskar](https://img.shields.io/badge/Pralhad%20Chaskar-informational)

                Kubestriker performs numerous in depth checks on kubernetes infrastructure to identify any misconfigurations which make organisations an easy target for attackers and safeguards against potential attacks on Kubernetes clusters.

                </details>
                
<details><summary><strong>[Lazyrecon v2.0](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/exploitation/lazyrecon.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Kirill Zhdanov](https://img.shields.io/badge/Kirill%20Zhdanov-informational)

                Lazyrecon v2.0 is a subdomain discovery tool that discovers and resolves valid subdomains then performs SSRF/LFI/SQLi fuzzing and port scanning. It has a simple modular architecture and is optimized for speed while working with github and wayback machine.

                </details>
                
<details><summary><strong>[PyRDP: Remote Desktop Protocol Monster-in-the-Middle (MITM)](https://github.com/GoSecure/pyrdp/blob/main/pyproject.toml)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Olivier Bilodeau](https://img.shields.io/badge/Olivier%20Bilodeau-informational)

                PyRDP is a Remote Desktop Protocol (RDP) monster-in-the-middle (MITM) tool and library useful in intrusion testing and malware research. Its out of the box offensive capabilities can be divided in three broad categories: client-side, MITM-side and server-side. On the client-side PyRDP can actively steal any clipboard activity, crawl mapped drives and collect all keystrokes. On the MITM-side PyRDP records everything on the wire in several formats (logs, JSON events), allows the attacker to take control of an active session and performs a pixel perfect recording of the RDP screen. On the server-side, on-logon PowerShell or cmd injection can be performed when a legitimate client connects.

On the malware research side, PyRDP can be used as part of a fully interactive honeypot. It can be placed in front of a Windows RDP server to intercept malicious sessions. It can replace the credentials provided in the connection sequence with working credentials to accelerate compromise and malicious behavior collection. It also saves a visual and textual recording of each RDP session, which is useful for investigation or to generate IOCs. Additionally, PyRDP saves a copy of the files that are transferred via the drive redirection feature, allowing it to collect malicious payloads.

Over the last year, we implemented several features that we are going to uncover in this brand-new arsenal workshop: improved file interception and crawling, dynamic certificate cloning, CredSSP/NLA support with private certificate and key, dynamic NLA redirection, NTLMSSP hash logging, and more.

                </details>
                

### Reverse Engineering

<details><summary><strong>[FileInsight-plugins: Decoding Toolbox of McAfee FileInsight Hex Editor for Malware Analysis](https://github.com/nmantani/FileInsight-plugins)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Nobutaka Mantani](https://img.shields.io/badge/Nobutaka%20Mantani-informational)

                FileInsight-plugins is a large set of plugins for McAfee FileInsight hex editor. It adds many capabilities such as decode, decryption, decompression, searching XOR-ed text strings, scanning with a YARA rule, code emulation, disassembly, and more! It is useful for various kinds of decoding tasks in malware analysis (such as extracting malware executable files from malicious document files, deobfuscation of malicious scripts).

Currently, FileInsight-plugins has 110 plugins. The plugins provide the following functions and many other functions.

- Calculation of hash values (CRC32, MD5, SHA1, SHA256, ssdeep, imphash, impfuzzy)
- Search for XORed, bit-rotated text strings and byte arrays
- XOR while incrementing / decrementing XOR key (rolling XOR)
- Encode and decode of BASE16, BASE32, BASE58, BASE64, BASE85 with custom tables
- Encryption and decryption (AES, ARC2, ARC4, Blowfish, ChaCha20, DES, Salsa20, TEA, Triple DES, XTEA)
- Compression and decompression (aPLib, Bzip2, Deflate, Gzip, LZ4, LZMA, LZNT1, LZO, PPMd, QuickLZ, XZ, Zstandard)
- Detection of embedded files in a file
- Extraction of text strings of ASCII and UTF-16 with auto decode of hex string and BASE64 strings
- Scanning with YARA and highlighting regions that match YARA rules
- Showing file metadata
- Parsing file structure (Gzip, RAR, ZIP, ELF, PE, MBR partition table, BMP, GIF, JPEG, PNG, Windows shortcut)
- Code emulation of shellcodes and executable files (Windows (x64, x86) and Linux (x64, x86, ARM, ARM64, MIPS)) with API call tracing and capturing memory dumps
- Disassembly (x64, x86, ARM, ARM64, MIPS, PowerPC, PowerPC64, SPARC)
- Opening data with other tools such as CyberChef, IDA, and VSCode (customizable with JSON config file).
- Visualization (Bitmap, Byte histogram, Entropy graph)

FileInsight-plugins is a tool that I develop privately, not professionally developed by the organization I belong to.

Links:
- GitHub repository: https://github.com/nmantani/FileInsight-plugins/
- Documents of use cases: https://github.com/nmantani/FileInsight-plugins/wiki

                </details>
                
<details><summary><strong>[Tracee: Linux Runtime Security and Forensics Using eBPF](https://github.com/aquasecurity/tracee)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Yaniv Agman](https://img.shields.io/badge/Yaniv%20Agman-informational) ![Roi Kol](https://img.shields.io/badge/Roi%20Kol-informational)

                Tracee is a runtime security and forensics tool for Linux. It is composed of tracee-ebpf, which collects OS events, and tracee-rules, which is the runtime security detection engine.


Tracee-ebpf is capable of tracing all processes in the system or a group of processes according to some given filters. The set of events to trace can be selected by the user and include the following:


1. System calls
2. LSM hooks (security_file_open, security_bprm_check, cap_capable, ...)
3. Internal kernel functions (vfs_write, commit_creds, ...)
4. Special events and alerts (magic_write, mem_prot_alert, ...)


Other than tracing, Tracee-ebpf is also capable of capturing files written to disk or memory (e.g. "fileless" malwares), and extracting binaries that are dynamically loaded to an application's memory (e.g. when a malware uses a packer). Using these capabilities, it is possible to automatically collect forensic artifacts for later investigation.
Tracee-Rules, is a rule engine that helps you detect suspicious behavioral patterns in streams of events. It is primarily made to leverage events collected with Tracee-eBPF into a Runtime Security solution.
Tracee supports authoring rules in Golang or in Rego.

                </details>
                

### Web/AppSec or Red Teaming

<details><summary><strong>[Find Security Bugs](https://github.com/find-sec-bugs/find-sec-bugs)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Philippe Arteau](https://img.shields.io/badge/Philippe%20Arteau-informational)

                Find Security Bugs is a plugin for the Java static analysis tool SpotBugs. This plugin consists of set rules that focus only on security weaknesses. It can be used by developers or security professionals to find vulnerabilities in their code.

The plugin can identify weaknesses in Java web applications from 138 different bug patterns including XSS, SQL injection, XXE, template injection and many more. It can scan any JVM languages such as Kotlin, Scala and Groovy. The assessment can be done in an IDE, such as Eclipse, or IntelliJ. It can also be configured in a continuous integration environment.

The most recent additions to the project include features to the IDE integration and Continuous Integration (CI). The IDE IntelliJ integration was greatly improved to have better support for alternative languages such as Kotlin. This makes it easier to scan Android applications. IDE integration is a great perspective for code audit. For developers, continuous integration is a highly sought-after configuration. A new Github Action will be presented. It provides an easy feedback for developers when integrating code to the master branch with a pull request.

The Black Hat Arsenal's demonstrations will include a live code review where samples of vulnerability and practical methods will be showcased in the new IDE and CI environment.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[Kraker](https://github.com/zzzteph)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Ivan Iushkevich](https://img.shields.io/badge/Ivan%20Iushkevich-informational)

                Kraker is a distributed password brute-force system that allows you to run and manage the hashcat on different servers and workstations, focused on ease of use. There were two main goals during the design and development: to create the most simple tool for distributed hash cracking and make it fault-tolerant.

                </details>
                
<details><summary><strong>[LUDA: Large URLs Dataset Analyzer for Security](https://github.com/akamai/luda)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Jordan Garzon](https://img.shields.io/badge/Jordan%20Garzon-informational) ![Asaf Nadler](https://img.shields.io/badge/Asaf%20Nadler-informational)

                What interesting stuff can we find by looking only at URLs without the actual HTTP traffic ?

Well, quite a lot. Hackers often do not reinvent the wheel. They buy existing malwares or phishing that use the same scheme for HTTP communication. Techniques to randomize URLs , like DGA, often apply on the domain part". But what about the rest?

In this talk, we present LUDA - Large URLs Dataset Analyzer for security. It works in two modes: Malware or Phishing.
The first will detect similarities between C2 communication and cluster them by families. The last will apply the same clustering with an additional layer of " brand " detection.
Both of them can automatically extract regexes, using Genetic algorithm, and can be deployed for inline detections.
This powerful tool already supports integration with various public malicious repositories like PhishTank, URLHaus , Virus Total as well as dozens more.
As opposed to similar projects , this tool is focused only on security. It includes specific options like automatic false positive cleaning.
We will demo how we can run LUDA on public datasets with the two modes and show how it succeeds to get quality insights from large datasets. Finally we will show what are the current threat families found on real traffic data taken from Akamai Secure Web Gateway.

                </details>
                
<details><summary><strong>[Slips: A Machine-Learning Based, Free-Software, Network Intrusion Prevention System](https://github.com/stratosphereips/StratosphereLinuxIPS)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Sebastian Garcia](https://img.shields.io/badge/Sebastian%20Garcia-informational) ![Kamila Babayeva](https://img.shields.io/badge/Kamila%20Babayeva-informational)

                Slips is a behavioral-based intrusion prevention system, and the first free software to use machine learning to detect attacks in the network. It is a modular system that profiles the behavior of IP addresses and performs detections in time windows. Slips' modules detect a range of attacks both to and from the protected device. Slips connects to other Slips using P2P, and exports alerts to other systems.

Slips works in several directionality modes. The concept of home network is not used to choose which detection to apply, but to choose which profile to analyze. The user can choose to detect attacks coming *to* or going *from* these profiles. This makes it easy to protect your network but also to focus on infected computers inside your network.

Among its modules, Slips includes the download/manage of external Threat Intelligence feed (including our laboratory's own TI feed), whois/asn/geocountry enrichment, a LSTM neural net for malicious behavior detection, port scanning detection (vertical and horizontal) on flows, long connection detection, etc. The decisions to block profiles or not are based on ensembling
algorithms. The P2P module connects to other Slips to share detection alerts.

Slips can read packets from the network, pcap, Suricata, Zeek, Argus and Nfdump, and can output alerts files and summaries. Having Zeek as a base tool, Slips can correctly build a sorted timeline of flows combining all Zeek logs. Slips can send alerts using the STIX/TAXII protocol.

More importantly, the Kalipso Node.js interface allows the analysts to see the profiles' behaviors and detections performed by Slips modules directly in the console. Kalipso displays the flows of each profile and time window and compares those connections in charts/bars. It also summarizes the whois/asn/geocountry information for each IP that communicates with a protected device.

                </details>
                

### OSINT

<details><summary><strong>[New Face, Who Dis? Protecting Privacy in a World of Surveillance](https://gist.github.com/summerofgeorge/7b996d51e0d79286c3d14040d51d69ce)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Mike Kiser](https://img.shields.io/badge/Mike%20Kiser-informational)

                While it has its potential benefits, facial recognition is eroding privacy and other human rights. Over the past year, several organizations have acknowledged that they have "scraped" social media and similar sites for photos to build their biometric databases, and photos intended for personal use only have now been potentially weaponized.

Industry and government have ethical responsibilities to prevent this, but what if there were a way to enhance privacy for individuals without waiting for the cavalry? Adversarial technology can provide a way to protect this biometric, but it must be as easy to use as picking up their mobile device and taking a photo.

Introducing "Ruse," a mobile app that seeks to use adversarial strategies to make personal photos less useful for commercial facial recognition systems while retaining a (relatively) low impact on human usefulness.

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[PingCastle: An Active Directory Auditing Tool](https://github.com/netwrix/PingCastleCloud)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Vincent Le Toux](https://img.shields.io/badge/Vincent%20Le%20Toux-informational)

                So many tools that exist to assess Active Directory security, and yet, it is impossible to have an overview of all. PingCastle has been designed to tackle these difficulties and get results fast and without any requirements. Healthcheck mode is the most well-known mode that gives vulnerability reports in minutes regarding major AD vulnerabilities. But what if the most important point was to convince the management that AD security is not that simple? PingCastle is more than a vulnerability scanner. This demo will include scanners, cartography and secret tricks.

                </details>
                
<details><summary><strong>[remote-method-guesser: A Java RMI Vulnerability Scanner](https://github.com/qtc-de/remote-method-guesser)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Tobias Neitzel](https://img.shields.io/badge/Tobias%20Neitzel-informational)

                remote-method-guesser (rmg) is a Java RMI vulnerability scanner that checks for common misconfigurations on Java RMI endpoints.
It combines well known techniques for RMI enumeration with detection capabilities for lesser known attack vectors that are often missed.
Apart from detecting RMI vulnerabilities, remote-method-guesser can perform attack operations for each supported vulnerability type.
The following list shows some of it's currently supported operations:

* List available bound names and their interface class names
* List codebase locations (if exposed by the remote server)
* Check for known vulnerabilities (enabled class loader, missing JEP290, JEP290 bypasses, localhost bypass (CVE-2019-2684))
* Identify existing remote methods by using a bruteforce (wordlist) approach
* Call remote methods with user specified arguments (no manual coding required)
* Call remote methods with ysoserial gadgets within the arguments
* Call remote methods with a client specified codebase (remote class loading attack)
* Perform DGC, registry and activator calls with ysoserial gadgets or a client specified codebase
* Perform bind, rebind and unbind operations against an RMI registry
* Bypass registry deserialization filters by using An Trinhs registry bypass
* Enumerate the unmarshalling behavior of java.lang.String
* Create Java code dynamically to invoke remote methods manually

                </details>
                
<details><summary><strong>[trapfuzzer](https://github.com/hac425xxx)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Sili luo](https://img.shields.io/badge/Sili%20luo-informational)

                Breakpoint mechanism based coverage-guided binary fuzzing tools for Windows and Linux platforms.

Binary instrument by breakpoint, in specific scenarios, this method is faster than dynamorio.

At present, more than 200 vulnerabilities have been found in WPS office, foxitpdf and other software

                </details>
                

### Web/AppSec

<details><summary><strong>[reNgine: An Automated Reconnaissance Framework](https://github.com/yogeshojha/rengine)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Yogesh Ojha](https://img.shields.io/badge/Yogesh%20Ojha-informational)

                reNgine is an automated reconnaissance engine(framework) that is capable of performing end-to-end reconnaissance with the help of highly configurable scan engines on web application targets. reNgine makes use of various open-source tools and makes a highly configurable pipeline of reconnaissance to gather the recon result.

reNgine also makes it possible for users to choose the tools they desire while following the same reconnaissance pipeline, example - with reNgine you aren't limited to using sublist3r for subdomains discovery, rather reNgine allows you to combine multiple tools like sublist3r, subfinder, assetfinder, and easily integrate them into your reconnaissance pipeline. The reconnaissance results are then displayed in a beautiful and structured UI after performing the co-relation in the results produced by these various tools. The developers behind reNgine understand that recon result most often is overwhelming due to the humongous data, so that's why reNgine also comes with advanced query lookup using natural language operators like and, or and not. Imagine, doing recon on facebook.com and filtering the results like

http_status!404&page_title=admin|page_title=dashboard&content_length>0&tech=php

or

severity=critical|severity=high&vulnerability_title=xss|vulerability_title=cve-1234-xxxx

reNgine's flexibility to easily incorporate any existing open-source tools and with advanced features like configurable scan engines, parallel scans, advanced query lookup on recon results, instant notification about the scan, scheduled scans, etc, separates reNgine from any other recon frameworks.

reNgine can be used for both reconnaissance and actively monitoring the targets.

During the Arsenal, the developers behind reNgine will demonstrate the capabilities and new features announcements.

What has changed since BHEU 2019?
1. Integration of Vulnerability Scanner
2. More powerful query lookup with recon data
3. OSINT Capabilities (Major update)
4. Scan Comparision - ability to identify the changes in subdomains, newly discovered subdomains or subdomains that disappeared in last scan etc
5. Interesting Lookup: reNgine will automatically identify the interesting subdomains and interesting URLs from recon data using the keywords match.
And many more..

                </details>
                
