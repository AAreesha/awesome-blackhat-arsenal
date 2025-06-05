# Asia 2022
---
## 🛠️ Tools from BH-ARSENAL

### [AISY: A Framework for Deep Learning-Based Side-Channel Analysis](https://github.com/AISyLab/AISY_Framework)
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Stjepan Picek](https://img.shields.io/badge/Stjepan%20Picek-informational)
Profiling side-channel attacks (SCA) allow evaluators to verify the worst-case security scenario of their products. Nowadays, deep learning has become the state-of-the-art method for profiling SCA as deep neural networks show the ability to learn side-channel leakages from protected implementations. While deep learning is a powerful technique for security evaluations, it offers numerous possibilities for neural network configurations and optimization techniques. Selecting the best setup for each evaluated product is far from trivial and requires expertise in SCA and deep learning fields. To improve SCA methods, and at the same time to be able to investigate the resistance of the product to more complex attack scenarios, researchers continuously propose new techniques.
Unfortunately, several obstacles are making the acceptance of such techniques a challenge. Security evaluators from the industry face difficulties following up on new promising methods. What is more, certification bodies also must be aware of new SCA techniques to issue the certifications. Indeed, one of the main issues is the lack of publicly available, easy-to-use frameworks that allow powerful and reliable side-channel analysis. Moreover, due to the absence of the uniformed evaluation/implementation method, the reproducibility of the outcomes is not easy to ensure.

We propose AISY as a tool to allow state-of-the-art deep learning-based SCA. AISY is a python-based open-source framework, and it provides state-of-the-art functionalities for profiling SCA with easy usage, extensibility, reproducibility, integrated database, and user interface. We envision a system where the user can efficiently run the attacks with few lines of code and based on state-of-the-art but also extend those functionalities to support new developments. AISY supports the complete development cycle for deep learning-based SCA: from dataset preparation to the automated development of new models and their assessment concerning the side-channel metrics.

### C0deVari4nt
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Chloe Ong](https://img.shields.io/badge/Chloe%20Ong-informational) ![Kar Wei Loh](https://img.shields.io/badge/Kar%20Wei%20Loh-informational)
None

### ChainAlert: Alert Developers and Open Source Maintainers of Potential Supply Chain Attacks and Suspicious Package Release
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Lior Kaplan](https://img.shields.io/badge/Lior%20Kaplan-informational) ![Jossef Harush](https://img.shields.io/badge/Jossef%20Harush-informational)
None

### CrowdSec: The Open-Source and Participative IPS
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Jean Devaux](https://img.shields.io/badge/Jean%20Devaux-informational) ![Sebastien Blot](https://img.shields.io/badge/Sebastien%20Blot-informational) ![Philippe Humeau](https://img.shields.io/badge/Philippe%20Humeau-informational)
None

### [EMBA: Open-Source Firmware Security Testing](https://github.com/e-m-b-a/emba/blob/master/emba)
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Michael Messner](https://img.shields.io/badge/Michael%20Messner-informational) ![Pascal Eckmann](https://img.shields.io/badge/Pascal%20Eckmann-informational)
IoT (Internet of Things) and OT (Operational Technology) are the current buzzwords for networked devices on which our modern society is based on. In this area, the used operating systems are summarized with the term firmware. The devices themselves, also called embedded devices, are essential in the private and industrial environments as well as in the so-called critical infrastructure.

Penetration testing of these systems is quite complex as we have to deal with different architectures, optimized operating systems, and special protocols. EMBA is an open-source firmware analyzer with the goal to simplify and optimize the complex task of firmware security analysis. EMBA supports the penetration tester with the automated detection of 1-day vulnerabilities on binary level. This goes far beyond the plain CVE detection: With EMBA you always know which public exploits are available for the target firmware. Besides the detection of already known vulnerabilities, EMBA also supports the tester on the next 0-day. For this, EMBA identifies critical binary functions, protection mechanisms and services with network behavior on a binary level. There are many other features built into EMBA, such as fully automated firmware extraction, finding file system vulnerabilities, hard-coded credentials, and more.

EMBA is the open-source firmware scanner, created by penetration testers for penetration testers.

### Flopz: Patch, Debug and Instrument Firmware When All You Have Is a Binary
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Henrik Ferdinand Nölscher](https://img.shields.io/badge/Henrik%20Ferdinand%20Nölscher-informational) ![Luca Dubies](https://img.shields.io/badge/Luca%20Dubies-informational)
None

### [Hayabusa](https://github.com/YamatoSecurity)
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Zach Mathis](https://img.shields.io/badge/Zach%20Mathis-informational)
Hayabusa is a sigma-based threat hunting and fast forensics timeline generator for Windows event logs written in rust by Yamato Security. Rules can either be written sigma or built-in hayabusa rules that let the analyst extract out only the important fields for Windows DFIR investigations.

### kdigger: A Context Discovery Tool for Kubernetes Penetration Testing
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Mahé Tardy](https://img.shields.io/badge/Mahé%20Tardy-informational)
None

### [Kinstrument: Binary-Only Instrumentation Framework for Linux Kernel Based on Breakpoint](https://github.com/hac425xxx/hac425xxx)
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Sili Luo](https://img.shields.io/badge/Sili%20Luo-informational)
For regular Linux kernels, we can use qemu or vmware, and then use gdb to debug the kernel, but for some special embedded devices, such as Android phones, it is difficult to debug and instrument the kernel. In order to debug the kernel, it often needs to recompile the kernel and use additional hardware.

The characteristics of kinstrument are as follows:

1. The kernel only needs to support the insertion of the ko module, the kernel does not need to be recompiled, and no additional hardware is required.
2. Support instrumentation basic blocks, and get basic block coverage of kernel code
3. Use the breakpoint mechanism to hook and debug arbitrary instructions.


Kinstrument can be used for kernel debugging and Fuzz.

### KNX Bus Dump
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Christopher Morales-Gonzalez](https://img.shields.io/badge/Christopher%20Morales-Gonzalez-informational) ![Michael Cash](https://img.shields.io/badge/Michael%20Cash-informational)
None

### Lupo: Malware IOC Extractor
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Vishal Thakur](https://img.shields.io/badge/Vishal%20Thakur-informational)
None

### Mitigating Open Source Software Supply Chain Attacks
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Ashish Bijlani](https://img.shields.io/badge/Ashish%20Bijlani-informational) ![Ajinkya Rajput](https://img.shields.io/badge/Ajinkya%20Rajput-informational)
None

### [Mobile App API Penetration Platform](https://github.com/Trustworthy-AI-Group/Adversarial_Examples_Papers)
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Yifeng Zhang](https://img.shields.io/badge/Yifeng%20Zhang-informational)
There are many protections being applied to mobile applications nowadays, and most penetration testing engineer use primitive methods to crack them. Therefore, if we can modify the data or insert the payload of the vulnerability before the protection is processed, all the protections will be transparent to the penetration testers and there will be no concern about their implementation, making app API testing purer.

### Node Security Shield
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Sukesh Pappu](https://img.shields.io/badge/Sukesh%20Pappu-informational) ![Lavakumar Kuppan](https://img.shields.io/badge/Lavakumar%20Kuppan-informational)
None

### [NtHiM (Now, the Host is Mine!): Super Fast Sub-Domain Takeover Detection](https://github.com/TheBinitGhimire/NtHiM)
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Binit Ghimire](https://img.shields.io/badge/Binit%20Ghimire-informational)
NtHiM, which stands for "Now, the Host is Mine!" is a Rust-based systems project, which enables security enthusiasts to discover subdomain takeover vulnerabilities in hostnames (domains and subdomains) from different organizations.


In this session, I will be discussing about the following things, apart from an introduction of myself as the project maintainer and your presenter for this session.

Project Overview
Brief Introduction (what this project actually is)
Initiation Story (how I decided to start working on this project)
Brief Logic Explanation (understanding the project workflow with a simple pseudocode)
Project Features (getting to know about all of the things built into the project)
User-level Video Documentation (Demonstration; including guides for the end-users of this project)
Developer-level Video Documentation (Demonstration; including guides on how you can get started with extending or contributing to this project)

### Purpleteaming with OWASP PurpleTeam (tool)
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Kim Carter](https://img.shields.io/badge/Kim%20Carter-informational)
OWASP PurpleTeam is a security regression testing SaaS and CLI that targets web applications and APIs. It can be run manually or sit within your build pipeline to continuously test your creations in close to real-time. Not only does PurpleTeam help you find and fix your security defects, it also helps train Developers and DevOps Engineers to recognise security defects and how to not introduce the same defects in the future.

### Pwnppeteer - Phishing Post {Exploi/Automa}tion at Scale
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Joffrey Czarny](https://img.shields.io/badge/Joffrey%20Czarny-informational)
None

### Rate Unlimiter
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![George Chen](https://img.shields.io/badge/George%20Chen-informational) ![Zheng Wei Chen](https://img.shields.io/badge/Zheng%20Wei%20Chen-informational)
None

### SCYTHE: The Yara Signature Crafter that Fingerprints Honeypot Traffic
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Shashank Gangaraju](https://img.shields.io/badge/Shashank%20Gangaraju-informational) ![Yu Zeng](https://img.shields.io/badge/Yu%20Zeng-informational) ![George Chen](https://img.shields.io/badge/George%20Chen-informational)
None

### Telegrip Forensic Tool
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Norah Alkhathlan](https://img.shields.io/badge/Norah%20Alkhathlan-informational)
None

### TMoC: Threat Modeler on Chain
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Yejun Kim](https://img.shields.io/badge/Yejun%20Kim-informational) ![Kwangsoo Cho](https://img.shields.io/badge/Kwangsoo%20Cho-informational) ![Paul Hong](https://img.shields.io/badge/Paul%20Hong-informational) ![Seungjoo Kim](https://img.shields.io/badge/Seungjoo%20Kim-informational)
None

### Tsurugi Linux Project: The Right Tool in the Wrong Time
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Tool](https://img.shields.io/badge/Tool-green) ![Giovanni Rattaro](https://img.shields.io/badge/Giovanni%20Rattaro-informational) ![Marco Giorgi](https://img.shields.io/badge/Marco%20Giorgi-informational)
Any DFIR analyst knows that everyday in many companies, it doesn't matter the size, it's not easy to perform forensics investigations often due to lack of internal information (like mastery all IT architecture, have the logs or the right one...) and ready to use DFIR tools.

As DFIR professionals we have faced these problems many times and so we decided last year to create something that can help who will need the right tool in the "wrong time" (during a security incident).

And the answer is the Tsurugi Linux project that, of course, can be used also for educational purposes.
After more than a year since the last release, a Tsurugi Linux special BLACK HAT EDITION with this major release will be shared with the participants before the public release.
