# USA 2017
---
## 🧠 Tools by Category
### Red Teaming

<details><summary><strong>A NEW TAKE AT PAYLOAD GENERATION: EMPTY-NEST</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![James Cook](https://img.shields.io/badge/James%20Cook-informational) ![Tom Steele](https://img.shields.io/badge/Tom%20Steele-informational)

🔗 **Link:** [A NEW TAKE AT PAYLOAD GENERATION: EMPTY-NEST](#)  
📝 **Description:** As the evolution of endpoint, egress, and network security controls continues, adversaries and pentesters are finding it increasingly more difficult to execute malicious payloads within properly-hardened enterprise networks. Although tools currently exist to aid in circumventing these controls, the current state fails to properly account for some of newest techniques used by these controls. Enter Empty-Nest, a command-and-control (C2) toolset created with circumvention in mind. Empty-Nest was designed to provide a flexible payload-generation mechanism and pluggable interface to enable adversaries to easily customize payloads for targeted security control bypass. Our presentation shows the Empty-Nest toolset, demonstrating how to leverage the pluggable interface to create keyed payloads capable of bypassing new-age, cloud-based binary analysis, unloading endpoint software DLLs from running processes, customizing C2 transports, and more.

</details>

<details><summary><strong>AVET - ANTIVIRUS EVASION TOOL</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Daniel Sauder](https://img.shields.io/badge/Daniel%20Sauder-informational)

🔗 **Link:** [AVET - ANTIVIRUS EVASION TOOL](#)  
📝 **Description:** Avet is an antivirus evasion tool: (link: https://github.com/govolution/avet).

What & Why:

When running an exe file made with msfpayload & co, the exe file will often be recognized by the antivirus software
Avet is a antivirus evasion tool targeting windows machines
The techniques used in avet evaded 9 antivirus suites (all of the tested), including MS Defender, McAfee, Sophos, Avira and more
Avet includes two tools, avet.exe with different antivirus evasion techniques and make_avet for compiling a preconfigured binary file
Avet.exe loads ASCII encoded shellcode from a textfile or from a webserver, further it is using an av evasion technique to avoid sandboxing and emulation
For encoding the shellcode the tools format.sh and sh_format are included
Avet is tested with Kali 2 and tdm-gcc
Interactive assistant for easier usage
Support for 64bit payloads

New:

More payloads
Support for metasploit psexec

Tool URLS:


Paper: https://govolution.wordpress.com/2017/07/27/paper-avet-blackhat-usa-2017/
GitHub: https://github.com/govolution/avet

</details>

<details><summary><strong>BLOODHOUND 1.3 - ARSENAL THEATER DEMO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Andy Robbins](https://img.shields.io/badge/Andy%20Robbins-informational) ![Rohan Vazarkar](https://img.shields.io/badge/Rohan%20Vazarkar-informational) ![Will Schroeder](https://img.shields.io/badge/Will%20Schroeder-informational)

🔗 **Link:** [BLOODHOUND 1.3 - ARSENAL THEATER DEMO](#)  
📝 **Description:** Released on-stage at DEF CON 24 last year, BloodHound fundamentally changed the way penetration testers and red teamers approach escalating rights in Active Directory domains. By combining the concepts of derivative local admin and graph theory, coupled with a powerful data ingestion and front-end analysis capability, BloodHound simplified the tedious, repetitive task of escalating rights, saving days, weeks, and sometimes months of manual processing.

In 2017, the BloodHound attack graph schema, data ingestor, and front-end were overhauled to provide greater speed, easier analysis, and brand new attack paths never discovered before. By adding object control edges to the attack graph, a brand new attack landscape was unveiled, allowing attackers and defenders to identify attacks which rely solely on Active Directory object manipulation. These attack paths require no malware, no pivoting, and can always be executed as long as the attacker can communicate with at least one domain controller. From the defender's perspective, identifying and measuring such attack paths was nigh impossible. Now, defenders can also quickly identify and remediate those same attack paths before an attacker can find and exploit them.

</details>

<details><summary><strong>BUILDING C2 ENVIRONMENTS WITH WARHORSE</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Ralph May](https://img.shields.io/badge/Ralph%20May-informational)

🔗 **Link:** [BUILDING C2 ENVIRONMENTS WITH WARHORSE](#)  
📝 **Description:** Building full featured command-and-control (C2) environments can be a major undertaking, taking significant time and effort. However, deployment or proper infrastructure is key to avoiding detection and maintaining proper operational security during offensive engagements. In many instances, once a C2 environment is operational, it's utilized for a short period then destroyed. There are many different tools used within these C2 environments, with most tools requiring significant amounts of manual configuration. In recent years, API-based, on-demand cloud infrastructure has reduced the cost of building a C2 environment while also exposing functionality that encourages process automation. Combine these on-demand cloud services with the rapid development of Docker containers, and you have the building blocks to create and deploy C2 environments on the fly. Warhorse has been designed to build these C2 environments with only minimal configuration. Warhorse enables pentesters to focus on tactics instead of managing C2 infrastructure. Warhorse approaches this creation of a C2 environment with a few unique features. First, it uses a module-based approach to everything that it creates. This way, any new tactics or tools can be added as a module to utilize in creating a C2 environment. Second, Warhorse is vendor-agnostic and can be used with any cloud service provider. This allows C2 environments to live in multiple data centers and utilize multiple vendors. Lastly, Warhorse employs a two-zone approach to limit backend C2 exposure. Systems that communicate directly with the target are treated as expendable and can have very short life spans. These features combined not only help with rapid deployment but also allow pentesters to build environments with the latest tactics and techniques that can evolve on the fly and be moved whenever required.

</details>

<details><summary><strong>CRACKMAPEXEC V4</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Marcello Salvati](https://img.shields.io/badge/Marcello%20Salvati-informational)

🔗 **Link:** [CRACKMAPEXEC V4](#)  
📝 **Description:** CrackMapExec (a.k.a CME) is a fully open-source, post-exploitation tool written in Python that helps automate assessing the security of *large* Active Directory networks. Built with stealth in mind, CME follows the concept of "Living off the Land:" abusing built-in Active Directory features/protocols to achieve it's functionality and allowing it to evade endpoint protection/IDS/IPS solutions. CME makes heavy use of the Impacket library and the PowerSploit Toolkit for working with network protocols and performing a variety of post-exploitation techniques. Although meant to be used primarily for offensive purposes (e.g. red teams), CME can be used by blue teams as well to assess account privileges, find possible misconfigurations and simulate attack scenarios. In this demo the author will be showing version 4.0: a major update to the tool bringing more modules, features and capabilities than ever before. If you're interested in the latest & greatest Active Directory attacks, techniques and general cool AD stuff this is the demo for you!

</details>

<details><summary><strong>CUMULUS - A CLOUD EXPLOITATION TOOLKIT</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Javier Godinez](https://img.shields.io/badge/Javier%20Godinez-informational)

🔗 **Link:** [CUMULUS - A CLOUD EXPLOITATION TOOLKIT](#)  
📝 **Description:** There is a lack of tools for testing the security of Cloud deployments; the Cumulus Toolkit is an attack framework for exploiting the Cloud's weak points.

The Cloud enables software projects to speed up development because it allows developers to provision infrastructure and make configuration changes to their networks without much friction. This ease of deployment was but a dream in the age of the traditional datacenter. However, the Cloud also brings new attack surface which needs further exploration. Cloud Identity and Access Management (IAM) services (such as Amazon's) are primary targets for attackers, as these typically control access to hundreds of API calls over many services.

Over the years there have been various discussions around cloud security, e.g., Pivoting in Amazon Clouds (2013), and few tools have been developed to enable testing the security of Cloud deployments. These tools are standalone, have not attained wide adoption, and/or have not made it into widely adopted toolkits. To fill this void, we have developed the Cumulus Toolkit. The Cumulus Toolkit is a Cloud exploitation toolkit based on the Metasploit Framework. We chose Metasploit because of its wide adoption and its wealth of existing features.

The Cumulus toolkit is a set of modules that can be used perform privilege escalation, account takeover, and to launch unauthorized workloads. To illustrate security concerns resulting from lax IAM policies, we present the Create IAM User module which can be used to create a user with administrative privileges. To perform complete account takeover, an attack that we've seen in the wild, we present the User Locker module which is used to lock out all legitimate users out of the account. Finally, we present the Launch Instances module which can be used to launch Cloud hosts on demand.

</details>

<details><summary><strong>EAPHAMMER</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Gabriel Ryan](https://img.shields.io/badge/Gabriel%20Ryan-informational)

🔗 **Link:** [EAPHAMMER](#)  
📝 **Description:** EAPHammer is a toolkit for performing targeted evil twin attacks against WPA2-Enterprise networks. It is designed to be used in full scope wireless assessments and red team engagements. As such, focus is placed on providing an easy-to-use interface that can be leveraged to execute powerful wireless attacks with minimal manual configuration. To illustrate how fast this tool is, here's an example of how to setup and execute a credential stealing evil twin attack against a WPA2-TTLS network in just two commands:

# generate certificates
./eaphammer --cert-wizard

# launch attack
./eaphammer -i wlan0 --channel 4 --auth ttls --wpa 2 --essid CorpWifi --creds

Features:

Steal RADIUS credentials from WPA-EAP and WPA2-EAP networks.
Perform hostile portal attacks to steal AD creds and perform indirect wireless pivots
Perform captive portal attacks
Built-in Responder integration
Support for Open networks and WPA-EAP/WPA2-EAP
No manual configuration necessary for most attacks.
No manual configuration necessary for installation and setup process

</details>

<details><summary><strong>GDB ENHANCED FEATURES (GEF)</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Chris Alladoum](https://img.shields.io/badge/Chris%20Alladoum-informational)

🔗 **Link:** [GDB ENHANCED FEATURES (GEF)](#)  
📝 **Description:** GEF is a set of commands for GDB, to massively boost the exploit development process on X86, ARM, MIPS, PowerPC and SPARC. GEF aims to be used mostly by exploit development and reverse-engineers, to provide greatly enhanced features to GDB heavily relying on Python API to assist during the process of dynamic analysis and exploit development.

</details>

<details><summary><strong>GOFETCH</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Tal Maor](https://img.shields.io/badge/Tal%20Maor-informational)

🔗 **Link:** [GOFETCH](#)  
📝 **Description:** GoFetch is a tool to automatically exercise an attack plan generated by the BloodHound application. The tool first loads a path of local admin users and computers generated by BloodHound and convert it to it's own attack plan format. Once the attack plan is ready, it advances towards the destination according to the plan, step by step by successively apply remote code execution techniques and compromising credentials with Mimikatz.

</details>

<details><summary><strong>GONE IN 59 SECONDS - HIGH SPEED BACKDOOR INJECTION VIA BOOTABLE USB - ARSENAL THEATER DEMO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Michael Wrzesniak](https://img.shields.io/badge/Michael%20Wrzesniak-informational) ![Piotr Marszalik](https://img.shields.io/badge/Piotr%20Marszalik-informational)

🔗 **Link:** [GONE IN 59 SECONDS - HIGH SPEED BACKDOOR INJECTION VIA BOOTABLE USB - ARSENAL THEATER DEMO](#)  
📝 **Description:** Gaining physical access was trivial, but now the computer is locked (or off) and time is running out…the "SmuggleBus" allows us to take advantage of unencrypted drives to quickly collect local password hashes and implant the backdoor of our choice without modifying any system binaries - all from a bootable USB and in a matter of seconds.

</details>

<details><summary><strong>GR-LORA: AN OPEN-SOURCE SDR IMPLEMENTATION OF THE LORA PHY</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Matt Knight](https://img.shields.io/badge/Matt%20Knight-informational)

🔗 **Link:** [GR-LORA: AN OPEN-SOURCE SDR IMPLEMENTATION OF THE LORA PHY](#)  
📝 **Description:** gr-lora is an open-source GNU Radio/Software Defined Radio implementation of the LoRa radio physical layer, as derived from the author's black box analysis of the protocol. gr-lora empowers developers and security researchers to think beyond packet sniffing and injection by exposing LoRa's physical layer in software.

LoRa is a wireless networking technology that can be thought of as high-endurance cellular for IoT and embedded devices. It utilizes a unique Chirp Spread Spectrum modulation and layered encoding scheme to achieve remarkable range while remaining frugal on power.

PHYs have long been taken for granted, however research such as Travis Goodspeed's packet-in-packet and Dartmouth/River Loop Security's 802.15.4 chipset fingerprinting have demonstrated that physical layer abuse can have severe consequences further up the stack. As a closed protocol, LoRa has only been exposed via layer 2+ interfaces; thus security researchers and developers have lacked the necessary tools to audit and analyze the security and robustness of its PHY.

With its flexible and open architecture, gr-lora gives security researchers the capability required to explore this nascent protocol from its most fundamental layer.

</details>

<details><summary><strong>JACKIT</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Alex Harvey](https://img.shields.io/badge/Alex%20Harvey-informational) ![Devin Kinch](https://img.shields.io/badge/Devin%20Kinch-informational)

🔗 **Link:** [JACKIT](#)  
📝 **Description:** JackIt is a wireless HID injection attack into NRF-based keyboard/mouse dongles based off the MouseJack vulnerability. It has a strong focus on providing system admins with the tools to demonstrate the attack to help promote and justify the need to move away from wireless keyboard and mice in a corporate environment.

</details>

<details><summary><strong>LEGION - SIMPLE DISTRIBUTED COMPUTING FOR THE MASSES AND PENTESTERS</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Adam Compton](https://img.shields.io/badge/Adam%20Compton-informational) ![Bill Harshbarger](https://img.shields.io/badge/Bill%20Harshbarger-informational)

🔗 **Link:** [LEGION - SIMPLE DISTRIBUTED COMPUTING FOR THE MASSES AND PENTESTERS](#)  
📝 **Description:** At its core, Legion is a distributed computing application. It is written in python and designed from the ground up to fulfill various IT related needs. Whether you need a way to logically distribute large or complex commands across multiple systems, or if you need a way to remotely administer 1 or more other systems, Legion can help. Legion goes beyond a typical Master/Manager/Slave architecture and makes use of a MeshNetworking approach to help to dynamically route around failed nodes and networking issues. Additionally, it has the ability to allow remote shell access to any node as well as send individual commands to 1 or all of the nodes within the mesh. And of course all the communications are encrypted between the nodes. If you want to learn more or just want to see the demo, please stop by.

</details>

<details><summary><strong>LEVIATHAN FRAMEWORK</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Ozge Barbaros](https://img.shields.io/badge/Ozge%20Barbaros-informational) ![Utku Sen](https://img.shields.io/badge/Utku%20Sen-informational)

🔗 **Link:** [LEVIATHAN FRAMEWORK](#)  
📝 **Description:** Leviathan is a mass audit toolkit which has wide range service discovery, brute force, SQL injection detection and running custom exploit capabilities. It consists open source tools such masscan, ncrack, dsss and gives you the flexibility of using them with a combination. The main goal of this project is auditing as many system as possible in country-wide or in a wide IP range.

Main Features:

Discovery: Discover FTP, SSH, Telnet, RDP, MYSQL services running inside a specific country or in an IP range via Shodan, Censys. It's also possible to manually discover running services on a IP range by integrated "masscan" tool.
Brute Force: You can brute force the discovered services with integrated "ncrack" tool. It has wordlists which includes most popular combinations and default passwords for specific services.
Remote Command Execution: You can run system commands remotely on compromised devices.
SQL Injection Scanner: Discover SQL injection vulnerabilities on websites with specific country extension or with your custom Google Dork.
Exploit Specific Vulnerabilities: Discover vulnerable targets with Shodan, Censys or masscan and mass exploit them by providing your own exploit or using pre-included exploits.

</details>

<details><summary><strong>MAILSNIPER</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Beau Bullock](https://img.shields.io/badge/Beau%20Bullock-informational)

🔗 **Link:** [MAILSNIPER](#)  
📝 **Description:** Oftentimes, on penetration tests we find ourselves having elevated access (Domain Admin) within an organization. One of the best ways to demonstrate risk to an organization is to show the ability to gain access to sensitive data. Email is often the primary messaging system inside most organizations and is the go-to medium for simple chit-chat about daily business, password resets, or even corporate strategy.

MailSniper is a PowerShell-based penetration testing tool whose primary purpose is to search through email in a Microsoft Exchange environment for specific terms (i.e. passwords, insider intel, network architecture information, etc.). It can be used as a non-administrative user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain.

MailSniper includes additional modules for attacking externally-facing Outlook Web Access (OWA) and Exchange Web Services (EWS) portals. With MailSniper, it is also possible to: perform password spraying attacks, enumerate internal domain names and usernames, locate inboxes with too broad permissions, and gather the Global Address List containing all email addresses of users at an organization from OWA and EWS.

</details>

<details><summary><strong>RATTLER</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Chris Le Roy](https://img.shields.io/badge/Chris%20Le%20Roy-informational)

🔗 **Link:** [RATTLER](#)  
📝 **Description:** Rattler is a tool that automates the identification of DLL's which can be used for DLL preloading attacks on Windows 7/8.1/10. The automation of such a process significantly decreases the amount of time required to identify vulnerable and exploitable DLL's.

For example, if an application were to have ~100 DLL's and if it took ~2 minutes to test each DLL, that is ~2 hours for a single application to be tested using a manual process. Additionally, the process for testing an application for DLL preloading vulnerabilities is rather simple and can be automated trivially using some C++, Windows API calls and fresh beard oil , hence Rattler.

The identification of vulnerable DLL's can assist in an attacker in achieving code execution or escalation of privileges.

</details>

<details><summary><strong>SETH</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Adrian Vollmer](https://img.shields.io/badge/Adrian%20Vollmer-informational)

🔗 **Link:** [SETH](#)  
📝 **Description:** Seth is a tool written in Python and Bash to MitM RDP connections. It attempts to downgrade the connection and extract clear text credentials - even with Network Level Authentication enabled.

The default configuration in a Windows landscape is to use self-signed certificates to secure SSL connections to RDP hosts. Since self-signed certificates provide almost no security at all, it is obvious that an attacker in a "Man in the Middle" position can simply present their own certificate and eavesdrop on the connection. However, so far there were no freely available open source tools that can do this. In order to raise awareness of how important it is to use properly signed certificates, Seth was developed.

It performs a man in the middle attack, downgrades any additional security if possible and extracts interesting information, such as password hashes, clear text credentials or key stroke events.

</details>

<details><summary><strong>YASUO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Saurabh Harit](https://img.shields.io/badge/Saurabh%20Harit-informational)

🔗 **Link:** [YASUO](#)  
📝 **Description:** Yasuo is a ruby framework that scans for vulnerable 3rd-party web applications. While working on a network security assessment (internal, external, redteam gigs etc.), we often come across vulnerable 3rd-party web applications or web front-ends that allow us to compromise the remote server by exploiting publicly known vulnerabilities. Some of the common & favorite applications are Apache Tomcat administrative interface, JBoss jmx-console, Hudson Jenkins and so on. Searching Exploit-db will reveal over 10,000 remotely exploitable vulnerabilities that exist in tons of web applications/front-ends and could allow an attacker to completely compromise the back-end server. These vulnerabilities range from RCE to malicious file uploads to SQL injection to RFI/LFI etc.

Yasuo is built to quickly scan the network for such vulnerable applications. Currently, it supports around 180 vulnerable applications. In addition to discovering the vulnerable applications through their unique signature, it also detects if the app requires authentication. If it does, Yasuo performs a brute-force attack against them. In the end, it outputs the IP, vulnerable app url, login status and credentials, if found. Currently, many new features are being added to Yasuo, like smart brute-forcing, internal network pentest mode, new signatures etc.

</details>


### Red Teaming / AppSec

<details><summary><strong>AARDVARK AND REPOKID</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Patrick Kelley](https://img.shields.io/badge/Patrick%20Kelley-informational) ![Travis McPeak](https://img.shields.io/badge/Travis%20McPeak-informational)

🔗 **Link:** [AARDVARK AND REPOKID](#)  
📝 **Description:** Amazon AWS provides a tool called "Access Advisor" that shows unused permissions for a given IAM role. Access advisor data can be very valuable for security practitioners as it shows unused permissions that can be removed to harden the environment and promote least privilege best practices.

In the past retrieving Access Advisor information and reclaiming unused permissions has been a tedious and manual process involving logging in to the console and making changes by hand. Aardvark and Repokid are two complementary tools that make this process easy and automatable. Aardvark automatically retrieves access advisor for all roles in all accounts in your environment and exposes it as a queryable API. Repokid uses data presented by Aardvark to enable automatic role right-sizing.

Used together, Aardvark and Repokid can ensure roles retain only the necessary privileges, even in large dynamic AWS deployments.

</details>

<details><summary><strong>HACK/400 AND IBMISCANNER TOOLING FOR CHECKING YOUR IBM I (AKA AS/400) MACHINES!</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Bart Kulach](https://img.shields.io/badge/Bart%20Kulach-informational)

🔗 **Link:** [HACK/400 AND IBMISCANNER TOOLING FOR CHECKING YOUR IBM I (AKA AS/400) MACHINES!](#)  
📝 **Description:** In many industries the back-end systems still rely on "heavy" machines such as IBM i (aka AS/400) for core transactional systems. However, this area remained rather uncovered by security researchers. Back in 2015 I presented certain weaknesses of IBM i security at DefCon 23, providing a demo tool for assessment of IBM i systems and exploitation of some weaknesses, like privilege escalation. Since 2015, we improved the tool making it more useful for security personnel and auditors to assess certain important aspects of IBM i system security. These developments led to also adding new functionality in famous cracking tool, John the Ripper, for AS/400 password hashes. Based on users' feedback we try to make it best of class tooling for security assessments, keeping it open source (GPL) for the community.

</details>

<details><summary><strong>KUBEBOT - SCALEABLE AND AUTOMATED TESTING SLACKBOT WITH THE BACKEND RUNNING ON KUBERNETES</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Anshuman Bhartiya](https://img.shields.io/badge/Anshuman%20Bhartiya-informational)

🔗 **Link:** [KUBEBOT - SCALEABLE AND AUTOMATED TESTING SLACKBOT WITH THE BACKEND RUNNING ON KUBERNETES](#)  
📝 **Description:** Security Testing, or for that matter any sort of testing, is still being done in ways that are not really scalable and extensible. Testers like to write their own tools/scripts and run them locally on their system. There are many problems that plague this kind of approach for testing.

We will be discussing some of these problems and releasing a new tool - KubeBot - that was primarily built for automating and scaling bug bounties i.e. something that would run multiple tools on a schedule against multiple targets and only returns back the output from these tools if the output changes.

However, over time, it has proven out to be a more generic framework that can be leveraged as a harness to run any security testing tool and is easily scaleable (because of Kubernetes in the backend). It is extensible and provides a nice front end in the form of a Slackbot so that you can look at the results on a real-time basis.

Tool URL: ﻿https://github.com/anshumanbh/kubebot

</details>

<details><summary><strong>POWERSAP: POWERSHELL TOOL TO ASSESS SAP SECURITY</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Joffrey Czarny](https://img.shields.io/badge/Joffrey%20Czarny-informational)

🔗 **Link:** [POWERSAP: POWERSHELL TOOL TO ASSESS SAP SECURITY](#)  
📝 **Description:** Most companies, small or big, use SAP technologies to work. Many of them provide access to their SAP environments through Citrix. Indeed, supplier or subcontractors need to reach SAP environment, from back office to boardroom, warehouse to storefront, desktop to mobile device; users can quickly and 'securely' access SAP enterprise application software with Citrix virtualization without exposing their SAP landscape to Internet.

To pentest SAP system required some knowledge of this technologies and some hacking tool. Unfortunately, lots of SAP hacking tools are not maintained anymore and dependencies are required like RFC SDK to work. When it comes to assess/pentest the security of SAP landscape from Citrix, no tool is freely available and it is not allow or possible to install third softwares or dependencies.

We present a compilation of powershell script to assess SAP, which try to answer to this problematic of dependencies and use from Citrix environment. The presentation will start by describing the issues around SAP hacking tools, then we will continue by explaining the restrictions meet to pentest from Citrix system. And then we will present in detail the tool developed to solve the issues meet and of course with some demos.

</details>

<details><summary><strong>SERPICO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Peter Arzamendi](https://img.shields.io/badge/Peter%20Arzamendi-informational) ![Will Vandevanter](https://img.shields.io/badge/Will%20Vandevanter-informational)

🔗 **Link:** [SERPICO](#)  
📝 **Description:** SERPICO is a simple and intuitive report generation and collaboration tool; the primary function is to cut down on the amount of time it takes to write a penetration testing report. Serpico was built by penetration testers with a pen-testers methodology in mind. Our goal is to save you time and improve your reporting process.

We are excited to be back at Arsenal!! We have a large release of Serpico planned with some exciting features to show off including plug-ins to simplify your life, more reports to choose from, shiny UI improvements, and better scoring. It might make you hate report writing just a little bit less.

</details>


### Blue Team & Detection

<details><summary><strong>ADVANCED SPECTRUM MONITORING WITH SHINYSDR</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Dominic Spill](https://img.shields.io/badge/Dominic%20Spill-informational) ![Michael Ossmann](https://img.shields.io/badge/Michael%20Ossmann-informational)

🔗 **Link:** [ADVANCED SPECTRUM MONITORING WITH SHINYSDR](#)  
📝 **Description:** ShinySDR is an advanced spectrum monitoring and analysis tool that allows us to monitor wide frequency ranges at high speed, while also drilling down in to interesting signals for real time analysis. These features are supplemented by OSINT data from regulatory bodies around the world. This is the tool that we are releasing as part of our "What's on the Wireless? Automating RF Signal Identification.”

</details>

<details><summary><strong>AKTAION V2 - OPENSOURCE MACHINE LEARNING AND ACTIVE DEFENSE TOOL</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Joseph Zadeh](https://img.shields.io/badge/Joseph%20Zadeh-informational) ![Rod Soto](https://img.shields.io/badge/Rod%20Soto-informational)

🔗 **Link:** [AKTAION V2 - OPENSOURCE MACHINE LEARNING AND ACTIVE DEFENSE TOOL](#)  
📝 **Description:** Aktaion is a machine learning open source & active defense (orchestration) tool. It is on its first iteration. The tool focuses on the detection of ransomware based on machine learning techniques, independent of static-based signatures. The tool has been mentioned and featured in may respected community publications and research. On AKTAION v2 we decided to expand our approach utilizing the blending of multiple signals which we call micro behaviors to expand tool detection into PHISHING URI/URL attack delivery.

</details>

<details><summary><strong>ASSIMILATOR</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Nicolas Videla](https://img.shields.io/badge/Nicolas%20Videla-informational)

🔗 **Link:** [ASSIMILATOR](#)  
📝 **Description:** Network Firewall configuration is difficult to automatize, vendor Firewalls have their own ways to configure Firewalls. Assimilator wraps all vendor Firewalls into one JSON REST api; from here we can easily automatize ( i.e: Python with Requests) policy configuration and route/rule lookup.

</details>

<details><summary><strong>AUTOMATED COLLECTION AND ENRICHMENT PLATFORM</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Jared Atkinson](https://img.shields.io/badge/Jared%20Atkinson-informational) ![Robert Winchester](https://img.shields.io/badge/Robert%20Winchester-informational)

🔗 **Link:** [AUTOMATED COLLECTION AND ENRICHMENT PLATFORM](#)  
📝 **Description:** Many expensive Endpoint Detection and Response (EDR) tools are available, but the high cost and effort required to deploy agents to every host can be offputting to companies. The Automated Collection and Enrichment (ACE) Platform is an open source solution that enables agentless threat hunting in an environment (SIEM not included). This tool makes it possible for anyone to begin gathering otherwise difficult to collect host data to hunt for threats in their environment.

As consultants performing Compromise Assessments, we rarely have the authority or ability to alter a customer's environment to support assessment operations. Actions like enabling Windows Remote Management (WinRM) can require levels of bureaucracy and take months to accomplish. It is also difficult to answer questions surrounding systems running OSX and Linux. By removing a few of our assumptions, we created ACE, an ASP.NET Web Application that not only allows the scanning of Windows, Linux, and MacOS machines, but also provides scan management with features like Scheduling, Credential Management, and File Downloading.

In addition to running scripts and collecting scan data, ACE provides a robust enrichment and ingestion pipeline. Users can easily create individual enrichments in ACE to integrate their favorite data sources, such as hash lookups, IP reputation, sandboxing. The enrichment details can be integrated with original results to create the finalized data types in one object. With a final enrichment, the robust data set can be sent directly to a waiting SIEM for analysis. ACE provides an easy and customizable solution for threat hunters to gather and enrich data before it ever reaches the SIEM, enabling more advanced analysis.

</details>

<details><summary><strong>CHKROOTKIT: EATING APTS FOR BREAKFAST SINCE 1997</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Nelson Murilo Rufino](https://img.shields.io/badge/Nelson%20Murilo%20Rufino-informational)

🔗 **Link:** [CHKROOTKIT: EATING APTS FOR BREAKFAST SINCE 1997](#)  
📝 **Description:** Chkrootkit is a suite of posix shell script and some tools written in ansi C. It works like a charm in virtually all Unix environment without extra dependencies. It is able to detect sereval rootkits, malicios activity (some APTs included) and can do post-mortem forensics analysis to detect malicious kernel modules activities and stuff like that. This tool currentlly detects ~70 known Rootkits, Worms and many malicious activities.

</details>

<details><summary><strong>CUCKOODROID</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Idan Revivo](https://img.shields.io/badge/Idan%20Revivo-informational)

🔗 **Link:** [CUCKOODROID](#)  
📝 **Description:** To combat the growing problem of Android malware, I present Cuckoodroid - a solution based on the popular open source framework Cuckoo Sandbox to automate the malware investigation process. Cuckoodroid enables the use of Cuckoo's features to analyze Android malware and provides new functionality for dynamic and static analysis. Cuckoodroid is an all-in-one solution for malware analysis on Android. It is extensible and modular, allowing the use of new - as well as existing - tools for custom analysis.

The main capabilities of our Cuckoodroid include:

Dynamic Analysis - based on Dalvik API hooking
Static Analysis - Integration with Androguard
Emulator Detection Prevention
Traffic Analysis
Behavioral Signatures in Cuckoodroid
Android Emulator, Android x86 support
Automatic unpacking
Malware Configuration Extractions
Thread View

Examples of well-known malware will be used to demonstrate the framework capabilities and its usefulness in malware analysis.

</details>

<details><summary><strong>EGRESSION</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Daniel Miessler](https://img.shields.io/badge/Daniel%20Miessler-informational)

🔗 **Link:** [EGRESSION](#)  
📝 **Description:** Egression is an enterprise traffic egress control testing and ranking system. It is a command-line tool that checks an organization's ability to restrict outbound uploads of sensitive data (a file containing fake CC numbers, SSNs, National ID numbers, addresses, names, and other PII) using increasingly difficult levels (which use increasingly evasive techniques), and then provides the rating for the given organization based on how difficult it was to egress the data from the network.

</details>

<details><summary><strong>GIBBER SENSE</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Ajit Hatti](https://img.shields.io/badge/Ajit%20Hatti-informational)

🔗 **Link:** [GIBBER SENSE](#)  
📝 **Description:** Found a Gibberish string or file in the wild and don't know what is it? Throw it to GibberSense - it might start to make some sense. GibberSense is a python-based tool and extension to LAMMA as a BCAF (Basic Crypt Analysis Framework) module.

The best use of Gibber Sense is to verify the robustness of encryption libraries if they are free from any backdoors or flaws. Itt can also be used to guess the type of encryption, hashing schemes, and type of encrypted session cookies. If you trying to develop your own secrete encryption scheme, try and see what GibberSense has to say about it.

</details>

<details><summary><strong>HASHVIEW</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Casey Cammilleri](https://img.shields.io/badge/Casey%20Cammilleri-informational) ![Hans Lakhan](https://img.shields.io/badge/Hans%20Lakhan-informational)

🔗 **Link:** [HASHVIEW](#)  
📝 **Description:** Hashview is a web front-end to hashcat with many powerful features geared towards penetration testers. Leverage task automation and real-time analytics for increased results and fancy reports.

Hashview includes the following features:

Automate workflow methodologies
Create custom password cracking tasks
Use data from previous jobs to increase cracking speeds
Fancy analytics useful for client reports
Distributed cracking
Email/SMS Notifications
Retroactively crack hashes from previous jobs
Advanced searching of hashes, usernames, and plains
Smart wordlists
Optional community integration for accelerated cracking

</details>

<details><summary><strong>LIMACHARLIE</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Maxime Lamothe-Brassard](https://img.shields.io/badge/Maxime%20Lamothe-Brassard-informational)

🔗 **Link:** [LIMACHARLIE](#)  
📝 **Description:** LimaCharlie is a cross-platform, open-source, endpoint monitoring, detection and response stack. The open source agent can be deployed to macOS, windows and Linux, reporting flight-recorder type information. The backend provides an easy and scalable framework to build automated detections and responses. Those automations have realtime access to the model stores in the backend as well as the sensors. Finally, a web ui provides visibility in the events from the sensor and their relationships. Output to systems like Splunk and Slack is also supported.

</details>

<details><summary><strong>NODDOS - STOP DDOS ATTACKS AT THE SOURCE</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Steven Hessing](https://img.shields.io/badge/Steven%20Hessing-informational)

🔗 **Link:** [NODDOS - STOP DDOS ATTACKS AT THE SOURCE](#)  
📝 **Description:** What if we could stop DDOS attacks before they even make it to the Internet? Noddos can block DDOS traffic in the gateway, router or firewall connecting the home- or enterprise network to the Internet. That's the truly scalable way to stop the botnets. Noddos enables that with open source client software, a big-data platform in the cloud and building a community that can sustain identifying botnets and defining the ACLs that can restrict their traffic flows.

</details>

<details><summary><strong>OBJECTIVE-SEE'S MACOS SECURITY TOOLS - ARSENAL THEATER DEMO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Patrick Wardle](https://img.shields.io/badge/Patrick%20Wardle-informational)

🔗 **Link:** [OBJECTIVE-SEE'S MACOS SECURITY TOOLS - ARSENAL THEATER DEMO](#)  
📝 **Description:** Patrick drank the Apple juice; to say he loves his Mac is an understatement. However, he is bothered by the increasing prevalence of macOS malware and how both Apple & 3rd-party security tools can be easily bypassed. Instead of just complaining about this fact, he decided to do something about it. To help secure his personal computer, he's written various macOS security tools that he now shares online (always free!), via objective-see.com.

So come watch as OverSight detects malware that spies on users (via the webcam/mic, Ransomwhere?), generically detects macOS ransomware, and a new open-source macOS firewall is released! Our Macs will remain secure!

</details>

<details><summary><strong>SITCH: DISTRIBUTED, COORDINATED GSM COUNTER-SURVEILLANCE - ARSENAL THEATER DEMO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Ash Wilson](https://img.shields.io/badge/Ash%20Wilson-informational)

🔗 **Link:** [SITCH: DISTRIBUTED, COORDINATED GSM COUNTER-SURVEILLANCE - ARSENAL THEATER DEMO](#)  
📝 **Description:** SITCH uses inexpensive hardware and open-source software to create a network of sensors for detecting malicious activity in GSM wireless networks.

SITCH sensors are based on the Raspberry Pi 3 platform and use inexpensive, easy-to-source software-defined, GPS, and GSM radios. One person can manage a large number of SITCH sensors, including on-the-fly configuration and firmware updates, from a web browser.

</details>

<details><summary><strong>SWEET SECURITY</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Travis Smith](https://img.shields.io/badge/Travis%20Smith-informational)

🔗 **Link:** [SWEET SECURITY](#)  
📝 **Description:** Sweet Security is a network security monitoring and defensive tool which can be deployed on hardware as small as a Raspberry Pi. Using the power of Bro IDS and threat intelligence feeds, malicious network traffic can be exposed. This data is gathered and visualized with the ELK stack (Elasticsearch, Logstash, and Kiban). Going beyond detection, the device can implement blocking for specific devices on a granular level. Sweet Security can monitor all network traffic with no infrastructure change and block unwanted traffic. It ships with Kibana dashboards, as well as a new web administration UI. Even better, the installation can be separated between web administration and sensor. Want to deploy the web administration to AWS and install a dozen sensors? No problem!

All of these tools and methodologies run on inexpensive hardware, such as the Raspberry Pi. If you're looking for a more scalable solution, these tactics and tools can be adapted to enterprise scale deployments, as well. Attendees can expect to take away methodologies they can put to use right away, from dorm-room to datacenter.

</details>

<details><summary><strong>WEB SIGHT - ENTERPRISE ATTACK SURFACE CARTOGRAPHY</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Christopher Grayson](https://img.shields.io/badge/Christopher%20Grayson-informational)

🔗 **Link:** [WEB SIGHT - ENTERPRISE ATTACK SURFACE CARTOGRAPHY](#)  
📝 **Description:** Web Sight is a platform that automates the process of enumerating enterprise attack surface at scale. Starting with IP addresses, domain names, and networks, Web Sight can quickly enumerate subdomains, collect DNS records, run network scans, analyze SSL/TLS certificates and protocol support, and perform network service fingerprinting and application-layer inspection. The end goal of this information gathering process is to provide users with the situational awareness required to successfully attack and/or defend target organizations.

</details>


### Reverse Engineering

<details><summary><strong>BINGREP</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Hiroki Hada](https://img.shields.io/badge/Hiroki%20Hada-informational)

🔗 **Link:** [BINGREP](#)  
📝 **Description:** We created a new tool for static malware analysis. Incident response is important and analysts must analyze malware promptly, but the cost of static analysis is too expensive. For effective analysis we sometimes reuse malware that was analyzed before. "BinDiff" is the most famous tool created by H. Flake that outputs "Diff" of functions between two malware. This outputs good results, but it can output only one result per function. So, we created "BinGrep" that outputs functions in order of similarity by searching resemble malware functions. This "Grep" tool is useful in malware analysis because malware analysts are interested in specific functions.

</details>

<details><summary><strong>CAN-PICK - A VISUALIZATION TOOL FOR EVALUATING CAN-BUS CYBERSECURITY - ARSENAL THEATER DEMO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Bin Guo](https://img.shields.io/badge/Bin%20Guo-informational) ![Jianhao Liu](https://img.shields.io/badge/Jianhao%20Liu-informational) ![Minrui Yan](https://img.shields.io/badge/Minrui%20Yan-informational)

🔗 **Link:** [CAN-PICK - A VISUALIZATION TOOL FOR EVALUATING CAN-BUS CYBERSECURITY - ARSENAL THEATER DEMO](#)  
📝 **Description:** With the development of automotive technology, vehicles become more electronic and intelligent on the basis of inner bus communication network, and they draw more attention to the study of automotive cybersecurity. To facilitate this process, we developed a tool that evaluates the cybersecurity of the CAN-bus, which can be used for black-box tests by security researchers and automotive engineers.

This tool is capable of sniffing CAN-bus packets, analyzing UDS, as well as launching fuzzing attacks, and brute-force attacks. Fuzzing attack has two modes; we can combine id with data or single one to fuzz CAN-bus packet. By visualizing the changes from different packets, it can help us to identify id and value range related with function quickly. And we can easily find out which data is encrypted, so that it’ll more convenient to guess encrypt algorithm. Users can also share their programmable examples within the tool. This talk will introduce the reverse engineering of CAN-bus and present the "CAN-Pick" tool by demonstrations of injecting CAN-bus packets on a car. We will show some videos to prove the results of our work. This tool can also be used as a remote access tool, which can realize full control over the car without adding any actuators on the vehicle in some modern car via Telematics system.

</details>

<details><summary><strong>FLARE VM</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Peter Kacherginsky](https://img.shields.io/badge/Peter%20Kacherginsky-informational)

🔗 **Link:** [FLARE VM](#)  
📝 **Description:** Have you ever needed to rapidly create a Windows VM with all your analysis tools? Do you get annoyed by constantly having to update each and every security tool to the latest version in you VMs? Has your VM been not updated or patched for years on end? If you answered yes to any of these questions, then you NEED the FLARE VM.

FLARE VM is the first of its kind freely available and open sourced Windows-based security distribution designed for reverse engineers, malware analysts, incident responders, forensicators, and penetration testers. Inspired by open-source Linux-based security distributions like Kali Linux, FLARE VM delivers a fully configured platform with a comprehensive collection of Windows security tools such as debuggers, disassemblers, decompilers, static and dynamic analysis utilities, network analysis and manipulation, web assessment, exploitation, vulnerability assessment applications, and many others.
FLARE VM comes in two flavors – Malware Analysis and Penetration Testing editions. Each edition targets a specific task. For example, FLARE VM - Malware Analysis Edition is optimized for and contains tools specifically for reverse engineering malware. The tools included with FLARE VM distribution were either developed or carefully selected by the members of the FLARE (FireEye Labs Advanced Reverse Engineering) Team who have been reverse engineering malware, analyzing exploits and vulnerabilities, and teaching malware analysis classes for over a decade.

The security distribution works as an easily deployable package that you can install on an existing Windows installation. FLARE VM brings a familiar, easy to manage package management system to quickly deploy and customize the platform to suite your specific needs. After the initial installation, you can easily add, remove and update packages in the FLARE VM package repository.

During the session attendees will be familiarized with different tools, plug-ins and scripts offered on the FLARE VM to do the following:

How to go from a basic Windows installation to a fully deployed FLARE VM ready to analyze malware and conduct security assessments in 30 minutes or less.
Perform basic static analysis of a real malware sample to gather basic indicators.
Run the malware sample in a safe manner in order to manually gather dynamic indicators by simulating a complete network environment and carefully observing malware behavior with a variety of tools and techniques.
Deep dive into malware inner workings by using a number of disassemblers and decompilers available on the system.
Advanced dynamic analysis and generic unpacking techniques using debuggers, various plugins, and other tools that come with the distribution.
Learn how to customize the VM, create new packages and your own custom editions using the FLARE VM package repository.

Bring a Windows 7+ Virtual Machine to easily participate in the hands-on section of the demo.

</details>


### Web/AppSec

<details><summary><strong>BURPSMARTBUSTER: A SMART WAY TO FIND HIDDEN TREASURES</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Patrick Mathieu](https://img.shields.io/badge/Patrick%20Mathieu-informational)

🔗 **Link:** [BURPSMARTBUSTER: A SMART WAY TO FIND HIDDEN TREASURES](#)  
📝 **Description:** This tool is the anticipated replacement of a better dirb/gobuster/DirBuster. Bruteforcing non-indexed data is often used to discover hidden files and directories which can lead to information disclosures, or even to system compromise when a backup file is found. This bruteforcing technique is still useful today, but the tools are lacking the application context and do not use any smart behaviour to reduce the bruteforce scanning time. BurpSmartBuster, a Burp Suite Plugin, offers to use the application context and add the smart into the Buster!

This demo will reveal this open-source plugin with its new features and show a practical case of how you can use this new tool to accelerate your Web pentesting to find hidden treasures! The following will be covered:

How to add context to a web bruteforce tool
How we can be stealthier
How smart context-based data can be used to find hidden files and directories
How simple the code is and how you can help to make it even better!

Introducing these new features:

Scan items based on the technologies of the webapp and web server (Basic ex: PHP files should not be scan on an ASPX application OR if SharePoint is in use scans its webservices).
This includes the new technology scanner class and results which are scanned
If time permits, Community data: Each time an items is find, the data is sent anonymously to a server compiling trend of hidden items found in the wild and will share the information to all
Multiple small fixes and improvements

</details>

<details><summary><strong>CSP AUDITOR</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Philippe Arteau](https://img.shields.io/badge/Philippe%20Arteau-informational)

🔗 **Link:** [CSP AUDITOR](#)  
📝 **Description:** CSP Auditor is a Burp and ZAP extension that helps build or improve the Content-Security-Policy header configurations. CSP can provide a solid defense against XSS. However, it is easy to add a directive by mistake that will make the policy completely ineffective against specially-crafted XSS. This plugin provided a readable view of CSP headers in the response tab. It will highlight the weakest configurations. It also includes passive scan rules to be notified of weak configurations. The most recent feature is the automatic generation of CSP configuration based on the resources intercepted.

</details>

<details><summary><strong>EASILY EXPLOIT TIMING ATTACKS IN WEB APPLICATIONS WITH THE 'TIMING_ATTACK' GEM</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Forrest Fleming](https://img.shields.io/badge/Forrest%20Fleming-informational)

🔗 **Link:** [EASILY EXPLOIT TIMING ATTACKS IN WEB APPLICATIONS WITH THE 'TIMING_ATTACK' GEM](#)  
📝 **Description:** The timing_attack gem is a simple application to exploit timing attacks in web applications. It focuses on ease-of-use over extreme resolution; its primary use is in exploiting known timing vulnerabilities in web applications.

</details>

<details><summary><strong>FTW: FRAMEWORK FOR TESTING WAFS</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Chaim Sanders](https://img.shields.io/badge/Chaim%20Sanders-informational) ![Zack Allen](https://img.shields.io/badge/Zack%20Allen-informational)

🔗 **Link:** [FTW: FRAMEWORK FOR TESTING WAFS](#)  
📝 **Description:** FTW is designed to be a comprehensive test suite to help provide rigorous tests for WAF rules. It uses the OWASP Core Ruleset V3 as a baseline to test rules on for various WAFs. It is designed to:

Find regressions in WAF deployments by using continuous integration and issuing repeatable attacks against a WAF
Provide a testing framework for new rules into the Core Rule Set, if a rule is submitted it MUST have corresponding positive & negative tests
Evaluate WAFs against a common, agreeable baseline ruleset (OWASP)
Test and verify custom rules for WAFs that are not leveraging the core rule set

</details>

<details><summary><strong>FUZZAPI - FUZZING YOUR RESTAPIS SINCE YESTERDAY</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Abhijeth Dugginapeddi](https://img.shields.io/badge/Abhijeth%20Dugginapeddi-informational) ![Lalith Rallabhandi](https://img.shields.io/badge/Lalith%20Rallabhandi-informational) ![Srinivas Rao](https://img.shields.io/badge/Srinivas%20Rao-informational)

🔗 **Link:** [FUZZAPI - FUZZING YOUR RESTAPIS SINCE YESTERDAY](#)  
📝 **Description:** After seeing the benefits of Automating REST API pen testing using a basic Fuzzapi tool, the authors have decided to come up with a better version which can automatically look into vulnerabilities in APIs from the time they are written. REST APIs are often one of the main sources of vulnerabilities in most web/mobile applications. Developers quite commonly make mistakes in defining permissions on various cross-platform APIs. This gives a chance for the attackers to abuse these APIs for vulnerabilities. Fuzzapi is a tool written in Ruby on Rails which helps to quickly identify such commonly found vulnerabilities in APIs which helps developers to fix them earlier in SDLC life cycle. The first released version of the tool only has limited functionalities however, the authors are currently working on releasing the next version which will completely automate the process which saves a lot of time and resources.

</details>

<details><summary><strong>HUNT: THE BUG HUNTER'S BURP EXTENSION</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Fatih Egbatan](https://img.shields.io/badge/Fatih%20Egbatan-informational) ![JP Villanueva](https://img.shields.io/badge/JP%20Villanueva-informational) ![Jason Haddix](https://img.shields.io/badge/Jason%20Haddix-informational) ![Ryan Black](https://img.shields.io/badge/Ryan%20Black-informational) ![Vishal Shah](https://img.shields.io/badge/Vishal%20Shah-informational)

🔗 **Link:** [HUNT: THE BUG HUNTER'S BURP EXTENSION](#)  
📝 **Description:** What if you could super-charge your bug hunting? Not through automation (since it can miss so much) but through powerful alerts created from real threat intelligence? What if you had a Burp plugin that did this for you? What if that plugin not only told you where to look for vulns but also gave you curated resources for additional exploitation and methodology? Well, now you do! HUNT is a new Burp Suite extension that aims to arm bug hunters and web testers with parameter level suggestions on where to look for certain classes of vulnerabilities (SQLi, CMDi, LFI/RFI, and more!).

</details>

<details><summary><strong>OFFENSIVE WEB TESTING FRAMEWORK (OWASP OWTF)</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Viyat Bhalodia](https://img.shields.io/badge/Viyat%20Bhalodia-informational)

🔗 **Link:** [OFFENSIVE WEB TESTING FRAMEWORK (OWASP OWTF)](#)  
📝 **Description:** OWASP OWTF is a project focused on penetration testing efficiency and alignment of security tests to security standards like the OWASP Testing Guide (v3 and v4), the OWASP Top 10, PTES and NIST so that pentesters will have more time to:

See the big picture and think out of the box
More efficiently find, verify and combine vulnerabilities
Have time to investigate complex vulnerabilities like business logic/architectural flaws, etc.
Perform more tactical/targeted fuzzing on seemingly risky areas
Demonstrate true impact despite the short timeframes we are typically given to test

The tool is highly configurable and anybody can trivially create simple plugins or add new tests in the configuration files without having any development experience. OWTF includes

A highly configurable plugin system
A fast (the fastest Python MiTM proxy yet!) MiTM SSL proxy
A pretty web interface
An interactive report
Full coverage for OWASP Testing Guide v3/v4, PTES, NIST, and CWE mappings
Built-in integrations for Mozilla Zest and Plug-n-Hack standards
REST API exposed to control and extend the functionality of OWTF

This release will see new completely revamped web interface, code refactoring, and much easier installation process. OWTF is expected to undergo an extensive change to add features like distributed architecture, proxy transaction modification/replay, plugin chaining, and much more for the new 2.1 release in the summer. The OWTF project, started in 2011, has grown into a community for tools like HTTP request translator, tool health monitor, Pentester's Tools Parser (PTP), and WafBypasser. OWTF has participated in Google Summer of Code 2013, 2014, and 2016. In addition to this, it was voted as 10th and 7th most popular tool in 2015 and 2014 respectively (Toolswatch Hackers Arsenal).

</details>

<details><summary><strong>PYMULTITOR</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Tomer Zait](https://img.shields.io/badge/Tomer%20Zait-informational)

🔗 **Link:** [PYMULTITOR](#)  
📝 **Description:** Have you ever wanted to be at two different places at the same time? When I asked myself this question, I actually started developing this solution in my mind. While performing penetration tests, there are often problems caused by security devices that block the "attacking" IP. This really annoyed me, so I wrote a script to supply a solution for this problem. With a large number of IP addresses performing the attacks, better results are guaranteed - especially when attempting attacks to bypass Web Application Firewalls, Brute-Force type attacks and many more. URLs: [Github] https://github.com/realgam3/pymultitor; [OwaspIL Old Presentation] https://www.owasp.org/images/3/3d/OWASPIL-2016-02-02_PyMultiTor_TomerZait.pdf; https://www.blackhat.com/asia-17/arsenal.html#pymultitor

</details>

<details><summary><strong>THREADFIX WEB APPLICATION ATTACK SURFACE CALCULATION</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Dan Cornell](https://img.shields.io/badge/Dan%20Cornell-informational)

🔗 **Link:** [THREADFIX WEB APPLICATION ATTACK SURFACE CALCULATION](#)  
📝 **Description:** The ThreadFix web application attack surface calculation utilities allow users to:

Calculate a web application's attack source based on application source code (available URLs and parameters)
Visually inspect web application attack surface to target manual penetration testing activities
Pre-seed dynamic application security testing tools like OWASP ZAP and Burpsuite
Calculate changes to application attack surface over time and across git commits
Run targeted DAST scans based on new attack surface and attack surface that has changed since previous tests were run

</details>

<details><summary><strong>WATOBO - THE WEB APPLICATION TOOLBOX</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Andreas Schmidt](https://img.shields.io/badge/Andreas%20Schmidt-informational)

🔗 **Link:** [WATOBO - THE WEB APPLICATION TOOLBOX](#)  
📝 **Description:** WATOBO is a security tool for testing web applications. It is intended to enable security professionals to perform efficient (semi-automated) web application security audits.

Most important features are:

Powerful session management capabilities! You can define login scripts as well as logout signatures. So you don't have to login manually each time you get logged out.
Can act as a transparent proxy (requires nfqueue)
Vulnerability checks (SQLinjectin, XSS, LFI) out of the box
Handles Anti-CSRF-/One-Time-Tokens
Supports inline de-/encoding, so you don't have to copy strings to a transcoder and back again. Just do it inside the request/response window with a simple mouse click.
Smart filter functions, so you can find and navigate to the most interesting parts of the application easily.
Is written in (FX) Ruby and enables you to easily define your own checks
Runs on Windows, Linux, MacOS every OS supporting (FX) Ruby

</details>

<details><summary><strong>WSSIP: A WEBSOCKET MANIPULATION PROXY</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Samantha Chalker](https://img.shields.io/badge/Samantha%20Chalker-informational)

🔗 **Link:** [WSSIP: A WEBSOCKET MANIPULATION PROXY](#)  
📝 **Description:** WSSiP is a tool for viewing, interacting with, and manipulating WebSocket messages between a browser and web server, with an outward bridge for debugging and fuzzing all WebSocket communications.

</details>


### OSINT

<details><summary><strong>DATASPLOIT - AUTOMATED OPEN SOURCE INTELLIGENCE (OSINT) TOOL</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Kunal Agrawal](https://img.shields.io/badge/Kunal%20Agrawal-informational) ![Shubham Mittal](https://img.shields.io/badge/Shubham%20Mittal-informational) ![Sudhanshu Chauhan](https://img.shields.io/badge/Sudhanshu%20Chauhan-informational)

🔗 **Link:** [DATASPLOIT - AUTOMATED OPEN SOURCE INTELLIGENCE (OSINT) TOOL](#)  
📝 **Description:** Utilizing various Open Source Intelligence (OSINT) tools and techniques that we have found to be effective, DataSploit brings them all into one place, correlates the raw data captured and gives the user, all the relevant information about the domain/email/ phone number/person, etc. It allows you to collect relevant information about a target which can expand your attack/defense surface very quickly. Sometimes it might even pluck the low hanging fruits for you without even touching the target and give you quick wins.

New release also includes ACTIVE modules which allow to use information collected from OSINT and use it for active exploitation either directly or by integrating with other Social Engineering / Pen-testing tools.

</details>

<details><summary><strong>DESENMASCARA.ME</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Emilio Casbas](https://img.shields.io/badge/Emilio%20Casbas-informational) ![Félix Brezo Fernández](https://img.shields.io/badge/Félix%20Brezo%20Fernández-informational) ![Yaiza Rubio Viñuela](https://img.shields.io/badge/Yaiza%20Rubio%20Viñuela-informational)

🔗 **Link:** [DESENMASCARA.ME](#)  
📝 **Description:** DESENMASCARA.ME IS A Super simple web service to analyze websites. In this edition, an open source feed of "Fake websites" related with the online counterfeiting fraud will be published. The tool was integrated with VirusTotal, and a SANS research paper about the new feature to detect "Online counterfeiters" has been recently published: https://www.sans.org/reading-room/whitepapers/detection/tracking-online-counterfeiters-37697.

</details>

<details><summary><strong>DRADIS: 10 YEARS HELPING SECURITY TEAMS SPEND MORE TIME TESTING AND LESS TIME REPORTING</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

🔗 **Link:** [DRADIS: 10 YEARS HELPING SECURITY TEAMS SPEND MORE TIME TESTING AND LESS TIME REPORTING](#)  
📝 **Description:** Dradis is an extensible, cross-platform, open source collaboration framework for InfoSec teams. It can import from over 19 popular tools, including Nessus, Qualys, Burp and AppScan. Started in 2007 (this is the 10th year anniversary!), Dradis Framework has been growing ever since (10,000+ in the last 12 months). Dradis is the best tool to combine the output of different scanners, add your manual findings and evidence and generate a report with one click.

Come to see the latest Dradis release in action. It's loaded with updates including new tool connectors, a Burp extension to send your findings into Dradis directly, combining of multiple issues, additional REST API coverage, and a leaner, faster interface. Find out why Dradis is being downloaded over 400 times every week and is loved by students preparing different certifications. Be sure to check it out before we run out of the exclusive 10th anniversary stickers!

</details>

<details><summary><strong>OSRFRAMEWORK: OPEN SOURCES RESEARCH FRAMEWORK</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Félix Brezo Fernández](https://img.shields.io/badge/Félix%20Brezo%20Fernández-informational) ![Yaiza Rubio Viñuela](https://img.shields.io/badge/Yaiza%20Rubio%20Viñuela-informational)

🔗 **Link:** [OSRFRAMEWORK: OPEN SOURCES RESEARCH FRAMEWORK](#)  
📝 **Description:** OSRFramework is a GNU AGPLv3+ set of libraries modularly developed by Yaiza Rubio and Félix Brezo to perform Open Source Intelligence tasks. In the framework, the authors include a series of applications related to username checking, DNS lookups, social media research, regular expressions extraction and many others. At the same time, by means of ad-hoc Maltego transforms, OSRFramework provides a way of making these queries graphically as well as including other interfaces to interact with it using the command line and a web server.

The most important tools included in the framework are:

usufy.py. Application focused on checking the existence of different usernames in up to 309 platforms (as May 4th, 2017).
domainfy.py. Application focused on finding existing domains and common subdomains that currently resolve to IP addresses (more than 1500 possible domains checked). Whois information is retrieved when possible.
mailfy.py. Application that validates the existence or not of an email account in more than 20 different email providers.
Other tools included are: alias_generator.py, phonefy.py and searchfy.py as well as osrfconsole.py (msfconsole-like command line GUI), osrframework_server.py (a Web interface that includes an API) and several local Maltego transforms and entities.
Amongst the capabilities included, it is possible to export to several formats (.csv, .xls, .xlsx, .gml, etc.), to configure the number of threads and proxy settings and to define the credentials to be used if the forum enforces it.

As each security analyst may be facing different information needs, the tool has been conceived to be easily configurable so as to include new local sources. By means of plugins that analysts can add locally using the templates provided by the authors, security researchers will be able to adapt the tool to his/her own specific needs at any time.

</details>

<details><summary><strong>PROJECT SPLINTER - MAKE INFORMED DECISIONS BASED ON CYBER THREAT INTEL</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Nicolas Kseib](https://img.shields.io/badge/Nicolas%20Kseib-informational) ![Shimon Modi](https://img.shields.io/badge/Shimon%20Modi-informational)

🔗 **Link:** [PROJECT SPLINTER - MAKE INFORMED DECISIONS BASED ON CYBER THREAT INTEL](#)  
📝 **Description:** Indicators of Compromise (IoCs) form a core component of a security analyst's decision making process, but there is very little emphasis paid to recognizing their dynamic nature in the overall analysis. Adversaries are dynamic entities that adapt to their environment and change their tactics and techniques with time. Our goal is to bring a scientific approach to cyber threat analysis by utilizing Bayesian inference to reduce uncertainty in decision making. We will present a tool that calculates statistical probabilities for assigning classification labels to campaign or malware families based on observed IoC's. This tool also allows analysts to take into account temporal quantity of the observations to strengthen this statistical inference. To demonstrate the capabilities of the tool we will use the Fidelis Barncat Threat Intelligence dataset. The Barncat dataset represents an acceptable ground truth for the past state of the world, which can be used to informed new observations. We will show how the tool allows to backtest classification models using this dataset and propose security centric decision metrics for identifying the most optimal model.

</details>


### Social Engineering / General

<details><summary><strong>ISTHISLEGIT</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Social Engineering / General](https://img.shields.io/badge/Category:%20Social%20Engineering%20/%20General-pink) ![Jordan Wright](https://img.shields.io/badge/Jordan%20Wright-informational) ![Mikhail Davidov](https://img.shields.io/badge/Mikhail%20Davidov-informational)

🔗 **Link:** [ISTHISLEGIT](#)  
📝 **Description:** When it comes to mitigating phishing, visibility is half the battle. Knowing what phishing attacks are hitting your organization is key to stopping them. Users can be an incredible source of alerting for phishing emails, but they often don't know where to report the emails. Also, having the ability to collect, correlate, and auto-respond to these reports is key to stopping attacks as quickly they come in. These are problems solved by IsThisLegit for free via open-source, unlike any somewhat similar but cost-prohibitive offerings out there.

IsThisLegit is a Chrome extension and web application dashboard (leveraging Google App Engine) designed to support the management of phishing response for end-users and admins. By rolling out the Chrome extension, users will see a button in Gmail that allows them to easily report phishing emails to their security team with a single click. Now there's no need for users to remember which email address they need to send reports to. The email is then automatically reported and deleted from their inbox.

Once submitted, admins can then use the dashboard to rapidly analyze reported emails, identify phishing trends, categorize phishing emails, and set up auto-response rules.This allows the security team to quickly identify and respond to ongoing attacks.

This demo will be unique for Arsenal because it covers the full lifecycle of phishing mitigation with the 'holy trinity' of tools (all developed by the Duo Labs team). These three distinct open-source tools work together seamlessly to test and train users (Gophish), help protect/take the burden off of users by making it more difficult for attackers (Phinn), and make reporting incidents as easy as a click of the button (IsThisLegit).



https://github.com/duo-labs/isthislegit

</details>


### Red Teaming / Embedded

<details><summary><strong>PTIOT: AN AUTOMATED SECURITY TESTING FRAMEWORK FOR THE INTERNET OF THINGS - ARSENAL THEATER DEMO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Jie Li](https://img.shields.io/badge/Jie%20Li-informational) ![Kaixiang Zhang](https://img.shields.io/badge/Kaixiang%20Zhang-informational) ![Mei Wang](https://img.shields.io/badge/Mei%20Wang-informational) ![Yangdong Wang](https://img.shields.io/badge/Yangdong%20Wang-informational) ![Yihan Lian](https://img.shields.io/badge/Yihan%20Lian-informational)

🔗 **Link:** [PTIOT: AN AUTOMATED SECURITY TESTING FRAMEWORK FOR THE INTERNET OF THINGS - ARSENAL THEATER DEMO](#)  
📝 **Description:** With the Internet of Everything era coming and millions of IoT devices becoming interconnected via the Internet, security issues caused by the IoT devices are increasingly serious more than any time before. Different from traditional security problems, there are no specific cognitions or orientations on the technology of security defense. Only if we knew our evil enemy and understood the means they used to attack, would we be able to build an efficient defense system.

PtIoT is an automated security testing framework for the Internet of Things, and it has already been used on 360 IoT devices' productive process. It is combined with 360GearTeam's daily security practice and understanding of the attack pattern the malicious frequently used. It contains grey box-based security tests on external ports, compilation options, communication encryption, OS check runtime program check, web application check, etc. It is used to test ROMs on the products' version iteration process. At present, the security test covers products like 360 Smart Camera, 360Safe Wifi Router, 360 Driver Recoder and so on.

</details>

<details><summary><strong>UNIVERSAL RADIO HACKER: INVESTIGATE WIRELESS PROTOCOLS LIKE A BOSS - ARSENAL THEATER DEMO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Johannes Pohl](https://img.shields.io/badge/Johannes%20Pohl-informational)

🔗 **Link:** [UNIVERSAL RADIO HACKER: INVESTIGATE WIRELESS PROTOCOLS LIKE A BOSS - ARSENAL THEATER DEMO](#)  
📝 **Description:** The spectrum of IoT products expands and with it the number of proprietary wireless protocols raises. Such protocols are designed under size and energy constraints so they tend to have a secondary focus on security. Security researchers can examine arbitrary IoT protocols with Software Defined Radios (SDR) but SDRs present the possibly encoded data in a complex IQ format. Therefore, data has to be to demodulated and decoded before researchers can investigate the actual protocol. After revealing the protocol logic with a differential analysis, vulnerabilities can be found e.g. using fuzzing. Present tools require expertise in Digital Signal Processing (DSP) and/or cover only parts of the process e.g. they only offer support for demodulation but do not help to analyze the protocol logic so researchers need to combine various tools and self-made scripts.

We address this problem with the Universal Radio Hacker (URH) - an open source, cross platform application that integrates the complete hacking process. First, URH performs demodulation with minimal user interaction so no deep DSP knowledge is required. Second, URH helps to reverse engineer the protocol logic by organizing with fields and message types. This can either be done manually or automatically by URH to boostrap a protocol. Third, URH includes a fuzzing component for logical protocol fields whereby the selected encoding and modulation is automatically applied to the crafted messages. URH aims to be both self-contained and expandable: Users find all required steps bundled into one application but at the same time URH provides several interfaces for external tools like GNU Radio so also DSP experts can benefit from it.

The source code of URH can be found at GitHub under https://github.com/jopohl/urh.

</details>

<details><summary><strong>VT AUTO-X VEHICLE AUTOMATED SECURITY TESTING TOOL - ARSENAL THEATER DEMO</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Wayne Yen](https://img.shields.io/badge/Wayne%20Yen-informational)

🔗 **Link:** [VT AUTO-X VEHICLE AUTOMATED SECURITY TESTING TOOL - ARSENAL THEATER DEMO](#)  
📝 **Description:** Currently, there are some research works on vehicle cybersecurity testing. Many of them are open-source projects, such as CANTact and GoodThopter. CANTact is a popular open-source toolkit available for purchase online that uses SocketCAN to communicate with a CAN bus. Since SocketCAN extends the Berkeley sockets API in Linux by introducing a new protocol family, it is easy to write script languages for CAN message injections. Python is one of the most widely-used script languages for SocketCAN programming. GoodThopter is another recent device targeted at hackers and hobbyists, but is not ready for use as a turn-key solution.

The drawbacks of these open-source tools are that they are not stable and do not work well under heavy-traffic testing scenarios. Also, open-source contributions may not meet the rigorous control and validation requirements of auto industry software practices. We found that it was possible to crash or lock up such tools when injecting them with bursty CAN traffic. For example, CANTact has limited buffer size which may cause buffer overflows. GoodThopter's timeout parameters and configuration file make it hard to work. In our case, we used the serial port for communications and Java as the programming language. Java is preferred over Python as it is faster, more stable, requires strict coding rules, and is better suited to remote control applications.

Cybersecurity testing focuses on finding and identifying unwanted weaknesses or vulnerabilities hiding inside vehicle software. Our goal is to develop an automated and black-box testing tool for OEMs and tier providers to test their vehicles or ECUs with consistent results, which requires no prior detailed knowledge of the testing workflow.

Automation means the tester only needs to follow pre-defined test scenarios one-by-one to finish the whole testing process. Even if the tester does not have prior security testing knowledge or background, he or she can still operate the test device and detect security vulnerabilities by following the automated steps.

Black-box testing strategies should have no prior knowledge of system commands, CAN bus command databases, or the specific manufacturer's practices within the vehicle or system under testing protocols. In this way, OEMs may feel more comfortable with black-box testing since they don't need to release too much of what they may consider to be proprietary system information to internal, outside, or third-party testers.

We have developed the automated automotive cybersecurity testing tool (named VT Auto-X) which has successfully detected serious security vulnerabilities in a number of production vehicles, and has helped several OEMs identify and correct these issues before they became expensive and embarrassing recall programs. It is a black-box test with no prior knowledge of vehicle CAN bus information. Live demonstrations of Auto-X have proven its ability to quickly find software and security vulnerabilities in most of the cars tested.

Auto-X is portable, and can easily connect to a vehicle's CAN bus. The device has a panel which has various types of connection interfaces, including OBD (SAE J1979/J1962) ports and multiple CAN High and CAN Low ports. It incorporates standard banana sockets to facilitate connecting to various vehicle CAN bus accessible points, as well as several power supply options for testing flexibility (bench, garage, mobile). Other connection arrangements are also possible for use when testing individual systems, ECUs, or bench testing components.

A USB 2.0 port is provided to connect to laptops or other computers. Power can also be provided directly via the OBD II connection, by direct 12V DC connection, or via an AC mains adapter power supply. Auto-X also contains several communication modules, such as WIFI, Bluetooth, and 3G, for both short-range and long-range communications making it easy to communicate with remote cloud or smart mobile phones.

Auto-X performs an automated sequence of test scenarios using either the local or cloud-based testing portal. Each scenario test time can range from minutes to hours, which varies depending on the vehicle configuration and equipment. The tool injects CAN traffic into the vehicle CAN bus. By monitoring and recording CAN traffic and responses, the testing portal then analyzes the logs and responses aiming to detect unexpected, unwanted, or potentially harmful security issues.

Auto-X acts as an interface between the entity being tested (an entire vehicle, a single CAN bus, multiple CAN buses, or a component, such as a specific Electronic Control Unit or ECU) and the secure cloud test portal (where the testing scripts reside). It also connects to the user's laptop to control and monitor activity during testing. Once connected to the vehicle, Auto-X can run a series of test scripts or protocols from the cloud portal.

</details>

<details><summary><strong>"HACKER MODE" FOR AMAZON ALEXA(TM)</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![David Cross](https://img.shields.io/badge/David%20Cross-informational)

🔗 **Link:** ["HACKER MODE" FOR AMAZON ALEXA(TM)](#)  
📝 **Description:** Have you ever been stuck at a command line, not quite remembering the syntax for a NetCat relay? Ever wish that buddy that has a photographic memory for man-pages was with you? Hacker Mode makes Amazon's Alexa(TM) be that epic hacker buddy for you!

The Hacker Mode skill designed for Alexa assists hackers and developers with:

HTML, Hex, URL, ASCII encodings
NetCat, NMap, and Metasploit command line interfaces
Well-known TCP and UDP ports, HTTP headers, HTTP response codes and HTTP verbs

Simply ask Alexa to enter "Hacker Mode" and then ask a question like: "How can I send a file with NetCat?" The app provides both voice feedback and Alexa App feedback to ensure you get the syntax just right.

</details>


### Web/AppSec or Red Teaming

<details><summary><strong>TINTORERA: SOURCE CODE INTELLIGENCE</strong></summary>

![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Simon Roses Femerling](https://img.shields.io/badge/Simon%20Roses%20Femerling-informational)

🔗 **Link:** [TINTORERA: SOURCE CODE INTELLIGENCE](#)  
📝 **Description:** Tintorera is a static analysis tool developed in Python that uses the GCC compiler to build C projects aiming to obtain intelligence from them. GCC offers a powerful plugin architecture that allows tapping into its internals, and static analysis tools can benefit from it to gather information of the source code while compiling.

Some Tintorera features that a code auditor can benefit from:

Obtain many code metrics: Cyclomatic Complexity (CC), comment density, physical lines of codes, design complexity, code averages and etc.
Attack Surface analysis of the entire project, identifies all entry and exit of data.
Can identify Linux API and well-known libraries such as OpenSSL
Perform different visualization maps of the source code such as function structure, logic and function calls relationship
Context and code analysis of: comments, inline assembly, global variables, function parameters and more
The entire source code is converted to a JSON representation allowing performing queries
Creates HTML reports while the project gets compiled by GCC
Extend Tintorera to fit your needs easily using Python
Tap into GCC internals and passes

By using static analysis techniques, Tintorera can gather intelligence of a C source code allowing a code auditor to learn about the project faster. Tintorera is a tactical response as projects grow in complexity and code reviews are usually performed under limited time.

</details>

