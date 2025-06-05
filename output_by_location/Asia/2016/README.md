# Asia 2016
---
## 🧠 Tools by Category
### Blue Team & Detection

<details><summary><strong>[BTA: An Open-Source Active Directory Security Audit Framework](https://github.com/adulau/hack-lu-website/blob/master/agenda/index.md)</strong></summary>

                ![BH-ASIA-16](https://img.shields.io/badge/BH-ASIA-16-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Joffrey Czarny](https://img.shields.io/badge/Joffrey%20Czarny-informational)

                When it comes to the security of the information system, Active Directory domain controllers are, or should be, at the center of concerns, which are (normally) to ensure compliance with best practices, and during a compromise proved to explore the possibility of cleaning the information system without having to rebuild Active Directory. Indeed, backdoors can be implemented in Active Directory to help an intruder to gain back his privileges. However, few tools implement this cleaning/survey process despite several ways existing for backdooring Active Directory.We propose to present some possible backdoors which could be set by an intruder in Active Directory to keep administration rights. For example, how to modify the AdminSDHolder container in order to reapply rights after administrator actions. Then, we will present BTA, an audit tool for Active Directory databases, and our methodology for verifying the application of good practices and the absence of malicious changes in these databases. One of example, that we will show, is how to spot accounts which have DCSync rights and pulls account credentials through the standard Domain Controller replication API.The presentation will be organized as follows:We begin by describing the stakes around the Active Directory, centerpiece of any information system based on Microsoft technologies.We will continue by demonstrating some backdoors in order to keep admins rights or to help an intruder to quickly recover admins rights.We will present BTA and the methodology developed to analysis Active Directory.We conclude with a feedback on real world usage of BTA.More information can be found on the Bitbucket repository: https: //bitbucket.org/iwseclabs/bta

                </details>
                
<details><summary><strong>[Limon - Sandbox for Analyzing Linux Malwares](https://github.com/monnappa22/Limon/blob/master/limon.py)</strong></summary>

                ![BH-ASIA-16](https://img.shields.io/badge/BH-ASIA-16-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Monnappa K A](https://img.shields.io/badge/Monnappa%20K%20A-informational)

                Limon is a sandbox for automating Linux malware analysis. It collects, analyzes, and reports on the run time indicators of Linux malware. It allows one to inspect the Linux malware before execution, during execution, and after execution (post-mortem analysis) by performing static, dynamic and memory analysis using open source tools. Limon analyzes the malware in a controlled environment, monitors its activities and its child processes to determine the nature and purpose of the malware. It determines the malware's process activity, interaction with the file system, network, it also performs memory analysis and stores the analyzed artifacts for later analysis.For more information, please visit this blog post on Limon: http://malware-unplugged.blogspot.in/2015/11/limon-sandbox-for-analyzing-linux.html; the download link is also available on GitHub: https://github.com/monnappa22/Limon.

                </details>
                
<details><summary><strong>[VirusTotal](https://github.com/orgs/VirusTotal/people)</strong></summary>

                ![BH-ASIA-16](https://img.shields.io/badge/BH-ASIA-16-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Karl Hiramoto](https://img.shields.io/badge/Karl%20Hiramoto-informational)

                VirusTotal is the free online file and URL scanner that everyone knows. However there are many free features that many users don't know about such as:A free public API for anyone to automate file or URL analysis.IP address and domain reputation. See malware files known to be associated with a particular IP address or domain, and history Passive DNS infoSearching on file hash, and related filesSysinternals, Carbon black, etc. integrationsStatic analysis of files, structural analysis of many file types (PE, ELF, APK, ZIP, RAR, MACHO, .NET, office, etc)Sandbox dynamic analysis of PE, APK, Apple Mach-O, and applications.ROMS, BIOS, and firmware filesSSDEEP, authentihash, imphash, and other similarity indexesCertificate checks on signed filesWhitelisting of trusted filesFree desktop scanning applications for Windows, MAC, and open source for compilation on linux.

                </details>
                

### Red Teaming

<details><summary><strong>[HackSys Extreme Vulnerable Driver](https://github.com/hacksysteam/HackSysExtremeVulnerableDriver)</strong></summary>

                ![BH-ASIA-16](https://img.shields.io/badge/BH-ASIA-16-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Ashfaq Ansari](https://img.shields.io/badge/Ashfaq%20Ansari-informational)

                HackSys Extreme Vulnerable Driver is an intentionally vulnerable Windows Kernel driver developed for security enthusiasts to learn and polish their exploitation skills. HackSys Extreme Vulnerable Driver caters to a wide range of vulnerabilities ranging from simple Buffer Overflow to complex Use After Free, Pool Overflow, Type Confusion and Arbitrary Memory Overwrite. This allows researchers to explore different exploitation techniques for every implemented vulnerabilities. HackSys Extreme Vulnerable Driver also comes with the mitigation for each implemented vulnerability which helps kernel driver developers understand how these mitigations are applied.Source Code: https://github.com/hacksysteam/HackSysExtremeVulnerableDriver Blog: http://www.payatu.com/hacksys-extreme-vulnerable-driver/

                </details>
                
<details><summary><strong>[Rudra: The Destroyer of Evil](https://github.com/7h3rAm/rudra)</strong></summary>

                ![BH-ASIA-16](https://img.shields.io/badge/BH-ASIA-16-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Ankur Tyagi](https://img.shields.io/badge/Ankur%20Tyagi-informational)

                Rudra aims to provide a developer-friendly framework for exhaustive analysis of (PCAP and PE) files. It provides features to scan and generate reports that include file's structural properties, entropy visualization, compression ratio, theoretical minsize, etc. These details, alongwith file-format specific analysis information, help an analyst to understand the type of data embedded in a file and quickly decide if it deserves further investigation.Rudra is the only tool to provide an effective bot based query mechanism for scanning files. Users can use Twitter and mention a Pastebin link that stores the base64 encoded version of the file to be scanned. It will pull the file from Pastebin, perform base64 decoding, initiate scanning on decoded file, submit base64 encoded json report to Pastebin and post a reply tweet with its link. This provides a quick and effective option to try Rudra without installing it.Rudra supports scanning PE files and can perform API scans, anti{debug, vm, sandbox} detection, packer detection, authenticode verification, alongwith Yara, shellcode, and regex detection upon them. Additionally, following new features are being added for the first beta release:Interactive console providing access to all internal data structures and objects, exposing a rich API for usersPlugin architecture to operate upon decoded file content (usecases might be to write a decoder for a new RAT found in the wild or to write a custom unpacker for a binary stub, etc.)Extracting subfiles and optionally scanning them if neededHeuristics to identify suspicious network flows and exe filesThe report for each analyzed file can be dumped to disk as a JSON/HTML/PDF. If needed, analysis can be customized via CLI arguments, config file, or interactive console.Rudra also supports protocol identification, decoding, and normalization. It can analyze embedded URLs and IP addresses within files and gather whois/geolocation information for them. Users can view live mapping of identified hosts and correlate the results from different analysis modules to perform deeper investigation.

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[SecBee](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Wireless.md)</strong></summary>

                ![BH-ASIA-16](https://img.shields.io/badge/BH-ASIA-16-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Tobias Zillner](https://img.shields.io/badge/Tobias%20Zillner-informational)

                SecBee is a ZigBee security testing tool. It is basically a kind of ZigBee vulnerability scanner, which allows the mapping of ZigBee networks and enables security testers and developers to check the actual product implementation for ZigBee specific vulnerabilities.Currently it supports direct and indirect ZigBee communication and provides features for command injection, scan for enabled devices, sniff network keys in plaintext and encrypted with the ZigBee default key and an insecure rejoin request.The tool is still under development and additional features are added. The final goal is to test for the correct application and implementation of every ZigBee security service.

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[Seebug](https://github.com/echarts-maps/echarts-cities-js)</strong></summary>

                ![BH-ASIA-16](https://img.shields.io/badge/BH-ASIA-16-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Zhong Chenming](https://img.shields.io/badge/Zhong%20Chenming-informational)

                Seebug is an open vulnerability platform based on vulnerability and PoC/Exp sharing communities. So far, it already has 50,000+ vulnerabilities and 40,000+ PoC/Exps.On this platform, users can submit new vulnerabilities or update information of existing ones that are lacking of details such as summaries, PoC/Exps, solutions, CVE-ID and other basic fields. In exchange, we will reward you with KBs, which can be used to buy other submissions (such as PoCs) or converted into RMB directly (1 KB is equivalent to RMB 5 Yuan currently).Seebug provides an opportunity for vulnerability learning. We plan to open BBS and CFP columns in the near future so that users can submit their technical articles, ideas, and communicate with each other on vulnerability mining issues.Besides, each vulnerability is accompanied by a lifeline, recording all the relevant events during this process and offering a complete picture about the vulnerability development course.With the help of ZoomEye, the latest vulnerabilities across the world can be detected timely and displayed on the vulnerability detail page. Based on the result, we can effectively conduct emergency response activities and provide online detection tools, affected vendor lists and early warning upon necessary.

                </details>
                

### OSINT

<details><summary><strong>[SensePost Toolset](https://github.com/planglois925/twitter_networker_simple/blob/master/data.json)</strong></summary>

                ![BH-ASIA-16](https://img.shields.io/badge/BH-ASIA-16-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Daniel Cuthbert](https://img.shields.io/badge/Daniel%20Cuthbert-informational)

                The SensePost Toolset consists of numerous transforms and mini-sets of transforms. This includes OSINT, language translation, twitter monitoring, Spotify, Skype stalking and detailed in-depth foot-printing capabilities.Sense Post Toolkit:https://www.sensepost.com/discover/tools/maltego/osint/SPToolset/

                </details>
                
