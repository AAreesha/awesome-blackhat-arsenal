# Europe 2017
---
## 🧠 Tools by Category
### Blue Team & Detection

<details><summary><strong>[411: A Framework for Managing Security Alerts](https://github.com/djeebus/defcon24ical/blob/master/defcon24.ics)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Kenneth Lee](https://img.shields.io/badge/Kenneth%20Lee-informational) ![Kai Zhong](https://img.shields.io/badge/Kai%20Zhong-informational)

                Modern web applications are noisy systems that generate enormous amounts of logging information. This information is valuable for debugging and for forensic reasons. Yet, sifting through this information is a daunting task, to say nothing of collecting it in the first case. Many teams have turned to suites like ELK (Elasticsearch, Logstash, Kibana) to ingest and surface this treasure trove of information. It's a valuable resource for Security teams, provided they can surface this information in a timely manner. These were the constraints Etsy worked with in 2014. We needed a solution for generating alerts on top of ELK. This system should have the capability to inject additional context into alerts. There was no available solution at the time, so we built one.We named this open-source framework 411. We designed 411 as a solution for detecting noteworthy security events, but it's a general useful alerting tool. Nor is it just limited to Elasticsearch, as we've built additional modules for pull data from other sources! This presentation assumes you have an ELK stack set up already. We'll show you some recommendations on logs to index in Elasticsearch. Examples will be provided of alerts that you can build off these logs. We'll demo some of the ways 411 can add context to alerts and the ways you can receive these alerts. Whether you're a newbie looking to learn more or a security veteran with an established system, 411 will be a valuable addition your toolkit.

                </details>
                
<details><summary><strong>[ACE (Automated Collection and Enrichment Platform)](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/L-SM-TH.md)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Jared Atkinson](https://img.shields.io/badge/Jared%20Atkinson-informational) ![Robby Winchester](https://img.shields.io/badge/Robby%20Winchester-informational)

                Many expensive Endpoint Detection and Response (EDR) tools are available, but the high cost and effort required to deploy agents to every host can be off-putting to companies. The Automated Collection and Enrichment (ACE) Platform is an open source solution that enables agentless threat hunting in an environment. This tool makes it possible for anyone to begin gathering otherwise difficult to collect host data to hunt for threats in their environment.As consultants performing Compromise Assessments, we rarely have the authority or ability to alter a customer's environment to support assessment operations. Actions like enabling Windows Remote Management (WinRM) can require levels of bureaucracy and take months to accomplish. It is also difficult to answer questions surrounding systems running MacOS and Linux. By removing a few of our assumptions, we created ACE, an ASP.NET Web Application that not only allows the scanning of Windows and MacOS machines, but also provides scan management with features like Credential Management, Scan Tracking, and File Downloading.In addition to running scripts and collecting scan data, ACE provides a robust enrichment and ingestion pipeline. Users can easily create individual enrichments in ACE to integrate their favorite data sources, such as hash lookups, IP reputation, sandboxing. The enrichment details can be integrated with original results to create the finalized data types in one object. With a final enrichment, the robust data set can be sent directly to a waiting SIEM for analysis. We supply an ELK docker image which will automatically ingest data collected by ACE. ACE provides an easy and customizable solution for threat hunters to gather and enrich data before it ever reaches the SIEM, enabling more advanced analysis.

                </details>
                
<details><summary><strong>[CERNE - Open IDS Platform](https://github.com/fuzihaofzh/distant_supervision_nlg/blob/master/output/preprocessed/wita50k/dev.src)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Dominic Smith](https://img.shields.io/badge/Dominic%20Smith-informational)

                The CERNE is a powerful, open IDS platform with on demand capture, delivering IDS alerts using the widely supports Suricata and complete TCP or UDP session data, containing suspected threats for rapid incident response analysis.

                </details>
                
<details><summary><strong>[DET (Data Exfiltration Toolkit)](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/L-SM-TH.md)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Paul Amar](https://img.shields.io/badge/Paul%20Amar-informational)

                DET aims to provide a framework to assist with exfiltrating data using either one or several channels. Social media has become extremely popular in recent attacks such as HammerToss, campaign uncovered by FireEye in July 2015. Several tools are also publicly available allowing you to remotely access computers through "legitimate" services such as Gmail (GCat) or Twitter (Twittor). Often gaining access to a network is just the first step for a targeted attacker. Once inside, the goal is to go after sensitive information and exfiltrate it to servers under their control. To prevent this from occuring, a whole industry has popped up with the aim of stopping exfiltration attacks. However, often these are expensive and rarely work as expected. With this in mind, I created the Data Exfiltration Toolkit (DET) to help both penetration testers testing deployed security devices and those admins who've installed and configured them, to ensure they are working as expected and detecting when sensitive data is leaving the network.

                </details>
                
<details><summary><strong>[Thalos - Simple and Secure Approach to Storage in Untrusted Environments](https://github.com/ecleipteon/Thalos)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Luca Maria Castiglione](https://img.shields.io/badge/Luca%20Maria%20Castiglione-informational)

                Thalos is a secure and distributed system for file storage in untrusted environments. Thalos design makes it impossible for anyone who has physical or virtual access to the servers to decrypt files without the right key and neither to establish a connection between one file and its owner. Thalos relies on local elaborations to perform encryption. Furthermore, a smart and "hierarchical" key management system makes it quick and simple to use for everyone who has an internet access.SOURCE CODE: https://github.com/ecleipteon/ThalosWHITEPAPER:  https://github.com/ecleipteon/Thalos/blob/master/docs/Thalos_doc.pdf

                </details>
                

### Red Teaming

<details><summary><strong>[2FAssassin](https://github.com/dothanthitiendiettiende/2FAssassin)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Maxwell Koh](https://img.shields.io/badge/Maxwell%20Koh-informational)

                There are many ways to steal someone's private keys without performing social engineering attacks. This talk is dedicated to discussing and demonstrating the newly discovered techniques to bypass the two-factor authentication by stealing and cracking OTP, private keys, and client certificates. By that means, an attacker must compromise the voice or text message accounts, software token, infecting memory agents, cracking passphrase, stealing hardware token, etc. 2FAssassin could turn these looted keys for more fun and profits. The demonstration will include the scenario where the private keys are compromised and then show how an attacker could leverage the situation to gain more access into the corporate networks, as well as making profits. These are not limited to systems that used single sign-on (with 2FA enabled), public key authentication (e.g., password-less authentication, authorized_keys abuse), free software token (e.g., Google Authenticator), website owner (e.g., phishing sites created using stolen private key), and even software vendors (e.g., stolen private key can be used to sign the malicious malware). 2FAssassin will automate the exploitations against the common vulnerabilities that lead to the private key leakage. It can be used to compromise individual system, or the entire network using looted private keys. It also capable to analyze and identify potential private keys from a pool of gathered files, critical key information extraction in order to identify and validate the target domain, cracking and removing the passphrase, injecting arbitrary key-based backdoors to all accessible machines, building multi-chained covert tunnels by leveraging on the loopholes found in vulnerable public key authentication, sign the malware with looted private key followed by automatic bulk distribution, generate phishing site, ... etc, and many many more exciting functionalities.

                </details>
                
<details><summary><strong>[FruityC2](https://github.com/xtr4nge/FruityC2)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![xtr4nge xtr4nge](https://img.shields.io/badge/xtr4nge%20xtr4nge-informational)

                FruityC2 is a post-exploitation (and open source) framework based on the deployment of agents on compromised machines. Agents are managed from a web interface under the control of an operator. It works as a command-and-control model and is language and system agnostic. New agents are being developed to expand the capabilities and options for FruityC2.A web client is used to interact with the FruityC2 API in a client/server mode. The client is a single web page divided into 5 sections: Interact, Listener, Payload, Delivery, Config. These options provide full control and access to the functions included in FruityC2 to create, deliver and interact with a functioning C2 capability.

                </details>
                

### Miscellaneous / Lab Tools

<details><summary><strong>[CyBot - Open-Source Threat Intelligence Chat Bot (Revamped)](https://github.com/rawalkhirodkar/chatbot/blob/master/aiml/standard/atomic.aiml)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20Miscellaneous%20/%20Lab%20Tools-gray) ![Tony Lee](https://img.shields.io/badge/Tony%20Lee-informational)

                Threat intelligence chat bots are useful friends. They perform research for you and can even be note takers or central aggregators of information. However, it seems like most organizations want to design their own bot in isolation and keep it internal. To counter this trend, our goal was to create a repeatable process using an completely free and open source framework, an inexpensive Raspberry Pi (or even virtual machine), and host a community-driven plugin framework to open up the world of threat intel chat bots to everyone from the home user to the largest security operations center.We were thrilled to demo the end result of our research at Black Hat Arsenal Vegas - a chat bot that we affectionately call CyBot. We received great feedback and ideas from an enthusiastic crowd and will demo now demo CyBot revamped at Black Hat Europe. Best of all, if you know even a little bit of Python, you can help write plugins and share them with the community. If you want to build your own CyBot, the instructions in this project will let you do so with about an hour of invested time and anywhere from $0-$35 in expenses. Come make your own threat intelligence bot today!

                </details>
                
<details><summary><strong>[Dradis - 10 Years Helping Security Teams Spend More Time Testing and Less Time Reporting](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Docs_and_Reports.md?plain=1)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20Miscellaneous%20/%20Lab%20Tools-gray) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

                Dradis is an extensible, cross-platform, open source collaboration framework for InfoSec teams. It can import from over 19 popular tools, including Nessus, Qualys, Burp and AppScan. Started in 2007 (this is the 10th year anniversary!), Dradis Framework has been growing ever since (10,000+ in the last 12 months). Dradis is the best tool to combine the output of different scanners, add your manual findings and evidence and generate a report with one click.Come see the latest Dradis release in action. It's loaded with updates including new tool connectors, a Burp extension to send your findings into Dradis directly, combining of multiple issues, additional REST API coverage, and a leaner, faster interface. Find out why Dradis is being downloaded over 400 times every week and is loved by students preparing different certifications. Be sure to check it out before we run out of the exclusive 10th anniversary stickers!

                </details>
                

### OSINT

<details><summary><strong>[DataSploit - OSINT Framework](https://github.com/DataSploit/datasploit)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Shubham Mittal](https://img.shields.io/badge/Shubham%20Mittal-informational)

                DataSploit is an OSINT framework that performs various recon techniques, aggregates all the raw data, and gives data in multiple formats. DataSploit:Performs automated OSINT on a domain/email / username / IP and find out relevant information from different sources.Easy to contribute OSINT Framework.Code for Banner, Main, and Output function. DataSploit automagically does rest of the things for you.Templates to easify your life while contributing.Useful for Pen-testers, Bug Bounty Hunters, Cyber Investigators, Product companies, Security Engineers, etc.Collaborate the results, show them in a consolidated manner.Tries to find out credentials, API-keys, tokens, subdomains, domain history, legacy portals, usernames, dumped accounts, etc. related to the target.Can be used as a library, automated script or standalone scripts.Can generate lists which can be fed to other active scan tools.Generates HTML, along with text files.

                </details>
                
<details><summary><strong>[Tinfoleak](https://github.com/vaguileradiaz)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Vicente Aguilera Diaz](https://img.shields.io/badge/Vicente%20Aguilera%20Diaz-informational)

                Tinfoleak is an open-source tool within the OSINT (Open Source Intelligence) and SOCMINT (Social Media Intelligence) disciplines, that automates the extraction of information on Twitter and facilitates subsequent analysis for the generation of intelligence. Taking a user identifier, geographic coordinates or keywords, Tinfoleak analyzes the Twitter timeline to extract great volumes of data and show useful and structured information to the intelligence analyst. Tinfoleak is included in several Linux Distros: CAINE, BlackArch, Buscador, and will be included in Kali Linux 2017.2 release. It is currently the most comprehensive open-source tool for intelligence analysis on Twitter.

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[Expliot - Internet Of Things Security Testing and Exploitation Framework](https://github.com/kzwkt/iot-exploit)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Aseem Jakhar](https://img.shields.io/badge/Aseem%20Jakhar-informational)

                IoT is an emerging field exploding with new products and innovation. The security of IoT products is still lagging behind for various reasons. One of the important reasons from security researcher's perspective is the availability of security tools. If you have been pentesting IoT products, you would agree that there are too many different tools required for the job and there is no single silver bullet. And when it comes to Smart Infrastructure, we do not have any existing solutions similar to IT penetration testing tools.We started looking at the learning curve and tools required for IoT security research and decided to create a framework that will enable the research community to speed up their research and pentesting effort. Meet expliot (pronounced - explaayotee) an open source IoT security testing and exploitation framework, right now in Beta phase, it will provide the building block for writing exploits and other IoT security assessment test cases with ease by making it simple for security researchers to create and execute simple to complex mis-use cases using the framework. The objective of the framework is:Simplicity - Ease of useExtendability - Easy to extendCoverage - Cover most of the IoT attack surfaceExpliot currently has a few recon test cases to aid pentesting. The aim of the project is to have a single framework provide multiple functionality including interfaces for IoT protocols like coAP, MQTT etc, radio protocols like BLE, Zigbee etc, hardware protocols like JTAG, I2C, SPI etc, firmware analysis.

                </details>
                
<details><summary><strong>[OpticSpy - Detecting Optical Covert Channels](https://github.com/mathew-fleisch/def-con-schedule/blob/master/docs/conference.json)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Joe Grand](https://img.shields.io/badge/Joe%20Grand-informational)

                Data exfiltration from a compromised device is usually achieved over the network, via hardware implant, or by manipulating the characteristics of an internal electronic component. Optical covert channels transmit data by modulating visible light in a way that is undetectable to the human eye. Even though hackers and academics have been exploring methods of optical data exfiltration for years, details on the techniques used to capture transmissions are not fully documented and/or require expensive equipment.OpticSpy consists of two open source hardware modules that provide a low-cost way to explore, evaluate, and experiment with optical covert channels. One is based on an easy-to-build digital receiver, while the other is an analog design that allows fine-tuning for a particular target signal.PRESENTATION MATERIALS:http://www.grandideastudio.com/optical-covert-channels/

                </details>
                
<details><summary><strong>[WHID Injector - How to Bring HID Attacks to the Next Level](https://github.com/whid-injector/WHID)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Luca Bongiorni](https://img.shields.io/badge/Luca%20Bongiorni-informational)

                WHID was born from the need for cheap and dedicated hardware that could be remotely controlled in order to conduct HID attacks (i.e. over WiFi or BLE). WHID stands for WiFi HID injector. It is a cheap but reliable piece of hardware designed to fulfill Pentesters needs related to HID Attacks, during their engagements. The core of WHID is mainly an Atmega 32u4 (commonly used in many Arduino boards) and an ESP-12s (which provides the WiFi capabilities and is commonly used in IoT projects). During the talk we will see in depth how WHID Injector was designed and its functionalities.

                </details>
                

### Web/AppSec

<details><summary><strong>[ModSecurity 3.0.0](https://github.com/SpiderLabs/owasp-modsecurity-crs/blob/v3.3/dev/CHANGES)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Victor Hora](https://img.shields.io/badge/Victor%20Hora-informational) ![Felipe Zimmerle](https://img.shields.io/badge/Felipe%20Zimmerle-informational)

                libModSecurity is a major rewrite of ModSecurity. It preserves the rich syntax and feature set of ModSecurity while delivering improved performance, stability, and a new experience in easy integration on different. Effort has also been put to testing the code extensively with regression tests, unit tests, Valgrind integration and Fuzzing, individually testing operators and transformations. This is an exciting release for the whole open-source WAF community with over 900 commits ahead of ModSecurity v2 branch. Significant updates, improvements and features added to the bleeding edge version of the open source libModSecurity (aka v3), the compatibility of rulesets, demos and future roadmap will be demonstrated. More information:Small outline of the latest release:https://github.com/SpiderLabs/ModSecurity/wiki/ModSecurity-version-3-RC1Blogpost when 3.0 development went full speed:https://www.trustwave.com/Resources/SpiderLabs-Blog/An-Overview-of-the-Upcoming-libModSecurity/Release announcement:https://sourceforge.net/p/mod-security/mailman/message/36017726/"

                </details>
                
<details><summary><strong>[OWASP ZAP](https://github.com/psiinon)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Simon Bennetts](https://img.shields.io/badge/Simon%20Bennetts-informational)

                The Zed Attack Proxy (ZAP) is currently the most active open source web application security tool and was voted the top security tool in the last Toolswatch annual survey. While it is an ideal tool for people new to appsec it also has many features specifically intended for advanced penetration testing. Simon will give a quick introduction to ZAP and then dive into the more advanced features as well as giving an overview of where its heading.

                </details>
                
<details><summary><strong>[PowerSAP - Powershell Tool to Assess SAP Security](https://github.com/CrackerCat/GitHubLinks)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Joffrey Czarny](https://img.shields.io/badge/Joffrey%20Czarny-informational)

                Most companies, small or big, use SAP technologies to work. Many of them provide access to their SAP environments through Citrix. Indeed, supplier or subcontractors need to reach SAP environment, from back office to boardroom, warehouse to storefront, desktop to mobile device; users can quickly and 'securely' access SAP enterprise application software with Citrix virtualization without exposing their SAP landscape to Internet.To pentest SAP system required some knowledge of this technologies and some hacking tool. Unfortunately, lots of SAP hacking tools are not maintained anymore and dependencies are required like RFC SDK to work. When it comes to assess/pentest the security of SAP landscape from Citrix, no tool is freely available and it is not allow or possible to install third softwares or dependencies.We present a compilation of powershell script to assess SAP, which try to answer to this problematic of dependencies and use from Citrix environment. The presentation will start by describing the issues around SAP hacking tools, then we will continue by explaining the restrictions meet to pentest from Citrix system. And then we will present in detail the tool developed to solve the issues meet and of course with some demos.

                </details>
                
<details><summary><strong>[XSSER - From XSS to RCE 2.75](https://github.com/Varbaek/xsser)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Hans-Michael Varbaek](https://img.shields.io/badge/Hans-Michael%20Varbaek-informational)

                This presentation demonstrates how an attacker can utilise XSS to execute arbitrary code on the web server when an administrative user inadvertently triggers a hidden XSS payload. Custom tools and payloads integrated with Metasploit's Meterpreter in a highly automated approach will be demonstrated live, including post-exploitation scenarios and interesting data that can be obtained from compromised web applications. This version includes new payloads for common web apps and other improvements!

                </details>
                

### Mobile Security

<details><summary><strong>[Objection](https://github.com/leonjza)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Mobile Security](https://img.shields.io/badge/Category:%20Mobile%20Security-yellow) ![Leon Jacobs](https://img.shields.io/badge/Leon%20Jacobs-informational)

                Objection is a runtime mobile exploration toolkit, powered by Frida. It was built with the aim of helping assess mobile applications and their security posture without the need for a jailbroken or rooted mobile device.The project's name quite literally explains the approach as well, whereby runtime specific objects are injected into a running process and executed using Frida.

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[OpenSCAP and SCAP Security Guide](https://github.com/redhatrises/scap-security-guide)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Martin Preisler](https://img.shields.io/badge/Martin%20Preisler-informational)

                OpenSCAP is the only free and open source implementation of the NIST SCAP standard. It has two major use cases:Vulnerability assessment - enables users to automatically scan their machines for vulnerabilities using OVAL CVE feeds coming from the operating system vendors - Red Hat, Canonical, SUSE, ... OpenSCAP can load the CVE feed and examine the machine, virtual machine storage image or container. Any missing patches are reported.Security compliance - allows fully automated evaluation and remediation of machines using SCAP security policies. Instead of looking at vulnerabilities in this use-case we are looking for weaknesses in the configuration. A good source for SCAP security policies is the open source SCAP Security Guide project which we will demo with OpenSCAP. Check out the list of available products and profiles by visiting https://static.open-scap.org/Recently we have added new Ansible remediation capabilities to both OpenSCAP and SCAP Security Guide. Now it's possible to generate Ansible playbooks out of SCAP Security Guide profiles for all products. Furthermore we have improved container scanning and now support compliance profiles as well as CVE scans.

                </details>
                
<details><summary><strong>[Seccubus](https://github.com/mrseccubus)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Frank Breedijk](https://img.shields.io/badge/Frank%20Breedijk-informational)

                Seccubus is a tool that helps reduce the time required to perform repeated vulnerability assessments on the same infrastructure.It is a wrapper around the following tools:NessusOpenVASNmapNiktoMedusaQualys SSL labsSSLyzeSkipfishZAPtestssl.shBurpAll findings are translated to the Intermediary Vulnerability Information Language (IVIL) and imported into a database. After import findings are marked as either NEW, CHANGED, OPEN, NO ISSUE, GONE or MASKED to reduce the time required for subsequent analysis.

                </details>
                
<details><summary><strong>[Threat Miner SDL - Automating Threat Intelligence for SDL](https://github.com/aaamini/hdpslicer/blob/master/HDP_data/ML.csv)</strong></summary>

                ![BH-EU-17](https://img.shields.io/badge/BH-EU-17-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Raghudeep Kannavara](https://img.shields.io/badge/Raghudeep%20Kannavara-informational)

                Although there are many readily available tools supporting Threat Intelligence for enterprise IT security, the lack of Threat Intelligence tools with a focus on Security Development Lifecycle (SDL) is a known gap in the security community. To address this shortcoming, we introduce "Threat Miner SDL," a tool leveraging machine learning to automate mining publicly available threat intelligence sources such as security blogs, twitter feeds, NVD (National Vulnerabilities Database) and threat feeds to deliver product specific potential threat information while continuously monitoring for disclosures of relevant potential vulnerabilities during product development and beyond deployment. Threat Miner SDL also provides an integrated threat management console to enable tracking triage and disposition of potential threats.

                </details>
                
