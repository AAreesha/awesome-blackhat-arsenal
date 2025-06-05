# Europe 2022
---
## 🧠 Tools by Category
### Web/AppSec or Red Teaming

<details><summary><strong>[AppsecStudy - open-source elearning management system for information security](https://github.com/zzzteph)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Ivan Iushkevich](https://img.shields.io/badge/Ivan%20Iushkevich-informational)

                AppsecStudy is an open-source platform for seminars, training, and organizing courses for practical information security for developers and IT specialists. This tool has all the built-in basic requirements needed for organizing normal and productive training.

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[Extensible Azure Security Tool](https://github.com/jsa2)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![joosua santasalo](https://img.shields.io/badge/joosua%20santasalo-informational)

                Extensible Azure Security Tool (Later referred to as E.A.S.T) is a tool for assessing Azure and to some extent Azure AD security controls. The primary use case of EAST is Security data collection for evaluation in Azure Assessments. This information (JSON content) can then be used in various reporting tools, which we use to further correlate and investigate the data.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[h0neytr4p - How to catch the external threat actors with an easy to configure Honeypot.](https://github.com/BSidesSG/2021)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Subhash Popuri](https://img.shields.io/badge/Subhash%20Popuri-informational)

                Working for large clients, we realised that large enterprises don't have any mechanism to trap external threat actors primarily exploiting web vulnerabilities. They are still reliant on threat intel firms to block potential attacker IPs. Sure, there are honeypots but it's really hard and time taking to configure. The turnaround time for SOC teams to configure a honeypot for a recently disclosed vulnerability is very high, discouraging the use of the same. We aim to fix this by introducing a template based honeypot. Honeytrap is stateless, it understands patterns and it can be configured to catch complicated 0day or 1day vulnerability exploitation attempts within minutes. It empowers and encourages blue teams to put an active honeytrap network around the network which can be used to capture Indicators of compromise that can be used to block at the perimeter firewall. h0neytr4p comes in a light weight single binary deployment mode, takes either one or multiple templates as input and has csv output mode which can be easily piped onto custom tools. Currently, it supports HTTP and HTTPS only but the plan is to make it a unified platform that supports SSH, RDP or any other protocols spanning multiple scenarios.

                </details>
                
<details><summary><strong>[Packing-Box: Playing with Executable Packing](https://github.com/packing-box/docker-packing-box/blob/main/CITATIONS.bib)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Alexandre D'Hondt](https://img.shields.io/badge/Alexandre%20D'Hondt-informational) ![Charles-Henry Bertrand Van Ouytsel](https://img.shields.io/badge/Charles-Henry%20Bertrand%20Van%20Ouytsel-informational) ![Axel Legay](https://img.shields.io/badge/Axel%20Legay-informational)

                This Docker image is an experimental toolkit gathering detectors, packers, tools and machine learning mechanics for making datasets of packed executables and training machine learning models for the static detection of packing. It aims to support PE, ELF and Mach-O executables and to study the best static features that can be used in learning-based static detectors.

                </details>
                

### Red Teaming

<details><summary><strong>[JavaScript Obfuscation - It's All About the P-a-c-k-e-r-s](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Web.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Or Katz](https://img.shields.io/badge/Or%20Katz-informational)

                The usage of JavaScript obfuscation techniques have become prevalent in today's threats, from phishing pages, to Magecart, and supply chain injection to JavaScript malware droppers all use JavaScript obfuscation techniques on some level.

The usage of JavaScript obfuscation enables evasion from detection engines and poses a challenge to security professionals, as it hinders them from getting quick answers on the functionality of the examined source code.

Deobfuscation can be technically challenging (sometimes), risky (if you don't know what you are doing), and time consuming (if you are lazy, as I am). Yet, the need to find and analyze high scaled massive attacks using JavaScript obfuscation is a task I'm faced with on a daily basis.

In this arsenal showcase I will present a lazy, performance cost effective approach, focusing on the detection of JavaScript packer templates. Once combined with threat intelligence heuristics, this approach can predict the maliciousness level of JavaScript with high probability of accuracy.

In addition, the showcase will include insights based on detections of the tool that were collected from the threat landscape, including some of the challenges associated with benign websites using obfuscation.

The showcase will also suggest techniques showing how the tool obfuscation detection can also be combined with other threat intelligence signals and heuristics, that can lead to better classification of detect obfuscated code as being malicious.

                </details>
                
<details><summary><strong>[Shoggoth: Asmjit Based Polymorphic Encryptor](https://github.com/frkngksl)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Furkan Goksel](https://img.shields.io/badge/Furkan%20Goksel-informational)

                From past to present, signature-based detection has been one of the first and most basic methods used to detect malicious files. Even today, every file written to the file system is first scanned using the signatures found in the database of security products. Therefore, when creating variants of a tool or a technique, one of the most used methods to prevent them from being captured by a single signature is Polymorphism.

While polymorphism was used for this purpose, it was embedded in the virus variant as an engine, especially in self-propagating viruses. Nowadays, polymorphism occurs in the obfuscation of a binary or a shellcode. New variants of these codes, which are produced with polymorphic encoders such as Shikata Ga Nai (SGN), make them difficult to detect with a general and single YARA rule. Shoggoth is yet another polymorphic encoder written using asmjit library.

For each encoding period of a binary, Shoggoth generates different encryption routines with different garbage instructions. After obtaining the encrypted form of the payload, the tool merges it with its decryptor stub which again contains different garbage instructions. Shoggoth uses asmjit library for assembling the process of randomly generated encryption and garbage instructions.

                </details>
                
<details><summary><strong>[ThunderCloud: Attack Cloud Without Keys!](https://github.com/Rnalter/ThunderCloud)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Shivankar Shivankar](https://img.shields.io/badge/Shivankar%20Shivankar-informational)

                "You can't audit a cloud environment without access keys!!".

Well. That's not completely true.

There is a good number of tools that help security teams find cloud misconfiguration issues. They work inside-out way where you give read-only access tokens to the tool and the tool gives you misconfigurations.

There's no single tool that helps Red Teamers and Bug Hunters find cloud misconfiguration issues the outside-in way.

This outside-in approach can find issues like:

1. S3 directory listing due to misconfigured Cloudfront settings
2. Amazon Cognito misconfiguration to generate AWS temporary credentials
3. Public snapshots
4. Generate Account takeover Phishing links for AWS SSO
5. Leaked Keys permission enumeration
6. IAM role privilege escalation
a) From leaked keys
b) Lambda Function

This exploitation framework also helps teams within organizations to do red teaming activities or run it across the accounts to learn more about misconfigurations from AWS and how badly they can be exploited.

ThunderCloud version 2 will now support GCP and Azure exploitation. Additionally will be releasing an open source "CLOUD OFFENSIVE" gitbook along with the same

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[RFQuack: A Versatile, Modular, RF Security Toolkit](https://github.com/rfquack/RFQuack/blob/master/pyproject.toml)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Federico Maggi](https://img.shields.io/badge/Federico%20Maggi-informational)

                Software-defined radios (SDRs) are indispensable for signal reconnaissance and physical-layer dissection, but despite we have advanced tools like Universal Radio Hacker, SDR-based approaches require substantial effort. Contrarily, RF dongles such as the popular Yard Stick One are easy to use and guarantee a deterministic physical-layer implementation. However, they're not very flexible, as each dongle is a static hardware system with a monolithic firmware. We present RFquack, an open-source tool and library firmware that combines the flexibility of a software-based approach with the determinism and performance of embedded RF frontends. RFquack is based on a multi-radio hardware system with swappable RF frontends, and a firmware that exposes a uniform, hardware-agnostic API. RFquack focuses on a structured firmware architecture that allows high- and low-level interaction with the RF frontends. It facilitates the development of host-side scripts and firmware plug-ins, to implement efficient data-processing pipelines or interactive protocols, thanks to the multi-radio support. RFquack has an IPython shell and 9 firmware modules for: spectrum scanning, automatic carrier detection and bitrate estimation, headless operation with remote management, in-flight packet filtering and manipulation, MouseJack, and RollJam (as examples). We used RFquack in high-schools to teach digital RF protocols, to setup RF hacking contests, and to analyze industrial-grade devices and key fobs, on which we found and reported 11 vulnerabilities in their RF protocols.

                </details>
                

### OSINT

<details><summary><strong>[shrewdeye - low hanging OSINT and reconnaissance](https://github.com/zzzteph)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Ivan Iushkevich](https://img.shields.io/badge/Ivan%20Iushkevich-informational)

                The vulnerability searching process requires a lot of time. If you want to cover all the perimeter in an appropriate amount of time and get valuables, automation of routines is one of the cornerstones, that will help you to focus on more complex things.
shrewdeye - opensource web platform for continuous reconnaissance. It allows you to combine other tools in chain to automate your perimeter workflow reconnaissance. It comes with built-in modules for famous tools like amass, assetfinder, subfinder, gau, nmap and others.

                </details>
                
