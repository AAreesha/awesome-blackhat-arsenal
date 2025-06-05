# Europe 2019
---
## 🧠 Tools by Category
### Red Teaming / AppSec

<details><summary><strong>[ART: Adversarial Robustness 360 Toolbox for Machine Learning Models](https://github.com/lfai/proposing-projects/blob/master/proposals/trusted-ai.adoc)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Irina Nicolae](https://img.shields.io/badge/Irina%20Nicolae-informational) ![Beat Buesser](https://img.shields.io/badge/Beat%20Buesser-informational)

                Adversarial attacks against machine learning systems have become an indisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (so-called poisoning attacks), or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (so-called evasion attacks). These attacks have been demonstrated in a number of different application domains, including malware detection, spam filtering, visual recognition, speech-to-text conversion, and natural language understanding. Devising comprehensive defences against poisoning and evasion attacks by adaptive adversaries is still an open challenge.

We will present the Adversarial Robustness 360 Toolbox (ART), a library which allows rapid crafting and analysis of both attacks and defense methods for machine learning models. ART provides an implementation for many state-of-the-art methods for attacking and defending machine learning. At Black Hat, we will introduce the major version 1.0, which contains new powerful black-box attacks, support for additional machine learning libraries, as well as new defenses and detectors. Through ART, the attendees will (re)discover how to attack and defend diverse machine learning systems.

                </details>
                
<details><summary><strong>[Automatic API Attack Tool](https://github.com/imperva/automatic-api-attack-tool)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Boris Serebro](https://img.shields.io/badge/Boris%20Serebro-informational)

                Imperva's customizable API attack tool takes an API specification as an input, creates and runs attacks which are based on it as an output.

After researching the web, we didn't find an automatic tool which takes an API specification and checks the server offering the service against it. But we saw a high demand for such a tool from the community. So we decided to build it.

The tool is able to parse the API specification and create fuzzing attack scenarios based on what it defines, and outside of its definition. Each endpoint is injected with cleverly generated values within the boundaries defined by the specification, and outside of it, the appropriate requests are sent and their success or failure are reported in a detailed manner. It is also able to run various security attack vectors targeted at the existing endpoints, or even non-existing ones (such as illegal resource access, XSS, SQLi and RFI).
No human intervention needed, simply run the tool and get the results.

The tool can be easily extended to adapt to the various needs; whether it is a developer who wants to test the API she wrote or an organization which wants to run regular vulnerability or positive security scans on its public API, you name it. It is built with CI/CD in mind.

We are using this tool, among other tools, to check our security products internally.

                </details>
                

### Red Teaming

<details><summary><strong>[Backoori: Tool Aided Persistence via Windows URI Schemes Abuse](https://github.com/giuliocomi/backoori)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Giulio Comi](https://img.shields.io/badge/Giulio%20Comi-informational)

                The widespread adoption of custom URI protocols to launch specific Universal App can be diverted to nefarious purposes. The URI schemes in Windows 10 can be abused in such a way to maintain persistence via fileless technique. Backdooring a compromised user (Administrator privileges not required) is a matter of seconds. The attack is transparent to the unaware victim that won't be able to identify the attack and to the antivirus solutions that are currently not monitoring the specific Registry keys involved. These subtle fileless payloads can be triggered in many contexts, from the Narrator in the Windows logon screen (a novel Accessibility Feature abuse discovered by Giulio right before deciding to implement Backoori) to the classical web attack surface. The payloads can also be dropped in gadgets that can interact between each other by abusing, once again, the Windows URI protocols.

                </details>
                
<details><summary><strong>[DSInternals PowerShell Module](https://github.com/MichaelGrafnetter/DSInternals)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Michael Grafnetter](https://img.shields.io/badge/Michael%20Grafnetter-informational)

                The DSInternals PowerShell Module exposes many internal and undocumented security-related features of Active Directory. It is included in FireEye's Commando VM and its cmdlets can be used in the following scenarios:

- Active Directory password auditing that discovers accounts sharing the same passwords or having passwords in a public database like HaveIBeenPwned.
- Offline ntds.dit file manipulation, password resets, group membership changes, SID History injection and enabling/disabling accounts.
- Bare-metal recovery of domain controllers from just IFM backups (ntds.dit + SYSVOL).
- Online password hash dumping through the Directory Replication Service Remote Protocol (MS-DRSR).
- Domain or local account password hash injection, either through the Security Account Manager Remote Protocol (MS-SAMR) or by directly modifying the database.
- LSA Policy modification through the Local Security Authority Remote Protocol (MS-LSAD / LSARPC).
- Extracting credential roaming data and DPAPI domain backup keys, either online through directory replication and LSARPC, or offline from ntds.dit files.

                </details>
                
<details><summary><strong>[FruityDC](https://github.com/xtr4nge/FruityDC)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![xtr4nge .](https://img.shields.io/badge/xtr4nge%20.-informational)

                FruityDC is focused on dynamic callbacks for re-establishing communication with C2 infrastructure and for achieving persistence, how payloads can heal themselves after being blocked including how communication can be re-established via dynamic parametric data. The methods described are code agnostic.

                </details>
                
<details><summary><strong>[Octopus: Pre-operation C2 Server](https://github.com/mhaskar/Octopus)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Mohammad Askar](https://img.shields.io/badge/Mohammad%20Askar-informational)

                Octopus is an open source, pre-operation C2 server based on python which can control an Octopus powershell agent through HTTP/S.

The main purpose of creating Octopus is for use before any red team operation, where rather than starting the engagement with your full operational arsenal and infrastructure, you can use Octopus first to attack the target and gather information before you start your actual red team operation.

Octopus works in a very simple way to execute commands and exchange information with the C2 over a well encrypted channel, which makes it inconspicuous and undetectable from almost every AV, endpoint protection, and network monitoring solution.

One cool feature in Octopus is called ESA, which stands for "Endpoint Situational Awareness", which will gather some important information about the target that will help you to gain better understanding of the target network endpoints that you will face during your operation, thus giving you a shot to customize your real operation arsenal based on this information.

Octopus is designed to be stealthy and covert while communicating with the C2, as it uses AES-256 by default for its encrypted channel between the powershell agent and the C2 server. You can also opt for using SSL/TLS by providing a valid certficate for your domain and configuring the Octopus C2 server to use it.

                </details>
                
<details><summary><strong>[OWASP Nettacker (Updated - More in-depth Demo)](https://github.com/OWASP/Nettacker/wiki/Events)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Paul Harragan](https://img.shields.io/badge/Paul%20Harragan-informational) ![Sam Stepanyan](https://img.shields.io/badge/Sam%20Stepanyan-informational)

                Nettacker project was created to automate for information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and information. This software is able to use SYN, ACK, TCP, ICMP and many other protocols to detect and bypass the Firewalls/IDS/IPS and devices. By using a unique solution in Nettacker to find protected services such as SCADA, we could make a point to be one of the bests of scanners.

                </details>
                
<details><summary><strong>[PyExfil: A Python Data Exfiltration Package](https://github.com/cjcase/beaconleak)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Yuval Nativ](https://img.shields.io/badge/Yuval%20Nativ-informational)

                PyExfil is a python data exfiltration package for python containing servers and clients for enabling covert channels communication. The package started as a self exploratory code project and developed into a library that helps analyze various detection mechanisms.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[CrackQ: Intelligent Password Cracking](https://github.com/f0cker/crackq)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Dan Turner](https://img.shields.io/badge/Dan%20Turner-informational)

                CrackQ is, first and foremost, a Python based queuing system for managing hash cracking using Hashcat. There are several tools available for this purpose, CrackQ was born from the frustration of using these tools on a daily basis. It adds some new and interesting additional features as solutions to these frustrations. CrackQ is essentially a REST API with clients in the form of a Python CLI tool and a web GUI. The API design is very stable and works very reliably as a platform to use for day-to-day password cracking within an offensive-security team. The tool is designed to be easy to install and comprises of currently 4 docker images, built on production ready containers segregating each component, all controlled seamlessly using docker-compose. The tool will also include detailed analysis/reporting with graphs representing a multitude of metrics and automated "intelligent" cracking using various pre-existing techniques and machine learning solutions. The tool will be released open-source in the coming months.

                </details>
                
<details><summary><strong>[Omniscient: Lets Map Your Network](https://github.com/varchashva/LetsMapYourNetwork)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Pramod Rana](https://img.shields.io/badge/Pramod%20Rana-informational)

                Omniscient: Lets Map Your Network aims to provide an easy-to-use and point-in-time interface to security engineers and network administrators to represent their network in graphical form with zero manual error, where a node represents a system and relationship between nodes represents a direct connection. It also monitors the 'identified' network with user-defined periodicity and provides the analytics on rogue systems/devices present in network.

It is utmost important for any security engineer to understand their network first before securing it and it becomes a daunting task to have a 'true' understanding of a widespread network. In a mid to large level organisation's network having a network architecture diagram doesn't provide the complete understanding of network and manual verification is a nightmare. Hence in order to secure entire network it is important to have a complete picture of all the systems which are connected to your network, irrespective of their type, function, technology etc.

BOTTOM LINE - YOU CAN'T SECURE WHAT YOU ARE NOT AWARE OF.

Omniscient does it in two phases:
1. Learning: In this phase, Omniscient 'learns' the network by utilising passive network enumeration, active scans and upload of existing CMDB for on-premises network; and by querying the APIs for cloud networks. Then it builds graph database leveraging the responses of all learning activities. User can perform any of the learning activities at any point of time and Omniscient will incorporate the results in existing database.

2. Monitoring: This is a continuous and automatic process, where Omniscient monitors the 'identified' network (with user-defined periodicity) for any changes, compare it with existing information and update the graph database accordingly.

                </details>
                
<details><summary><strong>[Sigma Hunting App for Splunk](https://github.com/P4T12ICK/Sigma-Hunting-App)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Patrick Bareiß](https://img.shields.io/badge/Patrick%20Bareiß-informational)

                The Sigma Hunting App for Splunk addresses two main challenges: missing collaboration in detection rule development and automated deployment of detection rules. By using Sigma as an generic signature description language, security analysts and security researcher from all over the world can work together independent from their SIEM tool. The joint detection rule development improves the general detection capabilities of the Security Operations Centers. The manual deployment of a detection rule in Splunk was a time-consuming task in order to complete all the needed fields for a scheduled search. The Sigma Hunting App solves that problem by providing a dedicated Splunk App, which can be used to dynamically update Sigma detection rules from a Git repository.

Furthermore, the Sigma Hunting App supports the analyst in their investigations of triggered detection rules. The triggered detection rules are stored as events in a separate threat-hunting index enriched with data of the Mitre ATT&CK Matrix.

The audience should learn the following aspects:

A modern approach of detection rule development
Continuous Delivery in detection rule development through the Sigma Hunting App
Installing and configuring the Sigma Hunting App
Automated deployment of detection rules into Splunk
Features of the Sigma Hunting App
Using Sigma Hunting App to find suspicious behavior

                </details>
                
<details><summary><strong>[The Big zBang Theory: Active Directory Risk Assessment](https://github.com/cyberark/zBang)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Asaf Hecht](https://img.shields.io/badge/Asaf%20Hecht-informational) ![Nimrod Stoler](https://img.shields.io/badge/Nimrod%20Stoler-informational)

                zBang is an Active Directory Risk Assessment tool that alerts against five different Active Directory attack vectors: ACLight, Skeleton Key, SID History, Risky SPN, and Mystique.

Organizations and red-teamers should utilize zBang to identify potential attack vectors and improve the security posture of the network. The results can be analyzed with a graphic interface specifically designed for the tool.

The new zBang tool discovers critical findings like:

The most privileged accounts that must be protected, including suspicious Shadow Admins.
Possible infected DCs with the "Skeleton Key" malware.
Suspicious SID history with hidden privileges.
Risky configurations of SPNs that might lead to credential theft of domain admins.
Risky Kerberos delegation configurations in the network.

The scans do not require any extra privileges; the tool performs read-only LDAP queries to the DC and can be run using any domain user.

                </details>
                

### Web/AppSec or Red Teaming

<details><summary><strong>[DumpTheGit](https://github.com/shubhamshubhankar/DumpTheGit)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Malkit Singh](https://img.shields.io/badge/Malkit%20Singh-informational)

                DumpTheGit searches through public repositories to find sensitive information uploaded to the Github repositories.

                </details>
                

### Web/AppSec

<details><summary><strong>[huskyCI: Performing Security Tests Inside Your CI](https://github.com/rafaveira3)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Rafael dos Santos](https://img.shields.io/badge/Rafael%20dos%20Santos-informational)

                huskyCI is an open-source tool that performs security tests inside CI pipelines of multiple projects and centralizes all results into a database for further analysis and metrics.

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[IotSecFuzz: Security Framework](https://github.com/securestep9/iotsecfuzz)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Ilya Shaposhnikov](https://img.shields.io/badge/Ilya%20Shaposhnikov-informational) ![Sofia Marakhovich](https://img.shields.io/badge/Sofia%20Marakhovich-informational) ![Sergey Bliznyuk](https://img.shields.io/badge/Sergey%20Bliznyuk-informational)

                IoTSecFuzz is Open Source framework which was created with the aim of combining the maximum number of utilities for comprehensive testing of IoT device security at all levels of implementation. It has a convenient console in order to use it as a stand-alone application, as well as the ability to import it as a library.

                </details>
                

### OSINT

<details><summary><strong>[TheTHE: The Thread Hunting Experience](https://github.com/epavlick/turker-demographics/blob/master/dictionaries/qual-cutoff/0.50/dictionary.ilo)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![David Garcia](https://img.shields.io/badge/David%20Garcia-informational) ![Pablo San Emeterio](https://img.shields.io/badge/Pablo%20San%20Emeterio-informational) ![Sergio de los Santos](https://img.shields.io/badge/Sergio%20de%20los%20Santos-informational)

                TheTHE is an environment intended to help analysts and hunters over the early stages of their work in an easier, unified and quicker way. One of the major drawbacks when dealing with a hunting is the collection of information available on a high number of sources, both public and private.

All this information is usually scattered and sometimes even volatile.

Perhaps at a certain point there is no information on a particular IOC (Indicator of Compromise), but that situation may change within a few hours and become crucial for the investigation.

Based on our experience on Threat Hunting, we have created a free and open source framework to make the early stages of the investigation simpler from:

- Automation of tasks and searches.

- Rapid API processing of multiple tools.

- Unification of information in a single interface, so that screenshots, spreadsheets, text files, etc. are not scattered.

- Enrichment of collected data.

- Periodic monitoring of a given IOC in case new information or related movements appear.

TheTHE has a web interface where the analyst starts its work by entering IOCs that will be sent to a backend, where the system will automatically look up for such resource on the various configured platforms in order to obtain unified information from different sources and access related reports or data existing on them. Furthermore, any change in the resources to be analyzed will be monitored.

Everything is executed on a local system, without needing to share information with third parties until such information is not organized, linked, complete and synthesized. This allows that in case the information must be analyzed on any other platform later (such as a Threat Intelligence Platform), it can be done in the most enriching possible manner.

                </details>
                
