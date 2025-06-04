# Awesome Black Hat Arsenal [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Last Update](https://img.shields.io/badge/Updated-June%202025-blue)](https://github.com/yourusername/awesome-blackhat-arsenal)

> 🚀 A curated list of cutting-edge cybersecurity tools showcased at the Black Hat Arsenal events — covering offensive, defensive, and research-focused security utilities.

Whether you're in red teaming, blue teaming, appsec, or OSINT — this list helps you explore and leverage the best tools demonstrated live by security professionals across the world.

---

## 📑 Table of Contents

- [Blue Team & Detection](#blue-team-detection)

- [Miscellaneous / Lab Tools](#miscellaneous-lab-tools)

- [OSINT](#osint)

- [Red Teaming](#red-teaming)

- [Red Teaming / AppSec](#red-teaming-appsec)

- [Red Teaming / Embedded](#red-teaming-embedded)

- [Reverse Engineering](#reverse-engineering)

- [Social Engineering / General](#social-engineering-general)

- [Web/AppSec](#webappsec)

- [Web/AppSec or Red Teaming](#webappsec-or-red-teaming)

---

## OSINT


### [!CVE: A New Platform for Unacknowledged Cybersecurity !Vulnerabilities](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
In the ever-evolving cybersecurity landscape, the identification and acknowledgment of vulnerabilities through the Common Vulnerabilities and Exposures (CVE) system play a crucial role. However, vendor discretion in determining whether a security issue warrants a CVE assignment often results in overlooked vulnerabilities that pose significant risks. This presentation introduces the !CVE initiative, a groundbreaking platform that addresses this critical gap by identifying, tracking, and sharing unacknowledged cybersecurity vulnerabilities.

Our presentation begins with an overview of the CVE system and the challenges security researchers face in dealing with unacknowledged vulnerabilities. We discuss real-world examples of security issues ignored by vendors and explore the potential consequences of these hidden threats. We then delve into the !CVE platform, detailing its mission, features, and collaborative approach to empower the security community.

Through case studies, we demonstrate the value of the !CVE initiative in strengthening the cybersecurity ecosystem, highlighting the significance of addressing vulnerabilities not recognized by vendors. We also showcase the reporting process, expert panel, and public availability of !CVE reports, fostering a transparent and inclusive environment for vulnerability tracking and sharing.

Join us in exploring the world of unacknowledged cybersecurity vulnerabilities and learn how the !CVE initiative is bridging the gap between vendor discretion and community-driven security efforts. By raising awareness and fostering collaboration, we can create a more secure and resilient digital landscape for all.


### [Attack Surface Mapper: Automate and Simplify the OSINT Process](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Reconnaissance is an integral part of the testing process. Successfully scanning and footprinting the attack surface can assist Red Teamers in crafting precise attacks, but can also help defenders identify weak spots.

Attack Surface Mapper aims to automates and simplify the OSINT process. It does this by taking a target domain as input, then analysing it using passive OSINT techniques and (optional) active reconnaissance methods. It expands the attack surface automatically with the aim to provide actual useful intelligence for an engagement.

This means that you can plug in a target domain, make a cup of tea and come back later to collect:

Email
Usernames
Breached Passwords
Phone Numbers
Linked IPs
Target subdomains
Website Maps
Social Media Presences
Open Ports

This is a list of techniques that Attack Surface Mapper uses:

[+] Reconnaissance:

Find IPs from ASN
Find Subdomains
BruteForce Subdomains
Port Scanning
Hostname Discovery
Passive & Active DNS Record capturing
WHOIS records
Take screenshots of web portals and remote services

[+] Intel Extraction:

Content Discovery (Phone Number, Addresses and Vacancy Postings)
Scrap LinkedIn Employee Names & Email addresses
Check Public Breaches
Find AWS buckets
Interesting Files (e.g PDF and XML)
Interesting Strings (sensitive data such us API keys, AWS secret keys and CreditCard numbers).

[+] Plugins:

Support for Shodan API
Support for dnsdumpster [Generate a DNS map]


### [CertPivot: Infra-Chaining + Cert-Check](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
CertPivot is a newest module of LAMMA specifically focuses on 2 features. One is Infra-Chaining using TLS certificates and second Cert-Check which looks for non-trusted TLS certificates in the trust store of a given machine.

Infra-Chaining feature of CertPivot module is useful specially for threat hunters and incident respondents, where as Certi-Check feature can be additionally used by admins and crypto-auditors


### [CrowdSec: The Open-Source & Participative IPS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
None


### [DRADIS: 10 YEARS HELPING SECURITY TEAMS SPEND MORE TIME TESTING AND LESS TIME REPORTING](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Dradis is an extensible, cross-platform, open source collaboration framework for InfoSec teams. It can import from over 19 popular tools, including Nessus, Qualys, Burp and AppScan. Started in 2007 (this is the 10th year anniversary!), Dradis Framework has been growing ever since (10,000+ in the last 12 months). Dradis is the best tool to combine the output of different scanners, add your manual findings and evidence and generate a report with one click.

Come to see the latest Dradis release in action. It's loaded with updates including new tool connectors, a Burp extension to send your findings into Dradis directly, combining of multiple issues, additional REST API coverage, and a leaner, faster interface. Find out why Dradis is being downloaded over 400 times every week and is loved by students preparing different certifications. Be sure to check it out before we run out of the exclusive 10th anniversary stickers!


### [DataSploit 2.0](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
An #OSINT Framework to perform various recon techniques on Companies, People, Phone Number, Bitcoin Addresses, etc., aggregate all the raw data, and give data in multiple formats.
Details:

Performs OSINT on a domain / email / username / phone and find out information from different sources
Correlate and collaborate the results, show them in a consolidated manner
Tries to find out credentials, api-keys, tokens, subdomains, domain history, legacy portals, etc. related to the target
Use specific script / launch automated OSINT for consolidated data
Performs Active Scans on collected data
Generates HTML, JSON reports along with text files

New Features:

Active Modules
Well parsed JSON and HTML Reports
BitCoin Address OSINT
More in-depth Social Media Searches
Basic Vulnerability checks on Subdomains
Subdomain Takeover, etc.
DB Support
Support for Multiple Alternative API Keys


### [DATASPLOIT - AUTOMATED OPEN SOURCE INTELLIGENCE (OSINT) TOOL](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Utilizing various Open Source Intelligence (OSINT) tools and techniques that we have found to be effective, DataSploit brings them all into one place, correlates the raw data captured and gives the user, all the relevant information about the domain/email/ phone number/person, etc. It allows you to collect relevant information about a target which can expand your attack/defense surface very quickly. Sometimes it might even pluck the low hanging fruits for you without even touching the target and give you quick wins.

New release also includes ACTIVE modules which allow to use information collected from OSINT and use it for active exploitation either directly or by integrating with other Social Engineering / Pen-testing tools.


### [Defascan: Defacement Scan and Alert](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Web server defacement is also a major problem especially for government sites. Therefore, this project intends to develop a web server defacement detection tool named DefaScan. This tool, DefaScan will detect a defaced website and notify about it.


### [Defaultinator: An Open Source Search Tool for Default Credentials](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Have you ever had to Google around trying to find a default password for a router? Are you sick of combing through user manuals just to find admin:admin buried on page 37. Then it's time you tried Defaultinator. This newly released tool is a repository for default credentials made searchable via API or the intuitive web interface. Why would someone make such a tool? Why, I'm so glad you asked!

Static device passwords are not only Really Bad, they are sometimes illegal. Yet legacy or poorly secured IoT devices still often contain default or hardcoded passwords. It's hard to know if you have default passwords in your environment, but this tool is here to help you find them. Or maybe you are on a Red Team engagement and want to audit for CWE-798 (Use of Hard-coded Credentials). Defaultinator has your back.

In this talk, I'll cover how default passwords contribute to the spread of malware, how common it is to see them used in brute force attacks 'in the wild', and how a tool like Defaultinator can help you identify them and remove them from your own environment.


### [Desenmascara.me: How to Track Online Counterfeiters](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
What is one of the biggest examples of online fraud being massively underestimated?: Online counterfeiters. This fraud captured the attention of two bigs intelligence providers by publishing a joint report titled: "Why Retailers Are Losing The Fight Against Online Counterfeiting."

However, security vendors providing protections against C2, malware and any kind of malicious domains still do not provide protection against online counterfeiters. In the rare cases when they do, they do it by playing the cat-and-mouse game (not scalable) and they confuse online counterfeiters with phishing even when is a totally different threat with different goals. Therefore, the goal of the online tool presented here: desenmascara.me is to raise awareness of this increasing online fraud with real examples of any major brand.


### [Dradis Framework: Combine the Output of 20 Scanners and Automate Your Reporting](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Dradis is an extensible, cross-platform, open source collaboration and reporting tool. It can import from 20+ popular tools, including Nessus, Qualys, Burp and AppScan. Started in 2007, Dradis Framework is still downloaded 400+ **per week**. Dradis is the best tool to combine the output of different scanners, add your manual findings and evidence and generate a report with one click.

If you're still reviewing your scan results manually, or putting together your reports by hand, or sending emails to your colleagues to coordinate your projects, or copying and pasting findings from old reports instead of having a findings database, you need to check Dradis out. Some of the features that set Dradis apart are:

Built in testing methodologies (OWASP, OSTMM, PTES,...)
Flexible reporting
Team collaboration: commenting, notifications, Slack integration
Burp extension
Full REST API coverage to build your own integrations
Dozens of open-source plugins to inspire your own
Solid community of users
Best tool to prepare your OSCP certification

If you're looking for a collaboration tool that has a track record, is open source, and keeps improving every day (there have been over 850 improvements and 4 major releases, since last year), come and visit our Arsenal station.


### [Dradis Framework: Learn How to Cut Your Reporting Time in Half - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Dradis is an extensible, cross-platform, open source collaboration framework for corporate and consulting teams. It can import from over 19 popular tools, including Nessus, Qualys, Burp and AppScan. Started in 2007 (yup, we've been helping 1000s of InfoSec pros for 11 years), Dradis Framework has been growing ever since. Dradis is the best tool to combine the output of different scanners, add your manual findings and evidence and generate a report with one click.

Come see the latest Dradis release in action. It's loaded with updates including better communication and notifications, new tool connectors, additional REST API coverage, cleaner and faster UI and much more. Find out why Dradis is being downloaded over 400 times every week and is loved by students preparing different certifications and experienced professionals alike. Be sure to check it out before we run out of our popular stickers! Btw, did you know Dradis is the only security tool with its own jingle? You've got to see this.


### [GitDorker: I'm in Your GitHub Dorking All Your Secrets](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
GitDorker is a tool that utilizes the GitHub Search API and an extensive list of GitHub dorks that I've compiled from various sources to provide an overview of sensitive information stored on GitHub given a search query.

The primary purpose of GitDorker is to provide the user with a clean and tailored attack surface to begin harvesting sensitive information on GitHub. GitDorker can be used with additional tools such as GitRob or Trufflehog on interesting repos or users discovered from GitDorker to produce best results.


### [GodEye: Advanced Geo-Localization Through AI-Powered Visual Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
God Eye is an innovative AI-powered geo-localization tool that can estimate a photograph's location without the need for EXIF data extraction. God Eye aims to improve the accuracy of current geolocation estimation techniques by combining cutting-edge models and techniques. The tool has a straightforward web-based interface that allows users to upload images and receive location estimates automatically. God Eye constantly improves its accuracy and expands its capabilities by comparing and training with open street view data and other crawled data sources. God Eye's primary applications are in open-source intelligence (OSINT) and cybersecurity, where it aids forensic investigations by identifying image source and location. God Eye, with its robust technology and user-friendly design, is poised to become an indispensable tool for professionals in a variety of fields who require precise and dependable image-based geolocation.


### [KubiScan: Searching for Risky Pods and Permissions in Kubernetes Cluster](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
KubiScan is a tool that was created to search for risky Pods which contain a privileged service account tokens that can be used for privilege escalation or even compromising the cluster. It can also show you all the risky roles, rolebindings, users and privileged pods in the Kubernetes Cluster and other cool stuff.


### [Maltego - Host.io](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Maltego is a link analysis application of technical infrastructure and social media and enriches disparate sources of Open Source INTelligence (OSINT). Maltego is listed on the Top 10 Security Tools for Kali Linux by Network World and Top 125 Network Security Tools by the Nmap Project. Host.io provides a list of outbound links, backlinks, etc for a given domain name. The integration of Host.io with Maltego displays technical infrastructure in an easy to understand graph format.


### [Maltego: FullContact](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
FullContact allows you to search on an e-mail address, Twitter username, location, name, company, and alias or verify an e-mail address.

Maltego is a link analysis application of technical infrastructure and/or social media networks from disparate sources of Open Source INTelligence (OSINT). Maltego is listed on the Top 10 Security Tools for Kali Linux by Network World and Top 125 Network Security Tools by the Nmap Project.

The integration of FullContact with Maltego links the input to it's e-mail address, Twitter username, location, name, company and alias in an easy to understand graph format that can be enriched with other sources of data.


### [Maltego: "Have I Been Pwned?""PwnedPasswords" and "FullContact"](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
“Have I been pwned?" allows you to search across multiple data breaches to see if your email addresses or aliases has been compromised by LinkedIn, MySpace, Dropbox, etc.

"PwnedPasswords" are half a billion real world passwords previously exposed in data breaches. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts.

"FullContact" allows you to enrich a Twitter username, location, person's name, company and alias or verify an e-mail address.

Maltego is a link analysis application of technical infrastructure and/or social media networks from disparate sources of Open Source INTelligence (OSINT). Maltego is listed on the Top 10 Security Tools for Kali Linux by Network World and Top 125 Network Security Tools by the Nmap Project.

The integration of "Have I been pwned?” "PwnedPasswords" and "FullContact" with Maltego presents this data in an easy to understand graph format that can be enriched with other sources.

Release:

Major Update i.e. "Have I Been Pwned?"
New tool to be released at Black Hat i.e. "FullContact"


### [Mantis - Asset Discovery at Scale](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
None


### [Manuka: A modular, scalable OSINT honeypot targeting pre-attack reconnaissance techniques](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Manuka is an Open-source intelligence (OSINT) honeypot that monitors reconnaissance attempts by threat actors and generates actionable intelligence for Blue Teamers. It creates a simulated environment consisting of staged OSINT sources, such as social media profiles and leaked credentials, and tracks signs of adversary interest, closely aligning to MITRE's PRE-ATT&CK framework. Manuka gives Blue Teams additional visibility of the pre-attack reconnaissance phase and generates early-warning signals for defenders.

Although they vary in scale and sophistication, most traditional honeypots focus on networks. These honeypots uncover attackers at Stage 2 (Weaponization) to 7 (Actions on Objectives) of the cyber kill chain, assuming that attackers are already probing the network.

Manuka conducts OSINT threat detection at Stage 1 (Reconnaissance) of the cyber kill chain. Despite investing millions of dollars into network defenses, organisations can be easily compromised through a single Google search. One recent example was hackers exposing corporate meetings, therapy sessions, and college classes through Zoom calls left on the open Web. Enterprises need to detect these OSINT threats on their perimeter but lack the tools to do so.

Manuka is built to scale. Users can easily add new listener modules and plug them into the Dockerized environment. They can coordinate multiple campaigns and honeypots simultaneously to broaden the honeypot surface. Furthermore, users can quickly customize and deploy Manuka to match different use cases. Manuka's data is designed to be easily ported to other third-party analysis and visualization tools in an organisation's workflow.

Designing an OSINT honeypot presents a novel challenge due to the complexity and wide range of OSINT techniques. However, such a tool would allow Blue Teamers to "shift left" in their cyber threat intelligence strategy.


### [New Face, Who Dis? Protecting Privacy in a World of Surveillance](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
While it has its potential benefits, facial recognition is eroding privacy and other human rights. Over the past year, several organizations have acknowledged that they have "scraped" social media and similar sites for photos to build their biometric databases, and photos intended for personal use only have now been potentially weaponized.

Industry and government have ethical responsibilities to prevent this, but what if there were a way to enhance privacy for individuals without waiting for the cavalry? Adversarial technology can provide a way to protect this biometric, but it must be as easy to use as picking up their mobile device and taking a photo.

Introducing "Ruse," a mobile app that seeks to use adversarial strategies to make personal photos less useful for commercial facial recognition systems while retaining a (relatively) low impact on human usefulness.


### [OSRFRAMEWORK: OPEN SOURCES RESEARCH FRAMEWORK](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
OSRFramework is a GNU AGPLv3+ set of libraries modularly developed by Yaiza Rubio and Félix Brezo to perform Open Source Intelligence tasks. In the framework, the authors include a series of applications related to username checking, DNS lookups, social media research, regular expressions extraction and many others. At the same time, by means of ad-hoc Maltego transforms, OSRFramework provides a way of making these queries graphically as well as including other interfaces to interact with it using the command line and a web server.

The most important tools included in the framework are:

usufy.py. Application focused on checking the existence of different usernames in up to 309 platforms (as May 4th, 2017).
domainfy.py. Application focused on finding existing domains and common subdomains that currently resolve to IP addresses (more than 1500 possible domains checked). Whois information is retrieved when possible.
mailfy.py. Application that validates the existence or not of an email account in more than 20 different email providers.
Other tools included are: alias_generator.py, phonefy.py and searchfy.py as well as osrfconsole.py (msfconsole-like command line GUI), osrframework_server.py (a Web interface that includes an API) and several local Maltego transforms and entities.
Amongst the capabilities included, it is possible to export to several formats (.csv, .xls, .xlsx, .gml, etc.), to configure the number of threads and proxy settings and to define the credentials to be used if the forum enforces it.

As each security analyst may be facing different information needs, the tool has been conceived to be easily configurable so as to include new local sources. By means of plugins that analysts can add locally using the templates provided by the authors, security researchers will be able to adapt the tool to his/her own specific needs at any time.


### [Octopii - AI-powered Personal Identifiable Information (PII) scanner](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Octopii is an open-source AI-powered Personal Identifiable Information (PII) scanner that can look for image assets such as Government IDs, passports, photos and signatures in a directory.


### [Octopii v2](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Today, given the number of services that collect Personal Identifiable Information (PII) for purposes such as 'KYC' (Know Your Customer) documents, bureaus keeping records of people, small businesses keeping records of their employees, and so on, PII faces a wide variety of threats. With increasing security breaches, protecting valuable data such as Personal Identifiable Information must be the top priority of all organizations. The first step in accomplishing this is to identify the exposure of such assets.

This is why we created Octopii, an AI-powered Personally Identifiable Information (PII) scanner that uses Optical Character Recognition (OCR), regular expression lists and Natural Language Processing (NLP) to search public-facing locations for Government ID, addresses, emails etc in images, PDFs and documents.


### [PROJECT SPLINTER - MAKE INFORMED DECISIONS BASED ON CYBER THREAT INTEL](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Indicators of Compromise (IoCs) form a core component of a security analyst's decision making process, but there is very little emphasis paid to recognizing their dynamic nature in the overall analysis. Adversaries are dynamic entities that adapt to their environment and change their tactics and techniques with time. Our goal is to bring a scientific approach to cyber threat analysis by utilizing Bayesian inference to reduce uncertainty in decision making. We will present a tool that calculates statistical probabilities for assigning classification labels to campaign or malware families based on observed IoC's. This tool also allows analysts to take into account temporal quantity of the observations to strengthen this statistical inference. To demonstrate the capabilities of the tool we will use the Fidelis Barncat Threat Intelligence dataset. The Barncat dataset represents an acceptable ground truth for the past state of the world, which can be used to informed new observations. We will show how the tool allows to backtest classification models using this dataset and propose security centric decision metrics for identifying the most optimal model.


### [PasteHunter: Scanning Pastebin with Yara Rules](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
From a security analytics and Threat Intelligence perspective, Pastebin is a treasure trove of information. All content that is uploaded to Pastebin and not explicitly set to private (which requires an account) is listed and can be viewed by anyone.

Hackers and script kiddies are quick to push their warez on to the site for the world to see and developers/network engineers are prone to accidentally leaking internal configurations and credentials. Anyway, how can we the lowly security analyst sift through all this data and use it to our advantage? We can scrape Pastebin and check all the data uploaded to see if any of it is of interest to us. There are some tools that can monitors paste sites with a set of regular expressions but I wanted more control and flexibility.

Having used Yara extensively in Malware analysis and Threathunting I saw it as a powerful method for quickly scanning large amounts of data and identifying the contents.

Over the last two years of development Pastehunter has grown to include modular inputs that can read from any data source and process the data in to a searchable indexed data set that also has the ability to send notifications with minutes of data matching your rules going public.

Inputs include Pastebin, Github Gists and all StackExchange posted questions. Ouptuts include Elastic Search and SMS / WhatsApp / Slack amongst others.


### [Quark Engine: Storyteller of Android Malware](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Quark is one of the most popular analysis engines for hunting threat intelligence inside the APK files. Since it is rule-based, you can use the ones built-in or customize as needed.

With ideas decoded from criminal law, Quark has its unique angles for malware analysis. We developed a Dalvik bytecode loader that has tainted analysis inside but also defeats the obfuscation techniques used against reverse engineering. And surprisingly, the loader matches perfectly the design of our malware scoring system.

Features/Progress in recent versions of Quark:
1. Public Reports: AhMyth RAT and Roaming Mantis. And we give out all detection rules used in the reports
2. Call Graphs for behavior detected
3. Behavior Classification
4. New Strategy for Generating Rules
5. Open-Sourced all codes for rule generation
6. Python Binding APIs: Made Quark easy to be integrated.
7. Integrated to Intel Owl, BlackArch Linux, Pithus/Bazaar and APKLAB

In recent versions of Quark, we put huge efforts into making it more useful and practical. We have public reports that analyze classic samples like AhMyth RAT and Roaming Mantis. And we gave out all detection rules used in these reports!

In those reports, we show how users can use new features of Quark to quickly realize how the malware works. For example, malware analysts now can use Quark to generate call graphs of each behavior detected. And we also provide a feature that can automatically classify the detected behaviors in APK so as to boost up the storytelling of malware.

Moreover, to make Quark a more practical tool to use, we developed a new strategy for generating detection rules. The new strategy improves the effectiveness of the rules and efficiency of the generating process. Even better, we open-sourced all codes for everyone.

With the usefulness of Quark, we now have developed python binding APIs for integration with other open-source projects. Now you can use Quark in projects like Intel Owl, BlackArch Linux, Pithus/Bazaar, and APKLAB. We'll be demonstrating how Quark enriches our partners during the presentation.


### [RTS: Real Time Scrapper](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
RTS (Realtime scrapper) is a tool developed to scrap all pasties, github, reddit, etc. in real time to identify occurrence of search terms configured. Upon match, an email will be triggered. Thus, allowing a company to react in case of leakage of code, any hacks tweeted, etc. and harden themselves against an attack before it goes viral.


### [RTTM: Real Time Threat Monitoring Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Monitoring possible threats of your company on the Internet is an impossible task to be achieved manually. Hence, many threats of the company go unnoticed until it becomes viral in public - thus causing monetary/reputation damage. This is where RTTM comes into action. RTTM (Real-Time Threat Monitoring Tool) is a tool developed to scrap all pasties, GitHub,reddit..etc in real-time to identify an occurrence of search terms configured. Upon a match, an email will be triggered. Thus allowing the company to react in case of leakage of code, any hacks tweeted..etc.. and harden themselves against an attack before it goes viral.

Over the past 2 years, the tool has evolved from a simple search. Artificial intelligence has been implemented to perform a better search. If regex is needed even that is supported. Thus, behavior is close to human and reduces false positives.

The best part of the tool is that alert will be sent to email in less than 60 seconds from the time threat has made it to the internet. Thus allowing response in real-time to happen.

The same tool in malicious user hands can be used offensively to get an update on any latest hacks, code leakage, etc..


### [Recon.Cloud - Cloud Attack Surface Management and Cloud Reconaissance](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Recon.Cloud is a public and free AWS cloud security reconnaissance tool that will enable users to reveal publicly exposed cloud assets on any domain. There are many tools in the market that are open to users for reconnaissance efforts, but there are few that specifically scope recon efforts to look at the cloud alone. Typical recon tools provide an exhaustive list of all assets they detect – there is no scope to define the cloud assets themselves. This leaves users overwhelmed with too much information that can be difficult and time-consuming to comb through.


### [ReconPal: Leveraging NLP for Infosec](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Recon is one of the most important phases that seem easy but takes a lot of effort and skill to do right. One needs to know about the right tools, correct queries/syntax, run those queries, correlate the information, and sanitize the output. All of this might be easy for a seasoned infosec/recon professional to do but for rest, it is still near to magic. How cool it will be to ask a simple question like "Find me an open Memcached server in Singapore with UDP support?" or "How many IP cameras in Singapore are using default credentials?" in WhatsApp chat or a web portal and get the answer?

The integration of GPT-3, deep learning-based language models to produce human-like text, with well-known recon tools like Shodan is the foundation of ReconPal. In this talk, we will be introducing ReconPal with report generation capabilities and interactive terminal sessions. We are also introducing a miniature attack module, allowing users to execute popular exploits against the server with just the voice commands. The code will be open-source and made available after the talk.


### [Report Writing Is Half the Battle: Finish Your Report in Less Time and Get Back to Hacking.](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
A single place to hold assessment findings, notes, methodologies, tasks, and feedback from your team makes working together simpler and saves time delivering reports. Dradis combines the output of 20+ popular security tools - including Nessus, Qualys, Burp, and Nmap, along with your manual notes to keep all of your findings centralized for one click report generation.
If you're reviewing scan results manually or putting together reports by hand, digging through emails and chat logs for details from teammates, or copying and pasting findings from old reports instead of having a findings database, do yourself a favor and download Dradis CE so you can get back to hacking.

Started in 2007 to solve the frustrations associated with creating reports, Dradis Framework has an established track record and a full time, international team working every day so you can ditch the overhead of a traditional security assessment workflow.


### [SCMPrey: Supply Chain Reconstruction Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Introducing SCMPrey, a threat intelligence tool to be used by either red or blue teams that would like to reconstruct and map-out repositories supply chain infrastructure, CI/CD system, build environment, packaged dependencies etc.

By consuming code repositories, looking for indicators of usage and propagation within the code base and the SCM system that holds the data, enacting post-processing and contextual reconstruction of the data in order to form a thorough reconstruction of the supply chain infrastracture components, configuration and automations in place.

With this knowledge - ethical hackers will be able to spot attack surface and home on designated attack targets of interest, spot weak points and low-hanging fruit; on the other - blue team will be able to spot the same weaknesses to enable them to form a solid threat model and hardening needs to fortify said infrastructure and implementations.


### [Scammer Detector (NFT Scam Activities Monitoring)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
We protect NFT users and the community from spam, scam and phishing attacks. In this context, we provide this with 4 main modules. (SpamEye, SpamPolice, ScamNotify, and BroExt)


### [Scrapesy: Open Source Credential Leak and Validation Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
None


### [Social Mapper: Social Media Correlation Through Facial Recognition](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Social Mapper is a Open Source Intelligence Tool that uses facial recognition to correlate social media profiles across different sites on a mass scale. It takes an automated approach to searching popular social media sites for targets names and pictures to accurately detect and group a person's presence, outputting the results into report that a human operator can quickly review.

Social Mapper has a variety of uses in the security industry, for example the automated gathering of large amounts of social media profiles for use on targeted phishing campaigns. Facial recognition aids this process by removing false positives in the search results, so that reviewing this data is quicker for a human operator.

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

An organisation's name
A folder full of named images
A CSV file with names and url's to images online


### [Spartacus as a Service (SaaS): Privacy via Obfuscation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
The Third Servile War was over. The slave army has been defeated, and the survivors are offered a pardon by their Roman captors. The only requirement was that they identify Spartacus, their leader (Kirk Douglas). Rather than give away his identity, however, they all begin to yell out "I'm Spartacus!"—thus preserving his anonymity by overwhelming the Romans with possibilities. (Spoiler alert: they all die as a result.)

Since users cannot rely on governments to ensure privacy, a different method of privacy assurance is proposed: privacy through obfuscation.

"Spartacus as a Service (SaaS)" is an open-source proof-of-concept is introduced that facilitates these obfuscation techniques. This will allow for automatic obfuscation of a chosen identity on a small scale, and lessons learned from its usage will be discussed.

Additional information:

Current version at: https://github.com/derrumbe/Spartacus-as-a-Service
Open-source tool written largely in Node.js under an MIT license
Development is ongoing, and this is expected to be a long-term project (first official release would coincide with BlackHat/DefCon)
Authorization for obfuscation is done via OAuth for a signed in user (explicit consent is therefore given)
Additional resources have been incorporated to accommodate this content. A Markov chain is used to generate new content based on a textual repository (ranging from political platforms to the oft-used Jane Austen canon to Aaron Franklin's book on BBQ (he's a big deal here in Austin.)) Amazon Mechanical Turk may be used to circumvent bothersome pieces such as captchas.
Note that this is not a tool that *prevents* targeted advertising and the like, instead it seeks to dilute the value of information that companies know about a user, masking the true information from the fake, so that it is impossible to tell what the real content (or in some cases, who the person) actually is.


### [Squatm3: Cybersquatting Made Easy](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Squatm3 is a python tool designed to enumerate available domains generated modifying the original domain name through different techniques:

Substitution attacks
Flipping attack
Homoglyph attack

Squatm3 will help penetration testers to identify domains to be used in phishing attack simulations and security analysts to prevent effective phishing attacks.

Presentation: https://www.dropbox.com/s/8r9t16s4x94iczu/blackhat-eu18-arsenal.pptx?dl=0


### [Squatm3gator: 360° Cybersquatting](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Squatm3gator (presented at BHEU 2018) is a python tool designed to enumerate available and not available domains generated by modifying the original domain name through different techniques:

- Substitution attack
- Flipping attack
- Duplicate attack
- Homoglyph attack

Squatm3gator is based on Squatm3 and will help penetration testers to identify domains to be used in phishing attack simulations and security analysts to prevent effective phishing attacks.

The new release will contains the following improvements:

- for each domain to retrieve whois information
- highlights soon-to-expire domains
- first release of automatic phishing website detection

Presentation Slides: http://i.blackhat.com/asia-19/Arsenal/BH-Asia-2019_Arsenal.pptx


### [TALR: Automating the Sharing and Ingestion of SIEM Rules](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Keeping up with the evolving landscape of attacker techniques can feel like an uphill battle. Many organizations use a SIEM to perform log correlation and analysis and can attest that keeping rules current is a challenge. To combat the burden of keeping pace with the offensive community, this presentation will detail a new initiative to develop, share, and assess the latest and greatest in alerting logic—the Threat Alert Logic Repository (TALR). TALR is a repository of curated SIEM rules, designed for quick and easy ingestion in to the SIEM tool of your choice. The TALR repository is a publicly available TAXII server intended to keep SIEM engineers and analysts up-to-date on the latest and greatest detection logic. The TALR agent will provide a means to submit new rules to the repository, and to download updates for the latest detection rules (using our repository, or any TAXII server hosting TALR formatted SIEM content).

Attendees will gain a comprehensive overview of TALR and understand how to incorporate it into their environments as a way to remain on the cutting edge of alerting logic, and as a means of enacting more contextualized and informed response.


### [TSURUGI LINUX: DFIR INVESTIGATIONS, MALWARE ANALYSIS AND OSINT ACTIVITIES MADE EASY](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Any DFIR analyst knows that every day in many companies, it doesn't matter the size, it's not easy to perform forensics investigations often due to a lack of internal information (like mastery of all IT architecture, having the logs or the right one...) and ready to use DFIR tools.

As DFIR professionals we have faced these problems many times and so we decided last year to create something that can help those who will need the right tool at the "wrong time" (during a security incident).

And the answer is the Tsurugi Linux project that, of course, can be used also for educational purposes.
After more than a year since the last release, a Tsurugi Linux special BLACKHAT EDITION with this major release will be shared with the participants before the public release.


### [TheTHE: The Thread Hunting Experience](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
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


### [Token-Hunter & Gitrob: Hunting for Secrets](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
Secrets like API tokens, encryption keys, and passwords are a keystone in the development world. They facilitate important functionality not only in the software that developers build, but also in the deployment, maintenance, integration, and security of both closed and open-source projects. Many companies providing services on the internet offer API tokens in multiple flavors that allow interaction with their systems, as does GitLab. Token-Hunter and Gitrob are complementary tools developed, augmented, and heavily used by GitLab's red team to support their engagements and, most importantly, find those exposed secrets and demonstrate their abuse!


### [WhiteRabbit: Combining Threat Intelligence, Public Blockchain Data, and Machine Learning to go Down the "Dirty Money" Rabbit Hole](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
WhiteRabbit will be used to demonstrate how machine learning models can be used on a merged dataset combining cyber related contextual information with Bitcoin (BTC) transaction data. The model can be used by both private and public sectors security professionals, working in the cryptocurrency field, to deny business for certain BTC addresses or, build legal cases to return illegally stolen coins.

To build the dataset, we collected a list of BTC addresses involved in illegal activities. Using these addresses as a starting point, we navigated along the chain, and reconstructed a cluster of connected "dirty" addresses. We used rules such as First-In-First-Out (FIFO) to label them. These labeling techniques can be used to tag certain BTC addresses that fall within this path as "dirty" addresses because they handled money acquired through illegal activities. We can then take this a step further and analyze the characteristic behavioral elements of these addresses. This behavioral analysis will allow us to determine the features representing this malicious behavior and use them within a machine learning model classifying new BTC addresses.

Our model-building approach is based on a three part framework: The first part is to collect a set of BTC addresses and classify them as "clean" or "dirty" to use them as our ground truth. The second part is to test the classification models using this dataset and propose decision metrics to optimally pick a model. In this part, we will also discuss ideas about how to compute expensive, but important features obtained from transaction data stored on a graph database. In the third part, we will show how to use the obtained optimal model to predict if an address is "dirty". Finally, we will discuss our challenges when solving this problem and propose solutions to overcome them.


### [iKy – OSINT TOOL](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
iKy is an Open Source project. From an e-mail or other selectors (username, twitter, instagram, etc) it tries to collect data to later convert them into visual information
OSINT tools are many and varied. But with iKY it was sought, apart from a good performance, an attractive graphic visual supported by the fact that neuroscientifically the brain interprets images better and faster than numbers and letters


### [kubeletctl: A Kubelet Client to Attack Kubernetes](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
kubeletctl is a CLI client for kubelet - the remote agent of Kubernetes on the nodes. It implements all the documented and undocumented API of kubelet but it also includes offensive capabilities:
- Scan for vulnerable nodes
- Scan for containers with RCE
- Run command on multiple containers


### [shrewdeye - low hanging OSINT and reconnaissance](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-OSINT](https://img.shields.io/badge/Category-OSINT-gray)  
The vulnerability searching process requires a lot of time. If you want to cover all the perimeter in an appropriate amount of time and get valuables, automation of routines is one of the cornerstones, that will help you to focus on more complex things.
shrewdeye - opensource web platform for continuous reconnaissance. It allows you to combine other tools in chain to automate your perimeter workflow reconnaissance. It comes with built-in modules for famous tools like amass, assetfinder, subfinder, gau, nmap and others.


---

## Blue Team & Detection


### [0365Squatting](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
One of the main benefits of cloud technology is to deploy quickly services, with minimum interaction from the administrator side, this is an advantage exploited by cyber criminals too. Nowadays the main threats all size companies are facing is phishing, every day cybercriminals are creating more sophisticated techniques to cheat users and make more difficult the job of blue teams. The most common technique used is typo squatting.

Part of the Blue team mission is to detect phishing, typo squatters, and attack domains before the phishing campaign begins, there is outside plenty of tools trying to detect that domains based on DNS, however none of them are focus into the cloud.
0365Squatting is a python tool created to identify that domains before the attack start. The tool can create a list of typo squatted domains based on the domain provided by the user and check all the domains against O365 infrastructure, (these domains will not appear on a DNS request).

At the same time, this tool can also be used by red teams and bug bunters, one of the classic attacks is the domain takeover so, the second option of this too is to check if the domain is registered in O365 in order to launch a domain takeover attack.


### [ACT: Semi-Automated Cyber Threat Intelligence](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
ACT is an open-source threat intelligence platform that has been built from the ground up to address the real-world needs of security analysts, incident responders and threat researchers across all industries. The platform is the product of a 3-year collaborative research project between the private sector, security agencies, CERTs and universities.


ACT enables advanced threat enrichment, threat analysis, visualisation, process automation, lossless information sharing and powerful graph analysis. Its modular design and APIs facilitate implementing new workers for enrichment, analysis, information sharing, and countermeasures.


Included in the platform is Scio, a component that ingests human-readable reports, like threat advisories and blog posts, and uses natural language processing and pattern matching to extract structured threat information to import to the platform. Our Github repositories also include support for information import and data enrichment from MISP, MITRE ATT&CK, VirusTotal, PassiveDNS, ShadowServer and Splunk, with more on the way.


So why build yet another threat intelligence platform?
In 2014 we set out to find a platform on the market to meet the needs of our SOC and threat intelligence team. Our requirements were not particularly unique: we needed a platform that would help us to collect and organise our knowledge of threats, facilitate analysis and sharing, and make it easy to retrieve that knowledge when needed. We spent too much time on manual processes, copy-pasting information between different systems. Much of our knowledge was in an unstructured form, like threat reports, that made it difficult and time consuming to figure out if we had relevant knowledge that could help us decide how to handle security alerts and security incidents.


Sound familiar? After evaluating the existing platforms, we concluded they could not easily be adapted to meet our requirements. In speaking with our partners, customers and the security community, we saw we were not alone and decided to research and develop a new platform: ACT.


This session will focus on threat analysis using the GUI to demonstrate how ACT can help SOC analysts, incident responders and threat analysts/hunters/researchers.

Source code: https://github.com/mnemonic-no/act


### [ADVANCED SPECTRUM MONITORING WITH SHINYSDR](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
ShinySDR is an advanced spectrum monitoring and analysis tool that allows us to monitor wide frequency ranges at high speed, while also drilling down in to interesting signals for real time analysis. These features are supplemented by OSINT data from regulatory bodies around the world. This is the tool that we are releasing as part of our "What's on the Wireless? Automating RF Signal Identification.”


### [AI VPN: A Free-Software AI-Powered Network Forensics Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [AKTAION V2 - OPENSOURCE MACHINE LEARNING AND ACTIVE DEFENSE TOOL](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Aktaion is a machine learning open source & active defense (orchestration) tool. It is on its first iteration. The tool focuses on the detection of ransomware based on machine learning techniques, independent of static-based signatures. The tool has been mentioned and featured in may respected community publications and research. On AKTAION v2 we decided to expand our approach utilizing the blending of multiple signals which we call micro behaviors to expand tool detection into PHISHING URI/URL attack delivery.


### [ANWI (All New Wireless IDS): The $5 WIDS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
ANWI is a new type of Wireless Intrusion Detection System which is based on a low cost WiFi module (ESP8266) and can be deployed at physical perimeter of the coverage area. It allows organizations which can't afford expensive WIDS solutions to protect their networks at fraction of the cost involved.

ANWI provides three layers of protection:

Detect the most commonly used WiFi attacks including Evil Twin, Jamming using de-authentication frames, attacks conducted using commonly used WiFi attack frameworks
Block unauthorized WiFi Access Points created in organization premises
Secure organizations AP by performing WiFi Geo-Fencing to prevent access outside of designated perimeter

ANWI supports standalone as well as managed mode for sending alerts. It also has ability to use separate radio for sending alerts as added resiliency.ANWI aims to fulfill the need of WIDS which is inexpensive yet can protect against most of the possible attacks. It is easy to setup and deploy and works on "fire and forget principle". Once the sensors have been configured they can be deployed across the perimeter. The sensors send heartbeat signal and in case any of the sensors goes offline an alert is generated by server. The current production version includes all the above features.


### [ARCTIC - Automated Remediation for Correlation Threat Intelligence Collections](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Arctic builds on the open-source MISP platform to enable threat intelligence based correlation of indicators of compromise using multiple sources like internally collected intelligence, intelligence filtered through free and paid feeds, cloud feeds from Guardduty and Route53,etc. and gives a relevance score to each IOC (Indicator of Compromise) which is specific to the organisation.

It uses MISP to further enrich the IOC and maps it with the MITRE TTPs which can be used to identify the suspected APTs involved in the attack


### [ASSIMILATOR](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Network Firewall configuration is difficult to automatize, vendor Firewalls have their own ways to configure Firewalls. Assimilator wraps all vendor Firewalls into one JSON REST api; from here we can easily automatize ( i.e: Python with Requests) policy configuration and route/rule lookup.


### [ATT&CK Framework: Endpoint Detection Super Powers on the Cheap with Sysmon and Splunk](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
By using the ATT&CK framework as a basis for hunting the likelihood of catching at least part of the attackers trail is significantly increased. To make use of this rich data source I will demonstrate a Threat Hunting application which will guide your investigation along all covered ATT&CK techniques.

I will release the (Mandatory Manual Learning) ThreatHunting Splunk app I've developed, which at the time of writing contains over 80 (multi)searches and over 10 dashboards leveraging summary indexes, custom visualisations and a rich set of workflow actions.
These dashboards contain overviews, threat indicators and facilitate consecutive drilldown workflows to help the analyst determine whether this is a threat or not and also provides a whitelisting option for false positives.

Knowledge is power; the workflow has been intentionally built on generic searches to cover all attack variations, in the beginning this will generate quite some false positives. It might not appear so but this is a great thing, it will teach the hunters a great deal about their environment and therefore over time they'll be more efficient in detecting malicious behavior.


### [ATT&CK Simulator](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
This project provides a set of tooling for repeatedly executing and detecting adversary techniques in order to improve detection engineering. This project uses the MITRE ATT&CK Enterprise techniques taxonomy and the MITRE ATT&CK navigator web app. Once set up, you will be able to repeatedly execute specific techniques, observe the resulting events, and refine your detection rules and methodology.


### [AUTOMATED COLLECTION AND ENRICHMENT PLATFORM](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Many expensive Endpoint Detection and Response (EDR) tools are available, but the high cost and effort required to deploy agents to every host can be offputting to companies. The Automated Collection and Enrichment (ACE) Platform is an open source solution that enables agentless threat hunting in an environment (SIEM not included). This tool makes it possible for anyone to begin gathering otherwise difficult to collect host data to hunt for threats in their environment.

As consultants performing Compromise Assessments, we rarely have the authority or ability to alter a customer's environment to support assessment operations. Actions like enabling Windows Remote Management (WinRM) can require levels of bureaucracy and take months to accomplish. It is also difficult to answer questions surrounding systems running OSX and Linux. By removing a few of our assumptions, we created ACE, an ASP.NET Web Application that not only allows the scanning of Windows, Linux, and MacOS machines, but also provides scan management with features like Scheduling, Credential Management, and File Downloading.

In addition to running scripts and collecting scan data, ACE provides a robust enrichment and ingestion pipeline. Users can easily create individual enrichments in ACE to integrate their favorite data sources, such as hash lookups, IP reputation, sandboxing. The enrichment details can be integrated with original results to create the finalized data types in one object. With a final enrichment, the robust data set can be sent directly to a waiting SIEM for analysis. ACE provides an easy and customizable solution for threat hunters to gather and enrich data before it ever reaches the SIEM, enabling more advanced analysis.


### [AVCLASS++: Yet Another Massive Malware Labeling Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Addressing malware threats requires constant efforts to create and maintain a dataset. Especially, labeling malware samples is a vital part of shepherding a dataset. AVCLASS, a tool which takes as input VirusTotal reports and returns labels that aggregates scan results of multiple anti-viruses, is one of the most well-used oracles in both academia and industry.

However, AVCLASS often suffers from the following drawbacks. First, AVCLASS is prone to fail labeling samples that have just been posted to VirusTotal because only a few anti-viruses give labels to such samples. An inconvenient truth: when we provided AVCLASS with 20,000 VirusTotal reports, half of them could not be labeled. Second, AVCLASS cannot determine if the label is randomly generated (as with domain generation algorithms of malware) or not. Some anti-viruses that VirusTotal has worked with after AVCLASS released were labeled with the DGA, resulting in a biased label. Because of them, we are forced to make a lot of manual, tedious intervention in malware labeling (otherwise, we need to drop samples with inconsistent labels from the dataset).

In this session, we present AVCLASS++, an open-source successor of AVCLASS. AVCLASS++ is carefully designed to address these drawbacks by arming with label propagation and DGA detection. We shall describe these techniques and demonstrate that AVCLASS++ can perform labeling more accurately than the vanilla one. Users of the vanilla AVCLASS can use AVCLASS ++ with the almost same command-line options as before. Even if you have never used AVCLASS, the use of AVCLASS++ is quite easy -- just prepare a malware sample and VirusTotal report, and give them as arguments. We envision that AVCLASS++ supports both practitioners (such as SOC operators, CSIRT members, and malware analysts) and academic researchers, and thus contributes to the further development of prompt security operation and reproducible security research.


### [An Easy ATT&CK-Based Sysmon Hunter Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
This tool delivers a more effective way to APT hunt and IR, and make it even easier to discover un-attributed attacks. Our goal is below:

Find evidence of any phase in cyber attack lifecycle based on the large amount of event logs.
Help to recover the probable ways of intrusion.
We'd like to view APT threat in its whole lifecycle, not just malware, tools and infrastructures.

The next step was to do some research on APT threat hunting, based on incident data analyzing. Our basic concept uses some widely known and classic theory, like ATT&CK and Threat Intelligence. We then tried more practical ways of processing and analyzing incident data and built our own model. The core of this topic will teach you how we standardized data and filtered abnormal behavior, and three major analysis model in our practice, Time-line analysis, Graphic analysis, Statistic analysis. Finally, we will show the practiced cases on some APT group and post-exploitation tools.

Source Code: https://github.com/baronpan/SysmonHunter


### [An Open Stack for Threat Hunting in Hybrid Cloud With Connected Observability](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
We present a cloud-native threat hunting architecture built on open-source technologies. The security architecture integrates SysFlow and Kestrel to provide connected endpoint observability, edge analytics, and a cyber-reasoning stack that enables threat hunters to quickly and uniformly perform threat hunting and investigation across cloud and premise environments. This facilitates a new threat discovery methodology in which declarative hunting flows automate the search for behavioral attack patterns and indicators of compromise in telemetry data streams that are automatically tagged with attack TTPs. We show how these two open-source frameworks can deploy and scale natively on cloud environments to discover attacks and security breaches against cloud services and container infrastructures.

SysFlow is an open observability framework that lifts and normalizes the representation of system activities into a compact entity-relational format that records workload behaviors by connecting single-event and volumetric flow representations of process control flows, file interactions, and network communications. It drastically reduces data footprints over existing approaches and is particularly suitable for large scale cloud-wide monitoring and forensic investigation of sophisticated cyber-attacks that may not be discovered for long periods of time.

Kestrel is a threat hunting language for creating composable, reusable, and shareable hunt flows. It brings two key innovations to the security community: (i) a composable way of expressing hunting knowledge for threat hypothesis development and reasoning over entity-relational data abstractions, and (ii) an open-source language runtime to compute how to perform hunting steps and execute them in a distributed fashion at the local hunting site, remote data sources, and in the cloud.

We will demonstrate through live threat hunting scenarios how the two open-source projects can help create a powerful open platform for gaining operational awareness and alleviating key pain points in integrating security solutions into a "single-pane-of-glass" for effective and shareable threat hunting in the cloud.


### [AndroCop: One Click Forensic Investigation & Data Extraction Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
AndroCop is a powerful and streamlined tool for in-depth forensic analysis and data extraction from Android devices, delivering rapid insights and efficient data export. The application, written in Java, streamlines the process of forensic investigation and data retrieval, eliminating the need for external utilities.

With a single click, AndroCop aggregates and exports a diverse array of data, encompassing call records, text messages, contacts, application usage records, device information, image captures, and screenshots. The tool enriches forensic investigation by facilitating the identification of potentially harmful Android applications, deciphering app usage patterns, extracting valuable call history insights, and revealing visited locations.

Moreover, AndroCop helps users to export forensic findings and data in multiple formats such as PDFs, XLSX spreadsheets, and CSV files. All the gathered information, along with images and other related data, will be consolidated into a singular ZIP file, streamlining the process of smooth data transmission. The gathered content is placed in the AndroCop directory within the internal storage, prepared for effortless transfer whenever required.

AndroCop is also designed to be user-friendly, with a simple and intuitive interface that makes it easy to use for both novice and experienced users. It helps users quickly extract and analyze data from Android devices, making it an important addition to any forensic investigator's toolkit.


### [AntiSquat - An AI-Powered Phishing Domain Finder](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
If you host a domain on the internet representing an individual or organization, chances are that there exists a phishing domain designed specially to attack the users of your product or website.
AntiSquat is an AI-Powered typo-squatting domain finder that checks for phishing domains based on misspellings. It has a flagging system that leverages a combination of Machine Learning Models as well as various other checks such as web page similarity matching. These are performed in real-time on the target domain, thus making sure that the results are impactful.


### [Ares](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [Art of Dancing with Shackles: Best Practice of App Store Malware Automatic Hunting System](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
We all know the iOS system from Apple to be one of the most secure among all popular operating systems. From a technical view, the protection feature of sandbox gardened application, runtime code signing check, hardware level application code packing protection and so forth, and Apple Store security check policy is extremely strict - before any application is released on Apple Store.

However, this is bad news for security vendors, for the defense protection solution has no chance being granted sufficient privilege to detect and defeat attacks in deep level, when end user suffered real APT attack such as PEGASUS. Our tools is aimed at introducing the tricks and lessons of Apple Store apps automatic crawling and security sandbox automatic analysis systems for security researchers and security vendors in the world.

Source Code: https://github.com/dongyangwu/iOS-AppStore-Malware-Automatic-Hunting-System


### [Attack Surface Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [BLACKPHENIX: Malware Analysis + Automation Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Various approaches have been developed through the years for malware analysis and vary from static, dynamic, behavioral, network, memory, and automated. Each analyst has developed his/her own strategy when analyzing malware. However, the accuracy of the results relies densely on their knowledge of system internals, analytical skills, and even reverse engineering. Therefore, novice analysts generate a strict dependency on experienced people to ensure the proper delivery of threat reports.

Even experienced analysts and reverse engineers could miss critical details, such as unexplored code paths, a specific or new self-defense mechanism, a challenging obfuscation algorithm difficult to decipher quickly, or hidden data that was not revealed in early stages. All of this is due to time constraints or a potential lack of information tracking throughout the analysis process.

BLACKPHENIX performs an Intelligent Automation and Analysis by combining all the known malware analysis approaches, automating the time-consuming stages and counter-attacking malware behavioral patterns. The objective: generate precise IOCs by revealing the real malware purpose and exposing its hidden data and related functionalities that are used to exfiltrate or compromise the user's information.

This framework focuses on consolidating, correlating, and cross-referencing the data collected between analysis stages by the execution of Python scripts and helper modules, providing full synchronization between the debugger, disassembler, and supporting components. The automation modules allow interaction with external tools and libraries that can be used to scale the framework functionality by developing plug-ins on top of it, allowing people of any skill level adapt it to their needs and producing actionable threat information in the shape of technical threat reports, IPS/AV signatures or the discovery of new malware attacks, variants or families.

The presentation will include a live demo of the system processing real different categories of malware taken from the wild.


### [Beagle: Accelerating Incident Response With Graphs](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Beagle is a tool which aims to accelerate an analyst's ability to respond to incidents by allowing them to quickly and reliably generate incident response oriented graphs from a variety of data sources.

Beagle takes, as input, a wide variety of types of data:

Host based logs such as FireEye HX, Sysmon or security event logs.
Full memory images (using volatility).
Sandbox reports such as Cuckoo.
Streamed data from your SIEM.

Beagle also supports inserting alert nodes into your graphs. For example, FireEye HX triages will contain an alert, and the process which it has alerted on. Beagle will automatically insert an alert node, and create the edge between the alert node and what it alerted on.

In Beagle's web interface, analysts can select the data they uploaded and quickly work through the incident. If an alert node is present, the graph will automatically focus on the context around that node based on what the alert node has an edge to, allowing analysts to extremely quickly pivot through an incident. Analysts can pivot between nodes using simple clicks, as well as remove and search for nodes. Additionally, the graphs can be transformed into rooted trees, or seen as timelines (based on what is currently visible in the graph).

Beagle is also easily extended. Do you have a unique data source not yet supported? Implement 7 functions and Beagle will support it. Graph algorithms can also be implemented using networkx, and can be automatically run when a graph is viewed in the browser, allowing you to even further speed up your incident response time.

Beagle: https://github.com/yampelo/beagle


### [BlueHound](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
BlueHound helps blue teams pinpoint the security issues that actually matter. By combining information about user permissions, network access and unpatched vulnerabilities, BlueHound reveals the paths attackers would take if they were inside your network


### [Botnet Simulation Framework (BSF)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
In the arms race between botmasters and defenders, the botmasters have the upper hand, as defenders have to react to actions and novel threats introduced by botmasters. The Botnet Simulation Framework (BSF) addresses this problem by leveling the playing field. It allows defenders to get ahead in the arms race by developing and evaluating new botnet monitoring techniques and countermeasures. This is crucial, as experimenting in the wild will interfere with other researchers and possibly alert botmasters.

BSF allows realistic simulation of peer-to-peer botnets to explore and study the design and impact of monitoring mechanisms and takedown attempts before being deployed in the wild. BSF is a discrete event botnet simulator that provides a set of highly configurable (and customizable) botnet features including:
- realistic churn behavior
- variable bot behavior
- monitoring mechanisms (crawlers and sensors)
- anti-monitoring mechanisms

Moreover, BSF provides an interactive visualization module to further study the outcome of a simulation. BSF is aimed at enabling researchers and defenders to study the design of the different monitoring mechanisms in the presence of anti-monitoring mechanisms [1,2,3]. Furthermore, this tool allows the users to explore and understand the impact of design choices of botnets seen to date.

[1] Leon Böck, Emmanouil Vasilomanolakis, Jan Helge Wolf, Max Mühlhäuser: Autonomously detecting sensors in fully distributed botnets. Computers & Security 83: 1-13 (2019)
[2] Leon Böck, Emmanouil Vasilomanolakis, Max Mühlhäuser, Shankar Karuppayah: Next Generation P2P Botnets: Monitoring Under Adverse Conditions. RAID 2018: 511-531
[3] https://www.blackhat.com/eu-17/briefings.html#i-trust-my-zombies-a-trust-enabled-botnet


### [Bro: Do You Bro? Beginner to Expert](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The Bro Network Security Monitor is an open-source framework that gives total visibility over network traffic in real-time. Since most cyber attacks cross the network (and hosts themselves can be compromised), threat hunters and incident responders typically rely on network data as a vital source of truth, to reconstruct what really happened (or is happening now) in their environment. Bro is perhaps the best and most widely used tool for network traffic analysis. Join us to learn more about Bro with Seth Hall, longtime Bro developer, and see a demo where he will provide a comprehensive overview of Bro, from introduction to advanced custom scripting.


### [CASPR - Code Trust Audit Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
With CASPR, we are addressing the Supply Chain Attacks by Left Shifting the code signing process.
CASPR aims to provide simple scripts and services architecture to ensure all code changes in an organization are signed by trusted keys; trustability of these keys should be instantly verifiable every time the code changes are consumed. It also makes the auditing and accountability of code-changes easier and cryptographically verifiable, leaving no scope for malicious actors to sneak in untrusted code at any point in the Software Development Life Cycle.


### [CASPR - Code Trust Auditing Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
CASPR is known for addressing the Supply Chain Attacks by Left Shifting the code signing process.
CASPR provides simple scripts and services architecture to ensure all code changes in an organisation are signed by trusted keys. What matters is where these keys are residing. Storing signing keys on a user's device has a certain degree of risk when the device is compromised.

In the latest release of CASPR, we are enabling developers to sign code commits from the keys stored on the phone.

CASPR makes the auditing and accountability of code-changes easier and cryptographically verifiable, leaving no scope for malicious actors to sneak in untrusted code at any point in the Software Development Life Cycle.


### [CCAT: Cisco Config Analysis Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
CCAT is designed for finding security misconfigurations in Cisco devices. It generates a detailed report with explanations and tips on fixing the issues. We will implement an option to automatically fix those issues in one of our next updates.

Presentation: https://drive.google.com/file/d/1kEB7dEe4uIkfxWuKgGDYTJly_spEVaO-/view
GitHub: https://github.com/cisco-config-analysis-tool/ccat


### [CHIRON: Home-Based Network Analytics & Machine Learning Threat Detection Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
CHIRON is an open-source ELK based analytics and Machine Learning framework that applies security analytics to home network traffic and for dynamic learning of indicators of external threats and other potential malicious activity. The tool continuously monitors network traffic and applies machine learning techniques for adaptive discovery and baselining of a small user population.

Use cases include:

Identification of assets in home network (IoTs, workstations, laptops, servers, routers)
Fingerprints users, services, and protocols
Applies analytics to users and devices (average session length, traffic, visited sites) to determine standard usage behavior and service profiles


### [CHKROOTKIT: EATING APTS FOR BREAKFAST SINCE 1997](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Chkrootkit is a suite of posix shell script and some tools written in ansi C. It works like a charm in virtually all Unix environment without extra dependencies. It is able to detect sereval rootkits, malicios activity (some APTs included) and can do post-mortem forensics analysis to detect malicious kernel modules activities and stuff like that. This tool currentlly detects ~70 known Rootkits, Worms and many malicious activities.


### [CNAPPgoat: A Multicloud Open-Source Tool for Deploying Vulnerable-by-Design Cloud Resources](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
CNAPPgoat is a CLI tool designed to deploy vulnerable-by-design cloud infrastructure.

The tool is designed to modularly provision intentionally vulnerable components in cloud environments with simple commands: launch a container with a crypto-miner installed, spawn a machine with a vulnerable image, create a public IAM role, and many more scenarios.

These capabilities empower defenders to test their protective strategies, tools, and procedures, and for offensive professionals to refine their skills and tooling. Instead of trusting their systems and procedures to prevent risk, they can manufacture risk in a controlled environment to verify that they actually do.


CNAPPgoat supports modular deployment of various vulnerable scenarios and is a multi-cloud tool. CNAPPgoat is built on Pulumi and supports multiple programming languages. It operates as a CLI tool, requiring no specific IaC expertise, enabling a wide range of professionals to deploy and monitor environments.

CNAPPgoat helps:
* Security professionals create sandboxes to test their teams, procedures, and protocols
* Pentesters use it to provision a "shooting range" to test their skills at exploiting the scenarios and developing relevant capabilities
* Security teams benchmark CNAPP solutions against known environments to prove their ability to deliver what they promise
* Instructors create vulnerable environments for hands-on workshops or chalk talks
* Educators create learning environments where cloud infrastructure risks can be explored, understood - and avoided


### [CQData: Data Extraction & Forensic Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
CQData Toolkit enables you to perform extraction of data that can be extremely useful during the investigation and incident. One of the most important things to learn during the incident is to learn the identity connected with the attack and also become familiar with hacker's actions through the detailed process tracking. CQData can extract information from the Automatic Destinations, generate a timeline, convert Automatic Destination into useful lists of processes, recover files, extract information from the configuration, calculate the vector of the attack based on the process related information and search across other affected computers, decode encrypted users' data, find encrypted data on the computer and display its characteristic, search for confirmation that logs were not manipulated with etc. It is a toolkit that authors use during the incident investigation. Toolkit was created with one purpose, to address the gaps in the evidence analysis and data collection tools. CQData also leverages the reverse engineering research done in the DPAPI area and our recent 1-year research in the Automatic Destinations area.


### [CQSysmon Toolkit: Advanced System Monitoring Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Our toolkit has proven to be useful in the 25000 computers environment. It relies on a free Sysmon deployment and its goal is to boost information delivered by the original tool. CQSysmon Toolkit allows you to extract information about what processes have been running in the operating system, get their hashes and submit them into Virus Total for the forensic information about the malware cases. It also allows to extract information into spreadsheet about what types of network connections have been made: what is the destination IP address, which process was responsible for it and who is the owner of IP. The toolkit also allows to extract information about the current system configuration and compare it with the other servers and much more that allows to become familiar of what is going on in your operating system. There is a special bonus tool in a toolkit that allows to bypass some parts of the Sysmon with another tool that allows to spot that situation so that everything stays in control. CQSysmon Toolkit allows you to established detailed monitoring of the situation on your servers and it is a great complement to the existing forensic tools in your organization.


### [CQSysmonToolkit: Advanced System Monitoring Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Our toolkit has proven to be useful in the 25000 computers environment. It relies on a free Sysmon deployment and its goal is to boost information delivered by the original tool. CQSysmon Toolkit allows you to extract information about what processes have been running in the operating system, get their hashes and submit them into Virus Total for the forensic information about the malware cases. It also allows to extract information into spreadsheet about what types of network connections have been made: what is the destination IP address, which process was responsible for it and who is the owner of IP. The toolkit also allows to extract information about the current system configuration and compare it with the other servers and much more that allows to become familiar of what is going on in your operating system. There is a special bonus tool in a toolkit that allows to bypass some parts of the Sysmon with another tool that allows to spot that situation so that everything stays in control. CQSysmon Toolkit allows you to established detailed monitoring of the situation on your servers and it is a great complement to the existing forensic tools in your organization.


### [CUCKOODROID](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
To combat the growing problem of Android malware, I present Cuckoodroid - a solution based on the popular open source framework Cuckoo Sandbox to automate the malware investigation process. Cuckoodroid enables the use of Cuckoo's features to analyze Android malware and provides new functionality for dynamic and static analysis. Cuckoodroid is an all-in-one solution for malware analysis on Android. It is extensible and modular, allowing the use of new - as well as existing - tools for custom analysis.

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


### [Cloud Security Suite: One Stop Tool for AWS/GCP/Azure/DigitalOcean Security Audit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Nowadays, cloud infrastructure is pretty much the de-facto service used by large/small companies. Most of the major organizations have entirely moved to cloud. With more and more companies moving to cloud, the security of cloud becomes a major concern.

While AWS, GCP, Azure, and DigitalOcean provide you protection with traditional security methodologies and have a neat structure for authorization/configuration, their security is as robust as the person in-charge of creating/assigning these configuration/policies. Also, the massive scale at which cloud services are adopted in enterprises, merged with inevitability of human error, often leads to catastrophic damages to the business.

Few vulnerable scenarios:
- Security groups/policies, password policy or IAM policies are not configured adequately
- S3 buckets and Azure blobs are world-readable
- Web servers are supporting vulnerable SSL ciphers
- Ports exposed to public with vulnerable services running
- If root credentials are used
- Logging or MFA is disabled
And many more such scenarios...

Knowing all this, audit of cloud infrastructure becomes a hectic task! There are a few open source tools which help in cloud auditing however none of them provides an exhaustive checklist. Also, setting up all the tools and looking at different result sets is a redundant task. While managing massive infrastructures, system audit of server instances is a challenging task as well.

Cloud Security Suite (CS Suite) is a one stop tool for auditing the security posture of the AWS/GCP/Azure/DigitalOcean infrastructures along with server audit feature. CS Suite leverages capabilities of current open source tools and has plethora of custom checks into one tool to rule them all.


### [Cloud Security Suite: One Stop Tool forAWS/GCP/Azure Security Audit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
While AWS, GCP & Azure provide protection with traditional security methodologies and have a neat structure for authorization/configuration, their security is as robust as the person in-charge of creating/assigning these configuration policies. As we all know, human error is inevitable and any such human mistake could lead to catastrophic damage to the environment.

Few vulnerable scenarios:

Your security groups/policies, password policy or IAM policies are not configured properly
S3 buckets and Azure blobs are world-readable
Web servers supporting vulnerable ssl ciphers
Ports exposed to public with vulnerable services running on them
If root credentials are used
Logging or MFA is disabled
And many more scenarios...

Knowing all this, audit of cloud infrastructure becomes a hectic task! There are a few open source tools which help in cloud auditing but none of them have an exhaustive checklist. Also, collecting, setting up all the tools and looking at different result sets is a painful task. Moreover, while maintaining big infrastructures, system audit of server instances is a major task as well.

CS Suite is a one stop tool for auditing the security posture of the AWS/GCP/Azure infrastructures and does OS audits as well. CS Suite leverages current open source tools capabilities and has custom checks added into one tool to rule them all.


### [Cloud Security Suite: One-Stop Tool for AWS/GCP/Azure Security Audit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Nowadays, cloud infrastructure is pretty much the de-facto service used by large/small companies. Most of the major organizations have entirely moved to cloud. With more and more companies moving to cloud, the security of cloud becomes a major concern.

While AWS, GCP & Azure provide you protection with traditional security methodologies and have a neat structure for authorization/configuration, their security is as robust as the person in-charge of creating/assigning these configuration/policies. Also, the massive scale at which cloud services are adopted in enterprises, merged with inevitability of human error, often leads to catastrophic damages to the business.

Few vulnerable scenarios:

Security groups/policies, password policy or IAM policies are not configured adequately
S3 buckets and Azure blobs are world-readable
Web servers are supporting vulnerable SSL ciphers
Ports exposed to public with vulnerable services running
If root credentials are used
Logging or MFA is disabled
And many more such scenarios...

Knowing all this, audit of cloud infrastructure becomes a hectic task! There are a few open source tools which help in cloud auditing however none of them provides an exhaustive checklist. Also, setting up all the tools and looking at different result sets is a redundant task. While managing massive infrastructures, system audit of server instances is a challenging task as well.

CS Suite is a one stop tool for auditing the security posture of the AWS/GCP/Azure infrastructures along with server audit feature. CS Suite leverages capabilities of current open source tools and has plethora of custom checks into one tool to rule them all.


### [Cloud Sniper](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Cloud Sniper is a platform designed to manage Cloud Security Operations, intended to respond to security incidents by accurately analyzing and correlating cloud artifacts. It is meant to be used as a Cloud Security Operations platform to detect and remediate security incidents by showing a complete visibility of the company's cloud security posture.

It introduces a centralized Incident and Response platform, which executes automatic actions, by learning from the analysts' expert knowledge. To do it, only native cloud artifacts and open source technologies are implemented. In this way, the community can extend the project with different security use cases.

Cloud Sniper receives and processes security feeds, providing an automatic response mechanism to protect the cloud infrastructure. To detect attackers' advanced TTPs, Cloud Sniper Analytics module correlates IOCs providing enhanced security findings to the security analyst.

With this platform, you get a complete and comprehensive management system of the security incidents. At the same time, an advanced security analyst can integrate Cloud Sniper with external forensic or incident-and-response tools to ingest new security feeds. The platform automatically deploys and provides cloud-based integration with all native resources, in a fully modularized manner, making it very easy to extend for the community.

Cloud Sniper introduces an analytics module to analyze data, metrics and telemetry generated on the cloud. This first version analyzes VPC flows to detect beaconing patterns.

As part of the platform, we have developed two modules to complement it:

* Cloud Droid (Incident and Response Simulations): Currently, incident and response teams develop different mechanisms to detect attacks, leaving aside the testing phase. Although each automation is tested before implementation, it is not constantly monitored. Droid proposes an automated testing model in which controlled actions are expected to be triggered to perform security incident simulations.

* Cloud Lusat (Internal Threat Intelligence Feeds, Inventory and Compliance Data Collection): It aims to process information based on threat intelligence feeds, generate an inventory and check the compliance of different cloud resources.


### [CornerShot: Gaining Foresight in Restrictive Networks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Legacy internal networks are usually flat, simple for a red team to cut through, and difficult for blue teams to defend. To fix this problem, modern networks apply zero trust access and network segmentation. This new paradigm presents new challenges not only to attackers but to defenders as well.

In such environments, visibility becomes crucial. Which computers can access others and be viable candidates for lateral movement? This question is certainly troubling attackers and red teams, but also defenders and blue teams looking to identify and defend such key network paths.

CornerShot utilized a novel technique to discover network access between two remote hosts, without requiring privileged access to those hosts. In modern warfare CornerShot is a weapon that allows a soldier to look past a corner (and possibly take a shot), without actually risking exposure. Similarly, the CornerShot capability allows one to look at another hosts' network access non-intrusively, without risking exposure.

CornerShot relies on several, well documented, standard Remote Procedure Call (RPC) methods that are used by various Microsoft services. By using methods that only require a non-privileged authenticated account in the domain, CornerShot is able to trigger network traffic from a destination host to a target. Once traffic is generated, CornerShot is able to determine the remote's port state by measuring the time an RPC call took, and the response it received from the destination host.

We will demonstrate real world applications, for example: how to scan an entire network access from a single deployment of CornerShot, and how to validate which BloodHound paths are practical given the underlying network access.


### [CrackQ: Intelligent Password Cracking](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
CrackQ is, first and foremost, a Python based queuing system for managing hash cracking using Hashcat. There are several tools available for this purpose, CrackQ was born from the frustration of using these tools on a daily basis. It adds some new and interesting additional features as solutions to these frustrations. CrackQ is essentially a REST API with clients in the form of a Python CLI tool and a web GUI. The API design is very stable and works very reliably as a platform to use for day-to-day password cracking within an offensive-security team. The tool is designed to be easy to install and comprises of currently 4 docker images, built on production ready containers segregating each component, all controlled seamlessly using docker-compose. The tool will also include detailed analysis/reporting with graphs representing a multitude of metrics and automated "intelligent" cracking using various pre-existing techniques and machine learning solutions. The tool will be released open-source in the coming months.


### [CrowdSec - the network effect of cybersecurity](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Discover CrowdSec, an open-source and collaborative intrusion prevention and detection system relying on IP behavior analysis and IP reputation. CrowdSec analyzes visitor behavior & provides an adapted response to all kinds of attacks. The solution also enables users to protect each other. Each time an IP is blocked, all community members are informed, so they can also block it. Already used in 160+ countries, the solution builds a crowd-sourced CTI database to secure individuals, companies, institutions etc. The recent release of CrowdSec Security Engine 1.5 brings new features to the table:
- Polling API Integration
- Real-time decisions management
- New Blocklist API and Premium Blocklists
- Kubernetes audit acquisition
- S3 audit acquisition
- Auditd support
- CrowdSec CTI API helpers
- AWS Cloudtrail Scenarios


### [CrowdSec: The Open-Source and Participative IPS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [CureIAM: The Ultimate Solution to Least Privilege Principle Enforcement on GCP](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
CureIAM is an easy-to-use, reliable, and performant engine that enables DevOps and security teams to quickly clean up over-permissioned IAM accounts on GCP infrastructure. By leveraging GCP IAM Recommender APIs and the Cloudmarker framework, CureIAM automatically enforces least privilege principle on a daily basis, and helps to ensure that only the necessary permissions are granted to GCP accounts.

Key Features

- Config driven workflow for easy customization
- Scalable and production-grade design
- Embedded scheduling for daily enforcement
- Plugin-driven architecture for additional functionality
- Track actionable insights and records actions for audit purposes
- Scoring and enforcement of recommendations to ensure safety and security


### [CyBot: Open-Source Threat Intelligence Chat Bot (Full Circle)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Threat intelligence chat bots are useful friends. They perform research for you and can even be note takers or central aggregators of information. However, it seems like most organizations want to design their own bot in isolation and keep it internal. To counter this trend, our goal was to create a repeatable process using a completely free open source framework, an inexpensive Raspberry Pi (or even virtual machine), and host a community-driven plugin framework to open up the world of threat intel chat bots to everyone from the average home user to the largest security operations center.

We were thrilled to debut the end result of our research (a chat bot that we affectionately call CyBot) at Black Hat Arsenal Vegas 2017. To build on that momentum we also brought CyBot to Black Hat Europe and Asia to gather more great feedback and ideas from an enthusiastic international crowd. This year's Black Hat Vegas will allow us to share new features that stemmed from Black Hat Asia feedback as well as lessons learned from the global collaboration effort.

Best of all, if you know even a little bit of Python, you can help our collaboration efforts by writing plugins and sharing them with the community. If you want to build your own CyBot, the instructions in this project will let you do so with about an hour of invested time and anywhere from $0-$35 in expenses. Come make your own threat intelligence chat bot today!


### [CyBot: Open-Source Threat Intelligence Chat Bot (Platform Enhanced)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Threat intelligence chat bots are useful friends. They perform research for you and can even be note takers or central aggregators of information. However, it seems like most organizations want to design their own bot in isolation and keep it internal. To counter this trend, our goal was to create a repeatable process using a completely free open source framework, an inexpensive Raspberry Pi (or even virtual machine), and host a community-driven plugin framework to open up the world of threat intel chat bots to everyone from the average home user to the largest security operations center.

We were thrilled to debut the end result of our research (a chat bot that we affectionately call CyBot) at Black Hat Arsenal Vegas 2017. To build on that momentum we also brought CyBot to Black Hat Europe and Asia to gather more great feedback and ideas from an enthusiastic international crowd. This year's Black Hat Vegas will allow us to share new features that stemmed from Black Hat feedback as well as enhancements provided by a platform upgrade.

Best of all, if you know even a little bit of Python, you can help our global collaboration efforts by writing plugins and sharing them with the community. If you want to build your own CyBot, the instructions in this project will let you do so with about an hour of invested time and anywhere from $0-$35 in expenses. Come make your own threat intelligence chat bot today!


### [DARWIN: Real World Use Cases for Covert Wireless](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
DARWIN is a result of an evolution of our covert channel research, where we considered use case of covert channel to facilitate an unmanaged chat in the local radio periphery. DARWIN can be divided into three parts viz., 1. Scripts for covert traffic 2. Mechanism to consume and push the data on terminal (presently we are considering terminal for input and output of the chat messages) 3. Integration (to consume the input from terminal and fit it into the requisite location in IEEE 802.11/IEEE 802.15.4 data link layer frame to ship it over the air and vice versa).


### [Deep Information Retrieval for Malware Searching System](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
More than 300,000 new malware samples are generated everyday, and it is well known that traditional malware detection based on file hash and rules is very vulnerable to variants. It is also getting harder to categorize unknown malware samples because the cost of finding similar samples is increasing. Therefore, the necessity of malware information retrieval system has emerged. Several attempts have been researched to perform this task, but they have limitations in terms of polymorphism, complexity, ambiguity, novelty and so on.

This research seeks to remedy these problems by introducing a deep metric learning method and proposes a new malware retrieval system which has learned a semantic similarities of malware samples. This system could retrieve information from perceptually similar samples as well as structurally similar samples. It could deal with new samples rapidly and roles as a good feature extractor for another tasks like malware classification or categorization. This approach can be easily adapted to other neural network models because it doesn't change the structure of the original network.

In this presentation, we describe the problems that arise when creating a malware retrieval system, and how we solve them. Also we visualize the embedding vectors of malware samples and show the retrieval results to prove the synchronization between our perception on malware and embedding space.


### [DeepViolet: SSL/TLS Scanning API & Tools](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
DeepViolet TLS/SSL scanner is an information gathering tool to test TLS/SSL configuration on secure web servers. DeepViolet is an API written in Java. Two proof of concept tools implement the API to demonstrate DeepViolet running from the command line or alternatively from a desktop application. Features of DeepViolet include enumeration of web server cipher suites, display X.509 certificate metadata, examine X.509 certificate trust chains, user configurable ciphersuite naming conventions and more. DeepViolet is an OWASP open source project written to help educate the technical community around TLS/SSL and strengthen knowledge of security protocols while strengthen security of web applications. DeepViolet project is always looking for volunteers.

Source Code: https://github.com/spoofzu/DeepViolet


### [Defending software development ecosystems with Safe Package](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
With typosquatting, with account takeover, and with dependency hijacking attackers are using malicious packages to target our deployment pipelines. They mimic popular packages like Material Tailwind, hijack popular dependencies like event-stream, and compromise privileged accounts. This talk explains these classes of attack with examples and introduces safe-package, an open-source security wrapper for all kinds of package managers that neutralizes these attacks.


### [DejaVu ++](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
DejaVu is an open source deception framework which can be used to deploy decoys across the infrastructure. This could be used by the defender to deploy multiple interactive (Server and Client) decoys strategically across the network and cloud.

We have done massive updates to our platform (now DejaVu ++) and are excited to present these at Blackhat Europe. Some key updates:

1. Decentralized architecture to support enterprise orgs
2. Video recording of attacker's movement, record attacker's activity
3. Highly interactive decoys to engage the attacker and reveal attacker motivation and TTP
4. Integrated IDS for enriched alerts
5. Full packet capture of attacker's interaction with the decoy for forensic analysis.
6. Cloud Ready decoys
- Now blue team can deploy DejaVu instance on AWS infra
- Configure decoy personality to mimic the environment
- AWS breadcrumbs
7. Dashboard with monitoring and analysis - Full lifecycle of event can be drilled into by an analyst
8. New decoys
- Email and client side decoys to detect Spear Phishing
- RDP Interactive and Non-Interactive
- Interactive SSH
- Detect MITM attacks : ARP Poisoning, Responder, SSDP
- HONEYCOMB (To capture events from Honey Docs)
- Beaconing Documents
- ICS/SCADA Decoys - Modbus and S7COMM
9. Personalized threat inteligiance - Deploy customised decoys on DMZ to detect targeted threats
10. Logging Capability - Ship logs to SIEM or other platforms using Syslog capability

https://github.com/bhdresh/Dejavu


### [DejaVu: An Open Source Deception Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Deception techniques - if deployed well - can be very effective for organizations to improve network defense and can be a useful arsenal for blue teams to detect attacks at very early stage of cyber kill chain. But the challenge we have seen is deploying, managing and administering decoys across large networks is still not easy and becomes complex for defenders to manage this over time. Although there are a lot of commercial tools in this space, we haven't come across open source tools which can achieve this.

With this in mind, we have developed DejaVu which is an open source deception framework which can be used to deploy across the infrastructure. This could be used by the defender to deploy multiple interactive decoys (HTTP Servers, SQL, SMB, FTP, SSH, client side – NBNS) strategically across their network on different VLAN's. To ease the management of decoys, we have built a web-based platform which can be used to deploy, administer and configure all the decoys effectively from a centralized console. Logging and alerting dashboard displays detailed information about the alerts generated and can be further configured on how these alerts should be handled. If certain IP's like in-house vulnerability scanner, SCCM etc. needs to be whitelisted, this can be configured which effectively would mean very few false positives.

Alerts only occur when an adversary is engaged with the decoy, so now when the attacker touches the decoy during reconnaissance or performs authentication attempts this raises a high accuracy alert which should be investigated by the defense. Decoys can also be placed on the client VLAN's to detect client side attacks such as responder/LLMNR attacks using client side decoys. Additionally, common attacks which the adversary uses to compromise such as abusing Tomcat/SQL server for initial foothold can be deployed as decoys, luring the attacker and enabling detection.


### [Detecting Linux Kernel Rootkits with Tracee](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Linux Kernel Rootkits is an advanced and fascinating topic in cyber security. These tools are stealthy and evasive by design and often target the lower levels of the OS, unfortunately, there aren't many solid security tools that can provide extensive visibility to detect these kinds of tools.

Tracee is a Runtime Security and forensics tool for Linux, utilizing eBPF technology to trace systems and applications at runtime, analyze collected events to detect suspicious behavioral patterns and capture forensics artifacts.

Tracee was presented in BH EU 2020 and BH USA 2021. Thus far we have presented Tracee-ebpf and spoken about its passive capabilities to collect OS events based on given filters, and Tracee-rules, which is the runtime security detection engine. But Tracee has another capability to safely interact with the Linux kernel, which grants Tracee even more superpowers.

Tracee was designed to provide observability of events in running containers. It was released in 2019 as an OSS project, allowing practitioners and researchers to benefit from its capabilities. Now, Tracee has greatly evolved, adding more robust and advanced capabilities. Tracee is a runtime security and forensics tool for Linux, built to address common Linux security issues.

For references see:

https://blog.aquasec.com/ebpf-container-tracing-malware-detection

https://blog.aquasec.com/advanced-persistent-threat-techniques-container-attacks


### [Detecting Typo-Squatting, Backdoored, Abandoned, and Other "Risky" Open-Source Packages Using Packj](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Software supply chain attacks on open-source software ecosystems, particularly on popular package managers such as NPM, PyPI have increased tremendously in the last few years. Today, developers must thoroughly analyze packages, and avoid risky packages that may expose them to high levels of supply chain risks.

But, there exists no tool to measure supply chain risks lurking in open-source packages. Current practices include sourcing only mature, stable, popular, and reputable packages, where such attributes are inferred from publicly available metrics, such as GitHub stars, package downloads, and software development activity. However, such vanity metrics do not reveal true information about the security posture of packages. More importantly, an attacker-controlled bot can easily manipulate such metrics. Manually vetting hundreds of dependencies is infeasible.

In this talk, we will present our open-source command line vetting tool, called Packj that allows developers to easily analyze dependencies for "risky" code/attributes and provide actionable insights into their security posture. In this presentation, we will cover the technical details of our tool and discuss its usage. Packj tool powers also our large-scale security vetting infrastructure that continuously analyzes millions of published packages, and provides detailed risk assessment reports. We have already detected a number of abandoned, typo-squatting, and malicious packages. We will present our findings, highlight different types of attack techniques adopted by bad actors, and discuss measures that developers can take to thwart such attacks. With our work, we hope to enhance productivity of the developer community by exposing undesired behavior in untrusted third-party code, maintaining developer trust and reputation, and enforcing security of package managers.


### [Dissect: The Open-Source Framework for Large-Scale Host Investigations](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Dissect is an incident response framework build from various parsers and implementations of file formats. Tying this all together, Dissect allows you to work with tools named target-query and target-shell to quickly gain access to forensic artefacts, such as Runkeys, Prefetch files, and Windows Event Logs, just to name a few!

And the best thing: all in a singular way, regardless of underlying container (E01, VMDK, QCoW), filesystem (NTFS, ExtFS, FFS), or Operating System (Windows, Linux, ESXi) structure / combination. You no longer have to bother extracting files from your forensic container, mount them (in case of VMDKs and such), retrieve the MFT, and parse it using a separate tool, to finally create a timeline to analyse. This is all handled under the hood by Dissect in a user-friendly manner.

This way you spend less time with the boring processing steps and have more time doing actual analysis or research!


### [DotDumper: automatically unpacking DotNet based malware](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Analysts at corporations of any size face an ever-increasing amount of DotNet based malware. The malware comes in all shapes and forms, ranging from skittish stealers all the way to nation-state-backed targeted malware. The underground market, along with public open-source tools, provides a plethora of ways to obfuscate and pack the malware. Unpacking malware is time-consuming, difficult, and tedious, which poses a problem.

To counter this, DotDumper automatically dumps interesting artifacts during the malware's execution, ranging from base64 decoded values to decrypted PE files. As such, the malware decrypts and executes the next stage, while DotDumper conveniently provides a copy of said decrypted stage. All this is done via a simple, compact, intuitive, and easy-to-use command-line interface.

Aside from the dumped artifacts, DotDumper provides an extensive log of the traced execution, based on managed hooks. For each hook, the log contains the original function name, arguments and their values, and the return value. Since DotDumper ensures that the original function is called, the malware's execution continues as if it was executed normally, allowing the analyst to get as many stages from the sample as possible.

DotDumper can execute DotNet Framework executables, as well as dynamic link libraries, due to the fully-fledged reflective loader which is embedded. Any given function can be selected within a library, along with any required variables and their values, all easily accessible from DotDumper's command-line interface.

DotDumper has proven to be effective in dealing with the renowned AgentTesla stealer or the WhisperGate Wiper loader, allowing an analyst to easily fetch the decrypted and unpacked in-memory only stages, thus decreasing the time spent on unpacking, allowing for a faster response to the given threat.


### [Drosera: Using Wireless Honeypot to Protect Wireless Networks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Drosera is a wireless honeypot platform for discovering wireless intrusion attacks and intruders identification.

In wireless attacks, hackers are often attacking vulnerable wireless hotspots as a breakthrough. This means that a wireless network with obvious flaws will be the primary target for an attacker. When an attacker targets our wireless honeypot network, Drosera will record all actions before and after the attacker connects the network, including the process of attempting to connect to the network at the 802.11 frame level and further attacks after entering the honeypot network. Drosera can accurately identify the attack, and the first time to generate an alarm.

We are equipped with high-interactive Windows and Linux honeypots in the network, which simulate normal business systems to confuse the attacker and delay the attack process. They will also help us get information about the hacker like the goals, the attack methods, and the skill level.


### [EGRESSION](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Egression is an enterprise traffic egress control testing and ranking system. It is a command-line tool that checks an organization's ability to restrict outbound uploads of sensitive data (a file containing fake CC numbers, SSNs, National ID numbers, addresses, names, and other PII) using increasingly difficult levels (which use increasingly evasive techniques), and then provides the rating for the given organization based on how difficult it was to egress the data from the network.


### [EKTotal](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
"EKTotal" is an integrated analysis tool that can automatically analyze the traffic of Drive-by Download attacks. The proposed software package can identify four types of Exploit Kits such as RIG and Magnitude, and more than ten types of attack campaigns such as Seamless and Fobos. EKTotal can also extract exploit codes and malware. The proposed heuristic analysis engine is based on Exploit Kit tracking research conducted since 2017, and is known as team "nao_sec". EKTotal provides a user-friendly web interface and powerful automated analysis functions. Thus, EKTotal can assist SOC operators and CSIRT members and researchers.

Drive-by download attacks are still actively conducted. Such attacks are continually changing and becoming more complex. At the beginning of 2017, attack campaigns targeting compromised websites were widespread. However, majority of the current attack campaigns are based on malvertising. Furthermore, in March 2018, several Exploit Kits began to exploit the critical vulnerability named CVE-2018-4878, which in turn is a significant threat. Various tools are available for analyzing malicious traffic. However, it's necessary to employ a combination of such tools or possess their knowledge for analyzing malicious traffic. Hence, EKTotal has been developed for conducting security analysis in a simplified manner.

EKTotal is an all-in-one malicious traffic analysis and processing tool that functions by submitting files of "pcap" or "saz" format. After identifying the attack campaign and associated Exploit Kit through multiple filters, EKTotal extracts the obfuscated exploit code from the traffic data, deobfuscates it, and decrypts the encrypted malware. For example, in the case of RIG Exploit Kit, EKTotal deobfuscates multiple obfuscated JavaScript codes, extracts all exploit codes and malware decryption keys, and thereby decrypts the malware encrypted with RC4.


### [Effective Alert Triage and Email Analysis with Security Onion and Sublime Platform](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
In this workshop, we will explore the integration of two cutting-edge free and open platforms: Security Onion, a versatile solution for threat hunting, enterprise security monitoring, and log management; and Sublime Platform, an innovative open email security platform designed to prevent email attacks such as BEC, malware, and credential phishing. Sublime Platform's unique domain-specific language (DSL) enables detection-as-code, allowing for highly customizable email security detection.

Attendees will learn how to:

1. Set up and configure the integration between Security Onion and Sublime Platform, leveraging the combined strength of these tools to detect, prevent, triage, and enrich email threats.
2. Utilize Sublime Platform's DSL for detection-as-code, crafting tailored rules and policies to identify and prevent a wide range of email threats.
3. Effectively triage Sublime email alerts within Security Onion, streamlining incident response and reducing the time needed to identify and remediate threats.
4. Pivot to Sublime for in-depth investigation and analysis of suspicious emails, extracting valuable context and indicators to inform security decisions.
5. Enrich and correlate Sublime alerts with other data sources in Security Onion, such as Zeek HTTP/DNS/TLS records, Suricata alerts, and full PCAP to answer questions with network metadata such as: Did the user click on the link? Has anyone ever visited this domain or link before? And more.

By combining Security Onion's robust capabilities with Sublime Platform's innovative approach to email security, participants will gain hands-on experience in creating a comprehensive defense against email-based attacks.

Equip yourself with the knowledge and tools needed to combat the evolving landscape of email threats by attending this workshop, and take advantage of these powerful, free solutions to bolster your organization's defenses.


### [EventList](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
EventList: What the log?! So many events, so little time...
Detecting adversaries is not always easy - especially when it comes to correlating Windows Event Logs to real-world attack patterns and techniques. EventList helps to match Windows Event Log IDs with the MITRE ATT&CK framework (and vice-versa) and offers methods to simplify the detection in corporate environments worldwide.

Use this tool to:

Import either MSFT Baselines or custom GPOs
Find out immediately which Events are being generated and what MITRE ATT&CK techniques are being covered by the selected Baseline/GPO
Choose MITRE ATT&CK techniques and generate GPOs to generate the events needed for detection
Generate Agent Forwarder Configs to only cover the events needed for the detection (avoid being "Log spammed")
Generate Queries to detect the chosen MITRE ATT&CK techniques, regardless of the SIEM solution used


### [Eventpad: Rapid and Cost Effective Malware Analysis Using Visual Analytics](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The analysis of malware behavior in network activity and event logs is a costly and time-consuming task. Even with automated techniques, inspection of network traffic in tools such as Wireshark is often tedious and overwhelming due to the many packet details.

We need faster techniques to speedup the discovery of malware activity and gain insight in our event logs by combining machine learning and visualization together. To this end we developed "Eventpad - the notepad editor for event data", a tool that enables analysts to quickly analyze network traffic by exploiting the human mind. Eventpad is a visual analytics tool that enables analysts to visually inspect system events as blocks on a screen. Just like a notepad editor find&replace, conditional formatting, and rewrite functionality can be used to accurately search and highlight system vulnerabilities in these block collections. Together with automated techniques such as clustering and multiple sequence alignment analysts can quickly drill down and extract nontrivial patterns and threat indicators from network conversations and event logs.

We demonstrate how we can use Eventpad to quickly discover patterns in PCAP DPI traffic. In particular, we give live demos on how we can use the tool to discover protocol misusage in VoIP traffic and reverse engineer Ransomware viruses in back office environments.


### [FalconEye: Windows Process Injection Techniques - Catch Them All](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Process injection (PI) in Windows has been a well-known security topic for many years. It is used to gain more stealth because it does not create additional processes in the system that could attract unwanted attention from the defender. It is also used to bypass security products that have limited visibility into the injection behaviors. Since PI techniques use legitimate windows APIs, detecting them becomes a challenging task.

FalconEye provides comprehensive detection for true PI techniques in real-time. True PIs inject into target processes which are already running. Pre-execution injections such as AppInit and process hollowing are not in scope. To the best of our knowledge, we analyzed all the publicly known PI techniques and our tool is able to detect all of them without false positives during our testing.

We identify PI behavior invariants that are unique compared to benign program behaviors but are common between various PI techniques. Based on the behavior invariants, we divide PI detections into three classes:
(1) Stateless detection
(2) Stateful detection
(3) Floating code detection

We propose a comprehensive detection algorithm to detect these behavior invariants classes. Our detection algorithm relies on two instrumentation primitives:
(1) System call interception
(2) Kernel callbacks

Based on our testing, the detection is compatible with Windows 10 1903 and previous versions. Evaluation results show that the detection is effective and has low overhead. Additionally, the generic detection mechanisms are also proven to detect newer PI techniques.



GitHub - rajiv2790/FalconEye


### [FalconHound, automatic attack path detection and enrichment for blue teams](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
For a long time, BloodHound has been the go-to tool for many red teams to uncover possible lateral movement paths in an environment. Fortunately, there are blue teams that also use it to great value. However, there are a lot of teams that struggle to use it due to lack of time or knowledge. On top of that, keeping the information in the BloodHound database up-to-date and using it for automatic detection and enrichment is often not implemented.

Introducing FalconHound, a toolkit that integrates with Microsoft Sentinel, Defender for Endpoint, the Azure Graph API, Neo4j and the BloodHound API to get the most out of your data. Some of its features allow it to track sessions, changes to the environment, alerts, and incidents on your entities and much, much more. All in near-real time!

This additional bi-directional context allows you to make better decisions and focus on the most important alerts and incidents. Allowing you, for instance, to run new path calculations frequently based on modifications, sessions or alerts and respond to these attacks which are very hard to detect without this information.


### [Find Blind Spots in Your Security with Paladin Cloud](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Paladin Cloud is an extensible, Security-as-Code (SaC) platform designed to help developers and security teams reduce risks in their cloud environments. It functions as a policy management plane across multi-cloud and enterprise systems, protecting applications and data. The platform contains best practice security policies and performs continuous monitoring of cloud assets, prioritizing security violations based on severity levels to help you focus on the events that matter..

Its resource discovery capability creates an asset inventory, then evaluates security policies against each asset. Powerful visualization enables developers to quickly identify and remediate violations on a risk-adjusted basis. An auto-fix framework provides the ability to automatically respond to policy violations by taking predefined actions.

Paladin Cloud is more than a tool to manage cloud misconfiguration. It's a holistic cloud security platform that can be used for continuous monitoring and reporting across any domain.


### [Firmware Audit: Platform Firmware Security Automation for Blue Teams and DFIR](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The first major release of our platform firmware security automation tool, Firmware Audit, aka: fwaudit. fwaudit automates the running and forensic hashing of output and firmware blobs for a variety of platform firmwares and across a variety of FOSS tools. fwaudit provides a pre-composed profiles for defense, exploration and forensics, to reduce the risk of bricking and maximize operational uptime.


### [Forecasting ATT&CK Flow by Recommendation System Based on APT](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Our tool is to forecast undetected ATT&CK techniques based on collaborative filtering and graph databases.
PCs and servers are generating massive logs daily, on the other hand, SOCs analysts are required to detect and respond quickly to cyber-attacks. However, it will take a lot of time to detect cyber-attacks if SOC analysts do not have clues. Conventional log analysis tools such as SIEM can detect attacks but cannot predict the next attack from the information already obtained. Recommendation systems often used in e-commerce sites can predict future purchasing behavior by analyzing the user's purchase history. Replacing with ATT&CK, each attacker group can be considered a user, and techniques attackers use can be regarded as a user's purchase history.
Using this tool, the logs are mapped to ATT&CK techniques by uploading log files to create a technique usage history of the attacker (adversary) currently conducting an ongoing attack. The adversary's technique usage history and past APT attack data are used for collaborative filtering to predict which techniques the adversary may use in the future. This visualization is　displayed together with the ATT&CK tactic, enabling you to see the attack flow in stages of progression. In addition, search queries of SIEM associated with forecasted ATT&CK technique are outputted. SOC analysts can consider attacks quickly and comprehensively by using queries.
The source code of this tool and an example analysis will be shown on GitHub. It is available as a web application.


### [Fortifying GCP Security: Open Source Just-In-Time access and Audit Log Monitoring](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Google does not make cloud security easy. The tool we're open sourcing doesn't make it easy either, but it makes it about 10% less painful than the existential dread the default GCP policies have infected on your organization.

In this talk, we'll guide you through setting up an audit log sink and evaluating events against Open Policy Agent (OPA) Rego policies. We'll discuss the included MITRE ATT&CK tactics policies and demonstrate how to create new custom policies using the OPA engine. We'll also cover how to make least privilege access control work for your organization with Just-In-Time access provisioning.

Our presentation aims to empower GCP users with the knowledge and tools necessary for effective large-scale monitoring of their environments' security and actions. We'll share some experience and insights on the current state of controls within GCP, and how infrastructure providers can enable more powerful tooling.

By the end of this talk, attendees will have gained practical knowledge in leveraging open source software to strengthen their GCP security posture. Don't miss this opportunity to stay ahead in the world of cloud security and enhance the protection of your GCP environment.


### [GIBBER SENSE](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Found a Gibberish string or file in the wild and don't know what is it? Throw it to GibberSense - it might start to make some sense. GibberSense is a python-based tool and extension to LAMMA as a BCAF (Basic Crypt Analysis Framework) module.

The best use of Gibber Sense is to verify the robustness of encryption libraries if they are free from any backdoors or flaws. Itt can also be used to guess the type of encryption, hashing schemes, and type of encrypted session cookies. If you trying to develop your own secrete encryption scheme, try and see what GibberSense has to say about it.


### [Gargamel](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Gargamel is a Windows tool for acquiring the forensic evidence from remote Windows or Linux machines using several different methods.

The program is able to download the following content from remote Windows machine:
- Windows Event Logs in evt and evtx format,
- dump of memory,
- specified files described with the support of expansions (*,?),
- output of commands specified in a text file,
- registry,
- state of firewall,
- state of network interfaces,
- logged on users,
- running processes,
- active network connections,

When targeting the remote Linux machine, the program will download:
- content of /var/log/directory
- specified files described with the support of expansions (*,?),
- output of commands specified in a text file,
- state of firewall,
- state of network interfaces,
- logged on users,
- running processes,
- active network connections,


Gargamel supports 5 connection methods, naming PowerShell remoting, WMI, PsExec, RDP and SSH (with SCP).


### [Grove: An Open-Source Log Collection Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Grove is a log collection framework designed to support a unified way of collecting, storing, and routing logs from Software as a Service (SaaS) providers which do not natively support log streaming.

This is performed by periodically collecting logs from configured sources, and writing them to arbitrary destinations.

Grove enables teams to collect security related events from their vendors in a reliable and consistent way, while allowing this data to be stored and analyzed with existing tools.


### [HASHVIEW](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Hashview is a web front-end to hashcat with many powerful features geared towards penetration testers. Leverage task automation and real-time analytics for increased results and fancy reports.

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


### [Hayabusa](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Hayabusa is a sigma-based threat hunting and fast forensics timeline generator for Windows event logs written in rust by Yamato Security. Rules can either be written sigma or built-in hayabusa rules that let the analyst extract out only the important fields for Windows DFIR investigations.


### [Honeyscanner: a vulnerability analyzer for Honeypots](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Honeypots are now considered a well-studied cyber-deception mechanism that can assist in defending networks as well as identifying new attack trends. However, recent research has shown that honeypots may also be vulnerable to attacks; especially fingerprinting identification ones. Moreover, many open-source honeypots lack an external security analysis and are often deployed with their default settings.

We present honeyscanner, an open-source vulnerability analyzer for honeypots. It is designed to automatically attack a given honeypot, to determine if the honeypot is vulnerable to specific types of cyber-attacks. The analyzer uses a variety of attacks, ranging from identifying vulnerable software libraries to DoS, and fuzzing attacks. In the end, an evaluation report is provided to the honeypot administrator, including advice on how to enhance the security of the honeypot.


### [HosTaGe: mobile honeypots for rapid deployment](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
HosTaGe is a lightweight, low-interaction, and portable honeypot for mobile devices that aims on the detection of malicious network environments. As most malware propagate over the network via specific protocols, a low-interaction honeypot located at a mobile device can check wireless networks for actively propagating malware. HosTaGe supports many commonly used protocols (e.g. HTTP, TELNET, SSH) along with many IoT/ICS specific ones (e.g. MQTT, S7COMM, MODBUS). We envision such honeypots running on all kinds of mobile devices to provide a quick assessment on the potential security state of a network.


### [IOC Explorer: Correlate IOC in Automatic Way](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
IOC correlation is usually a manual or semi-automatic work. It takes a lot of time to search multiple data sources and process different IOC types. IOC Explorer aims to introduce an automatic way to search data across major OSINT sources, like VirusTotal. Moreover, recursive searching feature will explore more possible IOCs based on previous IOCs, then build IOC relations automatically.

Source Code: https://github.com/lion-gu/ioc-explorer


### [Identify iOS Malicious Code Based on MachO File Structure](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
iOS Malicious Bit Hunter is a malicious plug-in detection engine for iOS applications. It can analyze the head of the macho file of the injected dylib dynamic library based on runtime, and can perform behavior analysis through interface input characteristics to determine the behavior of the dynamic library feature. The program does not rely on the jailbreak environment and can be used on the AppStore.


### [Identity Threat Hunting with Kestrel](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Attacks on Identity and access systems are starting points for major data breaches achieved through privilege escalation and lateral movement. Identity-threat hunting reduces time needed to detect traces of an attacker so that the consequences of a breach can be controlled. Identity-threat hunting involves data collection from identity providers, normalization and application of analytics while navigating the rabbit holes of authentication flows across the systems. Kestrel is a threat hunting language that accelerates cyber threat hunting by providing a layer of abstraction to build reusable, composable, and shareable "hunt-flows", providing a great platform for identity-threat hunting.


This arsenal session will showcase identity-threat hunting built on top of Kestrel. Starting with federated data retrieval from IAM systems using the OASIS Structured Threat Information eXpression (STIX) standard via OCA's STIX-shifter and lifting the results into an entity-relational data model. Then we will showcase analytic hunt steps besides data retrieval steps, walking you through the use case to hunt malicious activity in login data.


To showcase the capability of kestrel and identity threat hunting, we use event data gathered from IBM Security Verify Identity and access management (IAM). The queries and analysis follow OASIS STIX standards. Our hunt book will work with any Identity provider that has a stix-shifter connector.


The showcase uses a search for the IP address with multiple failed logins and later drills down and correlates with threat intel of known malicious activity for those IP addresses. The demo will also showcase the geographical distribution of those suspicious IP addresses, a list of applications which are accessed by these compromised IP addresses and accounts details of the logged-in user by IP address.


Making it ready to try by the audience, we will demonstrate live hunts in Jupyter Notebooks. At the end of the session, we will introduce the kestrel-huntbook repo for people to reuse existing huntbooks and share their hunting knowledge with their colleagues and other hunters in the community


### [In0ri](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Have you ever wondered how many ways there are to detect a defacement attack?

- Based on hash
- Based on signature
- Differential comparison
- Machine learning

Well, quite a lot. Nowadays, machine learning have really developed, with increasing agility and accuracy, this is
a new approach in Cyber Security in general which can adapt to new attack techniques.

In this talk, we will be presenting In0ri - a defacement detection system utilizing image-classification convolutional neural network.
There's two ways to deploy and use In0ri:
- Running off crontab by periodically visiting the URL.
- Internal agent running off the web server

With the first method, we can directly check if a path has been defaced or not.
As a system administrator, we can use the second method to check a local website with an internal Agent.

In0ri the first source machine learning project to detect defacement attacks, we will show the process of installing, training and running In0ri. After that, we will show how it succeeds to get high quality of detecting the deface attacks by using deep learning.


### [In0ri: Open Source Defacement Detection With Deep Learning](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
In0ri is the first open source system for detecting defacement attacks by utilizing image-classification convolutional neural network. In this presentation, we will be demonstrating the process of setting up In0ri and have it detect defacement attacks. And optionally the process of training the machine learning model. We will also be explaining the reason behind In0ri's high accuracy when classifying defacement attacks.


### [JVMXRay](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
JVMXRay is technology for monitoring access to system resources within the Java Virtual Machine at runtime. Since JVMXRay integrates with virtual machine, no code changes to the application are required for operation. An ancillary benefit of no code required is that the technology provides insight into 3rd party libraries used by your application and commercial software where no source code is available. JVMXRay is designed with application security emphasis but it's beneficial for other areas like software quality processes and diagnostics. JVMXRay may be extended to work with many technologies like OWASP Dependency Check and other tools.


### [KSBox: A Fine-Grained macOS Malware Sandbox](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Last year I published the Kemon open source project, which included a Pre and Post callback-based kernel inline hook engine. By using this engine, we can easily implement IPC and XPC monitoring, which helps build a fine-grained macOS malware sandbox. Therefore, there will be a new useful tool in our arsenal in August: KSBox.

Currently, KSBox malware sandbox has the following features: process and file operation monitoring; macOS IPC, XPC and network traffic monitoring; dynamic library and kernel extension monitoring; Mandatory Access Control (MAC) policy monitoring and filtering, etc. In short, security analysts can use this project to better analyze and gain insight into macOS malware.


### [Kemon: An Open-Source Pre and Post Callback-Based Framework for macOS Kernel Monitoring](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
If third-party vendors want to add new features to the macOS kernel, such as antivirus capabilities, ransomware blocking, data breach auditing, behavior monitoring and so on, they usually need the support of the system's exported interfaces. At present, only two known official interfaces are available, they are Kernel Authorization subsystem and Mandatory Access Control framework. Unfortunately, neither of them are suitable for today's kernel development tasks. The Kernel Authorization KPIs was designed thirteen years ago and it is clear that it lacks the necessary maintenance and upgrades. For example, there are only seven file operation related notification callbacks available, which are obviously not enough. For each notification callback (KAUTH_SCOPE_FILEOP), we cannot modify the return results. For some specific callback functions, the input parameters lack critical context information. As for the Mandatory Access Control framework, Apple directly claims that third parties should not use these private interfaces, this mechanism is not part of the KPI.

In order to bring about some changes, I'd like to introduce you to Kemon, an open source Pre and Post-operation based kernel callback framework. With the power of Kemon, we can easily implement LPC communication monitoring, MAC policy filtering, kernel driver firewall, etc. In general, from an attacker's perspective, this framework can help achieve more powerful Rootkit. From the perspective of defense, Kemon can help construct more granular monitoring capabilities. I also implemented a kernel fuzzer through this framework, which helped me find many vulnerabilities, such as: CVE-2017-7155, CVE-2017-7163, CVE-2017-13883, etc.

Source Code: https://github.com/didi/kemon
Documentation: https://github.com/didi/kemon/blob/master/doc/Kemon


### [Kraker](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Kraker is a distributed password brute-force system that allows you to run and manage the hashcat on different servers and workstations, focused on ease of use. There were two main goals during the design and development: to create the most simple tool for distributed hash cracking and make it fault-tolerant.


### [LATMA - lateral movement analyzer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
LATMA is a tool for offline detection and investigation of lateral movement attack based on AD event logs. The tool assists security teams to overcome the main challenges:

Data collection and preparation: in theory, event logs are an available data source to look for authentication anomalies. In practice, however, the source and destination machines are not represented in the same manner (hostname vs. IP), which prevents the ability to directly detect movement of a user account across different machines. LATMA conforms the representation of the source and destination machines, making the even log ready for analysis which is the tool's primary objectives.

Data analysis: LATMA scans the even data, looking for authentication patterns we have learned to be associated with lateral movement. For example, a chain of authentications where a single account logs from machine A to machine B and consecutively from machine B to C. Another example is what we call White-Cane in which an account logs from a single source to multiple destinations one after the other. The patterns LATMA searches for are based on our analysis of attacks in the wild, as well as on novel detection algorithm we have developed.

LATMA can be used in any environment where Kerberos and NTLM auditing is enabled, making it an easy and useful tool to any security professionals that handle an Active Directory environment. Offline analysis of authentications, while not real-time, is an efficient method to hunt for active lateral movement that goes under the radar and can provide the means to contain it before it reaches its objectives.


### [LIMACHARLIE](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
LimaCharlie is a cross-platform, open-source, endpoint monitoring, detection and response stack. The open source agent can be deployed to macOS, windows and Linux, reporting flight-recorder type information. The backend provides an easy and scalable framework to build automated detections and responses. Those automations have realtime access to the model stores in the backend as well as the sensors. Finally, a web ui provides visibility in the events from the sensor and their relationships. Output to systems like Splunk and Slack is also supported.


### [LMYN: Let's Map Your Network](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
It is of the utmost importance for any security engineer to understand their network first before securing it and it becomes a daunting task to have a 'true' understanding of a widespread network. In a mid to large level organisation's network having a network architecture diagram doesn't provide the complete understanding and manual verification is a nightmare. Hence in order to secure entire network it is important to have a complete picture of all the systems which are connected to your network.

BOTTOM LINE - YOU CAN'T SECURE WHAT YOU ARE NOT AWARE OF.

Let's Map Your Network (LMYN) aims to provide a easy to use interface to security engineer and network administrator to have their network in graphical form with zero manual error, where a node represents a system and relationship between nodes represent the connection. To achieve this it uses the basic network commands such as traceroute, ping scan etc.

Below are the modules in LMYN to perform the task of mapping

Project Management – Two modules (New Project and Working Project) will allow you to create and switch between the different projects

Load CMDB - This module allows an administrator to upload the CMDB file (new line separated) and map it entirely. Additionally, it have a Be Intrusive feature which, if selected, will perform enumeration to identify the 'rogue' host that are not present in CMDB. RED color node will depicts the rogue nodes

Find Me – This module enumerates the IP of system in which it is running and further network mapping will be done considering the current system as a 'seed'

Roam Around – This module identifies all 'live' hosts in the same LAN in which seed system is connected

Go To – This module displays graph of all hops that packet is traversing through to reach destination (provided by user) from seed system

Scan – This module will perform ping scan of any arbitrary IP range provided by user

Presentation: https://github.com/varchashva/LetsMapYourNetwork/blob/master/docs/LetsMapYourNetwork_BlackHat.pdf
Source Code: https://github.com/varchashva/LetsMapYourNetwork


### [LUDA: Large URLs Dataset Analyzer for Security](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
What interesting stuff can we find by looking only at URLs without the actual HTTP traffic ?

Well, quite a lot. Hackers often do not reinvent the wheel. They buy existing malwares or phishing that use the same scheme for HTTP communication. Techniques to randomize URLs , like DGA, often apply on the domain part". But what about the rest?

In this talk, we present LUDA - Large URLs Dataset Analyzer for security. It works in two modes: Malware or Phishing.
The first will detect similarities between C2 communication and cluster them by families. The last will apply the same clustering with an additional layer of " brand " detection.
Both of them can automatically extract regexes, using Genetic algorithm, and can be deployed for inline detections.
This powerful tool already supports integration with various public malicious repositories like PhishTank, URLHaus , Virus Total as well as dozens more.
As opposed to similar projects , this tool is focused only on security. It includes specific options like automatic false positive cleaning.
We will demo how we can run LUDA on public datasets with the two modes and show how it succeeds to get quality insights from large datasets. Finally we will show what are the current threat families found on real traffic data taken from Akamai Secure Web Gateway.


### [Learn How to Build Your Own Utility to Monitor Malicious Behaviors of Malware on macOS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The landscape of macOS malware has changed dramatically in the past couple of years. Threats are becoming more complex, more varied, and more numerous. As a malware analyst or security researcher, having a powerful dynamic analysis utility is vital to be effective and efficient. This utility can enable us to understand malware capabilities and quickly analyze the malicious behaviors of malware.

Want to know how to build your own arsenal? I will detail the implementation to monitor kinds of malicious behaviors of malware on macOS. The capabilities of the utility cover monitoring process execution with command line arguments, file system events (including all common file operations, such as open, read, write, delete, rename operations), dylib loading event, network activities (including UDP, TCP, ICMP, DNS query and response).

The Mandatory Access Control Framework is the substrate on top of which all of Apple's securities, both macOS and iOS, are implemented. I will discuss how to monitor process execution, file system events, and dylib loading events using MACF on macOS. Next, I'll provide the details for monitoring network activities using Socket Filters. The utility can also record some basic info including process name, parent process name, pid, ppid, uid besides the specific details for each event. For DNS response, this utility can parse the data of DNS response and record the IP:URL mappings.

The utility consists of two parts, one is the KEXT(core component) in kernel, the other one is a client program in user space, which involves the communication between kernel space and user space. After discussing some communication mechanisms, I'll choose the kernel control API, which is a socket-based API that allows you to communicate with and receive broadcast notifications from the KEXT. The client program is intended to receive the data from the KEXT and display it to users.

In this presentation, I provide an advanced solution to monitor kinds of malicious behaviors of malware in kernel on macOS. I will also provide all involved key technical details for the implementation of monitoring all common malicious behaviors of malware on macOS. This utility is designed to dynamically analyze the malicious behaviors of malware on macOS, helping analysts or security researchers more efficiently analyze malware. You can build your own utility for fun!

Source Code: https://fortinetweb.s3.amazonaws.com/fortiguard/research/fortiappmonitor_1.0.0_release.pkg

Presentation:

https://fortinetweb.s3.amazonaws.com/fortiguard/research/Learn_How_to_Build_Your_Own_Utility_to_Monitor_Malicious_Behaviors_of_Malware_on%20macOS_KaiLu.pdf


### [LogonTracer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
LogonTracer is a tool to investigate malicious logon by visualizing and analyzing Windows Active Directory event logs. Event log analysis is a key element in DFIR. In the lateral movement phase of APT incidents, analysis Windows Active Directory event logs is crucial since it is one of the few ways to identify compromised hosts. At the same time, examining the logs is usually a painful task because Windows Event Viewer is not a best tool. Analysts often end up exporting entire logs into text format, then feeding them to other tools such as SIEM. However, SIEM is neither a perfect solution to handle the increasing amount of logs.

We would like to introduce a more specialized event log analysis tool for incident responders. It visualizes event logs using network analysis and machine learning so as to show the correlation of accounts and hosts. Proven with our on the ground response experience, most importantly it is an open source tool.


### [Malboxes](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Malboxes is a tool to streamline and simplify the creation and management of virtual machines used for malware analysis.

Building analysis machines is a tedious task. One must have all the proper tools installed on a VM such as a specific version of vulnerable software (ie: Flash), Sysinternal tools, debuggers (Windbg), network traffic analyzers (Wireshark), man-in-the-middle tools (Fiddler). One must also avoid leaking his precious proprietary software licenses (IDA). At the moment, this menial job is not automated and is repeated by every analyst.

Malboxes leverages the DevOps principle of infrastructure as code to enable researchers to automatically create fully operational and reusable analysis machines. The tool uses Vagrant and Packer to do an initial out-of-band bootstrapping. Afterward, chocolatey is used to install further tools benefiting from the chocolatey package repository.

Attendees will learn a simple tool for safe malware analysis practice that is easy to grasp, enabling them to start doing analysis faster. Seasoned malware researchers will also gain from this demo by seeing how the DevOps approach can be applied to simplify and accelerate their labs' malware reverse-engineering capacity or reduce its management overhead.


### [MELEE: A Tool to Identify Ransomware Infections in MySQL Deployments](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Attackers are abusing MySQL instances for conducting nefarious operations on the Internet. The cybercriminals are targeting exposed MySQL instances and triggering infections at scale to exfiltrate data, destruct data, and extort money via ransom. For example one of the significant threats MySQL deployments face is ransomware. We have authored a tool named "MELEE" to detect potential infections in MySQL instances. The tool allows security researchers, penetration testers, and threat intelligence experts to detect compromised and infected MySQL instances running malicious code. The tool also enables you to conduct efficient research in the field of malware targeting cloud databases.


### [MLPdf: An Effective Machine Learning Based Approach for PDF Malware Detection](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Due to the popularity of portable document format (PDF) and increasing number of vulnerabilities in major PDF viewer applications, malware writers continue to use it to deliver malware via web downloads, email attachments and other methods in both targeted and non-targeted attacks. The topic on how to effectively block malicious PDF documents has received huge research interests in both cyber security industry and academia with no sign of slowing down.

In this work, we propose and demonstrate a novel approach based on a multilayer perceptron (MLP) neural network model, termed MLPdf, for the detection of PDF based malware. More specifically, the MLPdf model uses a backpropagation algorithm with stochastic gradient decent search for model update. A group of high quality features are extracted from two real-world datasets which comprise around 105000 benign and malicious PDF documents. Evaluation results indicate that the proposed MLPdf approach exhibits excellent performance which significantly outperforms all evaluated eight well known commercial anti-virus scanners with a much higher true positive rate (TPR) of 95.12% achieved while maintaining a very low false positive rate of 0.08%. Of the evaluated commercial AV scanners, the best scanner only has a TPR of 84.53%, which is over 10% lower than the proposed MLPdf model. In the demonstration, we will first manually analyze a malicious PDF document , then show how it can be automatically detected by the proposed ML approach.

Presentation: https://github.com/cyberML/MLPdf/blob/master/BlackHatUSA2018_MLPdf_slides.pdf
Paper: https://arxiv.org/abs/1808.06991


### [MLSploit: Resilient ML Platform - Advanced Deep Learning Analytic Platform Made Easy for Every Security Researcher](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Deep learning (DL) and machine learning (ML) had been proved to be effective tools to analyze or detect malware. To help security experts to apply cutting-edge ML technologies effortlessly, we designed a large scale DL analytic platform uniquely for security researches. This platform has a ML pipeline web interface which can guide users through each pipeline steps. Its novel feature analysis tool enables feature study and manipulation for adversarial ML evasive attack. The performances of classifiers can be compared and optimized and then used for prediction. The RESTful interface of this platform was developed to enable connections between external applications. Also it is possibly to productize this platform to become an cloud service.

Security analyst can upload either static or dynamic malware dataset to storage, i.e. big data Hadoop file system, and start the analysis. Or if backend sandbox is hooded, binaries can be uploaded for processing and then apply the output for inference. The ML pipeline supports several popular open source libraries, such as Scikit-Learn, big data Spark ML and deep learning Keras/Theano/Tensorflow. The slow DL training can be accelerated in a loosely connected backend worker, such as Intel Xeon Phi or GPGPU machines. The outputs are presented at web pages in several tables or in 2-D or 3-D interactive JavaScript diagrams for clear visualization. All the outputs, such as feature coefficient etc., can be downloaded for other usages. Also the prediction page can be used for ensemble inference or extended to be a test bed to demo new algorithm or adversarial attacks and defences. We will demo ransomware analysis on this platform and the perturbation attack against pre-trained image convolution neural network classifiers. We believe via this platform the security researches and analysis can be accelerated greatly.


### [MLsploit: A Cloud-Based Framework for Adversarial Machine Learning Research](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [MSTICpy: The Security Analysis Swiss Army Knife](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
MSTIC Jupyter and Python Security Tools (MSTICpy) is a Python library of security investigation tools developed by the Microsoft Threat Intelligence Center (MSTIC) to assist and support security analysts conducting security investigations and threat hunting.

The library provides features to collect data from a range of data sources, to enrich the data with Threat Intelligence and OSINT, to analyse the data using ML and data analysis techniques, and to visualise the output of this analysis for quick and easy comprehension.

Rather than a single tool MSTICpy is a Swiss Army knife for security investigations.


### [MalConfScan with Cuckoo: Automatic Malware Configuration Data Extraction and Memory Forensic](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
"MalConfScan with Cuckoo" is a tool for automatically extracting known malware configuration data. With the growing number of malware variants emerging day by day, the automation of malware analysis using sandbox systems is becoming popular. Such systems have a function to list malware behavior on Windows OS, such as communication, file and registry creation. On the other hand, malware analysts spend more time extracting malware configuration data rather than analyzing malware behavior. There are two reasons for it:

1. Many malware variants mostly share the same code except for configuration data. In other words, a type of malware and configuration data are the only elements that need to be checked.

2. Malware configuration data contains an attack campaign ID and communication encryption keys. This information would be the critical data for investigating logs in incident response, and also for knowing the actor's target.

We present a malware analysis tool to extract configuration data for incident responders and malware analysts. This tool automates analysis for many types of malware based on our long-time research and, reduce the time spent on malware analysis. In addition, this tool can be used not only for malware analysis but also for memory forensics. It can help a victim organization with malware infection to identify C2 server information and encryption key which are necessary for their incident response.


### [MalViz.ai](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The growth of internet and users increases exponentially and drastically in this decade that provides services inheriting various benefits to users such as online banking,marketing, buying /selling and various facility management services etc. It attracts some people to develop programs that perform
various malicious activities intentionally or unintentionally such as stealing sensitive informationfrom computer, displaying advertisement, causing harmful, unwanted activities. The malicious software are referred as
malwares. Therefore, this tool helps in detecting, classifying and visualizing the features of malware. Our tool uses the application of Malware Analysis, Machine learning and deep learning algorithms and some general framework applications to automatically classify whether the uploaded file is "Malicious or Legitimate". If it is legitimate the user is free to use but if it is malicious then that uploaded file(malware) is taken for review .It is analyzed and
important features of the malware are represented in graph based network.


### [MaliceIO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Malice's mission is to be a free open source version of VirusTotal that anyone can use at any scale from an independent researcher to a fortune 500 company.

Source Code: https://github.com/maliceio/malice


### [Malicious Executions: Unmasking Container Drifts and Fileless Malware with Falco](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Containers are the most popular technology for deploying modern applications. SPOILER ALERT: bypassing well-known security controls is also popular. In this talk, we explain how to use the recent updates in Falco, a CNCF open-source container security tool, to detect drifts and fileless malware in containerized environments.

As a best practice, containers should be considered immutable. Early this year, Falco introduced new features to detect container drift via OverlayFS, which can spot if binaries are added or modified after the container's deployment. New binaries are often a sign of an ongoing attack.

Of course, attackers can also use more advanced evasion techniques to stay hidden. By using in-memory, fileless execution, attackers can bypass most of the security controls such as drift detection and still reach their goals with no stress.

To combat fileless attacks, Falco has also added memfd-based fileless execution thanks to its visibility superpowers on Linux kernel system calls. Combining Falco's existing runtime security capabilities with these two new detection layers forms the foundation of a defense in depth strategy for cloud-native workloads.

We will walk you through real-world scenarios based on recent threats and malware, demoing how Falco can help detect and respond to these malicious behaviors and comparing both drift and fileless attack paths.


### [Malware Initial Assessment with pestudio](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
pestudio is used by Computer Emergency Response Teams and Labs worldwide in order to perform Malware Initial Assessment.


### [Memhunter: A Live Alternative to Volatility Memory Forensic Plugins](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Memhunter automates the hunting of memory resident malware, improving the threat hunter analysis process and remediation times. The tool detects and reports memory-resident malware living on endpoint processes. Memhunter only works on Windows at the moment, and it detects known malicious memory injection techniques. The detection process is performed through live analysis and without needing memory dumps. The tool was designed as a replacement of memory forensic volatility plugins such as malfind and hollowfind. The idea of not requiring memory dumps helps on performing the memory resident malware threat hunting at scale, without manual analysis, and without the complex infrastructure needed to move dumps to forensic environments.

In order to find footprints left by malware code injection techniques, memhunter relies on a set of memory inspection heuristics and ETW trace collection. Once a suspicious process gets identified, the tool filters out false-positives through Yara Rules analysis and VirusTotal queries. This down-selection process helps the tool to reduce the number of false positives, leaving only known-bad processes. The tool then gets forensic information on the remaining set of suspicious findings and report them back to the analyst for remediation steps.

The tool itself is a self-contained binary which can be run on the endpoint to conduct the memory hunting. The idea of a self-contained binary helps on reducing the footprint, the dependencies needed, and improving the deployability of the tool. The binary contains a set of embedded "hunters" plugins, each one in charge of performing a specific heuristic detection. It also contains the ability to register the binary as an ETW collection service, which will augment the findings of next runs by providing contextual information on the attack. The down-selection is performed through libyara and VirusTotal client functionality.

Source Code: https://github.com/marcosd4h/memhunter


### [Mimicry: An Active Deception Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
In incident response scenarios, intercepting attacks or quarantining backdoors is a common response technique. The adversarial active defense will immediately make the attacker perceive that the intrusion behavior is exposed, and the attacker may try to use defense evasion to avoid subsequent detection. These defense evasion may even result in later attacks going undetected. If we mislead or deceive the attacker into the honeypot, we can better consume the attacker's time cost and gain more response time.

We invented a series of toolkits to deceive attackers during the "kill-chain" . For Example:

Exploitation:
1. We return success and mislead the attacker into the honeypot for brute-force attacks.
2. We will simulate the execution of web attack payloads to achieve the purpose of disguising the existence of vulnerabilities in the system.

Command & Control:
1. For the Webshell scenario, we will replace the Webshell with a proxy and transfer the Webshell to the honeypot. When the attacker accesses Webshell, the proxy will forward his request to the honeypot.
2. For the reverse shell, we will inject the shell process and forward the attacker's operation to the shell process in the honeypot.
3. For the backdoor, we will dump the process's memory, resources, etc., and migrate it to the honeypot to continue execution.


### [Mitigating Open Source Software Supply Chain Attacks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [MoP: Master of Puppets - Open Source Super Scalable Advanced Malware Tracking Framework for Reverse Engineers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
MoP ("Master of Puppets") is an open source framework for reverse engineers who wish to create and operate trackers for new malware found in the wild for research purpose. To make it simple - MoP framework takes care of all the generic malware tracker stuff so the reverse engineer is left with pure reverse engineering work, You only need to implement a simple plugin on top of MoP which describes the malware's network protocol. MoP ships with a variety of workstation simulation capabilities, such as fake filesystem manager and fake process manager, multi-worker orchestration, TOR integration and more, all aiming to deceive adversaries into interacting with our simulated environment and possibly drop new unique samples. Since everything is done in pure python, no virtual machines or Docker containers are needed and no actual malicious code is executed, all of which enables us to scale up in a click of a button, connecting to potentially thousands of different malicious servers at once from a single instance running on a single laptop. MoP framework comes with a number of pre-built plugins for known RATs, such as NjRAT and Gh0stRAT which will be showcased live with real command and control servers!


### [Mobile Malware Mimicking Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [N3XT G3N WAF: ML based WAF with Retraining and Detainment through Honeypots](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
With the explosive growth of web applications since the early 2000s, web-based attacks have progressively become more rampant. One common solution is the Web Application Firewall (WAF). However, tweaking rules of current WAFs to improve the detection mechanisms can be complex and difficult.

NGWAF seeks to address the drawback method mentioned earlier with a novel machine learning and honeypot based architecture.

Firstly, we replace the traditional rulesets with deep learning models to reduce the complexity of managing and updating those rules. Instead of manually identifying rules, we use machine learning to automate the process of learning patterns from previous malicious data. In addition, we include a system model maintenance where we monitor the performance of the model and regularly retrain the model with new malicious data collected. A detection mechanism based on a fully automated machine learning pipeline will greatly reduce the manpower required and potential for error involved in WAF maintenance.

Malicious data detected will then be redirected into our novel system: an interactive, honeypotted, quarantine environment built to isolate potential hostile attackers and act as a sinkhole to gather current attack methods. Unlike conventional WAFs that just drop or block malicious attempts, NGWAF traps and diverts the threat actors to emulated systems to soften the impact of their malicious actions. By detaining the attacker to a series of scalable honeypotted environments, we are able to observe and collect their out-in-the-wild malicious data for future improvements to the detection mechanism. These data are automatically scrubbed and can be batched to be retrained into our detection model.

NGWAF is scalable and can be easily deployed either natively or in a cloud environment.


### [NEW TSURUGI LINUX ACQUIRE & DIGITAL FORENSIC ACQUISITIONS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Tsurugi ACQUIRE is a dedicated Linux OS to perform DIGITAL FORENSIC acquisition before to start post mortem DFIR investigations.


### [NFC Scrambler](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
NFC Scrambler is an android app that emulates a rfid card to prevent nfc skimming. Rfid cards are used nearly everywhere, either in the forms of identification cards or credit cards. RFID Skimming statistics reveal that every two seconds a new case of identity theft is reported in the United States; however, not everyone can afford a rfid blocker card or wallet. Thus this app will help them block rfid skimming for free.


### [NODDOS - STOP DDOS ATTACKS AT THE SOURCE](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
What if we could stop DDOS attacks before they even make it to the Internet? Noddos can block DDOS traffic in the gateway, router or firewall connecting the home- or enterprise network to the Internet. That's the truly scalable way to stop the botnets. Noddos enables that with open source client software, a big-data platform in the cloud and building a community that can sustain identifying botnets and defining the ACLs that can restrict their traffic flows.


### [Nethive Project](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The Nethive Project provides a Security Information and Event Management (SIEM) infrastructure empowered by CVSS measurements.

Nethive Architecture consists of four main components:

- Nethive Engine monitors every request coming through HTTP protocol to detect and identify any attempt of SQL Injection attacks. It also anonymously monitors every SQL query response to provide a wide range of XSS protection for your server, with both Stored and Reflected XSS attacks fully covered.

- Nethive Auditing watch everything that happens inside your valuable system, with your permission of course. This would detects any strange and suspicious activity inside the system, whether it is a post-exploitation attempt of an attacks, or simply someone you trust is making mistake inside your system.

- Nethive Dashboard provides you with resourceful, sleek user inferface that gives you the advantage of knowing everything. From resource consumption to the recent read-write action, it gives you full detail of what's happening, in near real-time.

- Nethive CVSS analyze the unfortunately already happening attacks and measure its vulnerability metrics, making sure you are ready to put your reports done in no time.


### [Network Monitoring Tools for macOS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
As the majority of malware contains networking capabilities, it is well understood that detecting unauthorized network access is a powerful detection heuristic. However, while the concepts of network traffic analysis and monitoring to detect malicious code are well established and widely implemented on platforms such as Windows, there remains a dearth of such capabilities on macOS.

Here, we will present various tools capable of enumerating network state, statistics, and traffic, directly on a macOS host. We will showcase open-source tools that leverage low-level APIs, private frameworks, and user-mode extensions that provide insight into all networking activity on macOS:

Specifically we'll demonstrate:

* A network monitor that allows one to explore all network sockets and connections, either via an interactive UI, or from the commandline.

* A DNS monitor that uses Apple's Network Extension Framework to monitors DNS requests and responses directly from the Terminal.

* A firewall that monitors and filters all network traffic, giving users with the ability to block unknown/unauthorized outgoing connections.


### [Noriben: Quick and Easy Automated Malware Analysis Sandbox](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Noriben is a Python-based tool that works Sysinternals Procmon to automatically collect, analyze, and report on runtime indicators of malware. It allows for the collection and analysis of unusual behavior on a system while attacks are being performed. The use of Noriben allows for manual analysis of malware while collecting its behavior, such as the use of command line arguments or manual debugging. With a host-based component, it can even run and collect info from thousands of malware samples automatically.


### [OBJECTIVE-SEE'S MACOS SECURITY TOOLS - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Patrick drank the Apple juice; to say he loves his Mac is an understatement. However, he is bothered by the increasing prevalence of macOS malware and how both Apple & 3rd-party security tools can be easily bypassed. Instead of just complaining about this fact, he decided to do something about it. To help secure his personal computer, he's written various macOS security tools that he now shares online (always free!), via objective-see.com.

So come watch as OverSight detects malware that spies on users (via the webcam/mic, Ransomwhere?), generically detects macOS ransomware, and a new open-source macOS firewall is released! Our Macs will remain secure!


### [OWASP Nettacker](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Nettacker project was created to automated for information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and information. This software is able to use SYN, ACK, TCP, ICMP and many other protocols to detect and bypass the Firewalls/IDS/IPS and devices. By using a unique solution in Nettacker to find protected services such as SCADA, we could make a point to be one of the bests of scanners.


### [OWASP Python Honeypot](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
OWASP Honeypot is an open-source software in Python language which is designed for creating honeypot and honeynet in an easy and secure way! This project is compatible with Python 2.x and 3.x and tested on Windows, Mac OS X, and Linux.


### [Objective-See's MacOS Security Tools](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Patrick drank the Apple juice; to say he loves his Mac is an understatement. However, he is bothered by the increasing prevalence of macOS malware and how both Apple & 3rd-party security tools can be easily bypassed. Instead of just complaining about this fact, he decided to do something about it. To help secure his personal computer, he's written various macOS security tools that he now shares online (always free!), via objective-see.com.

Come watch as DoNotDisturb detects physical access attacks, LuLu blocks malware attempting to communicate with C&C servers, OverSight detect webcam spying, and much more. Our Macs will remain secure!


### [Omniscient: Lets Map Your Network](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Omniscient: Lets Map Your Network aims to provide an easy-to-use and point-in-time interface to security engineers and network administrators to represent their network in graphical form with zero manual error, where a node represents a system and relationship between nodes represents a direct connection. It also monitors the 'identified' network with user-defined periodicity and provides the analytics on rogue systems/devices present in network.

It is utmost important for any security engineer to understand their network first before securing it and it becomes a daunting task to have a 'true' understanding of a widespread network. In a mid to large level organisation's network having a network architecture diagram doesn't provide the complete understanding of network and manual verification is a nightmare. Hence in order to secure entire network it is important to have a complete picture of all the systems which are connected to your network, irrespective of their type, function, technology etc.

BOTTOM LINE - YOU CAN'T SECURE WHAT YOU ARE NOT AWARE OF.

Omniscient does it in two phases:
1. Learning: In this phase, Omniscient 'learns' the network by utilising passive network enumeration, active scans and upload of existing CMDB for on-premises network; and by querying the APIs for cloud networks. Then it builds graph database leveraging the responses of all learning activities. User can perform any of the learning activities at any point of time and Omniscient will incorporate the results in existing database.

2. Monitoring: This is a continuous and automatic process, where Omniscient monitors the 'identified' network (with user-defined periodicity) for any changes, compare it with existing information and update the graph database accordingly.


### [Ox4Shell - Deobfuscate Log4Shell payloads with ease](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Since the release of the Log4Shell vulnerability (CVE-2021-44228), many tools were created to obfuscate Log4Shell payloads, making the lives of security engineers a nightmare.

Threat actors tend to apply obfuscation techniques to their payloads for several reasons. Most security protection tools, such as web application firewalls (WAFs), rely on rules to match malicious patterns. By using obfuscated payloads, threat actors are able to circumvent the rules logic and bypass security measures. Moreover, obfuscated payloads increase analysis complexity and, depending upon the degree of obfuscation, can also prevent them from being reverse-engineered.

Decoding and analyzing obfuscated payloads is time-consuming and often results in inaccurate data. However, doing so is crucial for understanding attackers' intentions.

We believe that security teams around the world can benefit from using Ox4Shell to dramatically reduce their analysis time. To help the security community, we have decided to release Ox4Shell - a payload deobfuscation tool that would make your life much easier.


### [PA Toolkit: Wireshark Plugins for Pentesters](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Wireshark is the most basic tool that anyone thinks of when network traffic analysis is mentioned. Wireshark is beyond doubt, a wonderful tool which is available free of cost to the community and is well maintained. It is also modular and allows the user to add more functionality in form of C/Lua plugins. There are some good dissectors and plugins available for Wireshark which make user's life easy but when we talk the plugins related to attack detection or macro analysis from the security point of view, there is not much available. Our PA Toolkit is such an attempt to extend the functionality of Wireshark from a micro-analysis tool and protocol dissector to the macro analyzer and threat hunter.

PA toolkit is a collection of Wireshark plugins which enables a pentester to get insights for multiple network protocols like WiFi, VoIP, ARP, DNS, DHCP, SSL etc. This eliminates the need for a separate software/framework to detect basic attacks. The plugins are easy to add and are platform independent.


### [Packing-Box: Breaking Detectors & Visualizing Packing](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
This Docker image is an experimental toolkit gathering analyzers, detectors, packers, tools and machine learning mechanics for making datasets of packed executables and training machine learning models for the static detection of packing. It aims to support PE, ELF and Mach-O executables and to study the best static features that can be used in learning-based static detectors. Furthermore, it currently additional functionalities to focus on supervised and unsupervised learning but also on adversarial learning for breaking static detectors and detection models.

https://raw.githubusercontent.com/packing-box/docker-packing-box/main/docs/material/bheu23-packingbox.pdf


### [Packing-Box: Playing with Executable Packing](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
This Docker image is an experimental toolkit gathering detectors, packers, tools and machine learning mechanics for making datasets of packed executables and training machine learning models for the static detection of packing. It aims to support PE, ELF and Mach-O executables and to study the best static features that can be used in learning-based static detectors.


### [Performing Live Forensics Without Killing Your Evidence](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
In a threat landscape characterized by targeted attacks, file-less malware and other advanced hacking techniques, the days of relying solely on traditional "dead box" forensics for investigations are, well… dead. Live forensics, a practice considered a dangerous and dark art just a decade ago, has now become the de-facto standard. However, many CSIRT teams still struggle with this type of threat hunting.

This session will discuss the benefits, pitfalls to avoid and best practices for performing live box forensics as a threat hunting tool. The presenter will also introduce a free and publicly available command line tool for Windows that automates the execution and data acquisition from other live forensics tools in a more secure, easier to maintain manner.


### [Post-Quantum Cryptography Library](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
This library provides a convenient way for developers to integrate post-quantum cryptography into their applications, helping to protect sensitive information from potential quantum computing attacks. We present f5oqs_sdk, a Python 3 library that wraps the liboqs C library, which is part of the Open Quantum Safe (OQS) project. The OQS project aims to develop and prototype quantum-resistant cryptography. The f5oqs_sdk offers a unified API for post-quantum key encapsulation and digital signature schemes, as well as a collection of open-source implementations of post-quantum cryptography algorithms. It also provides support for alternative RNGs through the randombytes[] functions. The library is available on PyPI and can be easily installed with pip. The paper provides a brief overview of the installation process and usage of the library, along with examples of how to use the API.

f5oqs_sdk is a powerful tool for developers who want to integrate post-quantum cryptography into their applications. It provides a unified and easy-to-use API for implementing quantum-resistant cryptography, helping to protect sensitive information from potential quantum computing attacks.


### [Protecting your Crypto Asset against Malicious JS Phishing](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Cryptocurrencies and NFT are taking over with predictions of 90% of the population holding at least one of them by the end of the decade. Users that want to facilitate these new assets, trade them and sell them typically do that using wallets, and in particular hot wallets that are easy-to-use. The most popular hot wallets today (e.g., MetaMask) are browser based and are thus vulnerable to phishing and scams made possible through malicious JavaScript, such as a recent campaign carried out by the Lazarus group which resulted in more than 400M$ worth of stolen cryptocurrencies.

We release our internal tool used by the Security Operation and the research at Akamai to scan the JS from any website.
It includes a Python recursive crawler that extracts every JS from any domain (written within the HTML or imported), analyzes it with a model and heuristics - that we provide -, and brings metadata ( from VT, publicwww…) It finally gives a score to every piece of code running on any URL of a specified domain.
The code works also as a Web App and exposes a REST API as well.

We will finish by presenting some real detection we caught with this tool and explaining them.


### [PurpleSharp 2.0: Active Directory Attack Simulations](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [PurpleSharp: Adversary Simulation for the Blue Team](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Defending enterprise networks against attackers continues to present a difficult challenge for blue teams. Prevention has fallen short; improving detection & response capabilities has proven to be a step in the right direction. However, without the telemetry produced by adversary behavior, building and testing detection capabilities will be a challenging task. Executing adversary simulations in monitored environments produces the telemetry that allows security teams to identify gaps in visibility as well as build, test and enhance detection analytics

PurpleSharp is an open source adversary simulation tool written in C# that executes adversary techniques against Windows Active Directory environments. The resulting telemetry can be leveraged to measure and improve the efficacy of a detection engineering program. PurpleSharp executes different behavior across the attack lifecycle following the MITRE ATT&CK Framework's tactics: execution, persistence, privilege escalation, credential access, lateral movement, etc.

PurpleSharp executes simulations on remote hosts by leveraging administrative credentials and native Windows services/features such as Server Message Block (SMB), Windows Management Instrumentation (WMI), Remote Procedure Call (RPC) and Named Pipes.

PurpleSharp can assist blue teams in the following use cases:

- Verify prevention controls ( are Lsass dumps being blocked ? )
- Build new detection controls ( build a detection rule for T1117)
- Test/verify existing detection controls (are we really detecting process injection ?)
- dentify gaps with existing detection analytics ( broken logic, lack of coverage, etc. )
- Identify gaps in visibility ( broken agents, broken event pipelines, etc. )
- Train the SOC with credible simulations


### [PurpleSharp: Automated Adversary Simulation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [PyExfil - A Python Data Exfiltration & C2 Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
PyExfil is a python data exfiltration package. It is currently an open source package allowing everyone to download, use and edit the code. It has several modules classified in 4 types of data exfiltration purposes. It is designed to enable Security personnel to test their Data Leakage Prevention mechanisms by attempting to leak various types of data and examine alerting and prevention mechanisms employed in their infrastructure.


### [REW-sploit: Dissecting Metasploit Attacks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Metasploit and Cobalt Strike are wildly used tool for red-teams, pen-testers and sometimes malicious actors. They deliver a lot of ready-to-use exploits facilitating work of the attacker. But who thinks about the poor blue-team members? They are left alone. It looks automation is for attackers only!
But now, there is a hope: REW-sploit is a new tool with the aim to help defenders in analyzing Metasploit (and in some form Cobalt Strike) based attacks. Leveraging some well know frameworks it can emulate payloads, extracts crypto keys and correlate PCAP dumps to get extra info about what is going on. Automation is now for defenders too!


### [RIoTPot: A Modular Hybrid-Interaction IoT/OT Honeypot](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [ROADtools and ROADrecon](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
ROADtools is a framework to interact with Azure AD. It currently consists of a library (roadlib) and the ROADrecon Azure AD exploration tool.

ROADlib is a library that can be used to authenticate with Azure AD or to build tools that integrate with a database containing ROADrecon data. The database model in ROADlib is automatically generated based on the metadata definition of the Azure AD internal API.

ROADrecon is a tool for exploring information in Azure AD from both a Red Team and Blue Team perspective. In short, this is what it does:

- Uses an automatically generated metadata model to create an SQLAlchemy backed database on disk.
- Use asynchronous HTTP calls in Python to dump all available information in the Azure AD graph to this database.
- Provide plugins to query this database and output it to a useful format.
- Provide an extensive interface built in Angular that queries the offline database directly for its analysis.

ROADrecon also provides a built-in plugin to export it's data to a custom version of BloodHound with Azure AD capabilities.

Both ROADtools and ROADrecon are completely free and open source software.


### [Rapid Data Exploration With Apache Drill](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [Real-Time AD Attack Detection: Detect Attacks Leveraging Domain Administrator Privilege](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
In Advanced Persistent Threat (APT) attacks, attackers tend to attack the Active Directory to expand infections. Attackers try to take over Domain Administrator privileges and create a backdoor called the "Golden Ticket". Attackers leverage this Golden Ticket to disguise themselves as legitimate accounts and obtain long-term administrator privilege. However, detecting attacks that use this method is quite difficult because the attackers' use of legitimate accounts and commands are not identified as anomalies.

We introduce a real-time detection tool that uses Domain Controller Event logs for detecting attack activities leveraging Domain Administrator privileges. Our tool can minimize the damages these types of attacks can cause even if the attackers maliciously take advantage of the Golden Ticket.

Our tool consists of the following steps to reduce false detection rate and support immediate incident response.

Step1 (Signature based detection): Analyze Event logs focusing on the characteristics of the attack activities.
Step2 (Machine Learning): Use unsupervised machine learning and anomaly detection in order to detect suspicious commands that attackers tend to use as outliers.
Step3 (Real-time alert): Raise real-time alerts using Elastic Stack if attack activities are detected.

We will publish our tool on GitHub and show specific algorithms that we have implemented so that visitors can customize or develop their own system. Our tool is all open sourced, enabling immediate and efficient incident responses against attacks at a reasonable cost.

Presentation: ﻿https://github.com/sisoc-tokyo/Real-timeDetectionAD/blob/master/Arsenal_eu-18-Real-time-Detection-of-Attacks-Leveraging-Domain-Administrator-Privilege.pdf


### [Real-Time Detection Tool of High-Risk Attacks Leveraging Kerberos and SMB](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
In Advanced Persistent Threat (APT) attacks, attackers tend to attack against the Active Directory. Especially vulnerabilities fixed in MS14-068 and MS17-010 have been leveraged to get administrator privileges. Attackers who can get administrator privileges likely create "Golden Ticket" and "Silver Ticket" to disguise themselves as arbitrary administrative accounts for a long period. However, detecting these attacks is quite difficult since legitimate accounts and processes are leveraged. Since sometimes attackers successfully accomplish lateral movement in a short period, immediate detection is needed.

We will introduce a real-time detection tool for the following attack activities against Active Directory using Event logs and Kerberos packets.
-Attacks leveraging the vulnerability fixed in MS14-068 and MS17-010
-Attacks using Golden Ticket
-Attacks using Silver Ticket

We introduced the detection tool for Golden Ticket from Event Logs in Black Hat Europe 2018, but sometimes false positive occurs because of the Kerberos specification. In this time, we introduce the improved tool. The detection rate is improved, and introduce a new feature to detect Silver Ticket attacks.

Our tool can detect attacks against Windows 2008 R2, 2012, 2016. Additionally, our tool utilizes only Domain Controller's built-in Event Logs and minimum Kerberos packets. Thus, it can be implemented in easy way and helps immediate incident response.

Finally, ATT&CK, a knowledge base of adversary tactics and techniques, is becoming common recently. The tool can identify the possible tactics for each detected attack activity automatically.

Source code: https://github.com/sisoc-tokyo/Real-timeDetectionAD_ver2


### [RedHunt OS (VM): A Virtual Machine for Adversary Emulation and Threat Hunting](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The ultimate aim of any security exercise (offensive or defensive) is to make the organization more resilient and adaptive towards modern adversaries. RedHunt OS (Virtual Machine) aims to provide defenders a platform containing the toolset to emulate adversaries and on the other hand arm them with advanced logging and monitoring setup to actively hunt such adversaries. The project aims to provide a one stop shop which defenders can quickly spin up and practice blue team exercises in the presence as well as absence of an active attacker. Similarly, red team can utilize the platform to identify and understand the footprints they leave behind during a red team exercise. Both the teams can utilize the setup to become better at what they do ultimately leading to better security.

Source Code: https://github.com/redhuntlabs/RedHunt-OS/﻿


### [RedHunt-OS v2: Virtual Machine for Adversary Emulation and Threat Hunting](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The ultimate aim of any security exercise (offensive or defensive) is to make the organization more resilient and adaptive towards modern adversaries. RedHunt OS (Virtual Machine) from RedHunt Labs aims to provide defenders a platform containing the toolset to emulate adversaries as well as advanced logging and monitoring setup to actively hunt such adversaries.

The project aims to provide a one-stop shop which defenders can quickly spin up and practice blue team exercises in the presence as well as the absence of an active attacker. On the other hand, the red team can utilize the platform to identify and understand the footprints they leave behind during a red team exercise. Apart from Adversary Emulation and Threat Hunting tools, the OS also provides Open Source Intelligence (OSINT) and Threat Intelligence tools. Both red and blue teams can utilize the setup to become better at what they do, ultimately leading to better security.


### [RuleCraftLab - A Detection Rule Development Platform](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
"RuleCraftLab" is an open-source platform that provides SOC engineers, security researchers, and detection engineers with a robust environment for developing and testing detection content using real threat logs from actual systems. As the landscape of threats continues to evolve and diversify, there is a growing need for accurate and effective rules to detect and mitigate these threats. However, traditional rule development methods often lack real-world context, relying on blog posts or public rules without thorough testing. "RuleCraftLab" addresses these challenges by offering a dedicated playground where users can develop and test their rules in a realistic environment to streamline the rule development process.


### [S-TIP: Seamless Threat Intelligence Platform](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
S-TIP is an open-source platform for those who analyze threats and share the results with CSIRT etc.

There are a variety of CTI (Cyber Threat Intelligence) in the world. "Human CTI" is knowledge of cyberattacks to be consumed by people through social media, email, and other channels. "System CTI" is cyber attack-related knowledge that is consumed by systems in a format that can be understood by computers, namely STIX.

However, there were barriers between Human CTI and System CTI. There were divided and could not be utilized from the other realm. For example, security operators need intensive manual labor to convert a new threat report for human readers into CTI in a machine-readable format for automated defense.

S-TIP solves this problem by integrating Human CTI and System CTI seamlessly through its STIX database to bring down those barriers. When a user creates a new post, it is automatically converted to the STIX file and saved into the database. The system can trigger automated defense by consuming the STIX file. These processes can be done transparently while a user is unaware of the conversion.

Main features of S-TIP are:
1. CTI Element Extractor: Human posts to the social media UI of S-TIP are automatically captured as STIX data.
2. CTI Graph Analytics View: The STIX data can be associated with other pieces of CTI. This mechanism makes it much easier for users to grasp the whole picture of the cyberattack quickly.
3. Integration with Other Platforms: The STIX data can be readily consumed by security tools like MISP, Splunk, JIRA, and Slack.
4. STIX/TAXII - Compliant: Collects CTI from open STIX / TAXII servers on the Internet like AlienVault OTX.

These features support a more predictive and proactive response.

Available at : https://github.com/s-tip


### [SCYTHE: The Yara Signature Crafter that Fingerprints Honeypot Traffic](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [SITCH: DISTRIBUTED, COORDINATED GSM COUNTER-SURVEILLANCE - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
SITCH uses inexpensive hardware and open-source software to create a network of sensors for detecting malicious activity in GSM wireless networks.

SITCH sensors are based on the Raspberry Pi 3 platform and use inexpensive, easy-to-source software-defined, GPS, and GSM radios. One person can manage a large number of SITCH sensors, including on-the-fly configuration and firmware updates, from a web browser.


### [SMBeagle: SMB Share Hunter](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [SNDBOX: The Artificial Intelligence Malware Research Platform](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
SNDBOX is the world's first Artificial Intelligence (AI) malware research platform designed to scale up research time. Developed by researchers for researchers, SNDBOX offers never-seen-before malware analysis visibility powered by kernel mode next generation sandbox. Multiple AI detection vectors work alongside our big data malware similarity engine to reduce false positive classification errors. Behavioral signatures, multi-vector deep learning classifiers and multiple AI similarity search engines seamlessly work together to provide high visibility and data-driven explanations to scale malware research capabilities and reduce research time. Furthermore, with full access to our data, all levels of your team can leverage information necessary for complete malware remediation and new research possibilities, while sharing insights, public samples and IOC's through our community platform.


### [SSH into any device from anywhere with ZERO Open Network ports](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
SSH to Any Device with No Ports Open
Make your devices reachable while eliminating network attack surfaces & reducing administrative overhead.

Atsign's patent pending core technology is engineered to deliver the following benefits:
Addressability
Atsign's core technology uses identifiers which replace the need to manage IP addresses. If you remember the atSign (Atsign's version of an address), you can look up the IP address and port in the atDirectory which manages this information for you.
Reachability
‍Atsign's core technology provides each device with its own microserver which makes it reachable from anywhere on the internet.
No open ports (no network attack surface) on the device
Connections are always made from the device to the microserver, meaning that no ports ever need to be opened on devices using this technology.
End-to-end encrypted
Information is automatically encrypted on the edge devices before it is sent over Atsign's control plane.
Zero Trust
Atsign's technology is designed such that cryptographic keys are only stored at the edge device. No third party or intermediary ever possesses the decryption keys which are required to access the information. You don't need to trust any of the microservers, because they never see information in the clear.
In other words, sending information using Atsign's control plane requires no open ports and is fully edge-to-edge encrypted, all without needing to know the IP address of the device!


### [SSHook: A Lightweight Syscall Hooking Tool for Uncovering Hidden Malicious Instructions](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Most Android hook ways aim at watching APIs for Java or Native code. However, some malicious apps try to escape hooking and access sensitive data using syscall directly, so it is crucial in order to uncover hidden code that some malicious apps use to bypass standard hooking techniques and access sensitive data directly through system calls. We have implemented a syscall hooking tool based on Seccomp-BPF named SSHook, which gives better balance between performance and compatibility.

Seccomp-BPF was introduced into Linux kenel to filter syscalls and their arguments, we transform this security feature into a syscall hook framework which support devices range from Android 8.1 to Android 13. Our tool SSHook combined Seccomp-BPF with throwing an exception to catch syscall, and resuming instructions for normal execution by preparing additional threads earlier, which avoids frequent interruptions and possible risks like deadlocks, suspensions, or crashes. For performance improvement, we have implemented a flag that determines whether to resume execution using either the inactive parameter or the higher 4 bytes of an integer type, but the program can still run normally without any impact. Besides, SSHook is a lightweight framework but performs efficiently and robustly compared with other invasive or complicated solutions, which keep stable and reliable by standing on the shoulders of kernel features.

SSHook can help to identify suspicious behavior in malicious Apps which abuse syscall to steal privacy files or collect sensitive data like MAC, applist, which can be integrated into sandbox environment to conduct more complete dynamic analysis. Furthermore, SSHook allows us to replace syscall arguments and bypass hooking tools to evade detection, which is particularly useful in preventing the collection of device fingerprints and protecting user privacy against tracking.


### [SWEET SECURITY](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Sweet Security is a network security monitoring and defensive tool which can be deployed on hardware as small as a Raspberry Pi. Using the power of Bro IDS and threat intelligence feeds, malicious network traffic can be exposed. This data is gathered and visualized with the ELK stack (Elasticsearch, Logstash, and Kiban). Going beyond detection, the device can implement blocking for specific devices on a granular level. Sweet Security can monitor all network traffic with no infrastructure change and block unwanted traffic. It ships with Kibana dashboards, as well as a new web administration UI. Even better, the installation can be separated between web administration and sensor. Want to deploy the web administration to AWS and install a dozen sensors? No problem!

All of these tools and methodologies run on inexpensive hardware, such as the Raspberry Pi. If you're looking for a more scalable solution, these tactics and tools can be adapted to enterprise scale deployments, as well. Attendees can expect to take away methodologies they can put to use right away, from dorm-room to datacenter.


### [SYNwall: A Zero-Configuration (IoT) Firewall](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
A lots of words has been spent in the last years about IoT security: but instead of thinking to deploy a new device, let's try to stay on what we already have: we have a TCP/IP stack. And what we don't want to have? Complicated and cumbersome security configurations.

The aim of SYNwall is to build an easy to configure, no new hardware, low footprint, lightweight and multi-platform security layer on TCP/IP: with a one way OTP authentication, SYNwall can make every device more secure and resilient to the real world networking reconnaissance and attacks.

If we think at some of the IoT installations (may be directly internet exposed, in difficult environments, with no support infrastructure available), the possibility to have an on-board and integrated way to control access, can make a huge difference in terms of security.

The device will became virtually unaccessible to anyone who don't have the proper OTP key, blocking all the communications at the very first level of it: the SYN packet. No prior knowledge of who need to access is required at this point, making configuration and deploy a lot easier.


### [Sandbox Scryer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
"Sandbox Scryer: An open source tool leveraging free sandbox technologies to enable threat hunting and intelligence"

When defending against APTs or Advanced Persistent Threats, persistent is the most important aspect of that definition. Often a security solution will stop a threat actor on initial access, when they inject command and control beacons into processes, or when they move laterally. Which leads to important questions. What's next? Will the actor try again? What are they after? How do I improve my defenses when the threat actor inevitably tries again?

A defender must be able to answer these questions. SoC analyst time is among the most valuable in any organization, and automated research tools such as sandboxes can be a valuable solution to accelerate this process. Unfortunately, making sense of all the data takes time. Indicators of Compromise (IOCs) are invaluable for communicating actionable intelligence about attacks, as is identifying relevant secondary payloads and top ATT&CK tactics and techniques among all the data a sandbox can generate. This critical information can be used to drive threat hunting, assessment of attack success and penetration, and pre-emptive identification of risk of future attack.

In this demonstration, we will showcase an open source tool, the Sandbox Scryer, which performs sample submission to the free Hybrid Analysis Sandbox, retrieval of results of the Sandbox's automated analysis, and extraction from these sets of important IOCs and techniques matched against MITRE Att&ck. This open source tool will be made available, which enables an organization to adapt it to their favorite free or paid sandbox (of which there are many), along with expanding it to produce of types of IOCs.


### [Sandboxing in Linux with zero lines of code](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Linux seccomp is a simple, yet powerful tool to sandbox running processes and significantly decrease potential damage in case the application code gets exploited. It provides fine-grained controls for the process to declare what it can and can't do in advance and in most cases has zero performance overhead.

The only disadvantage: to utilize this framework, application developers have to explicitly add sandboxing code to their projects and developers usually either delay this or omit completely as their main focus is mostly on the functionality of the code rather than security. Moreover, the seccomp security model is based around system calls, but many developers, writing their code in high-level programming languages and frameworks, either have little knowledge to no experience with syscalls or just don't have easy-to-use seccomp abstractions or libraries for their frameworks.

All this makes seccomp not widely adopted—but what if there was a way to easily sandbox any application in any programming language without writing a single line of code? This presentation discusses potential approaches with their pros and cons.


### [Siembol: An Open-Source Real-Time SIEM Tool Based on Big Data Technologies](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [Sigma Hunting App for Splunk](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The Sigma Hunting App for Splunk addresses two main challenges: missing collaboration in detection rule development and automated deployment of detection rules. By using Sigma as an generic signature description language, security analysts and security researcher from all over the world can work together independent from their SIEM tool. The joint detection rule development improves the general detection capabilities of the Security Operations Centers. The manual deployment of a detection rule in Splunk was a time-consuming task in order to complete all the needed fields for a scheduled search. The Sigma Hunting App solves that problem by providing a dedicated Splunk App, which can be used to dynamically update Sigma detection rules from a Git repository.

Furthermore, the Sigma Hunting App supports the analyst in their investigations of triggered detection rules. The triggered detection rules are stored as events in a separate threat-hunting index enriched with data of the Mitre ATT&CK Matrix.

The audience should learn the following aspects:

A modern approach of detection rule development
Continuous Delivery in detection rule development through the Sigma Hunting App
Installing and configuring the Sigma Hunting App
Automated deployment of detection rules into Splunk
Features of the Sigma Hunting App
Using Sigma Hunting App to find suspicious behavior


### [SilkETW: Collecting Actionable ETW Data](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Event Tracing for Windows (ETW) provides researchers with a rich data set which can be leveraged both for defensive as well as offensive purposes. ETW collectors can alert the user to malicious behavior such as user-land APC injection from the Kernel, or equally, allow an attacker to spy on keyboard and mouse activity. The scope for ETW research is large but the information security community has been slow to adopt it. The two primary problems with ETW are: the complexities involved in event collection, and the volume of data that is generated.

SilkETW is a flexible C# ETW wrapper which attempts to mitigate the aforementioned issues by providing a straightforward interface for data collection, various filtering mechanics, and an output format that can be easily processed. ETW output can be written locally to disk, to the Windows event log or shipped off (using POST requests) to 3rd party infrastructure such as Elasticsearch.

This project was originally implemented by the FireEye Advanced Practices (AP) team to aid in the rapid analysis of novel attacker trade-craft, and to feed that analysis back into the detection engineering process.


### [SinCity: Build Your Dream Lab Environment](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Security practitioners are still wasting time today building and maintaining lab environments through "manual" and cumbersome processes. In doing so, they are missing out on the potential DevOps methodologies and Infrastructure-as-Code (IaC) practices offer. This daunting work must end now.

This arsenal demonstration will introduce SinCity, a GPT-powered, MITRE ATT&CK-based tool which automates the provisioning and management of an IT environment in a conversational way. SinCity reduces the efforts needed to build a full-blown lab environment from months to minutes by providing an abstraction layer for customizing network topologies, crafting attack scenarios, and tuning security controls.

Attendees who frequently sandbox malware, analyze TTPs, or evaluate detection capabilities - this arsenal will save you precious time.


### [Slips: A Machine-Learning Based, Free-Software, Network Intrusion Prevention System](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [Slips: A machine-learning based, free-software, P2P Network Intrusion Prevention System](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
For the last 7 years we developed Slips, a behavioral-based intrusion prevention system, and the first free-software network IDS using machine learning. Slips profiles the behavior of IP addresses and performs detections inside each time window in order to also *unblock* IPs. Slips has more than 20 modules that detect a range of attacks both to and from the protected device. It is an network EDR with the capability to also protect small networks.

Slips consumes multiple packets and flows, exporting data to SIEMs. More importantly, Slips is the first IDS to automatically create a local P2P network of sensors, where instances share detections following a trust model resilient to adversaries..

Slips works in several directionality modes. The user can choose to detect attacks coming *to* or going *from* these profiles, or both. This makes it easy to protect your network but also to focus on infected computers inside your network, which is a novel technique.

Among its modules, Slips includes the download/manage of external Threat Intelligence feed (including our laboratory's own TI feed), whois/asn/geocountry enrichment, a LSTM neural net for malicious behavior detection, port scanning detection (vertical and horizontal) on flows, long connection detection, etc. The decisions to block profiles or not are based on ensembling
algorithms. The P2P module connects to other Slips to share detection alerts.

Slips can read packets from the network, pcap, Suricata, Zeek, Argus and Nfdump, and can output alerts files and summaries. Having Zeek as a base tool, Slips can correctly build a sorted timeline of flows combining all Zeek logs. Slips can send alerts using the STIX/TAXII protocol.

Slips web interface allows to clearly see the detections and behaviors, including threat inteligence enhancements. The interface can show multiple Slips runs, summarize whois/asn/geocountry information and much more.


### [Slips: Free software machine learning tool for Network Intrusion Prevention System](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Slips is the first free software, behavioral-based, intrusion prevention system to use machine learning to detect attacks in the network. It is a modular system that profiles the behavior of devices and performs detections in time windows. Slips' modules detect a range of attacks both to and from the protected devices.

Slips detect attacks to and from devices protecting your network but also focusing on infected computers. All the analyses are reevaluated in time windows so computers can be unblocked if they are cleaned. Avoiding permanent detections when the risk is gone.

Slips manages Threat Intelligence feeds (44 external feeds, including our own), the enrichment with WHOIS/ASN/geo location/mac vendors. Allowing it to detect MITM attacks, scans, exfiltration, port scans, long connections, data uploads, unknown ports, connections without DNS, malicious JA3/JA3S, TLS certificates, etc.

An LSTM neural network detects C&C channels, a Random Forest is used to detect attacks on flows, and anomaly detection methods are used on the traffic. A final ML ensembling algorithm is used for blocking decisions and alert generation.

Slips reads packets from an interface, PCAPs, Suricata, Zeek, Argus and Nfdump. It generates alerts in text, json, and using the STIX/TAXII protocol, sending to CESNET servers using IDEA0 format, or to Slack.

Slips is the first IDS to use its own local P2P network to find other Slips peers and exchange data about detection using trust models that are resilient to adversarial peers.

The Kalipso Node.js and a Web interface allows the analysts to see the profiles' behaviors and detections performed by Slips modules directly in the console. Kalipso displays the flows of each profile and time window and compares those connections in charts/bars. It also summarizes the whois/asn/geocountry information for each IP in your traffic.


### [SmogCloud: Expose Yourself Without Insecurity - Cloud Breach Patterns](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Do you know what is internet accessible in your AWS environments? The answer and methodology of how you arrive at the answer may be the difference between missing critical exposures and complete situational awareness. Dynamic and ephemeral exposures are being created on an unprecedented level and your old generation of tools, techniques, and internet scanners can't find them. Let us show you how to find them and what it means for the future of unwanted exposures. A comprehensive asset inventory is step one to any capable security program. What does having an accurate inventory mean to an AWS administrator and ongoing security engineering effort?

Our approach involves leveraging AWS security services and metadata to translate the raw configuration into patterns of targetable services that a security team can utilize for further analysis.

In this presentation we will look at the most pragmatic ways to continuously analyze your AWS environments and operationalize that information to answer vital security questions. Demonstrations include integration between IAM Access Analyzer, Tiros Reachability API, and Bishop Fox CAST Cloud Connectors, along with a new open source tool SmogCloud to find continuously changing AWS internet-facing services.

Key Takeaways:
+ Learn how to continuously maintain an inventory of AWS services and understand their internet-exposures
+ Discover how to leverage automation from AWS Access Analyzer and a freely available open source tool from Bishop Fox to operationalize exposure testing
+ See practical demonstrations of how engineering and security teams can determine impact of their security group configurations


### [Splunk Threat Hunting Application](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
This is a Splunk application containing several dashboards and over 120 reports that will facilitate initial hunting indicators to investigate. One of the reasons this app was created is because the endpoint is an often used entry way into a network. There are quite some Endpoint Detection & Remediation (EDR) solutions out there and most of them are quite good; however, they can be costly and not everyone is able to afford that (yet).

The goal was to create an alternative approach to the detection aspect, using the MITRE ATT&CK framework and work with the existing environment. It allows you to leverage your existing data platform, in this case Splunk.


### [StegoWiper+: A Powerful and Flexible Active Attack for Disrupting Stegomalware and Advanced Stegography](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Over the last 10 years, many threat groups have employed stegomalware or other steganography-based techniques to attack organizations from all sectors and in all regions of the world. Some examples are: APT15/Vixen Panda, APT23/Tropic Trooper, APT29/Cozy Bear, APT32/OceanLotus, APT34/OilRig, APT37/ScarCruft, APT38/Lazarus Group, Duqu Group, Turla, Vawtrack, Powload, Lokibot, Ursnif, IceID, etc.Our research shows that most groups are employing very simple techniques (at least from an academic perspective) and known tools to circumvent perimeter defenses, although more advanced groups are also using steganography to hide C&C communication and data exfiltration. We argue that this lack of sophistication is not due to the lack of knowledge in steganography (some APTs have already experimented with advanced algorithms) but simply because organizations are not able to defend themselves, even against the simplest steganography techniques.

During the demonstration we will show the practical limitations of applying existing automated steganalysis techniques for companies that want to prevent infections or information theft by these threat actors. For this reason, we have created stegoWiper, a tool to blindly disrupt any image-based stegomalware, attacking the weakest point of all steganography algorithms: their robustness. We'll show that it is capable of disrupting all steganography techniques and tools (Invoke-PSImage, F5, Steghide, openstego, ...) employed nowadays. In fact, the more sophisticated a steganography technique is, the more disruption stegoWiper produces. Moreover, our active attack allows us to disrupt any steganography payload from all the images exchanged by an organization by means of a web proxy ICAP (Internet Content Adaptation Protocol) service, in real time and without having to identify which images contain hidden data first.

After our presentation at BlackHat USA 2022 Arsenal we have been working on supporting, disrupting, state-of-the-art advanced algorithms available in the academic literature, based on matrix encryption, wet-papers, etc. (e.g. Hill, J-Uniward, Hugo). Especially we have paid attention to the YASS algorithm (https://pboueke.github.io/CryptoStego/) resistant to numerous active attacks and commercial CDR-type software. Finally our tool is able to defeat them.


### [Stop Wasting Time: Use Falco Plugins to Extend Detection with any Event Stream](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Data leaks can cost companies a fortune, storing millions of logs which "might" come in handy in the future. The majority of the time, only a small portion of those logs are actually useful in the event of a security investigation. Using newly developed Falco plugins, you can generate live events for the point in time you are interested in and forward those for further analysis, speeding and simplifying incident response.

Falco is a CNCF open source container security tool designed to detect anomalous activity in your local machine, containers, and Kubernetes clusters. It taps into Linux kernel system calls and Kubernetes Audit logs to generate an event stream of all system activity. Thanks to its powerful and flexible rules language, Falco will generate security events when it finds malicious behaviors as defined by a customizable set of Falco rules.

The recent major Falco update introduced support of Falco Plugins, opening Falco to a new world of data that Falco can handle and process. This new approach allows users to create and integrate different types of Falco plugins and extend the Falco detection engine with new event sources and generate security events using Falco rules. The event sources that can be integrated in Falco are infinited. AWS CloudTrail, Docker, and Video Stream are already available, and the Falco community is already working on new plugins to integrate new event sources.

During this talk, we show the new Falco plugins approach and how you can use it in real breaches. The recent OKTA breach is a perfect example. By developing the related plugin and Falco rules for OKTA events, it was possible to detect and get an immediate alert if something anomalous happened in your environment.


### [Strafer: A Tool to Detect Infections in Elasticsearch Instances](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Elasticsearch infections are rising exponentially. The adversaries are exploiting open and exposed Elasticsearch interfaces to trigger infections in the cloud and non-cloud deployments. During this talk, we will release a tool named "STRAFER" to detect potential infections in the Elasticsearch instances. The tool allows security researchers, penetration testers, and threat intelligence experts to detect compromised and infected Elasticsearch instances running malicious code. The tool also enables you to conduct efficient research in the field of malware targeting cloud databases.




In this version of the tool, the following modules are supported:

Elasticsearch instance information gathering and reconnaissance
Elasticsearch instance exposure on the Internet
Detecting potential ransomware infections in the Elasticsearch instances
Detecting potential botnet infections such as meow botnet.
Detecting infected indices in the Elasticsearch instances

Note: This is the first release of the tool and we expect to add more modules in the nearby future.


### [Streamlining and Automating Threat Hunting With Kestrel](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Kestrel is a rapidly evolving threat hunting language designed to accelerate cyber threat hunting by providing a layer of abstraction to build reusable, composable, and shareable hunt-flow. It brings two key innovations to the security community: (i) a composable way expressing threat hypothesis development over entity-relational data abstractions, and (ii) an open-source language runtime generating and executing repetitive hunt instructions on local hunting sites, remote data sources, and in the cloud. Kestrel significantly simplifies hunting and sharing by creating a standard way to encode a single hunt step, chain multiple hunt steps, and fork/merge hunt-flows to develop threat hypothesis. It focuses threat hunters on the reusable business logic of hunt, other than writing multiple endpoint query languages, understanding incompatible query results, and converting analytics and visualization for each specific hunt.

This arsenal session will showcase the latest language development and community opportunities for Kestrel. We will start with powerful federated data retrieval using the Structured Threat Information eXpression (STIX) standard and STIX-shifter and lift the results into an entity-relational data model. Then we will showcase analytic hunt steps besides data retrieval steps, compare the new Python analytics interface with the container-based interface, and execute analytics for context enrichment, de-obfuscation, and visualization. After creating, executing, saving, and re-executing huntbooks, we will connect Kestrel with the Open Command and Control (OpenC2) standard to respond to "investigate" commands and automate huntbook execution, data gathering, false positive elimination, and comprehensive analysis.

Making it ready to try by the audience, we will demonstrate live hunts in Jupyter Notebooks launched and executed in a Binder cloud sandbox as part of a purple team exercise. At the end of the session, we will introduce the kestrel-huntbook repo for people to reuse existing huntbooks and share their hunting knowledge with their colleagues and other hunters in the community.


### [SubParse - Malware Artifact and Correlation Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
SubParse is a modular framework designed for the automation of malware analysis using static and dynamic analysis, external threat intelligence sources and historical data/event correlation. The novelty of this approach comes in the correlation of extracted data to not only assist in identification of current samples, but also in correlating any facet of information with other samples stored within the framework. Data will be accessible through an intuitive web-based user interface which offers a comprehensive filter syntax sub-system.

Static file identification and parsing is the entry point into the framework. Currently, the scope of the framework is to support Windows-based portable executable (PE) files and Linux executables (ELF). However, the modularity of the framework allows for the easy integration of additional file parsers through plugins. Static file characteristics can be extracted using file format parsing, such as: file hashes, compile time, version information, code entry address, and section information. Across a larger sample set these attributes can offer unique views into threat actor operations and allow for the correlation of previously uncorrelated samples.

Analysis can be further enriched using enricher plugins. After completion of the static file parsing, the framework looks for any enabled enrichers. Enrichers provide an open-ended opportunity to gather additional data about the sample and add it to the framework. For example, an enricher that utilizes services provided by Abuse.ch can provide additional insight into malware behavior.

Another key enricher provides dynamic analysis. The framework will orchestrate dynamic analysis using a CAPEv2 sandbox. Dynamic analysis will provide behavioral insights into the malware, such as process activity, memory allocations and network activity. These results will be exported from CAPE and correlated with the sample within SubParse. For these artifacts, they will be submitted to the framework for full analysis and correlated to the original sample.


### [Suricata: An Open-Source IDS/IPS/NSM Engine](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Suricata is a free and open-source, mature, fast, and robust network threat detection engine. The Suricata engine is capable of real-time intrusion detection (IDS), inline intrusion prevention (IPS), network security monitoring (NSM), and offline PCAP processing.

Suricata inspects the network traffic using a powerful and extensive rules and signature language, and has powerful Lua scripting support for detection of complex threats. With standard input and output formats like YAML and JSON integrations with tools like existing SIEMs, Splunk, Logstash/Elasticsearch, Kibana, and other database become effortless.

Suricata's fast-paced community driven development focuses on security, usability, and efficiency.

The Suricata project and code are owned and supported by the Open Information Security Foundation (OISF), a non-profit foundation committed to ensuring Suricata's development and sustained success as an open source project.


### [SysmonX: An Augmented and Community-Driven Drop-In Replacement of Sysmon](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Sysmon is a free and powerful host-level tracing tool, developed by an epic team at Microsoft, which has been widely adopted and deployed by defenders over the last few years. The tool provides a free alternative for those who want to augment the Microsoft Windows Auditing Capabilities, effectively enabling them to detect anomalous endpoint behaviors and to perform threat-hunting activities over the collected data.

Despite providing a lot of features, Sysmon main disadvantage is around its closed-source nature. Not having the ability to extend the tool data collection or to extend the way that the tool filters, aggregate and logically correlate events are impacting on the tool's ability to keep up with the current threat landscape. What is more, the infosec community is not empowered to fix the well-known subversion and evasion techniques created to bypass tool auditing (i.e Matt Graeber talk at BH USA 18).

Introducing SysmonX: SysmonX is an open-source, community-driven, and drop-in replacement version of Sysmon that provides a modularized architecture with the purpose of enabling the infosec community to:

Extend the Sysmon data collection sources and create new security events
Extend the Sysmon ability to correlate events. Effectively enabling new logical operations between events and the creation of advanced detection capabilities
Enrich the current set of events with more data!
Enable the false positive reduction by narrowing down suspicious events through dedicated scanners
Extend the security configuration schema
React to known subversion and evasion techniques that impact Sysmon, and by doing so, increasing the resilience of security auditing and data collection mechanism such as this one.

SysmonX is composed of a standalone binary that gets itself deployed as a windows service, supports legacy Sysmon configurations and event reporting mechanism, while also providing users the ability to configure all the SysmonX aspects through command-line interface. The SysmonX binary is a drop-in replacement of Sysmon. This effectively means that SysmonX is a feature-compatible version of Sysmon (same input, same output). This is possible thanks to the SysmonX ability to package, deploy, manage Sysmon binaries behind the scene. SysmonX uses this to intercept data collected by Sysmon drivers, enrich them, along with the ability to create, combine, and add scanning logic on top of new security events. The result is a combined output, with the old good features from Sysmon + the new features from SysmonX.

Example of new security events and features added to SysmonX are:

Cmdline and Parent Process Spoofing detection
WMI calls over all the namespaces, not just root:subscription
Ability to collect authentication information
Ability to collect powershell events
Ability to collect DNS lookups
Ability to detect userspace injection techniques (eventing + memory inspection through built in scanner modules)
Ability to perform regex over security event fields
Many more!

Source Code: https://github.com/marcosd4h/sysmonx


### [T3SF (Technical TableTop Exercises Simulation Framework)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
T3SF is a framework that offers a modular structure for the orchestration of events from a master scenario events list (MSEL) together with a set of rules defined for each exercise and a configuration that allows defining the parameters of the correspondent platform. The main module performs the communication with the specific module (Discord, Slack, Telegram, WhatsApp, Teams, etc.) which allows the events to be presented in the input channels as injects for each platform. Also, the framework supports different use cases: single organization-multiple areas, multiple organization-single area, and multiple organization-multiple areas. It has been successfully tested in exercises with international companies, which allowed us to validate its commercial level.

Tabletop exercises have 2 approaches: traditional (scenarios with discussion) and modern (automatic events on a platform). The 1st platform was funded by the DHS (USA) with USD20 MM over 10 years. In 2021 we proposed a novel approach using free collaborative platforms, which allowed the development of a free and open source framework.

The original research paper presented and published at the IEEE ARGENCON 2022 academic congress, under the title "Cybersecurity Incident Response Simulation for Organizational and Classroom Learning." (preprint available at IEEE TechRxiv).

The tool itself was first presented and released in the most important cybersecurity conference in Spain (RootedCon 2022) and then updated and presented in the most important cybersecurity conference in Latin America (Ekoparty 2022, video available on YouTube). Then it was presented at FIRST Technical Colloquium Amsterdam 2023 (April) and BlackHat Asia Arsenal 2023.

This version is a major update that includes new features like a better GUI frontend for configuration and scenario setup, an automatic inject creation engine based on a given set of parameters (design decisions) and real time interactions based on ChatGPT predefined prompts.


### [TSURUGI LINUX - the sharpest weapon in your DFIR arsenal](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Any DFIR analyst knows that everyday in many companies, it doesn't matter the size, it's not easy to perform forensics investigations often due to lack of internal information (like mastery all IT architecture, have the logs or the right one...) and ready to use DFIR tools.

As DFIR professionals we have faced these problems many times and so we decided last year to create something that can help who will need the right tool in the "wrong time" (during a security incident).

And the answer is the Tsurugi Linux project that, of course, can be used also for educational purposes.
A special Tsurugi Linux BLACKHAT EDITION will be shared only with the participants.


### [Telegrip Forensic Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [Telfhash: Hunting IoT elves](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Telfhash is an architecture-agnostic hash based on symbols of ELF files. It can also cluster ELF files with no symbols based on a creative algorithm to cluster them. Designed as a Python library, Telfhash is also shipped with a command-line tool that allows malware researchers to correctly group similar ELF files together. In this demo I'll show you how Telfhash works and how to extract the most of it while conducting malware investigations that involves ELF files, which is a common situation in this IoT/non-PC malware era.


### [The Big zBang Theory: Active Directory Risk Assessment](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
zBang is an Active Directory Risk Assessment tool that alerts against five different Active Directory attack vectors: ACLight, Skeleton Key, SID History, Risky SPN, and Mystique.

Organizations and red-teamers should utilize zBang to identify potential attack vectors and improve the security posture of the network. The results can be analyzed with a graphic interface specifically designed for the tool.

The new zBang tool discovers critical findings like:

The most privileged accounts that must be protected, including suspicious Shadow Admins.
Possible infected DCs with the "Skeleton Key" malware.
Suspicious SID history with hidden privileges.
Risky configurations of SPNs that might lead to credential theft of domain admins.
Risky Kerberos delegation configurations in the network.

The scans do not require any extra privileges; the tool performs read-only LDAP queries to the DC and can be run using any domain user.


### [The Eye of Falco: You can escape but not hide](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Container technologies rely on features like namespaces, cgroups, SecComp filters, and capabilities to isolate different services running on the same host. However, SPOILER ALERT: container isolation isn't bulletproof. Similar to other security environments, isolation is followed by red-teamer questions such as, "How can I de-isolate from this?"

Capabilities provide a way to isolate containers, splitting the power of the root user into multiple units. However, having lots of capabilities introduces complexity and a consequent increase of excessively misconfigured permissions and container escape exploits, as we have seen in recently discovered CVEs.

Falco is a CNCF open source container security tool designed to detect anomalous activity in your local machine, containers, and Kubernetes clusters. It taps into Linux kernel system calls and Kubernetes Audit logs to generate an event stream of all system activity. Thanks to its powerful and flexible rules language, Falco will generate security events when it finds malicious behaviors as defined by a customizable set of Falco rules.

The recent Falco update introduced the feature to keep track of all the syscalls that may modify a thread's capabilities, modifying its state accordingly, allowing Falco to monitor capabilities assigned to processes and threads. This new feature allows users to create detection over those malicious misconfigurations and automatically respond by implementing actions to address the issue

In this talk, we explain how you can use Falco to detect and monitor container escaping techniques based on capabilities. We walk through show real-world scenarios based on recent CVEs to show where Falco can help in detection and automatically respond to those behaviors


### [The Mathematical Mesh](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The Mathematical Mesh is a Threshold Key Infrastructure that allows cryptographic applications to provide effortless security. Threshold key generation and threshold key agreement are used to provide end-to-end security of data in transmission and data at rest without requiring any additional user interactions.

Once a device is connected to a user's personal Mesh through a simple, one-time configuration step, all private key and credential management functions are automated. Devices may be provisioned with private keys required to support applications such as OpenPGP, S/MIME and SSH according to intended use of that device.


### [ThreatPatrol](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
ThreatPatrol is a powerful open-source SaaS tool that offers Blue Teams a wealth of information on potential threats, allowing them to gain situational awareness and perform threat hunting. The tool's flexibility is a significant advantage, as it can be hosted on the cloud or on an internal standalone machine, providing users with the convenience and customisation options they need.

ThreatPatrol offers a comprehensive database of over 160 threat actor groups, indicators of compromise (IOCs), tactics, techniques, and procedures (TTPs), and their modus operandi out of the box. This information is regularly updated to ensure that users have access to the latest information on potential threats, providing insights into emerging threats and enabling proactive measures to prevent cyber-attacks.

Cyber Defenders can add, update, or degrade TTPs and IOCs for their network and map them to the MITRE Framework, which can be visualised on the dashboard in graph form, and generate reports for sharing with executive members. By proactively collecting and analysing data on potential threats, cyber teams can improve their situational awareness, enabling them to take appropriate action to prevent or mitigate attacks.

ThreatPatrol also provides feeds from over 100+ different sources, allowing organisations to stay up-to-date with the latest attack methods and trends, adjust their security posture, and protect themselves better against cyber threats. With improved situational awareness, organisations can respond more quickly and effectively when incidents occur, making ThreatPatrol an essential tool for protecting valuable data and avoiding the devastating consequences of a cyber-attack.


### [ThreatScraper: Automated Threat Intelligence Gathering and Analysis from VirusTotal](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The continuous growth of malware threats necessitates efficient and comprehensive tools for tracking malware detection and propagation. VirusTotal serves as a popular platform for aggregating malware information submitted by Anti-Virus (AV) software providers, which can be searched using parameters such as hashes (SHA-1, SHA-256, MD5), file names, and malicious web links. In order to enhance and automate the process of malware intelligence gathering, we introduce ThreatScraper, a Python-based tool that automates free API queries and rescanning tasks on VirusTotal.
ThreatScraper is designed to periodically request reports on specified files and save the results in a local database. It allows users to pull and aggregate malicious file reports from multiple AV vendors over time, providing insights into the adoption of malware detection across providers. Easily implemented from any Windows command line, ThreatScraper can rescan a file, pull a report, and then sleep until the next designated time identified by the user.
By leveraging ThreatScraper, developers can efficiently identify potentially malicious files, track when an AV provider has flagged a file as malicious and monitor the categorization of the file. The tool ultimately aids in enhancing threat intelligence gathering and response capabilities for users, developers, and enterprise entities.


### [Trash Taxi: Taking Out the Garbage in Your Infrastructure](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Auditors dream of a world in which they can guarantee that few possess unrestricted administrator access. Yet, developers and operations staff often need to debug complex events - that only occur with load - in production. How can we balance the need to grant occasional superuser access with the incentive to ensure changes make their way back into configuration management, while reducing the risk of configuration drift? We built Trash Taxi to help us understand why people use "sudo -i," and also clean up hosts that have had arbitrary commands run on them by "taking out the trash" as in: terminating them.


### [Tsurugi Linux Project the Right DFIR Tool in the Wrong Time](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Any DFIR analyst knows that everyday in many companies, it doesn't matter the size, it's not easy to perform forensics investigations often due to lack of internal information (like mastery all IT architecture, have the logs or the right one...) and ready to use DFIR tools.

As DFIR professionals we have faced these problems many times and so we decided last year to create something that can help who will need the right tool in the "wrong time" (during a security incident).

And the answer is the Tsurugi Linux project that, of course, can be used also for educational purposes.
After more than a year since the last release, a Tsurugi Linux special BLACK HAT EDITION with this major release will be shared with the participants before the public release.


### [Tsurugi Linux Project: The Right Tool in the Wrong Time](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Any DFIR analyst knows that everyday in many companies, it doesn't matter the size, it's not easy to perform forensics investigations often due to lack of internal information (like mastery all IT architecture, have the logs or the right one...) and ready to use DFIR tools.

As DFIR professionals we have faced these problems many times and so we decided last year to create something that can help who will need the right tool in the "wrong time" (during a security incident).

And the answer is the Tsurugi Linux project that, of course, can be used also for educational purposes.
After more than a year since the last release, a Tsurugi Linux special BLACK HAT EDITION with this major release will be shared with the participants before the public release.


### [Unprotect Project: Malware Evasion Techniques](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Malware evasion consists of techniques used by malware to bypass security in place, circumvent automated and static analysis as well as avoiding detection and harden reverse engineering. There is a broad specter of techniques that can be used. In this talk we will review the history of malware evasion techniques, understand the latest trends currently used by threat actors and bolster your security analysis skills by getting more knowledge about evasion mechanisms.

We will present the latest major update of the Unprotect Project an open-source documentation about malware evasion techniques. The goal will be to present the project and see how we can leverage it for use cases, including threat intelligence, malware analysis, strengthen security, train people, and extend the Mitre ATT&CK matrix. Over the years it has become a well renowned place for security researchers. During this talk we will review some of the most important update.

This presentation can benefit both Blue and Red Team as it will provide knowledge and information on how malware can bypass your security in place and stay under the radar. You will learn about the intrinsic mechanisms used by attackers to compromise you without you even realizing it!


### [Unprotect Project: Unprotect Malware for the Mass](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
To perform malicious actions, attackers create malware; however, they cannot achieve their goals unless their attempts remain undetected. There is a cat and-mouse game between defenders and attackers, which includes attackers monitoring the operations of security technologies and practices.

The Unprotect Project is an open-source project that aims to propose a complete classification about Evasion Techniques to help to understand and analyze a malware. This project is dedicated to Windows PE malware but will be extended to other platforms in the future.

Presentation Slides: https://drive.google.com/file/d/1koZ5emW2vu9o3gvWdaWZx_mz90bD3rSH/view


### [Using Dorothy to Test Okta SSO Visibility and Detection](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [VECTR: Purple Teams Simulation Platform](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
VECTR is a free tool and platform designed to facilitate your red and blue security teams through comprehensive purple team threat simulations. Document your attacks, develop metrics, gauge the effectiveness of your defensive tools, and improve your detection capabilities through historical performance tracking. We'll demo how to operationalize your purple teams and show measurable progress of your program with live test cases and simulations.


### [VirusTotal Graph: Investigation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
VirusTotal Graph is a free visualization tool built on top of the VirusTotal data set. It understands the relationship between files, urls, domains and ip addresses and it provides an easy interface to pivot and navigate over them. The tool is available for individual researchers and security professionals.

By exploring and expanding each of the nodes in your graph, you can build the network and see the connections across the samples you are studying. By clicking on the nodes, you can see at a glance the most relevant information for each item. You can also add labels and see an in-depth report by going to VirusTotal Public or VirusTotal Intelligence report.

The tool can also save a snapshot -as you see in your screen- of the graph, so that you can go back to your investigation any time and share your findings with other users. All saved graphs are public and linked in VirusTotal public report when the file, URL, IP address or domain appear in the graph. This intelligence benefits the entire community.

Learn more here: http://blog.virustotal.com/2018/01/virustotal-graph.html

Demo video: https://www.youtube.com/watch?v=QEqHXU04IkI&feature=youtu.be


### [VoIP Wireshark Attack-Defense Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
VoIP Wireshark Attack-Defense Toolkit is a collection of Wireshark plugins which enables a pentester to analyze VoIP traffic. The toolkit can provide summary of VoIP traffic, automatically decrypt VoIP calls wherever possible, export the call audio to popular formats, detect attacks/misconfigurations, and highlight the DTMF/SMS interactions. This eliminates the need for a separate software/framework to analyze VoIP traffic. The plugins are written in Lua and are easy to add to Wireshark. And, the toolkit, just like Wireshark, is platform independent.


### [Vovk - Advanced Dynamic Yara Rule Generator](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Vovk - Debugging module for Advanced Dynamic Yara Rule Generation.
Vovk is a dynamic analysis tool that can be used as a module with the debugger (WinDBG). The tool itself is a DLL, built using both WdbgExts and DbgEng frameworks.
The way the tool works is pretty straightforward. You load Vovk into the debugger and then execute it. It runs through the malware and collects code snippets from memory and writes them to Yara file as a complete ruleset on the disk. You can then use the generated Yara ruleset to contain and neutralize malware campaigns or simply respond to security incidents that you are working on.


### [WEB SIGHT - ENTERPRISE ATTACK SURFACE CARTOGRAPHY](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Web Sight is a platform that automates the process of enumerating enterprise attack surface at scale. Starting with IP addresses, domain names, and networks, Web Sight can quickly enumerate subdomains, collect DNS records, run network scans, analyze SSL/TLS certificates and protocol support, and perform network service fingerprinting and application-layer inspection. The end goal of this information gathering process is to provide users with the situational awareness required to successfully attack and/or defend target organizations.


### [Weapons of Office Destruction: Prevention with Machine Learning](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The broad-brush popularity of Microsoft (MS) Office documents led them to become one of the main cyber-attacking vectors to spread malware via email attachments or web downloads. The first major outbreak of its kind is the notorious macro-based malware "Melissa" during the turn of last century and this century. Since 2014 we started to see rising weaponized Office documents, particularly visual basic application (VBA) macro-based attacks (banking Trojan like "Dridex" or ransomware such as "Locky"). According to a Sophos report in 2017, over 80% of document-based malware were delivered via MS Word or Excel files. Even though these attacks are not new in nature, the increasing volume and complexity of the attacks impose huge challenges to traditional signature-based anti-virus (AV) products.

As a countermeasure, AV companies have spent an enormous amount of effort creating heuristic rules over decades for signature-based detection. To better leverage the rules already used in traditional AV solutions, we propose to combine them statistically using a simple random forest-based machine learning (ML) classifier. In this demonstration, a comprehensive list of over 3000 existing heuristic rules is used to train the ML model. The training data feed comprises around 92600 real-world benign and malicious MS Office documents including Word, Excel and PowerPoint file formats. The testing datasets include 17929 malicious files and 12511 benign files collected recently. Evaluation results indicate that the proposed approach exhibits enhanced performance and significantly outperforms eleven well known commercial anti-virus scanners with a much higher true positive rate (TPR) of 98.46% achieved while maintaining a low false positive rate (FPR) of 0.33%. Of the evaluated commercial AV scanners, the best one achieves only a TPR of 87.5%, which is more than 10% lower than the proposed ML model.


### [White Phoenix - Beating Intermittent Encryption](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Intermittent Encryption (aka Partial Encryption) is a new trend in the world of ransomware. It's been adopted by many notorious groups such as BlackCat Ransomware, Play Ransomware and more. Altogether, the groups using intermittent encryption have successfully targeted hundreds of organizations in 2022 alone. However, even though intermittent encryption has its advantages, it leaves much of the content of targeted files unencrypted. In this talk, we will demonstrate a tool that uses this limitation to recover valuable data, such as text and images from documents encrypted by these groups, allowing the victims to recover some of their lost data.


### [Wireshark Forensics Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Wireshark is the most widely used network traffic analyzer. It is an important tool for both live traffic analysis & forensic analysis for forensic/malware analysts. Even though Wireshark provides incredibly powerful functionalities for protocol parsing & filtering, it does not provide any contextual information about network endpoints. For a typical analyst, who has to comb through GBs of PCAP files to identify malicious activity, it's like finding a needle in a haystack.

Wireshark Forensics Toolkit is a cross-platform Wireshark plugin that correlates network traffic data with threat intelligence, asset categorization & vulnerability data to speed up network forensic analysis. It does it by extending Wireshark native search filter functionality to allow filtering based on these additional contextual attributes. It works with both PCAP files and real-time traffic captures.

This toolkit provides the following functionality
- Loads malicious Indicators CSV exported from Threat Intelligence Platforms like MISP and associates it with each source/destination IP from network traffic
- Loads asset classification information based on IP-Range to Asset Type mapping which enables filtering incoming/outgoing traffic from a specific type of assets (e.g. filter for 'Database Server', 'Employee Laptop' etc)
- Loads exported vulnerability scan information exported from Qualys/Nessus map IP to CVEs.
- Extends native Wireshark filter functionality to allow filtering based severity, source, asset type & CVE information for each source or destination IP address in network logs


### [YAMA: Yet Another Memory Analyzer for Malware Detection](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
YAMA is a system for generating tools that can inspect whether specific malware is present in memory during incident response. While numerous security countermeasure products exist for malware detection, targeted attacks utilizing malware that operates only in memory remain challenging to detect using existing products and continue to pose a threat.
Looking at existing open-source software (OSS) projects, some, such as PeSieve and Moneta, perform memory scans on live memory. However, few offer detection methods specifically tailored to particular malware for live systems. As file-less malware threats increase, having the means to verify the presence of malware in memory across multiple endpoints becomes crucial in incident response.
Using our proposed YAMA system, the scanner generated can create memory scanners tailored explicitly to any malware. The scanner generated by YAMA is a standalone executable capable of running on most 64-bit Windows OS. When infection investigation of malware present only in memory is required during incident response, executing the scanner created by YAMA on the suspected device will easily detect whether it is infected. Furthermore, in cases where a large-scale infection is suspected, the scanner can be distributed via Active Directory (AD) to clarify the infection status within the network.
YAMA is expected to be a powerful support tool for enhancing the investigative capabilities of Blue Teams, who conduct incident response daily.


### [YAWNING-TITAN](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
YAWNING-TITAN is an abstract, graph based cyber-security simulation environment that supports the training of intelligent agents for autonomous cyber operations. YAWNING-TITAN focuses on providing a fast simulation to support the development of defensive autonomous agents who face off against probabilistic red agents. YAWNING-TITAN has been designed with the following things in mind:

• Simplicity over complexity;
• Minimal Hardware Requirements;
• Operating System agnostic;
• Support for a wide range of algorithms;
• Enhanced agent / policy evaluation support;
• Flexible environment and game rule configuration;
• Generation of evaluation episode visualisations (gifs).

YAWNING-TITAN contains a small number of specific, self-contained OpenAI Gym environments for autonomous cyber defence research, which are great for learning and debugging; it also provides a flexible, highly configurable generic environment which can be used to represent a range of scenarios of increasing complexity and scale. The generic environment only needs a network topology and a settings file to create an OpenAI Gym compliant environment which enables open research and enhanced reproducibility.

When training and evaluating an agent, YAWNING-TITAN can be run from either a command-line interface, or a graphical user interface (GUI). The GUI allows the underlying Python to be executed without need for a command line interface or knowledge of the python language. The GUI also integrates with a customised version Cytoscape JS which has been extended to work directly with YAWNING-TITAN, and allows users to directly interface with network topologies that subsequently updates a database of stored networks. Both the command-line interface and the GUI provide read-outs throughout agent training and evaluation, as well as generation of a final summary.


### [Zhouhe: Threat Analysis and Detection of Network Traffic](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Today, the malicious behavior of hackers is aimed at all kinds of terminals, servers, and websites. Sadly, when the hacker came, did something, and took away what we didn't know, in many cases. However, no matter what the hacker did, his behavior in the network could not be erased. Zhouhe is a free tool/platform, it has detection rules and machine learning algorithms maintained by a team of experts to detect threats, it provides network threat analysis and detection capabilities. You only need to upload traffic files to let you quickly understand the threats and malicious behaviors in the network.


### [capa: Automatically Identify Malware Capabilities](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
capa is an open-source tool that detects capabilities in programs to reduce the time-to-triage and make malware analysis more accessible. Anyone dealing with potentially malicious programs and especially forensic, intelligence, and malware analysts can use capa to understand a sample's capabilities, role (downloader, backdoor, etc.), and any suspicious or unique functionality.
capa takes automated malware triage to the next level going from simply saying "this is probably bad" to providing a concise description of what a program actually does. This report provides critical, decision-making information to anyone dealing with malware.

capa uses a new algorithm that reasons over the features found in a file to identify its capabilities. The lowest level features range from disassembly tricks to coding constructs, while intermediate features include references to recognized strings or API calls. Users compose rules that train capa how to reason about features – and even the significance of other rules. This makes it easy for the community to extend the tool's abilities.

We will describe how and why our tool works. We will also show to use it to enhance every malware analysis workflow. Furthermore, you will learn how to develop capability detections that extend capa.


### [eBPFShield: Advanced IP-Intelligence & DNS Monitoring using eBPF](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
eBPFShield is a powerful security tool that utilizes eBPF and Python to provide real-time IP-Intelligence and DNS monitoring. By executing in kernel space, eBPFShield avoids costly context switches, making it a high-performance solution for detecting and preventing malicious behavior on your network. The tool offers efficient monitoring of outbound connections and comparison with threat intelligence feeds, making it an effective solution for identifying and mitigating potential threats. The tool includes features such as DNS monitoring, IP-Intelligence, and the ability to pull down public threat feeds.

Additionally, it includes a roadmap for future developments such as support for IPv6, automated IP reputation analysis using Machine Learning algorithms, and integration with popular SIEM systems for centralized monitoring and alerting.

eBPFShield is especially useful for companies and organizations that handle sensitive information and need to ensure the security of their networks. It's an efficient solution to monitor and protect servers from potential threats and it can help to prevent data breaches and other cyber attacks.


### [eBPFShield: Unleashing the Power of eBPF for OS Kernel Exploitation and Security.](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Are you looking for an advanced tool that can help you detect and prevent sophisticated exploits on your systems? Look no further than eBPFShield. Let's take a technical look at some of the capabilities of this powerful technology:

DNS monitoring feature is particularly useful for detecting DNS tunneling, a technique used by attackers to bypass network security measures. By monitoring DNS queries, eBPFShield can help detect and block these attempts before any damage is done.

IP-Intelligence feature allows you to monitor outbound connections and check them against threat intelligence lists. This helps prevent command-and-control (C2) communications, a common tactic used by attackers to control compromised systems. By blocking outbound connections to known C2 destinations, eBPFShield can prevent attackers from exfiltrating sensitive data or delivering additional payloads to your system.

eBPFShield Machine Learning feature, you can develop and run advanced machine learning algorithms entirely in eBPF. We demonstrate a flow-based network intrusion detection system(IDS) based on machine learning entirely in eBPF. Our solution uses a decision tree and decides for each packet whether it is malicious or not, considering the entire previous context of the network flow.

eBPFShield Forensics helps address Linux security issues by analyzing system calls and kernel events to detect possible code injection into another process. It can also help identify malicious files and processes that may have been introduced to your system, allowing you to remediate any security issues quickly and effectively.

During the workshop, we'll delve deeper into these features and demonstrate how eBPFShield can help you protect your systems against even the most advanced threats.


### [goKey: Reclaim Back Keys for Your Kingdom - A Vaultless Password Manager](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The password is the oldest and most widely used pillar of authentication. We use passwords everywhere: from everyday online shopping to accessing government services and managing our money. Every day, the number of online services increases and each of service most likely requires a password to use it.

On the other hand, as password-cracking techniques increase and evolve, so do the restrictions on the types of passwords we can use. It is not enough anymore to use your favourite movie as a password across all your accounts. The modern Internet threat model requires passwords to be either ridiculously long or look like random gibberish of uppercase and lowercase letters, numbers and special characters. And in NO WAY should you reuse same password on any two services. In other words, the most secure passwords are hardly memorable to ordinary people and the number of passwords you have to remember makes this task even harder.

That's where password managers kick in. Instead of remembering each password, you only have to remember the password for your password manager (the "master password"), and the password manager remembers your other passwords for you. But how? They store your other passwords in a vault (a simple encrypted database). However, as with any database, a vault requires management: you need to store it somewhere (which means more backups), sync it across all your devices (you definitely want to access your services from home/work laptops, smartphone, tablet etc). And as with any database management, there comes usability and security issues. Basically, you either have to manually update and manage the vault yourself (if you use a free open-source password manager) or rely on some kind of cloud-based service (often paid and proprietary) for that.

So it is a matter of usability vs security: either you're using a convenient proprietary password manager and have no idea if it is working as advertised, or you have more confidence in your open-source password manager, but have to deal with your vault yourself.

Wouldn't it be great to have a password manager without a vault? We would no longer have to manage vaults or rely on any third parties. This presentation introduces an open-source vaultless password manager, which does not store your passwords, but rather derives them from the master-password in a cryptographically secure manner. There is an option to generate secure cryptographic keys so that your passwords/keys are never stored anywhere, but can be reliably regenerated when needed.


Presentation: https://drive.google.com/file/d/1B5CXRaTzG8yYTW6sN9L70GW3NBLpZVJb/view?usp=sharing
GitHub: https://github.com/cloudflare/gokey


### [h0neytr4p - How to catch the external threat actors with an easy to configure Honeypot.](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Working for large clients, we realised that large enterprises don't have any mechanism to trap external threat actors primarily exploiting web vulnerabilities. They are still reliant on threat intel firms to block potential attacker IPs. Sure, there are honeypots but it's really hard and time taking to configure. The turnaround time for SOC teams to configure a honeypot for a recently disclosed vulnerability is very high, discouraging the use of the same. We aim to fix this by introducing a template based honeypot. Honeytrap is stateless, it understands patterns and it can be configured to catch complicated 0day or 1day vulnerability exploitation attempts within minutes. It empowers and encourages blue teams to put an active honeytrap network around the network which can be used to capture Indicators of compromise that can be used to block at the perimeter firewall. h0neytr4p comes in a light weight single binary deployment mode, takes either one or multiple templates as input and has csv output mode which can be easily piped onto custom tools. Currently, it supports HTTP and HTTPS only but the plan is to make it a unified platform that supports SSH, RDP or any other protocols spanning multiple scenarios.


### [ioc2rpz: Where Threat Intelligence Meets DNS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
DNS is the control plane of the Internet with unprecedented detailed views on applications, devices and even transferred data going in and out of a network. 80% of malware uses DNS to communicate with Command & Control for DNS data exfiltration/infiltration and phishing attacks using lookalike domains. Response Policy Zones or DNS Firewall is a feature which allows us to apply security policies on DNS. Commercial DNS Firewall feeds providers usually do not allow users to generate their own feeds. Cloud only DNS service providers do not provide feeds for on-prem DNS.

ioc2rpz is a DNS server which automatically creates, maintains and distributes DNS Firewall feeds from various local (files, DB) and remote (http, ftp, rpz) sources. This enables easy integrations with Threat Intel providers and Threat Intelligence Platforms. The feeds can be distributed to any open source and commercial DNS servers which support RPZ, e.g. ISC BIND, PowerDNS, Infoblox, BlueCat, Efficient IP etc. With ioc2rpz you can create your own feeds, actions and prevent undesired communications before they happen.

https://ioc2rpz.net is a community portal which is powered by ioc2rpz where you can try several free DNS Firewall feeds.

RpiDNS is a new feature integrated into ioc2rpz.gui which includes an installation script and a web interface to monitor and manage local secure DNS services.


### [pwnSpoof](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
None


### [rastrea2r (reloaded!): Collecting & Hunting for IOCs with Gusto and Style](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Rastrea2r (pronounced "rastreador" - hunter- in Spanish) is a multi-platform open source tool that allows incident responders and SOC analysts to triage suspect systems and hunt for Indicators of Compromise (IOCs) across thousands of endpoints in minutes. To parse and collect artifacts of interest from remote systems (including memory dumps), rastrea2r can execute sysinternal, system commands and other 3rd party tools across multiples endpoints, saving the output to a centralized share for automated or manual analysis. By using a client/server RESTful API, rastrea2r can also hunt for IOCs on disk and memory across multiple systems using YARA rules. As a command line tool, rastrea2r can easily integrate with AV consoles and SOAR tools, allowing incident responders and SOC analysts to collect forensics evidence and hunt for IOCs without the need for an additional agent, with 'gusto' and style!

Source Code: https://github.com/rastrea2r/rastrea2r
Presentation: https://github.com/rastrea2r/rastrea2r/blob/master/presentations/BH%20Arsenal%20rastrea2r%202018.pdf


### [soc-faker: A python package for use in generating fake data for SOC and security automation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
soc-faker is used to generate fake data for use by Security Operation Centers, Information security professionals, product teams, and many more.


### [stegoWiper: A powerful and flexible active attack for disrupting stegomalware](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Over the last 10 years, many threat groups have employed stegomalware or other steganography-based techniques to attack organizations from all sectors and in all regions of the world. Some examples are: APT15/Vixen Panda, APT23/Tropic Trooper, APT29/Cozy Bear, APT32/OceanLotus, APT34/OilRig, APT37/ScarCruft, APT38/Lazarus Group, Duqu Group, Turla, Vawtrack, Powload, Lokibot, Ursnif, IceID, etc.
Our research shows that most groups are employing very simple techniques (at least from an academic perspective) and known tools to circumvent perimeter defenses, although more advanced groups are also using steganography to hide C&C communication and data exfiltration. We argue that this lack of sophistication is not due to the lack of knowledge in steganography (some APTs have already experimented with advanced algorithms) but simply because organizations are not able to defend themselves, even against the simplest steganography techniques.
During the demonstration we will show the practical limitations of applying existing automated steganalysis techniques for companies that want to prevent infections or information theft by these threat actors.
For this reason, we have created stegoWiper, a tool to blindly disrupt any image-based stegomalware, attacking the weakest point of all steganography algorithms: their robustness. We'll show that it is capable of disrupting all steganography techniques and tools (Invoke-PSImage, F5, Steghide, openstego, ...) employed nowadays, as well as the most advanced algorithms available in the academic literature, based on matrix encryption, wet-papers, etc. (e.g. Hill, J-Uniward, Hugo). In fact, the more sophisticated a steganography technique is, the more disruption stegoWiper produces.
Moreover, our active attack allows us to disrupt any steganography payload from all the images exchanged by an organization by means of a web proxy ICAP (Internet Content Adaptation Protocol) service, in real time and without having to identify which images contain hidden data first.


### [tknk_scanner: Community-Based Integrated Malware Identification System](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
The original code of a malware must be scanned using YARA rules after processing with a debugger (or other means) to account for obfuscated malware binaries. This is a complicated process and requires an extensive malware analysis environment. The tknk_scanner is a community-based integrated malware identification system, which aims to easily identify malware families by automating this process using an integration of open source community-based tools and freeware. The original malware code can be scanned with with your own YARA rules by submitting the malware in PE format to the scanner. tknk_scanner can thus support surface analysis performed by SOC operators, CSIRT members, and malware analysts.


### [tshark + ELK: Network Traffic Monitoring and Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
This project builds virtual machine for network traffic monitoring and analysis. It uses ELK (Elasticsearch, Logstash, Kibana) to process Wireshark decoded output (by using tshark -T ek ndjson output). The virtual appliance is built using vagrant, with pre-installed and pre-configured ELK stack.

https://www.h21lab.com/tools/tshark-elasticsearch
https://github.com/H21lab/tsharkVM


### [vPrioritizer: Learn to say NO to almost every vulnerability (art of risk prioritisation…)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
As suggested by vulndb and cve, on a daily basis, approximately 50 new vulnerabilities become known to industry and even if an organization considers the impact rate of 10%, it’s still very challenging to manage it effectively and it’s safe to assume that count is going to increase furthermore. So with this amount organization is focusing (or should focus) on reducing the risk rather than eliminating it.

In current era, vulnerability management is (almost) equal to risk prioritisation because

- Resources (skillset and time) is limited in every organisation
- Environment is changing too fast and too frequently (ROI is less in analysis and remediation of a vulnerability if affected asset is not going to be live for a longer time - small attack surface)
- Attack surface is increasing exponentially in diversity (which again comes down to prioritisation)
- Remember the 80/20 rule - 20% of vulnerabilities bring 80% of risk

So what is risk? How do we calculate it? What are the factors contributing to risk?

1. CVSS (historically used) - No
2. Asset Criticality - No
3. Asset Accessibility - No
4. Exploit Applicability - No
5. Exploit Availability - No
6. Ease of Exploitation - No
7. Attack Surface - No
8. All of the Above - Yes

Theoretically, the above approach looks appropriate to adopt but practically it’s not possible to do it manually for every vulnerability affecting every asset by every organisation.

To overcome the above challenges I have prepared an open-source framework, vPrioritizer, which gives us ability to assess the risk on different layers such as (and hence comprehensive control on granularity of each component of risk):

- We can assign significance on per asset basis
- We can assess severity on per vulnerability basis
- At the same time, we can adjust both factors at asset & vulnerability relationship level
- On top of that, community analytics provides insights as suggested risk

This framework enables us to understand the contextualized risk pertaining to each asset by each vulnerability across the organization. It’s community based analytics provides a suggested risk for each vulnerability identified by vulnerability scanners and further strengthens risk prioritization process. So at any point of time teams can make an effective and more informed decision, based on unified and standardized data, about what (vulnerability/ties) they should remediate (or can afford not to) on which (asset/s).


### [wpa-sec: The Largest Online WPA Handshake Database](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Blue--Team--&--Detection](https://img.shields.io/badge/Category-Blue--Team--&--Detection-gray)  
Started as pet project in 2011, wpa-sec collects WPA handshake captures from all over the world. Contributors use client script to download handshakes and special crafted dictionaries to initiate attack against PSKs. With more than 115 GB captures from 240,000 submissions, collected samples represent invaluable source for wireless security research. This includes:

Many improvements for emerging wireless security tools like hcxtools suite (https://github.com/ZerBea/hcxtools)
Identified default PSK key generation algorithms, used by various ISPs. Those, along with fixes for current implementations get in RouterKeygen project (https://github.com/routerkeygen/routerkeygenPC). Many more to come, based on current research activities
Performance optimizations for WPA crackers
Identified some linux kernel driver bugs

Live installation: https://wpa-sec.stanev.org
GitHub: https://github.com/RealEnder/dwpa﻿
Presentation: https://alex.stanev.org/presentations/en/BlackHatUSA2018_DEFCON26-PHV_wpa-sec_AlexStanev.pdf


---

## Social Engineering / General


### [A DECEPTICON and AUTOBOT walk into a bar: A NEW Python tool for enhanced OPSEC](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
When we see the terms Natural Language Processing (NLP) or Machine Learning (ML), often, our guts are correct, and it is vendor marketing material, frequently containing FUD. After tinkering with various libraries in Python and R with the use of some OSINT and SOCMINT techniques, I have found a use for NLP and ML that is 100% FUD free in the form of a brand new, Python-based tool.

In this presentation, which goes further than the previous DECEPTICON presentation, we address topics that I have frequently spoken about in past years is disinformation, deception, OSINT, and OPSEC. When working through learning NLP and ML in Python, it dawned on me: marry these technologies with DECEPTICON for good. Enter the DECEPTICON bot. The DECEPTICON bot is a python* based tool that connects to social media via APIs to read posts/tweets to determine patterns of posting intervals and content then takes over to autonomously post for the user. What is the application you ask: people who are trying to enhance their OPSEC and abandon social media accounts that have been targeted without setting off alarms to their adversaries. Use case scenarios include public figures, executives, and, most importantly – domestic violence and trafficking victims.


### [AiCEF: An AI-powered Cyber Exercise Content Generation Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
The core idea of AiCEF, is to harness the intelligence that is available from online and MISP reports, as well as threat groups' activities, arsenal etc., from, e.g., MITRE, to create relevant and timely cybersecurity exercises. To this end, we have developed a specialised ontology called Cyber Exercise Scenario Ontology (CESO), which extends STIX [2]. The core idea is to map reports; both from online resources and MISP, via a common ontology to graphs. This way, we abstract the events from the reports in a machine-readable form. The produced graphs can be infused with additional intelligence, e.g. the threat actor profile from MITRE, also mapped in our ontology. While this may fill gaps that would be missing from a report, one can also manipulate the graph to create custom and unique models. Finally, we exploit transformer-based language models like GPT to convert the graph into text that can serve as the scenario of a cybersecurity exercise.
We have tested and validated AiCEF with a group of experts in cybersecurity exercises, and the results clearly show that AiCEF significantly augments the capabilities in creating timely and relevant cybersecurity exercises in terms of both quality and time.


### [Amini Project](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
The AirTag IoT device is a tracking tool developed by Apple and designed to help people find misplaced objects. However, even when Apple states that AirTag technology is solely used for tracking items, a growing number of malicious individuals are taking advantage for the simplicity to install it and set up to track unaware targets, in other words, people.

Amini is a specialized open-source hardware project to scan, detect, spoof, and play a sound for AirTag devices. This project is part of "Spy-wear: Misuse of Apple AirTags" research where we analyzed a privacy concern about AirTag misuse for tracking capabilities. It was designed to be implemented with Arduino environment, for flexible designs, and to be used in any Arduino-supported devices with BLE capabilities.


### [Faceless - Deepfake detection](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
Faceless is a deepfake detection system.

The proposed deepfake detection model is based on the EfficientNet structure with some customizations. It is hoped that an approachable solution could remind Internet users to stay secure against fake contents and counter the emergence of deepfakes.
The deepfake dataset were used in the final model is Celeb-DF


### [From Boar to More: Upgrading Your Security with Trufflehog's Terminal UI](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
Trufflehog is an open-source tool that helps organizations detect sensitive data leaks across their software development life cycle. It identifies text with potentially sensitive information and verifies if they are actually secret keys or passwords, reducing false-positive noise that often leads to alert fatigue.

Previously Trufflehog required command-line interface expertise and familiarity, which could be challenging to non-technical users. A new feature was recently added to provide a terminal user interface (TUI), enhancing accessibility for individuals with varying levels of technical expertise. Easy-to-use tooling contributes to a collaborative security culture that ultimately empowers individuals to engage in and improve their organization's security posture. Trufflehog's TUI enables anyone, regardless of technical skills, to scan for secrets across their organization and be a hero.


### [Ghostwriter](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
Ghostwriter is a part of your team. It enables collaborative management of penetration test and red team assessments. It helps you manage the critical pieces of every project, including client information, project plans, infrastructure, findings, and reports in one application.

Since its debut at BHUSA Arsenal in 2019, Ghostwriter has grown and matured. Last year was a building year for the project. Now, the development team is excited to re-introduce Ghostwriter with new features to be rolled out in Q1 and Q2 2022 – such as a new GraphQL API! This new version gives teams the power to manage their projects via the API layer and custom scripts or integration with third-party projects.


### [ISTHISLEGIT](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
When it comes to mitigating phishing, visibility is half the battle. Knowing what phishing attacks are hitting your organization is key to stopping them. Users can be an incredible source of alerting for phishing emails, but they often don't know where to report the emails. Also, having the ability to collect, correlate, and auto-respond to these reports is key to stopping attacks as quickly they come in. These are problems solved by IsThisLegit for free via open-source, unlike any somewhat similar but cost-prohibitive offerings out there.

IsThisLegit is a Chrome extension and web application dashboard (leveraging Google App Engine) designed to support the management of phishing response for end-users and admins. By rolling out the Chrome extension, users will see a button in Gmail that allows them to easily report phishing emails to their security team with a single click. Now there's no need for users to remember which email address they need to send reports to. The email is then automatically reported and deleted from their inbox.

Once submitted, admins can then use the dashboard to rapidly analyze reported emails, identify phishing trends, categorize phishing emails, and set up auto-response rules.This allows the security team to quickly identify and respond to ongoing attacks.

This demo will be unique for Arsenal because it covers the full lifecycle of phishing mitigation with the 'holy trinity' of tools (all developed by the Duo Labs team). These three distinct open-source tools work together seamlessly to test and train users (Gophish), help protect/take the burden off of users by making it more difficult for attackers (Phinn), and make reporting incidents as easy as a click of the button (IsThisLegit).



https://github.com/duo-labs/isthislegit


### [King Phisher: A Phishing Campaign Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
King Phisher is a phishing toolkit created to meet the highly customized and flexible needs that offensively-focused security testers require. It boasts a wide range of features to facilitate it's use both on offensive, breaching-centric engagements as well as for user awareness training.

This arsenal demonstration will show the newer features that have been added to King Phisher in recent years. Viewers will see the latest campaign improvements including from the template selection process to gathering MFA tokens, validating submitted credentials and the Let's Encrypt integration. By integrating with Let's Encrypt through certbot, users are able to quickly and easily issue certificates for, and enable HTTPS for their phishing sites. Finally, viewers will see a demonstration of the newest plugins for campaign data management, the usage of various alerting services and finally SPAM evasion.

Source code: https://github.com/securestate/king-phisher


### [Phishing Simulation Assessment](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
People in IT eco-system are becoming 'favorite' targets because, 1. they remain weakest link and 2. organisation are becoming mature in securing technology. For a security tester, it is a daunting task to set up a phishing campaign, which includes, decide a look-alike domain, buy it, setup a phishing website with infrastructure, design an email and choose target audience, track the open/click/download and build the analytics. All of these activities are time-consuming and demands a certain skill-set.

Phishing Simulation provides one-stop-solution for organisation to understand security awareness posture without actually performing 'live' phishing attack. Phishing Simulation prepares phishing assessment with tailor-made questions specific to organisation, facilitates target users to complete the assessment, provides an intuitive tutorial and builds the analytics on basis of responses and the meta-data collected about user.

Phishing Simulation has 2 modules:
Admin Module: This module will be used by tester to setup and monitor phishing assessments
- On the basis of inputs provided by tester like organisation name, email ID, domain name, tool automatically generates questions with tailor-made data such as look-alike domains using typo-squatting technique, spoofed sender address, look-alike web-site content
- Assessment will comprise of questions having phishing web-site, spear-phishing email, SMiShing, scenario-based question to make it close to real-world phishing attacks
- Tool also provides analytics in form of graphs to represent security awareness posture of organisation by different categories such as department, employee, target-user action

Client Module: This module will be used by target user to complete the assessment and view tutorial
- Every user within a campaign itself will have 10 unique questions to answer, with the mix of positive and negative scenarios
- Passing criteria is to answer every question correct because all it takes is just one click!


### [Pwnppeteer - Phishing Post {Exploi/Automa}tion at Scale](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
None


### [RAT Exploitation Tool for Social Networks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
As we all know, many risks are involved with social networks such as impersonation, social-engineering, and data breach.

To demonstrate these attacks, we developed an innovative tool that can hijack and remotely control social network accounts by combining the powers of social engineering with malicious third party apps.

We built a private app store of phishing apps, with genres, that a bad actor can choose from to gain RAT control over victim accounts. To enable this, our tool manages oauth tokens within a single web console, allowing the hacker to exercise the functions of the victim accounts. To this end, we discuss other features and extensions of our tool, such as social engineering chat bots, crawlier bots, password crackers, and visualization tools for social network analytics.


### [SPF: SpeedPhishing Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
SpeedPhishing Framework (SPF) is a small collection of tools which can assist penetration testers in quickly/automatically deploying phishing exercises in minimal time.

Among the various capabilities included with SPF is the ability to automate the phishing process of OSINT and target selection, deployment of one or more phishing websites, the crafting and sending of phishing emails to the targets, recording the results, and generating a basic report.

SPF also includes more advanced capabilities such as dynamically building new web phishing templates, automatically validating captured credentials against target mail servers and the pillaging of sensitive information, and SPF can assist in the phishing of multifactor authentication portals.


### [Sharkcop: A Phishing Detector Using Machine Learning](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
Sharkcop use criterias such as ssl certifucate, domain length, domain age,... with SVM classification algorithm to determine if a url is phishing or not. Sharkcop includes a restful web server and a chrome extension to highlight malicious links on Facebook and Messenger.


### [SniperPhish: The Web-Email Spear Phishing Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
Spear Phishing campaigns are commonly used to test employees' awareness in a company/organization. This exercise involves mostly the combination of phishing emails and websites. An effective campaign requires sophisticated methods starting from designing a phishing website to executing payload at the target in an undetectable manner. A platform is required to send emails to targeted users and tracking campaign progress. This basically involves the use of a mail server (to send email) and a web server (to host phishing website). To collect campaign data, these two domains need to be considered. Precisely, the campaign required to track email delivery status and the data submitted in the phishing website.

Usually, the data from these two domains can be collected easily, but it is more challenging and time-consuming when these data are to be consolidated and address questions such as which victim in the mail submitted data through the website. SniperPhish comes in handy here so that the data is tracked centrally, and displays the consolidated data in its dashboard.

SniperPhish is an advanced Web-Email spear-phishing toolkit developed in PHP to conduct professional phishing assessments. The abstract idea behind this toolkit is to simulate, combine, and centrally track all campaigns that involve email and phishing websites. SniperPhish supports tracking data from web site containing n number of pages. The data submitted in the phishing website containing multiple pages are tracked sequentially with email campaigns. The advanced customization in the report generation module helps to customize column fields and export in multiple outputs. In addition to the core campaign module, SniperPhish also provides additional functionalities such as hosting phishing websites, payload generation, encryption options, and options to convert payloads to FUD using different methods (eg: conversion to reflective DLL/PE).


### [Social Attacker: Automated Phishing on Social Media Platforms](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
Social Attacker is the first Open Source, Multi-Site, automated Social Media Phishing Framework. It allows you to automate the phishing of Social Media users on a mass scale by handling the connecting to, and messaging of targets.

You provide Social Attacker with a phishing message and a list of target profiles (collected either by hand or with Social Mapper). Then over a timeframe you set, it attempts to connect to the targets and, if they accept, sends them phishing message. It can even scrape a targets public profile history and use rudimentary message generation to craft a personal message specific to that person, as an alternative to sending the same phish to all targets.

Social Attacker provides Red Teamers, Penetration Testers & Social Engineers an efficient way to exploit and pivot through an alternative attack route.

Social Attacker supports the following Social Media platforms:

LinkedIn
Facebook
Twitter
VKontakte

Additional Features Include:

Report Generation
Tracking Connections & Clicks
Customized Phishing Message Generation


### [TapIt: SMS Phishing Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Social--Engineering--/--General](https://img.shields.io/badge/Category-Social--Engineering--/--General-gray)  
Email phishing is the weapon of choice for most attackers and red teamers alike for getting initial compromise on a network. Email phishing awareness is also heightened in today's cyber security atmosphere. What if I told you there's another social engineering method to achieve initial compromise that is largely unnoticed by defenders?

Mobile phones and SMS are technologies that are largely unmonitored by defenders. TapIt aims to exploit scenarios and situations where SMS Phishing (SMiShing) may be used by attackers to achieve their goals, such as initial compromise, credentials harvesting & 2FA phishing.

TapIt allows easy execution of large-scale SMS phishing campaigns, allowing SMS to be sent to large number of recipients, and to follow-up with tracking of these SMS. Its in-built functionality will also allow ease of setup for purpose of credentials harvesting, delivery of payloads and social engineering.


---

## Web/AppSec


### [A Look at ModSec 3.0 for NGINX: A Software Web Application Firewall](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Today more and more websites are becoming subject to the constant and malevolent barrage coming from malicious hackers. A websites name can be tarnished quickly by a simple breach of their application stack. Web application security is becoming more and more a crucial part of the IT infrastructure, but what exactly does a WAF do and why do you need it? In this talk we will answer those questions.

We will first take a look at how the popular and highly adopted open source proxy server known as NGINX can be combined with the long respected open source web application firewall known as ModSecurity to achieve an effective and highly secure layer for your web application stack. We will explain the detailed benefits that NGINX and ModSecurity can provide, including protection from layer 7 attacks such as XSS, SQLi and LFI. We will showcase how the combination of these technologies can automatically block traffic from known malicious IP addresses. We will cover the visibility and auditing ModSecurity can provide from its detailed log files.

Lastly, we will walk through the setup process and configurations so that after attending this session you can easily and quickly setup NGINX and ModSecurity as a effective and highly secure web application firewall.


### [Akto - Open Source API Security Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
We released Open source Akto in Feb '23 & we have 310 stars on Github. This tool is mainly focuses on solving the problems below:
- Tough api inventory for both testers, compliance and developers
- Testing with complex chained apis - Multi step authentication, refresh/access token etc.
- Automated testing of APIs - Both OWASP Top 10 and some business logic tests

Our tool Akto focuses on solving the above problems by providing:
1. Provide automated API inventory -
1.a) Automated - Akto can populate inventory automatically from traffic sources like Burp Proxy, Postman or even Chrome HAR files.
1.b) All formats - Akto also covers different formats of APIs such as JSON, GraphQL, gRPC, JSONP, forms.
2. Inspects traffic & provides alerts on suspicious apis -
2.a) Sensitive data - Akto comes with an in-built library for sensitive data patterns. Akto can tell which APIs are sharing sensitive data such as SSN, email, Phone number etc. Users can add their own patterns too.
2.b) Alerts - Users can set up daily alerts using Slack and Webhooks to get alerts about new sensitive data/APIs found
3. Automated API testing which covers OWASP Top 10 & some business logic testing
3.a) OWASP Coverage - Akto has 130+ tests to cover for OWASP Top 10
3.b) Business logic tests - Akto also supports business logic tests such as BOLA, Broken Function Level Authorization, Broken Authentication etc.
3.c) Add your own - Users can also add their own tests.

This tool will be very interesting for:
- Bugbounty Hunters - has a blackbox feature where complex apis can be uploaded from Burp history & can be useful for chained requests.
- Pentesters & testing teams in appsec - getting accurate api collection is complex & time consuming. Provides a one stop solution for getting the inventory. Tests like BOLA and BFLA will be especially interesting for them.
- Blue teamers/infra security - Getting an automated API inventory and getting alerts for any new sensitive APIs. They can also get a view of all sensitive PII data being shared across all their services and across all their APIs. They can check unauthenticated APIs, download the swagger file and use it in other security apps too.


### [AppSecLens: AI-Driven Adaptive Application Risk Ranking](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
AppSecLens is an innovative web application security tool, specifically designed to assist organizations in proactively managing their attack surface, identifying vulnerabilities, and prioritizing remediation efforts with a focus on Application Risk Ranking.

Inspired by VulnHero, AppSecLens identifies related web applications using domain knowledge, conducts context-based discoveries, and employs AI-powered algorithms to assign application risk rankings. The tool evaluates web applications based on criteria such as potential business risks, presence of PII/NPI/HPI data, authentication structure, underlying technology stack, patch cadence, and security posture. AppSecLens's AI-driven algorithm assigns automatic tags and labels accordingly, enabling efficient risk prioritization.

By integrating with third-party APIs and threat intelligence databases, AppSecLens remains up-to-date with the latest vulnerabilities and exploits. The tool also supports seamless collaboration with other security tools and systems, facilitating coordinated remediation efforts. Its customizable dashboards and reporting options empower users to monitor and manage risks effectively, ensuring a more robust and secure web application environment.


### [AppsecStudy: Open-Source eLearning Management System for Information Security](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Because preventing vulnerability is less costly than redeveloping the complete application, infosec education and training become more and more actual. As a result, developers can greatly reduce the risk and expense from cyber attacks in the future by creating secure code. In addition, training the team based on the security assessment results to correct actual errors provides ongoing protection for existing and future products.

Since studying is impossible without a practical part, providing hands-on lab training for developing teams is a necessary step.
AppsecStudy - an open-source platform for seminars, training, and organizing courses for practical information security for developers and IT specialists. This tool has all the built-in basic requirements needed for organizing normal and productive training.


### [Astra: Automated Security Testing For REST APIs](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
REST API penetration testing is complex due to continuous changes in existing APIs and the addition of new APIs. Astra (Sanskrit: अस्त्र) can be used by security engineers or developers as an integral part of their process, so they can detect and patch vulnerabilities in the initial phase of the development cycle. Astra can automatically detect and test login & logout (Authentication API), which makes it easy for anyone to integrate this into CICD pipeline. Astra can take API collection as an input so this can also be used for testing APIs in stand-alone mode.


### [BURPSMARTBUSTER: A SMART WAY TO FIND HIDDEN TREASURES](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
This tool is the anticipated replacement of a better dirb/gobuster/DirBuster. Bruteforcing non-indexed data is often used to discover hidden files and directories which can lead to information disclosures, or even to system compromise when a backup file is found. This bruteforcing technique is still useful today, but the tools are lacking the application context and do not use any smart behaviour to reduce the bruteforce scanning time. BurpSmartBuster, a Burp Suite Plugin, offers to use the application context and add the smart into the Buster!

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


### [BlueMap - An Interactive Tool for Azure Exploitation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
As demonstrated in BlackHat UK & Asia - BlueMap helps cloud red teamers and security researchers identify IAM misconfigurations, information gathering, and abuse of managed identities in interactive mode without ANY third-party dependencies. No more painful installations on the customer's environment, and No more need to custom the script to avoid SIEM detection!

The tool leaves minimum traffic in the network logs to help during red team engagements from on-prem to the cloud. Developed in Python and implemented all Azure integrations from scratch with zero dependencies on Powershell stuff. The idea behind the tool is to let security researchers and red team members have the ability to focus on more Opsec rather than DevOps stuff.


### [BlueMap](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
None


### [Build Your Own Reconnaissance System with Osmedeus Workflow Engine](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Osmedeus is a is a workflow framework designed to perform reconnaissance, with a focus on identifying the attack surface and conducting security testing on the specified target, including vulnerability scanning, port scanning, and content discovery


### [Burp Replicator: Automate Reproduction of Complex Vulnerabilities](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Developers often struggle to reproduce vulnerabilities discovered during pen tests. This is especially true for complex issues that need to bypass JavaScript validation, work with multi-step forms, handle dynamic CSRF tokens and more. This does not fit well with agile development where the ability to quickly reproduce problems enables efficient test driven development. Replicator solves this issue by allowing a pen tester to create a reproduction script that a developer can use on their system. Complex vulnerabilities can be confirmed with a single click, allowing the developer to stay in their productive coding flow. The tool is fully integrated with Burp Suite, making the script greatly easier to produce than a shell script, and keeping the tester in productive flow.


### [CSP AUDITOR](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
CSP Auditor is a Burp and ZAP extension that helps build or improve the Content-Security-Policy header configurations. CSP can provide a solid defense against XSS. However, it is easy to add a directive by mistake that will make the policy completely ineffective against specially-crafted XSS. This plugin provided a readable view of CSP headers in the response tab. It will highlight the weakest configurations. It also includes passive scan rules to be notified of weak configurations. The most recent feature is the automatic generation of CSP configuration based on the resources intercepted.


### [ChainAlert: Alert Developers and Open Source Maintainers of Potential Supply Chain Attacks and Suspicious Package Release](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
None


### [Cloud AuthZ Trainer (CAZT)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
CAZT is a simulator of cloud-provider responsible REST APIs. It includes a lab manual for getting hands-on practice with how to attack authorization vulnerabilities in a cloud API.

It is different from other vulnerable cloud practice environments because it focuses on the cloud-provider shared responsibility instead of the customer. This enables pen testers to gain experience with testing the cloud vendor itself as well as an understanding of what a vulnerable cloud service will look like.


### [EASILY EXPLOIT TIMING ATTACKS IN WEB APPLICATIONS WITH THE 'TIMING_ATTACK' GEM](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
The timing_attack gem is a simple application to exploit timing attacks in web applications. It focuses on ease-of-use over extreme resolution; its primary use is in exploiting known timing vulnerabilities in web applications.


### [Emulating Any HTTP Software as a Honeypot with HASH: A Deceptive Defense Against Cyberattacks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
HASH (HTTP Agnostic Software Honeypot), an open-source framework for creating and launching low interaction honeypots. With simple YAML configuration files HASH can simulate any HTTP based software with built in randomization capabilities to avoid being identified.


### [Eyeballer: A Picture is Worth a Thousand Vulns - Weaponized Machine Learning to Target Website Screenshots](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
AI-based hacking tools are here and taking aim at your network perimeter. With recent advances in machine learning, hackers can now solve tasks that previously required human experience and decision making. Our open source tool Eyeballer uses a convolutional neural network to sift through mountains of screenshots and tells the hacker what is likely to have vulnerabilities and what isn't, just by looking at it.

You know a busted website when you see one: broken HTML, blocky frames—something obviously written in raw PHP before MVC frameworks even existed, made custom by your target over a decade ago. Signature-based scanners won't help you find this diamond-in-the-rough vulnerability. And who has time to look through 100,000 EyeWitness screenshots to find your most likely entry point? This is where AI comes in to give those websites a quick eyeballing so you don't have to.

The future of hacking will augment human expertise with AI analysis. To help spur this on, we'll be releasing both the source code behind Eyeballer and our training dataset of tens of thousands of carefully curated website screenshots. We'll also be showing off live demos of the whole thing so you can witness for yourself the results of melding machine and man.


### [FTW: FRAMEWORK FOR TESTING WAFS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
FTW is designed to be a comprehensive test suite to help provide rigorous tests for WAF rules. It uses the OWASP Core Ruleset V3 as a baseline to test rules on for various WAFs. It is designed to:

Find regressions in WAF deployments by using continuous integration and issuing repeatable attacks against a WAF
Provide a testing framework for new rules into the Core Rule Set, if a rule is submitted it MUST have corresponding positive & negative tests
Evaluate WAFs against a common, agreeable baseline ruleset (OWASP)
Test and verify custom rules for WAFs that are not leveraging the core rule set


### [FUZZAPI - FUZZING YOUR RESTAPIS SINCE YESTERDAY](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
After seeing the benefits of Automating REST API pen testing using a basic Fuzzapi tool, the authors have decided to come up with a better version which can automatically look into vulnerabilities in APIs from the time they are written. REST APIs are often one of the main sources of vulnerabilities in most web/mobile applications. Developers quite commonly make mistakes in defining permissions on various cross-platform APIs. This gives a chance for the attackers to abuse these APIs for vulnerabilities. Fuzzapi is a tool written in Ruby on Rails which helps to quickly identify such commonly found vulnerabilities in APIs which helps developers to fix them earlier in SDLC life cycle. The first released version of the tool only has limited functionalities however, the authors are currently working on releasing the next version which will completely automate the process which saves a lot of time and resources.


### [FireTail - inline API security checking](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
FireTail sits on top of popular open source frameworks for building web services and APIs, like OpenAPI/Swagger, Express and Rails, and then provides in-line security processing of the API calls. FireTail checks for (in sequential order):
1. API call is hitting valid route using a valid method. This allows for a zero-trust, declarative API structure, with proper error handling at the HTTP layer.
2. Inspection of authentication token. Does the API expect a JWT, application-issued API key or other? FireTail will check whether a valid token of the correct type is present.
3. Payload inspection. FireTail will look for and fail invalid queries.


### [GCPGoat : A Damn Vulnerable GCP Infrastructure](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
GCPGoat is a vulnerable by design infrastructure on GCP featuring the latest released OWASP Top 10 web application security risks (2021) and other misconfiguration based on services such as IAM, Storage Bucket, Cloud Functions and Compute Engine. GCPGoat mimics real-world infrastructure but with added vulnerabilities. It features multiple escalation paths and is focused on a black-box approach.


### [Gerobug: Open-Source Private (Self-Managed) Bug Bounty Platform](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Are you a company, planning to have your own bug bounty program, with minimum budget? We got you!

We are aware that some organizations have had difficulty establishing their own bug bounty program.
If you know what you're doing, using a third-party managed platform usually comes with a hefty price tag and increased security concerns.
However, creating your own independently run platform will take time and effort.

GEROBUG FEATURES:
Homepage
This should be the only page accessible by public, which contains Rules and Guidelines for your bug bounty program.

Email Parser
Bug Hunter will submit their findings by email, which Gerobug will parse, filter, and show them on dashboard.

Auto Reply and Notification
Bug Hunter's inquiries will be automatically replied and notified if there any updates on their report.
Company will also be notified via Slack if there any new report.

Report Management
Manage reports easily using a kanban model.

Report Filtering and Flagging
Reports from Bug Hunter will be filtered and flagged if there are duplicate indication.

Email Blacklisting
Gerobug can temporarily block and release emails that conducted spam activity

Auto Generate Certificate
We can generate certificate of appreciations for bug hunters so you don't have to ;)

Hall of Fame / Wall of fame / Leaderboard
Yeah we have it too


### [Ghost in the Browser: Backdooring with Shadow Workers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Service Workers are all the rage for progressive web apps nowadays. This talk will take a look at Service Workers from a different perspective. We will be focusing on our tool called "Shadow Workers" that serves as an exploitation toolkit to weaponize Service Workers

We'll explore some of the tools features including the ability to implant a pseudo backdoor in the browser and ghost through a victim's browser session to sniff, manipulate, and even proxy data silently.

We'll demo the various persistence mechanisms our tool provides to keep service workers alive and demo how MITM can be done at the browser layer. We'll also release a compendium tool to provide various mitigation mechanisms against such attacks.


### [Ghosts in the Browser: Backdooring with Service Workers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
None


### [GoTestWAF - well-known open-source WAF tester now supports API security hacking](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
GoTestWAF is a well-known open-source WAF testing tool which supports a wide range of attacks, bypassing techniques, data encoding formats, and protocols, including legacy web, REST, WebSocket, gRPC, and more.

With this major update, the tool now supports Swagger/OpenAPI-based scanning and becomes the first open-source testing tool available for API security solutions.


### [HAWK Eye - PII & Secret Detection tool for your Servers, Database, Filesystems, Cloud Storage Services](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
HAWK Eye is a powerful Command-Line Interface (CLI) tool designed to enhance data source security by detecting and protecting Personally Identifiable Information (PII) across various platforms. Inspired by the precision and vision of majestic birds of prey, HAWK Eye swiftly scans multiple data sources, including S3, MySQL, Redis, Firebase, filesystem, and Google Cloud Storage (GCS), for potential data breaches and cyber threats.

With data breaches becoming more prevalent, organizations need robust security measures to safeguard sensitive information. HAWK Eye provides a comprehensive solution, capable of seamlessly integrating with different data sources to identify and protect PII. Its extensible architecture allows developers to contribute new commands, empowering the tool to address evolving security needs.

Future Roadmap:
HAWK Eye is continuously evolving, and we have an exciting roadmap ahead! Our plans include adding support for more than 20+ additional data sources, such as MongoDB, Jira, and ticketing services. These integrations will enable HAWK Eye to detect PII and secrets from a diverse range of applications, ensuring comprehensive data source security for users.


### [HUNT: THE BUG HUNTER'S BURP EXTENSION](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
What if you could super-charge your bug hunting? Not through automation (since it can miss so much) but through powerful alerts created from real threat intelligence? What if you had a Burp plugin that did this for you? What if that plugin not only told you where to look for vulns but also gave you curated resources for additional exploitation and methodology? Well, now you do! HUNT is a new Burp Suite extension that aims to arm bug hunters and web testers with parameter level suggestions on where to look for certain classes of vulnerabilities (SQLi, CMDi, LFI/RFI, and more!).


### [JSShell: An Interactive XSS Management & Browser Debugging Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
JSShell is an interactive multi-user web based javascript shell that enables the user to debug esoteric browsers and manage XSS (cross site scripting) campaigns. It was originally created during research to have the ability to debug remote esoteric browsers that did not have a simple debugging console. This tool can be also used to easily attach to a XSS (Cross Site Scripting) payload to achieve browser remote code execution (similar to the BeeF framework) and manage the vulnerability.

Version 2.0 is created entirely from scratch, introducing new exciting features, stability and maintainability.


### [LazyCSRF: A More Useful CSRF PoC Generator on BurpSuite](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Burp Suite is an intercepting HTTP Proxy, and it is the defacto tool for performing web application security testing. The feature of Burp Suite that I like the most is `Generate CSRF PoC`. However, the function to automatically determine the content of the request is broken, and it tries to generate PoCs using `form` even for PoCs that cannot be represented by `form`, such as JSON parameters and PUT requests. In addition, multibyte characters that can be displayed in Burp Suite itself are often garbled in the generated CSRF PoC. These were the motivations for creating LazyCSRF.


I have implemented a feature to solve them. It has the following features:
- Automatically switch to PoC using XMLHttpRequest
- In case the parameter is JSON
- In case the request is a PUT/PATCH/DELETE
- Support displaying multibyte characters (like Japanese)
- Generating CSRF PoC with Burp Suite Community Edition (of course, it also works in Professional Edition)


https://github.com/tkmru/lazyCSRF


### [Makes: A tool for avoiding supply chain attacks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
As the open-source ecosystem keeps growing, and applications increase their reliance on public libraries, we also see a spike in supply chain attacks. Recent scandals like SolarWinds or Log4j remind us how exposed software is when it comes to malicious, vulnerable or broken packages. Modern applications have thousands of dependencies, which means that managing dependency trees only becomes harder over time, while exposure keeps rising.

Think about how often you need things like

- keeping execution environments frozen for a strict dependency control (I'm looking at you, supply chain attacks);
- running applications locally so you can try whatever you are coding;
- executing CI/CD pipelines locally so you can make sure jobs (Linters, tests, deployments, etc.) are passing;
- running applications anywhere, no matter what OS you are using;
- knowing the exact dependency tree your application has for properly managing risk (Software Bill of Materials);
- making sure applications will work as expected in production environments.

At Fluid Attacks, we have experienced such concerns firsthand. That is why we created Makes, an open-source framework for building CI/CD pipelines and application environments in a way that is

- secure: Direct and indirect dependencies for both applications and CI/CD pipelines are cryptographically signed, granting an immutable software supply chain;
- easy: Can be installed with just one command and has dozens of generic CI/CD builtins;
- fast: Supports a distributed and completely granular cache;
- portable: Runs on Docker, VM's, and any Linux-based OS;
- extensible: Can be extended to work with any technology.

Makes is production ready and used currently in 11 different products that range from static and dynamic websites to vulnerability scanners. It was released on GitHub in July 2021 and has already been starred 170 times. It currently has 9 contributors from the community and gets a minor update each month.


### [Mal2Vec: Word2Vec Variant for Analytics of Web Attacks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Word2Vec is one of the most successful and popular technologies for Natural Language Processing. It facilitates the understanding of the semantics of words using their context. Many other domains adopted the Word2Vec approach and used embedding of domain objects in Euclidean spaces for distance calculation, clustering, visualization and more.

Mal2Vec is a Word2Vec-based framework for analytics of security incidents that helps the analyst understand the contextual relations between attack vectors, and thus to understand better attack flows. The tool looks at malicious web request as words and at sequences of malicious web requests as sentences, and applies a variant of Word2Vec to embed the attack vectors in Euclidean space and to analyze their contextual relations. Using this approach, the analyst can get better understanding of the attack flows, e.g., he can see which attack vectors tend to come together.

While we developed Mal2Vec to improve our understanding of web attack based on analysis of security events of Web Application Firewall (WAF), we also provide an easy customization flow that will make it useful for analytics of other cyber-attack data.


### [ModSecurity 3.0](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
ModSecurity is a toolkit for real-time web application monitoring, logging, and access control. I like to think about it as an enabler: there are no hard rules telling you what to do; instead, it is up to you to choose your own path through the available features.


### [ModSecurity 3.1: Stepping up the Game for Web Attacks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
With this upcoming release of ModSecurity we are delivering improved performance, stability and new exciting features!

We are bringing the possibility of virtual patch on demand through the ability of reloading the rules without restart among other improvements in that area. Additionally, we will be showing a testing feature that is exclusive to ModSecurity that allows rules writers and WAF administrators to effortlessly search and match for known malware payloads and signatures. This intends to step-up the game on the detection and blocking of countless types of malware and exploits.

In this presentation we will also be demonstrating the flexibility of ModSecurity by showing the feasibility of running a WAF inside an IoT device.

This release includes around 300 commits since the first 3.0 release with fixes, improvements and features added to the bleeding edge version of the open source libModSecurity. It contains a number of improvements in different areas: These include, clean ups, better practices for improved code readability, resilience, overall performance, support to a few missing features, LuaJIT and a number of fixes to actions and transformations.

Last but not least, there's an improved user experience while reading the logs with a new API component that allows the unique id informed on transactions, making possible to match an id that it is already in use by the consuming application (the connector).


### [N3XT G3N WAF 2.0](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Previously, we introduced N3XT G3N WAF (NGWAF) 1.0 at BHUSA 2022. The novel WAF 3.0 tool that seeks to relieve complex and difficult WAF detection mechanism with detection utilising a Sequential Neural Network (SNN) and traps attackers through a custom honeypotted environment. These assets are all dockerised for scalability.

However, further experiments have proven that a SNN may not be the most optimal when it comes down to contextualised defence as it processes information in a step by step and sequential manner. It gets relatively cumbersome and ineffective detecting chained or contexualised attacks. Both of which are extremely common in today's attacks.

Thus, we took another approach by swapping out our "brains". We revamped the SNN and went with a Recurrent Neural Network (RNN). The RNN is a much better choice for contextualised defense as the output of each layer is fed back as the input of the same layer. Thus, this allows the network to maintain a "memory" of the data it has processed. Our latest model is a RNN with a bi-directional LSTM module, it has an accuracy of 0.995 and a f1 score of 0.993.

We have also upgraded NGWAF's scalability in model deployment, model maintenance and the overall detection pipeline. This is all done with cloudifying the operations of the entire Machine Learning detection module. As compared to version 1.0 where users have to install and run the entire framework on their local system, NGWAF 2.0 has employed Infrastructure-as-Code (IaC) scripts, which auto-deploys the machine learning model's training & maintenance pipeline onto AWS resources (Sagemaker). The detection module has also been shifted from local deployment to AWS Sagemaker where we are able to standardise the hardware utilised for the ML model. This also allows further decoupling of the detection module from the rest of the system and allow for greater customisability.

BHUSA 2022 - Version 01: (https://www.blackhat.com/us-22/arsenal/schedule/index.html#nxt-gn-waf-ml-based-waf-with-retraining-and-detainment-through-honeypots-26609)


### [Nekuda: IDN-Squatting Detector](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Put yourself in the shoes of a fraudster, you are trying to create a phishing website. Why inserting detectable unicode characters into a mostly-ASCII domain when you can register an entire domain in unicode? This is available when one uses a lesser-known feature called Internationalized Domain Name Top Level Domains (IDN TLD). Consider registering domains like google.com's lookalike in Hebrew - גוגל.קום, アマゾン.コム in Japanese instead of amazon.com or 微软.公司 which is the Chinese equivalent of microsoft.com.

Nekuda (dot in Hebrew) assists blue teamers to detect such domains. Its input is a string (e.g. the blue teamer's employer Brand name) and it emits over 150 potential IDN TLD domains and its registration status. It covers a potential gap in proactive phishing detection and prevention strategies and can be easily integrated into existing open-source tools like dnstwist.


### [Node Security Shield - A Lightweight RASP for NodeJS Applications](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Node Security Shield (NSS) is an Open source Runtime Application Self-Protection (RASP) tool which aims at bridging the gap for comprehensive NodeJS security.

NSS is designed to be Developer and Security Engineer friendly and enables them to declare what resources an application can access.

Inspired by the Log4Shell vulnerability which can be exploited because an application can make arbitrary network calls, we felt there is a need for an application to have a mechanism so that it can declare what privileges it allows in order to make the exploitation of such vulnerabilities harder by implementing additional controls.

In order to achieve this, NSS (Node Security Shield) has a Resource Access Policy and the concept is similar to CSP (Content Security Policy). Resource Access Policy lets developer/security engineers declare what resources an application should access and Node Security Shield will enforce it.

If the Application is compromised and requests 'attacker.com' or executes a malicious command. Node Security Shield will block it automatically and thus protect the application from malicious attacks.

Node Security Shield was first announced in Black Hat Asia 2022 Arsenal.

Later at Black Hat USA 2022 arsenal (Virtual), the first major update was released which adds support for the 'module-level' Resource Access Policy. Allowing Developers or Security Engineers to declare what resources a module can access.

This release is a major update and adds support for Command Execution. Allowing Developers or Security Engineers to declare if the application can execute system commands. If allowed, what type of system commands are allowed.


### [Node Security Shield](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
None


### [NtHiM (Now, the Host is Mine!): Super Fast Sub-Domain Takeover Detection](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
NtHiM, which stands for "Now, the Host is Mine!" is a Rust-based systems project, which enables security enthusiasts to discover subdomain takeover vulnerabilities in hostnames (domains and subdomains) from different organizations.


In this session, I will be discussing about the following things, apart from an introduction of myself as the project maintainer and your presenter for this session.

Project Overview
Brief Introduction (what this project actually is)
Initiation Story (how I decided to start working on this project)
Brief Logic Explanation (understanding the project workflow with a simple pseudocode)
Project Features (getting to know about all of the things built into the project)
User-level Video Documentation (Demonstration; including guides for the end-users of this project)
Developer-level Video Documentation (Demonstration; including guides on how you can get started with extending or contributing to this project)


### [OFFENSIVE WEB TESTING FRAMEWORK (OWASP OWTF)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
OWASP OWTF is a project focused on penetration testing efficiency and alignment of security tests to security standards like the OWASP Testing Guide (v3 and v4), the OWASP Top 10, PTES and NIST so that pentesters will have more time to:

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


### [OWASP JoomScan Project](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
OWASP Joomla! Vulnerability Scanner (JoomScan) is an open source project, developed with the aim of automating the task of vulnerability detection and reliability assurance in Joomla CMS deployments. Implemented in Perl, this tool enables seamless and effortless scanning of Joomla installations, while leaving a minimal footprint with its lightweight and modular architecture. It not only detects known offensive vulnerabilities, but also is able to detect many misconfigurations and admin-level shortcomings that can be exploited by adversaries to compromise the system. Furthermore, OWASP JoomScan provides a user-friendly interface and compiles the final reports in both text and HTML formats for ease of use and minimization of reporting overheads.
OWASP JoomScan is included in Kali Linux distributions.

Source Code: https://github.com/rezasp/joomscan


### [OWASP Offensive Web Testing Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
OWASP OWTF is a project focused on penetration testing efficiency and alignment of security tests to security standards like the OWASP Testing Guide (v3 and v4), the OWASP Top 10, PTES and NIST so that pentesters will have more time to

See the big picture and think out of the box
More efficiently find, verify and combine vulnerabilities
Have time to investigate complex vulnerabilities like business logic/architectural flaws
Perform more tactical/targeted fuzzing on seemingly risky areas
Demonstrate true impact despite the short timeframes we are typically given to test

OWTF is highly configurable and anybody can trivially create simple plugins or add new tests in the configuration files without having any development experience.


### [Open-Source API Firewall: New Features & Functionalities](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
The open-source API Firewall by Wallarm is a great option for API development. It offers a rich feature set, and its underlying technology is mature. The firewall's new feature of blocklisting for compromised tokens and cookies is a great way to gain visibility into threats and prevent issues. The feature is easy to set up and offers a high degree of visibility into the security posture of your APIs and services.


### [Purpleteaming with OWASP PurpleTeam (tool)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
OWASP PurpleTeam is a security regression testing SaaS and CLI that targets web applications and APIs. It can be run manually or sit within your build pipeline to continuously test your creations in close to real-time. Not only does PurpleTeam help you find and fix your security defects, it also helps train Developers and DevOps Engineers to recognise security defects and how to not introduce the same defects in the future.


### [PyGoat](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
PyGoat -
Intentionally vuln web Application Security in django. our roadmap build intentionally vuln web Application in django. The Vulnerability can based on OWASP top ten
• A1:2017-Injection
• A2:2017-Broken Authentication
• A3:2017-Sensitive Data Exposure
• A4:2017-XML External Entities (XXE)
• A5:2017-Broken Access Control
• A6:2017-Security Misconfiguration
• A7:2017-Cross-Site Scripting (XSS)
• A8:2017-Insecure Deserialization
• A9:2017-Using Components with Known Vulnerabilities
• A10:2017-Insufficient Logging & Monitoring


### [RWDD: Remote Web Deface Detection Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
RWDD (Remote Web Deface Detection) tool is an application designed to help secure a web with IoT (Internet Of Things) and notify users (via various communication mechanisms), whenever source code of website changed (by programmer or attacker).


### [ReDTunnel: Explore Internal Networks via DNS Rebinding Tunnel](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Did you wonder how you could browse target's internal network without deploying anything on the victim machine? Sounds like magic, right? Imagine that you could have a one-click setup that will provide you a magic tunnel from the outside world. That's when we came up with the "ReD Tunnel" idea. The design goal was to use tools that exist on the victim's device, like the browser, rather than rely on 0days to stay below the radar of the most advanced AV. To create this new capability, we decided to combine two concepts: JavaScript reconnaissance techniques and the DNS rebinding attack. Open your browser, wait until the victim visits your website and start browsing the internal websites in their network. Now, when red-teaming you could really "be a guest, but feel at home".


### [Revealing 2MS: New Secrets Detection Open Source, the Connection to Supply Chain Attacks, and The Developer's Responsibility](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Too many secrets (2ms) is a command line tool written in Go language and built over gitleaks. 2ms is capable of finding secrets such as login credentials, API keys, SSH keys and more hidden in code, content systems, chat applications and more.

https://github.com/checkmarx/2ms


### [Security Attacks as Software Tests: Building dev-oriented AppSec challenges with Play open source SDK](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
This talk focuses on the unique process of transforming security attacks into software tests for building secure programming challenges using an open-source SDK, 'Play'. A practical workshop where we explore the mechanics of choosing real-world-inspired security vulnerabilities, and transforming them into cloud-native apps with integrated security tests which can then be played as challenges. These challenge provides a new dimension to the traditional Capture The Flag experiences, emphasizing not just the identification but the remediation of vulnerabilities


### [SnitchDNS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
"It's always DNS". SnitchDNS is database driven (basic) DNS server built using Twisted, with a fancy web interface to go with it. Ideal for Red Team infrastructure, bug bounties, ad-blocking, DNS tunnels, and more.

As it's database driven, any changes are reflected immediately, match wildcard subdomains, source IP restrictions, conditional responses (great for SSRF), Slack/Teams/Email/Push notifications, logging, Swagger 2.0 API, full CLI interface, and more!

Ideal use cases are as a DNS Tunnel, DNS forwarding server, red teams, canary tokens, LetsEncrypt DNS challenge, and even ad-blocking.


### [SucoshScanny](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
SucoshScan is a automated open source SAST(Static Application Security Testing) framework. It's can detect a lot of vulnerability(RCE,SSTI,Insecure Deserilisation,SSRF,SQLI,CSRF etc.) in given source code.For now, only the detection modules of python(flask,django) and nodejs(express js.) languages are finished. In the future, specific detection functions will be written for php (Laravel, Codeigniter), .NET, Go languages.


### [Swimming with the (Data)Flow – Analyzing & Visualizing Web Application Data Flows for Enhanced Penetration Testing](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Imagine pentesting a large web application with hundreds of pages and forms, as well as user roles and tenants. You discover that your chosen username is reflected in many locations inside the application, but you don't have a detailed overview. You want to test whether the chosen username is handled properly or allows for injection attacks, such as Cross-Site Scripting or Server-Site Template Injection. Now you face the challenge of finding all locations where your payloads appear when injecting into the username. In large applications, you'll likely miss some, potentially leaving vulnerabilities undetected.

This is where FlowMate comes into play, our novel tool to detect data flows in applications for enhanced vulnerability assessments. FlowMate consists of two components: A BurpSuite plugin and a data flow graph based on Neo4j. It records inputs to the application as you go through the pages. In contrast to existing tools that require server-side access, FlowMate works from a black-box perspective by observing HTTP request and response pairs. Thereby FlowMate records all input parameters and locations as well as user-supplied values. In parallel, all HTTP responses from the server are matched against the central store of already identified parameter values to find occurrences of known input parameters. This results in a data graph, mapping inputs to outputs simply while using the application.

Understanding the data flow results in a significant improvement of test coverage in web app pentests, as all input and output occurrences of parameters can be systematically tested for vulnerabilities. More precisely, analysts can use FlowMate in the following ways: First, for a given input parameter, FlowMate shows all output locations, thus enabling verification of output filtering and encoding, even across role, tenant, and session boundaries. Second, for a given form, FlowMate visualizes all parameters and their respective output locations across the application.


### [THREADFIX WEB APPLICATION ATTACK SURFACE CALCULATION](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
The ThreadFix web application attack surface calculation utilities allow users to:

Calculate a web application's attack source based on application source code (available URLs and parameters)
Visually inspect web application attack surface to target manual penetration testing activities
Pre-seed dynamic application security testing tools like OWASP ZAP and Burpsuite
Calculate changes to application attack surface over time and across git commits
Run targeted DAST scans based on new attack surface and attack surface that has changed since previous tests were run


### [Threagile: Agile Threat Modeling Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
If we can build software in a reliable, reproducible and quick way at any time using Pipeline-as-Code and have also automated security scans as part of it, how can we quickly capture the risk landscape of agile projects to ensure we didn't miss an important thing? Traditionally, this happens in workshops with lots of discussion and model work on the whiteboard. It's just a pity that it often stops then: Instead of a living model, a slowly but surely eroding artifact is created, while the agile project evolves at a faster pace.

In order to counteract this process of decay, something has to be done continuously, something like "Threat-Model-as-Code" in the DevSecOps sense. The open-source tool Threagile implements the ideas behind this approach: Agile developer-friendly threat modeling right from within the IDE. Models editable in developer IDEs and diffable in Git, which automatically derive risks including graphical diagram and report generation with recommended mitigation actions.

The open-source Threagile toolkit runs either as a command line tool or a full-fledged server with a REST-API: Given information about your data assets, technical assets, communication links, and trust boundaries as input in a simple to maintain YAML file, it executes a set of over 40 built-in risk rules (and optionally your custom risk rules) against the processed model. The resulting artifacts are diagrams, JSON, Excel, and PDF reports about the identified risks, their rating, and the mitigation steps as well as risk tracking state.

Agile development teams can easily integrate threat modeling into their process by maintaining a simple YAML input file about their architecture and the open-source Threagile toolkits handles the risk evaluation.


### [Threagile: The Open-Source Agile Threat Modeling Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
The open-source tool Threagile enables agile teams to create a threat model directly from within the IDE using a declarative approach: Given information about the data assets, technical assets, communication links, and trust boundaries as input in a simple to maintain YAML file, it executes a set of over 40 built-in risk rules, which can be extended with custom risk rules, against the processed model. The resulting artifacts are graphical diagrams, Excel, and PDF reports about the identified risks, their rating, and the mitigation steps as well as risk tracking state. DevSecOps pipelines can be enriched with Threagile as well to process the JSON output.


### [ThreatPlaybook](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Threat Modeling is currently performed as a 'static' exercise, where the security team creates threat models as documents. These documents tend to be largely unused by anyone after the threat model and ends up being a static document. ThreatPlaybook is a "Threat Modeling as Code" framework, where you can capture Threat Models in a "playbook style" manner. Once you do, you can automatically generate diagrams, use the Threat Models to run application security automation like Vulnerability Scanning, etc.

The key benefits of ThreatPlaybook is that you can:
* Codify Threat Models for Iterative Threat Modeling
* Use Threat Models and Security Test Cases to launch targeted application security automation that can be used in a CI/CD environment or by pen testers who want to automate several tasks in their "Pentest Pipeline"
* Auto-generate Process Flow Diagrams from Codified Threat Models
* Capture Security Test Cases linked to Threat Modeling
* Generate reports correlating Threat Models to Vulnerabilities, Security Test Cases and so on.


### [VulnLab Web Application Vulnerabilities Lab](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
VulnLab is a lab environment to learn various Web vulnerabilities and test different exploitation techniques developed with PHP and runs on Docker container. The main reason we created Vulnlab is that there are already well-known applications with similar content but these applications are getting out of date day by day. In order to solve this problem,
VulnLab will be updated by our community when a new vulnerability has been found such as spring4shell or log4j. Currently, Vulnlab only includes the OWASP TOP 10 vulnerabilities.


### [WARCannon: Grep the Entire Internet for WebApp Vulnerabilities](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
Have you ever found a novel vulnerability in a website, framework, javascript library, or third-party integration, and wondered how many other people in the world are vulnerable, too? Have you ever wished that you could non-invasively grep the internet for a vulnerability indicator?

WARCannon was built for exactly this purpose, and is fed by Common Crawl via the AWS Open Data program to allow for petabyte-scale analysis of previously-spidered websites. Security researchers and bug bounty hunters can leverage WARCannon to scale their research horizontally across the entire internet in a fast, cost-effective, and entirely non-invasive/invisible way.


### [WATOBO - THE WEB APPLICATION TOOLBOX](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
WATOBO is a security tool for testing web applications. It is intended to enable security professionals to perform efficient (semi-automated) web application security audits.

Most important features are:

Powerful session management capabilities! You can define login scripts as well as logout signatures. So you don't have to login manually each time you get logged out.
Can act as a transparent proxy (requires nfqueue)
Vulnerability checks (SQLinjectin, XSS, LFI) out of the box
Handles Anti-CSRF-/One-Time-Tokens
Supports inline de-/encoding, so you don't have to copy strings to a transcoder and back again. Just do it inside the request/response window with a simple mouse click.
Smart filter functions, so you can find and navigate to the most interesting parts of the application easily.
Is written in (FX) Ruby and enables you to easily define your own checks
Runs on Windows, Linux, MacOS every OS supporting (FX) Ruby


### [WSSIP: A WEBSOCKET MANIPULATION PROXY](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
WSSiP is a tool for viewing, interacting with, and manipulating WebSocket messages between a browser and web server, with an outward bridge for debugging and fuzzing all WebSocket communications.


### [What's new in reNgine?](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
reNgine, an automated reconnaissance framework, helps quickly discover the attack surface and identifies vulnerabilities using extremely customizable and powerful scan engines. The most recent update introduces some of the most innovative features such as powerful sub scans feature, highly configurable reconnaissance & vulnerability pdf report, Tools Arsenal which allows updating preinstalled tools, their configurations, WHOIS identification, identifies related domains and related TLDs, and tons of actionable insights such as most common vulnerability, most common CVE IDs, etc. In a nutshell, the newer upgrade of reNgine makes it more than just a recon tool! The latest update aims to fix the gap in the traditional recon tools and probably a much better alternative for some of the commercial recon and vulnerability assessment tools.

This talk will be a walkthrough on some of the newest features to be introduced in reNgine and how corporates and individuals can make the best use of it.


### [XSSER: From XSS to RCE 3.0](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
This presentation demonstrates how an attacker can utilize XSS to execute arbitrary code on the web server when an administrative user inadvertently triggers a hidden XSS payload. Custom tools and payloads integrated with Metasploit's Meterpreter in a highly automated approach will be demonstrated live, including post-exploitation scenarios and interesting data that can be obtained from compromised web applications. This version includes more payloads for common web apps and various other improvements too!


### [crawlergo: A Powerful Browser Crawler for Web Vulnerability Scanners](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
crawlergo is a browser crawler that uses chrome headless mode for URL collection. It dynamically finds all URL requests contained in a web page through powerful automated intelligent analysis and de-duplication, providing comprehensive and high quality input for subsequent web vulnerability scanning.


### [c{api}tal - Learn OWASP API Security Top 10 by playing with vulnerable by design application](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
APIs are a critical part of modern mobile, SaaS, and web applications and can be found in customer-facing, partner-facing, and internal applications.

By nature, APIs expose application logic and sensitive data, potentially leading to data breaches, account takeovers, and much more.

Because of this, APIs have increasingly become a target for attackers. Without secure APIs, organizations would face many security risks and rapid innovation would be impossible.

It is extremely important to be aware of the OWASP API top 10 risks and enforce proper API security mitigations for your APIs. Therefore, we developed c{api}tal - an Open Source API training and learning platform by Checkmarx.

c{api}tal is a built-to-be-vulnerable API application based on the OWASP top 10 API vulnerabilities. Use c{api}tal to learn, train and exploit API Security vulnerabilities within your own API Security CTF.

In DefCon30, 2022, we first introduced c{api}tal to the world by conducting an API security CTF event to allow users to learn about the API security top 10 risks and exploit them in an isolated, vulnerable platform. Now we're open sourcing it.

In this session, you will learn about:
- The OWASP API top 10 risks
- c{api}tal overview
- Demo of exploiting one of the OWASP API top 10 risks
- How to mitigate API risks to keep your APIs safe


### [huskyCI: Performing Security Tests Inside Your CI](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
huskyCI is an open-source tool that performs security tests inside CI pipelines of multiple projects and centralizes all results into a database for further analysis and metrics.


### [reNgine: an automated reconnaissance Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
reNgine is an open-source reconnaissance engine that does end to end reconnaissance with the help of highly configurable scan engines to gather more information about the target for web application penetration testing. reNgine makes use of various open-source tools and makes a configurable pipeline of reconnaissance. With the recent release, reNgine also makes it possible to periodically perform the reconnaissance, say perform reconnaissance every 24 hours or so. With the highly configurable YAML based engines, reNgine makes it possible for users to choose the tools they desire while following the same reconnaissance pipeline, example - with reNgine you aren't limited to just using sublist3r for subdomains discovery, rather reNgine allows you to combine multiple tools like sublister, subfinder, assetfinder and easily integrate them into your reconnaissance pipeline. The reconnaissance results are then displayed into a beautiful and structured UI, which is one of the most loved features of reNgine.

Some Key Features are
>Subdomain Discovery, Ports Discovery, Endpoints Discovery, Directory Bruteforce, Visual Reconnaissance (Screenshot the targets)
>IP Discovery, CNAME discovery, Subdomain Takeover Scan
>Highly configurable scan engines
>Run multiple scans in parallel
>Run Clocked Scans (Run reconnaissance exactly at X Hours and Y minutes)
>Run Periodic Scans (Runs reconnaissance every X minutes/hours/days/week)
>Vulnerability Scan (Coming soon)


### [reNgine: An Open-Source Automated Reconnaissance/Attack Surface Management tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
None


### [route-detect: Find Authentication and Authorization Security Bugs in Web Application Routes](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
This demo introduces route-detect. route-detect is a command-line tool that seeks to aid security researchers and engineers in finding authentication (authn) and authorization (authz) security bugs in web application routes. These bugs are some of the most common security issues found today. The following industry standard resources highlight the severity of the issue:

- 2021 OWASP Top 10 #1 - Broken Access Control
- 2021 OWASP Top 10 #7 - Identification and Authentication Failures
- 2019 OWASP API Top 10 #2 - Broken User Authentication
- 2019 OWASP API Top 10 #5 - Broken Function Level Authorization

Of course, not all authn or authz bugs occur in web application routes, but route-detect seeks to confront this pervasive class of bugs.


### [vAPI: Vulnerable Adversely Programmed Interface (OWASP API Top 10)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
vAPI is a Vulnerable Interface in a Lab like environment that mimics the scenarios from OWASP API Top 10 and helps the user understand and exploit the vulnerabilities according to OWASP API Top 10 2019. The lab is divided into 10 exercises that sequentially demonstrate the vulnerabilities and give a flag if exploited successfully.


### [vAPI: Vulnerable Adversely Programmed Interface](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec](https://img.shields.io/badge/Category-Web/AppSec-gray)  
vAPI is a Vulnerable Interface in a Lab like environment that mimics the scenarios from OWASP API Top 10 and helps the user understand and exploit the vulnerabilities according to OWASP API Top 10 2019. Apart from that, the lab consists of some more exercises/challenges related to advanced topics related to Authorization and Access Control.


---

## Red Teaming


### [A NEW TAKE AT PAYLOAD GENERATION: EMPTY-NEST](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
As the evolution of endpoint, egress, and network security controls continues, adversaries and pentesters are finding it increasingly more difficult to execute malicious payloads within properly-hardened enterprise networks. Although tools currently exist to aid in circumventing these controls, the current state fails to properly account for some of newest techniques used by these controls. Enter Empty-Nest, a command-and-control (C2) toolset created with circumvention in mind. Empty-Nest was designed to provide a flexible payload-generation mechanism and pluggable interface to enable adversaries to easily customize payloads for targeted security control bypass. Our presentation shows the Empty-Nest toolset, demonstrating how to leverage the pluggable interface to create keyed payloads capable of bypassing new-age, cloud-based binary analysis, unloading endpoint software DLLs from running processes, customizing C2 transports, and more.


### [AADInternals: PowerShell Module for Administering Azure AD and Office 365](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AADInternals is a PowerShell module for administering Azure AD and Office 365. It is a result of hours of reverse-engineering and debugging of Microsoft tools related to Azure AD, such as PowerShell modules, directory synchronisation, and admin portals.

AADInternals contains tools for retrieving detailed information about Azure AD/Office 365 tenant not available otherwise, tools for manipulating Azure AD objects (e.g., users and passwords), and tools for creating backdoors to Azure AD/Office 365. The backdoor tools are based on the discovery and research of vulnerabilities in Azure AD identity federation, pass-through authentication, and Desktop SSO (aka Seamless SSO).


### [AADInternals: The Swiss Army Knife for Azure AD & M365](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AADInternals is a popular attacking and administration toolkit for Azure Active Directory and Microsoft 365, used by red and blue teamers worldwide. The toolkit is written in PowerShell, making it easy to install and use by anyone familiar with the Microsoft ecosystem. It has been downloaded from PowerShell gallery over 20,000 times and it is listed in MITRE ATT&CK tools.

With AADInternals, one can create backdoors, perform elevation of privilege and denial-of-service attacks, extract information, and even bypass multi-factor authentication (MFA).

Join this session to see in action the research results conducted during the past three years, including a new technique to extract AD FS signing certificates remotely, exporting certificates of AAD joined devices, gathering OSINT, and more!


### [ACSploit: Exploit Algorithmic Complexity Vulnerabilities](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [ACsploit: Exploiting Algorithmic Complexity Vulnerabilities](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Algorithmic Complexity (AC) vulnerabilities arise when a program uses an algorithm with a particularly inefficient worst-case computational complexity, and allows a user to provide input that will trigger it. Determining whether a program is vulnerable requires more than an understanding of what algorithms the program implements. It also requires understanding
how user input is filtered and formatted before it's given to the potentially exploitable algorithm. One way to do this is with time consuming manual analysis, such as reverse engineering, static code review, or debugging. Alternatively, feeding the algorithm input formatted to trigger its worst case, and then measuring the effects in time (i.e. CPU utilization) and space (e.g. RAM or disk usage) is quicker and requires less skill.

ACsploit is a command-line utility that generates worst-case inputs to commonly used algorithms, such as sorting, hashing, string manipulation, etc. It is modular and highly configurable, supporting a wide variety of user-specified constraints on the generated output, allowing it to appropriately fit the requirements of the application under test. ACsploit also supports an equally wide array of output formats to assist the user in delivering the resulting exploit from ACsploit to the target system. ACsploit supports both script-driven and interactive use through a familiar Metasploit-like interface. Originally developed under the DARPA STAC program to help rapidly triage potential AC vulnerabilities, we have released ACsploit as an open source tool to the broader vulnerability researcher community.

ACsploit comes with algorithmic complexity exploits for 30+ algorithms and is easily extensible. It's designed to allow members of the community to contribute new exploit modules, input constraints, and output formatters to expand upon all aspects of its functionality. Future plans for the development of ACsploit include debugger integration and a testing framework for measuring resource usage by the targeted application.


### [ADRecon: Active Directory Recon](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
ADRecon is a tool which extracts various artifacts (as highlighted below) out of an AD environment in a specially formatted Microsoft Excel report that includes summary views with metrics to facilitate analysis. The report can provide a holistic picture of the current state of the target AD environment. The tool is useful to various classes of security professionals like system administrators, security professionals, DFIR, etc. It can also be an invaluable post-exploitation tool for a penetration tester. It can be run from any workstation that is connected to the environment, even hosts that are not domain members. Furthermore, the tool can be executed in the context of a non-privileged (i.e. standard domain user) accounts. Fine Grained Password Policy, LAPS and BitLocker may require Privileged user accounts. The tool will use Microsoft Remote Server Administration Tools (RSAT) if available, otherwise it will communicate with the Domain Controller using LDAP.

The following information is gathered by the tool: Forest; Domain; Trusts; Sites; Subnets; Default Password Policy; Fine Grained Password Policy (if implemented); Domain Controllers, SMB versions, whether SMB Signing is supported and FSMO roles; Users and their attributes; Service Principal Names (SPNs); Groups and memberships; Organizational Units (OUs); ACLs for the Domain, OUs, Root Containers and GroupPolicy objects; Group Policy Object details; DNS Zones and Records; Printers; Computers and their attributes; LAPS passwords (if implemented); BitLocker Recovery Keys (if implemented); and GPOReport (requires RSAT).

Available at https://github.com/sense-of-security/ADRecon


### [ATTPwn](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
ATTPwn is a computer security tool designed to emulate adversaries. The tool aims to bring emulation of a real threat into closer contact with implementations based on the techniques and tactics from the MITRE ATT&CK framework. The goal is to simulate how a threat works in an intrusion scenario, where the threat has been successfully deployed. It is focused on Microsoft Windows systems through the use of the Powershell command line. This enables the different techniques based on MITRE ATT&CK to be applied. ATTPwn is designed to allow the emulation of adversaries as for a Red Team exercise and to verify the effectiveness and efficiency of the organization's controls in the face of a real threat.


### [AVET - ANTIVIRUS EVASION TOOL](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Avet is an antivirus evasion tool: (link: https://github.com/govolution/avet).

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


### [AVET: AntiVirus Evasion Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AVET is an antivirus evasion tool that is based on different antivirus evasion techniques as described in my research, found here:

https://govolutionde.files.wordpress.com/2014/05/avevasion_pentestmag.pdf
https://deepsec.net/docs/Slides/2014/Why_Antivirus_Fails_-_Daniel_Sauder.pdf

What & Why:

When running an exe file made with msfpayload & co, the exe file will often be recognized by the antivirus software
AVET is an antivirus evasion tool targeting windows machines with executable files
Different kinds of payloads can be used now: shellcode, exe and dlls
More techniques can be used now, such as shellcode injection, process hollowing and more
Most payloads can be delivered from a file, the network or command line
The payload can be encrypted with a key, the key can be delivered like payloads
Tested for Kali 2018.x (64bit) and tdm-gcc (should work on other Kali/Linux/32bit versions also)

AVET Version 2 was released in the beginning of 2019:

Internal mechanisms for building the executable have been rewritten, new features can be added much easier now
https://github.com/govolution/bfg has been integrated

With the new architecture and features of AVET 2 you can, for example, now build an executable that is loading an encrypted .exe file via network or file, receiving the key also via network or file, decrypt in memory and then inject via process hollowing. The same applies also for other payloads like shellcode or dlls and other techniques.

Presentation: https://govolution.files.wordpress.com/2019/08/bhusa19_arsenal_avet.pdf


### [AWSGoat : A Damn Vulnerable AWS Infrastructure](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Compromising an organization's cloud infrastructure is like sitting on a gold mine for attackers. And sometimes, a simple misconfiguration or a vulnerability in web applications, is all an attacker needs to compromise the entire infrastructure. Since the cloud is relatively new, many developers are not fully aware of the threatscape and they end up deploying a vulnerable cloud infrastructure. When it comes to web application pentesting on traditional infrastructure, deliberately vulnerable applications such as DVWA and bWAPP have helped the infosec community in understanding the popular web attack vectors. However, at this point in time, we do not have a similar framework for the cloud environment.

In this talk, we will be introducing AWSGoat, a vulnerable by design infrastructure on AWS featuring the latest released OWASP Top 10 web application security risks (2021) and other misconfiguration based on services such as IAM, S3, API Gateway, Lambda, EC2, and ECS. AWSGoat mimics real-world infrastructure but with added vulnerabilities. The idea behind AWSGoat is to provide security enthusiasts and pen-testers with an easy to deploy/destroy vulnerable infrastructure where they can learn how to enumerate cloud applications, identify vulnerabilities, and chain various attacks to compromise the AWS account. The deployment scripts will be open-source and made available after the talk.


### [Abusing Microsoft SQL Server with SQLRecon](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
In November 2022, Kaspersky Lab publicly released research which outlined that reoccurring attacks against Microsoft SQL Server rose by 56% (https://usa.kaspersky.com/about/press-releases/2022_kaspersky-finds-reoccurring-attacks-using-microsoft-sql-server-rise-by-56-in-2022).

I'd like to share a tool I wrote called SQLRecon, which will demonstrate how adversaries are leveraging Microsoft SQL services to facilitate with furthering their presence within enterprise networks through privilege escalation and lateral movement. I will also share defensive considerations which organizations can practically implement to mitigate attacks. I feel that this will add a fresh perspective on the various ancillary services within enterprise Windows networks which are under less scrutiny, however still ripe for abuse.

For red team operators, SQLRecon helps address the post-exploitation tooling gap by modernizing the approach operators can take when attacking SQL Servers. The tool is written in C#, rather than long-standing existing tools that use PowerShell or Python. SQLRecon has been designed with operational security and detection avoidance in mind – with a special focus on stealth, reconnaissance, lateral movement, and privilege escalation. The tool was designed to be modular, allowing for ease of extensibility from the hacker community. SQLRecon is compatible stand-alone or within a diverse set of command and control (C2) frameworks (Cobalt Strike, Nighthawk, Mythic, PoshC2, Sliver, Havoc, etc). When using the latter, SQLRecon can be executed either in-process, or through traditional fork and run.

Furthermore, I will be releasing a new version, one that is currently only used internally on advanced red team engagements by IBM X-Force Red's Adversary Services team.


### [Afterimage: Evading Traditional IOC Blocking](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Malicious IP addresses are critical indicators of cyber threats, and blocking these addresses is a standard practice during network forensics and incident response. Current solutions for maintaining anonymity, such as Tor nodes and botnets, have proven to be either compromised or illegal, thus posing challenges for legitimate red team exercises. In response to this growing demand for an effective solution, we have developed Afterimage, a novel application that enables attackers to enumerate and attack from multiple IP addresses without requiring the infrastructure of a botnet and with minimal time and effort.

Afterimage operates as an intermediary, accepting malicious traffic from an attacker through an open port, forwarding it to a proxy, and ultimately to the victim. If the proxy's IP is blocked, the application automatically cycles to another proxy to continue sending traffic. This process is more efficient and secure than existing methods such as VPNs, which are often monitored and costly, or compromised solutions like Tor nodes and botnets.

Our proposed solution, written in Python, is designed for deployment on remote servers, enabling multiple attackers to connect simultaneously. This unique approach to IP address cycling addresses key challenges faced during red team exercises, providing a more secure and effective solution for cyber security testing. By leveraging Afterimage, blue teams and SOCs can enhance their incident response capabilities and improve their overall cyber defense strategies.


### [All-Purpose Remote Access Trojan](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Apfell: Multi-Platform Command and Control](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Apfell is a collaborative, command and control platform designed to facilitate a plug-n-play architecture. It uses a web-based front-end so that it can be accessed from any OS and a Python/Docker based back-end. Apfell focuses on quality of life improvements for operators, especially while operating across macOS and *nix operating systems, such as searchable tasks, per-task comments, artifact tracking, MITRE ATT&CK mappings/exports, multiple concurrent c2 profiles, command versioning, and much more. It features a JavaScript for Automation (JXA) agent that runs in memory on macOS devices, but offers agents across a variety of platforms and services.


### [Armory](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Armory is a tool designed to run various existing tools, collating all of the output into a local database, and using that information for further attacks. It is extremely modular, and it is pretty easy to create custom modules and reports. Armory's purpose is to streamline client discovery and external penetration tests.


### [AtlasReaper: Sowing Chaos and Reaping Rewards in Confluence and Jira](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AtlasReaper is a .NET command-line tool developed for offensive security purposes, primarily focused on reconnaissance and keyword searching on Confluence and Jira instances. AtlasReaper also provides various features that are helpful for tasks such as credential farming and social engineering.

AtlasReaper was designed to be run from Command and Control (C2) to reduce the network overhead incurred from establishing a SOCKS proxy. The tool leverages Atlassian REST APIs to query metadata and content from the target Confluence and Jira. Read operations include search, listspaces, listpages, listissues, listattachments, and listusers. Any attachments that look interesting can be downloaded. It is also possible to dump all of the data for offline processing.

AtlasReaper extends its functionality with write operations, enabling users to attach files, create deceptive links, and comment on issues within Confluence or Jira. It is also contains functionality to embed images. Embedding 1x1 pixel images hosted on external servers enables stealthy NetNTLMv2 hash harvesting in Active Directory environments. The tool also facilitates targeted user engagement by @ mentioning victims on pages.


### [AttackForge ReportGen v2: Powerful Pentest Reporting Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AttackForge ReportGen is a freely available and downloadable pentest reporting tool with powerful features such as:
- Rich template library in DOCX format to cover different types of pentest reports
- Support for over 200 tags - covering projects, vulnerabilities, assets, attack chains, test cases, retesting, and more
- Support for DOCX reports
- Support for tables, images, styled text, custom fields
- Easy to apply styles & changes directly in Word – no need or hassle to write code
- Logic engine for complex reporting requirements and templates


### [AttackForge.com: A Pentest Management & Collaboration Platform for Everyone](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AttackForge.com is a free-to-use collaboration platform to manage pentesting projects. AttackForge allows a project team to easily collaborate in one place, reducing overheads and pain for all people involved - Customer, 3rd parties and Pentest Team. This is what makes AttackForge unique and different to other pentest collaboration solutions. It goes beyond automated reporting and issue library. It brings everyone together in one place and gives them tools and workflows to initiate & deliver a pentest, and also manage remediation testing.

Pentesters love to break things. However, they hate responding to unnecessary emails and phone calls; having to chase people for details to start testing; having to figure out who to talk to when things aren't working; and most of all having to write and review reports. AttackForge.com is purpose built to help pentesters focus their time and efforts on breaking things, and reduce distractions and unnecessary tasks. This helps to get the best out of the pentest team and provide better results for customers.

AttackForge.com also helps people to start a career in penetration testing. AttackForge provides a secure online environment to create a portfolio of pentests to reflect skills, knowledge, and communication ability in an industry-standard way – to demonstrate to recruiters and future employers that they are ready for the workforce. This may also help to reduce the shortage of supply and skills-gap our industry is currently facing.


### [AttackForge.com: Giving Time Back To Pentesters - More Breaking, Less Reporting](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Pentesters love what they do – breaking things. But there’s no denying that Penetration Testing as a practice itself is broken. Pentesters have only few days to a) learn how an entirely new system works under the hood; b) with this knowledge, learn some more so they can figure out how to break the system; c) try countless different ways to break the system or make it do things never intended or designed by the architects and developers; then d) write an executive and technical report to explain how they did it.

It feels like an impossible task for the typical <1-week project, so why on earth would you want to become or remain a pentester? When you do this week-in week-out, add on top pressures from clients, organisational bureaucracy, worrying about utilisation, fighting Word formatting, or having to constantly justify your risk ratings – it’s no wonder pentesters get burned out – fast!

We can’t fix all of these problems, but we have found a way to take some pressure off pentesters and help make communication, collaboration, transparency and reporting much easier, and reduce some of the overheads wasted on trivial tasks which all are part of a pentest project… introducing AttackForge.com.


### [AttackForge: Pentest Collaboration Platform for Everyone](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AttackForge.com is a free-to-use collaboration platform to manage pentesting projects. AttackForge allows a project team to easily collaborate in one place, reducing overheads and pain for Business, Technology and Pentest Team. This is what makes AttackForge unique and different to other pentest collaboration solutions. It goes beyond automated reporting and issue library. It's like JIRA for pentesting.

Pentesters love to break things. However they hate responding to unnecessary emails and phone calls; having to chase people for details to start testing; having to figure out who to talk to when things aren't working; and most of all having to write and review reports. AttackForge.com is purpose built to help pentesters focus their time and efforts on breaking things, and reduce distractions and unnecessary tasks. This helps to get the best out of the pentest team and provide better results for business.

AttackForge.com also helps people to start a career in penetration testing. AttackForge provides a secure online environment to create a portfolio of pentests to reflect skills, knowledge and communication ability in an industry-standard way – to demonstrate to recruiters and prospective employers that they are ready for the workforce. This may in turn help to reduce the shortage of supply and skills-gap our industry is currently facing.


### [AttackForge: Pentest Management & Collaboration Platform](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AttackForge.com is a free-to-use platform to manage your pentesting projects & programs, and to collaborate with everyone who needs to be involved - reducing overheads and pain for Customers, 3rd parties and Pentest Teams. This is what makes AttackForge unique and different to other pentest management & collaboration solutions. It goes beyond automated reporting and issue library. It brings everyone together in one place and gives them tools and workflows to initiate & deliver a pentest from start to end, and also manage remediation testing - with integrations into other industry tools & platforms.

Pentesters love to break things. They don't like manual, repetitive, boring tasks such copy/paste vulnerability write-up templates from old reports. AttackForge provides a rich issue library with over 1300 issues already built in that you can keyword search and select on your pentest. You can import vulnerabilities from your favourite tools such as Nessus & BURP, or even directly via the API. Reports can be generated on-demand and in PDF, DOCX, HTML, CSV, JSON. You can even use your own DOCX templates with the ReportGen tool to create fully customized and localised reports in minutes!

AttackForge.com also helps people to start a career in penetration testing. AttackForge provides a secure online environment to create a portfolio of pentests to reflect skills, knowledge, and communication ability in an industry-standard way – to demonstrate to recruiters and future employers that they are ready for the workforce. This may also help to reduce the shortage of supply and skills-gap our industry is currently facing.


### [AttackForge: Pentest Management Platform](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AttackForge.com is Community Pentest Management Platform that supports workflows for pentesting & collaboration between engineering & security teams.

AttackForge.com equips pentesters with the following:

- Dedicated workspace for penetration testing projects. You can invite other pentesters or engineers to your workspace and assign their roles. You can store all information/entry criteria/logs/etc.
- Assign methodologies/checklists to each project. AttackForge includes pre-built methodologies for convenience.
- Professional automated reporting. Fully customizable report templates using AttackForge ReportGen tool. AttackForge includes a styled base template to get started fast or you can use your own templates.
- Vulnerability library pre-loaded with 1300+ vulnerabilities. You can add your own.
- Import vulnerabilities from tools such as Nessus, BURP, Qualys, Netsparker, Acunetix, Nexpose, OpenVAS, ZAP. RESTful API for custom imports & generic CSV importer.
- Build AttackChains and map to MITRE ATT&CK Framework.
- Project management support including calendar, daily tracking, retesting tracking, and others.
- Integration with DevOps tools like JIRA & ServiceNow.
- Custom themes including "The Matrix" for the full Hacker experience

Come check out the new features we have not yet presented to public!


### [AutoRDPwn: The Shadow Attack Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AutoRDPwn is a post-exploitation framework created in Powershell, designed primarily to automate the Shadow attack on Microsoft Windows computers. This vulnerability (catalogued as a feature by Microsoft) allows a remote attacker to view the desktop of his victim without his consent, and even control it on demand, using native tools of the operating system itself.

Thanks to the additional modules, it is possible to obtain a remote shell through Netcat, dump system hashes with Mimikatz, load a remote keylogger and much more. All this, through a totally intiutive menu in seven different languages.

In this talk, we will briefly review the most common remote desktop attacks and the big difference the Shadow attack makes to them. Afterwards, we will make different live demonstrations, in which all the functionalities of the tool will be put into practice. Some of them are the following:

- UAC, AMSI and Windows Defender Bypass
- Remote Shell using native system and third party tools
- Obtaining hashes and pass the hash
- Remote execution without credentials via SMB, WMI and WinRM
- Shadow attack on different operating systems (both desktop and server versions)
- Miscellaneous (remote keylogger, one-line execution, pivoting and more)


### [Automated Attack Path Planning and Validation (A2P2V)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [AzureGoat : A Damn Vulnerable Azure Infrastructure](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Microsoft Azure cloud has become the second-largest vendor by market share in the cloud infrastructure providers (as per multiple reports), just behind AWS. There are numerous tools and vulnerable applications available for AWS for the security professional to perform attack/defense practices, but it is not the case with Azure. There are far fewer options available to the community. AzureGoat is our attempt to shorten this gap.

In this talk, we will be introducing AzureGoat, a vulnerable by design infrastructure on the Azure cloud environment. AzureGoat will allow a user to do the following:

- Explore a vulnerable infrastructure hosted on an Azure account
- Exploring different ways to get a foothold into the environment, e.g., vulnerable web app, exposed endpoint, attached MSI
- Learn and practice different attacks by leveraging misconfigured Azure components like Virtual Machines, Storage Accounts, App Services, Databases, etc.
- Abusing Azure AD roles and permissions
- Auditing and fixing misconfiguration in IaC
- Redeploying the fixed/patched infrastructure

The user will be able to deploy AzureGoat on their Azure account using a pre-created Docker image and scripts. Once deployed, the AzureGoat can be used for target practice and be conveniently deleted later.

All the code and deployment scripts will be made open-source after the talk.


### [BLOODHOUND 1.3 - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Released on-stage at DEF CON 24 last year, BloodHound fundamentally changed the way penetration testers and red teamers approach escalating rights in Active Directory domains. By combining the concepts of derivative local admin and graph theory, coupled with a powerful data ingestion and front-end analysis capability, BloodHound simplified the tedious, repetitive task of escalating rights, saving days, weeks, and sometimes months of manual processing.

In 2017, the BloodHound attack graph schema, data ingestor, and front-end were overhauled to provide greater speed, easier analysis, and brand new attack paths never discovered before. By adding object control edges to the attack graph, a brand new attack landscape was unveiled, allowing attackers and defenders to identify attacks which rely solely on Active Directory object manipulation. These attack paths require no malware, no pivoting, and can always be executed as long as the attacker can communicate with at least one domain controller. From the defender's perspective, identifying and measuring such attack paths was nigh impossible. Now, defenders can also quickly identify and remediate those same attack paths before an attacker can find and exploit them.


### [BUILDING C2 ENVIRONMENTS WITH WARHORSE](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Building full featured command-and-control (C2) environments can be a major undertaking, taking significant time and effort. However, deployment or proper infrastructure is key to avoiding detection and maintaining proper operational security during offensive engagements. In many instances, once a C2 environment is operational, it's utilized for a short period then destroyed. There are many different tools used within these C2 environments, with most tools requiring significant amounts of manual configuration. In recent years, API-based, on-demand cloud infrastructure has reduced the cost of building a C2 environment while also exposing functionality that encourages process automation. Combine these on-demand cloud services with the rapid development of Docker containers, and you have the building blocks to create and deploy C2 environments on the fly. Warhorse has been designed to build these C2 environments with only minimal configuration. Warhorse enables pentesters to focus on tactics instead of managing C2 infrastructure. Warhorse approaches this creation of a C2 environment with a few unique features. First, it uses a module-based approach to everything that it creates. This way, any new tactics or tools can be added as a module to utilize in creating a C2 environment. Second, Warhorse is vendor-agnostic and can be used with any cloud service provider. This allows C2 environments to live in multiple data centers and utilize multiple vendors. Lastly, Warhorse employs a two-zone approach to limit backend C2 exposure. Systems that communicate directly with the target are treated as expendable and can have very short life spans. These features combined not only help with rapid deployment but also allow pentesters to build environments with the latest tactics and techniques that can evolve on the fly and be moved whenever required.


### [Backdoor Pony: Evaluating Backdoor Attacks and Defenses in Different Domains](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Outsourced training and crowdsourced datasets lead to a new threat for deep
learning models: the backdoor attack. In this attack, the adversary inserts a
secret functionality in a model, activated through malicious inputs. Backdoor
attacks represent an active research area due to diverse settings where they
represent a real threat. Still, there is no framework to evaluate existing
attacks and defenses in different domains. Only a few toolboxes have been
implemented, but most of them focus on computer vision and are difficult
to use. To bridge this gap, we present Backdoor Pony, a framework for
evaluating attacks and defenses in different domains through a user-friendly
GUI.


### [Backoori: Tool Aided Persistence via Windows URI Schemes Abuse](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The widespread adoption of custom URI protocols to launch specific Universal App can be diverted to nefarious purposes. The URI schemes in Windows 10 can be abused in such a way to maintain persistence via fileless technique. Backdooring a compromised user (Administrator privileges not required) is a matter of seconds. The attack is transparent to the unaware victim that won't be able to identify the attack and to the antivirus solutions that are currently not monitoring the specific Registry keys involved. These subtle fileless payloads can be triggered in many contexts, from the Narrator in the Windows logon screen (a novel Accessibility Feature abuse discovered by Giulio right before deciding to implement Backoori) to the classical web attack surface. The payloads can also be dropped in gadgets that can interact between each other by abusing, once again, the Windows URI protocols.


### [Badrats: Initial Access Made Easy](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Remote Access Trojans (RATs) are one of the defining tradecraft for identifying an Advanced Persistent Threat. The reason being is that APTs typically leverage custom toolkits for gaining initial access, so they do not risk burning full-featured implants. Badrats takes characteristics from APT Tactics, Techniques, and Procedures (TTPs) and implements them into a custom Command and Control (C2) tool with a focus on initial access and implant flexibility. The key goal is to emulate that modern threat actors avoid loading fully-featured implants unless required, instead opting to use a smaller staged implant.

Badrats implants are written in various languages, each with a similar yet limited feature set. The implants are designed to be small for antivirus evasion and provides multiple methods of loading additional tools, such as shellcode, .NET assemblies, PowerShell, and shell commands on a compromised host. One of the most advanced TTPs that Badrats supports is peer-to-peer communications over SMB to allow implants to communicate through other compromised hosts.


### [Batea: Digging for gold in network data](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Batea is a simple tool that showcases how basic machine learning can help security analysts in their day-to-day operations. It is a context-driven network device ranking framework based on the anomaly detection family of machine learning algorithms. The goal of Batea is to allow security teams to automatically filter interesting network devices in large networks using nmap scan reports. We call those Gold Nuggets. Batea outputs the gold nuggets in order of interest for an attacker given the context of the network.

The human challenge is, on the one hand, that a typical enterprise network will host thousands of endpoints, far too many for a few security team members to constantly track and evaluate for their "attractiveness" to a potential intruder. On the other hand, the notion of interest is highly context-sensitive.

Batea works by constructing a numerical representation of all devices from your nmap reports (XML) and then applying the Isolation Forest algorithm to uncover the gold nuggets. It is easily extendable by adding specific "features", or interesting characteristics, to the numerical representation of the network elements.

The features act as elements of intuition, and the unsupervised anomaly detection methods allow the context of the device, along with the total description of the network, to be used as the central building block of the ranking algorithm.

Given that we have taken meaningful elements of intuition all at once, the fact that the Isolation Forest algorithm always takes the whole dataset into consideration ensures that the network context is embedded in the ranking used to predict Gold Nuggets.

Pen testers can train the Batea machine learning model from scratch on new network data, or use a model that has been pre-trained on various networks.


### [BloodHound 1.5](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
BloodHound is a single page Javascript web application, built on top of Linkurious, compiled with Electron, with a Neo4j database fed by a PowerShell ingestor. BloodHound uses graph theory to reveal the hidden and often unintended relationships within an Active Directory environment. Attackers can use BloodHound to easily identify highly complex attack paths that would otherwise be impossible to quickly identify. Defenders can use BloodHound to identify and eliminate those same attack paths. Both blue and red teams can use BloodHound to easily gain a deeper understanding of privilege relationships in an Active Directory environment. BloodHound is developed by @_wald0, @CptJesus, and @harmj0y.


### [BloodHound 5.0](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
BloodHound 5.0 is faster, more powerful, and easier to deploy and use than any previous version. With this major update, we are completely overhauling BloodHound's code and bringing many features from the commercial versions of BloodHound to the free and open source version. That convergence means we can release features much faster, and that the application is much faster than it ever has been. It also means the deployment model is fundamentally changing.


Come see our Arsenal presentation to see how to set up and use BloodHound 5.0, including attack path analysis and execution demonstrations covering on-prem Active Directory and Azure.


### [Blue Pigeon: Bluetooth-Based Data Exfiltration and Proxy Tool for Red Teamers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Break out the Box (BOtB): Container Analysis, Exploitation and CICD Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
BOtB is the first tool aimed at hackers and developers to automate Container exploitation. BOtB is a tool that can be used to analyze and identify vulnerabilities for Containers such as LXC and Docker. Not only does BOtB provide the user with a detailed analysis of identified vulnerabilities of the container, BOtB provides an autopwn feature which allows for the user to automagically exploit the vulnerabilities identified and break out onto the host. BOtB is able to identify multiple container vulnerabilities and contains a vast collection of exploits to break out of the container. BOtB is also developer friendly and has a Continuous Integration Continuous Development (CICD) mode which when enabled, BOtB will attempt to autopwn identified vulnerabilities but instead of dropping to host shells, it will return exit codes greater than 0 which is used by CICD technologies to indicate failed tests. When used in an Agile SDLC process implementing DevSecOps principles, this can assist developers with identifying Container issues prior to production deployments. BOtB is written in Golang and is distributed as a binary for multiple platforms.


### [Building Our Nemesis: Fighting Data with Data](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The offensive industry is about exploring what's possible. Part of this is observing and taking lessons from other disciplines that have already solved a myriad of related challenges, from proper software engineering practices to using graph theory for offensive problems. But despite various leaps forward over the last several years, the offensive post-exploitation community has yet to fully embrace data analysis and enrichment pipelines beyond basic log aggregation and searching. If offensive tools were structured for automated processing instead of solely human consumption, we could unify post-ex data to exploit the known (and unknown) relationships within the data our offensive tools emit.

Imagine a system that could ingest data from any C2 framework or post-ex tool, and could not just automate common operator tasks like binary analysis for known vulnerabilities and hash extraction and cracking of encrypted documents, but could perform complex offline analysis like host privilege escalation. If we could unify all post-exploitation data from offensive engagements we could improve operator workflows, provide tradecraft assistance, facilitate automation of onerous tasks, and uncover new data-driven research opportunities. A year ago, our team embarked on the development of just such a system, and we are excited to introduce the result of our effort: Nemesis.


### [C2 Matrix](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Command and Control is one of the most important tactics in the MITRE ATT&CK matrix as it allows the attacker to interact with the target system and realize their objectives. Organizations leverage Cyber Threat Intelligence to understand their threat model and adversaries that have the intent, opportunity, and capability to attack. Red Team, Blue Team, and virtual Purple Teams work together to understand the adversary Tactics, ﻿Techniques, and Procedures to perform adversary emulations and improve detective and preventive controls.

The C2 Matrix was created to aggregate all the Command and Control frameworks publicly available (open-source and commercial) in a single resource to assist teams in testing their own controls through adversary emulations (Red Team or Purple Team Exercises). Phase 1 lists all the Command and Control features such as the coding language used, channels (HTTP, TCP, ﻿DNS, SMB, etc.), agents, key exchange, and other operational security features and capabilities.﻿﻿ This allows more efficient decisions making when called upon to emulate and adversary TTPs.

It is the golden age of Command and Control (C2) frameworks. Learn how these C2 frameworks work and start testing against your organization to improve detective and preventive controls.


### [C2 Matrix: Comparison of Command and Control Frameworks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Command and Control is one of the most important tactics in the MITRE ATT&CK matrix as it allows the attacker to interact with the target system and realize their objectives. Organizations leverage Cyber Threat Intelligence to understand their threat model and adversaries that have the intent, opportunity, and capability to attack. Red Team, Blue Team, and virtual Purple Teams work together to understand the adversary Tactics, Techniques, and Procedures to perform adversary emulations and improve detective and preventive controls.

The C2 Matrix was created to aggregate all the Command and Control frameworks publicly available (open-source and commercial) in a single resource to assist teams in testing their own controls through adversary emulations (Red Team or Purple Team Exercises). Phase 1 lists all the Command and Control features such as the coding language used, channels (HTTP, TCP, DNS, SMB, etc.), agents, key exchange, and other operational security features and capabilities. This allows more efficient decisions making when called upon to emulate and adversary TTPs.

It is the golden age of Command and Control (C2) frameworks. Learn how these C2 frameworks work and start testing against your organization to improve detective and preventive controls.

The C2 Matrix currently has 41 command and control frameworks documented in a Google Sheet, web site, and questionnaire format.

For Blackhat, C2 Matrix will release phase 2 of the project which involves mapping each C2 to MITRE ATT&CK and correlate with known adversaries. This will allow much quicker selection of which C2s to use for a given adversary or threat scenarios.


### [CALDERA: Automating Adversary Emulation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Adversary emulation is great, but it can be time consuming – so why not automate it? CALDERA automates the adversary emulation process, allowing users to run fully automated adversary emulation exercises, aligning its operations with MITRE ATT&CK. Blue and red teamers alike can use CALDERA for training, to test analytics and defensive tools, and just generally to stress test their networks and systems.


CALDERA was first released in late 2017 featuring its end-to-end “adversary mode” capability, where operators could use CALDERA to run fully end-to-end tests emulating the full adversary lifecycle. This mode allowed CALDERA to run intelligently and autonomously, leveraging a planning system to dynamically compose operations.


Since this first release, the MITRE team has continued to expand CALDERA’s capabilities, releasing a new “chain mode” in 2019. This new mode allows users much more control over CALDERA, letting them orchestrate and automate atomic unit tests as opposed to end-to-end operations. With more fine-grained control over CALDERA, users can better control their operations to accommodate more use cases, such as testing and refining analytics.


This demo will highlight both of CALDERA’s modes, providing demos and guides on how to use CALDERA including how to extend it with new plugins and adding additional tests. CALDERA is open source and can be downloaded off of the MITRE GitHub repository.


### [CANalyse: A Vehicle Network Analysis and Attack Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CANalyse is a software tool built to analyze the log files to find out unique data sets automatically and able to connect to simple attacker interfaces such as Telegram. Basically, while using this tool you can provide your bot-ID and be able to use the tool over the internet through telegram. It is made to be installed inside a raspberry-PI and able to exploit the vehicle through a telegram bot by recording and analyzing the data logs, it is like a hardware implant planted inside a car which acts as a bridge between the Telegram bot and the Vehicle's network.


### [CDK: Zero Dependency Container Penetration Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CDK is an open-sourced container penetration toolkit, offering stable exploitation in cloud-native docker/k8s/serverless deployments. It comes with many powerful tools and exploits without any OS dependency, helps you to escape container and takeover K8s cluster easily.


### [CQ PrivilegeEscalation Toolkit: Effective Tools for Windows Privilege Escalation Gamers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CQURE PE Toolkit is focused on Windows Privilege Escalation tactics and techniques created to help to improve every privilege escalation game. This toolkit guides you through the process of exploiting a bug or design flaw in an operating system or software to gain elevated privileges to resources that are normally highly protected. Once you know what to look for and what to ignore, Privilege Escalation will become so much easier. This powerful toolkit is tremendously useful for those who are interested in penetration testing and professionals engaged in pen-testing who work in the areas of databases, systems, networks, or application administration.


### [CQOffensiveSecurity: The Extreme Windows Offensive Security Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CQOffensiveSecurity Toolkit enables you to perform advanced Windows Infrastructure Penetration Testing. It guides you through the process of gathering intel about network, workstations and servers. Common technics for privilege escalation, antimalware avoidance and bypass, credential harvesting and lateral movement. Toolkit allows also for decrypting RSA keys and EFS protected files as well as blobs and objects protected by DPAPI and DPAPI-NG. This toolkit is commonly used among CQURE Experts and pentesters on daily basis. Among published presented tools: CQRepacker, CQSecretDumper, CQLsasSecretDumper, CQCredentialHarvester, CQSystemEscalator, CQTcbImpersonate, CQSqlTDEdecrypter and many more. During the BlackHat we would like to announce brand new tools for escalation and lateral movement for PKI and ADFS as well as disabling Azure Information Protection to search through encrypted and protected files at rest. CQOffensiveSecurity is a very practical toolkit for pentesters and RedTeamers.


### [CQPenetrationTesting Toolkit: A Powerful Toolset That All Pentesters Want to Have](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CQ Penetration Testing Toolkit supports you in performing complex penetration tests, shows you their possible application, and highlights the situations in which they apply. It guides you through the process of gathering intel about network, workstations, and servers, and showcases common techniques for antimalware avoidance and bypass, lateral movement, and credential harvesting. The toolkit also allows decrypting RSA keys and EFS-protected files as well as blobs and objects protected by DPAPI and DPAPI NG. This powerful toolkit is useful for those who are interested in penetration testing and professionals engaged in pen-testing who work in the areas of databases, systems, networks, or application administration.


### [CQPenetrationTesting Toolkit: Powerful Toolset That All Pentesters Want to Have](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CQ Penetration Testing Toolkit supports you in performing complex penetration tests as well as shows the ways to use them, and the situations in which they apply. It guides you through the process of gathering intel about network, workstations, and servers. Common technics for antimalware avoidance and bypass, lateral movement, and credential harvesting. The toolkit allows also for decrypting RSA keys and EFS protected files as well as blobs and objects protected by DPAPI and DPAPI-NG. This powerful toolkit is useful for those who are interested in penetration testing and professionals engaged in pen-testing working in the areas of database, system, network, or application administration. Among published presented tools are CQARPSpoofer, CQCat, CQDPAPIBlobDecrypter, CQMasterKeyDecrypt, CQReverseShellGen, and many more.


### [CQPrivilegeExcalation Toolkit: Effective Tools for Windows Privilege Escalation Gamers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CQURE PE Toolkit is focused on Windows Privilege Escalation tactics and techniques created to help improve every privilege escalation game. This toolkit guides you through the process of exploiting a bug or design flaw in an operating system or software to gain elevated privileges to resources that are normally highly protected. Once you will know what to look for and what to ignore, Privilege Escalation will be so much easier. This powerful toolkit is useful for those who are interested in penetration testing and professionals engaged in pen-testing working in the areas of database, system, network, or application administration. Among published presented tools are CQSecretsDumper, CQNTDSDTDecrypter, CQLsassSecretsDumper, CQCreateProcessWithParent, and many more.


### [CUMULUS - A CLOUD EXPLOITATION TOOLKIT](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
There is a lack of tools for testing the security of Cloud deployments; the Cumulus Toolkit is an attack framework for exploiting the Cloud's weak points.

The Cloud enables software projects to speed up development because it allows developers to provision infrastructure and make configuration changes to their networks without much friction. This ease of deployment was but a dream in the age of the traditional datacenter. However, the Cloud also brings new attack surface which needs further exploration. Cloud Identity and Access Management (IAM) services (such as Amazon's) are primary targets for attackers, as these typically control access to hundreds of API calls over many services.

Over the years there have been various discussions around cloud security, e.g., Pivoting in Amazon Clouds (2013), and few tools have been developed to enable testing the security of Cloud deployments. These tools are standalone, have not attained wide adoption, and/or have not made it into widely adopted toolkits. To fill this void, we have developed the Cumulus Toolkit. The Cumulus Toolkit is a Cloud exploitation toolkit based on the Metasploit Framework. We chose Metasploit because of its wide adoption and its wealth of existing features.

The Cumulus toolkit is a set of modules that can be used perform privilege escalation, account takeover, and to launch unauthorized workloads. To illustrate security concerns resulting from lax IAM policies, we present the Create IAM User module which can be used to create a user with administrative privileges. To perform complete account takeover, an attack that we've seen in the wild, we present the User Locker module which is used to lock out all legitimate users out of the account. Finally, we present the Launch Instances module which can be used to launch Cloud hosts on demand.


### [Chiron: An Advanced IPv6 Security Assessment and Penetration Testing Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Chiron is an IPv6 Security Assessment Framework, written in Python and employing Scapy. It is comprised of the following modules:

• IPv6 Scanner
• IPv6 Local Link
• IPv4-to-IPv6 Proxy
• IPv6 Attack Module
• IPv6 Proxy
All the above modules are supported by a common library that allows the creation of completely arbitrary IPv6 header chains, fragmented or not. Suggested host OS: Linux (*BSD may also work).

Source Code: https://github.com/aatlasis/Chiron﻿


### [Cloud Katana](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Cloudtopolis: Zero Infrastructure Password Cracking](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Cloudtopolis is a tool that facilitates the installation and provisioning of Hashtopolis on the Google Cloud Shell platform, quickly and completely unattended (and also, free!). Together with Google Collaboratory, it allows us to break hashes without the need for dedicated hardware from any browser (even from your smartphone).

Thanks to its implementation through Docker, it can be run almost anywhere in a fast and easy way. In addition, it can be used collaboratively using different accounts, being very useful for use in CTF teams or in Red Team exercises.

As a novelty in this talk, automated clients for Windows and Linux (not disclosed yet) will be presented, being able to additionally use the user's local resources together with the graphic cards provided by Colab.


### [Codecepticon - One Obfuscator to Rule Them All](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Codecepticon is an obfuscator that works with C#, PowerShell, and VBA (macros), and has been battle-tested for the last 1.5yr against modern ERD and AV technologies with great success. It supports a variety of obfuscation techniques such as renaming classes, and functions, rewriting strings and the tool's command line arguments, and even generating "English sounding" variable names using Markov chains. Instead of targeting compiled executables/assemblies, it focuses on the source code and utilizes Roslyn for C#, PS Automation for PowerShell, and ANTLR for VBA, in order to achieve the best possible result.


### [CoffeeShot: Avoid Detection with Memory Injection](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
For the first time ever, we are introducing a framework that utilizes the usage of Java Native Access with Java. How did we take advantage of that? Well, we used this to call to interesting Windows API's directly from Java. CoffeeShot is a framework that was designed for creating Java-based malware which bypasses most of the anti-virus vendors. CoffeeShot utilizes the features of JNA to look for a victim process, once it finds it - a shellcode will be injected directly from the Java Archive file (JAR).

Java malware like "Jrat" and "Adwind" are used by malicious adversaries day by day, more and more. Their main reason for writing malware in Java is to be evasive and avoid security products – including those that use advanced features like machine learning. To overcome the above, blue-teamers can use this framework and thereby understand their status of anti-malware weakness against Java-based malware.

On the other hand, CoffeeShot can be applied by penetration testers as well. The framework provides red-teamers a friendly toolset by allowing them to embed any shellcode in a JAR file, assisting them to avoid detection with memory injection and to PWN the target!


### [CoffeeShot: Memory Injection to Avoid Detection](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CoffeeShot is an evasion framework that designed for creating Java-based malware which bypasses most of the anti-virus vendors. The framework utilizes JNA (Java Native Access) to look for a victim process, once it finds it - a shellcode will be injected directly from the Java Archive file (JAR).

Java malware like "Jrat" and "Adwind" are used by malicious adversaries' day by day, more and more. Their main reason to write malware in Java is to be evasive and avoid security products - including those that use advanced features like machine learning. To overcome the above, blue-team members can use this framework in assessing the effectiveness of their anti-malware measures against malicious software written in Java.

On the other hand, CoffeeShot can be applied by penetration testers as well. The framework provides red-teamers a friendly toolset by allowing them to embed any shellcode in a JAR file, assisting them to avoid detection with memory injection and to PWN the target!


### [Commando VM 2.0: Security Distribution for Penetration Testers and Red Teamers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Commando VM is an open-source Windows-based security distribution designed for Penetration Testers and Red Teamers. It is an add-on from FireEye's very successful Reverse Engineering distribution: FLARE VM. Much like Kali Linux, Commando VM is designed with an arsenal of open-source offensive tools that will help operators achieve assessment objectives.

Being built on Windows, Commando VM comes with all the native support for accessing Active Directory environments. Additionally, Commando VM includes Web Application assessment tools, scripting languages (such as Python and Go), Information Gathering tools (such as Nmap, WireShark, and PowerView), Exploitation Tools (such as PowerSploit, GhostPack and Mimikatz), Persistence tools, Lateral Movement tools, Evasion tools, Post-Exploitation tools (such as FireEye's SessionGopher), Remote Access tools, Command-Line tools, and all the might of FLARE VM's reversing tools.

Commando VM 1.0 was greeted with tremendous enthusiasm and praise when it debuted at Black Hat Asia in Singapore this year; afterwards, it generated lots of media buzz. Less than two weeks after release our GitHub repository had over 2000 followers and over 400 forks. For Black Hat USA, we are debuting Commando VM 2.0, with full support for Kali on the Windows Subsystem for Linux, as well as giving users the ability to customize what tools get installed on their system.


### [Commando VM and FLARE VM: Enhanced Toolsets for Penetration Testing and Windows-Based Malware Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
We are excited to release the latest version of Commando VM and showcase recent advancements of FLARE VM at the Black Hat Arsenal. Commando VM is a virtual machine distribution focused on penetration testing and red teaming. FLARE VM is tailored for malware analysis and reverse engineering. Both Windows-based tools have undergone significant enhancements to improve their usability, functionality, and efficiency. The projects now open source all packages, allowing the community to add and improve tools. Additionally, we have implemented a new GUI installation process to streamline the setup and configuration experience for both new and experienced users.

The latest iteration boasts new profiles for Commando VM, enabling users to tailor their environment to specific penetration testing and red teaming scenarios. Whether the user focuses on Cloud, Web App, or Internal testing, Commando VM has a ready-to-use profile for them with all relevant configurations and toolkit. In addition to that, the user can also create and save their own custom profile, allowing them to easily automate future VM deployments.

Furthermore, we have made substantial quality of life improvements, including debloating and performance optimization, resulting in faster, leaner, and more efficient virtual machines. Users will benefit from these enhancements as they navigate through the intricacies of malware analysis, reverse engineering, and penetration testing with the updated Commando VM and FLARE VM toolsets.

Join us at the Black Hat Arsenal to discover the power and flexibility of the next generation of Commando VM and FLARE VM. We will share how the updated tools can support your workflows in malware analysis, reverse engineering, and penetration testing. Additionally, you will learn how to contribute new tool and code updates benefiting thousands of analysts around the world.


### [CommandoVM: Security Distribution for Penetration Testers and Red Teamers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CommandoVM is an open-source Windows-based security distribution designed for Penetration Testers and Red Teamers. It is an add-on from FireEye's very successful Reverse Engineering distribution: FLARE VM. Much like Kali Linux, CommandoVM is designed with an arsenal of open-source offensive tools that will help operators achieve assessment objectives.

Being built on Windows, CommandoVM comes with all the native support for accessing Active Directory environments. CommandoVM includes Web Application assessment tools, scripting languages (such as Python and Go), Information Gathering tools (such as Nmap, WireShark, and PowerView), Exploitation Tools (such as PowerSploit, GhostPack and Mimikatz), Persistence tools, Lateral Movement tools, Evasion tools, Post-Exploitation tools (such as FireEye's SessionGopher), Android Hacking tools, Remote Access tools, Command-Line tools, and all the might of FLARE VM's reversing tools.

Quality-of-Life changes to the OS include: disabling UAC, Windows Defender and Windows Firewall, disabling LLMNR and NetBIOS , having some pinned applications (CMD, PowerShell, Sublime Text, VS Code) run as administrator automatically, as well as added context menu options like "Open With Sublime Text" and "Open Command Prompt Here" to ease the frustration of working with a Windows pen-testing environment. CommandoVM strives to be your go-to Windows environment for penetration tests, red team engagements, and Capture-the-Flag events.


### [Cotopaxi - M2M Protocols Assessment Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Cotopaxi is a set of tools for security testing of endpoints using state-of-the-art Machine-To-Machine network protocols (like AMQP, CoAP, gRPC, HTTP/2, HTCPCP, MQTT, DTLS, KNX, mDNS, QUIC, RTSP, SSDP).


### [Cotopaxi: IoT/IIoT/M2M Protocols Security Testing Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Cotopaxi is a set of tools for security testing of network devices using specific and general network IoT/IIoT/M2M protocols (AMQP, CoAP, DTLS, gRPC, HTTP/2, HTCPCP, KNX, mDNS, MQTT, MQTT-SN, QUIC, RTSP, SSDP).


### [Covenant: .NET Command and Control](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Covenant is a .NET command and control platform and web application that aims to highlight the attack surface of the .NET Framework and .NET Core, make the use of offensive .NET tradecraft easier, and serve as a collaborative platform for red teamers.

Covenant is multi-platform, multi-user, provides an intuitive web application interface, and is extendible through an API.

Covenant includes multiple built-in implants that utilize the traditional .NET Framework and .NET Core, which gives Covenant multi-platform implants that run on Windows, Linux, and MacOS. Additionally, Covenant allows operators to edit and add additional custom implants.

Covenant includes built-in support for custom and complex command and control routing. The platform includes built-in outbound listeners, including an HTTP and TCP listener, and peer-to-peer SMB communications over named pipes, which allows for complex implant networking. The platform also includes a protocol for adding new, custom communication protocols that gives the operator complete control over how the command and control traffic appears on the wire.

Covenant includes tons of built-in tasks based on libraries such as SharpSploit and GhostPack, and uses dynamic C# compilation and ConfuserEx obfuscation on tasks and payloads.

Covenant also has an emphasis on implant and network communication security to protect the data accessed by implants. Covenant implements an Encrypted Key Exchange protocol between implants and listeners to achieve forward secrecy for new implants and enforces SSL certificate pinning for implants.

In the age of EDR and threat hunting, red teamers need flexible, robust, and intuitive command and control platforms. Red teamers need the ability to collaborate with teammates, customize implant behavior and command and control traffic, track artifacts, and quickly adapt for defensive technologies. In this demo, you'll be shown how to accomplish this with Covenant.


### [CRACKMAPEXEC V4](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
CrackMapExec (a.k.a CME) is a fully open-source, post-exploitation tool written in Python that helps automate assessing the security of *large* Active Directory networks. Built with stealth in mind, CME follows the concept of "Living off the Land:" abusing built-in Active Directory features/protocols to achieve it's functionality and allowing it to evade endpoint protection/IDS/IPS solutions. CME makes heavy use of the Impacket library and the PowerSploit Toolkit for working with network protocols and performing a variety of post-exploitation techniques. Although meant to be used primarily for offensive purposes (e.g. red teams), CME can be used by blue teams as well to assess account privileges, find possible misconfigurations and simulate attack scenarios. In this demo the author will be showing version 4.0: a major update to the tool bringing more modules, features and capabilities than ever before. If you're interested in the latest & greatest Active Directory attacks, techniques and general cool AD stuff this is the demo for you!


### [CuddlePhish: Bypassing MFA on Nearly Impenetrable Web Portals](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
With the increased adoption of multi-factor authentication, traditional credential harvesting attacks are quickly losing effectiveness. Instead, redteamers have shifted focus away from credential harvesting and are now focussing on session hijacking attacks. Popular redteaming tools like Evilginx2 use transparent proxies to collect both credential AND session cookies from phishing targets. But what if the target service uses more advanced authentication flows like Oauth or SAML? What about apps that use JavaScript to directly thwart MitM attacks? Or even worse, services that don't grant authorization through session cookies at all? Our team has seen many instances of MitM protections like these, and in response, we are raising the bar for session hijacking tradecraft. Instead of using a transparent proxy, our solution leverages browser automation to force target users to log us into services for them. We don't just get to view the traffic. We get full control of an authenticated browser tab. Our solution, CuddlePhish, allows operators to bypass MFA even when MitM protections are in place, target multiple users simultaneously, key log users' credentials, trigger arbitrary javascript on victims' browsers to either redirect them or deliver payloads, and hijack not just session cookies, but authenticated browser tabs themselves. We have successfully used this attack against extremely difficult portals like Gmail and Lastpass.


### [Cyber Weapon Range](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [CyberRange: An Open-Source Offensive/Defensive Security Lab in AWS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
This CyberRange project represents the first open-source Cyber Range blueprint in the world.

This project provides a bootstrap framework for a complete offensive, defensive, reverse engineering, and security intelligence tooling in a private research lab using the AWS Cloud. This project contains vulnerable systems, open-source tools.

It simply provides a researcher with a disposable offensive/defensive AWS-based environment in less than 10 minutes.


### [DELTA: SDN Security Evaluation Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
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


### [DFEX](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
DFEX - [DNS File EXfiltration]

Data exfiltration is a common technique used for post-exploitation, DNS is one of the most common protocols through firewalls.
We take the opportunity to build a unique protocol for transferring files across the network.

Existing tools have some limitations and NG Firewalls are getting a bit "smarter", we have been obliged to explore new combinations of tactics to bypass these. Using the good old fashion "HIPS" (Hidden In Plain Sigh) tricks to push files out.


### [DNSStager: A Tool to Hide Your Payload in DNS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [DSInternals PowerShell Module](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The DSInternals PowerShell Module exposes many internal and undocumented security-related features of Active Directory. It is included in FireEye's Commando VM and its cmdlets can be used in the following scenarios:

- Active Directory password auditing that discovers accounts sharing the same passwords or having passwords in a public database like HaveIBeenPwned.
- Offline ntds.dit file manipulation, password resets, group membership changes, SID History injection and enabling/disabling accounts.
- Bare-metal recovery of domain controllers from just IFM backups (ntds.dit + SYSVOL).
- Online password hash dumping through the Directory Replication Service Remote Protocol (MS-DRSR).
- Domain or local account password hash injection, either through the Security Account Manager Remote Protocol (MS-SAMR) or by directly modifying the database.
- LSA Policy modification through the Local Security Authority Remote Protocol (MS-LSAD / LSARPC).
- Extracting credential roaming data and DPAPI domain backup keys, either online through directory replication and LSARPC, or offline from ntds.dit files.


### [DSP: Docker Security Playground](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
This presentation covers the design and implementation of the Docker Security Playground (DSP), an architecture leveraging a microservices-based approach in order to build complex network infrastructures specifically tailored to the study of network security. DSP has been conceived at the outset as a tool for learning network security with a hands-on approach. A number of security labs have been already realized and made available in a public repository. The talk discusses how such labs can be fruitfully exploited by students, as well as presents the Application Programming Interface offered to programmers interested in the implementation of new labs.


### [DeepSea Phishing Gear](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Introducing DeepSea, the phishing gear you will want to take with you on your next offensive expedition. 

It is designed to help Red Team operators and teams with the tactical delivery of opsec-tight, flexible email phishing campaigns carried out in a portable manner on the outside as well as on the inside 
of a perimeter. 

Have you ever wanted to seamlessly operate with external and internal email providers; quickly re-target connectivity parameters per campaign; flexibly add headers, targets, attachments, correctly format and inline email templates, images and multipart messages; use content templates for personalization; clearly separate artifacts and content delivery for multiple (parallel or sequential) phishing campaigns; get actionable context help and deploy with minimal dependencies? 

In this session, we will show how you can do this and more in a portable, one binary cross platform setup, with less than 50 lines in a configuration file. 

With DeepSea, you will be able to keep campaign persistence with DNS tricks and an embedded email server used for running advanced two-way threaded campaigns you have always wanted. Catch and respond to those often missed inquiry emails, solidifying pretext and pacifying your marks.

Whether you plan on executing phishing campaigns deep on the inside of the perimeter, or bounce across multiple email providers for an external stealthy campaign delivery, DeepSea is very likely able to help.


### [Democratizing Attack Techniques in the Cloud withThe DeRF](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
DeRF (Detection Replay Framework) is an "Attacks As A Service" framework, allowing the emulation of offensive techniques and generation of repeatable detection samples from a UI - without the need for End Users to install software, use the CLI or possess credentials in the target environment.

Notable built-in attack modules are listed below with a complete list of all built-in attack techniques in The DeRF documentation.

o AWS | EC2 Steal Instance Credentials
o AWS | Retrieve a High Number of Secrets Manager secrets.
o AWS | Stop CloudTrail
o AWS | Execute Commands on EC2 Instance via User Data
o AWS | EC2 Download User Data
o AWS | EC2 Share EBS Snapshot
o GCP | Impersonate Service Account

Similar to other tools focused on detection generation, the DeRF deploys and manages the target cloud infrastructure, which is manipulated to simulate attacker techniques.
Terraform is used to manage all resources, deploying (and destroying) hosted attack techniques and target infrastructure in under 3 minutes.

While a bring-your-own-Infrastructure (BYOI) model isn't currently supported, maintaining The DeRF infrastructure costs less than $10/month for Google Cloud and $5/month for AWS. The tool's convenient deployment model means you can use it as needed rather than continuously running 24/7. Check out the deployment guide for more details.

The initial release of The DeRF encompasses a wide range of prevalent cloud attack techniques, providing your organization with ample resources for training, controls testing, and executing on attack scenarios. However, as needs evolve, you may need to expand beyond the initial set and introduce your own custom attack modules. With The DeRF, this process is simplified. All attack techniques are defined as Google Cloud Workflows, which can be deployed as additional terraform modules within your forked version of the codebase.


### [Docker Exploitation Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Docker Exploitation Framework is a cross-platform framework that is focused on attacking container environment (think kubernetes, docker etc). It can identify vulnerabilities, misconfigurations, and potential attack vectors. It also helps to automate different stages of a successful kill-chain through features such as:
- Vulnerability Scanning
- Container breakouts
- Pod2Pod Lateral movement
- File layers deep inspection and extraction
- Attack Surface discovery and mapping
- Privilege Escalation etc

It uses a agent/server architecture. The agents are modular and are designed to be portable with minimal dependencies for maximum compatibility in restricted containers. This is a tool created for pentesters and red teamers.


### [Docker Security Playground](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Docker Security Playground is an architecture leveraging a microservices-based approach in order to build complex network infrastructures specifically tailored to the study of network security. The idea is to leverage latest fashion virtualization techniques in order to: (i) reproduce real-world networking scenarios; (ii) build ad-hoc network playgrounds involving vulnerable nodes/services and malicious users/tools; (iii) provide lab participants with low-cost, COTS-based, easily reproducible networking tools.


### [Dolos Cloak: Your NAC Can't See This](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Dolos Cloak is a new tool designed to give penetration testers and red team members the ability to easily bypass 802.1x network access controls. The tool performs an advanced man-in-the-middle attack against nearly any authorized network device, automatically configures a NAT to blend in, and pass legitimate traffic unaltered. Simply plug a Dolos Cloak device in between a network jack and an available workstation, IP phone, printer, or other device and walk away. Dolos Cloak can be configured to call home using TPC/UDP reverse shells, SSH, VPN, Empire, or other custom methods to maintain a stealthy foothold on the network. The creation of Dolos Cloak was inspired by sysadmins that thought they could rely solely on 802.1x to keep attackers off their networks.


### [Dragnmove: Infect Shared Files In Memory for Lateral Movement](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
People share files with each other every day using different applications like email clients, chat applications, browsers, etc. These channels are commonly used for lateral movement usually in the context of internal phishing. Dragnmove tool provides a different approach to abuse file sharing in order to move laterally in the target environment. Dragnmove can be used to inject payloads into the files that are being sent without touching the files in the file system.

The tool works on Windows targets and can be executed as Beacon Object File (BOF) or Reflective DLL in order to work with various C2 servers. Dragnmove injects itself into the target processes that the attacker chooses and waits for the user to drag a file into this process or attach a file to it.

When a compromised user starts the sharing process, Dragnmove can modify files in memory to inject the attacker's payload into the shared files by hooking the Windows mechanisms used by actions like "drag and drop" or "attach file". This method provides a better opportunity for the attackers to get their payloads executed in the lateral targets because the files sent will be relevant to the targets' contexts. Since the context and sender are relevant, it is more possible that the target sees this file as trustable and opens it. Dragnmove can also be used in environments where the targets are working in different locations or in isolated networks (like working from home) so the usual lateral movement methods cannot be utilized.


### [Dynamic Labs: Windows & Active Directory Exploitation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
If you are after red-team training, there are multiple excellent courses and online resources for practising adversary simulation. That's not the primary motivation behind Alfa labs.

Alfa labs allows:
- Blue/red teamers to test or demonstrate specific attacks/attack-paths (e.g. when GMSA edges were introduced into BloodHound).
- Beginners to take a structured approach to learning Active Directory weaknesses (which have largely been practically accessible if you build your own lab, during workshops w/ limited spaces or commercial training).
- Replicate any technical issues and confirm your results

Therefore, stop by and spin up your own lab to practise your Windows Active Directory tools, techniques and procedures (TTPs) in isolation, or red-team your way through the dynamically-built Alfa labs.


### [EAPHAMMER](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
EAPHammer is a toolkit for performing targeted evil twin attacks against WPA2-Enterprise networks. It is designed to be used in full scope wireless assessments and red team engagements. As such, focus is placed on providing an easy-to-use interface that can be leveraged to execute powerful wireless attacks with minimal manual configuration. To illustrate how fast this tool is, here's an example of how to setup and execute a credential stealing evil twin attack against a WPA2-TTLS network in just two commands:

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


### [Echidna: Penetration Test Assist & Collaboration Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Echidna is a tool designed to support teams or beginners in conducting penetration testing.
While there are many tools available to assist or automate penetration testing, mastering them requires knowledge of numerous commands and techniques, making it challenging for beginners to learn and carry out penetration testing. Furthermore, when conducting penetration tests in a team, each member tends to work independently, which can lead to duplication of work and lack of visibility of progress for managers and beginners.
Therefore, we developed Echidna, which visualizes and shares the terminal console of penetration testers, and recommends the next command based on each situation.


### [ElfPack: ELF Binary Section Docking in Stageless Payload Delivery](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
When it comes to generating and delivering malware on Linux, offensive operators have choices. Some objectives call for a dynamic payload bootstrap off the wire, others require stageless implants.

Often, malware deployed with bundled payloads can be successfully detected and analyzed. However, we think there are opportunities to improve on the process of embedding payloads in standalone implants that can elevate their survival levels.

ElfPack is one such development in the static payload embedding and loading tailored for adversary simulation teams. In our demo we will demonstrate the mechanisms of construction of ELF binaries, focusing on how ELFPack can use sections facilitate a successful stealthy payload hosting, retrieval and loading.

We will show the concept of ELF section docking, whereby a section containing payload can be independently attached to the payload-agnostic loader. We will further expand the concept to address in-field (re-)attachment of sections to loaders without the use of compilers which may be very useful for long-haul offensive operations.

Furthermore, we will show how ElfPack can be successfully used as an alternative to executable packing when addressing complex payloads and providing teams with options and flexibility in multiple payload delivery scenarios.

We will demonstrate both detection opportunities and the enhanced evasion features implemented in a ElfPack proof-of-concept loader and injector tooling.

We feel that ElfPack and section docking in general can help solve some of the payload bundling challenges for the offensive operators, and also introduce ideas to hunters to detect and respond to this technique.


### [EmoLoad: Loading Emotet Modules without Emotet](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Empire: Post-Exploitation Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Empire is a Command and Control (C2) framework powered by Python 3 that supports Windows, Linux, and macOS exploitation. It leverages many widely used offensive security tools through PowerShell, Python 3, and C# agents. At the same time, it offers cryptologically-secure communications and flexible modular architecture that links Advanced Persistent Threats (APTs) Tactics, Techniques, and Procedures (TTPs) through the MITRE ATT&CK database.

Empire has evolved significantly since its introduction in 2015 and has become one of the most widely used open-source C2 platforms. Through this time, Empire has advanced from a single user experience to allowing multiple user operations through an API with Empire acting as a teamserver. Currently, 2 different applications are available to connect to the Empire teamserver: Empire Command Line Interface (CLI) and Starkiller.

The Empire CLI is built from the ground up as a replacement to the embedded legacy CLI and gives users a familiar feel of the legacy CLI, but is portable and connects through the Empire API. While Starkiller is a cross-platform UI available in Linux, Windows, and macOS powered by ElectronJS.

The framework's flexibility to easily incorporate new modules allows for a single solution for red team operations with the aim for Empire to provide an easy-to-use platform for emulating APTs. Customization is essential to any successful red team operation, which has driven the expansion of user plugins. These plugins allow any custom program to run side-by-side with the Empire teamserver. In addition, the commonality between other C2 platforms allows profiles and modules to be easily dropped in without the need for additional development. These features allow both red and blue teams to easily emulate and defend against the APT attack vectors.


### [EmploLeaks: Finding Leaked Employees Info for the Win](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  



### [EntraID Guest to Corp Data Dump with powerpwn](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
EntraID guest accounts are widely used to grant external parties limited access to enterprise resources, with the assumption that these accounts pose little security risk. As you're about to see, this assumption is dangerously wrong.

powerpwn is an offensive security toolset for Microsoft 365 focused on Power Platform. It allows you to achieve the full potential of a guest in EntraID by exploiting a series of undocumented internal APIs and common misconfiguration for collecting privileges, and using those for data exfiltration and actions on target, leaving no traces behind. The tool operates by leveraging shared credentials shared over Power Platform, a low-code / no-code platform built into Office365.

PowerGuest allows gaining unauthorized access to sensitive business data and capabilities including corporate SQL servers and Azure resources. Furthermore, it allows guests to create and control internal business applications to move laterally within the organization. All capabilities are fully operational with the default Office 365 and Azure AD configuration.


### [EvilnoVNC: Next-Gen Spear Phishing Attacks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
One of the main attack vectors in Red Team exercises, and possible entry points for an attacker, are phishing campaigns.

Currently, there are all kinds of tools and countermeasures to perform or defend against them, with a very high level of maturity and fully consolidated by the industry for many years.

On the other hand, there are hardly any tools oriented to Spear Phishing or any other type of more sophisticated attack, regardless of whether you are part of the Red Team or the Blue Team.

In this presentation, and from a totally offensive approach, we will explain how it has been possible to develop a new tool aimed at Spear Phishing, which will use techniques never seen before for this purpose, allowing us to see what the victim is doing in real time, intercept keystrokes with a keylogger, obtain and decrypt cookies, among many other things.


### [Exegol](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Exegol is a free and open-source pentesting environment made for professionals. It allows pentesters to conduct their engagements in a fast, effective, secure and flexible way. Exegol is a set of pre-configured and finely tuned docker images that can be used with a user-friendly Python wrapper to deploy dedicated and disposable environments in seconds.


### [Exegol: Professional Hacking Setup](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Exegol is a free and open-source pentesting environment made for professionals. It allows pentesters to conduct their engagements in a fast, effective, secure and flexible way. Exegol is a set of pre-configured and finely tuned docker images that can be used with a user-friendly Python wrapper to deploy dedicated and disposable environments in seconds.


### [Exploitivator: A Tool to Automate Exploitation as Part of the Scanning Process](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Exploitivator is a tool which takes a range of IP addresses and scans for user-specified vulnerabilities, automatically exploiting any verified instances of vulnerable machines with a Metasploit payload. The tool also includes an additional feature to run multiple MSF scans against a range of IP addresses, without a need to repeatedly set up and then run each scan.


### [Faraday: Open Source Vulnerability Manager](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Faraday is a powerful and versatile security tool designed to help cybersecurity professionals perform effective and efficient penetration testing. It is an open-source framework that enables security testers to manage and track their penetration testing activities, from initial reconnaissance to final reporting.

With Faraday, users can integrate multiple tools and methodologies, including vulnerability scanning, exploitation, and post-exploitation techniques. It supports a wide range of tools, such as Metasploit, Nmap, and Burp Suite, and provides a central console to manage all the testing activities.


### [FireDrill: Adversarial Simulation Platform - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
AttackIQ has released a free Community Edition of it's AttackIQ FireDrill Adversarial Simulation Platform. An open platform, where contributors can create attack scenarios, share and discuss those scenarios in the community and test those scenarios using the Community Edition of our platform. All scenarios are written in python and there is an extensive development community with documentation, videos and other community members to support each other in building scenarios that help validate and test defensive technologies, processes, tools and people against Attacker TTPs. The Community edition gives you full access to the development community and scenarios that have been developed by that community. Useful for both red team/blue team exercises as well as truly being able to test, measure and improve your defensive security controls we're proud to be showcasing the AttackIQ Community Edition at Black Hat this year!


### [Foxtrot C2: A Journey of Payload Delivery](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Execution of an offensive payload may begin with a safe delivery of the payload to the endpoint itself. When secure connections in the enterprise are inspected, reliance only on transmission level security may not be enough to accomplish that goal. Foxtrot C2 serves one goal: safe last mile delivery of payloads and commands between the external network and the internal point of presence, traversing intercepting proxies, with the end-to-end application level encryption.

While the idea of end-to-end application encryption is certainly not new, the exact mechanism of Foxtrot's delivery implementation has advantages to Red Teams as it relies on a well known third party site, enjoying elevated ranking and above average domain fronting features. Payload delivery involves several OpSec defenses: sensible protection from direct attribution, active link expiration to evade consistent interception, inspection, tracking and replay activities by the defenders. Asymmetric communication channels are also planned.

And if your standalone Foxtrot agent is caught, the delivery mechanism may live on, you could still manually bring the agent back into the environment via the browser. A concept tool built on these ideas will be presented and released. It will be used as basis for our discussion.


### [FruityDC](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
FruityDC is focused on dynamic callbacks for re-establishing communication with C2 infrastructure and for achieving persistence, how payloads can heal themselves after being blocked including how communication can be re-established via dynamic parametric data. The methods described are code agnostic.


### [Fudge: A Collaborative C2 Framework for Purple Teaming](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Fudge is a Python3/Flask web-based C2 framework and Powershell implant designed to facilitate purple teaming activities, post-campaign review and timelining.

Fudges' inception is based on 3 main areas:

Creating a suitable way for blue teamers to review the chronological activities a red team engagement, allowing them to assess if key alerts were missed.
Finding ways to incrementally increase detection rates, allowing defenders to identify the intrusion. This provides a gauge of skill & target areas for upskilling if the intrusion is not identified.
Providing a way for junior testers to experience red teaming without increasing risk to the campaign OpSec/client network.
Purple teaming was born out of the need for tighter integration between offensive and defensive teams. If the red team is successful in compromise, their ability to export the campaign timeline and logging can prove invaluable insight to the blue team. Allowing defenders to review network and host logs as they follow a campaign timeline, allows for blind spots to be identified and tooling adjusted and tuned.

Fudges' implant also supports varying levels and types of obfuscation to allow for varying levels of noise to be made during the engagement to help a SoC benchmark their detection skills.

Lastly, Fudge is designed around team usage, which allows for a senior red teamer to allow another user to have read or read/write access to the campaign. These access controls allow a junior member to view the campaign and see the kind of commands, and techniques used in a post-exploitation environment.

Fudge can be found on Github at: https://github.com/Ziconius/Fudge


### [FumbleChain: A Purposefully Vulnerable Blockchain](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
FumbleChain is a deliberately insecure blockchain designed to raise awareness about blockchain security. Cryptocurrencies and blockchains are still relatively new, and there have been plenty of news stories about people losing money through compromises in various components making up a blockchain ecosystem. FumbleChain hopes to bridge the awareness gap in a fun way, one in which nobody loses money.

FumbleChain allows people to test their skills attacking the chain and store running on top. The FumbleStore is a CTF in the form of a fake e-commerce web application that offers products you can buy using FumbleCoins, which is the ecosystem's cryptocurrency. Purchasing new products requires players to exploit flaws and steal coins from crypto-wallets. Of course, you could mine coins and use the system legitimately, but where's the fun in that?

The project is written in Python making it easy for anyone to read and modify its source code. It's also modular, making it easy to hack and add new challenges. The entire project is fully dockerized, letting anyone play with FumbleChain in a quick and hassle-free way.


### [GCP Scanner](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Google Cloud Platform (GCP) is a rapidly growing cloud infrastructure with millions of customers worldwide and more than a hundred of various products offered to them. While Cloud offers undeniable benefits in scalability, performance and security, it also opens new and unique challenges for security engineers working with Cloud. One such challenge is credential management.

Cloud credentials such as GCP service account (SA) key can open access to the most critical parts of cloud infrastructure. An incorrectly stored or leaked SA key with such permissions represents high interest for an attacker. Security engineers need to understand the impact of such key leak/compromise to draft a proper security response.

The main objective of GCP Scanner is to offer the community a tool that can be used to evaluate the security impact of a given cloud identity compromise. Security engineers can use this tool to assess the impact of a certain credentials leak, OAuth2 token, potential compromise of a GCP VM or Kubernetes pod.

By now, the only option available was to rely on heavy-weight solutions or time-consuming manual analysis that require privileged access to the affected GCP organization. In contrast, the GCP Scanner works with individual credentials and offers an easy-to-use solution that can be executed from various types of environments with just a single command.

In the demo, we will talk about the scanner architecture and show the audience on how to use the tool in various types of situations (leaked GCP service account key, compromised end-user credentials, VMs and Docker containers, standalone binary from any machine). We will also cover how the scanner can be used to evaluate whether a GCP SA key can be used to impersonate other service accounts and understand potential impact.


### [GDB ENHANCED FEATURES (GEF)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
GEF is a set of commands for GDB, to massively boost the exploit development process on X86, ARM, MIPS, PowerPC and SPARC. GEF aims to be used mostly by exploit development and reverse-engineers, to provide greatly enhanced features to GDB heavily relying on Python API to assist during the process of dynamic analysis and exploit development.


### [GOFETCH](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
GoFetch is a tool to automatically exercise an attack plan generated by the BloodHound application. The tool first loads a path of local admin users and computers generated by BloodHound and convert it to it's own attack plan format. Once the attack plan is ready, it advances towards the destination according to the plan, step by step by successively apply remote code execution techniques and compromising credentials with Mimikatz.


### [GONE IN 59 SECONDS - HIGH SPEED BACKDOOR INJECTION VIA BOOTABLE USB - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Gaining physical access was trivial, but now the computer is locked (or off) and time is running out…the "SmuggleBus" allows us to take advantage of unencrypted drives to quickly collect local password hashes and implant the backdoor of our choice without modifying any system binaries - all from a bootable USB and in a matter of seconds.


### [GR-LORA: AN OPEN-SOURCE SDR IMPLEMENTATION OF THE LORA PHY](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
gr-lora is an open-source GNU Radio/Software Defined Radio implementation of the LoRa radio physical layer, as derived from the author's black box analysis of the protocol. gr-lora empowers developers and security researchers to think beyond packet sniffing and injection by exposing LoRa's physical layer in software.

LoRa is a wireless networking technology that can be thought of as high-endurance cellular for IoT and embedded devices. It utilizes a unique Chirp Spread Spectrum modulation and layered encoding scheme to achieve remarkable range while remaining frugal on power.

PHYs have long been taken for granted, however research such as Travis Goodspeed's packet-in-packet and Dartmouth/River Loop Security's 802.15.4 chipset fingerprinting have demonstrated that physical layer abuse can have severe consequences further up the stack. As a closed protocol, LoRa has only been exposed via layer 2+ interfaces; thus security researchers and developers have lacked the necessary tools to audit and analyze the security and robustness of its PHY.

With its flexible and open architecture, gr-lora gives security researchers the capability required to explore this nascent protocol from its most fundamental layer.


### [Ghost Tunnel: Covert Data Exfiltration Channel to Circumvent Air Gapping - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
In recent years, attacking air gapped networks through HID devices is becoming popular. The HID attack uses the USB interface to forge the user's keystrokes or mouse movement to modify the system settings and run malware. In 2009, NSA's Office of Tailored Access Operations (TAO) developed the COTTON-MOUTH – a USB hardware implant which provides a wireless bridge into a target network as well as the ability to load exploit software onto a target machine. Unlike COTTON-MOUTH, Ghost Tunnel attacks the target through the HID device only to release the payload, and it can be removed after the payload is released.

Advantages:

Covertness
HID attack device is only required to release the payload and it can be removed after that
No interference with the target's existing connection status and communications
Can bypass firewalls
Can be used to attack strictly isolated networks
Communication channel does not depend on the target's existing network connection
Cross-Platform Support
Can be used to attack any device with wireless communication module, we tested this attack on Window 7 up to Windows 10, and OSX

Source Code: https://github.com/360PegasusTeam/GhostTunnel


### [GodPotato: As Long as You Have the ImpersonatePrivilege Permission, Then You are the SYSTEM!](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Based on the history of Potato privilege escalation for 6 years, from the beginning of RottenPotato to the end of JuicyPotatoNG, I discovered a new technology by researching DCOM, which enables privilege escalation in Windows 2012 - Windows 2022, now as long as you have "ImpersonatePrivilege" permission. Then you are "NT AUTHORITY\SYSTEM", usually WEB services and database services have "ImpersonatePrivilege" permissions.



Potato privilege escalation is usually used when we obtain WEB/database privileges. We can elevate a service user with low privileges to "NT AUTHORITY\SYSTEM" privileges.
However, the historical Potato has no way to run on the latest Windows system. When I was researching DCOM, I found a new method that can perform privilege escalation. There are some defects in rpcss when dealing with oxid, and rpcss is a service that must be opened by the system. , so it can run on almost any Windows OS, I named it GodPotato


### [Haaukins: A Highly Accessible and Automated Virtualization Platform for Security Education](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Haaukins is a highly accessible platform for security education, which allows users to try out ethical hacking and penetration testing using Kali Linux through a browser. It makes it possible to conduct trainings for even large groups without the need for installing virtual environments or other tools – the participants can work on their own laptops just through their web browser of choice, and have access within a couple of minutes.

Haaukins allows the teacher/instructor to set up an event using a command line interface specifying e.g. which challenges to include and how many labs are needed. Labs can include different kind of challenges, such as a number of vulnerable machines. The challenges can also include e.g. sniffing network traffic between different machines. Once an event is setup, users/teams can easily register and see the challenges as in any CTF.

What makes Haaukins stand out is that each user is assigned a virtual lab, which is accessed through a Kali Linux accessible through a web browser. After registration, the user just clicks the "connect" button, and he can access the Kali Linux desktop.

Haaukins is designed with training in mind rather than for competition. For this reason a number of features are implemented such as Dynamic Flags, so the teams cannot exchange flags between each other, and a randomization of IP addresses throughout the challenges, so teams really have to work their own way through.

It is easy to contribute with new challenges, since challenges can consist of any set of docker images and VirtualBox OVA's.

During the last year, the platform has been tested out with different target audiences, including OWASP groups, networks of IT professionals, companies, high schools and higher education.


### [HardeningMeter](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
HardeningMeter is an open-source Python tool carefully designed to comprehensively assess the security hardening of binaries and systems. Its robust capabilities include thorough checks of various binary exploitation protection mechanisms, including Stack Canary, RELRO, randomizations (ASLR, PIC, PIE), None Exec Stack, Fortify, ASAN, NX bit. This tool is suitable for all types of binaries and provides accurate information about the hardening status of each binary, identifying those that deserve attention and those with robust security measures.

The genesis of HardeningMeter stems from extensive research into the dynamic cat-and-mouse game between attackers and defenders when exploiting binaries. While certain binary hardening measures are designed to thwart binary exploitation, resourceful attackers continue to find ways to circumvent these protections. HardeningMeter is a wake-up call that raises awareness of the critical need to protect against binary exploitation, monitors vulnerable binaries that lack critical hardening, and promotes a broader understanding of the offensive research landscape.

HardeningMeter's uniqueness lies in its precision, which is based on a deep understanding of binary structures, exploitation techniques, and hardening mechanisms. It supports all binary file types, including executables, dynamic executables, dynamic shared objects, relocatables, and statically linked files.

The tool offers a significant benefit to users, each check that the tool performs is documented in detail to allow users to dive into the inner workings of binary hardening. Users can gain a deeper understanding of the underlying concepts, explore the intricacies of binary exploitation protection mechanisms, and expand their knowledge in this important area. Moreover, users can set the output to receive tailored recommendations on which binary files require heightened attention and monitoring.

We hope to contribute to the cybersecurity community and benefit from their ideas and perceptions to extend our features and make HardeningMeter a better tool that supports systems other than Linux in the future.


### [HazProne](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
HazProne is a Cloud Pentesting Framework that emulates close to Real-World Scenarios by deploying Vulnerable-By-Demand aws resources enabling you to pentest Vulnerabilities within, and hence, gain a better understanding of what could go wrong and why!!


### [HomePwn](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The hyperconnected world is a reality nowadays. Today, we should consider that companies have a considerable number of these devices within their workplaces or offices. With the famous BYOD (Bring Your Own Device) companies are opening an attack vector that can be exposed or increased by the different devices that employees can carry to the office, either on their body, on a keyring, in their backpack or even on their clothes. The many different technologies that can be used are a vector attack for assailants and Red Team members.

The emergence of millions of devices, from different nature, have caused changes in the security applied for each of them. Using several technologies between these devices makes security heterogeneous. Bluetooth Low-Energy, WiFi, NFC are just some examples of the technologies being used by millions of devices around our society. Most of them can be found at home or in our offices. Companies are suffering many attacks that can come through a wrong configuration and can be used by an attacker to gain access to other resources within the company itself. HomePwn is a framework that provides several features for auditing and pentesting on devices connected to the Internet using different technologies such: WiFi, Bluetooth Low-Energy, or NFC, among others.

HomePwn is a framework that provides features to audit and pentesting devices that company employees can use in their day-to-day work and inside the same working environment.


### [Humble Chameleon: Eating 2FA for Breakfast](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
By creating a simple tool that performs a man-in-the-middle attack against the HTTP protocol, we can eliminate the need to manually create phishing sites. In addition, this same tool can be used to harvest session cookies from applications that require 2FA, disallow victims from logging out and killing our stolen cookies, hide phishing domains behind legitimate content, categorize phishing domains, serve malware alongside legitimate content, only serve payloads in response to whitelisted requests, and target multiple services at the same time, all without SSL warnings. *Note: This is not just a tool, but a release of a new attack methodology.


### [InQL: Introspection GraphQL Scanner](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
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


### [Interactive Kubernetes Security Learning Playground - Kubernetes Goat](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Kubernetes Goat is an interactive Kubernetes security learning playground. It has intentionally vulnerable by design scenarios to showcase the common misconfigurations, real-world vulnerabilities, and security issues in Kubernetes clusters, containers, and cloud native environments.

It's tough to learn and understand Kubernetes security safely, practically, and efficiently. So here we come to solve this problem not only for security researchers but also to showcase how we can leverage it for attackers, defenders, developers, DevOps teams, and anyone interested in learning Kubernetes security. We are also helping products & vendors to showcase their product or tool's effectiveness by using these playground scenarios and also help them to use this to educate their customers and organizations. This project is a place to share knowledge with the community in well-documented quality content in hands-on scenario approaches.


### [Introducing subCrawl: A Framework for the Analysis and Clustering of Hacking Tools Found Using Open Directories](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
From phishing kits to command-and-control panels, web shells and multiple samples of malware, open directories can provide a wealth of information into threat actor operations. But how can we discover open directories? And once we discover them, what are the next steps for identifying interesting content?

To answer these questions, we created the open-source framework subCrawl. subCrawl is written in Python3 and provides a modular framework for discovering open directories, unique content through signatures and organizing the data with optional output modules, such as MISP.

Open directories are simply folders that are viewable on a public web server that provides direct links to all its content. While open directories can be used to legitimately share files, they are often overlooked by threat actors. Therefore, they can provide insight into the structure, tools and malware being used by many threat actors. This oversight can provide direct access to the tools they've placed on a server, such as web shells, C2 panels or proxy scripts.

To organize the data, we use our framework subCrawl to aggregate the data with fuzzy hashes, web server information, used scripting languages and more. This approach allows for the creation of signatures that can be used to track tool usage across multiple hosts and cluster threat actor activities. To help manage the hosts explored and the data collected, we create consolidated MISP events, which enables us to cluster the found artifacts and draw interesting conclusions about the use of tools.

We will present the open-source framework subCrawl, which reflects our approach for hunting open directories. We will also explore our methodology to detect and cluster malicious content using publicly available threat feeds with the support of the well-known tool MISP, which helps us to store the data in a structured form and cluster it.


### [Invoke-AntiVM: A Powershell Module for VM Evasion](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Recently, attackers have been using living off the land tools such as Powershell and the community has developed a large arsenal based on it such as - just to mention a few - PowerSploit, Invoke-Mimikatz, Powerup, Nishang,Powershell Empire, Invoke-Obfuscation and recently Covenant.

With so many options available to attackers Windows has introduced advanced Powershell logging capabilities and the AMSI interface.

This is not enough however because the attackers have started to use VM detections within their payload to thwart analysis, one needs to remember that powershell script logging only de-obfuscate the functions that have been executed.

Therefore we wrote a powershell module with a set of functions that an attacker or a pentester can import in their powershell implant to decide whether the target is a sandbox VM or possibly a real target. In addition to the techniques used in Nishang (Check-VM) which are mostly based on signatures of specific registry keys and process names, we have used a more general – and behavioral – approach which includes all the information from the OS including for example how many programs are installed, what screenshot is used, what network cards are installed, what is the history usage of certain applications such as explorer or word etc. etc.

We have also added a fingerprinting module which can be included into a word document for example that once is run collects key metrics from the running OS and reports them into a pastebin account or gmail account, after being compressed and encrypted. Once on pastsebin the attacker can download the exfiltrated profile via a python script and decode for further analysis. We are also building a simple machine learning module that given enough data points is able to infer the decision boundary to determine if a host is a VM or not in addition or in replacement of setting manual thresholds.

This is a pretty powerful recon technique for red-team pentesting because in most cases the sandbox will execute the incoming attached documents (if they contain macros for example) thus allowing the exfiltration of the VM data. This can then be used to tweak the payload to avoid the specific sandbox solution and to make sure the malicious payload is run into a real target.

We developed this tool to increase awareness of recent techniques for the reverser community. It includes a full readme that explains how can be just in conjunction with Invoke-Obfuscation, Invoke-Cradle and the MaliciousMacroGenerator. We are also periodically running the fingerprinting service to provide profiles for popular online services such as HybridAnalysis, AnyRun, CuckooSandbox as well desktop solutions such as Qemu, VirtualBox, and VMWare.


### [Invoke-DNSteal: Exfiltrating DNS information "Like a Boss"](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [JACKIT](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
JackIt is a wireless HID injection attack into NRF-based keyboard/mouse dongles based off the MouseJack vulnerability. It has a strong focus on providing system admins with the tools to demonstrate the attack to help promote and justify the need to move away from wireless keyboard and mice in a corporate environment.


### [JavaScript Obfuscation - It's All About the P-a-c-k-e-r-s](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The usage of JavaScript obfuscation techniques have become prevalent in today's threats, from phishing pages, to Magecart, and supply chain injection to JavaScript malware droppers all use JavaScript obfuscation techniques on some level.

The usage of JavaScript obfuscation enables evasion from detection engines and poses a challenge to security professionals, as it hinders them from getting quick answers on the functionality of the examined source code.

Deobfuscation can be technically challenging (sometimes), risky (if you don't know what you are doing), and time consuming (if you are lazy, as I am). Yet, the need to find and analyze high scaled massive attacks using JavaScript obfuscation is a task I'm faced with on a daily basis.

In this arsenal showcase I will present a lazy, performance cost effective approach, focusing on the detection of JavaScript packer templates. Once combined with threat intelligence heuristics, this approach can predict the maliciousness level of JavaScript with high probability of accuracy.

In addition, the showcase will include insights based on detections of the tool that were collected from the threat landscape, including some of the challenges associated with benign websites using obfuscation.

The showcase will also suggest techniques showing how the tool obfuscation detection can also be combined with other threat intelligence signals and heuristics, that can lead to better classification of detect obfuscated code as being malicious.


### [KernelGoat](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
"KernelGoat is a 'Vulnerable by Design' Linux kernel environment to learn and practice Kernel security issues"


### [Koadic: Two Years of Mischief](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Koadic is a post-exploitation toolkit that leverages the Windows Script Host, delivering all the features expected from a modern RAT via VBScript/JScript. Koadic was first released at DEF CON in 2017, and has since seen two years of development. Koadic is robust enough to have been chosen in nation-state cyberespionage campaigns by APT favorites such as Fancy Bear, Stone Panda, and MuddyWater. It has been the tool of choice on the road to domain admin for many pentests, especially in environments where PowerShell and filesystems are heavily audited by antivirus.

New payloads have been added since release, such as Squiblytwo WMIC.exe XSL files (discovered by SubTee and Mattifestation) and Bitsadmin.exe transfer jobs. Existing payloads have been upgraded to include obfuscation and antivirus evasion.

Several new implants have been added, including UAC bypasses via slui, fodhelper, compmgmtlauncher, and compdefaults. A loot finder module automates the process of finding files which may contain sensitive data. Persistence is now available via registry autoruns, WMI, and scheduled tasks. "One shot" stagers now allow an implant to be run immediately on a zombies first call home.

A new credential storage feature has been added, transforming Mimikatz outputs acquired into a readily searchable format. A full fledged API is also available, allowing all available functionality of the toolkit to be automated through HTTP interactions. There are innumerable bug fixes, improvements to reliability, and additional stealth since the initial release, with new features being added regularly.


### [Konstellation: RBACpacking in Kubernetes](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Konstellation is a new open-source tool that simplifies Kubernetes role-based access control (RBAC) data collection and security analysis. Kubernetes RBAC is a powerful tool to manage access to resources, but its complexity increases exponentially as principals and resources grow, making it challenging to analyze the resulting data at scale. Konstellation uses graph theory to map and analyze all Kubernetes resources and RBAC permissions, which simplifies analysis of RBAC implementations for security vulnerabilities.

Konstellation allows engineers to understand what actions principals are allowed to perform on resources, analyze complex relationships not visible in native Kubernetes or other tools, and find overprovisioning and privilege escalation paths. Additionally, Konstellation is configuration-driven, allowing for quick adaptation to different environments, configurations, and analysis needs.

The tool features three primary modes: enumeration, data ingestion, and querying. The enumeration mode connects directly to a Kubernetes cluster, enumerates each resource type returned by the API server, and writes the results to files in JSON format. Alternatively, Konstellation can ingest kubectl JSON output.

Konstellation is schema-less and uses structured output from enumeration to determine data structures. Every resource instance and its attributes map into a Neo4j node with node properties. Users can query all enumerated resource data from the schema without data loss. After ingesting the resource instances, Konstellation maps relationships using Neo4j cypher queries defined in its configuration.

Query mode allows for rapid data analysis. Konstellation ships with 40+ queries that look for privilege escalation paths and known vulnerable configurations. Users also can perform ad-hoc queries through command line or directly in Neo4j.

Analyzing Kubernetes RBAC weaknesses at scale can be daunting, but Konstellation offers a clear overview of RBAC implementations and simplifies the process of identifying security vulnerabilities.


### [Kube-Hunter: Pentest Platform for Kubernetes Environments](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Kubernetes is today's most popular container orchestrator. But it's also a complex distributed system, with defaults tuned for usability rather than for security. More so, configuring Kubernetes correctly is not trivial. Failing to configure Kubernetes in a secure way exposes the applications running on it to imminent risk, regardless of how securely those application are built.

We recognized the need to assess the level of security of a Kubernetes cluster deployment, and built kube-hunter to be an extensible pentesting and risk assessment platform for Kubernetes environments. We contributed quite a few discovery and hunt techniques from the get-go, and will add more over time. Kube-hunter is also designed to be easily extended by the community. The full list is too long for 300 words and ever-growing. This is the list of newest tests:
Newest Passive Tests (tests not making any change to the cluster):
● Vulnerabilities hunter (added CVEs):
○ CVE-2019-9512
○ CVE-2019-9514
○ CVE-2019-11247
○ CVE-2019-11246
○ CVE-2019-1002101
● Hunt pods that have write access to host's /var/log. Potentially allows an attacker to read files on the host machine
● Checks for default enabled capabilities in a pod

Newest Active Tests (may perform state-changing actions on the cluster):
● Checks for the possibility of running an ARP spoof attack from within a pod
● Checks for the possibility for a malicious pod to compromise DNS requests of the cluster


### [Kubesploit: A Post-Exploitation Framework, Focused on Containerized Environments](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Kubestriker: A Blazing Fast Kubernetes Security Auditing Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Kubestriker performs numerous in depth checks on kubernetes infrastructure to identify any misconfigurations which make organisations an easy target for attackers and safeguards against potential attacks on Kubernetes clusters.


### [Kubestriker: A Blazing Fast Security Auditing Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Kubestriker performs numerous in depth checks on kubernetes infrastructure to identify any misconfigurations which make organisations an easy target for attackers and safeguards against potential attacks on Kubernetes clusters.


### [LEGION - SIMPLE DISTRIBUTED COMPUTING FOR THE MASSES AND PENTESTERS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
At its core, Legion is a distributed computing application. It is written in python and designed from the ground up to fulfill various IT related needs. Whether you need a way to logically distribute large or complex commands across multiple systems, or if you need a way to remotely administer 1 or more other systems, Legion can help. Legion goes beyond a typical Master/Manager/Slave architecture and makes use of a MeshNetworking approach to help to dynamically route around failed nodes and networking issues. Additionally, it has the ability to allow remote shell access to any node as well as send individual commands to 1 or all of the nodes within the mesh. And of course all the communications are encrypted between the nodes. If you want to learn more or just want to see the demo, please stop by.


### [LEVIATHAN FRAMEWORK](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Leviathan is a mass audit toolkit which has wide range service discovery, brute force, SQL injection detection and running custom exploit capabilities. It consists open source tools such masscan, ncrack, dsss and gives you the flexibility of using them with a combination. The main goal of this project is auditing as many system as possible in country-wide or in a wide IP range.

Main Features:

Discovery: Discover FTP, SSH, Telnet, RDP, MYSQL services running inside a specific country or in an IP range via Shodan, Censys. It's also possible to manually discover running services on a IP range by integrated "masscan" tool.
Brute Force: You can brute force the discovered services with integrated "ncrack" tool. It has wordlists which includes most popular combinations and default passwords for specific services.
Remote Command Execution: You can run system commands remotely on compromised devices.
SQL Injection Scanner: Discover SQL injection vulnerabilities on websites with specific country extension or with your custom Google Dork.
Exploit Specific Vulnerabilities: Discover vulnerable targets with Shodan, Censys or masscan and mass exploit them by providing your own exploit or using pre-included exploits.


### [Lauschgerät: Gets in the Way of your Victim's Traffic and Out of Yours](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Lauschgerät gets in the way of your victim and out of yours. This python tool acts as a convenient man-in-the-middle tool to sniff traffic, terminate TLS encryption, host malicious services and bypass 802.1X - provided you have physical access to the victim machine, or at least its network cable.

There are three ways to run it: Either on its own dedicated device like a Raspberry Pi or Banana Pi, in a virtual machine with two physical USB-NICs attached, or on your regular pentest system in its own network namespace. It will look like a completely transparent piece of wire to both victim systems you are getting in the middle of, even if they are using 802.1X because it is implementing the ideas presented in a talk by Alva Lease 'Skip' Duckwall IV.

The Lauschgerät operates with three interfaces: Two interfaces going to the victim client and the victim switch respectively, and one management interface which you can connect to and initiate the redirection of traffic, inject your own traffic, start and stop malicious services, and so forth. It comes with a few services included, such as a service that terminates TLS encryption (which will of course cause a certificate warning on the victim's end) or a service that performs the classic "SSL strip" attack. And more to come!

An optional wireless interfaces can either be used as another management interface or for intercepting traffic of wireless devices. The management can be done via SSH or via a web application, making sure you can hit the ground running.


### [Lazyrecon v2.0](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Lazyrecon v2.0 is a subdomain discovery tool that discovers and resolves valid subdomains then performs SSRF/LFI/SQLi fuzzing and port scanning. It has a simple modular architecture and is optimized for speed while working with github and wayback machine.


### [LinkTap: New Threats are Already Around You - The IPV6 Attack Must be Understood](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Due to the exhaustion of IPv4 free address space, the use of IPv6 on the Internet is gradually increasing. All Windows operating systems since Windows Vista have IPv6 enabled by default. IPv6 brings a series of improvements compared to IPV4, but these improvements are also put a double-edged sword.

Recently, we have been focusing on "IPv6" attack research and found that in the IPV6 environment, there are many attack points, such as Iptables will fail, use IPV6 to bypass the Web defense strategy and abuse IPV6-specific protocols for man-in-the-middle attacks, and Other attack ideas!

In this presentation, I will disclose the attack methods and ideas I have found for IPV6, and will also release tools for IPV6 attacks.


### [MAILSNIPER](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Oftentimes, on penetration tests we find ourselves having elevated access (Domain Admin) within an organization. One of the best ways to demonstrate risk to an organization is to show the ability to gain access to sensitive data. Email is often the primary messaging system inside most organizations and is the go-to medium for simple chit-chat about daily business, password resets, or even corporate strategy.

MailSniper is a PowerShell-based penetration testing tool whose primary purpose is to search through email in a Microsoft Exchange environment for specific terms (i.e. passwords, insider intel, network architecture information, etc.). It can be used as a non-administrative user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain.

MailSniper includes additional modules for attacking externally-facing Outlook Web Access (OWA) and Exchange Web Services (EWS) portals. With MailSniper, it is also possible to: perform password spraying attacks, enumerate internal domain names and usernames, locate inboxes with too broad permissions, and gather the Global Address List containing all email addresses of users at an organization from OWA and EWS.


### [MUSHIKAGO-femto: Automated Pentest & First Aid Tool for IT/OT Environments](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
At the Black Hat USA 2021 Arsenal, we presented MUSHIKAGO, an automated penetration testing tool for both IT and OT. MUSHIKAGO can automatically perform penetration tests and post-exploitation in various environments without prior learning.

This time, we have newly evolved MUSHIKAGO as MUSHIKAGO-femto, incorporating cutting-edge features. The evolution includes the implementation of a mechanism to perform first aid on the tested system and acquire immune functions so that the same attack can be defended against attacks that could be achieved by penetration tests. A function was implemented to defend against vulnerability attacks by applying patches, injecting FW functions or proprietary IPS into terminals. Specifically, taking advantage of the fact that the penetration test was able to penetrate the system, patches are applied as if injecting a vaccine at the penetrated terminal, or a unique thin IPS is incorporated. This allows the system to be defended before the actual attacker can exploit the vulnerability or misconfiguration. Based on these results, MUSHIKAGO-femto has become the Next-Generation Pentest Tool that strengthens system defenses while performing penetration testing.

Other additional features include the implementation of a scan function to detect ICS protocols in order to detect ICS devices with high accuracy. MUSHIKAGO-femto has both Active Scan and Passive Scan functions, enabling comprehensive detection of PLCs and ICS devices. This enables automatic penetration of OT system. This makes it possible to perform automatic penetration tests on OT system with high accuracy. In the demo, we will show how it can perform automatic penetration testing and automatic protection against Hack THe Box and VulnHub machines. We will also show that it is possible to perform effective penetration testing in our OT/ICS environment.


### [MacAttack - A Client/Server Framework with Macro Payloads for Domain Recon and Initial Access](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
While using macros for malicious purposes is nothing new, this tool provides a suite of payloads ideal for initial recon and footholds that will not burn other methods of attack. MacAttack is a framework that generates payloads for use in Excel and includes client/server communication to perform dynamic alterations at runtime and collate received data.
The payloads included in MacAttack cover a number of areas that have not been published before, including a new stealth technique for hiding payloads, methods for retrieving a user's hash, and performing common recon/early stages attacks such as As-Rep roasting, retrieving documents, browser credentials, password spraying the domain, enumerating users, and domain fronting. The client/server communication and GUI will allow for dynamic checks such as only allowing a password spray to run once or once within a certain time period even if multiple targets enable the payload at the same time, and will provide a visual representation of the enumerated information. Part of the benefit of this tool is that this information is retrievable from a "zero foothold" position - a phishing campaign may be detected or blocked - but this does not burn any existing beacons and the potential rewards can be as great as multiple sets of credentials for users and relevant authentication portals. Microsoft are rolling out changes to macros that have still not been fully deployed by the time of the deadline - and research into these changes and impacts will be included in the discussion. It looks like these changes will only affect O365 to begin with and will include a "recommended policy" to implement.


### [Malicious NFTs](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Web3 stands as a dynamic technology harboring significant potential for diverse business opportunities and applications. As web3's technological landscape continues to evolve, malicious actors are similarly driven to explore novel and innovative methods to exploit these technologies. A notable example of such exploitative endeavors involves the realm of Malicious NFTs.


### [Mallet: An Intercepting Proxy for Arbitrary Protocols](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
This prsentation will focus on a new open-source intercepting proxy named Mallet, based on the mature and high-performance Netty framework, that wraps it with a drag and drop graph-based graphical user interface and a datastore. In doing so, we gain access to an existing library of protocol implementations, including TLS (and SNI), various compression algorithms, HTTP, HTTP/2, MQTT, REDIS, and many others, and most important, an existing community of developers creating new protocol decoders and encoders, and the associated body of knowledge in this area.

The Mallet user interface closely follows the Netty model, making it simple to construct a pipeline of encoders and decoders by dragging existing codecs, or adding your own codecs or script blocks to a palette, taking the researcher from a simple TCP intercept-and-forward proxy, to a full-blown protocol stack with scriptable processing, with every change being recorded for review and replay in a subsequent connection. As Netty supports a variety of transports, from the common TCP and UDP to SCTP, Serial Port and File, as well as native kqueue and epoll transports, Mallet can be used to intercept all sorts of data, however you may find it.

Source Code: https://github.com/SensePost/Mallet


### [Merlin](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Mobile Security Framework - MobSF](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Mobile Security Framework - MobSF is an automated mobile application security testing environment designed to help security engineers, researchers, developers, and penetration testers to identify security vulnerabilities, malicious behaviors and privacy concerns in mobile applications using static and dynamic analysis. It supports all the popular mobile application binaries and source code formats built for Android and iOS devices. In addition to automated security assessment, it also offers an interactive testing environment to build and execute scenario based test/fuzz cases against the application.

Visit our Arsenal station to witness:

* Brand new MobSF iOS Dynamic Analyzer
* Live Pentest of Android/iOS apps
* Solving Mobile app CTF challenges
* Reverse engineering and runtime analysis of Mobile malware
* How to shift left and integrate MobSF/mobsfscan in your build pipeline


### [Modern Active Directory Attacks with the Metasploit Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Active Directory is the foundation of the infrastructure for many organizations. As of 2023, Metasploit has added a wide range of new capabilities and attack workflows to support Active Directory exploitation. This Arsenal demonstration will cover new ways to enumerate information from LDAP, attacking Active Directory Certificate Services (AD CS), leveraging Role Based Constrained Delegation, and using Kerberos authentication.

The Kerberos features added in Metasploit 6.3 will be a focal point. The audience will learn how to execute multiple attack techniques, including Pass-The-Ticket (PTT), forging Golden/Silver Tickets, and authenticating with AD CS certificates. Finally, users will see how these attack primitives can be combined within Metasploit to streamline attack workflows with integrated ticket management. The demonstration will also highlight inspection capabilities that are useful for decrypting traffic and tickets for debugging and research purposes.


### [Mr.SIP: SIP-Based Audit & Attack Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Mr.SIP is a simple console based SIP-based Audit and Attack Tool. Originally it was developed to be used in academic work to help developing novel SIP-based DDoS attacks and then as an idea to convert it to a fully functional SIP-based penetration testing tool.

Initially, it was developed to be used in academic researches to help developing novel SIP-based DDoS attacks and then as an idea to convert it to a fully functional SIP-based penetration testing tool. So far it has been used more than 5 journal papers. Mr.SIP can also be used as SIP client simulator and SIP traffic generator.

The initial academic journal paper which Mr.SIP is used is titled "Novel SIP-based DDoS Attacks and Effective Defense Strategies" published in Computers & Security 63 (2016) 29-44 by Elsevier, Science Direct http://sciencedirect.com/science/article/pii/S0167404816300980.

In the current state, Mr.SIP comprises 7 sub-modules named as SIP-NES (network scanner), SIP-ENUM (enumerator), SIP-DAS (DoS attack simulator), SIP-ASP (attack scenario player), SIP-EVA (eavesdropper), SIP-SIM (signaling manipulator) and SIP-CRACK (cracker). Since it provides a modular structure to developers, more modules will continue be added by the authors and it is open to be contributed by the open-source developer community.

SIP-NES is a network scanner. It needs the IP range or IP subnet information as input. It sends SIP OPTIONS message to each IP addresses in the subnet/range and according to the responses, it provides the output of the potential SIP clients and servers on that subnet.

SIP-ENUM is a enumerator. It needs the output of SIP-NES and also pre-defined SIP usernames. It generates SIP REGISTER messages and sends them to all SIP components and try to find the valid SIP users on the target network. You can write the output in a file.

SIP-DAS is a DoS/DDoS attack simulator. It comprises four components: powerful spoofed IP address generator, SIP message generator, message sender and response parser. It needs the outputs of SIP-NES and SIP-ENUM along with some pre-defined files.

IP spoofing generator has 3 different options for spoofed IP address generation, i.e., manual, random and by selecting spoofed IP address from subnet. IP addresses could be specified manually or generated randomly. Furthermore, in order to bypass URPF filtering, which is used to block IP addresses that do not belong to the subnet from passing onto the Internet, we designed a spoofed IP address generation module. Spoofed IP generation module calculated the subnet used and randomly generated spoofed IP addresses that appeared to come from within the subnet.

SIP-DAS basically generates legitimate SIP INVITE message and sends it to the target SIP component via TCP or UDP. In the current state it doesn't support instrumentation which helps you to understand the impact of the attack by using Mr.SIP, but we will support it very soon. In the current state, we can see the impact of the attack by checking the CPU and memory usage of the victim SIP server.

SIP is a text based protocol such as HTTP but more complex than HTTP. For example, when we talk about SIP INVITE message, there are some specific headers and parameters need to be vendor specific and unique for each call. SIP Message Generator allows you to bypass security perimeters bu generating all these headers and parameters as it should be, so basic it is harder to be detected by anomaly detection engines that these messages are generated automatically. You can generate SIP methods such as INVITE message, REGISTER message etc.

You can specify the message count, the destination port, you can use predefined toUser list, fromUser list, userAgent list etc.

In order to bypass automatic message generation detection (anomaly detection) systems, random "INVITE" messages are generated that contained no patterns within the messages. Each generated "INVITE" message is grammatically compatible with SIP RFCs and acceptable to all of the SIP components.

"INVITE" message production mechanism specifies the target user(s) in the "To" header of the message. This attack can be executed against a single user or against legitimate SIP users on the target SIP server as an intermediary step before the DoS attack. The legitimate SIP users are enumerated and written to a file. Next, they are placed randomly in the "To" header of the generated "INVITE" messages. "Via, "User-Agent, "From," and "Contact" headers within an "INVITE" message were syntactically generated using randomly selected information from the valid user agent and IP address lists. The tag parameter in the "From" header, the branch and source-port parameters in the "Via" header, and the values in the "Call-ID" header are syntactically and randomly generated using the valid user agent list. In addition, the source IP addresses in the "Contact" and "Via" headers are also generated using IP spoofing.

UDP is used widely in SIP systems as a transport protocol, so attacks on the target server are implemented by sending the generated attack messages in the network using UDP. Also TCP can be used optionally. The message sender of SIP-DAS allows the optional selection of how many SIP messages could be sent during one second. The number of SIP messages sent in one second depended on the resources (CPU and RAM) of the attacker machine.

SIP-ASP is Attack Scenario Player. It is working like a sub function of SIP-DAS. It has a powerful parser and allows you to create stateful SIP attack call flows. In our academic studies, we have developed new attack vectors by using our SIP-DAS and SIP-ASP such as re-transmission based DDoS attacks and reflection based DRDoS attacks.

SIP-EVA is an eavesdropper. It sniffs the target network and can grasp the SIP messages. It allows you to extract call specific information such as who is calling, who i called, the duration of the call, the unique call-ID value and you can even download the media content of the call.

SIP-SIM is a signaling manipulator. It is working like Intercepting SIP Proxy. It uses the same sniffer mechanism with SIP-EVA but it allows you to catch the messages between clients and server and you can replicate the messages and manipulate some headers and/or parameters as you want and send it to the victim server.

By using SIP-SIM you can do do Caller-ID spoofing attacks. SIP-SIM support both LAN-based and WAN-based Caller-ID spoofing attacks. But in order to make WAN-based Caller-ID spoofing attack, you need to have proper service provider account.

SIP-CRACK is a password cracker. Again, it uses the same sniffing mechanism and it allows you to catch the SIP REGISTER messages, extract the authentication data such as hash values. You can do brute-force based cracking, or you can choose dictionary or rainbow table cracking. So SIP is a time critical protocol and cracking should be an offline attack.


### [Mr.SIP: SIP-Based Audit and Attack Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Mr.SIP Pro is a comprehensive attack-oriented VoIP product developed to simulate VoIP-based attacks and audit VoIP networks and applications from a security perspective. Originally it was developed to be used in academic work to support developing novel SIP-based attacks and then as an idea to convert it to a fully functional SIP-based penetration testing tool. So far Mr.SIP resulted in several academic research papers and journal articles and won first prizes in various cyber security competitions. Mr.SIP can also be used as a SIP client simulator and SIP traffic generator.

Mr.SIP Pro detects SIP components and existing users on the network, intercepts, filters, and manages call information, reports known vulnerabilities and exploits, develops various TDoS attacks, and cracks user passwords. It has many innovative and competitive features such as high-performance multi-threading, IP spoofing, intelligent SIP message generation, self-hiding, and interception capabilities. Mr.SIP also has a customizable scenario development framework for stateful attacks.

In the current state, the public version of Mr.SIP contains 3 modules; SIP-NES (network scanner), SIP-ENUM (enumerator), and SIP-DAS (DoS attack simulator). The Pro version includes 19 modules in 4 categories; Information Gathering, Vulnerability Scanning, Offensive, and Utility modules as listed below.

Information Gathering Modules: SIP-NES (network scanner), SIP-ENUM (SIP enumerator), SIP-SNIFF (SIP traffic sniffer), SIP-EAVES (call eavesdropper)

Vulnerability Scanning Modules: SIP-VSCAN (vulnerability & exploit scanner), Auto-Deep (automated scanner)

Offensive Modules: SIP-DAS (DoS attack simulator), SIP-MITM (man in the middle attacker), SIP-ASP (attack scenario player), SIP-CRACK (digest authentication cracker), SIP-SIM (signaling manipulator), SIP-FUZZ (protocol fuzzer), RTP-EAVES (media sniffer), RTP-MIM (media manipulator), RTP-Robo (robocall/SPIT attacker), RTP-DTMF (DTMF stealer)
Utility Modules: IP Spoofing Engine, Message Generator, GUI


### [Mr.SIP: The Ultimate SIP-Based Penetration Testing Tool for VoIP Systems](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Mr.SIP is a cutting-edge penetration testing tool designed specifically for VoIP systems. It is the most advanced and comprehensive offensive security tool available in the market for VoIP systems. Developed to assist security experts and system administrators in assessing the security of their VoIP systems and evaluating potential risks, Mr.SIP Pro offers a wide range of features to aid in this process.

Mr.SIP Pro enables users to discover VoIP servers and active users on the network, intercept and manipulate call data, crack user passwords, and identify and report on security vulnerabilities, exploits, and misconfigurations. It also provides a framework for creating advanced, stateful attack scenarios, such as stateful TDoS (Telephony Denial of Service) attacks. Additionally, it allows users to test the server's protocol stack for undiscovered zero-day vulnerabilities by sending irregular messages. With Mr.SIP Pro, security experts and system administrators can have complete visibility and control over their VoIP systems, enabling them to proactively identify and mitigate potential threats.


### [Mushikago: IT and OT Automation Penetration Tool Using Game AI](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Penetration testing is an effective means of discovering vulnerabilities and inadequate settings in the overall system, and of investigating whether there are any operational security risks. However, in manual penetration testing, there are many cases where it is unclear whether the test content is really appropriate, because the diagnosis varies depending on the tester's strong and weak, interests, physical condition, and mental state on that day. Also, excellent testers are already booked by a large amount of work, and it is not always possible to request them without fail. In addition, cyber attacks on ICS (Industrial Control System) have been increasing recently, especially in 2020, when there were many cases of ransomware infections that caused damage to ICS. Furthermore, the number of reports of ICS vulnerabilities is increasing every year. In response to this situation, penetration testing for ICS has been attracting much attention.

In this work, we developed Mushikago, an automatic penetration testing tool using game AI, which focuses on the verification of post-exploit among penetration tools. A post-exploit is an attack that an attacker carries out after entering the target environment. By focusing on post-exploit verification, we can understand how far an attacker can actually penetrate and what kind of information is collected. Mushikago uses the GOAP (Goal Oriented Action Planning), which is game AI commonly used in NPC (Non Player Character). To using Mushikago, we can flexibly change the content of the attack according to the environment and mimic the attacks conducted by actual APT attackers and testers. It is also possible to identify terminal information, account information, and network information without manual intervention, and visualize and report them based on MITRE ATT&CK. In addition, Mushikago supports ICS, and can be used for penetration testing across IT and OT (Operation Technology).


### [Mística: Anything is a tunnel if you're brave enough - Covert channels for everyone!](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
From exposing internal network ports in restricted environments to the internet to controlling a meterpreter implant via DNS, everything is possible with protocol encapsulation.

To prove this, we have developed Mística, a tool that allows us to finely tune how we want to create a tunnel over protocols like HTTP, DNS and more, and combine this encapsulation with custom applicatrions like io, shell or port redirection.

Mística allows to embed data into other protocol fields, with the goal of establishing a bi-directional channel for arbitrary communications. Mística has a modular design, built around a custom transport protocol, called SOTP (Simple Overlay Transport Protocol). Data is encrypted, chunked and put into SOTP packets. SOTP packets are encoded and embedded into the desired field of the application protocol, and sent to the other end.

During this talk, we will talk about how to quickly design and create covert channels over different protocols and for different purposes. This is both useful for red teams that need new ways to hide their traffic and blue teams that want to easily test their monitoring capabilities.

We will do several demos, where we showcase how encapsulation works and how we can end up tunneling a RAT (meterpreter, in this case) connection over DNS. We will also showcase how to expose any port over the desired covert channel to combine it with tools like Evil-WinRM, for instance.

Mística is available at https://github.com/IncideDigital/Mistica under the GPLv3 license


### [Nebula: A Case Study in Penetrating Something as Soft as a Cloud](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Nebula is a cloud C2 Framework, which at the moment offers reconnaissance, enumeration, exploitation, post exploitation on AWS, but still working to allow testing other Cloud Providers and DevOps Components.
It started as a project to unify all Cloud + DevOps Pentest and Security Techniques for a better assessment of the Infrastructures. It is build with modules for each provider and each functionality. As of April 2021, it only covers AWS, but is currently an ongoing project and hopefully will continue to grow to test GCP, Azure, Kubernetes, Docker, or automation engines like Ansible, Terraform, Chef, etc.


### [NetRipper: Smart Traffic Sniffing for PenetrationTesters](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
NetRipper is a post-exploitation tool targeting Windows systems which uses API hooking in order to intercept network traffic. It also uses encryption-related functions from a low privileged user, making it able to capture both plain-text traffic and encrypted traffic before encryption/after decryption.


### [NovAttack](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The NovAttack platform requires minimal setup time and few resources to implement. We love open source. So NovAttack is open source, it will remain open source.

NovAttack simulates real cyber attacks, focusing on the following attack categories.

Features / Test Capabilities

- IPS / IDS / Firewall
- Malware Download
- Content Filtering
- DLP (Data Loss Protection)
- WAF (Web Application Firewall) (New)

How does NovAttack work?

NovAttack advocates the open source philosophy. Uses the capabilities of PHP and libraries. All communication is prepared with API.

NovAttack simulates cyber attacks with its point-to-point connection. Thus, it reduces the amount of false positive. Attack vectors in it can be edited and updated.

- NovAttack simulates web-based attacks.
- You can provide continuous cyber attack simulation by adding current malware to NovAttack.
- You can develop DLP vectors specific to your organization, such as credit card leak). NovAttack provides continuous analysis for you.
- You can test your institution's content or URL filter.


### [NovAttack: Cyber Attack Simulation for Perimeter Security](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The NovAttack platform requires minimal setup time and few resources to implement. We love open source. So NovAttack is open source, it will remain open source.

NovAttack simulates real cyber attacks, focusing on the following attack categories.

### Features / Test Capabilities

- IPS / IDS / Firewall
- Malware Download
- Content Filtering
- DLP (Data Loss Protection)
- WAF (Web Application Firewall) / Roadmap

### How does NovAttack work?

NovAttack advocates the open source philosophy. Uses the capabilities of python and libraries. All communication is prepared with API.

NovAttack simulates cyber attacks with its point-to-point connection. Thus, it reduces the amount of false positive. Attack vectors in it can be edited and updated.

- You can provide continuous cyber attack simulation by adding current malware to NovAttack.
- You can develop DLP vectors specific to your organization, such as credit card leak). NovAttack provides continuous analysis for you.
- You can test your institution's content or URL filter.


### [OMLASP - Open Machine Learning Application Security Project](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Generally, when deploying applications that use Machine Learning or Deep Learning algorithms, only security audits check for common vulnerabilities. However, these algorithms are also exposed to other vulnerabilities or weaknesses that attackers could exploit. A framework, called OMLASP - Open Machine Learning Application Security Project, is being developed to gather a list of attack and mitigation techniques for these algorithms. This Framework aims to become a standard for auditing Machine Learning algorithms and has been divided into the following two sections:

• Security: the attack surface and attack scenarios will be defined and the capabilities and goals of the attackers. The different attack and defense techniques will be described in-depth to define a methodology to perform an audit of these algorithms.

• Biases: the reasons, types, and solutions will be explained in detail to define a methodology to minimize them. This part is still under development.


### [OWASP Nettacker (Updated - More in-depth Demo)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Nettacker project was created to automate for information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and information. This software is able to use SYN, ACK, TCP, ICMP and many other protocols to detect and bypass the Firewalls/IDS/IPS and devices. By using a unique solution in Nettacker to find protected services such as SCADA, we could make a point to be one of the bests of scanners.


### [OWASP Nettacker: Automated Penetration Testing Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
OWASP Nettacker project is created to automate information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and other information. This software will utilize TCP SYN, ACK, ICMP and many other protocols in order to detect and bypass Firewall/IDS/IPS devices. By leveraging a unique method in OWASP Nettacker for discovering protected services and devices such as SCADA. It would make a competitive edge compared to other scanner making it one of the bests.


### [OWFuzz: WiFi Protocol Fuzzing Tool Based on OpenWiFi](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Generally, when using WiFi Fuzzing Tool to test the security of WiFi protocol, you need a WiFi USB dongle that supports monitor mode and set the WiFi USB dongle to monitor mode to listen and inject arbitrary WiFi frames. However, many WiFi USB dongles fail to meet our expectations. For example, some are not stable enough in monitor mode and often get stuck, which leads to the interruption of the fuzzing process. And some, we don't have complete control over some frame fields.

OWFuzz is a WiFi protocol testing tool using OpenWiFi. OpenWiFi is an open-source WiFi protocol stack based on SDR that is fully compatible with Linux mac80211. It's driver takes advantage of the Linux kernel's supports (mac80211, cfg80211) for WiFi high MAC, so it can provide an interface to the application layer like a common WiFi USB dongle. In The hardware part, CSMA/CA protocol and other functions of WiFi low MAC layer are implemented on FPGA. It supports monitoring and injection of arbitrary WiFi frames，The application layer software can also directly communicate with the OpenWiFi driver/FPGA/RF underlying functions through nl80211, which provides users with great autonomous and controllable ability. OWFuzz is the first to use OpenWiFi platform (Xilinx ZC706 dev board + FMCOMMS3) to implements a WiFi protocol fuzzing test framework, which supports the fuzzing test of all WiFi frames and the interactivity testing of WiFi protocols.

This research introduces a comprehensive overview of the OWFuzz. We will introduce its architecture, implementation (arbitrary frame and protocol interactivity fuzzing test), and how it works. And finally we will have a video demonstration.


### [Octopus: Pre-operation C2 Server](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Octopus is an open source, pre-operation C2 server based on python which can control an Octopus powershell agent through HTTP/S.

The main purpose of creating Octopus is for use before any red team operation, where rather than starting the engagement with your full operational arsenal and infrastructure, you can use Octopus first to attack the target and gather information before you start your actual red team operation.

Octopus works in a very simple way to execute commands and exchange information with the C2 over a well encrypted channel, which makes it inconspicuous and undetectable from almost every AV, endpoint protection, and network monitoring solution.

One cool feature in Octopus is called ESA, which stands for "Endpoint Situational Awareness", which will gather some important information about the target that will help you to gain better understanding of the target network endpoints that you will face during your operation, thus giving you a shot to customize your real operation arsenal based on this information.

Octopus is designed to be stealthy and covert while communicating with the C2, as it uses AES-256 by default for its encrypted channel between the powershell agent and the C2 server. You can also opt for using SSL/TLS by providing a valid certficate for your domain and configuring the Octopus C2 server to use it.


### [Osiris-Framework: A Scalable Tool for Penetration Testing and Vulnerability Assessment on Cross-Platform Systems](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Abstract—Osiris-Framework V1.337 is an open-source project designed to assist security researchers in penetration testing and vulnerability assessment exercises through unique features such as 0-days and helpers, custom-made modules, and the ability to provide valuable information about vulnerabilities in a specific target. Additionally, the framework can be executed in multi-platform systems which allows security researchers to perform audits from geographically widespread locations.


### [Overlord: Red Teaming Automation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Overlord provides a python-based console CLI which is used to build Red Teaming infrastructure in an automated way. The user has to provide inputs by using the tool’s modules (e.g. C2, Email Server, HTTP web delivery server, Phishing server etc.) and the full infra / modules and scripts will be generated automatically on a cloud provider of choice. Currently supports AWS and Digital Ocean.

Links:
- GitHub repository - https://github.com/qsecure-labs/overlord
- A demo infrastructure - https://blog.qsecure.com.cy/posts/overlord/
- Full documentation of the tool - https://github.com/qsecure-labs/overlord/wiki

Acknowledgments:
This project could not be created without the awesome work for Marcello Salvati @byt3bl33d3r with the RedBaron Project. That is the reason why we are referencing the name of RedBaron on our project as well.
As Marcello stated on his acknowledgments, further thanks to:
1. @_RastaMouse's two serie's blogpost on 'Automated Red Team Infrastructure Deployment with Terraform' Part 1 and 2
2. @bluscreenofjeff's with his amazing Wiki on Read Team Infrastucture
3. @spotheplanet's blog post on Red team infrastructure


### [P.A.K.U.R.I Penetration Test Achieve Knowledge Unite Rapid Interface](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PAKURI is a semi-automated, user-friendly framework for penetration testing tools. Using only the keypad, you can use the penetration test tool like a game.

It's also a great introductory tool for beginners. Learn the flow of penetration testing with PAKURI without having to wrestle with confusing command lines and tools.

https://github.com/01rabbit/PAKURI


### [PEASS: Privilege Escalation Awesome Scripts SUITE](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PEASS - Privilege Escalation Awesome Scripts SUITE is as the name suggests a collection of privilege escalation scripts. We have a script for Linux, Windows and a Windows .net4 executable. We are launching macOSx version at Black Hat Asia 2020. These tools search for possible local privilege escalation paths that you could exploit and print them with nice colours so you can recognise misconfigurations easily.


### [PEsidious: Creating Chaos with Evasive Mutative Malware](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Over the past two decades, research has been conducted on using AI to detect malware by extracting features and then classifying them using machine learning algorithms.

What's more interesting is how adversaries have begun using AI to attack these AI models. One current use case of such an approach is the use of AI (GAN) to generate Deepfakes.

Pesidious draws inspiration from this approach to use AI to mutate the malware samples in order to evade AI-based classifiers.
The tool uses the Generative Adversarial Network to first generate benign-looking imports and sections that can make malware look benign and fool machine learning models. We further use deep reinforcement learning to teach a model in which other mutations can reduce the detection rate for malware. The various mutations include changes to imports, exports, headers, signature, sections, and size.

Pesidious bagged the first place prize and a whopping $40000 in the HITB CyberWeek AI challenge 2019, and we are back again with some additional features to improve its efficiency and the chaos it brings with it!

The tool presented and views expressed are solely our own and do not express the views or opinions of our employer.


### [POLAR: Accelerating the Search for Vulnerable Functions](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
When developing exploits for complex platforms, finding function relationships between dynamically compiled binaries and its libraries, and representing them in a Graph Database, we can quickly identify exploitation points. In this presentation, I'll discuss Graphs, Binary Relationships and Vulnerable Functions.


### [Pentest Collaboration Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Pentest Collaboration Framework - An opensource, cross-platform and portable toolkit that allows you to exchange information on the penetration testing process. It also contains a model of differentiation of rights for use by several teams or independent researchers.

One of latest major updates from previous Black Hat conference is a new feature - issue templates library which allow pentesters to create issues much more faster!


### [Phishmonger: Welcome to the Phish Market](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [PivotSuite: Hack The Hidden Network - A Network Pivoting Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PivotSuite is a portable, platform independent and powerful network pivoting toolkit, which helps Red Teamers/Penetration Testers to use a compromised system to move around inside a network. It is a Standalone Utility, which can be uses as a Server or as a Client.

PivotSuite as a Server: If the Compromised host is directly accessible (Forward Connection) from our pentest machine, then we can run pivotsuite as a server on a compromised machine and access the different subnet hosts from our pentest machine, which was only accessible from a compromised machine.

PivotSuite as a Client: If the Compromised host is behind a Firewall/NAT and isn't directly accessible from our pentest machine, then we can run pivotsuite as a server on pentest machine and pivotsuite as a client on compromised machine for creating a reverse tunnel. Using this, we can reach different subnet hosts from our pentest machine, which was only accessible from a compromised machine.

Key Features:

Supported Forward & Reverse TCP Tunneling
Supported Forward & Reverse Socks5 Proxy Server
UDP over TCP and TCP over TCP Protocol Supported
Corporate Proxy Authentication (NTLM) Supported
Inbuilt Network Enumeration Functionality, Eg. Host Discovery, Port Scanning, OS Command Execution
PivotSuite allows to get access to different Compromised host and their network, simultaneously (Act as C&C Server)
Single Pivoting, Double Pivoting and Multi-level pivoting can perform with help of PivotSuite
PivotSuite also works as SSH Dynamic Port Forwarding but in the Reverse Direction

Advantage Over Other tools:

Doesn't required admin/root access on Compromised host
PivotSuite also works when Compromised host is behind a Firewall / NAT, When Only Reverse Connection is allowed
No dependency other than python standard libraries
No Installation Required
UDP Port is accessible over TCP


### [Power Automate C2: Stealth Living-Off-the-Cloud C2 Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PowerAutomate C2 is a framework designed to emulate "Living Off the Cloud" attacks, leveraging only legitimate functions in PowerAutomate.

The battlefield has shifted from the endpoint to the cloud in evolving cyber warfare. This shift can increase the wealth of useful information the cloud offers, making it a more lucrative target for attackers. This transition introduces a new tactic, "Living Off the Cloud," which has become increasingly prevalent in cyber-attacks.

PowerAutomate, a powerful cloud-based automation platform also known as the "New PowerShell", allows for the execution of these "Living Off the Cloud" attacks. PowerAutomate is particularly attractive to attackers as it enables stealth activities. One characteristic is a client-free execution which carries out an attack that leaves no logs on the client and completes entirely in the cloud. It ensures no traces are left on the endpoint, network devices, or within the Office 365 environment. Despite this, continuous access to PowerAutomate on the victim's user profile is required to execute and manage the flow of an attack. PowerAutomate provides a connector known as PowerAutomate Management to address this challenge. This connector allows for managing the flow itself, thus eliminating the need for persistent access to the victim's user profile.

In this presentation, we introduce the concept and demonstration of PowerAutomate C2, which utilizes the basic functions of PowerAutomate and exclusively employs the PowerAutomate Management connector. PowerAutomate C2 is built on a Python-based platform, enabling control over PowerAutomate's flow without a GUI-based low-code interface. This approach also facilitates the remote creation and deletion of flows with no logs, even after access to PowerAutomate is lost. For C2 communication, we have implemented support for HTTP(S) and storage services like Dropbox, enhancing the flexibility and stealth of the operation. We also alert the risk of improper permission to use PowerAutomate Management.


### [PowerGuest: AAD Guest Exploitation Beyond Enumeration](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Azure AD guest accounts are widely used to grant external parties limited access to enterprise resources, with the assumption that these accounts pose little security risk. As you're about to see, this assumption is dangerously wrong.

PowerGuest is a new tool that allows you to achieve the full potential of a guest in Azure AD by exploiting a series of undocumented internal APIs and common misconfiguration for collecting privileges, and using those for data exfiltration and actions on target, leaving no traces behind. The tool operates by leveraging shared credentials shared over Power Platform, a low-code / no-code platform built into Office365.

PowerGuest allows gaining unauthorized access to sensitive business data and capabilities including corporate SQL servers, SharePoint sites, and KeyVault secrets. Furthermore, it allows guests to create and control internal business applications to move laterally within the organization. All capabilities are fully operational with the default Office 365 and Azure AD configuration.


### [PowerShell-RAT](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PowerShell-RAT is a stealthy tool which exfiltrates sensitive information from the Windows environment through screenshots and keystrokes. The exfiltrated information is sent to a malicious user over a HTTPS protocol in the form of email attachments. The RAT can be invoked with a single key press using 'Hail Mary' option. Gmail is used to receive files from the backdoored machine. As Gmail is considered one of the highly trusted domains, this would allow an attacker to avoid network detection by NextGen Firewalls.

During a Red Team engagement, this tool can be executed on any Windows machine which backdoors the user machine using a number of task schedulers which will run the PowerShell scripts. Once backdoored, malicious user receives screenshots of the user activities via email every 5 minutes. After the email is received, screenshots are deleted from the machine to clean up the disk space, hence, avoiding the detection.

On successful authentication on a Windows machine, backdoor triggers the keystroke module on the user machine. It saves every key press via keyboard in the "log.txt" file on the user machine and sends it to the malicious user every hour as an email attachment. Setup requires a dedicated throw away Gmail account with modification to PowerShell script credential variables and a malicious user needs to enable "Allow less secure apps" under the security settings of the Gmail account to receive screenshots and key logs from the backdoored machine.

Target system can be identified using attachments naming convention which is Computer name followed by the timestamp. The backdoor Python file can be converted into an executable using Pyinstaller. During demo, I would also walk through a number of defence mechanisms to detect stealthy backdoors using publicly available tools such as Sysinternals from Microsoft.


### [PowerUpSQL: A PowerShell Toolkit for Attacking SQL Serversin Enterprise Environments](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PowerUpSQL includes functions that support SQL Server discovery, weak configuration auditing, privilege escalation on scale, and post exploitation actions such as OS command execution. It is intended to be used during internal penetration tests and red team engagements. However, PowerUpSQL also includes many functions that can be used by administrators to quickly inventory the SQL Servers in their ADS domain and perform common threat hunting tasks related to SQL Server. This should be interesting to red, blue, and purple teams interested in automating day to day tasks involving SQL Server.

Source Code: https://github.com/netspi/powerupsql
Slides: https://bit.ly/2OxbGYy﻿
Video: https://youtu.be/UX_tBJQtqW0


### [Powerglot: Encoding offensive scripts using polyglots for stego-malware, privilege escalation & lateral movement](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
In red-team exercises or offensive tasks, masking of payloads is usually done by using steganography, especially to avoid network level protections, being one of the most common payloads scripts developed in powershell. Recent malware and APTs make use of some of these capabilities: APT32, APT37, Ursnif, Powload, LightNeuron/Turla, Platinum APT, Waterbug/Turla, Lokibot, The dukes (operation Ghost), Titanium, etc. But offensive tools based on steganography need a loader to run the payload. Powerglot tries to reduce this exposition using polyglots in several scenarios.

Powerglot is a multifunctional and multi-platform attack and defense tool based on polyglots. Powerglot allows to mask a script (powershell, shellscripting, php, ...) mainly in a digital image, although other file formats are in progress. Unlike the usual offensive tools or malware, Powerglot does not need any loader to execute the "information hidden", minimizing the noise on the target system.

PowerGlot has a clear utility in offensive tasks but it is also defined as a discovery and blue team tool. To our knowledge, it is the first general and complete open-source tool that allows to search for the presence of masked information with polyglots, information that could be useful to achieve persistence in a system or to hide malware (stego-malware, privilege escalation, lateral movement, reverse shell, etc.)


### [PyExfil: A Python Data Exfiltration Package](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PyExfil is a python data exfiltration package for python containing servers and clients for enabling covert channels communication. The package started as a self exploratory code project and developed into a library that helps analyze various detection mechanisms.


### [PyRDP: Python 3 Remote Desktop Protocol Man-in-the-Middle (MITM) and Library](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PyRDP is an RDP man-in-the-middle tool that has applications in pentesting and malware research. On the pentesting side, PyRDP has a number of features that allow attackers to compromise RDP sessions when combined with TCP man-in-the-middle solutions. If network-level authentication (NLA) is not enforced on an organization's RDP servers, attackers can use PyRDP to take complete control of RDP sessions. The graphical interface shows the client's credentials, keystrokes and clipboard contents as well as the current screen. It also has a "take control" button that allows attackers to hijack sessions. While the attacker is in control, all output going to the client is blocked to hide malicious activity. PyRDP also lists the contents of the drives mapped by the clients and allows attackers to download files from them. Finally, attackers can configure the man-in-the-middle to automatically run payloads on new connections. These payloads can be console commands or PowerShell scripts, and are hidden from the clients. Attackers can make use of PyRDP even when NLA is enforced by redirecting traffic to their own virtual machine. This setup allows them to collect credentials and use the functionalities for stealing clipboard contents and files.

On the malware research side, PyRDP can be used as part of a fully interactive honeypot. It can be placed in front of a Windows RDP server to intercept malicious sessions. It has the ability to replace the credentials provided in the connection sequence with working credentials to accelerate compromise and malicious behavior collection. It also saves a visual and textual recording of each RDP session, which is useful for investigation. Additionally, PyRDP saves a copy of the files that are transferred via the drive redirection feature, allowing it to collect malicious payloads. This accelerates malware analysis since there is no need to search for the payloads on the infected machines or in the network activity.


### [PyRDP: Remote Desktop Protocol MITM for Purple Teamers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PyRDP is a Remote Desktop Protocol (RDP) monster-in-the-middle (MITM) tool and library useful in intrusion testing, and protocol and malware research. Its out-of-the-box offensive capabilities can be divided in three broad categories: client-side, MITM-side and server-side. On the client-side, PyRDP can actively steal any clipboard activity, crawl mapped drives and collect all keystrokes. On the MITM-side PyRDP records everything on the wire in several formats (logs, JSON events), captures the user's hashes on-the-fly to enable hash cracking, it also allows an attacker to take control of an active session and performs a pixel perfect recording of the RDP screen. On the server-side, on-logon PowerShell or command injection can be performed when a legitimate client connects.

As a research tool, PyRDP can be used as part of a fully interactive honeypot. It can be placed in front of a Windows RDP server to intercept malicious sessions. It can replace the credentials provided in the connection sequence with working credentials to accelerate compromise and malicious behavior collection. It also saves a visual and textual recording of each RDP session, which is useful for investigation or to generate IOCs. Additionally, PyRDP saves a copy of the files that are transferred via the drive redirection feature, allowing it to collect malicious payloads.

This year we have implemented NetNTLMv2 hash capturing for NLA sessions which enables pentesters and offensive researchers to crack hashes in order to retrieve passwords used during the user's connection.


### [PyRDP: Remote Desktop Protocol Monster-in-the-Middle (MITM)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
PyRDP is a Remote Desktop Protocol (RDP) monster-in-the-middle (MITM) tool and library useful in intrusion testing and malware research. Its out of the box offensive capabilities can be divided in three broad categories: client-side, MITM-side and server-side. On the client-side PyRDP can actively steal any clipboard activity, crawl mapped drives and collect all keystrokes. On the MITM-side PyRDP records everything on the wire in several formats (logs, JSON events), allows the attacker to take control of an active session and performs a pixel perfect recording of the RDP screen. On the server-side, on-logon PowerShell or cmd injection can be performed when a legitimate client connects.

On the malware research side, PyRDP can be used as part of a fully interactive honeypot. It can be placed in front of a Windows RDP server to intercept malicious sessions. It can replace the credentials provided in the connection sequence with working credentials to accelerate compromise and malicious behavior collection. It also saves a visual and textual recording of each RDP session, which is useful for investigation or to generate IOCs. Additionally, PyRDP saves a copy of the files that are transferred via the drive redirection feature, allowing it to collect malicious payloads.

Over the last year, we implemented several features that we are going to uncover in this brand-new arsenal workshop: improved file interception and crawling, dynamic certificate cloning, CredSSP/NLA support with private certificate and key, dynamic NLA redirection, NTLMSSP hash logging, and more.


### [RATTLER](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Rattler is a tool that automates the identification of DLL's which can be used for DLL preloading attacks on Windows 7/8.1/10. The automation of such a process significantly decreases the amount of time required to identify vulnerable and exploitable DLL's.

For example, if an application were to have ~100 DLL's and if it took ~2 minutes to test each DLL, that is ~2 hours for a single application to be tested using a manual process. Additionally, the process for testing an application for DLL preloading vulnerabilities is rather simple and can be automated trivially using some C++, Windows API calls and fresh beard oil , hence Rattler.

The identification of vulnerable DLL's can assist in an attacker in achieving code execution or escalation of privileges.


### [RID Hijacking: Maintaining Access on Windows Machines](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The art of persistence is (and will be...) a matter of concern when successfully exploitation is achieved. Sometimes it is pretty tricky to maintain access on certain environments, especially when it is not possible to execute common vectors like creating or adding users to privileged groups, dumping credentials or hashes, deploying a persistent shell, or anything that could trigger an alert on the victim. This statement ratifies why it's necessary to use discrete and stealthy techniques to keep an open door right after obtaining a high privilege access on the target.

What could be more convenient that only use OS resources in order to persist an access? This presentation will provide a new post-exploitation hook applicable to all Windows versions called RID Hijacking, which allows setting desired privileges to an existent account in a stealthy manner by modifying some security attributes. To show its effectiveness, the attack will be demonstrated by using a module which was recently added by Rapid7 to their Metasploit Framework, and developed by the security researcher Sebastián Castro.


### [ROP ROCKET: Advanced Framework for Return-Oriented Programming](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Racketeer: Prototyping Ransomware Operations](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Rate Unlimiter](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Red Kube](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Red Kube is a red team cheat sheet based on kubectl commands to Asses the Kubernetes Cluster Security Posture.


### [RedHerd Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
RedHerd is a collaborative serverless framework for orchestrating a geographically distributed set of assets in order to simulate/conduct complex offensive cyberspace operations. The design and implementation of RedHerd perfectly fit the Open Systems Architecture design pattern, thanks to the adoption of both open standards and wide-spread open source software components.

The framework allows to seamlessly deploy a ready-to-use infrastructure that can be adopted for effective conduct, simulation and training purposes, by reliably joining a real-world cyberspace battlefield in which red and blue teams challenge each other to reach their goals. These elements lead to the Offensive Cyberspace Operations as a Service (OCOaaS) paradigm, which involves a complete software solution, locally set up, remotely deployed or Cloud-based, offering a layer of abstraction placed in front of the operative infrastructure and tools.

In this way, the operational actors have the opportunity to focus on the task execution, while ignoring all of the collateral activities. In addition, OCOaaS provides a flexible and quickly deployable solution to reduce costs. The RedHerd framework is a practical implementation of this model empowering the approach with strong orchestration capabilities and other additional features.


### [Remove-Signature](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Remove-Signature is a tool designed to automate the process of generating a payload that can bypass anti-virus detection.

During red team testing, red team operators often need to prepare a payload that will not be detected by anti-virus software in order to be successful. One way to do this is to identify where the signatures used by anti-virus software are located in the payload, and then modifies bytes of the locations so that the modified payload will not be detected as malicious. This process can be time-consuming.

Remove-Signature aims to automate this process by identifying the signatures in the payload, and modifying a single byte of the signatures location in a way that will bypass anti-virus detection, while still maintaining the functionality of the payload. The tool understands the PE file format and only makes modifications that will not affect the payload's functionality. Unlike other existing tools that can only identify signatures, Remove-Signature is able to automatically generate a modified payload that can evade anti-virus detection.

The use of Remove-Signature can help to reduce the workload of red team operators and allow them to focus on other aspects of the red team engagement.


### [Route53Sweep: Empowering AWS Route53 Security with Automated Scanning & Comprehensive Inventory Management](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Route53Sweep uses the AWS Route53 service to improve the management of Route53 security providing a innovative solution to DNS Security. AWS Route53-managed resources like domains, subdomains, DNS records, and related services are all secured and protected by this, which also adopts a comprehensive approach to DNS security management. Organizations can easily track changes to their AWS Route53 resources with Route53Sweep, as well as automate procedures for scanning public IPs and fixing them. Organizations can increase their security and dependability with Route53Sweep, freeing them up to concentrate on other important business operations.

Key Topics:

Addressing the Urgent Need: We investigate the escalating security issues surrounding AWS Route53 and the necessity of specialized scanning software like Route53Sweep. To protect organizations from potential threats, we emphasize the value of ongoing monitoring and keeping a complete inventory of Route53 assets.

Route53Sweep Unleashed: Learn more about our cutting-edge tool's inner workings and how it effectively makes use of a variety of open source tools such as the Nuclei engine, Anew, Httpx, and Notify. The combination of these open-source components with Route53Sweep improves vulnerability scanning capabilities and makes asset discovery and monitoring in real time easier.

A Unique Approach: We are proud of our "Desi Jugaad" spirit, which embodies ingenuity and resourcefulness. This idea is embodied by Route53Sweep, which offers an unusual but effective way to automate AWS Route53 security management. Our tool ensures user friendliness while streamlining scanning, automating inventory management, and reducing common security issues.

Mitigating Critical Security Issues: Learn how Route53Sweep handles important security issues like NXDomain, Subdomain Takeovers & External Vulnerability Scanning. We demonstrate how our tool enables businesses to proactively address these issues and fortify their security defenses.

Real-Time Alerting with Slack: Take a glimpse at the power of Slack integration, which enables real-time alerting for discovered assets and vulnerabilities. Organizations are kept informed and ready to act quickly in case of threats thanks to Route53Sweep.

Live Demonstration: It presents a interactive, live demonstration of Route53Sweep in use. Discover how the tool manages AWS Route53 assets, identifies vulnerabilities, and performs all of these tasks in a simple and effective way.


### [Router Exploit Shovel: Automated Application Generation for Stack Overflow Types on Wireless Routers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Router exploits shovel is an automated application generation tool for stack overflow types on wireless routers. The tool implements the key functions of exploits, it can adapt to the length of the data padding on the stack, generate the ROP chain, generate the encoded shellcode, and finally assemble them into a complete attack code. The user only needs to attach the attack code to the overflow location of the POC to complete the Exploit of the remote code execution. The tool also incorporates live recovery, leaving no trace of attack after the Exploit attack is completed.


### [Routopsy: Routing Protocol Vulnerability Analysis and Exploitation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Routopsy is a new network attack toolkit that leverages a "virtual router" in a Docker container to scan for and attack various networking protocols and misconfigurations. Vulnerabilities include overly broad configured network statements within routing protocols, unauthenticated or plaintext authentication for protocols such as OSPF and HSRP, and the lack of passive interface usage within routing protocols.

Routopsy was designed in a way that will allow users to trivially perform attacks without requiring extensive networking knowledge. Attacks include the injection of new routes, discovery of new networks and gateway takeover attacks which ultimately could lead to Person-in-the-Middle attacks. Additionally, a fully-fledged router interface is also available for more experienced users and for more advanced attacks.

Internally, Routopsy leverages a "virtual router" which has been around for a number of years, is well maintained and supports a variety of protocols. Once the scan phase of Routopsy is complete a simple configuration is loaded within the virtual router and used to attack the target protocol.


### [SCADAsploit: a Command & Control for OT. How to break an ICS system](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
SCADAsploit is the only C2 (Command & Control) framework targeting OT systems. Its powerful arsenal of pre- and post-exploitation modules for SCADA/PLC systems makes it a unique tool in Adversary Simulation operations in the OT and IoT environment. Its modular client/server architecture, which can be controlled remotely with a super-secure connection, provides modules dedicated to penetration testing, vulnerability scanning, asset discovery, and pre- and post-exploitation.


SCADAsploit boasts a robust client/server architecture that ensures seamless communication and collaboration between your team members. This scalable framework enables the efficient distribution of tasks and enhances your offensive capabilities, allowing you to penetrate even the most complex OT environments.


But it is even more than that. Thanks to its flexibility and inherent EDR evasion capability, SCADAsploit is also an effective and powerful tool for traditional IT infrastructures.


### [SCAVENGER: A Post-Exploitation Scanning/Mapping Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
SCAVENGER is a multi-threaded post-exploitation scanning tool for mapping systems and finding "interesting" and most frequently used files, folders and services. Once credentials are gained, it can scan remote systems (Linux, Windows and OSX) via services like SMB and SSH to scrape that system looking for "interesting" things and then cache the result. SCAVENGER has the ability to find the newest files that have been accessed/modified/created and keep the result in an ordered database. Then, after time has passed, hours or days later the systems can be scanned again. SCAVENGER can then compare the previous list of "newest files" to the latest list of "newest files." This gives the user the ability to find the "interesting" and most frequently files used on that system, for example password files being accessed by an administrator or heavily used credit card database files.

Whilst looking for "interesting" files, folder and services, SCAVENGER scans these filenames and their content for various "interesting" phrases, for example "password" or "secret." Once detected SCAVENGER then downloads the "interesting" file to the local system. At the same time SCAVENGER also scans for Card Holder Data and also downloads the file if Card Holder Data is found.

Future features will be the addition of services like NFS, FTP and database connections. Also adding more capability of retrieving passwords from remote Linux or Windows systems, without touching to the disk of the remote system. And without reinventing the wheel using SCAVENGER as a wrapper to use on Windows systems performing more post-exploitation techniques.

Source Code: https://github.com/SpiderLabs/scavenger﻿


### [SCMKit: Source Code Management Attack Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Source Code Management (SCM) systems play a vital role within organizations and have been an afterthought in terms of defenses compared to other critical enterprise systems such as Active Directory. SCM systems are used in the majority of organizations to manage source code and integrate with other systems within the enterprise as part of the DevOps pipeline, such as CI/CD systems like Jenkins. These SCM systems provide attackers with opportunities for software supply chain attacks and can facilitate lateral movement and privilege escalation throughout an organization.

This presentation will announce the public release of SCMKit, a toolkit that can be used to attack SCM systems. SCMKit allows the user to specify the SCM system and attack module to use, along with specifying valid credentials (username/password or API key) to the respective SCM system. Currently, the SCM systems that SCMKit supports are GitHub Enterprise, GitLab Enterprise and Bitbucket Server. The attack modules supported include reconnaissance, privilege escalation and persistence. SCMKit was built in a modular approach, so that new modules and SCM systems can be added in the future by the information security community.


### [SETH](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Seth is a tool written in Python and Bash to MitM RDP connections. It attempts to downgrade the connection and extract clear text credentials - even with Network Level Authentication enabled.

The default configuration in a Windows landscape is to use self-signed certificates to secure SSL connections to RDP hosts. Since self-signed certificates provide almost no security at all, it is obvious that an attacker in a "Man in the Middle" position can simply present their own certificate and eavesdrop on the connection. However, so far there were no freely available open source tools that can do this. In order to raise awareness of how important it is to use properly signed certificates, Seth was developed.

It performs a man in the middle attack, downgrades any additional security if possible and extracts interesting information, such as password hashes, clear text credentials or key stroke events.


### [SIEMs Framework: Open Source MultiSIEM Python Attack Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
SIEMs are defensive tools increasingly used in information security, especially in large companies and regulated companies to monitor critical networks and devices. However, from the standpoint of the attacker, the permissions that the SIEMs have on the devices and accounts of a corporate network are very broad. Administrative access to a SIEM can be used to obtain code execution in the server where the SIEM is installed, and, in some cases, also in the "client" equipment from which the SIEM collects events, such as Active Directory servers, Databases, and network devices like Firewalls and Routers.

During our investigation, we detected many attack vectors that could be used in different SIEMs to compromise them, such as:

Obtaining the user accounts and passwords of critical equipment stored in the SIEM (LDAP/AD servers, databases, network devices, generally accounts with administrative permissions)
Developing and installing malicious applications such as a bind shell or a reverse shell to compromise the server where the SIEM is installed, or send malicious applications to compromise the devices from which the SIEM collects the events
Performing a brute force attack on the SIEM web interface
Reading arbitrary files from the server where the SIEM is installed
Using log events as intelligence source

Based on the results of this research, we developed an open source tool in Python: SIEMs Framework that allows to automate the mentioned attacks, both in commercial and open source SIEMs.


### [SILENTTRINITY (v0.2.0): Async Post-Exploitation Agent Powered by Python, C# & .NET's DLR](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
SILENTTRINITY is an asynchronous post-exploitation agent powered by Python, IronPython, C# and .NET's DLR (Dynamic Language Runtime), it attempts to weaponize and demonstrate the flexibility that BYOI (Bring Your Own Interpreter) payloads have over traditional C# implants. What are BYOI payloads? Turns out, by harnessing the sheer craziness of the .NET framework, you can embed entire interpreters inside of .NET languages allowing you to natively execute scripts written in third-party languages (like Python) on windows! Not only does this allow you to dynamically access all of the .NET API from a scripting language of your choosing, but it also allows you to still remain completely in memory and has a number of advantages over traditional C# payloads! Essentially, BYOI payloads allow you to have all the "power" of PowerShell, without going through PowerShell in anyway! Additionally, you can nest multiple interpreters within each other to perform what I've coined "engine inception"! If you're interested in bleeding-edge and out of the ordinary C#/.NET offensive trade-craft, this is the demo for you!


### [SMBeagle](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
SMBeagle is an SMB file share auditing and enumeration tool that rapidly hunts out file shares and inventories their contents. Built from a desire to find poorly protected files, SMBeagle casts the spotlight on files vulnerable to ransomware, watering hole attacks and which may contain sensitive credentials.

SMBeagle hunts out all files it can see in the network and reports if the file can be read and/or written. All these findings are streamed out to either a CSV file or an elasticsearch host?

Businesses of all sizes often have file shares with awful file permissions.

Large businesses have sprawling file shares and its common to find sensitive data with misconfigured permissions and small businesses often have a small NAS in the corner of the office with no restrictions at all!

SMBeagle crawls these shares and lists out all the files it can read and write. If it can read them, so can ransomware.

SMBeagle can provide penetration testers with the less obvious routes to escalate privileges and move laterally.

By outputting directly into elasticsearch, testers can quickly find readable scripts and writeable executables.

Finding watering hole attacks and unprotected passwords never felt so easy!


### [SMERSH](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
It's a collaborative open source tool to manage pentest campaigns.
You can install it via Docker ( it includes an Angular front end with a symfony API )
There is also a python client for the bearded ones.
The graphical interface allows you to add your scope and vulnerabilities and exchange information with your hacker partners in a Quick and easy way (also possible to generate report).


### [SSHoRTy: Linux/MacOS Armored SSH Implant Delivery With a Smile](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
SSHoRTY is a Linux/MacOS implant attempting to alleviate the challenges Red Teams face at establishing initial foothold on non-Windows machines and initiating clean egress communications to the team C2 servers across a stack of defensive monitoring. Native SSH tunnels with automated port forwards, convenient SOCKS proxy capabilities built right into a reverse shell. All that wrapped in a HTTP/S proxy-aware fully encrypted websocket connection to evade even the most tight policies. Built on demand for every deployment, with a choice of binary-embedded shared keys or out-of-band channels PKI authentication, SSHoRTy is also very progressive. It can even be injected as a shared library into a running process to hide its presence. It assumes nothing, and just gives the Red a consistent, reliable and flexible tunnel into the network.


### [Scanhanced: An Automation Tool for Pentesting and Vulnerability Assessments](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
A lot of the initial steps in black box penetration testing involve information gathering using techniques such as port scanning. This information is then usually used for OSINT such as searching for known vulnerabilities for the found services and versions. Next steps often include searching for exploits for the found vulnerabilities. This process is inconvenient as it is often both labor and time intensive, both of which can often be a limiting factor for an engagement.
Scanhanced solves this by providing an easy command line interface that can then perform the previously mentioned steps automatically, reducing both labor and time needed to minutes. It will perform a port scan, and then using that information attempt to find vulnerabilities and search community resources for exploits. Additionally, Scanhanced provides additional features such as identifying whether a given exploit is available in existing exploit frameworks, being able to download exploits, or download the vulnerable apps in question. Moreover, Scanhanced can produce output in JSON, XML, or CSV for use in further automation or ingestion into another tool if so desired.
This entire process in addition to more complex functionality can be performed with an easy to use command and flags, saving pentesters time and from having to do tedious work.


### [Scapy: Python-Based Interactive Packet Manipulation Program + Library](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Scapy (https://github.com/secdev/scapy) is a renowned packet manipulation tool written in Python that supports a wide number of protocols on many different platforms (Linux, macOS, *BSD, and Windows). Initially developed by Philippe Biondi since 2003, it is now maintained by Guillaume Valadon, Pierre Lalet and Gabriel Potter. While the existence of this tool is well-known, its grip is much less, to the community's detriment. This presentation aims at filling this gap using practical and detailed examples.


### [SecScanC2 -- Manage Assesment to Create P2P Network for Security Scanning & C2](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
In the realm of security attack and defense, as well as penetration testing, two key challenges often arise. Firstly, attack scanning is frequently detected by defensive security systems, resulting in the scanning IP being blocked. Secondly, when defensive assets are controlled and connected back to the command and control (C2) server, security devices may detect the connection, leading to countermeasures against penetration testers. To address these challenges and enable safe, efficient asset detection and secure connections to controlled assets, we have enhanced the Kademlia protocol and developed a Distributed Hash Table (DHT) technology.

Our hacking tool is highly effective during attack scanning, consisting of a large number of Internet nodes that dynamically update IDs and node tree structures at regular intervals. This approach allows each session to initiate requests from different nodes during the scanning process, thus avoiding IP blocking due to high-frequency scanning. Moreover, when connecting controlled assets back to the C2 server, nodes are randomly selected based on a user-defined hop count, effectively preventing penetration testers from being traced and significantly enhancing the stealthiness of the entire penetration testing process.


### [Secureworks® Primary Refresh Token (PRT) viewer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Azure AD registered and joined devices use a device certificate and transport key to sign and decrypt communication between the device and Azure AD. The most important part of this is Primary Refresh Token (PRT) and an associated session key. The session key can be decrypted with the transport key and subsequent communication with the session key.
Secureworks® Primary Refresh Token (PRT) viewer automates the decryption process. Using the transport key exported from the target computer, it automatically decrypts the session key from the PRT authentication request response. With the decrypted session key, it decrypts subsequent requests/responses decrypted with the session key.
The tool enables monitoring the traffic between the target device and Azure AD in plaintext, allowing extracting keys, access tokens, and other secrets.
The tool is available as Burp Suite Extender and Fiddler Add-On.


### [SharpSCCM 2.0 - Abusing Microsoft's C2 Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
SharpSCCM 2.0 - Abusing Microsoft's C2 Framework

SharpSCCM is a post-exploitation tool designed to leverage Microsoft Endpoint Configuration Manager (a.k.a. ConfigMgr, formerly SCCM) for credential gathering and lateral movement without requiring access to the SCCM administration console GUI (e.g., from a C2 agent).

The release of SharpSCCM 2.0 includes new functionality to execute arbitrary commands on groups of devices, coerce NTLM authentication from remote SCCM clients that belong to specific users, dump and decrypt additional credentials from an SCCM client or by requesting them from a management point, and triage of local client files for software distribution point locations.

This session will include demonstrations of multiple techniques that can be used to take over an SCCM site, dump credentials from an SCCM client, execute arbitrary commands on remote SCCM clients, and coerce NTLM authentication from remote SCCM clients and servers.

Each demo will be followed by practical recommendations for mitigating these attacks and Q&A.


### [SharpSCCM](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
SharpSCCM is an open-source C# utility for interacting with SCCM, inspired by the PowerSCCM project by @harmj0y, @jaredcatkinson, @enigma0x3, and @mattifestation. This tool can be used to demonstrate the impact of configuring SCCM without the recommended security settings, which can be found here: https://docs.microsoft.com/en-us/mem/configmgr/core/clients/deploy/plan/security-and-privacy-for-clients

Currently, SharpSCCM supports the NTLMv2 coercion attack techniques noted in this post (https://posts.specterops.io/coercing-ntlm-authentication-from-sccm-e6e23ea8260a), as well as the attack techniques noted in this post (https://enigma0x3.net/2016/02/29/offensive-operations-with-powersccm/), which have been modified to coerce NTLMv2 authentication rather than running PowerShell on the target. SharpSCCM can also be used to dump information about the SCCM environment from a client, including the plaintext credentials for Network Access Accounts.

Research is ongoing to add SharpSCCM features to:
- pull and decrypt Network Access Account credentials from SCCM servers using a low-privileged account on any client machine
- execute actions in SCCM environments that require PKI certificates to secure client/server communications
- escalate privileges from local administrator on site servers to SCCM Full Administrator


### [SharpToken: Windows Token Stealing Expert](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
During red team lateral movement, we often need to steal the permissions of other users. Under the defense of modern EDR, it is difficult for us to use Mimikatz to obtain other user permissions, and if the target user has no process alive, we have no way to use "OpenProcessToken" to steal Token.


SharpToken is a tool for exploiting Token leaks. It can find leaked Tokens from all processes in the system and use them. If you are a low-privileged service user, you can even use it to upgrade to "NT AUTHORITY\SYSTEM" privileges, and you can switch to the target user's desktop to do more without the target user's password. ..


### [Shoggoth: Asmjit Based Polymorphic Encryptor](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
From past to present, signature-based detection has been one of the first and most basic methods used to detect malicious files. Even today, every file written to the file system is first scanned using the signatures found in the database of security products. Therefore, when creating variants of a tool or a technique, one of the most used methods to prevent them from being captured by a single signature is Polymorphism.

While polymorphism was used for this purpose, it was embedded in the virus variant as an engine, especially in self-propagating viruses. Nowadays, polymorphism occurs in the obfuscation of a binary or a shellcode. New variants of these codes, which are produced with polymorphic encoders such as Shikata Ga Nai (SGN), make them difficult to detect with a general and single YARA rule. Shoggoth is yet another polymorphic encoder written using asmjit library.

For each encoding period of a binary, Shoggoth generates different encryption routines with different garbage instructions. After obtaining the encrypted form of the payload, the tool merges it with its decryptor stub which again contains different garbage instructions. Shoggoth uses asmjit library for assembling the process of randomly generated encryption and garbage instructions.


### [SquarePhish: Combining QR Codes and OAuth 2.0 Device Code Flow for Advanced Phishing Attacks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
SquarePhish is an advanced phishing tool that uses a technique combining the OAuth Device code authentication flow and QR codes. Previous OAuth 2.0 Device Code phishing tools (like PhishInSuits) required a user open the phishing email and authenticate within 15 minutes of the email being sent. This drastically decreased the chances of a successful phish, as many emails expired prior to user interaction.

SquarePhish fixes this issue, by decoupling the initial email from the OAuth Device Code flow. Combining this technique, QR Codes, and a Microsoft MFA pretext we are able to perform advanced phishing attacks.

We have also added a subtool called Rephresh that utilizes undocumented Microsoft functionality that allows the SquarePhish obtained tokens to be swapped out for tokens for other applications.


### [Starkiller: Threat Emulation Platform for Red Teams and Penetration Testers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The ultimate goal for any security team is to increase resiliency within an organization and adapt to the modern threat. Starkiller aims to provide red teams with a platform to emulate Advanced Persistent Threat (APT) tactics. Starkiller is a frontend for the post-exploitation framework, PowerShell Empire, which incorporates a multi-user GUI application that interfaces with a remote Command and Control (C2) server. Empire is powered by Python 3 and PowerShell and includes many widely used offensive security tools for Windows, Linux, and macOS exploitation. The framework's flexibility to easily incorporate new modules allows for a single solution for red team operations. Both red and blue teams can utilize Starkiller to emulate and defend against the most used APT attack vectors.


### [Stratus Red Team, an Open-Source Adversary Emulation Tool for the Cloud](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Stratus Red Team is an open-source project for adversary emulation and validation of threat detection in the cloud. It comes with a catalog of cloud-native attack techniques mapped to MITRE ATT&CK that you can easily detonate against a live cloud environment or Kubernetes cluster.

Stratus Red Team supports common AWS and Kubernetes attack techniques. You can point it at a live AWS account or Kubernetes cluster and easily detonate TTPs commonly used by offensive actors, without any prerequisite infrastructure or configuration needed. It helps you validate your threat detection end-to-end and even has a programmatic interface to integrate it with existing automation.
Stratus Red Team transparently leverages Terraform to provision the infrastructure required to detonate TTPs, and Go to perform the actual attacks. The TTPs it packages are opinionated: granular, threat-informed, and actionable for defenders.


### [Suborner: A Windows Bribery for Invisible Persistence](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Whenever an attacker is trying to persist the access on a compromised machine, the first offensive approach usually involves the creation of a new identity. Nevertheless, this may not work easily under hardened environments with diverse detection mechanisms against common attack vectors.

What if we "suborn" Windows to create our own hidden account that will grant us total access to a victim, while stealthily impersonating any account we want?

Now it is possible with the Suborner Attack.

This technique will dynamically create an invisible machine account with custom credentials and custom properties without calling any user management Win32 APIs (e.g. netapi32.dll::netuseradd) and therefore evading detection mechanisms (e.g Event IDs 4720, 4721). By "suborning" Windows, we can also impersonate any desired account to keep our stealthiness even after a successful authentication/authorization.

To show its effectiveness, the attack is going to be demonstrated against the latest Windows version available.


### [The Air-Gap Malware of X-Sploit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
X-Sploit is a Linux-based Red-Teaming-Toolkit for IT security experts and geeks. In this presentation, we will introduce a physical penetration tip, the Air-gap malware in X-Sploit Toolkit. The victim device's hardware adapter could be controlled and used for backdoor data transmission without interfering with the target's existing connection status and communication.


Advantage:
Cross-platform support (Windows, Mac OS, Linux)
Bypass Firewall/IDS/IPS
No signature, more difficult to detect
Used in isolate network environment attack
Does not affect the victim's existing connection status and communication


### [The Grinder Framework - Bringing Light to the Shodan](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The security-related search engines like Shodan, Censys or ZoomEye are daily cybersecurity research tools. They can be used to gather information within threat Intelligence, discover vulnerable hosts, craft fingerprints for vulnerability scanners. At the same time, such search engines have some fundamental limitations and constraints leading to blind spots, false negatives and wrong results. It is very disappointing, especially when new research has been started and the cost of a mistake could be days or even weeks spent in the wrong direction.

The Grinder Framework is an open-source security research toolkit adopted to Internet-wide surveys and allows you to use the full power of tools like Nmap, Shodan, Censys, Vulners, TLS-attacker and bringing the light through tailored scanning and threat intelligence approach. The Grinder was born in the SD-WAN New Hope project when we explored SD-WAN security on the Internet.

In this talk, we will describe the essence of the Grinder framework and show how you can employ it in your security researches. We will consider the blind spots of the modern search engines, describe non-trivial use cases we worked out during our Internet-scale surveys and illustrate new features by examples from the SD-WAN New Hope, AIsec and DICOMSec projects.


### [The Metasploit Framework's Payload Improvements](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Memory corruption vulnerabilities are becoming less common than their more reliable command execution counterparts. In the last year, two-thirds of the exploits Metasploit released resulted in OS command execution in some way as opposed to direct execution of injected code. Metasploit has made multiple improvements to its command payloads to keep pace with these exploitation trends. These updates make it easier for module authors to deliver a wider variety of second-stage payloads and grant users greater flexibility in selecting their delivery mechanism.

This arsenal demonstration will cover the latest improvements to Metasploits payloads, command stagers, and Meterpreter. The audience will see how these payloads can be used, customized and how the exploit development process has improved.


### [The Metasploit Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Modern attack emulation is a multi-step process involving different tools and techniques as testers execute custom workflows to achieve their objectives. One primary advantage of the Metasploit Framework is a unified approach to solving this problem.

This arsenal demonstration will cover some of the latest improvements to the Metasploit Framework and showcase how these improvements maximize effectiveness while performing common tasks. Viewers will see the latest workflows for capturing credentials, UI optimizations for running modules, and demonstrations of Metasploit's new payload-less session types. Capturing credentials is an integral part of many penetration testing methodologies and, when combined with the Metasploit database, can be a powerful technique for users engaged in breaching simulations. The latest features streamline configuring all the services Metasploit has capture modules for and managing them as a single unit. Users will also learn about some of the latest improvements related to pivoting in Metasploit, which allow capturing services to be started on compromised hosts when combined.


### [ThunderCloud: Attack Cloud Without Keys!](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
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


### [Tool Aids in Monitoring Dynamic Scanning](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Antivirus software, as one of the important tools to protect computer security, its detection technology is also constantly developing. At the same time, penetration testing and malicious attacks have become more difficult. The core principle of our newly developed network security tool is to load the security software to be used into memory and relocate all import function tables (IAT) to a middle code area, so that it can continue to run without being killed. When each external function is referenced, it will jump to the middle stub function and retain the call information. If our security tool is killed by antivirus software, we can easily find the detection point of antivirus software based on the call information. Our security tool can detect its scanning rules in real time while antivirus software is running, so as to help you understand the behavior and rules of antivirus software. Our tool can detect antivirus software without disrupting its normal work, so as to help you better understand the behavior and rules of antivirus software.


### [Vajra - Your Weapon To Cloud](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Abstract:

Vajra (Your Weapon to Cloud) is a framework capable of validating the cloud security posture of the target environment. In Indian mythology, the word Vajra refers to the Weapon of God Indra (God of Thunder and Storms). Because it is cloud-connected, it is an ideal name for the tool.
Vajra supports multi-cloud environments and a variety of attack and enumeration strategies for both AWS and Azure. It features an intuitive web-based user interface built with the Python Flask module for a better user experience. The primary focus of this tool is to have different attacking and enumerating techniques all in one place with web UI interfaces so that it can be accessed anywhere by just hosting it on your server.


The following modules are currently available:

• Azure
- Attacking
1. OAuth Based Phishing (Illicit Consent Grant Attack)
- Exfiltrate Data
- Enumerate Environment
- Deploy Backdoors
- Send mails/Create Rules
2. Password Spray
3. Password Brute Force
- Enumeration
1. Users
2. Subdomain
3. Azure Ad
4. Azure Services
- Specific Service
1. Storage Accounts
• AWS
- Enumeration
1. IAM Enumeration
2. S3 Scanner
- Misconfiguration


### [WIG: Wi-Fi Information Gathering](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
WIG (Wi-Fi Information Gathering) is a free and open source (GPLv3) utility for IEEE 802.11 device fingerprinting. WIG uses Wi-Fi network interfaces that supports monitor mode to obtain information on nearby devices with Wi-Fi support. The tool supports vendors proprietary protocols such as Apple AirDrop/AirPlay, Cisco Client eXtensions, Wi-Fi Protected Setup (WPS) and Wi-Fi Direct. Using these protocols the tool is able to find and fingerprint potential Wi-Fi targets that other tools are not able to find. The tool output it's useful on the threat modeling phase during wi-fi penetration testing or to find potential targets during a network assessment.


### [WMIHacker: A New Way to Use 135 Port Lateral Movement Bypass AV and Transfer File](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
After the eternal blue virus flood, most intranets no longer open port 445, so the 135-port DCOM service becomes another exploitable point. We need a tool or method that can use 135 ports to execute commands and the Ability to transfer files. WMIHacker is such a tool and can bypass av.

Remote command execution tools such as psexec (sysinternals) and wmiexec (impacket) are frequently used during lateral movement. However, these tools will be killed by anti-virus software and the command executed will fail. Psexec will create services and leaves a lot of logs, including a lot of operations such as service creation. The way win32_process.create used by wmiexec.py will no doubt be blocked by AV. I found a new way to execute commands on a machine with an AV and can overwrite window2003 to the latest version of windows. Because I use VBScript to run it. There is no doubt that someone is studying the same content as I did. I found that there are many ways to execute on the internet, including deriving win32_process, registering COM and making it as a malicious provider, msi abuse, etc., but these known ways of using Being intercepted by av.


### [WMImplant: An Offensive Use Case of WMI](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
When looking forward to the latest defenses that are being seen in environments all over the world today, we're consistently seeing EDR, "Next-Gen AV", and application whitelisting. Of the available defenses, application whitelisting seemed like the most interesting challenge to undertake. We wanted to build something that would work against one of the best application whitelisting solutions from a detection/prevention perspective, Windows Defender Application Control (WDAC), previously known as Device Guard.

WDAC aims to lock down Windows workstations via multiple methods, one example is digital signature based rule enforcement when determining if an application is allowed to execute. Another, is that WDAC automatically enforces PowerShell into Constrained Language Mode (CLM), a severely restricted version of PowerShell. So how can you operate in a restricted WDAC environment?

WMImplant is one possible answer. Why not leverage a service that is built in to Windows and enabled by default since the days of Windows Server 2000? Windows Management Instrumentation (WMI) enables us to execute commands on systems, remotely and locally. WIth the enforcement of PowerShell Constrained Langauge Mode (CLM), our PowerShell based code had to adhere to the restrictions of the language mode. WMImplant is fully PowerShell CLM compliant and is designed to provide a Meterpreter-esque menu for users to easily perform post-exploitation tasks against the targeted system.

Come learn how a CLM compliant code-base designed to operate exclusively over WMI can allow you to survive and thrive in a heavily restricted application whitelisting environment.


### [WTS: Scenario-Based WiFi Network Threat Simulation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The WiFi Network Threat Simulation project is designed to perform scenario-based wifi network security tests. Thanks to the modules inside, you can test both the user and AP devices as well as the wireless IDS and IPS devices.


### [WarBerryPi - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
WarBerryPi was built to be used as a hardware implant during red teaming scenarios where we want to obtain as much information as possible in a short period of time while being as stealthy as possible. The WarBerryPi also includes an intuitive interactive reporting module for viewing the results of each red teaming engagement.


### [When World War II meets CDNs: A New Class of Pulsing DDoS Attack](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Content Delivery Networks (CDNs) are commonly believed to offer their customers protection against denial of service (DoS) attacks. However, our research reveals a novel architecture vulnerability in CDNs, enabling attackers to turn globally distributed CDN Infrastructure into powerful DDoS amplifiers.

In this talk, we draw the analogy to a military tactic used in World War II and introduce a new class of pulsing denial-of-service attacks. We demonstrate how CDNs can be exploited to concentrate low-rate attacking requests into short, high-bandwidth pulse waves, resulting in a pulsing DDoS attack to saturate targeted TCP services periodically.

We tested five leading CDN vendors and found all of them are susceptible to this attack. By mounting an attack against our own Web site, we show that attackers can use it to achieve peak bandwidths over 1000 times greater than their upload bandwidth, seriously degrading the performance and availability of target services. We have reported our findings to all tested CDNs and received positive feedback.

As this problem is rooted in the inherent nature of CDN forwarding networks, it is difficult to eliminate entirely. We discuss possible mitigation strategies for this emerging threat. We believe it is important that CDN operators and their customers be aware of this attack so that they can protect themselves accordingly.


### [WhiskeySAML and Friends](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [WhoC: Peeking Under the Hood of CaaS Offerings](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
None


### [Zuthaka: A Collaborative Free Open-Source Command & Controls (C2s) Integration Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
A collaborative free open-source Command & Control development framework that allows developers to concentrate on the core function and goal of their C2.
Zuthaka presents a simplified API for fast and clear integration of C2s and provides a centralized management for multiple C2 instances through a unified interface for Red Team operations.
Zuthaka is more than just a collection of C2s, it is also a solid foundation that can be built upon and easily customized to meet the needs of the exercise that needs to be accomplished. This integration framework for C2 allows developers to concentrate on a unique target environment and not have to reinvent the wheel.
After we first presented Zuthakas' MVP at Black Hat USA 2021, we are now presenting the first release with a live demo lab to share the possibilities of integration and flexibility of Red Team infrastructure.


### [Zuthaka: Collaborative C2 Development Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
A collaborative free open-source Command & Control development framework that allows developers to concentrate on the core function and goal of their C2.

Zuthaka presents a simplified API for fast and clear integration of C2s and provides a centralized management for multiple C2 instances through a unified interface for Red Team operations.


### [aDLL: adventure Dynamic Link Library](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Adventure of Dynamic Link Library (aDLL) is a console tool for the analysis of binaries and focused on the automatic detection of possible DLL Hijacking cases in Windows systems. The purpose of the tool is to analyse every DLL that an executable will load in memory, anticipating the Windows DLL search order and identifying those DLLs that are missing from the expected directory. That may lead in the replacement of the legitimate DLL by a malicious one if the directory has misconfigured permissions.


### [barq: The AWS Post-Exploitation Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
barq is a post-exploitation framework that allows you to easily perform attacks on a running AWS infrastructure.


### [bloodyAD](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
BloodyAD is an Active Directory Privilege Escalation Framework. It helps you interact with the Active Directory (AD) to read/modify its objects in order to perform privilege escalation.
Two modes exist, the first one lets you perform atomic operations on the AD, it's the manual mode. The second one automates most of the privilege escalation operations.
The tool can be installed on Linux and Windows and is designed to be used on your offensive machine even if you're not on the local network of the targeted AD, relying on encapsulation protocols like SOCKS.


### [git-wild-hunt: Pwn API and leaked secrets](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Git Wild Hunt is a tool that allows researchers and security operators to find leaked credentials and secrets in Github covering over 30 types of credentials. This tool is great for cloud security/DevOps security awareness or for cloud security pentesters and red teamers. We will show how deep into an organization or even personal sensitive information can be found by simply starting from leaked credentials in a GitHub project.


### [go-exploit: An Exploit Framework for Go](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
go-exploit is an exploit development framework for Go. The framework helps exploit developers create small, self-contained, portable, and consistent exploits.

Many proof-of-concept exploits rely on interpreted languages with complicated packaging systems. They implement wildly differing user interfaces, and have limited ability to be executed within a target network. Some exploits are integrated into massive frameworks that are burdened by years of features and dependencies which overwhelm developers and hinder the attacker's ability to deploy the exploits from unconventional locations.

To overcome these challenges, go-exploit offers a lightweight framework with minimal dependencies, written in Go—a language renowned for its portability and cross-compilation capabilities. The framework strikes a balance between simplicity for rapid proof-of-concept development and the inclusion of sophisticated built-in features for operational use.


### [hideNsneak: An Attack Obfuscation Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
hideNsneak evolved as a tool to expand evasive penetration testing capabilities. It allows users to rapidly deploy, manage, and quickly take down a distributed cloud attack infrastructure by leveraging features of large Cloud Providers and their content delivery networks. Techniques include domain fronting with multiple providers, distributed scanning, and source of attack obfuscation. Leaning on the reputation of these networks allows traffic to more easily blend in to network traffic and create difficulty in blocking attack infrastructure. Furthermore, the ephemeral nature of the tool itself provides a realistic threat simulation, which also simulates the realistic headache this type of attack causes defenders, when they try to attribute actions to certain sets of hosts.

The overview of the toolsets features will contain an explanation of the tactics and techniques in order to provide both red teamers and blue teamers alike with more insight into why this works in "modern" networks, as well as real world scenarios. Also, this tool was written in the Go programming standard in which each functionality is encapsulated in its own package. This allows for users to use the frameworks individual packages in their own projects as well as add components with relative ease. Finally, information will be provided to blue teamers in an effort to provide knowledge that can be brought back and leveraged to increase security posture.


### [iBombShell: Dynamic Remote Shell](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The emergence of PowerShell within pentesting post-exploitation is important. Its flexibility, possibilities and power make this Microsoft´s command line an efficient post-exploitation tool. In scenarios where we cannot use neither install pentesting techniques this tool acquires special relevance. iBombShell gives access to a pentesting repository where the pentester could use any function oriented to the post-exploitation phase and, in some cases, exploit vulnerabilities. iBombShell is a remote pentesting Shell that loads itself automatically in memory offering unlimited tools for the pentester.

iBombShell is a tool written in PowerShell that allows post-exploitation functionalities in a shell or a prompt, anytime and in any operating system. Moreover, it allows, in some cases, the execution of vulnerability exploitation features. These features are loaded dynamically, depending on when they are needed, from a GitHub repository.

The shell is downloaded directly to memory giving access to many pentesting features and functionalities, avoiding any hard drive access. These functionalities downloaded to memory are in PowerShell function format. This execution strategy is called EveryWhere.

In addition, iBombShell allows a second way of execution called Silently. Using this execution way, an iBombShell instance (called warrior) can be launched. When the Warrior is executed over a compromised machine, it will connect to a C2 through the http protocol. From the C2, written in Python, a warrior can be controlled to dynamically load functions to the memory and to offer pentesting remote execution functionalities. All those steps are part of the post-exploitation phase.


### [on the fly](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
The 'on-the-fly' tool intends to give the pentester an 'all-in-one' tool by deploying different functionalities applicable across the three domains of work: IoT, ICS & IT. The present work introduces a new framework in which enough functionalities will be provided to discover, evaluate, and audit technologies from the three mentioned domains.


### [peetch - an eBPF based networking tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
peetch is a collection of tools aimed at experimenting with different aspects of eBPF to bypass TLS protocol protections.


### [pstf^2: Link Scanners Evasion Made Easy](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
Link scanners are a critical component in many essential security products, checking whether a URL is malicious or not. It is embedded within email security products, sandbox solutions and as a standalone direct link scanner.

This tool will present how to circumvent them all using passive browser fingerprinting - a set of techniques allowing a server to profile a client based only on the request being sent.

While often used to detect and repel internet bots, we will show how this fingerprinting can be applied against blue teamers, specifically - how a resourceful attacker may use it to determine if it is being scanned and serve benign content to scanners while delivering harmful content to users.

pstf^2 leverages passive fingerprints in HTTP, TCP, IP layers and even link-layer protocols.


### [tty2web](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming](https://img.shields.io/badge/Category-Red--Teaming-gray)  
tty2web can take any console program and convert it into a web application. It provides a proper console for your shell needs directly inside your browser, which means programs like vim, mc, or any program that needs tty will work as expected by default. Features include support for both bind and reverse mode, which is useful for penetration testing and NAT traversal, bidirectional file transfer, reverse SOCKS 5 functionality by emulating the regeorg interface, and API support for executing commands (imagine having a RESTful interface to your operating system shell). It supports collaboration and sharing between teams, is multiplatform, and runs well on Unix/Linux-based OSs running container payloads. It is based on gotty but has been heavily improved for security and penetration tester needs.


---

## Red Teaming / AppSec


### [AARDVARK AND REPOKID](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Amazon AWS provides a tool called "Access Advisor" that shows unused permissions for a given IAM role. Access advisor data can be very valuable for security practitioners as it shows unused permissions that can be removed to harden the environment and promote least privilege best practices.

In the past retrieving Access Advisor information and reclaiming unused permissions has been a tedious and manual process involving logging in to the console and making changes by hand. Aardvark and Repokid are two complementary tools that make this process easy and automatable. Aardvark automatically retrieves access advisor for all roles in all accounts in your environment and exposes it as a queryable API. Repokid uses data presented by Aardvark to enable automatic role right-sizing.

Used together, Aardvark and Repokid can ensure roles retain only the necessary privileges, even in large dynamic AWS deployments.


### [ADA: Android Dynamic Analysis Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
ADA analyzes the dynamic behavior of an Android application in runtime. ADA discovers the attack surface that is not shown during the static analysis and performs a rapid vulnerability assessment of the application.

ADA discovers the best attack path to follow to compromise the application. The automated dynamic analysis is focused on discovering the security measures implemented in the application. In this way, ADA shows the best attack path to compromise the application. Some of the features that ADA detects are whether the application uses certificate pinning, JNI libraries, SQL database discovery, KeyStores identification, hardware-backed KeyStore (TEE), etc.


### [AISY: A Framework for Deep Learning-Based Side-Channel Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Profiling side-channel attacks (SCA) allow evaluators to verify the worst-case security scenario of their products. Nowadays, deep learning has become the state-of-the-art method for profiling SCA as deep neural networks show the ability to learn side-channel leakages from protected implementations. While deep learning is a powerful technique for security evaluations, it offers numerous possibilities for neural network configurations and optimization techniques. Selecting the best setup for each evaluated product is far from trivial and requires expertise in SCA and deep learning fields. To improve SCA methods, and at the same time to be able to investigate the resistance of the product to more complex attack scenarios, researchers continuously propose new techniques.
Unfortunately, several obstacles are making the acceptance of such techniques a challenge. Security evaluators from the industry face difficulties following up on new promising methods. What is more, certification bodies also must be aware of new SCA techniques to issue the certifications. Indeed, one of the main issues is the lack of publicly available, easy-to-use frameworks that allow powerful and reliable side-channel analysis. Moreover, due to the absence of the uniformed evaluation/implementation method, the reproducibility of the outcomes is not easy to ensure.

We propose AISY as a tool to allow state-of-the-art deep learning-based SCA. AISY is a python-based open-source framework, and it provides state-of-the-art functionalities for profiling SCA with easy usage, extensibility, reproducibility, integrated database, and user interface. We envision a system where the user can efficiently run the attacks with few lines of code and based on state-of-the-art but also extend those functionalities to support new developments. AISY supports the complete development cycle for deep learning-based SCA: from dataset preparation to the automated development of new models and their assessment concerning the side-channel metrics.


### [ART: Adversarial Robustness 360 Toolbox for Machine Learning Models](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Adversarial attacks against machine learning systems have become an indisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (so-called poisoning attacks), or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (so-called evasion attacks). These attacks have been demonstrated in a number of different application domains, including malware detection, spam filtering, visual recognition, speech-to-text conversion, and natural language understanding. Devising comprehensive defences against poisoning and evasion attacks by adaptive adversaries is still an open challenge.

We will present the Adversarial Robustness 360 Toolbox (ART), a library which allows rapid crafting and analysis of both attacks and defense methods for machine learning models. ART provides an implementation for many state-of-the-art methods for attacking and defending machine learning. At Black Hat, we will introduce the major version 1.0, which contains new powerful black-box attacks, support for additional machine learning libraries, as well as new defenses and detectors. Through ART, the attendees will (re)discover how to attack and defend diverse machine learning systems.


### [ART: Adversarial Robustness Toolbox for Machine Learning Models](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Adversarial attacks of machine learning systems have become an indisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (so-called poisoning attacks) or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (so-called evasion attacks). Adversarial attacks have been demonstrated in a number of different application domains, including malware detection, spam filtering, visual recognition, speech-to-text conversion, and natural language understanding. Devising comprehensive defences against poisoning and evasion attacks by adaptive adversaries is still an open challenge.

We will present the Adversarial Robustness Toolbox (ART), a library which allows rapid crafting and analysis of both attacks and defense methods for machine learning models. It provides an implementation for many state-of-the-art methods for attacking and defending machine learning. Through ART, the attendees will (re)discover how to attack and defend machine learning systems.


### [Adversarial Robustness Toolbox for Machine Learning Models - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Adversarial attacks of machine learning systems have become an undisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (so-called poisoning attacks), or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (so-called evasion attacks). Adversarial attacks have been demonstrated in a number of different application domains, including malware detection, spam filtering, visual recognition, speech-to-text conversion, and natural language understanding. Devising comprehensive defences against poisoning and evasion attacks by adaptive adversaries is still an open challenge.

We will present the Adversarial Robustness Toolbox (ART), a library which allows rapid crafting and analysis of both attacks and defence methods for machine learning models. It provides an implementation for many state-of-the-art methods for attacking and defending machine learning. Through ART, the attendees will (re)discover how to attack and defend machine learning systems.


### [Adversarial Threat Detector](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
In recent years, deep learning technology has been developing, and various systems using deep learning are spreading in our society, such as face recognition, security cameras (anomaly detection), and ADAS (Advanced Driver-Assistance Systems).

On the other hand, there are many attacks that exploit vulnerabilities in deep learning algorithms. For example, the Evasion Attacks are an attack that causes the target classifier to misclassify the Adversarial Examples into the class intended by the adversary. The Exfiltration Attacks are an attack that steals the parameters and train data of a target classifier. If your system is vulnerable to these attacks, it can lead to serious incidents such as face recognition being breached, allowing unauthorized intrusion, or information leakage due to inference of train data.

So we released a vulnerability scanner called "Adversarial Threat Detector" (a.k.a. ATD), which automatically detects vulnerabilities in deep learning-based classifiers.

ATD contributes to the security of your classifier by executing the four cycles of "Detecting vulnerabilities (Scanning & Detection)", "Understanding vulnerabilities (Understanding)", "Fixing vulnerabilities (Fix)", and "Check fixed vulnerabilities (Re-Scanning)".

1. Detecting vulnerabilities（Scanning & Detection）
ATD automatically executes a variety of attacks against the classifier and detects vulnerabilities.

2. Understanding vulnerabilities (Understanding)
When a vulnerability is detected, ATD will generate a countermeasure report (HTML style) and a replay environment (ipynb style) of the vulnerabilities. Developers can understand the vulnerabilities by referring to the countermeasure report and the replay environment.

3. Fixing vulnerabilities (Fix)
ATD automatically fixes detected vulnerabilities.

4. Check fixed vulnerabilities (Re-Scanning)
The ATD checks fixed vulnerabilities of the fixed classifier.

Our "Adversarial Threat Detector" will contribute greatly to keep your safety.


### [ArcherySec - Manage and Automate your Vulnerability Assessment](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
ArcherySec is an open-source vulnerability assessment and automation tool which helps developers and pentesters to perform scans and manage vulnerabilities. ArcherySec uses popular open-source tools to perform comprehensive scanning for web applications and networks. It also performs web application dynamic authenticated scanning and covers the whole application by using selenium. The developers can also utilize the tool for the implementation of their DevOps CI/CD environment.

Overview of the tool
- Perform web and network vulnerability scanning using open-source tools.
- Correlates and collaborates all raw scans data, shows them in a consolidated manner.
- Multi-user role-based accounts admin, analyst & viewer
- Policy-based CI/CD integration
- Perform authenticated web scanning.
- Perform web application scanning using selenium.
- Vulnerability management.
- Enable REST APIs for developers to perform scanning and vulnerability management.
- JIRA Ticketing System.
- Periodic scans.
- Useful for DevOps teams for vulnerability management.


### [ArcherySec 2.0 - Open Source Vulnerability Assessment and Management](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
ArcherySec is an opensource vulnerability assessment and management tool which helps developers and pentesters to perform scans and manage vulnerabilities. ArcherySec uses popular opensource tools to perform comprehensive scanning for web applications and networks. It also supports multiple continuous integrations and continuous delivery software. The developers could utilize this tool for the implementation of vulnerability management in the DevOps CI/CD environment.

- Perform Web and Network Vulnerability Scanning using opensource tools.
- Correlates and Collaborate all raw scans data, shows them in a consolidated manner.
- Perform authenticated web scanning.
- Vulnerability Management.
- Enable REST API's for developers to perform scanning and Vulnerability Management.
- JIRA Ticketing System.
- Sub domain discovery and scanning.
- Periodic scans.
- Concurrent scans.
- Integrate with CI/CD software.


### [Archery: Open Source Vulnerability Assessment and Management - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
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


### [Artificial Intelligence Phishing Email Detector](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
An artificial intelligence-based phishing email detector that analyses emails and its content, vocabulary, sender, subject etc and detects if it's a phishing email even if it was not flagged as one by an email gateway based on the analysis of collection of phishing emails.


### [Attack Knowledge Base for Automotive](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Ensuring cybersecurity in the automotive sector is more crucial than ever, especially with the rising intricacies and susceptibilities of vehicle-connected systems. The ISO/SAE 21434 standard serves as a beacon in this endeavor. However, compliance with this standard reveals discernible information disparities across its V-model phases: Concept & Design, Implementation, and Verification & Validation. Addressing these gaps is paramount for cohesive vehicle cybersecurity.

To tackle these hurdles, we introduce the "Attack Knowledge Base for Automotive." Inspired and aligned with the ATT&CK framework, this tool aids in seamless compliance with the ISO/SAE 21434 standard. We will demonstrate its efficacy in delivering a thorough and objective outcome during Threat Analysis and Risk Assessment (TARA). Moreover, it bridges information lacunas across the lifecycle, enabling the red team to synergize insights from earlier stages with our Attack Knowledge Base, ensuring holistic automotive cybersecurity.


### [Automatic API Attack Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Imperva's customizable API attack tool takes an API specification as an input, creates and runs attacks which are based on it as an output.

After researching the web, we didn't find an automatic tool which takes an API specification and checks the server offering the service against it. But we saw a high demand for such a tool from the community. So we decided to build it.

The tool is able to parse the API specification and create fuzzing attack scenarios based on what it defines, and outside of its definition. Each endpoint is injected with cleverly generated values within the boundaries defined by the specification, and outside of it, the appropriate requests are sent and their success or failure are reported in a detailed manner. It is also able to run various security attack vectors targeted at the existing endpoints, or even non-existing ones (such as illegal resource access, XSS, SQLi and RFI).
No human intervention needed, simply run the tool and get the results.

The tool can be easily extended to adapt to the various needs; whether it is a developer who wants to test the API she wrote or an organization which wants to run regular vulnerability or positive security scans on its public API, you name it. It is built with CI/CD in mind.

We are using this tool, among other tools, to check our security products internally.


### [Automating Fuzzable Target Discovery with Static Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Vulnerability researchers conducting security assessments on software will often harness the capabilities of coverage-guided fuzzing through powerful tools like AFL++ and libFuzzer. This is important as it automates the bughunting process and reveals exploitable conditions in targets quickly. However, when encountering large and complex codebases or closed-source binaries, researchers have to painstakingly dedicate time to manually audit and reverse engineer them to identify functions where fuzzing-based exploration can be useful.

Fuzzable is a framework that integrates both with C/C++ source code and binaries to assist vulnerability researchers in identifying function targets that are viable for fuzzing. This is done by applying several static analysis-based heuristics to pinpoint risky behaviors in the software and the functions that executes them. Researchers can then utilize the framework to generate basic harness templates, which can then be used to hunt for vulnerabilities, or to be integrated as part of a continuous fuzzing pipeline, such as Google's oss-fuzz.

In addition to running as a standalone tool, Fuzzable is also integrated as a plugin for Binary Ninja, with support for other disassembly backends being developed.


### [Azucar: Multi-Threaded Plugin-Based Tool to Help Assess the Security of Azure Cloud Environment Subscription](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Azucar is a multi-threaded plugin-based tool to help assess the security of Azure Cloud environment subscription. By leveraging the Azure API, Azucar automatically gathers a variety of configuration data and analyses all data relating to a particular subscription in order to determine security risks.


### [BucketLoot - An Automated S3-compatible Bucket Inspector](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
BucketLoot is an automated S3-compatible Bucket inspector that can help users extract assets, flag secret exposures and even search for custom keywords as well as Regular Expressions from publicly-exposed storage buckets by scanning files that store data in plain text.


### [C0deVari4nt](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
None


### [CATSploit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
CATSploit is an automated penetration testing tool using Cyber Attack Techniques Scoring (CATS) method that can be used without pentester.
Currently, pentesters implicitly made the selection of suitable attack techniques for target systems to be attacked.
CATSploit uses system configuration information such as OS, open ports, software version collected by scanner and calculates a score value for capture eVc and detectability eVd of each attack techniques for target system.
By selecting the highest score values, it is possible to select the most appropriate attack technique for the target system without hack knack(professional pentester's skill) .


### [CSF: Container Security Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
There are billions of containers started by organizations on a daily basis. Thus, there has been a considerable need to invest in container security along with the security for conventional compute instance (like a physical machine, AWS EC2, etc.). Currently, there is no open-source automated solution that enables the organization to constantly monitor security hygiene of their container ecosystem.

ArmourBird CSF - Container Security Framework is an extensible, modular, API-first framework build for regular security monitoring of docker installations and containers against CIS and other custom security checks.

ArmourBird CSF has a client-server architecture and is thus divided into two components:

a) CSF Client

This component is responsible for monitoring the docker installations, containers, and images on target machines
In the initial release, it will be checking against Docker CIS benchmark
The checks in the CSF client will be configurable and thus will be expanded in future releases and updates
It has been build on top of Docker bench for security

b) CSF Server

This will be the receiver agent for the security logs generated by the various distributed CSF clients (installed on multiple physical/virtual machines)
This will also have a UI sub-component for unified management and dashboard-ing of the various vulnerabilities/issues logged by the CSF Clients
This server will also expose APIs that can be used for integrating with other systems

Watch out this GitHub space for update: https://github.com/armourbird
Follow the tool updates on twitter: https://twitter.com/ArmourBird


### [CWE_Checker: Architecture-Independent Binary Vulnerability Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Assessing the security of programs running on embedded devices is a difficult task. Source code is generally unavailable and both static and dynamic binary analysis tools often do not offer support for the many different hardware configurations found in embedded devices.

The cwe_checker is an open-source tool for finding bugs and vulnerabilities in binary executables without requiring source code access or any knowledge about the hardware. By using static analysis techniques built atop Ghidra P-Code it supports a wide range of CPU architectures including x86, ARM, MIPS and PowerPC. While its focus is the analysis of ELF binaries commonly found in Linux-based firmware, there exists experimental support for PE files and even bare-metal binaries.

The cwe_checker offers detection of over 16 different bug classes including Buffer Overflows (CWE-119), Use-After-Frees (CWE-416) and Null Dereferences (CWE-476). The tool is built in a modular fashion where each analysis can use its own bug detection technique ranging from simple heuristics to complex data flow analysis. Furthermore, each analysis has a set of configuration parameters that can be modified to adjust the analysis to specific usage scenarios. For example, you can add your own functions to the "Use of potentially dangerous function" check (CWE-676).

It is easy to integrate the cwe_checker into other tools and workflows using the alternative JSON output. For example, as a plugin into the Firmware Analysis and Comparison Tool (FACT) you can use it to hunt for vulnerabilities in large firmware data sets.


### [Carnivore: Microsoft External Attack Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Carnivore is a username enumeration and password spraying tool for Microsoft services (Skype for Business, ADFS, RDWeb, Exchange and O365). It includes new post compromise functionality for Skype for Business (pulling the internal address list and user presence), and a new method for smart detection of the username format. Carnivore originally began as an on-premises Skype for Business enumeration/spray tool as, these days, organizations have often locked down their implementations of Exchange, however, Skype for Business has been left externally accessible, and does not seem to have received as much attention from penetration tests.


### [CloudPathSniffer: Detect and Visualize Abnormal Lateral Movements in Cloud](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
CloudPathSniffer is an open-source, straightforward, and extensible Cloud Anomaly Detection Tool explicitly crafted to assist security teams in uncovering hard-to-see risks and undetected attackers within their control plane of cloud environments.

In the dynamic environment of cloud security, the invisibility of temporary credentials has consistently posed a risk, making identifying and tracing potential malicious activity a challenging endeavor.

Unlike traditional tools, CloudPathSniffer boasts a unique capability that sets it apart: It can effectively track temporary credentials and attack paths made by them. Beyond monitoring, it reveals vulnerabilities concealed within logs and creates a comprehensive attack schema. Utilizing graphics-based visualization, it offers a simplified interpretation of lateral movements within data. By seamlessly integrating these insights into a graph database alongside your credentials, CloudPathSniffer provides an unmatched defense strategy, ensuring every detail is meticulously addressed.


### [Counterfit: Attacking Machine Learning in Blackbox Settings](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
None


### [Deep Exploit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
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


### [Deep Exploit: Fully Automatic Penetration Test Tool Using Machine Learning](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
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


### [Demystifying the State of Kubernetes Cluster Security - The Cloud Native Way](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Attackers always get better with new attack techniques, so our threat modelling and defense mechanisms needs to level up.

The security of the Kubernetes cluster, of course, cannot be achieved in a single process. There are many moving parts within the Kubernetes cluster that must be properly secured.

Kube-striker performs numerous in depth checks on kubernetes infra to identify the security misconfigurations and challenges that devops/developers are likely to encounter when using Kubernetes.

Kube-striker is Platform agnostic and works equally well across more than one platform such as self hosted kubernetes, EKS, AKS, GKE etc.


### [DetectiveSQ: A Extension Auditing Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
In the modern digital realm, internet browsers, particularly Chrome, have transcended traditional boundaries, becoming hubs of multifunctional extensions that offer everything from AI-integrated chatbots to sophisticated digital wallets. This surge, however, comes with an underbelly of cyber vulnerabilities. Hidden behind the guise of innovation, malicious extensions lurk, often camouflaged as benign utilities. These deceptive extensions not only infringe upon user privacy and security but also exploit users with unasked-for ads, skewed search results, and misleading links. Such underhanded strategies, targeting the unsuspecting user, have alarmingly proliferated.

Addressing this conundrum, we present DetectiveSQ - an advanced command-line interface designed to rigorously audit Chrome extensions. At its core, DetectiveSQ is engineered to be compatible with both Manifest V2 (MV2) and Manifest V3 (MV3) architecture, ensuring a wide-ranging applicability across extensions of different generations. Through an intricate examination of permissions - delving deep into how they're invoked and utilized within the extension's codebase - DetectiveSQ brings forth potential security and privacy breaches. The tool not only assesses permissions but also correlates them with actual behaviors, scripts, and external calls, offering a holistic evaluation. DetectiveSQ will be open source and made available after the talk.


### [Extensible Azure Security Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Extensible Azure Security Tool (Later referred to as E.A.S.T) is a tool for assessing Azure and to some extent Azure AD security controls. The primary use case of EAST is Security data collection for evaluation in Azure Assessments. This information (JSON content) can then be used in various reporting tools, which we use to further correlate and investigate the data.


### [FuzzCube](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Fuzzing over the ages has improved in tooling, logic, and process, but is still a number-crunching problem! You are improving your odds by throwing more CPU power at it.

How do we make it happen without hacking through custom solutions that cannot be reused? Enter FuzzCube - Batteries Included! FuzzCube comes with State Sharing Features, Mutation Engines and Crash Verification tools that you could leverage in your projects. It leverages Kubernetes for its infrastructure orchestration capabilities. Using Kubernetes operators, we abstract the complexity of deploying a fuzzing infrastructure with distributed high throughput workloads, fault tolerance, storage orchestration, and high scalability. We will practise distributed fuzzing in the era of Cloud Native Computing and use our new skills to find some 0days ;)


### [Git Wild Hunt: A Tool for Hunting Leaked Credentials](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Git Wild Hunt is a tool designed to search and identify leaked credentials at public repositories such as Github. Git Wild Hunt searches for footprints and patterns of over 38 of the most used secrets/credentials on the internet, especially those used in Devops and IT Operations. This tool helps developers and security operation departments discover leaked credentials in public repositories. This tool is also a recon tool for red teamers and pentesters, as it also provides metadata from leaks such as usernames, company names, secret types, and dates.


### [GoGoGadget - Post Exploitation Utilities for Embedded Systems](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
GoGoGadget is a toolkit that provides useful command line utilities for embedded systems using a broad variety of processor architectures and operating systems. GoGoGadget is written in Go and cross-compiles to a static binary that runs on any of thirteen operating systems and supports thirteen processor architectures with all required libraries included.


### [GyoiThon: Penetration Testing Using Machine Learning](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
In GyioThon released at Black Hat Asia 2018 Arsenal, we used Deep Learning to enable us to identify products that traditional penetration test tools could not identify. In the original GyoiThon, as well as in other tools, it has always been necessary for someone to investigate product-specific features and signature generation with continuous updates, which we've been working to update to make easier. GyoiThon is the growing penetration test tool using Deep Learning. Deep Learning improves classification accuracy in proportion to the amount of learning data. Therefore GyoiThon will be taking in new learning data every scanning. Since GyoiThon uses various features of software included in HTTP response as learning data, you scan more, the accuracy of software detection improves. For this reason, GyoiThon is the growing penetration test tool.

GyoiThon identifies the software installed on web server (OS, Middleware, Framework, CMS, etc...) based on the learning data. After that, GyoiThon executes valid exploits for the identified software. GyoiThon automatically generates reports of scan results. GyoiThon executes the above processing fully automatically.

GyoiThon's major updates:
- Automatically generates the signature to identify various products.
- Can generate signatures necessary for product identification by even users without Deep Learning knowledge using Deep Learning. You no longer have to investigate product-specific features. You no longer need to create a signature, because GyoiThon itself can generate signatures fully automatically.

GyoiThon is the first penetration test tool that made it possible to generate signatures automatically. GyoiThon is evolving as the growing penetration test tool. For further details: https://github.com/gyoisamurai/GyoiThon/blob/master/handout/BHA2018_handout.pdf

GitHub: https://github.com/gyoisamurai/GyoiThon﻿
Presentation Slides: https://github.com/gyoisamurai/GyoiThon/blob/master/handout/BHASIA2019_slide.pdf


### [HACK/400 AND IBMISCANNER TOOLING FOR CHECKING YOUR IBM I (AKA AS/400) MACHINES!](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
In many industries the back-end systems still rely on "heavy" machines such as IBM i (aka AS/400) for core transactional systems. However, this area remained rather uncovered by security researchers. Back in 2015 I presented certain weaknesses of IBM i security at DefCon 23, providing a demo tool for assessment of IBM i systems and exploitation of some weaknesses, like privilege escalation. Since 2015, we improved the tool making it more useful for security personnel and auditors to assess certain important aspects of IBM i system security. These developments led to also adding new functionality in famous cracking tool, John the Ripper, for AS/400 password hashes. Based on users' feedback we try to make it best of class tooling for security assessments, keeping it open source (GPL) for the community.


### [Halcyon IDE: For Nmap Script Developers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Halcyon IDE lets you quickly and easily develop Nmap scripts for performing advanced scans on applications and infrastructures with a wide range capabilities from recon to exploitation. It is the first IDE released exclusively for Nmap script development. Halcyon IDE is free and open source project (always will be) released under MIT license to provide an easier development interface for rapidly growing information security community around the world. The project was initially started as an evening free time "coffee shop" project and has taken a serious step for its developer/contributors to spend dedicated time for its improvements very actively.

Source Code: https://halcyon-ide.org﻿


### [Halcyon IDE: Nmap Script Development IDE](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Halcyon IDE lets you quickly and easily develop Nmap scripts for performing advanced scans on applications and infrastructures with a wide range capabilities from recon to exploitation. It is the first IDE released exclusively for Nmap script development. Halcyon IDE is a free and open-sourced project (always will be) released under MIT license to provide an easier development interface for rapidly growing information security community around the world. The project was initially started as an evening free-time "coffee shop" project and has taken a serious step for its developer/contributors to spend dedicated time for its improvements very actively.


### [HazProne : Cloud Hacking](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
HazProne is a Cloud Pentesting Framework that emulates close to Real-World Scenarios by deploying Vulnerable-By-Demand aws resources enabling you to pentest Vulnerabilities within, and hence, gain a better understanding of what could go wrong and why!!


### [HazProne: Cloud Security Ed](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
HazProne is a Cloud Pentesting Framework that emulates close to Real-World Scenarios by deploying Vulnerable-By-Demand AWS resources enabling you to pentest Vulnerabilities within, and hence, gain a better understanding of what could go wrong and why!!


### [HazProne: Cloud Vulnerability Simulator](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
HazProne is a Cloud Vulnerability Simulator Framework that emulates close to Real-World Scenarios by deploying Vulnerable-By-Demand AWS resources enabling you to pentest Vulnerabilities within, and hence, gain a better understanding of what could go wrong and why!!


### [Introducing RAVEN: Discovering and Analyzing CI/CD Vulnerabilities in Scale](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
As the adoption of CI/CD practices continues to grow, securing these pipelines has become increasingly important. However, identifying vulnerabilities in CI/CD pipelines can be daunting, especially at scale. In this talk, we present our tooling, which we intend to release as open-source software to the public that helped us uncover hundreds of vulnerabilities in popular open-source projects' CI/CD pipelines.

RAVEN (Risk Analysis and Vulnerability Enumeration for CI/CD) is a powerful security tool designed to perform massive scans for GitHub Actions CI workflows and digest the discovered data into a Neo4j database. With RAVEN, we were able to identify and address potential security vulnerabilities in some of the most popular repositories hosted on GitHub, including FreeCodeCamp (the most popular project on GitHub), Storybook (One of the most popular frontend frameworks), Fluent UI by Microsoft, and much more.
This tool provides a reliable and scalable solution for security analysis, enabling users to query the database and gain valuable insights into their codebase's security posture.


### [Ipa-medit: Memory modification tool for iOS apps without Jailbreaking](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Ipa-medit is a memory search and patch tool for resigned ipa without jailbreaking. It supports iOS apps running on iPhone and Apple Silicon Mac. It was created for mobile game security testing. Many mobile games have jailbreak detection, but ipa-medit does not require jailbreaking, so memory modification can be done without bypassing the jailbreak detection.

Memory modification is the easiest way to cheat in games, it is one of the items to be checked in the security test. There are also cheat tools that can be used casually like GameGem and iGameGuardian. However, there were no tools available for un-jailbroken device and CUI, Apple Silicon Mac. So I made it as a security testing tool.

I presented a memory modification tool ipa-medit which I presented at Black Hat USA 2021 Arsenal. At that time, it could only target iOS apps running on iPhone, but now it supports iOS apps running on the Apple Silicon Mac. The Apple Silicon Mac was recently released and allows you to run iOS apps on macOS. For memory modification, I'll explain how the implementation and mechanisms are different for iOS apps running on iPhone or Apple Silicon Mac.

GitHub: https://github.com/aktsk/ipa-medit


### [Jackhammer: One Security Vulnerability Assessment/Management Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Jackhammer is an integrated tool suite which comes with out-of-the-box industry standard integrations. It is a first of its kind tool that combines static analysis, dynamic web app analysis, mobile security, API security, network security, CMS security, AWS/Azure security tools, docker/container security, and vulnerability manager that gives a complete glimpse into security posture of the organization. Using this suite, even senior leadership can have a comprehensive view of their organization's security.

Why was it needed?
Security, while being imperative for any organization, it is hard to comprehend by most of the developers. Security engineers need to scrutinize every service or app turning security analysis a time intensive and repetitive. What if there exists a tool that can empower everyone to test their code for vulnerabilities, automate security analysis, and show the overall security hygiene of the company?

How does it work?
Jackhammer intiates various types of scans using existing proven tools and the results are consumed by onboard vulnerability manager. Unique dashboard presents intuitive interface giving the user a holistic view of the code base. The normalized reports are instantly accessible to Developers, QAs, TPMs, and security personnel.

It can be plugged/integrated with:

CI systems and Git via hooks giving complete control over code commits
AWS/Azure account and can keep on scanning complete IP space in realtime
Additional commercial/open source tools within few minutes and manage those tools from jackhammer
Ticketing systems (like Jira)
slack/pagerduty for real time alerting in addition to SMS and emails

It creates a sandbox using dockers for every tool and scales the systems when the scan needs it and descale on completion of the scans. The spin-up and tear down is a completely automated process so no person needs to look at the resources making it inexpensive and cost-effective.


### [Joern: An Interactive Shell for Code Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Joern is an award-winning open-source platform for robust query-based analysis of C/C++. It enables mining large code bases for vulnerabilities using a Scala-based domain-specific query language and provides the reference implementation for code property graphs. With its fuzzy parsing approach, it is specifically suited for machine learning applications. Joern serves as the fundament for the commercial SAST and code exploration products at ShiftLeft.

The Code Property Graph (CPG) is an intermediate code representation designed for code querying. The core idea it promotes is to merge multiple different program representations into a joint graph data structure and allowing queries to be formulated as graph traversals. In its initial form as presented in 2014, the CPG makes available syntactical information, control flow information and data flow for C/C++ programs. It was later further generalized to host multiple different programming languages, and higher-level code representations.



Important Links
Joern Documentation: https://docs.joern.io
Joern query database: https://queries.joern.io
Joern Community: https://discord.gg/AUzy45EHdf

Demo preparation:

Download VLC v3.0.12 source and extract in a convenient directory
> wget http://get.videolan.org/vlc/3.0.12/vlc-3.0.12.tar.xz
> tar -xvf vlc-3.0.12.tar.xz

Download Joern and install
> wget https://github.com/joernio/joern/releases/latest/download/joern-install.sh
> chmod +x ./joern-install.sh
> sudo ./joern-install.sh


### [KICS - Your IaC Secure Now!](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
KICS stands for Keeping Infrastructure as Code Secure. It is open source and is a must-have for any cloud native project to find security vulnerabilities, compliance issues, and infrastructure misconfigurations early in the development cycle of the underlying infrastructure-as-code (IaC).

KICS supports about 20 different technologies including Terraform, Cloudformation, Kubernetes, Docker, over several cloud providers like AWS, Microsoft Azure or Google Cloud. It is the only open-source project that has achieved any Center for Internet Security (CIS) certification.

KICS is fully customizable and extensible by the addition of rules for new vulnerabilities. It is available as a Docker image, and is paired in multiple platforms to leverage its integration on the development life-cycle and the DevSecOps mentality of its users. Gitlab has chosen KICS as its default IaC scanner; it is also available in ArgoHub, as a hook in TerraformCloud or as a Github Action for Github workflows.

One of the most recent features of KICS is auto remediation. With this feature KICS goes full cycle in preventing vulnerable code from going into production by scanning the code, exposing the issues, and automatically remediating them. Such a feature is both available from the CLI interface, or via a plugin for the Visual Studio Code editor, where we bring together auto-remediation and real-time scanning. As the developer writes IaC scripts, KICS automatically looks for vulnerabilities, proposes fixes and remediates them. By the time the IaC scripts are finished, developers are rest assured that it is safe to go into production. This is shift-left security brought to its splendor.


### [KUBEBOT - SCALEABLE AND AUTOMATED TESTING SLACKBOT WITH THE BACKEND RUNNING ON KUBERNETES](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Security Testing, or for that matter any sort of testing, is still being done in ways that are not really scalable and extensible. Testers like to write their own tools/scripts and run them locally on their system. There are many problems that plague this kind of approach for testing.

We will be discussing some of these problems and releasing a new tool - KubeBot - that was primarily built for automating and scaling bug bounties i.e. something that would run multiple tools on a schedule against multiple targets and only returns back the output from these tools if the output changes.

However, over time, it has proven out to be a more generic framework that can be leveraged as a harness to run any security testing tool and is easily scaleable (because of Kubernetes in the backend). It is extensible and provides a nice front end in the form of a Slackbot so that you can look at the results on a real-time basis.

Tool URL: ﻿https://github.com/anshumanbh/kubebot


### [Kinstrument: Binary-Only Instrumentation Framework for Linux Kernel Based on Breakpoint](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
For regular Linux kernels, we can use qemu or vmware, and then use gdb to debug the kernel, but for some special embedded devices, such as Android phones, it is difficult to debug and instrument the kernel. In order to debug the kernel, it often needs to recompile the kernel and use additional hardware.

The characteristics of kinstrument are as follows:

1. The kernel only needs to support the insertion of the ko module, the kernel does not need to be recompiled, and no additional hardware is required.
2. Support instrumentation basic blocks, and get basic block coverage of kernel code
3. Use the breakpoint mechanism to hook and debug arbitrary instructions.


Kinstrument can be used for kernel debugging and Fuzz.


### [Kubernetes Goat: Interactive Kubernetes Security Learning Playground](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Kubernetes Goat is a "vulnerable by design" Kubernetes Cluster environment to practice and learn about Kubernetes Security. It has step by step detailed guide and digital book on how to get started with Kubernetes Goat by exploring different vulnerabilities in Kubernetes Cluster and Containerized environments. Also, it has scenarios taken from the real-world vulnerabilities and maps the Kubernetes Goat scenarios. The complete documentation and instruction to practice Kubernetes Security for performing security assessments, pentesting, and in general Kubernetes Security. As a defender you will see how we can learn these attacks, misconfigurations to understand and improve your cloud-native infrastructure security posture.

Some of the high-level scenarios include, but are not limited to

1. Sensitive keys in code-bases
2. DIND (docker-in-docker) exploitation
3. SSRF in K8S world
4. Container escape to access host system
5. Docker CIS Benchmarks analysis
6. Kubernetes CIS Benchmarks analysis
7. Attacking private registry
8. NodePort exposed services
9. Helm v2 tiller to PwN the cluster
10. Analysing crypto miner container
11. Kubernetes Namespaces bypass
12. Gaining environment information
13. DoS the memory/CPU resources
14. Hacker Container preview
15. Hidden in layers
16. RBAC Least Privileges Misconfiguration
17. KubeAudit - Audit Kubernetes Clusters
18. Sysdig Falco - Runtime Security Monitoring & Detection
19. Popeye - A Kubernetes Cluster Sanitizer
20. Secure network boundaries using NSP


### [LaiFu: A Modern Protocol Fuzzing Framework Based on Scapy](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
As a protocol tester, we often use scapy to interact with the protocol because it is able to craft or decode packets easily and it implements a wide number of protocols. However, the fuzz function supported by scapy can not fuzz protocols sufficiently and effectively. Testers often need to write additional fuzzing code based on other fuzzing frameworks such as Peach and Boofuzz.

According to the current situation, we design a protocol fuzzing tool named "LaiFu". LaiFu framework allows testers to use scapy to specify protocol formats directly. We designed the corresponding mutation algorithm according to the various field types of scapy's packet. Meanwhile, we also provide a tool to show the coverage of fuzzing target in real time. Testers only need to put each data packet as a node into the graph and then start the fuzzing test. Another advantage is that LaiFu makes many protocols already implemented by scapy to be fuzzable.

We are going to open source this tool to assist testers or developers to test their code and make protocol fuzzing easy and effective.


### [Lucky CAT: A Distributed Fuzzing Management Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Lucky CAT (Crash All the Things!) is a distributed fuzzing framework with an easy to use web interface. It allows management of fuzzing jobs on several remote machines concurrently. Lucky CAT aims to be easily usable, scaleable, extensible, and fun. To achieve this, it is built using several micro services and it relies on many open source projects. Furthermore, it offers a RESTful API to automate it or to integrate it with other tools.

Lucky CAT comes with several plugins for mutation engines (e.g. /dev/urandom, radamsa), fuzzers (afl, qemu_fuzzer, a minimalistic file fuzzer) and verifiers (local gdb exploitable, remote gdb exploitable). There are templates (in Python and C) that allow to quickly integrate, for example, new fuzzers and verifiers. Fuzzers can rely on their own mutation engine (e.g. afl) but Lucky CAT can also generate test cases for a fuzzer. This is handy when writing a fuzzer for an embedded device with limited computational resources or a small one-shot fuzzer for a custom protocol.

Its origin is the Nightmare Fuzzing Project. However, Lucky CAT goes beyond its ancestor. It is more 2018-ish using latest technologies such as RabbitMQ, Flask, MongoDB, and Python3. Lucky CAT's main objective is to automate the fuzzing process as far as possible so as to security researchers can focus on what they can best: identifying attack surfaces or writing custom fuzzers.
Therefore, future releases will focus on, amongst others, automatic deployment of fuzzers, crash notification and job summaries via email and instant messaging, and kernel core dump analysis.

Presentation: https://net.cs.uni-bonn.de/fileadmin/ag/martini/Staff/thomas_barabosch/blackhat-eu18-arsenal.pdf
Source Code: https://github.com/fkie-cad/LuckyCAT


### [MI-X (Am I Exploitable?).](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
‘Am I Exploitable?’, is an open source tool aimed at effectively determining whether a local host or a running container image is truly vulnerable to a specific vulnerability by accounting for all factors which affect *actual* exploitability. The tool prints the logical steps it takes in order to reach a decision and can generate a flow chart depicting the complete logical flow.

The first critical step to address any security vulnerability is to verify whether or not your environment is affected. Even if a vulnerable package is installed on your system, this condition alone does not determine exploitability as several conditions must be in place in order for the vulnerability to be applicable (exploitable). For example, can the vulnerability only be exploited under a specific configuration or in a specific OS?.

Most conventional vulnerability scanners rely on package manager metadata in order to determine the installed components (and in which versions) and then cross reference this data with vulnerability advisories in order to determine what vulnerabilities affect the system. The problem with that is that often software may be deployed without a package manager. For example, software might be built from source and then added to an image or unzipped from a tarball to a specific location on the file system. In these cases, no package manager data is associated with the application, which can result in false negatives (a scanner will “miss” these vulnerabilities) and offer a false sense of security.

We aim to build a community of researchers that can improve the validation process of historically dangerous vulnerabilities, as well as newly discovered ones, so users and organizations will understand whether they are vulnerable or not, as well as which validation flow is used to reach that verdict, and what steps are necessary for remediation or mitigation.


### [MI-X - Am I Exploitable?](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
None


### [Magpie: An Open Source CSPM Built to Scale](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
None


### [MetaHub: Automating Ownership, Context and Impact Assessments in Security Findings](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Security findings from automated sources such as CSPMs, software vulnerability scanners, or compliance scanners often overwhelm security teams with excessive, generic, context-less information. You may have heard countless times that context in security is key, so why don't these tools provide you with more of it? Simply put, they were not designed to do so.

This shortcoming means that determining ownership and impact can be time-consuming, leading to critical vulnerabilities going unnoticed, and causing unnecessary noise or friction between security teams and other departments.

My proposed demo introduces MetaHub, a tool designed to address these issues by automating the three essential stages of security finding assessment: owner determination, contextualization, and impact definition. Leveraging metadata through MetaChecks, MetaTags, MetaTrails, and MetaAccount, MetaHub provides a detailed, context-aware assessment of each finding.

By integrating MetaHub, teams can significantly reduce false positives, streamline the detection and resolution of security findings, and strategically tailor their scanner selection to minimize unnecessary noise. The ability to concentrate on meaningful, high-impact issues will be the primary focus of the demo.

MetaHub relies on the ASFF format for ingesting security findings and can consume data from AWS Security Hub or any ASFF-supported scanner like Prowler, ElectricEye, or Inspector. This compatibility means you can continue using the scanners you already rely on but add what's missing to those findings: Ownership, Context, and Impact.

MetaHub also generates powerful visual reports and is designed for use as a CLI tool or within automated workflows, such as AWS Security Hub custom actions or AWS Lambda functions.

The automation of context, ownership, and impact is not commonly addressed by open-source tools; MetaHub introduces a solution to this problem that aims to be agnostic to the source scanner.


### [Nightingale: Docker for Pentesters](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Have you ever been encounter where you configured the security virtual envieonment in the virtualbox and after someday the VM got crashed. All your configuration, tool setup, important information about the taget, POC's and what not, all will be gone and you can't recover the same.

With the same problem, I created the Nightingale based on the docker technology which provides you the exact security environment where you can expreicne the tools which a pentesters required at the time of pentesting. Adding to this, you no need to worry about your data, configuration and all other important. Nightingale will automatically restore the configuration once the new container will be up.


### [OpenSecDevOps (OSDO)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Join us to easily build a fortified software development lifecycle (SDLC) using open source tools. Find out how these powerful resources can improve the security of your software applications and improve your development process. We'll explore popular open source tools like Gitlab, Harbor, defectdojo... Seamlessly integrating them into your workflow to enforce strong security policies, detect vulnerabilities, and ensure compliance with industry best practices. Through hands-on exercises and real-world examples, you'll learn how to mitigate security risks, harden your code, and adopt security best practices, resulting in secure, scalable, and resilient software applications. Don't miss this transformative opportunity to unlock the potential of open source tools in your SDLC and strengthen your organization's overall security posture. All the information will be published on opensecdevops.com for the community to use and improve on the day of the presentation, in addition to integrating the different tools, an app will be shown to facilitate said integration according to your needs.


### [POWERSAP: POWERSHELL TOOL TO ASSESS SAP SECURITY](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Most companies, small or big, use SAP technologies to work. Many of them provide access to their SAP environments through Citrix. Indeed, supplier or subcontractors need to reach SAP environment, from back office to boardroom, warehouse to storefront, desktop to mobile device; users can quickly and 'securely' access SAP enterprise application software with Citrix virtualization without exposing their SAP landscape to Internet.

To pentest SAP system required some knowledge of this technologies and some hacking tool. Unfortunately, lots of SAP hacking tools are not maintained anymore and dependencies are required like RFC SDK to work. When it comes to assess/pentest the security of SAP landscape from Citrix, no tool is freely available and it is not allow or possible to install third softwares or dependencies.

We present a compilation of powershell script to assess SAP, which try to answer to this problematic of dependencies and use from Citrix environment. The presentation will start by describing the issues around SAP hacking tools, then we will continue by explaining the restrictions meet to pentest from Citrix system. And then we will present in detail the tool developed to solve the issues meet and of course with some demos.


### [Patronus: Swiss Army Knife SAST Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Patronus is a fully dockerised and comprehensive config driven Security Framework which helps to detect security vulnerabilities in the Software Development Life Cycle of any application. The framework inculcates a highly automated approach for vulnerability identification and management. With Patronus's fully whitebox approach, the framework currently covers four major verticals; Secrets Scanning, Software Composition Analysis, Static Application Security Testing and Asset Inventory. Finding all these four verticals together is a very strenuous task in the industry as no other framework currently solves this like Patronus which provides a fully comprehensive dashboard containing all the four verticals in a single central platform, and this is something very unique to Patronus. Patronus automatically identifies the latest code commits and focuses on the major aspects of the application source code to identify and detect key and high severity vulnerabilities within the application and aims for minimal false positives in the reports.

The framework focuses on the needs of the security engineers and the developers alike with a dedicated web dashboard to abstract all the nitty gritty technicalities of the security vulnerabilities detected and also empowers the user with higher level of vulnerability tracking for better patch management. The dashboard is built completely with analytics, functionality and maintaining ease in mind to demonstrate and display various metrics for the scans and vulnerabilities. It also helps to search, analyse and resolve vulnerabilities on-the-go and provides a completely consolidated vulnerability report.

Patronus is very powerful and hugely reduces the time and efforts of the security team in thoroughly reviewing any application from a security lens. The framework comes with an on-demand scanning feature apart from the scheduled daily automated scans, using which developers and security engineers can scan particular branches and repositories at any point of time in the SDLC, directly from the dashboard or integrations like Slack. The framework is completely adaptable and various softwares like Slack and Jira can be easily integrated directly with Patronus for better accessibility and tracking since most organisations today use these extensively.


### [PingCastle: An Active Directory Auditing Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
So many tools that exist to assess Active Directory security, and yet, it is impossible to have an overview of all. PingCastle has been designed to tackle these difficulties and get results fast and without any requirements. Healthcheck mode is the most well-known mode that gives vulnerability reports in minutes regarding major AD vulnerabilities. But what if the most important point was to convince the management that AD security is not that simple? PingCastle is more than a vulnerability scanner. This demo will include scanners, cartography and secret tricks.


### [PingCastle: An Active Directory Security Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
So many tools that exist to assess Active Directory security, and yet, it is impossible to have an overview of all. PingCastle has been designed to tackle these difficulties and get results fast and without any requirements. Healthcheck mode is the most well-known mode that gives vulnerability reports in minutes regarding major AD vulnerabilities. But what if the most important point was to convince the management that AD security is not that simple? PingCastle is more than a vulnerability scanner. This demo will include scanners, cartography and secret tricks.


### [Principal Mapper (PMapper): A Tool for Identifying Unique AWS Account/Organization Permissions Risks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
None


### [Prowler v3 the handy multi-cloud security tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
None


### [Prowler, Open Source for Multi-Cloud Security Assessments and Pentesting](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Whether you use AWS, Azure or Google Cloud, Prowler helps to assess, audit, pentest and harden your cloud infrastructure configuration and resources.


### [Prowler: Cloud Security Assessment, Auditing, Hardening, Compliance and Forensics Readiness Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Prowler helps to assess, audit and harden your AWS account configuration and resources. It also helps to check your configuration with CIS recommendations, and check if your cloud infrastructure is GDPR compliance or if you are ready for a proper forensic investigation. It is a command line tool that provides direct and clear information about configuration status related to security of a given AWS account, it performs more than 80 checks.


### [Responding to Microsoft 365 Security Reviews Faster with Monkey365](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Monkey 365 is a multi-threaded plugin-based tool to help assess the security posture of not only Microsoft 365, but also Azure subscriptions and Azure Active Directory. It contains multiple controls and currently supports CIS 1.4/1.5, HIPAA, GDPR, as well as custom security rules.


### [Scout Suite: A Multi-Cloud Security Auditing Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Scout Suite (https://github.com/nccgroup/ScoutSuite) is an open source multi-cloud security-auditing tool, which enables security posture assessment of cloud environments. Using the APIs exposed by cloud providers, Scout Suite gathers configuration data for manual inspection and highlights risk areas. Rather than going through dozens of pages on the web consoles, Scout Suite presents a clear view of the attack surface automatically.

The following cloud providers are currently supported:

Amazon Web Services
Microsoft Azure
Google Cloud Platform

During the presentation, we will run Scout Suite against a number of cloud environments preconfigured with typical flaws. We will display how Scout Suite can be used to identify and help with remediation of security misconfigurations.

We will also release support for a number of new cloud providers (Oracle Cloud Infrastructure, Alibaba Cloud & IBM Cloud), and demonstrate how Scout Suite's cloud-agnostic architecture allows for great extensibility.

Presentation Slides: https://github.com/nccgroup/ScoutSuite/files/3502099/BH.Arsenal.2019.Scout.Suite.pdf


### [SERPICO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
SERPICO is a simple and intuitive report generation and collaboration tool; the primary function is to cut down on the amount of time it takes to write a penetration testing report. Serpico was built by penetration testers with a pen-testers methodology in mind. Our goal is to save you time and improve your reporting process.

We are excited to be back at Arsenal!! We have a large release of Serpico planned with some exciting features to show off including plug-ins to simplify your life, more reports to choose from, shiny UI improvements, and better scoring. It might make you hate report writing just a little bit less.


### [SimpleRisk GRC](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk, via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform risk management activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to submit risks, plan mitigations, facilitate management reviews, prioritize for project planning, and track regular reviews. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.


### [SimpleRisk](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform organizational Governance, Risk Management, and Compliance activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to manage control frameworks, policies, and exceptions, facilitate audits, and perform risk prioritization and mitigation activities. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.


### [SimpleRisk: ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk, via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform risk management activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to submit risks, plan mitigations, facilitate management reviews, prioritize for project planning, and track regular reviews. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.

Source Code: https://github.com/simplerisk


### [SimpleRisk: Governance, Risk Management & Compliance](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform organizational Governance, Risk Management, and Compliance activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to manage control frameworks, policies, and exceptions, facilitate audits, and perform risk prioritization and mitigation activities. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.


### [SupplyShield: Protecting your software supply chain](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
SupplyShield is a comprehensive supply chain security framework aimed at defending against the increasingly sophisticated attacks posed by software supply chain vulnerabilities. With numerous organizations hosting hundreds of micro-services and thousands of builds occurring daily, effectively monitoring the software supply chain to construct the final application becomes a complex challenge. This is where SupplyShield can assist any organization in seamlessly integrating this framework into their Software Development Lifecycle (SDLC) to ensure software supply chain security.

The current framework version is predominantly designed for the AWS environment. Any organization utilizing AWS infrastructure can seamlessly implement this framework with minimal effort via AWS CloudFormation templates to enhance the security of their supply chain. The framework mainly focuses on generating and maintaining a Software Bill of Materials (SBOM) and performing Software Composition Analysis (SCA) for all the micro-services within an organization. The scans are event-driven, targeting the final micro-service image pushed into AWS ECR. As a result, it generates an SBOM of base image binaries and 3rd-party packages introduced by developers, and performs SCA on top of that. This approach provides a comprehensive view of the software components involved in the overall development of a micro service.

Built with scalability in mind, SupplyShield is capable of generating an SBOM and performing SCA in a CI/CD environment where thousands of builds take place daily. SupplyShield enables the rapid detection of zero-day vulnerabilities, such as the log4j exploit, even for organizations with over 100 micro-services, significantly reducing the Mean Time To Detect (MTTD) to mere minutes. This significantly simplifies the tasks of both security engineers and developers in identifying and managing patches for events like the log4j vulnerability. The framework also offers a dashboard for developers and security engineers, presenting relevant metrics and actionable insights.


### [TMoC: Threat Modeler on Chain](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
None


### [TROMMEL - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
TROMMEL is a custom, open-source tool using Python to assist researchers during embedded device vulnerability analysis. TROMMEL sifts through embedded device files to identify potential vulnerable indicators. TROMMEL has also integrated vFeed Community Database which allows for further in-depth vulnerability analysis of identified indicators.

Source Code: https://github.com/CERTCC/trommel


### [TROMMEL: Sift Through Embedded Device Files to Identify Potential Vulnerable Indicators](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
TROMMEL sifts through embedded device files to identify potential vulnerable indicators. Specifically, TROMMEL identifies the following indicators:

Secure Shell (SSH) key files
Secure Socket Layer (SSL) key files
Internet Protocol (IP) addresses
Uniform Resource Locators (URLs)
Email addresses
Shell scripts
Web server binaries
Configuration files
Database files
Specific binaries files (for example, Dropbear, BusyBox, and others)
Shared object library files
Web application scripting variables

Android application package (APK) file permissions

TROMMEL integrates vFeed, to provide a custom intersection with Exploit-DB, Metasploit, Snort, and Nmap. This integration allows for further in-depth vulnerability analysis of identified indicators. All in all, TROMMEL significantly lessens the manual analysis time of the researcher by automating much of the vulnerability discovery and analysis process.


### [TaintedLove: Dynamic Security Analysis Tool for Ruby](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
TaintedLove is a dynamic security analysis tool for Ruby. It leverages Ruby's object tainting and monkey patching features to identify potentially vulnerable code paths at runtime. TaintedLove is library agnostic and provides a simple framework to extend the detection of unsafe method usage and user input tracking.


### [The Vulnerability Complete Definition Library](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
More and more security researchers treat source code as a database and use code patterns to search or query potential vulnerabilities. At the Black Hat 2021 USA conference, the 360 ​​Alpha Lab team disclosed how to use code patterns to find 11 CVEs on Chrome, and developed a 0day exploit based on this. The code pattern is essentially a set of conditions for the code, and the code that satisfies certain conditions is very likely to have vulnerabilities. However, the industry does not seem to have a publicly available tool that can accurately describe or define the necessary and sufficient conditions for a specific vulnerability. Although CodeQL (https://securitylab.github.com/tools/codeql/) is already trying to convert the vulnerability described in natural language in Common Weakness Enumeration (https://cwe.mitre.org/) into query sentences , But most of its query conditions are sufficient and non-essential conditions to form a specific vulnerability, that is, it does not include all the circumstances that form this vulnerability. These query sentences avoid the conditions that CodeQL is difficult to process or describe to improve the success rate of the query. And I personally think that the grammatical rules of SQL often cannot intuitively describe the constraints of the code and the code running process, and a large number of built-in query processes also make the learning cost higher.

Therefore, I have developed a complete definition library for vulnerabilities and believe that this library has two main advantages. First, this library can describe constraints with syntax, design ideas, and keywords similar to the code used by developers, which makes this tool have a lower learning cost. Second, this library is designed to describe the necessary and sufficient conditions for the formation of vulnerabilities. The necessary and sufficient conditions here is used to describe all possible situations that form the vulnerabilities. We should not artificially modify the search conditions to make it easier for the algorithm of the search program to search for results, but should let the search algorithm determine by itself how to search can speed up the display of results.

This library is developed based on LLVM's AST (Abstract Syntax Tree) and the constraint solver STP (Simple Theorem Prover), and supports the description of constraints on objects such as control flow, data flow, value size, variable relations, variable types, variable names, etc. The library will also contain a batch of vulnerability definitions I wrote and a simple search algorithm. I will use a simple example to demonstrate how the algorithm finds a vulnerability in a specific situation based on the vulnerability definition. All source code will be hosted on github, you can download and study by yourself.


### [The WiFi Kraken Lite](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
None


### [USB Controlled Stress Test Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Windows anti-forensics USB monitoring tool for stress test.


### [Unleash Purple Knight: Fend Off Invaders Lurking in Your Active Directory](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Purple Knight is a free Active Directory (AD) and Azure AD security assessment tool developed by Semperis identity security experts that has been downloaded by 5,000+ users since its first release in spring 2021. Purple Knight runs as a standalone utility that queries the AD environment and performs a set of tests against many aspects of AD's security posture, including AD Delegation, account security, AD Infrastructure security, Group Policy security, and Kerberos security. The tool scans for indicators of exposure (IOEs) and indicators of compromise (IOCs). Each security indicator is mapped to security frameworks such as MITRE ATT&CK and the French National Agency for the Security of Information Systems (ANSII).

Purple Knight produces a report that includes an overall score, scores in individual categories, and prioritized guidance from identity security experts that serves as a roadmap for improving overall security posture. The report includes an explanation of what aspects of the indicator were evaluated and the likelihood that the exposure will compromise AD.

Purple Knight is continuously updated to address new security indicators based on original research and in response to emerging threats. As an example, the Purple Knight team released indicators for the Windows Print Spooler service and PetitPotam flaws within days after their discovery. New updates to be demonstrated at Arsenal include:
• Newest in the 100+ indicators of exposure (IOEs) and indicators of compromise (IOCs)
• New Azure Active Directory security indicators
• Post-breach forensics capabilities that enable incident response teams to specify an attack window to accelerate remediation

Purple Knight continuously evolves through feedback from an engaged community of users on the Purple Knight Slack channel and through individual outreach to users who communicate directly with the product teams.


### [V2X Validation Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
The V2X Validation Tool (called dsrcvt because focused on DSRC technology) facilitates penetration testing on automotive On-Board Units (OBUs) used for Vehicle-to-X communication. Currently, dsrcvt is capable of sending unsigned or signed Basic Safety Messages (BSMs) by re-signing a recorded BSM sent for automotive onboard units. Using these BSMs it tries to cause a surge in an OBU's processing power. It also attempts to bypass the security checks posed by the IEEE 1609.2 security layer. An enhanced version of dsrcvt (dsrcvt-crafter) facilitates crafting entirely custom BSMs from scratch, conforming to the IEEE 1609 standards family. dsrcvt also comes as an OBU fuzzer that can fuzz user-selected fields of a BSM to pen-test OBU implementations.


### [Vulmap: Online Local Vulnerability Scanners Project](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Vulmap is an open source online local vulnerability scanner project. It consists of online local vulnerability scanning scripts for Windows and Linux. These scripts can be used for defensive and offensive purposes. It is possible to conduct vulnerability assessments by using these scripts. Also they can be used for privilege escalation by pentesters/red teamers. Vulmap scans vulnerabilities on localhost, shows related exploits and downloads them. It basically, scan localhost to gather installed software information and ask Vulmon API if there are any vulnerabilities and exploits related with installed software. If any vulnerability exists, Vulmap shows CVE ID, risk score, vulnerability's detail link, exploit ids and exploit titles. Exploits can be downloaded with Vulmap also. Main idea of Vulmap is getting real-time vulnerability data from Vulmon instead of relying of a local vulnerability database. Even the most recent vulnerabilities can be detected with this approach. Also its exploit download feature helps privilege escalation process. Since most Linux installations have Python, Vulmap Linux is developed with Python while Vulmap Windows is developed with PowerShell to make it easy to run it on most Windows versions without any installation.


### [Vuls: Agent-less Vulnerability Scanner for Linux, FreeBSD, Container Image, Running Container, WordPress, Application Libraries, and Network Devices](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Over 10,000 new vulnerabilities are registered on the NVD each year. Constantly monitoring new vulnerabilities and keeping a manual inventory of installed software to determine which devices are affected is necessary. Without automation, vulnerability lifecycle managed imposes huge burdens and challenges.

Having personally experienced these challenges, Kota Kanbe created Vuls, an open source vulnerability scanner for Linux and FreeBSD [https://github.com/future-architect/vuls].

With users worldwide, Vuls has over 7,000 GitHub stars and is the highest-ranked security-tool https://github.com/topics/security-tools

Vuls lets you know which servers and software are affected by newly disclosed vulnerabilities. Using multiple detection methods and data sources including changelog, Package Manager, NVD and OVAL, Vuls is more accurate than other open source scanners.

Additionally, using CPE offers a wide detection range. Vuls not only detects vulnerabilities in OS packages but also in non-OS packages such as libraries for programming languages and network devices. https://vuls.io/docs/en/usage-scan-non-os-packages.html Wordpress vulnerability scanning(core, plugins, themes) is also supported. Scan WordPress ... https://vuls.io/docs/en/usage-scan-wordpress.html

Another important feature is the speed; by using parallel processing, numerous servers can be scanned at high speeds with most scans completed within 10 seconds.

Vuls supports major distributions of Linux and FreeBSD as well as containers such as Docker, LXC and LXD.

Vuls is extremely easy to set up since it connects to other servers via SSH for the scans. Of course, it can also be used to scan servers locally without SSH.

Vuls is a Dynamic Scanner which logs in running servers. This means that it's possible to acquire the useful state of the server for system administrators. For instance, Vuls will let you know if there are processes affected by an update and when daemons forgot to perform a restart after the update.

With non-intrusive scans, Vuls works well with Continuous Integration and can help find vulnerabilities very quickly by conducting scans every day.

How can a system administrator automate vulnerability lifecycle management?


### [Wabhawk/Catch - Unsupervised Machine Learning Detection](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Webhawk/Catch helps automatically finding web attack traces in HTTP logs without using any preset rules. Based on the usage of Unsupervised Machine Learning, Catch groups log lines into clusters, and detects the outliers that it considers as potentially attack traces. The tool takes as input a raw HTTP log file (Apache, Nginx..) and returns a report with a list of findings.

Catch uses PCA (Principal Component Analysis) technique to select the most relevant features (Example: user-agent, IP address, number of transmitted parameters, etc.. ). Then, it runs DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm to get all the possible log line clusters and anomalous points (potential attack traces).

Advanced users can fine tune Catch based on a set of options that help optimising the clustering algorithm (Example: minimum number of points by cluster, or the maximum distance between two points within the same cluster).

The current version of Webhawk/Catch generates an easy-to-read HTML report which includes all the findings, and the severity of each one.


### [Zelos: Applying Emulation to Cross Architecture Root Cause Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Zelos (Zeropoint Emulated Lightweight Operating System) is a python-based binary emulation platform that omits the cumbersome setup of virtual machines, yet provides instrumentation capabilities missing in user-space emulation. While it is built on top of the QEMU powered Unicorn CPU emulator, Zelos provides the operating system details required to fully emulate binary execution from loading, down to system calls. We quickly found use for Zelos as a dynamic instrumentation tool that could unpack malware, categorize and report malicious behavior, as well as extract domains from Domain Generation Algorithms (DGA). The myriad of uses we uncovered drove us to develop a plugin system to encourage extensions.

In this demo, in addition to highlighting Zelos's core dynamic analysis features, we'll showcase a new plugin released at BlackHat which provides automated root cause analysis (RCA), a method of identifying causes of crashes, through data flow analysis. Applications of automated RCA range from helping developers locate and fix bugs to triaging crashes generated through fuzzing. Existing techniques for identifying root cause through data flow analysis may require recompilation of binaries to insert instrumentation, integration of multiple tools, or collecting execution traces. Using Zelos, identifying the root cause can be as simple as providing the binary with the crashing input. We will highlight how we perform architecture agnostic dataflow analysis by utilizing QEMU's internal assembly code representation and show how easy RCA can be, even without source code.


### [boofuzz](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
boofuzz is an open-source network protocol fuzzing framework, competing with closed source commercial products like Defensics and Peach. Inheriting from the open source tools Spike and Sulley, boofuzz improves on a long line of block-based fuzzing frameworks.

The fuzzing framework allows hackers to specify protocol formats, and boofuzz does the heavy lifting of generating mutations specific to the format. boofuzz makes developing protocol-specific "smart" fuzzers relatively easy. Make no mistake, designing a smart network protocol fuzzer is no trivial task, but boofuzz provides a solid foundation for producing quality fuzzers.

Written in Python, boofuzz builds on its predecessor, Sulley, with key features including:

Online documentation
More extensibility including support for arbitrary communications mediums
Built-in support for serial fuzzing, ethernet- and IP-layer, UDP broadcast
Much easier install experience!
Far fewer bugs

Source Code: https://github.com/jtpereyda/boofuzz


### [cwe_checker: Hunting Binary Code Vulnerabilities Across CPU Architectures](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
cwe_checker is an open source suite of tools to detect common bug classes like Use After Free (CWE-416) or Null Pointer Dereference (CWE-476). These bug classes are formally known as Common Weakness Enumerations (CWEs). Its main goal is to quickly point analysts to vulnerable code paths in binaries (e.g. firmware) without access to the source code.

cwe_checker is built on top of the Binary Analysis Platform (BAP). By using an intermediate representation for the binary code it can analyze ELF binaries of different CPU architectures, including x86/64, ARM, MIPS, and PPC. It has a modular and extensible architecture implementing static and dynamic analysis techniques. So far cwe_checker implements checks for more than 15 CWE classes including CWE-190 (Integer Overflow), CWE-415 (Double Free), and CWE- 676 (Use of Potentially Dangerous Function).

In addition, cwe_checker has been adopted as a core plugin for the Firmware Analysis & Comparison Tool (FACT). This enables analysts to hunt for vulnerabilities in large firmware data sets. Furthermore, the results of cwe_checker are exportable and there is an IDA Pro plugin that highlights any findings in the binary.


### [kdigger: A Context Discovery Tool for Kubernetes Penetration Testing](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
None


### [macOS Bluetooth Analysis Suite (mBAS)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
mBAS is a set of Bluetooth tools for macOS platforms, including Bluetooth HCI request sniffer, fuzzer and Broadcom firmware SoC tools, etc. Among them, the HCI fuzzer helped me discover many Bluetooth kernel vulnerabilities, such as CVE-2020-3892, CVE-2020-3893, CVE-2020-3905, CVE-2020-3907, CVE-2020-3908 and CVE-2020-3912. With these tools, we can better understand the design and implementation of Bluetooth subsystem of macOS and other platforms.


### [remote-method-guesser: A Java RMI Vulnerability Scanner](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
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


### [trapfuzzer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--AppSec](https://img.shields.io/badge/Category-Red--Teaming--/--AppSec-gray)  
Breakpoint mechanism based coverage-guided binary fuzzing tools for Windows and Linux platforms.

Binary instrument by breakpoint, in specific scenarios, this method is faster than dynamorio.

At present, more than 200 vulnerabilities have been found in WPS office, foxitpdf and other software


---

## Miscellaneous / Lab Tools


### [AI Risky Business: Hands-on AI Payload Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [ARSENAL LAB - Applied Hardware Attacks: Prototyping Malicious Hardware on the Cheap](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [ARSENAL LAB - ICU-ICS: An ICS Assessment Framework Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [ARSENAL LAB - JTAGulator: Assisted Discovery of On-Chip Debug Interfaces](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
For over five years, the JTAGulator has been the de facto open source tool for identifying interfaces commonly used for hardware hacking, such as JTAG and UART, from a target product's test points, vias, component pads, or connectors. The tool bridges the gap between gaining physical access to circuitry and exploiting it, and can save a significant amount of effort compared to traditional reverse engineering processes. For the first time at Black Hat Arsenal, attendees will have the opportunity to play with the JTAGulator and a variety of real-world embedded devices in an informal, hands-on environment.


### [ARSENAL LAB - ZigBee Hacking: Smarter Home Invasion with ZigDiggity](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Cluster Fuzz, Introduction to Car Hacking With Real Car Hardware](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Deepfake Detection with Faceless](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Dialing Home: ATM Protocol Reversing](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Disrupting OT and IoT by Exploiting TCP/IP Stacks](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Drone Remote ID Spoofer and Low Cost Receiver Application](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Drone Threats and Countermeasures](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Exploiting & Securing Trains](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Hacking the Digital Drone License Plate](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Hands-on Firmware Extraction, Exploiration, and Emulation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Hands-on RF Hacking 101: From Waveforms to System Takeover](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Hands-on RF Hacking: Your Table is (always) Ready](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Hands-on RFID: Sniff it, crack it, clone it](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Hands-on Security Analysis of Selected Avionics Systems Using the Triton Testbed](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Industrial Control Systems: Capture the Train!](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [JTAGulator: Assisted Discovery of On-Chip Debug Interfaces](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Mining for Secrets: Repos, firmware, and more](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Packet Carving for SATCOMs Hackers](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Practical IoT Hacking: Introduction to Multi-Band Hacking with the CatSniffer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Rapid Fire: Flipper vs. All the Things](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


### [Vehicle Control System](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Miscellaneous--/--Lab--Tools](https://img.shields.io/badge/Category-Miscellaneous--/--Lab--Tools-gray)  
None


---

## Web/AppSec or Red Teaming


### [APKHunt | OWASP MASVS Static Analyzer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
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


### [Analyzing SAP Communication Security: Introducing sncscan](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
SAP systems are used around the world to handle crucial business processes and highly confidential data such as financial details or information regarding a company's staff. To ensure confidentiality and integrity, sensitive data, and especially access credentials, must only be transmitted over encrypted communication channels. Transport layer encryption for SAP systems is provided by the Secure Network Communications (SNC) protocol. Currently, the configuration of the SAP SNC protocol (such as the Quality of Protection parameter or the installed CryptoLib) can only be audited with authenticated access to the SAP system or by manually connecting to the system through the SAP GUI. These approaches have additional requirements and are impractical for assessing the security of a larger number of systems.

To address the beforementioned issues, we developed 'sncscan', an SNC scanner, that works without authentication and similar to the various tools that are available to analyze the security of services that use SSL/TLS. To achieve this, 'sncscan' starts SNC handshakes with varying encryption parameters to the tested service and analyzes the returned error messages and responses. This is especially useful in context of professional penetration tests and enables us to identify configuration weaknesses and provide actionable recommendations on improving the transport security in SAP environments.

'sncscan' benefits from the tools and research of the `pysap` project and will be released as Open-Source tool in the OWASP CBAS-SAP project. It aims to enable security researchers, professional penetration testers and SAP basis administrators to verify the correct use of the SNC protocol.

Currently 'sncscan' can analyze the SNC configuration of the SAP Router protocol. The next steps are to implement similar functionality for the protocols DIAG and RFC to increase the coverage of SAP services.


### [AppsecStudy - open-source elearning management system for information security](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
AppsecStudy is an open-source platform for seminars, training, and organizing courses for practical information security for developers and IT specialists. This tool has all the built-in basic requirements needed for organizing normal and productive training.


### [Bugsy - Automated Vulnerability Remediation CLI](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Bugsy is a command-line interface (CLI) tool that provides automatic security vulnerability remediation for your code. It is a community edition version of Mobb, the first vendor-agnostic automatic security vulnerability remediation tool. Bugsy is designed to help developers easily identify and fix security vulnerabilities in their code.

When pointed at an open-source repo, Bugsy will automatically scan the repo using Snyk Code and produce fixes the developer can easily review and commit.


### [Build Inspector Open Source](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Build Inspector provides processing of plain-text CI/CD build and deployment logs with an eye towards identifying consumed and produced dependencies, along with identifying actions that introduce additional risk into the process. Quickly identify changes from one pipeline run to the next, and home in on spots where developers have added unnecessary risk or are performing actions that could be opportunities for a supply chain compromise.


### [CodeTotal: Shift Left Just Became Easier](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Looking for a powerful and easy-to-use open-source scanning tool? CodeTotal is your solution! CodeTotal is an online scanning tool aggregates multiple open-source scanning tools, providing free and lightning-fast code scanning.

But CodeTotal offers much more than just speed and convenience. Our unique tool also aggregates the data from these scans, enabling users to identify any security issues that their current scanning software may have missed. With CodeTotal, you can even verify alerts suspected to be possible false positives, getting a valuable second opinion that can help you stay ahead of any potential threats.

Tired of maintaining multiple tool environments for each repository? CodeTotal offers a simple and streamlined solution. No more wasting time setting up and maintaining 10 to 20 tool environments - CodeTotal takes care of everything for you. Our revolutionary tool allows developers to independently scan their code for security issues in minutes, freeing up valuable resources and avoiding the need for involvement or approval from R&D and DevOps.

But that's not all. CodeTotal also produces an SBOM, giving developers a detailed view of their code dependencies and ensuring that any licensing issues are immediately flagged. With CodeTotal, you can use open-source libraries confidently and with peace of mind.


### [Daksh SCRA (Source Code Review Assist Tool)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Daksh SCRA is an open source tool that assists with manual source code review by providing helpful information to the code reviewer. This tool differs from traditional code review tools because it aims to help reviewers collect various details about the code base and identify areas of interest to review and confirm potential vulnerabilities. Even if code reviewers use automated code review tools, there are still many manual tasks they must perform to confirm findings and ensure precision in the code review process.

Although there are numerous automated code review tools available, none of them can perform a reconnaissance of the code base and provide code reviewers with useful insights. Typically, code reviewers must search for relevant information to confirm findings or ensure precision. Daksh SCRA offers valuable information such as technology and platform usage, functionalities, use cases, vulnerable patterns, and libraries used, among other data.

While most code review tools search for vulnerable patterns, they often report a high percentage of false positives. Daksh SCRA, on the other hand, is designed to be a reconnaissance tool that provides code reviewers with maximum insights about the target code base to assist with precise code review. Although Daksh SCRA is in its infancy stage, it is still a usable tool that supports a wide range of languages and platforms, and new features will be added in future releases.


### [Defending GitHub Actions: Unmasking Attack Vectors and Verifying Integrity with eBPF](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
GitHub Actions has gained immense popularity as a powerful tool for software development and release. However, this popularity has also attracted bad actors, In this session, we will delve into the active risks that attackers leverage to abuse and attack GitHub Actions, shedding light on their techniques and exploits.
In response, we will show an OSS Runtime Security solution, which introduces the concept of profiling with eBPF the CI\CD runtime environment, we will demonstrated how it can prevent and alert on malicious behaviour, and create a build profile of the environment


### [Dependency Combobulator](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
None


### [DumpTheGit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
DumpTheGit searches through public repositories to find sensitive information uploaded to the Github repositories.


### [Electronegativity: Identify Misconfigurations and Security Anti-Patterns in Electron Applications](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Electronegativity is a tool to identify misconfigurations and security anti-patterns in Electron-based applications (electronjs.org).

This is the first and only tool capable of detecting potential weaknesses and implementation bugs when developing applications using Electron, as recommended in the official security guidelines of the Electron project. Software developers and security auditors can use this tool to create secure desktop applications using web technologies.

After being first introduced at Black Hat US 2017 (Electronegativity - A Study of Electron Security) and featured in Black Hat Asia 2019 (Preloading Insecurity In Your Electron), the tool will be showcased for the first time ever at the Black Hat USA 2019 Arsenal where we will demonstrate its potential by scanning well-known applications.

Come see live demonstrations of Electronegativity hunting Electron applications for vulnerabilities and walk away with an open-source (Apache 2.0) static analysis engine to help secure your Electron applications!


### [Find Security Bugs](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Find Security Bugs is a plugin for the Java static analysis tool SpotBugs. This plugin consists of set rules that focus only on security weaknesses. It can be used by developers or security professionals to find vulnerabilities in their code.

The plugin can identify weaknesses in Java web applications from 138 different bug patterns including XSS, SQL injection, XXE, template injection and many more. It can scan any JVM languages such as Kotlin, Scala and Groovy. The assessment can be done in an IDE, such as Eclipse, or IntelliJ. It can also be configured in a continuous integration environment.

The most recent additions to the project include features to the IDE integration and Continuous Integration (CI). The IDE IntelliJ integration was greatly improved to have better support for alternative languages such as Kotlin. This makes it easier to scan Android applications. IDE integration is a great perspective for code audit. For developers, continuous integration is a highly sought-after configuration. A new Github Action will be presented. It provides an easy feedback for developers when integrating code to the master branch with a pull request.

The Black Hat Arsenal's demonstrations will include a live code review where samples of vulnerability and practical methods will be showcased in the new IDE and CI environment.


### [KICS](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
KICS is an open-source solution for static code analysis of Infrastructure as Code. It finds security vulnerabilities, compliance issues, and infrastructure misconfigurations in the following Infrastructure as Code solutions: Terraform, Kubernetes, Docker, AWS CloudFormation, Ansible. And more to come. Over 1000 rules are already available.


### [KICS: Keeping Infrastructure-as-Code Secure](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Infrastructure as Code (IaC) makes deploying cloud or container configurations scalable and faster. If you are launching a microservice into a Kubernetes cluster, or even building an entire AWS virtual infrastructure, IaC can automate the deployment. By building repeatable templates you can also ensure that deployments happen exactly as you design, every time.

However, errors in infrastructure configuration are now regarded as the second biggest cause of data breaches. There are many ways to give adversaries an advantage through security misconfigurations. Overly permissive storage volumes, unauthenticated database access, or ports left open to the internet have all been a cause of compromise. The solution? Treat your infrastructure code the same as your application code. During your build process, use tools to scan for infrastructure misconfigurations. When you find them raise alerts or even break the build. 

In this session, we will discuss common types of IaC misconfigurations, and demonstrate a free, open source security tool that developers can build into their pipelines to help protect infrastructure from compromise.


### [Kubescape: Open-Source Kubernetes Security Single-Pane-of-Glass](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Kubescape (https://github.com/armosec/kubescape) is a K8s open-source tool that provides a multi-cloud K8s single pane of glass, including risk analysis, security compliance, RBAC visualizer, and image vulnerabilities scanning.
Kubescape scans K8s clusters, YAML files, and HELM charts, detecting misconfigurations according to multiple frameworks (such as the NSA-CISA, MITRE ATT&CK, and more), software vulnerabilities, and RBAC (role-based-access-control) violations at early stages of the CI/CD pipeline, calculates risk score instantly and shows risk trends over time.
It became one of the fastest-growing Kubernetes tools among developers due to its easy-to-use CLI interface, flexible output formats, and automated scanning capabilities, saving Kubernetes users and admins precious time, effort, and resources.
Kubescape integrates natively with other DevOps tools, including Jenkins, CircleCI, Github workflows, Prometheus, and Slack, and supports multi-cloud K8s deployments like EKS, GKE, and AKS.

in this session, we will reveal new capabilities and features for the first time


### [Kurukshetra: Playground for Interactive Security Learning](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Kurukshetra is a web framework that's developed with the aim of being the first open source framework which provides a solid foundation to host reasonably complex secure coding challenges where developers can learn secure coding practices in a hands-on manner. It is composed of two components, the backend framework written in PHP, which manages and leverages the underlying docker system to provide the secure sandbox for the challenge execution, and the frontend, which is a user facing web app providing all the necessary controls, for the admin to host and modify the challenges, and the user to execute and view the result of each of his input.

The Framework currently supports challenges written in 4 major languages including PHP, Python, NodeJS and Ruby.


### [OWASP Dependency-Check](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
With the number of critical vulnerabilities in FOSS libraries that have affected so many applications over the last few years - Software Composition Analysis is a critical component to maintaining the security of your custom application. From Struts to Spring to jackson-databind, etc. the list of libraries that have had vulnerabilities that lead to remote code execution in the applications using the libraries goes on and on. As does the list of sites that have been compromised by these vulnerabilities. OWASP dependency-check is an open source Software Composition Analysis tool that provides a solution the `OWASP Top 10 2017: A9 - Using Components with Known Vulnerabilities`.


### [Puma Scan](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Puma Scan provides real-time, continuous source code analysis for .NET applications with over 50 security-focused rules targeting insecure deserialization, injection, weak cryptography, cross-site request forgery, misconfiguration, and many more insecure coding patterns. Puma Scan displays vulnerabilities in Visual Studio as spell check errors and compiler warnings to prevent engineers from committing vulnerabilities into code repositories.

DevSecOps teams can use Puma Scan's command line interface to enable security scanning in continuous integration pipelines (e.g. Jenkins, TFS), monitor code for security issues, and verify security thresholds are met during each build.
Come see live demonstrations of the Puma hunting source code for vulnerabilities and walk away with an open-source (MPL v2.0) static analysis engine to help secure your .NET applications.


### [RIDE: Efficient Highly-Precise Systematic Automatic Bug Hunting in Android Systems](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Vulnerabilities in various android systems such as the AOSP and vendor-specific components directly impact user security & privacy and should be eliminated. Do we have a way to efficiently identify bugs in ready-to-ship phones conveniently and precisely? From a researcher perspective, vendor codes are mainly closed-source which means they cannot use open-source auditing tools and usually the only obtainable resource is phone firmware. From vendor QA and security team's perspective, the ability to perform a systematic vulnerability assessment directly on ready-to-ship phone images would also be much more useful and easier than maintaining complex dependency and version information on each model.

We come up with a framework named RIDE (Rom Intelligent Defect assEsment) that directly operates on factory images of major android systems such as AOSP, Samsung, Huawei, Xiaomi, Oppo etc, which discovered 40+ CVEs including critical and high severity level bugs in the vendors in less than one year. RIDE combines highly precise whole-program static taint analysis and dynamic blackbox binary fuzzing to pinpoint vulnerabilities in user-space code such as system apps, system services and bundled closed-source libraries. In this talk, we will share in detail about the system's design and architecture, including the whole-program static analysis algorithm and implementation with high precision and acceptable performance, and the blackbox fuzzing component which is fed by the information collected from previous static analysis. Also, we will share the detail and exploitation of several bugs found, which range from system-level arbitrary file read/write/code execution to RCE ones in AOSP and other major vendors etc.


### [Route Sixty-Sink: Connecting Application Inputs to Sinks Using Static Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Route Sixty-Sink is an open source static analysis tool that traces the flow of user input through any .NET binary and determines whether it is passed as an argument to a dangerous function call (a "sink"). Route Sixty-Sink does this using two main modules:

1. RouteFinder, which enumerates API routes in MVC-based and classic ASP page web applications.
2. SinkFinder, which takes an entry point and creates a call graph of all classes and method calls. Then, it queries strings, method calls, and class names for "sinks".

By tying these two pieces of functionality together, Route Sixty-Sink is able to quickly identify high fidelity vulnerabilities that would be difficult to discover using black box or manual static analysis approaches.

We have used Route Sixty-Sink to reveal and successfully exploit vulnerabilities including unsafe object deserialization, SQL injection, command injection, arbitrary file uploads and access, authorization bypasses, and more in both open-source and proprietary .NET applications.


### [SASTRI: Plug and Play VM for SAST/*Static Application Security Testing Realtime Integration*/](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Abiding by the new hot concept of "Secure By Design," SASTRI is project carved out of the experiences/struggles/conflicts of product security engineers. It is an in-house SAST capability (plug and play VM) we are proposing, to make security engineers' inputs more receivable and reachable to the product developers and the decision-makers - while making our products more and more secure. This will save a lot of security engineers' and DevOps experts' time when it coms to setting up and fine tuning the SAST tools.

Highlights of SASTRI are:

Open source (hence free to edit and reconfigure)
Presently capable of scanning Python, C, C++ programs
Almost zero understanding of security principles is required to "run" SASTRI. (For bug resolution, yes definitely a deep understanding is required)
Automated bug reporting
Email alert for the issues reported
Same email contains attachment of report where buggy code snippet is mentioned along with the exact position of bug
Easy to integrate approach

SASTRI is an effort towards making SAST tools available right at the time of unit testing of code, in an automated way. The reason being, in most of Agile flavors of development, security testing is done in the end of the sprint, leaving very little to no time for bug fixes. Also, the smaller time window for security testing results in "not so in depth security testing" and "superficial fixes."
However, on the other hand, introducing security testing right at the programming phase in SDLC, can help in:

Finding vulnerabilities which are easy to exploit but difficult to mitigate
Finding vulnerabilities which are present due to complicated execution paths
Finding vulnerabilities specific to insecure configuration
Setting up basic secure code development principles amongst developers (Trust me this is the trickiest task, as most of the Devs are super possessive about their code and coding styles.

Also, this effort can help reduce apprehensions of security engineers when uploading source code on some vendors server which they do not trust. The list of advantages is huge; we have tried generalize them to the least count possible.


### [SCoDA: Smart COntract Defender and Analyzer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
SCoDA (Smart Contract Defender and Analyzer) module in LAMMA tool, written in python for solidity based smart contract scanning. The tools is a unified and python ported version of various other scanners and vulnerabilities reported on Ethereum Platform.


### [SCodeScanner (SourceCodeScanner)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
None


### [SCodeScanner - An Open-Source Source-Code Scanner](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
SCodeScanner is a powerful tool for identifying vulnerabilities in source-code. It is designed to be easy to use and provides a range of features to help users quickly and accurately identify vulnerabilities with fewer false positives.

Some key features of SCodeScanner include:

- Support multiple languages: SCodeScanner is capable of scanning source code written in multiple languages such as JAVA, PHP and YAML. The most commonly used languages in web development.

- Relatively Less false positives: SCodeScanner includes flags that help to eliminate false positives and only report on vulnerabilities that are mostly confirmed to exist.

- Custom rules: SCodeScanner works with semgrep and allows users to create their own rules to scan for advanced patterns.

- Ability to track user input variables: SCodeScanner can identify instances where user input variables are defined in one file but used insecurely in another file for better coverage.

- Fast scanning: SCodeScanner's rules are designed to check for multiple vulnerabilities at once, which results in a faster scanning process.

- Integration: SCodeScanner can integrate with CI/CD pipelines and also pass results to bug-tracking services such as Jira and Slack, allowing users to easily share the results of their scans with their team.

- Scan mutltiple ways: It automatically download all git repo mentioned inside a txt file and start scan. Not only this but also support git, folder, file scans aswell.

Proof of results, SCodeScanner has already found 5 vulnerabilities in multiple Wordpress plugins and has been awarded following CVEs:

CVE-2022-1604
CVE-2022-1465
CVE-2022-1474
CVE-2022-1527
CVE-2022-1532

Overall, SCodeScanner is a valuable tool for any developer or security professional looking to identify vulnerabilities in their source-code before it is published in production. Its fast scanning, less false positives, and CI/CD pipeline integrations as well as bug-tracking services, make it a powerful tool for ensuring the security of your code.


### [SGXRay: Automated Vulnerability Finding in SGX Enclave Application](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
None


### [Scanning DNA to Detect Malicious Packages in Your Code](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
PackageDNA is an open-source tool, free and modular tool developed in Python3, that offers developers and researchers the ability to analyze code packages from different programming languages, in search of vulnerabilities in the code, the possible manipulations or spoofing of the package ('typosquatting'), identifying suspicious files, searching for strings in the code, among other data for analysis.

PackageDNA, enables threat intelligence analysis or code audits, which allow to detect attacks to the software supply chain, the vast majority of companies integrate third-party code in their developments, thus the need to have a suite such as PackageDNA that performs the analysis of all these external codes and delivers the results of the analysis in a standardized way.


### [Security Code Scan: Vulnerability Patterns Detector](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Security Code Scan is static code analysis tool for C# and VB.NET. It detects various security vulnerability patterns: SQL and XPath injections, Cross-Site Request Forgery (CSRF), XML eXternal Entity Injection (XXE), unsafe deserialization and many more...

It is available as Visual Studio extension (2015 and higher), but can be integrated into other editors, that support Roslyn analyzers. It is also available as NuGet package and can be integrated into continuous integration builds.


### [Semgrep: a code-aware grep for finding vulnerabilities and enforcing secure defaults](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Semgrep is a tool for easily detecting and preventing bugs and anti-patterns in your codebase. It combines the convenience of grep with the correctness of syntactical and semantic search.

Semgrep is fast (scans 100Ks LOC in seconds), supports multiple languages (JavaScript, Python, Golang, Java, C), and is easy to customize, so that users can create high value org-specific or project-specific checks without spending weeks learning a complicated DSL.

Semgrep works by parsing source code into an abstract syntax tree (AST), then allows users to supply patterns that fuzzily match the interesting code patterns. Because it's source code aware, its checks are higher signal than regexes (i.e., it's easy to match function calls, and not match text in comments, multi-line calls, or strings), but because it isn't doing interprocedural dataflow analysis, it doesn't take hours to run and won't make assumptions that result in hundreds of false positives requiring triage.

https://github.com/returntocorp/semgrep


### [The OWASP RAF: Static Application Security Testing Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
The OWASP Risk Assessment Framework consist of Static Application Security Testing and Risk Assessment tools. Even though there are many SAST tools available for testers, the compatibility and the environment setup process is complex. By using OWASP Risk Assessment Framework's Static Application Security Testing tool, testers will be able to analyze and review their code quality and vulnerabilities without any additional setup. OWASP Risk Assessment Framework can be integrated in the DevSecOps toolchain to help developers to write and produce secure code.

User Guide https://github.com/OWASP/RiskAssessmentFramework/blob/master/user-guide.md


### [TINTORERA: SOURCE CODE INTELLIGENCE](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Tintorera is a static analysis tool developed in Python that uses the GCC compiler to build C projects aiming to obtain intelligence from them. GCC offers a powerful plugin architecture that allows tapping into its internals, and static analysis tools can benefit from it to gather information of the source code while compiling.

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


### [npm-scan: An Extensible, Heuristic-Based Vulnerability Scanning Tool for Installed NPM Packages](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
An extensible, heuristic-based vulnerability scanning tool for installed npm packages.

Active heuristics-based scanning: quick and easy for anyone to use

Improves/enforces quality of open source coding


### [promptmap](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
Prompt injection is a type of security vulnerability that can be exploited to control the behavior of a ChatGPT instance. By injecting malicious prompts into the system, an attacker can force the ChatGPT instance to do unintended actions.

promptmap is a tool that automatically tests prompt injection attacks on ChatGPT instances. It analyzes your ChatGPT rules to understand its context and purpose. This understanding is used to generate creative attack prompts tailored for the target. promptmap then run a ChatGPT instance with the system prompts provided by you and sends attack prompts to it. It can determine whether the prompt injection attack was successful by checking the answer coming from your ChatGPT instance.


### [pytm: A Pythonic Framework for Threat Modeling](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Web/AppSec--or--Red--Teaming](https://img.shields.io/badge/Category-Web/AppSec--or--Red--Teaming-gray)  
pytm is a Pythonic framework for threat modeling. Developers can define their system in Python code as a collection of objects and annotate them with properties. Security practitioners can add threats to the "Threats" object (see https://github.com/izar/pytm/blob/master/pytm/threats.py). The logic lives in the "condition" of the "Threats" object, where members of target can be logically evaluated. If the "condition" returns a "True", that means the rule found a potential threat. More details at https://github.com/izar/pytm

Usage:
tm.py [-h] [--debug] [--resolve] [--dfd] [--report] [--all]
[--exclude EXCLUDE] [--seq]

optional arguments:
-h, --help show this help message and exit
--debug print debug messages
--resolve identify threats
--dfd output DFD (default)
--report output report
--all output everything
--exclude EXCLUDE specify threat IDs to be ignored
--seq output sequential diagram


---

## Reverse Engineering


### [APKiD: Fast Identification of Mobile RASP SDKs](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
APKiD is like "PEiD" for Android applications. It gives information on how an APK was built by fingerprinting compilers, packers, obfuscators, and protectors. The main idea behind the tool is to help provide context on how the APK was potentially built or changed after it was built. This is all context useful for attributing authorship and finding patterns.

Extracting information about how the APK was made, it can provide a lot of information to assess the healthiness of an Android application (e.g. malware or pirated). The framework is the combination of a bunch of Yara rules and Python wrappers that scan files within APKs. Mainly, APKiD unpacks files and explores AndroidManifest.xml, DEX and ELF files to match rules and offers results based on them.


### [BINGREP](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
We created a new tool for static malware analysis. Incident response is important and analysts must analyze malware promptly, but the cost of static analysis is too expensive. For effective analysis we sometimes reuse malware that was analyzed before. "BinDiff" is the most famous tool created by H. Flake that outputs "Diff" of functions between two malware. This outputs good results, but it can output only one result per function. So, we created "BinGrep" that outputs functions in order of similarity by searching resemble malware functions. This "Grep" tool is useful in malware analysis because malware analysts are interested in specific functions.


### [Bringing the X86 Complete RE Experience to Smart Contract](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Currently there is more than 2 Trillion USD market cap for the crypto currency market, DeFi alone is more than 100 Billion. With the popularity of the DeFi market, smart contracts again become the playground of hackers and security researchers. Token "robbery" became the most problematic issue for both investors and crypto currency exchange.

Ethereum Virtual Machine (EVM) is still the most widely used architect to support the core of smart contracts such as Polkadot, EVM and soon Cardano blockchain. Emulators built around EVM are merely good for development purposes. Most of the EVM analysis engines are just debugging tools based on symbolic execution. Unfortunately, these engines are just simple tools that do not encourage and support us to develop tools on top of them.

During Black Hat Asia, Arsenal 2021, we presented "Qiling: Smart Analysis for Smart Contract" [1] and explained the foundation of Qiling's EVM engine. In Blackhat USA Arsenal 2021, we would like to take this opportunity to demonstrate the full capabilities and tools that we build on top of the Qiling's EVM engine. That brings the complete traditional X86 reverse engineering experience to the smart contract space.

- Real time EVM debugger, with step into, step over and memory stack modification capabilities
- Full emulation of multi cross contract instrumentation
- Ultra fast emulation with pre-set environment variable
- Fully automated reapply and verify latest smart contract attack to all existing contract on a exchange or chain
- Make symbolic execution to work with Qiling EVM engine to provide a more in depth emulation
- Added a fully functional LLVM Intermediate Representation(IR). It allow a users to build a ultra fast fuzzer on-top of Qiling Framework.

To demonstrate the power of our framework and tools. We prepared some case study and demo on how we can rebuild the entire blockchain and verify the currently existing smart contract against the latest attack being discovered in the wild in the matters on few lines of code.

Once the talk ends, we will release the code and tools into the Qiling github repo, as usual.

References:

[1] Black Hat Arsenal 2021: https://www.blackhat.com/asia-21/arsenal/schedule/index.html#qiling-smart-analysis-for-smart-contract-22643


### [CAN-PICK - A VISUALIZATION TOOL FOR EVALUATING CAN-BUS CYBERSECURITY - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
With the development of automotive technology, vehicles become more electronic and intelligent on the basis of inner bus communication network, and they draw more attention to the study of automotive cybersecurity. To facilitate this process, we developed a tool that evaluates the cybersecurity of the CAN-bus, which can be used for black-box tests by security researchers and automotive engineers.

This tool is capable of sniffing CAN-bus packets, analyzing UDS, as well as launching fuzzing attacks, and brute-force attacks. Fuzzing attack has two modes; we can combine id with data or single one to fuzz CAN-bus packet. By visualizing the changes from different packets, it can help us to identify id and value range related with function quickly. And we can easily find out which data is encrypted, so that it’ll more convenient to guess encrypt algorithm. Users can also share their programmable examples within the tool. This talk will introduce the reverse engineering of CAN-bus and present the "CAN-Pick" tool by demonstrations of injecting CAN-bus packets on a car. We will show some videos to prove the results of our work. This tool can also be used as a remote access tool, which can realize full control over the car without adding any actuators on the vehicle in some modern car via Telematics system.


### [CryptGrep: Rapidly Search a Cryptographic Function to Analyze Malware](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
'CryptGrep' is an IDA python script which makes it possible to search a cryptography function to analyze malware rapidly. There are many existing implementations such as 'FindCrypt' (http://www.hexblog.com/?p=28) and 'idascope' (https://github.com/nihilus/idascope) which take an approach to find cryptographic magic number statically.

But, there are some cryptographic algorithm that doesn't use a magic number such as RC4, or malware can also hide the magic number. We needed another tool that can apply for these malware. The same malware family usually use the same cryptographic algorithm, and don't change their algorithm and implementation so frequently. Therefore, CryptGrep adopted signature based approach. Our approach also uses improved 'BinGrep' algorithm that was specialized for cryptographic function using several heuristic technique.

We created several pre-set signatures for typical malware. The usage is very simple and easy. And if you need additional signature, you can also create your original signature using your malware.


### [DaaS: Decompilation as a Service](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
"Decompilation-as-a-Service" or "DaaS" is a tool designed to change the way of file decompiling. An analyst usually decompiles malware samples one by one using a program with a GUI. That's pretty good when dealing with a few samples, but it becomes really tedious to do with larger amounts. Not to mention if you have to decompile different types of files, with different tools and even different operating systems. Besides, lots of decompilers cannot be integrated with other programs because they do not have proper command line support.

DaaS aims to solve all those problems at the same time. The most external layer of DaaS is docker-compose, so it can run on any OS with Docker support. All the other components run inside Docker so now we can integrate the decompiler with any program on the same computer. In addition, we developed an API to use DaaS from the outside, so you can also connect the decompiler with programs from other computers and use the decompiler remotely. In our particular case at Deloitte Threat Intelligence team, we needed to decompile thousands of samples received from different systems and to be able to distribute processing and dynamically scale our capabilities.

Although the tool's modular architecture allows you to easily create workers for decompiling many different file types, we started with the most challenging problem: decompile .NET executables. To accomplish that, we used Wine on a Docker container to run Windows decompilers flawlessly on a Linux environment. In addition, on Windows some programs create useless or invisible windows in order to work, so we needed to add xvfb (x11 virtual frame buffer; a false x11 environment) to wrap those decompilers and avoid crashes on our pure command line environment. This allows you to install DaaS in any machine without desktop environment and be able to use any decompiler anyway.

You can access the tool's source code at: https://github.com/codexgigassys/daas


### [Deoptfuscator: Automated Deobfuscation of Android Bytecode using Compilation Optimization](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Code obfuscation is a technique that makes programs harder to understand. Malware writers widely the obfuscation technique to evade detection from anti-malware software, or to deter reverse engineering attempts for their malicious code. Typical obfuscation techniques applied to Android malicious apps include identifier renaming, string encryption, control-flow obfuscation, and Java reflection (API hiding). If we de-obfuscate the obfuscated code and restore it to the original code before obfuscation was applied, we can analyze the obfuscated malware effectively and efficiently.

Therefore, we have developed Deoptfuscator, an effective tool for de-obfuscating the Android applications that have been transformed using control-flow obfuscation mechanisms. That is, it can reverse the control-flow obfuscation of Android APKs.

The features of Deoptfuscator are as follows:
- Deoptfuscator can detect obfuscation traces (especially, opaque predicates) utilizing the optimization approach of Android ART's ahead-of-time (AOT) compiler. It effectively optimizes the control flow of an obfuscated app using ReDex as well as the detected obfuscation traces.
- If the obfuscated Android app can run on a device, the de-obfuscated app reversed by Deoptfuscator can run on the device too.
- Deoptfuscator can reverse the control-flow obfuscation techniques of DexGuard that other de-obfuscation tools haven't.
- If Deoptfuscator is used in conjunction with other de-obfuscators such as DeGuard that can reverse identifier renaming of Android APKs, it can be a more powerful de-obfuscation tool.



This research was supported by Basic Science Research Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science and ICT (no. 2018R1A2B2004830)


### [FLARE VM](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Have you ever needed to rapidly create a Windows VM with all your analysis tools? Do you get annoyed by constantly having to update each and every security tool to the latest version in you VMs? Has your VM been not updated or patched for years on end? If you answered yes to any of these questions, then you NEED the FLARE VM.

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


### [FileInsight-plugins: Decoding Toolbox of McAfee FileInsight Hex Editor for Malware Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
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


### [Ghidra-EVM: Reversing Smart Contracts with Ghidra](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
In the last few years, attacks on deployed smart contracts in the Ethereum blockchain have ended up in a significant amount of stolen funds due to programming mistakes. Since smart contracts, once compiled and deployed, are complex to modify and update different practitioners have suggested the importance of reviewing their security in the blockchain where only Ethereum Virtual Machine (EVM) bytecode is available. In this respect, reverse engineering through disassemble and decompilation can be effective.

Ghidra-EVM is a Ghidra module for reverse engineering smart contracts. It can be used to download Ethereum Virtual Machine (EVM) bytecode from the Ethereum blockchain and disassemble and decompile the smart contract. Further, it can analyze creation code, find contract methods and locate insecure instructions.


### [Glyph - An Architecture Independent Binary Analysis Tool for Fingerprinting Functions Through NLP](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Reverse engineering is an important task performed by security researchers to identify vulnerable functions and malicious functions in IoT (Internet of Things) devices that are often shared across multiple devices of many system architectures. Common techniques to currently identify the reuse of these functions do not perform cross-architecture identification unless specific data such as unique strings are identified that may be of use in identifying a piece of code. Utilizing natural language processing techniques, Glyph allows you to upload an ELF binary (32 & 64 bit) for cross-architecture function fingerprinting, upon analysis, a web-based function symbol table will be created and presented to the user to aid in their analysis of binary executables/shared objects.


### [IDA2Obj: An Innovative Tool for Static Binary Instrumentation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
As well known, object files are generated by c/c++ compiler or assembler from source code, and linked into an executable binary. But now, I can directly dump multiple object files just from one executable binary (exe, dll, ...) by using this tool. What's more amazing is that they can be linked again to a new binary, which is almost same as the old one !

It is designed mainly for SBI (Static Binary Instrumenation), to collect code coverage and integrate with popular fuzzing engines (AFL, honggfuzz, ...). Of course, it is faster than all of the DBI solutions.


### [Lupo: Malware IOC Extractor](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
None


### [Packet Sender](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
None


### [ParseAndC 2.0 – We Don't Need No C Programs (for Parsing)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
This is the 2.0 version of the ParseAndC tool that was presented in BH and DEFCON last year, with many new features added. The 1.0 version was capable of mapping any C structure(s) to any datastream, and then visually displaying the 1:1 correspondence between the variables and the data in a very colorful, intuitive display so that it was very easy to understand which field had what value.

In 2.0 version, we essentially expand the C language so that C structures alone has the same power as full-fledged C programs. We introduce Dynamic structure, which changes depending on what data it has seen till now. It supports variable-sized array, variable-sized bitfield, and addition/deletion of struct members depending on what value the previous struct members have. Suppose we are parsing the network packets, and after we decode the IP header, depending on the protocol field this tool can automatically decode the next header as either the TCP or UDP. We also add speculative execution, where user just provides the key expected values of certain fields (like magic numbers, mentioned by C initializations), and the tool automatically finds out from which offset to map so that all fields indeed have the expected value.

This tool is extremely portable – it's a single Python 1MB text file, is cross-platform (Windows/Mac/Unix), and also works in the terminal /batch mode without GUI or Internet connection. The tool is self-contained - it doesn't import anything, to the extent that it implements its own C compiler (front-end) from scratch!!

This tool is useful for both security- and non-security testing alike (reverse engineering, network traffic analyzing, packet processing etc.). It is currently being used at Intel widely. The author of this tool led many security hackathons at Intel and there this tool was found to be very useful.


### [ParseAndC: A Universal Parser and Data Visualization Tool for Security Testing](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
None


### [Play with Fire: Uncovering Fairplay DRM and Obfuscation for Fun and Profit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Apple has introduced Fairplay DRM into App Store apps since 2013. For a long time before, a jailbroken IOS device is necessary for decrypting DRM protected app, which brings many problems for security researchers and malware analysts. And Apple's property DRM implementation and other components are highly protected with LLVM-based obfuscation, the lack of review and research may also leaves the vulnerability lasting. With the release of highly iOS-similar Apple Silicon device, we are able to explore more secrets of hardware and software on Apple platforms. My work will cover on three parts: firstly, how Fairplay DRM works and how to make a DRM decryption system on M1 Mac without breaking the system; secondly, possible attack surface of FairplayIOKit; and lastly, what methods Apple uses to obfuscate their property software and attack the weakness.


### [ProcJack + Clove: Non-Invasive Code Instrumentation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Code instrumentation is expensive work, especially when a target application is large and complex, or even impossible if you don't know the build environment or source code.

This technique, non-invasive code instrumentation, leverages two known techniques: Reflective DLL Injection and Microsoft Detours, enabling you to inject arbitrary code at arbitrary places without re-compiling the target application.

The project consists of two parts: DLL injector and Injectee DLL. You can write your own logic(s) to run and interact with the code of the target process in Assembly and/or C++ and embed it into a DLL file, which can be injected into any user-mode process running on Windows x86 or x64. After injected, the Detours' part of the DLL dynamically re-routes the target's code to run your logic.

Linux, ARM, or kernel-mode is not supported. Injection into Google Chrome and Microsoft Edge will be demonstrated.

Presentation Slides: https://github.com/msmania/procjack/blob/master/BHAsia-2019-Arsenal.pdf


### [QiLing: Lightweight Advanced Binary Analyzer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Analyzing binaries mostly rely on high level user tools. At the same time, you need to run the binary on the same target architecture & platform. These restrictions limit advanced automatic analysis, require special hardware resources (such as for IoT analysis), and also expose against malicious binaries.

QIling is a sandbox framework that focuses on providing high level Python API to enable users to build highly customizable analysis tool on top. Using emulator technology inside, our engine can run any machine code on any target platforms. This allows analyzing Windows malware on Linux Arm64, or running IoT firmware based on Mips on MacOS, and so on.

This research introduces a comprehensive overview on the Qiling. We will present all the technical issues we had to deal with, including emualating operating system layers such as syscalls, loader and linker, how qiling supports all executable file formats (PE, MachO, ELF, UEFI and MBR), and finally how we provide a framework for users to easily build their analysis tools on top of this foundation.

To conclude the presentation, we will show some cool live demos, such as:

Run IDA on top of Qiling of with Qiling's IDA scriptable plugin
Emulate, debug and instrument MBR from Qiling Framework


### [Qiling Framework: Deep Dive Into Obfuscated Binary Analysis](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Modern obfuscation techniques are getting more and more challenged. Existing static techniques are no longer sufficient to analyze binary in heavy obfuscated form. To address this issue, we have to provide security analysts with the ability to perform high-fidelity emulation and sophisticated binary instrumentation framework.

Qiling Framework (https://qiling.io) is an advanced sandboxed emulator framework. It encloses a rich set of Python APIs that allow security analysts to develop highly customizable analysis tools with minimal implementation efforts. With the facilitation of the emulation technology in Qiling, our engine can run arbitrary executables in a cross-platform-architecture fashion. As such, security analysts could use it to analyze various executable file-formats, including Windows PE, MachO, ELF, UEFI, MBR, etc.

Since we released Qiling Framework in Nov 2019, our project has received significant attention from the community. Currently, we have about 60+ contributors and almost 1,700 followers on GitHub.

This session shares the latest update on Qiling Framework, focusing on deobfuscating binaries. We will demonstrate how we can provide instant support for presenting code execution flow in the form of intermediate representations (e.g., IDA Pro or R2). Thanks to some advanced features of Qiling Framework, security analysts can use a series of newly added APIs to ease their efforts in reverse engineering. To conclude, we have few live demos to show how to deal with some real sophisticated binaries.

I. Syscall, Operating System API and Library Hijack

We will demonstrate how we can use different APIs in Qiling Framework to intercept a binary function and hijack its execution. By intercepting a binary function, we meant intercepting a library function or syscall at the stage of pre-execution, execution, and post-execution, without the restrictions imposed by the OS or underlying computing architecture.


II. Save and Restore Current Binary Emulation States

Sophisticated binaries impose significant challenges for reverse engineering. With the facilitation of a save-and-restore feature in Qiling Framework, security analysts are able to save and resume an emulation state at any stage. This provides the reverse engineering professionals with the ability to avoid repeatedly running a binary from the beginning state. Given the program state entering into a branch (e.g., taking a jump with jz, jnz, and other branch-taken instructions), Qiling can always save the necessary program state and enable program resume later on.


III. ollvm de-flattern techniques

ollvm is a well-known obfuscation tool. One of its obfuscation techniques is Control Flow Flattening. With Qiling emulation, we can search real control flow and restore it easily. Thanks to the newly added feature to present control flow in an intermediate representation (like IDA microcode API, R2 ESIL, VEX, and etc), the new version of Qiling will make such de-flattern techniques cross-architecture.


### [Qiling: Smart Analysis for Smart Contract](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Ethereum Virtual Machine (EVM) is the most widely used architect to support the core of smart contracts. Many existing EVM emulators are just debugging tools based on symbolic execution. Unfortunately, these engines are just simple tools that do not encourage and support us to develop tools on top of them.

To raise the bar, we extended Qiling [1] to support EVM smart contracts (so Qiling is not just limited to analyze machine binary code, but also works for smart contracts) . Our framework offers some key features as follows.

- Analyze smart contracts only with their bytecode, without requiring source codes.
- Can instrument smart contracts at various level: instruction, code, event and activity
- Rule based dynamic smart contract analysis
- Not just limited to EVM smart contracts, but is also compatible with other EVM based smart contracts, supporting modern smart contract requirements.

In this talk, we will present our instrument-able EVM based smart contract framework. With our framework, users will be able to build all kinds of tools on top of it. For example, one could develop a scanner to test the corresponding smart contracts and even perform an automated analysis against smart contracts.

To demonstrate the power of our framework, we built an ultra-fast fuzzer for smart contract, using coverage guided technique. We extended the traditional binary fuzzer named AFL for this. Our fuzzer can efficiently discover typical vulnerabilities in EVM smart contracts, without requiring contract source code.


### [Reversing MCU with Firmware Emulation](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
A microcontroller unit (MCU) is a small computer on a single metal-oxide-semiconductor (MOS) integrated circuit (IC) chip. It is widely used in various types of devices, appliances, automobiles, and many more. Recently MCU security has been raised as a major concern among users and operators, as MCU vulnerabilities can be catastrophic. For this reason, it is important to audit MCU code for security issues. Unfortunately, due to the limited resources on MCU, the on-device test for MCU is not feasible. Besides, there are no emulation solutions able to provide a full instrumentation analysis platform for MCU firmware.

On the other hand, the tight coupling between MCU and hardware peripherals makes it difficult to build an MCU firmware emulator. This greatly hinders the application of dynamic analysis tools in firmware analysis, such as fuzzing.

This talk discusses how we emulated MCU emulation without real peripheral hardware. This requires to model peripheral's registers and interrupts, and implements their internal logic based on the official peripheral documentation and hardware abstraction layer (HAL). We can now emulate widely used MCU chips from top MCU vendors such as STM, Atmel, NXP, and so on. Each of them includes a diverse set of peripherals, including UART, I2C, SPI, ADC, Ethernet, SD Card, Timer, etc.

Upon our emulation, we built several analysis tools for various firmware formats, such as ELF, Binary, and Intel Hex, which are widely used in MCU libraries (RTOS, Arduino, Protocol Stack, etc). We are able to perform advanced tasks, such as:

- Instrument and hijack MCU's activities (e.g, reads and writes to peripherals).
- Save and restore current peripheral/execution states (e.g. register and interrupts).
- Supports multi-threaded firmware, such as RTOS.
- Hijack the interrupts from peripherals, so users can control the scheduling policy of multi-threaded firmware.

To demonstrate the power of our work, we will have live demos to show some exciting cases:

- Emulate MCU with external devices via SPI. UART and I2C
- Fuzz MCU firmware to find 0days with a customized AFL fuzzer.
- Password brute forcing for MCU firmware
- To solve some MCU challenges on CTFs

New code and demo will be released after the talk.


### [SHAREM: Advanced Windows Shellcode Analysis Framework with Ghidra Plugin](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Shellcode can be cryptic, especially when encoded. Understanding its functionality is not straightforward. SHAREM is a cutting-edge Shellcode Analysis Framework, with both emulation and its own disassembler. SHAREM's unprecedented capabilities can allow us to unravel the mysteries of shellcode in new ways not seen.

Windows syscalls have become trendy in offensive security, yet SHAREM is the only tool that can emulate and log all user-mode Windows syscalls. Additionally, SHAREM also emulates and logs thousands of WinAPI functions. SHAREM is the only shellcode tool to parse and discover not only parameters, but also entire structures passed as parameters. SHAREM doesn't present parameters as hexadecimal values, but converts each to human readable format, in vivid colors.

Disassemblers like IDA Pro and Ghidra can be poor at disassembling shellcode accurately. SHAREM's disassembler is significantly more accurate with its original analysis capabilities. SHAREM additionally can uniquely integrate emulation results to provide flawless disassembly. Novel signature identifications are used to identify each function in the shellcode, and parameter values. SHAREM uses unique capabilities to accurately identify data, presenting data the correct way, not as misinterpreted instructions. SHAREM also uniquely provides complete-code coverage via emulation, capturing all functionality.

New at Arsenal, we will release a new script that allows SHAREM's output to be ingested by Ghidra. While Ghidra can handle shellcode in some cases, it simply cannot beat a framework specifically designed to handle and emulate shellcode. As such, this new release leverages SHAREM's advanced capabilities. Additionally, major updates include revamped complete-code coverage, timeless debugging of stack, nearly doubling the number of supported WinAPIs.

SHAREM provides unprecedented capabilities with encoded shellcode. Not only does it fully deobfuscate shellcode through emulation, discovering WinAPIs and syscalls, but it automatically recovers the shellcode's deobfuscated form. SHAREM presents error-free disassembly of its decoded form, with function calls and parameters labelled.


### [SafeNet - Securing Your Network From Your Research](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
In the world of Cyber Security and especially malware research and reverse engineering, we often put ourselves and our PCs at constant risk, and a common method to mitigate this is by using a Virtual Machine and while this method is great for keeping our PCs safe, it does not address a larger issue - our network.

This is true especially now, with the rise in popularity of remote and hybrid work where we have to research on networks that lack corporate-level protection solutions like our homes!

SafeNet is a solution to keep our research labs and dirty virtual machines connected to the internet, all while segregating them from our local network and keeping it safe, ensuring that we can continue researching while staying as safe as possible.


### [Snake: The Malware Storage Zoo](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Snake is a malware storage zoo that was built out of the need for a centralized and unified storage solution for malicious samples that could seamlessly integrate into the investigation pipeline. Snake utilizes a plugin system to provide extensive static analysis capability along with interface capability to allow interaction with 3rd party platforms, such as Cuckoo. Snake adheres to the RESTful API philosophy and as a result allows for seamless interaction with 3rd party tools from within a single UI. It provides enough information to allow analysts to quickly and efficiently pivot to the most suitable tools for the task at hand.


### [Stantinko deobfuscation arsenal](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Stantinko is a malware family, which has been active since at least 2012, and has been gradually improving its code obfuscation techniques to hinder analysis and detection – especially in its recent versions. The half-million-strong Stantinko botnet has been used by its operators for various cybercriminal activities, including click fraud, ad injection, social network fraud, password stealing attacks, and cryptomining.

Stantinko's custom obfuscation techniques can be divided into four categories: control-flow flattening, string obfuscation, do-nothing code, and dead code, strings and resources. The techniques are employed in both x86 and x64 versions of the malware and we'll focus particularly on the first two.

These control-flow-flattening loops generally merge multiple functions into one. They transform the control flow to a form that is hard to read and the execution order of basic blocks is unpredictable without extensive analysis.

Stantinko's string obfuscation technique resembles construction of strings on the stack, but it additionally uses standard C functions for string manipulation with various decoy words and sentences to compose the final string.

These enhancements to the otherwise common obfuscations are what make them unique and turn ordinary reverse engineering methods to deal with the techniques useless.


### [The Go Reverse Engineering Tool Kit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
The Go Reverse Engineering Tool Kit (go-re.tk) is a new open source toolset for analyzing Go binaries. The tool is designed to extract as much metadata as possible from stripped binaries to aid both reverse engineering and malware analysis. Gore can, for example, detect the compiler version used, extract type information and recover function information, including source code line numbers for functions and source tree structure.

The core library is written in Go, but the tool kit includes C-bindings and a library implementation in Python. When using the C-bindings or the Python library, it is possible to write plugins for other analysis tools such as IDA Pro and Ghidra. The toolset also includes "redress", a command line tool to "re-dress" stripped Go binaries. It can both be used standalone to print out extracted information from the binary or as a radare2 plugin to reconstruct stripped symbols and type information.

The goal with the tool kit is to lower the bar to enter for anyone that wants to analyze programs written in Go.

Source Code: https://github.com/goretk


### [Tracee: Linux Runtime Security and Forensics Using eBPF](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Tracee is a runtime security and forensics tool for Linux. It is composed of tracee-ebpf, which collects OS events, and tracee-rules, which is the runtime security detection engine.


Tracee-ebpf is capable of tracing all processes in the system or a group of processes according to some given filters. The set of events to trace can be selected by the user and include the following:


1. System calls
2. LSM hooks (security_file_open, security_bprm_check, cap_capable, ...)
3. Internal kernel functions (vfs_write, commit_creds, ...)
4. Special events and alerts (magic_write, mem_prot_alert, ...)


Other than tracing, Tracee-ebpf is also capable of capturing files written to disk or memory (e.g. "fileless" malwares), and extracting binaries that are dynamically loaded to an application's memory (e.g. when a malware uses a packer). Using these capabilities, it is possible to automatically collect forensic artifacts for later investigation.
Tracee-Rules, is a rule engine that helps you detect suspicious behavioral patterns in streams of events. It is primarily made to leverage events collected with Tracee-eBPF into a Runtime Security solution.
Tracee supports authoring rules in Golang or in Rego.


### [Tracee: Linux malware tracing and forensics using eBPF](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Tracee is a system tracing tool, focused on malware related behaviours.

Using eBPF technology of the Linux kernel, Tracee can trace selected system calls and internal kernel functions.
Other than tracing, Tracee is also capable of capturing files written to disk or memory (e.g. "fileless" malwares), and extracting binaries that are dynamically loaded to an application's memory (e.g. when a malware uses a packer). With these features, it is possible to quickly gain insights about the running processes that previously required the use of dynamic analysis tools and special knowledge.


### [Tracing Golang Windows API calls with gftrace](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
gftrace is a Windows API tracing tool that abuses the way that the Golang runtime works to monitor all the API calls performed by Go applications. The project is a command line tool that only requires the user to specify what Windows functions to trace. Since the tool was designed to work with Go applications specifically it provides a very clean output based on the calls the main package performs and filters all the noise the Go runtime produces.

The tool is also very portable and reliable since it works with several (if not all) Go versions and only interacts with the Go runtime, without touching any Windows API call. gftrace can be very handy for fast malware triage and reverse engineering in general, specially when it comes to obfuscated, stripped and/or trojanized samples.


### [Unblob: A Firmware Extraction Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
One of the major challenges of embedded security analysis is the sound and safe extraction of arbitrary firmware.

Specialized tools that can extract information from those firmwares already exists, but we wanted something smarter that could identify both start offset of a specific chunk (e.g. filesystem, compression stream, archive) and end offset.

We stick to the format standard as much as possible when deriving these offsets, and we clearly define what we want out of identified chunks (e.g., not extracting meta-data to disk, padding removal).

This strategy helps us feed known valid data to extractors and precisely identify unidentified chunks, turning unknown unknowns into known unknowns.

Given the modular design of unblob and the ever expanding repository of supported formats, unblob could be used in areas outside of embedded security such as data recovery, memory forensics, or malware analysis.

unblob has been developed with the following objectives in mind:

* Accuracy - chunk start offsets are identified using battle tested rules, while end offsets are computed according to the format's standard without deviating from it. We minimize false positives as much as possible by validating header structures and discarding overflowing chunks.
* Security - unblob does not require elevated privileges to run. It's heavily tested and has been fuzz tested against a large corpus of files and firmware images. We rely on up-to-date third party dependencies that are locked to limit potential supply chain issues. We use safe extractors that we audited and fixed where required (e.g., path traversal in ubi_reader, path traversal in jefferson, integer overflow in Yara).
* Extensibility - unblob exposes an API that can be used to write custom format handlers and extractors in no time.
* Speed - we want unblob to be blazing fast, that's why we use multi-processing by default, make sure to write efficient code, use memory-mapped files, and use Hyperscan as high-performance matching library. Computation intensive functions are written in Rust and called from Python using specific bindings.


### [Unravelling the Mysteries of Shellcode with SHAREM: A Novel Emulator and Disassembler for Shellcode](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
None


### [YARASAFE: Automatic Binary Function Similarity Checks with Yara](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
YARASAFE is a new Yara module that automates the generation of rules containing binary similarity checks. Given a binary function, YARASAFE computes automatically its signature and includes it into a rule that will match any similar function.

This module rely on SAFE, a tool developed to create embedding vectors to represent binary functions. SAFE generates similarity-preserving embeddings: given two similar functions, their SAFE embeddings will be similar.

To create the embedding of a desired function YARASAFE includes an IDA Pro plugin: it sufficient to select the function in IDA and run the plugin to obtain its embedding.

YARASAFE can be used to create automatically yara rules for different purposes:

- Malware hunting
- Library function recognition
- Vulnerable function detection


### [Z9 - Malicious PowerShell Script Analyzer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
Reversing a malicious PowerShell script can be a very tedious and time-consuming process, especially when the script is obfuscated. Z9 provides an efficient solution to this problem. It is a PowerShell script analyzer that can quickly deobfuscate the script and determine whether it is malicious or not. Z9 leverages several detection engines to make an informed decision.

* Obfuscation Detection
* Randomized String Detection
* URL Extractor
* Blacklist
* AI (Logistic Regression)
* Sandbox


### [chocoProxy: Aiding in the Reverse Engineering of Windows Applications' Network Traffic](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
chocoProxy is a Windows tool intended to aid in reverse engineering Windows applications' network traffic. The proxy works by hooking the sending and receiving Windows APIs after being injected into a target process. The traffic can be modified to arbitrary values to observe the behaviour of an application when provided with unexpected input. The tool is meant to expedite the discovery and development of memory corruption exploits that occur in the implementation of complex and custom network protocols. chocoProxy takes away the necessity for exploit developers to reverse engineer a network protocol by utilizing the existing client/server functionality in the target.


### [uftrace: Dynamic Function Tracing Tool for C/C++/Rust programs](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
uftrace is a function tracing tool that helps in the analysis of C/C++/Rust programs. It hooks into the entry and exit of each function, recording timestamps as well as the function's arguments and return values. uftrace is capable of tracing both user and kernel functions, as well as library functions and system events providing an integrated execution flow in a single timeline.

Initially, uftrace only supported function tracing with compiler support. However, it now allows users to trace function calls without recompilation by analyzing instructions in each function prologue and dynamically and selectively patching those instructions.

Users can also write and run scripts for each function entry and exit using python/luajit APIs to create custom tools for their specific purposes.

uftrace offers various filters to reduce the amount of trace data and provides visualization using Chrome trace viewer and flame graphs, allowing for a big picture view of the execution flow.

uftrace was open sourced in 2016 and has been developed at https://github.com/namhyung/uftrace.


### [unblob](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Reverse--Engineering](https://img.shields.io/badge/Category-Reverse--Engineering-gray)  
One of the major challenges of embedded security analysis is the sound and safe extraction of arbitrary firmware.

Specialized tools that can extract information from those firmwares already exists, but we wanted something smarter that could identify both start offset of a specific chunk (e.g. filesystem, compression stream, archive) and end offset.

We stick to the format standard as much as possible when deriving these offsets, and we clearly define what we want out of identified chunks (e.g., not extracting meta-data to disk, padding removal).

This strategy helps us feed known valid data to extractors and precisely identify unidentified chunks, turning unknown unknowns into known unknowns.

Given the modular design of unblob and the ever expanding repository of supported formats, unblob could be used in areas outside of embedded security such as data recovery, memory forensics, or malware analysis.

unblob has been developed with the following objectives in mind:

* Accuracy - chunk start offsets are identified using battle tested rules, while end offsets are computed according to the format's standard without deviating from it. We minimize false positives as much as possible by validating header structures and discarding overflowing chunks.
* Security - unblob does not require elevated privileges to run. It's heavily tested and has been fuzz tested against a large corpus of files and firmware images. We rely on up-to-date third party dependencies that are locked to limit potential supply chain issues. We use safe extractors that we audited and fixed where required (e.g., path traversal in ubi_reader, path traversal in jefferson, integer overflow in Yara).
* Extensibility - unblob exposes an API that can be used to write custom format handlers and extractors in no time.
* Speed - we want unblob to be blazing fast, that's why we use multi-processing by default, make sure to write efficient code, use memory-mapped files, and use Hyperscan as high-performance matching library. Computation intensive functions are written in Rust and called from Python using specific bindings.


---

## Red Teaming / Embedded


### [ARP covert channel attacks by 8bit microcomputer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Introduces a method of embedding information in the padding part of ARP and performing secret communication with only one small 8-bit microcomputer. The transmitter uses an 8-bit microcomputer called Atmega328P. A 10BASE-T Ethernet frame is generated using only the GPIO of the microcomputer without using a dedicated chip such as an Ethernet controller. By using this method, it is possible to perform a covert channel attack with a smaller and cheaper method than the conventional method.

Since this attack can be performed with a single inexpensive and small microcomputer, it can be hidden and operated inside devices that can be connected to various networks. This lecture introduces some attack scenarios, discusses various attack methods that use this attack method, and discusses their defense methods.


### [Alexa HackerMode 2.0: Voice Auto Pwn Using Kali Linux and Alexa Skill Combo](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
HackerMode 2.0 code-named: "Death Star" is an Alexa driven auto-sploit tool designed for the cloud. Not only will it help with syntax and encodings, but it will go full hacker mode and exploit systems automatically for you.

"Alexa, ask HackerMode to hack IP address 192.168.1.135" will instruct Alexa to begin and manage the process of port scanning, fingerprinting, exploit selection, and smart brute forcing exploits through Metasploit 4 or 5.

Alexa will entertain you with mood music or various other activities while it roots and dumps users and passwords from your target. If the exploit is taking a while you can check in on the progress by asking "How's the hack going?"


### [An Extensible Dynamic Analysis Framework for IoT Devices](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
As IoT devices are more than ever present in our society, their security is becoming an increasingly important issue. Dynamic analysis has been proved the arsenal to many security applications (e.g., malware analysis, vulnerability discovery, backdoor analysis, etc.). While several dynamic analysis systems(Avatar, FEMU, Firmadyne, etc. ) have been proposed for IoT devices, they either rely on IoT hardware(Avatar), or lack user friendly interfaces for further extension. In this talk, we will present an extensible whole-system dynamic analysis framework for IoT devices. Specifically, on top of QEMU, we build a Pintool-like framework FirmPin, which provides Just-In-Time Virtual Machine Introspection and a plugin architecture with a simple-to-use event-driven programming interface. FirmPin provides the instrumentation at basic block level, system call level and memory access level for both user level and kernel level programs. Currently, FirmPin supports ARM and MIPS and can run customized kernel from Firmadyne project.

To demonstrate the power of FirmPin, we have created two plugins - MalScalpel and FirmFuzzer. MalScalpel is able to collect the instruction trace, system call trace, and unpacked code of the monitored program(e.g., Mirai). FirmFuzzer utilizes FirmPin to collect the execution information of fuzzed IoT applications, and integrates with AFL to conduct efficient fuzzing for IoT applications. In the future, we plan to add tainting, a powerful technique for many security applications, to the system. The ultimate goal of FirmPin is to be a general analysis framework for IoT devices.

Source Code: https://github.com/DeepBitsTechnology/FirmPin﻿


### [Attack Demonstration Tool Kits for Industry 4.0 Using AI and Cloud](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Industry 4.0 is a new concept of automation data exchange in manufacturing, and technologies and structures are significantly different from the current general ICS. Autonomous judgment and execution are required, and it is based on information exchange using AI and cloud technologies. Devices are supposed to connect interactively that can create new attack surfaces and risks of cyber-attacks.

For instance, if AI on the cloud is used for controlling the ICS, attackers could change parameters for controlling ICS by contaminating the judgment of AI. In such a situation, attackers could compromise ICS without accessing the ICS network. Detecting such attacks is quite challenging if operators rely on AI to judge the desirable parameters of ICS. Therefore, it is important to instruct cyber risks of ICS in Industry 4.0.

We introduce attack demonstration took kits for Industry 4.0 using actual machines (water supply pump system).

This tool kit is portable, and easy to prepare, so is useful for instructing the cyber-risks of ICS whenever and whenever we want. In aspects of Industry 4.0, we especially focus on the security risks of ICS in the following aspects:
- When computers and devices are connected interactively
- When AI on the cloud is used for controlling the ICS

We will show you a demonstration of attacks: the attacker can change the physical status of ICS without accessing the ICS network through an attack against AI.


### [AutoSuite: An Open-Source Multi-Protocol Low-Cost Vehicle Bus Testing Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Vehicle buses such as FlexRay, LIN, CAN (FD) and Ethernet are the cornerstones of ECUs communication. At present, the security research of vehicle buses mainly focuses on CAN Bus. Due to the characteristics of the protocol itself, CAN data is usually transmitted within the domain. while Flexray is often used as a backbone network connecting powertrain control, autonomous driving, and body control domains for cross-domain communication and transmission of critical data.
It is commonly used in high-end brands such as Audi, Lotus, and BMW. However, security research on Flexray is still in its infancy.

We will present AutoSuite, an open-source, multi-protocol, low-cost vehicle bus testing framework, consisting of the AutoBox(hardware) and AutoFunc (software). AutoSuite can be used to access the FlexRay bus and simulate malicious ECUs to send forged data to realize cross-domain ECU attacks and discover potential security vulnerabilities.

AutoBox is probably the first open-source, multi-protocol, low-cost vehicle bus testing hardware that support FlexRay. It can automatically analyze FlexRay bus configuration parameters, join the cluster, and send malicious data on the FlexRay bus. The hardware cost is about $200, which is much lower than the commercial FlexRay bus testing tool Vector VN8910 ($50k). AutoBox also supports remote control, multiple device collaboration, and Ethernet, LIN, and CAN (FD) protocols. AutoBox will provide a friendly, open-source, and low-cost testing tool for vehicle bus researchers, much like HACKRF has become a low-cost alternative to USRP.

AutoFunc may be the first open-source software for functional-level communication testing and functional-level fuzzing that supports condition monitoring. Current open-source vehicle bus testing methods mainly rely on random fuzzing of the CAN protocol by using random data frame IDs, payloads, and DLC. However, a vehicle function typically involves multiple data frames, and a single data frame may not have any impact on the bus. With opendbc and other open-source projects, the .dbc file is no longer a commercial secret. AutoFunc can organize the frames defined in the .dbc file into specific functions, and monitor the function where the crash occurs to achieve a multi-protocol fuzzing test.

In addition, we will show 2 demos,
(1) Demonstrate all functions supported by AutoBox, such as FlexRay, CAN, LIN, Ethernet, WiFi, etc.
(2) Functional-level fuzzing using AutoBox and AutoFunc.


### [BLE CTF Project](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
The purpose of BLE CTF is to teach the core concepts of Bluetooth low energy client and server interactions. While it has also been built to be fun, it was built with the intent to teach and reinforce core concepts that are needed to plunge into the world of Bluetooth hacking. After completing this CTF, you should have everything you need to start fiddling with any BLE GATT device you can find. Built to run on the esp32 microcontroller, the BLE CTF is a fully functional BLE GATT server which challenges users to utilize fundamental bluetooth communication methods. Focusing on fun and education, the CTF is the first of its kind to help teach hackers how to dive into the world of Bluetooth.

Source Code: https://github.com/hackgnar/ble_ctf


### [BLE hardware-less hackme](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
The new, free tool aims to help getting familiar with the very basics of ubiquitous Bluetooth Low Energy technology and its (in)security - without the need of any dedicated hardware. It is based on a specially designed software (running on a typical Windows 10 laptop) - which simulates a BLE device, on the radio layer working exactly the same as a real one. The simulated device contains several "hackme" challenges of increasing level: starting with simple communication protocol introduction up to unlocking smart locks. Most of these challenges can be solved using nothing more than just a free mobile application, which connects via Bluetooth to the laptop running simulated device. This unique approach makes the fun available for everyone who would like to start the journey into fascinating vulnerabilities of BLE devices, but is afraid of gearing up with special hardware or steep learning curve for advanced tools. The basics possible to grasp using the introduced hackme can however be easily applicable to take control of surprisingly lot of real devices surrounding us.


### [BLEMystique: Affordable Custom BLE Target](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
BLEMystique is an ESP32 based custom BLE target which can be configured by the user to behave like one of the multiple BLE devices i.e. Heart rate monitor, Smart Lock, Smart Bottle, Smart band, Smartwatch etc. BLEMystique allows a pentester to play with BLE side of different Smart devices with a single piece of affordable ESP32 chip.


### [CANalyse (2.0): A vehicle network analysis and attack tool.](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
A prerequisite to using telegram option of this tool is that the Hardware implant is already installed in the car and capable of communicating with the Network inside the vehicle. Also, the library requiremnt are satisfied.

Let's assume we have a car in which we have connected with USBtin(or user choice) which is connected to Raspberry pi (or any linux machine of userchoice) and the pi can communicate on the internet.
LInk to USBtin - https://www.fischl.de/usbtin/

What is CANalyse?

Canalyse uses python-can library to sniff vehicle network packets and analyze the gathered information and uses the analyzed information to command & control certain functions of the car.

CANalyse is a software tool built to analyze the log files in a creative powerful way to find out unique data sets automatically and able to connect to simple interfaces such as Telegram. Basically, while using this tool you can provide your bot-ID and be able to use the tool over the internet through telegram.

canalyse can be installed inside a raspberry-PI, it is made to analyse log files in a creative way and also made to exploit the vehicle through a telegram bot by recording and analyzing the data logs.


### [CANalyse 2.0 : A Vehicle Network Analysis and Attack Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
CANalyse is a software tool built to analyse the log files in a creative powerful way to find out unique data sets automatically and inject the refined payload back into vehicle network. It can also connect to simple interfaces such as Telegram for remote control. Basically, while using this tool you can provide your bot-ID and be able to use the tool's inbuilt IDE over the internet through telegram.

CANalyse uses python-can library to sniff vehicle network packets and analyse the gathered information and uses the analysed information to command & control certain functions of the vehicle. CANalyse can be installed inside a raspberry-PI, to exploit the vehicle through a telegram bot by recording and analysing the vehicle network.


### [CLExtract: An End-to-End Tool Decoding Highly Corrupted Satellite Stream from Eavesdropping](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
While satellite communication with ground stations can be eavesdropped on using consumer-grade products, the received signals are oftentimes highly corrupted and cannot be effectively decoded using the traditional finite-state machine (FSM) based approach.

To this end, we develop a tool named CLExtract which utilizes contrastive learning techniques to decode and recover corrupted satellite streams. Unlike the traditional FSM-based approach which relies on critical fields that become unreliable after corruption, CLExtract directly learns the features of packet headers at different layers and identifies them in a stream sequence. By filtering out these headers, CLExtract extracts the innermost payload which contains sensitive and private data. Further, CLExtract incorporates data augmentation techniques to entitle the trained contrastive learning models with robustness against unseen forms of corruption.

To evaluate CLExtract, we performed eavesdropping on the spectrum range from 11 GHZ to 12.75 GHZ in a suburban area of a metropolis with more than 10 million of population in Asia, covering radio signals from seven commercial satellites. CLExtract can successfully decode and recover 71-99% of the total 23.6GB eavesdropped data, a significant improvement over the traditional FSM-based approach implemented by GSExtract which only recovers 2%.

During the arsenal presentation, we will make CLExtract open source and demonstrate its usage to the security community using real-world satellite streams. This way, we hope to foster future research on satellite offense and defense techniques.


### [ChangWei: A Modern Fuzzing Framework for VxWorks System](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
VxWorks is the industry's leading real-time operating system. It has been widely used in various industry scenarios, which require real-time, deterministic performance and, in many cases, safety and security certification. Since VxWorks has so much importance in industry, more and more people are working on security problems around it.

Fuzzing is an effective technique to discovery vulnerabilities. Feedback-guided fuzzing, such as AFL(American Fuzzy Lop), has proven its excellent ability in finding vulnerabilities of complex programs. Fuzzing tools using this technique have been widely applied to Linux, MacOS and even Windows, but never to VxWorks. According to the current situation, we design a feedback-guided fuzzing tool named "ChangWei" especially for VxWorks. We take advantage of the instrumentation API of Bochs emulator to measure and extract target coverage in a persistent fuzzing mode, and then generate input samples with the help of AFL mutation engine.

We are going to utilize this tool to assist developers to test their code and find hidden vulnerabilities before they are discovered by malicious attackers. Apart from that, we'd like anyone who has interest in this to help us optimize it and build a powerful tool for the security industry.


### [Cotopaxi: IoT Protocols Security Testing Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Cotopaxi is a set of tools for security testing of Internet of Things devices using specific network IoT/IIoT/M2M protocols (e.g. AMQP, CoAP, DTLS, HTCPCP, mDNS, MQTT, MQTT-SN, QUIC, SSDP).


### [Drone Hacking with DroneSploit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
This project is aimed to provide a Metasploit-like CLI framework tailored to drone hacking.

It currently supports modules for the C-me and Flitt drones (Hobbico) but should be extended in a near future with new modules for other brands and models (i.e. Parrot and DJI).


### [EMBA – From firmware to exploit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
IoT (Internet of Things) and OT (Operational Technology) are the current buzzwords for networked devices on which our modern society is based on. In this area, the used operating systems are summarized with the term firmware. The devices themselves, also called embedded devices, are essential in the private and industrial environments as well as in the so-called critical infrastructure.

Penetration testing of these systems is quite complex as we have to deal with different architectures, optimized operating systems, and special protocols. EMBA is an open-source firmware analyzer with the goal to simplify and optimize the complex task of firmware security analysis. EMBA supports the penetration tester with the automated detection of 1-day vulnerabilities on a binary level. This goes far beyond the plain CVE detection: With EMBA you always know which public exploits are available for the target firmware. Besides the detection of already known vulnerabilities, EMBA also supports the tester on the next 0-day. For this, EMBA identifies critical binary functions, protection mechanisms, and services with network behavior on a binary level. There are many other features built into EMBA, such as fully automated firmware extraction, finding file system vulnerabilities, hard-coded credentials, and more.

EMBA is the open-source firmware scanner, created by penetration testers for penetration testers.


### [EMBA – Open-Source Firmware Security Testing](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
IoT (Internet of Things) and OT (Operational Technology) are the current buzzwords for networked devices on which our modern society is based on. In this area, the used operating systems are summarized with the term firmware. The devices themselves, also called embedded devices, are essential in the private and industrial environments as well as in the so-called critical infrastructure.
Penetration testing of these systems is quite complex as we have to deal with different architectures, optimized operating systems and special protocols. EMBA is an open-source firmware analyzer with the goal to simplify and optimize the complex task of firmware security analysis. EMBA supports the penetration tester with the automated detection of 1-day vulnerabilities on binary level. This goes far beyond the plain CVE detection: With EMBA you always know which public exploits are available for the target firmware. Besides the detection of already known vulnerabilities, EMBA also supports the tester on the next 0-day. For this, EMBA identifies critical binary functions, protection mechanisms and services with network behavior on a binary level. There are many other features built into EMBA, such as fully automated firmware extraction, finding file system vulnerabilities, hard-coded credentials, and more.

EMBA is the open-source firmware scanner, created by penetration testers for penetration testers.


### [EXPLIoT: IoT Security Testing and Exploitation Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
EXPLIoT

noun
/ɛkˈsplʌɪəti:/

A Framework for security testing and exploiting IoT products and IoT infrastructure. It provides a set of plugins (test cases) which are used to perform the assessment and can be extended easily with new ones. The name EXPLIoT (pronounced expl-aa-yo-tee) is a pun on the word exploit and explains the purpose of the framework i.e. IoT exploitation. It is developed in python3.

It can be used as a standalone tool for IoT security testing and more interestingly, it provides building blocks for writing new plugins/exploits and other IoT security assessment test cases with ease. EXPLIoT supports most IoT communication protocols, hardware interfacing functionality and test cases that can be used from within the framework to quickly map and exploit an IoT product or IoT Infrastructure.
It will help the security community in writing quick IoT test cases and exploits. The objectives of the framework are:
1. Easy of use
2. Extendable
3. Support for hardware, radio and IoT protocol analysis

Currently, the framework has support for analyzing and exploiting various IoT, radio and hardware protocols. The current suite includes:
- BLE
- CAN
- DICOM (Will be fully implemented before the conference)
- MQTT
- Modbus
- I2C
- SPI
- UART

We are also very happy to announce that we have released a comprehensive documentation including User and Developer guide to help the security community kick start quickly and easily with the framework. Source code and documentation is available here - https://gitlab.com/expliot_framework/expliot

We are currently working on plugins for medical, radio and hardware analysis and will release it at Blackhat.


### [Expl-iot: IoT Security Testing and Exploitation Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Expl-iot is an open source flexible and extendable framework for IoT Security Testing and exploitation. It will provide the building blocks for writing exploits and other IoT security assessment test cases with ease. Expliot will support most IoT communication protocols, firmware analysis, hardware interfacing functionality and test cases that can be used from within the framework to quickly map and exploit an IoT product or IoT Infrastructure. It will help the security community in writing quick IoT test cases and exploits. The objectives of the framework are:

Easy of use
Extendable
Support for hardware, radio and IoT protocol analysis

We are currently working on the python3 version and will release it in a month. The new Alpha release is envisioned to have support for UART(serial), ZigBee, BLE, MQTT, CoAP (next version will have support for JTAG, I2C and SPI) and few miscellaneous test cases.

Source Code: https://gitlab.com/expliot_framework/expliot


### [FACT 4.0](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Analyzing Firmware specifically to identify potential vulnerabilities is a common activity for security analysts, pentesters, researchers or engineers concerned with embedded devices such as in IoT. FACT offers an automated and usable platform to gain an immediate overview of potential vulnerabilities based on the firmware of a device and supercharges the process of finding deep vulnerabilities.

For this FACT automatically breaks down a firmware into its components, analyzes all components and summarizes the results. The analysis can then be perused in the desired amount of detail using either the responsive web application or a REST API.

The offered analyses include a list of included software and libraries, a matching of said software to CVE databases, identification of hard-coded credentials, private key material and weak configuration among others. FACT also applies source and binary code analysis to identify (possibly exploitable) bugs in the components and offers a large amount of meta data for further manual analysis.

A focus of recent development has been to offer more information regarding interdependencies between firmware components to ease the identification of data flow inside a firmware. This allows quickly grading the risk involved with uncovered vulnerabilities or configuration flaws by finding possible attack vectors concerning given component.

Finally, FACT offers multiple ways to collect and fuse analysis results, such as firmware comparison, advanced search options including regular expression on binary components and an integrated statistics module.


### [GRFICS: A Graphical Realism Framework for Industrial Control Simulations - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
GRFICS is a graphical realism framework for industrial control simulations designed to lower the barrier to entry for learning about ICS security. This initial version of GRFICS provides a virtual chemical process control network including everything from the plant operator's human machine interface, to a vulnerable programmable logic controller, down to a realistic chemical process simulation being visualized in the Unity 3D game engine. With GRFICS, beginners in ICS security can practice exploiting common ICS vulnerabilities and vividly see the impact of their attacks on the virtual chemical reactor.


### [HIDE & SEEK: An Open Source Implant for Red Teams](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Many Enterprises are shifting away from dedicated workstations and cubes, and moving to a more flexible workspace with thin client and desk hoteling. This creates the ideal landscape for hardware implant attacks. The current implant market, as it exists today, has not kept up with this shift. While closed source for-profit solutions exist, by their nature they lack the flexibility and customization to adapt to large scale targeted deployments. Open source projects similarly exist but focus more on individual workstations (dumb keyboards and remote terminals) relying on corporate networks for remote control and are easily detectable. Neither solution today is able to meet the needs of a modern Red Team.
This presentation introduces an open source, freely available hardware implant which adopts modern IoT technologies, leveraging non-standard communication channels to create a remotely managed mesh network of hardware implants. Attendees will learn about the new techniques and tactics that we used to create a new breed of open-source hardware implant. Topics covered in this presentation will include the scaling of implants for a stealthy enterprise takeover, creating and utilizing a flexible command and control mesh network, creating a new class of remote access shells that survive idle screen lock, and more. Attendees will leave the talk with new tactics and a new platform from which to innovate their own custom implants from. Live demos will be used to demonstrate these new tactics against real world infrastructure.
Previous hardware implant talks have covered: basic implants, their benefits, injecting keystrokes, Wi-Fi connectivity, and attack scripts. This presentation builds off of those but shows attendees how to leverage new techniques and technologies to push the innovation of hardware implants forward evolutionarily for use in today's modern Red Team operations.


### [ICS Forensics Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
ICS Forensics Tools is an open source forensic toolkit for analyzing Industrial PLC metadata and project files. Microsoft ICS Forensics Tools enables investigators to identify suspicious artifacts on ICS environment for detection of compromised devices during incident response or manual check. ICS Forensics Tools is open source, which allows investigators to verify the actions of the tool or customize it to specific needs, currently support Siemens S7.


### [ICS Forensics Tools](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Open Source ICS Forensics Toolkit This cutting-edge toolkit is designed for in-depth analysis of Industrial PLC metadata and project files, providing an essential resource for cybersecurity experts in the industrial control systems (ICS) sector. Our ICS Forensics Tools stand out by enabling thorough investigation of ICS environments, aiding in the detection of anomalies and compromised devices during critical incident responses or routine checks. This exciting arsenal presentation will not only introduce the new protocols but also feature live demonstrations that showcase its capabilities in real-time scenarios. Attendees will receive a concise, user-friendly forensics guide to leverage the full potential of the tool effectively. And there's more – attendees will have exclusive, immediate access to this groundbreaking tool right as the session begins. Don't miss out on this opportunity to enhance your ICS forensics capabilities with our latest open-source solution! https://github.com/microsoft/ics-forensics-tools


### [IR(Inreared) BadUSB attack](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Conventional BadUSB executes a pre-programmed key sequence upon insertion.
This lecture reports a new vulnerability that arises from the addition of an IR receiver element to the traditional BadUSB, such as the IR Infrared Receiver TL1838 VS1838B 1838 38Khz.
The addition of this element allows an external operator to execute key sequences at arbitrary times. Multiple pre-programmed key sequences can be selected at will by external operation.


### [IoT Hunter: A Framework Tool for Building IoT Threat Intelligence System](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Tencent IoT Hunter is a framework tool created to quickly build the IoT threat intelligence platform, which is more specifically designed to analyze IOT threats. The tool contains all important modules for IOT threat analysis, including information collection, data extraction, threat data analysis, and intelligence visualization. Intelligence data includes, but is not limited to, static information extraction, dynamic operation information extraction, and third-party network platform information. The goal of this tool is to help security researchers quickly and easily build their own IOT intelligence platform for IOT malware research and threat tracking.

Using this framework tool, you can get the malicious information (CNC, Domain, function, etc.) in the IoT sample file very precisely and fine-grained. Compared with the traditional simple string extraction, this extraction method is more accurate and supports the extraction of encrypted information. This malicious information can be directly used to integrate into the IoT malicious information base and threat cloud search services, without the need for analysts to re-confirm, greatly improving the efficiency of malicious information processing.

Traditional intelligence information extraction tools are often used to extract predefined information. The framework provides a good extension interface, where users can write personalized plugins to expand the scope of information extraction. For the emerging threats, security analysts can quickly integrate analysis experience such as decryption algorithm into the framework, accurately extract malicious intelligence, and reduce invalid redundant information.

In the tool demonstration phase, we will demonstrate how to use the entire tool. Including the static information of IOT samples. Take popular IOT threats as examples to show how to precisely extract CNC, weak passwords, and configuration files. We will also show how to develop and integrate the platform plug-ins to extract any specific intelligence information of concern. All of the above data information is imported to the platform, security personnel can be free to carry out data analysis, malware track, threat visualization.


### [IoT-Home-Guard: A Tool for Malicious Behavior Detection in IoT Devices](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
IoT devices, especially secondhand devices and rental devices, are under threat of malware implant attack with physical access. Once IoT devices are compromised, hackers can turn them into snooping devices. From a defensive perspective, there are no solutions to detect Trojans in IoT devices.

We present IoT-Home-Guard, a hardware device to detect malicious behaviors of Trojans in IoT devices, such as audios/videos snoop and remote control. It consists of four parts: data flow catcher, traffic analyzing engine, device fingerprint database and a web server. Features of network traffic are extracted by traffic analyzing engine and compared with pre-built device fingerprint database to detect malicious behaviors.

In another research, we were able to implant Trojans in eight devices including smart speakers, ip cameras, routers, driving recorders and mobile translators. We collected characteristics of those devices and ran IoT-Home-Guard. All devices implanted Trojans have been detected. We believe that malicious behaviors of more devices can be identified with high accuracy after supplement of fingerprint database.

The first generation IoT-Home-Guard tool is a hardware device based on Raspberry Pi with wireless network interface controllers. We will customize new hardware in the second generation. Software part is available in our Github (https://github.com/arthastang/IoT-Home-Guard). The system can be set up with software part in laptops after essential environment configuration.


### [IoT-Implant-Toolkit: Framework for Trojans Implantation Research of IoT Devices](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
During our Trojans implantation research for IoT devices, we found many tools outdated and not compatible with high versions. We present IoT-Implant-Toolkit, a framework for Trojans implantation research of IoT devices. It is a toolkit consisting of essential software tools on firmware modification, serial port debugging, software analysis and stable spy clients. We wrapped tools we proved useable in the framework and provided a universal call interface. Additionally, we packed useful open-source tools we developed into the framework. Each software tool acts as a plugin which can be easily added into the framework. With an easy-to-use and extensible shell-like environment, IoT-Implant-Toolkit is a one-stop-shop toolkit simplifying complex procedure of IoT malware implantation.

With IoT-Implant-Toolkit, we were able to implant Trojans in eight devices with physical access, including smart speakers, cameras, driving recorders and mobile translators. We turned them into snooping devices, which send audios or videos in real time. Our presentation will also include live demos of those implanted devices.

IoT-Implant-Toolkit is open-source at https://github.com/arthastang/IoT-Implant-Toolkit.


### [IoXT Hunter: A Remote Discover & Pentest Tool for IoT Devices](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
IoXT Hunter is an open source, extendable, large-scale IoT device remote discovery and pentest tool. It is designed to discover all known IoT devices for a specified range of network addresses and to perform security testing on related IoT devices using generic or targeted payloads.

If you are a security administrator for a complex or large-scale IoT network (such as an industrial IoT network or a medical IoT network), IoXT Hunter will be your powerful tool. It can help you discover and record all your IoT device assets and perform full remote security testing of your IoT devices.

IoXT Hunter also supports writing and loading your own plugins extensions. If you are an IoT security researcher and have discovered the security vulnerabilities of a kind of IoT device. You can write the appropriate discovery and pentest scripts to scan and evaluate the status of the IoT device on the public network through the IoXT Hunter.


### [IotSecFuzz: Security Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
IoTSecFuzz is Open Source framework which was created with the aim of combining the maximum number of utilities for comprehensive testing of IoT device security at all levels of implementation. It has a convenient console in order to use it as a stand-alone application, as well as the ability to import it as a library.


### [KNX Bus Dump](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
None


### [Kouba: Industrial Pentesting](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Introduction to Industrial security: brief introduction to industrial cyber-attacks and why it's important to protect OT infrastructures. In this part I'll introduce the importance of industrial security, speak about Stuxnet and other dangerous attacks that had impact in industrial sector, and some prevention tips.

Introduction to Kouba: proposing a simple methodology that includes enumeration, footprinting and automatic exploitation with open tools. Presenting the advantages of using Debian with these specific tools* instead of Kali, and how to apply public key/password encryption and magic-wormhole using the scripts for securely exporting encrypted logs out of the virtual machine.

Choosing open hardware for attacks: Once we have footprinted the devices and machines in the OT, in case we have physical access to the infrastructure, there are some things to look for regarding to physical security, such as USB ports, RTU (remote terminal units) details or DNP3 protocol serial communication. Using Arduino nano, pro mini, leonardo and attiny85 for designing either badusb or specific tools; RPI4/3/ZERO; ATMega2560 customizable PLC (PLDuino); S232 shield (for UNO), multi-protocols shield; Radio modules and others.

* The system includes Redpoint and other nmap scripts, Kamerka, Aztarma, PLCinject, S7Scan, ISF, etc as well as Python 2.7 and 3, git, xfce4 terminal, Docker and Vagrant for needed virtualization, Celery and Redis for Kamerka, openssl, clang and other few compiling tools.


### [LoRaWAN Auditing Framework](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
IoT deployments continue to grow, and one part of that significant growth is composed of millions of LPWAN (low-power wide-area network) sensors deployed in hundreds of cities (Smart Cities) around the world, also in industries and homes. One of the most used LPWAN technologies is LoRa for which LoRaWAN is the network standard (MAC layer). LoRaWAN is a secure protocol with built in encryption, but implementation issues and weaknesses affect the security of most current deployments.

This project intends to provide a series of tools to craft, parse, send, analyze and crack a set of LoRaWAN packets in order to audit or pentest the security of a LoraWAN infrastructure.


### [MQTT-PWN: Your IoT Swiss-Army Knife](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
MQTT is a machine-to-machine connectivity protocol designed as an extremely lightweight publish/subscribe messaging transport and widely used by millions of IoT devices worldwide.

MQTT-PWN intends to be a one-stop-shop for IoT Broker penetration-testing and security assessment operations, as it combines enumeration, supportive functions and exploitation modules while packing it all within command-line-interface with an easy-to-use and extensible shell-like environment.

Built-in abilities/modules:

Credential Brute-Forcer - configurable brute force password cracking to bypass authentication controls
Topic enumerator - establishing comprehensive topic list via continuous and accumulated sampling.
Broker information grabber - obtaining and labeling data from an extensible predefined list containing known topics of interest, broker type and version and more
GPS tracker - plotting routes from devices using OwnTracks app and collecting published coordinates, battery usage, connection method etc.
Sonoff exploiter – design to extract passwords and other sensitive information off smart switches

A full circle of scenarios of attack using the tool will be demonstrated.


### [MUD-Visualizer](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Manufacturer Usage Description (MUD) is a recently introduced IETF standard designed to protect IoT devices and networks by isolating IoT device based on the information that define the behavior of that device. The standard defines a straight-forward method to implement a defensive mechanism based on the rules that are introduced by manufacturer of the device. MUD-Files are the core component of the MUD standard and contain the access control information of IoT devices. However, MUD-Files may contain possibly hundreds of access control rules. As a result, reading and validating these files is a challenge; and determining how multiple IoT devices interact is difficult for the developer and infeasible for the consumer. MUD-Visualizer is a tool that provides a visualization of any number of MUD-Files and is designed to enable developers to produce correct MUD-Files by providing format corrections, integrating them with other MUD-Files, and identifying conflicts through visualization. MUD-Visualizer is scalable and its core task is to merge and illustrate ACEs for multiple devices; both within and beyond the local area network.


### [Medaudit: Auditing Medical Devices and Healthcare Infrastructure](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Medaudit is a healthcare/ medical device auditing tool that would help anyone auditing a healthcare networks and medical devices. At the time of writing, there are no tools - commercial or free - that can help security pentest healthcare infrastructure. This tool aims to close that gap and help security analysts use their web app skill set to analyze medical devices. The tool support HL7 protocol right now and will have support for FHIR and DICOM in near future.

The tool does the following things:

Create a visual map of HL7 traffic flow on a network (Passive analysis), extract HL7 traffic on the network.
Scan and verify for open HL7 ports on a host
Perform DOS attacks against HL7 streams on HL7 reciever
Send HL7 messages (malformed attacks)
Fuzzer
Malicious HL7 Server

The tool also acts a proxy using web API so you can reuse web application tests on medical devices.


### [Out-Of-Band Anti Virus Dock (OOBAVD) - A Hardware & Artificial Intelligence Based Anti Virus Solution](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
USB-based attacks account for more than 52% of all cybersecurity attacks on operational technology (OT) systems in the industrial control systems (ICS) industry. The discovery of Stuxnet in 2015 served as a stark reminder that even air-gapped computers, previously thought to be impervious to cyberattacks, are vulnerable. These systems are found in secure military organizations or Supervisory Control and Data Acquisition (SCADA) systems. The societal impact of such attacks can be enormous. Stuxnet, for example, caused significant damage to Iran's nuclear programs and facilities.

While air-gapped systems are considered "secure," they are inconvenient for computer operators, particularly when performing updates and transferring data, which require the use of mobile storage devices, such as USB sticks. Unfortunately, this introduces a flaw into the air-gapped systems, exposing them to computer viruses and malware. Furthermore, adding new peripherals to these systems, such as keyboards and mice, allows BadUSB attacks to be carried out.

OOBAVD is a solution to close this gap. OOBAVD acts as a intermediary between the air-gapped system and USB devices, scanning and blocking detected malicious files from the air-gapped system. Furthermore, malware can attack commercial software-based antivirus software on the host machine by blocking, corrupting, and replacing core antivirus engine files, rendering them inoperable and defenseless. OOBAVD being out of band in the transfer process, is mitigated from this risk.

OOBAVD is designed to have minimum software pre-installed, which reduces the attack surface area to be infected by malware. OOBAVD can also be wiped clean and flashed before connecting to new air-gapped computers, removing persistent malware that manages to infect OOBAVD.


### [PTIOT: AN AUTOMATED SECURITY TESTING FRAMEWORK FOR THE INTERNET OF THINGS - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
With the Internet of Everything era coming and millions of IoT devices becoming interconnected via the Internet, security issues caused by the IoT devices are increasingly serious more than any time before. Different from traditional security problems, there are no specific cognitions or orientations on the technology of security defense. Only if we knew our evil enemy and understood the means they used to attack, would we be able to build an efficient defense system.

PtIoT is an automated security testing framework for the Internet of Things, and it has already been used on 360 IoT devices' productive process. It is combined with 360GearTeam's daily security practice and understanding of the attack pattern the malicious frequently used. It contains grey box-based security tests on external ports, compilation options, communication encryption, OS check runtime program check, web application check, etc. It is used to test ROMs on the products' version iteration process. At present, the security test covers products like 360 Smart Camera, 360Safe Wifi Router, 360 Driver Recoder and so on.


### [Puppet Fuzz: Discovering Critical Kernel Vulnerabilities with Innovative Approach](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Internet of Things (IoT) devices have become an integral part of our lives, but their security vulnerabilities pose a significant risk to our privacy and security. While previous research has focused on user space components of embedded firmware, we have discovered that kernel vulnerabilities in these complex devices are particularly high-risk, potentially leading to full system compromise.
Kernel modules are typically tightly bound to the kernel, but because different IoT devices use different kernel versions and compile options, it is difficult to load them correctly in other simulated environments. However, true device-based fuzz testing is very time-consuming and resource-intensive. Additionally, unlike user-level programs, kernel-level programs require a device reboot after every crash, which further limits the development of IoT kernel fuzz testing.
To address these challenges, we propose a novel approach that abstracts closed-source kernel modules code to execute on a stable Linux kernel environment that we have constructed by using our aspect oriented system. This platform allows us to transfer library function calls and stack management, enabling us to detect kernel-level vulnerabilities that were previously difficult to identify. In addition, due to our front-end and back-end separation design, the platform can easily support IoT drivers of multiple architectures. Our approach has enabled us to discover a multitude of issues across devices from top manufacturers such as Netgear, Cisco, Asus, HP,TPLink,DLink and Western Digital etc.
In this talk, we will show our method and present one such universal kernel hardware module vulnerability, demonstrating how we were able to exploit a kernel driver vulnerability to achieve remote command execution on the device. Our platform provides a replicable and stable environment that forms the basis for efficient and effective kernel fuzz testing, ultimately improving the security of IoT devices and protecting the privacy of their users.


### [RF( Radio Frequency ) Offensive and Defense Exercise Server](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
We believe that cyber security should not only cover the Internet space but also the RF (radio frequency) space.
In the radio space, interception, decryption, tampering, jamming, and spoofing are actively practiced against hostile countries.　For example, the Russian Красуха-4 is a well-known electronic warfare weapon.
In fact, it has a longer history than the Internet, and there is much to learn from it.
However, there are not so many RF training environments that can be easily used.


### [RFQuack: A Versatile, Modular, RF Security Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Software-defined radios (SDRs) are indispensable for signal reconnaissance and physical-layer dissection, but despite we have advanced tools like Universal Radio Hacker, SDR-based approaches require substantial effort. Contrarily, RF dongles such as the popular Yard Stick One are easy to use and guarantee a deterministic physical-layer implementation. However, they're not very flexible, as each dongle is a static hardware system with a monolithic firmware. We present RFquack, an open-source tool and library firmware that combines the flexibility of a software-based approach with the determinism and performance of embedded RF frontends. RFquack is based on a multi-radio hardware system with swappable RF frontends, and a firmware that exposes a uniform, hardware-agnostic API. RFquack focuses on a structured firmware architecture that allows high- and low-level interaction with the RF frontends. It facilitates the development of host-side scripts and firmware plug-ins, to implement efficient data-processing pipelines or interactive protocols, thanks to the multi-radio support. RFquack has an IPython shell and 9 firmware modules for: spectrum scanning, automatic carrier detection and bitrate estimation, headless operation with remote management, in-flight packet filtering and manipulation, MouseJack, and RollJam (as examples). We used RFquack in high-schools to teach digital RF protocols, to setup RF hacking contests, and to analyze industrial-grade devices and key fobs, on which we found and reported 11 vulnerabilities in their RF protocols.


### [RPL Attacks Framework: Attacking RPL in WSNs](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
This tool is a framework for attacking the Routing Protocol for Low power and lossy networks (RPL) implementation of Contiki for Wireless Sensor Networks (WSN).

Presentation: https://github.com/dhondta/rpl-attacks/raw/master/doc/bheu18-arsenal-presentation.pdf


### [RadioT Shield: A Radio Way to Protect Most of Your IoT Devices](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
RadioT Shield is an open source platform dedicated to detecting the attack of various IoT devices in a given space by radio communication data. RadioT Shield can detect a lot of radio-based IoT-related attacks, such as WIFI attacks, BLE attacks, GSM attacks, ZigBee attacks, etc. Unlike other IoT hardware and software security solutions, this system does not require any modification of the protected IoT device and does not affect the existing functionality of the device.

RadioT Shield is suitable for all IoT devices that use radio communications, even devices that are more than a decade old. It is therefore particularly suitable for scenarios with complex IoT device types and IoT networks consisting of old, non-secure IoT devices, especially industrial control IoT devices, medical IoT devices, smart home IoT devices, and more.


### [Remote Assessment and Proctoring using Intelligent Devices (RAPID)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Many educational institutions have adopted online proctoring as a mean to conduct and ensure academic integrity during online assessments, spurred by the pandemic. Most of such remote assessment solutions are closed-source, and requires the installation of various libraries or dependencies; this introduces potential risk for students who would not be able to scrutinize, or have a say as to what is installed on their computers. Being closed source, such solutions can also be slow to react to mala fide actions to tamper and bypass measures put in place to deter cheating. In fact, one only needs to perform cursory searches online to find various ways to defeat some well-known closed-source remote assessment solutions.

To tackle the issue at hand, we introduce a proof of concept, open-source system for remote proctoring that does not require prior installation of any software or libraries. It leverages the Raspberry Pi Zero hardware that is programmed to inject fileless scripts into a Windows system to monitor surface level and internal activities during remote assessments. To deter mala fide attempts to tamper with our solution, we incorporate techniques typically used by malware and C2 infrastructure in the development of our solution, with the ultimate goal of using such techniques for good. Hence at the end of each proctoring session, our solution leaves no trace of its presence or any residue within the proctored environment.

Being a proof-of-concept, we envision extending our solution to support other popular operating systems, as well as capture and analyze more data with greater efficiency.


### [Safe Scan&C2 Tool](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
In the process of security attack and defense, as well as penetration testing, there are two prominent issues. First, the attack scanning is often detected by the security systems of the defense side, resulting in the scanning IP being blocked. Second, when the defense side is controlled and assets are connected back to the command and control (C2) server, it may be detected by security devices, leading to countermeasures against the penetration testers. In order to safely and conveniently conduct asset detection during the attack and defense process, as well as secure connection back to the controlled assets on the defense side, we have improved the Kademlia protocol and developed a distributed hash table (DHT) technology. We have also developed a networking tool that consists of a large number of Internet nodes, which dynamically updates IDs and node tree structures at regular intervals. This allows each session to initiate requests from a different node during the scanning process, preventing IP blocking due to high-frequency scanning. Additionally, during the controlled asset's connection back to the C2 server, nodes are randomly selected based on user-selected hop count, effectively preventing penetration testers from being traced, thus improving the penetration testing process.


### [ShodanSeeker: Command-Line Tool Using Shodan API](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
The large number of assets published on the Internet - some of which organizations are not even aware of their existence - increase the probability of services being exposed that could put them at risk. As a first step towards resolving this problem, we introduce ShodanSeeker.

Taking advantage of Shodan's crawlers, ShodanSeeker analyzes historical records on-the-fly to discover differences between previously performed scans in order to identify new published services.

Enhancing the capabilities of Shodan's real-time stream of data, our fully customizable solution monitors and generates notification messages once a new risk service is discovered.

Presentation slides: https://drive.google.com/open?id=1Fi5XJ5-1QyXSawHKXVm_emF3NUR2Nx7X


### [Thunderstorm: Turning Off the Lights in Your Data Center](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
One of the main premises of any IT installation, is to protect the entire infrastructure against possible failures. In addition to firewalls and other network elements, one of the vital points is the electrical system.

Thanks to uninterruptible power supplies (UPS), it is possible to cover and manage these issues economically. The main problem, is that many of these systems inherit the same bugs as other IoT devices, which makes them vulnerable to all kinds of attacks.

In this presentation, we will explain how it has been possible to develop different zero-day vulnerabilities thanks to social engineering, some investment, and a bit of common sense. Among other things, these flaws would make it possible to compromise the electrical system of an office or even that of a Data Center.

Since these devices share common components, it would be possible to obtain remote code execution (with the highest possible privileges) and/or denial of service on more than 100 different manufacturers. Moreover, all of this has been automated in a single framework, making it possible to detect and exploit these vulnerabilities easily, simply and fully automatically.


### [UFO: A Security Verification Tool for IoT Device Firmware](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
UFO is an IoT firmware security assessment tool that helps firmware developers or security researchers assess the security level of IoT device firmware.

UFO profiles the IoT firmware in many surfaces, like known vulnerabilities, sensitive data, cracked passwords, and hidden backdoors. It saves penetration testers time to gather information and help create attack vectors. Meanwhile, as a handy tool, UFO exposes vulnerabilities as early as possible to mitigate attacks from IoT malware like the notorious Mirai, which also collected default passwords of IoT devices from firmware. We did leverage UFO to pwn two COTS network cameras by discovering their backdoors and default passwords.

Main features of UFO are:
- Known 3rd Party Suite CVE Risk Report: Post-scan report based on the Common Vulnerability Scoring System (CVSS) which is an open industry standard for assessing the severity of computer system security vulnerabilities.
- Sensitive Data Statistics: Assessment of the email, IP, URL, private or password vulnerabilities.
- Cracked Passwords and Certificates Review: Check if your passwords or certificates are vulnerable.
- Shell Dependency Backdoor Paths: Produces a visual guide of backdoor paths.

A full circle of scenarios of using UFO to analysis IoT firmware will be demonstrated.

Among the above features, the source code used to trace shell dependency has been released on Github: https://github.com/dayanuyim/shdep.

The promotional video: https://youtu.be/0XupD3PAbuo


### [UNIVERSAL RADIO HACKER: INVESTIGATE WIRELESS PROTOCOLS LIKE A BOSS - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
The spectrum of IoT products expands and with it the number of proprietary wireless protocols raises. Such protocols are designed under size and energy constraints so they tend to have a secondary focus on security. Security researchers can examine arbitrary IoT protocols with Software Defined Radios (SDR) but SDRs present the possibly encoded data in a complex IQ format. Therefore, data has to be to demodulated and decoded before researchers can investigate the actual protocol. After revealing the protocol logic with a differential analysis, vulnerabilities can be found e.g. using fuzzing. Present tools require expertise in Digital Signal Processing (DSP) and/or cover only parts of the process e.g. they only offer support for demodulation but do not help to analyze the protocol logic so researchers need to combine various tools and self-made scripts.

We address this problem with the Universal Radio Hacker (URH) - an open source, cross platform application that integrates the complete hacking process. First, URH performs demodulation with minimal user interaction so no deep DSP knowledge is required. Second, URH helps to reverse engineer the protocol logic by organizing with fields and message types. This can either be done manually or automatically by URH to boostrap a protocol. Third, URH includes a fuzzing component for logical protocol fields whereby the selected encoding and modulation is automatically applied to the crafted messages. URH aims to be both self-contained and expandable: Users find all required steps bundled into one application but at the same time URH provides several interfaces for external tools like GNU Radio so also DSP experts can benefit from it.

The source code of URH can be found at GitHub under https://github.com/jopohl/urh.


### [Universal Radio Hacker v2: Simulate Wireless Devices with Software Defined Radio](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Wireless communication between Internet of Things (IoT) devices is, in many cases, built upon proprietary protocols designed under size and energy constraints. Vulnerabilties in such protocols are critical, e.g. an attacker breaks into a house by hacking a wireless door lock. Software Defined Radios (SDR) offer a generic way to investigate such protocols, but require software support when it comes to demodulating and decoding messages. The Universal Radio Hacker (URH) is an open source tool to support researchers when operating with SDRs by abstracting most of the required HF basics needed for demodulation. Furthermore, it assists reverse engineering the protocol format. While this works well for stateless and undirectional protocols, there are more sophisticated protocols on the market that can not be handled without state machine.

Version 2.0 of the Universal Radio Hacker introduces a Simulation tab that allows to specify a complete HF protocol with several states and participants. It is called Simulation because URH has the ability to play the protocol from the perspective of one or more participants, i.e. URH evaluates all messages towards the simulated participant and dynamically crafts responses depending on the state and previous information. The simulation advancement complies to the easy-to-use philosophy that we also use for the basic URH. Users can see all messages of the analyzed protocol in a graphical flow graph and add new messages, edit or move them around at convenience. Message field values are dynamically derived with access to all previously sent and received information or even by using external programs, e.g. for AES encryption. Conditions, jump and pause elements in the graphical user interface allow generating complex state machines. In our presentation, we demonstrate a practical attack that shows how the simulation component of URH opens a sophisticated wireless door lock (AES encryption) with SDRs.


### [VT AUTO-X VEHICLE AUTOMATED SECURITY TESTING TOOL - ARSENAL THEATER DEMO](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Currently, there are some research works on vehicle cybersecurity testing. Many of them are open-source projects, such as CANTact and GoodThopter. CANTact is a popular open-source toolkit available for purchase online that uses SocketCAN to communicate with a CAN bus. Since SocketCAN extends the Berkeley sockets API in Linux by introducing a new protocol family, it is easy to write script languages for CAN message injections. Python is one of the most widely-used script languages for SocketCAN programming. GoodThopter is another recent device targeted at hackers and hobbyists, but is not ready for use as a turn-key solution.

The drawbacks of these open-source tools are that they are not stable and do not work well under heavy-traffic testing scenarios. Also, open-source contributions may not meet the rigorous control and validation requirements of auto industry software practices. We found that it was possible to crash or lock up such tools when injecting them with bursty CAN traffic. For example, CANTact has limited buffer size which may cause buffer overflows. GoodThopter's timeout parameters and configuration file make it hard to work. In our case, we used the serial port for communications and Java as the programming language. Java is preferred over Python as it is faster, more stable, requires strict coding rules, and is better suited to remote control applications.

Cybersecurity testing focuses on finding and identifying unwanted weaknesses or vulnerabilities hiding inside vehicle software. Our goal is to develop an automated and black-box testing tool for OEMs and tier providers to test their vehicles or ECUs with consistent results, which requires no prior detailed knowledge of the testing workflow.

Automation means the tester only needs to follow pre-defined test scenarios one-by-one to finish the whole testing process. Even if the tester does not have prior security testing knowledge or background, he or she can still operate the test device and detect security vulnerabilities by following the automated steps.

Black-box testing strategies should have no prior knowledge of system commands, CAN bus command databases, or the specific manufacturer's practices within the vehicle or system under testing protocols. In this way, OEMs may feel more comfortable with black-box testing since they don't need to release too much of what they may consider to be proprietary system information to internal, outside, or third-party testers.

We have developed the automated automotive cybersecurity testing tool (named VT Auto-X) which has successfully detected serious security vulnerabilities in a number of production vehicles, and has helped several OEMs identify and correct these issues before they became expensive and embarrassing recall programs. It is a black-box test with no prior knowledge of vehicle CAN bus information. Live demonstrations of Auto-X have proven its ability to quickly find software and security vulnerabilities in most of the cars tested.

Auto-X is portable, and can easily connect to a vehicle's CAN bus. The device has a panel which has various types of connection interfaces, including OBD (SAE J1979/J1962) ports and multiple CAN High and CAN Low ports. It incorporates standard banana sockets to facilitate connecting to various vehicle CAN bus accessible points, as well as several power supply options for testing flexibility (bench, garage, mobile). Other connection arrangements are also possible for use when testing individual systems, ECUs, or bench testing components.

A USB 2.0 port is provided to connect to laptops or other computers. Power can also be provided directly via the OBD II connection, by direct 12V DC connection, or via an AC mains adapter power supply. Auto-X also contains several communication modules, such as WIFI, Bluetooth, and 3G, for both short-range and long-range communications making it easy to communicate with remote cloud or smart mobile phones.

Auto-X performs an automated sequence of test scenarios using either the local or cloud-based testing portal. Each scenario test time can range from minutes to hours, which varies depending on the vehicle configuration and equipment. The tool injects CAN traffic into the vehicle CAN bus. By monitoring and recording CAN traffic and responses, the testing portal then analyzes the logs and responses aiming to detect unexpected, unwanted, or potentially harmful security issues.

Auto-X acts as an interface between the entity being tested (an entire vehicle, a single CAN bus, multiple CAN buses, or a component, such as a specific Electronic Control Unit or ECU) and the secure cloud test portal (where the testing scripts reside). It also connects to the user's laptop to control and monitor activity during testing. Once connected to the vehicle, Auto-X can run a series of test scripts or protocols from the cloud portal.


### [VxHunter: A Tool Set for VxWorks Based Embedded Device Analyses](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
VxWorks is the industry's leading real-time operating system. It has been widely used in various industry scenarios, which require real-time, deterministic performance and, in many cases, safety and security certifications such as the NASA's Insight Spacecraft. There was lot's of research on Linux based Router and camera, rarely seen research of VxWorks based device.

Most of VxWorks based IoT devices on the market didn't contain any built-in debugger like WDB(VxWorks WDB Debug Agent) or command line debugger. Without debugger it's almost impossible to analyze the root cause of vulnerability or exploit vulnerabilities.

VxHunter contains an firmware analyze tool and an serial debugger tool. The firmware analysis tool is an IDA plugin which can automatically analyze and rebase firmware to correct loading address, fix function name from symbol table, etc. The serial debugger tool is designed for the target which didn't have built-in debugger like WDB. With VxHunter's help, we successfully analyzed and exploited the CVE-2018-19528 vulnerability.


### [WHID Elite: The Hacking Device for Pwning Computers, Moving Cranes, Exploding Things and Electrocuting Nuts](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
During the last few years, Red Teaming engagements have become more and more popular. This trend pushed some hackers to R&D and release new opensource devices with the intent to make PhySec operations even more interesting. Smoothing the path to new TTPs and improving some old ones. During this talk, I will present two new hacking devices developed from Offensive Ninjas, for Offensive Ninjas:
- WHID Elite (a 2G-enabled offensive device that allows a threat actor to remotely inject keystrokes, bypass air-gapped systems, conduct mousejacking attacks, do acoustic surveillance, RF replay attacks and much more).
- USBsamurai (a Remotely Controlled Malicious USB HID Injecting Cable DIY for less than 10$ that can be used to compromise targets remotely in the most stealthiest way ever seen).


### [WHID Injector and WHID Elite: A New Generation of HID Offensive Devices](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
WHID Injector was born from the need for cheap and dedicated hardware that could be remotely controlled in order to conduct HID attacks. WHID stands for WiFi HID injector. It is a cheap but reliable piece of hardware designed to fulfill pentesters' needs related to HID Attacks, during their engagements. The core of WHID Injector is mainly an Atmega 32u4 (commonly used in many Arduino boards) and an ESP-12s (which provides the WiFi capabilities and is commonly used in IoT projects).

However, during the last months, a new hardware was under R&D (i.e. WHID Elite). It replaces the Wi-Fi capabilities with a 2G baseband. Which extends its wireless capabilities to (potentially) an unlimited working range. This cute piece of hardware is perfect to be concealed into USB gadgets and used during engagements to get remote shell over an air-gapped environment. In practice, is the "wet dream" of any Red Teamer out there. During the Arsenal presentation, we will see in depth how WHID Injector and WHID Elite were designed and their functionalities. We will also look which tools and techniques Blue Teams can use to detect and mitigate this kind of attacks.


### [Wi-Fi Access Point Rootkits](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Wi-Fi access point (AP) security is one of the most important aspects when it comes to securing networks. The compromise of a Wi-FI AP (which mostly also double-up as a router in SOHO environments) can lead to several secondary attacks. There are multiple vectors that are used to compromise the WiFi AP ranging from default passwords to sophisticated 0-days. But, after compromising the device, avoiding detection and maintaining access are the most important areas which eventually dictate the impact of the compromise.

We are going to release a set of code snippets along with the documentation making it easy for people who want to understand the working of Kernel rootkits for IoT devices like Wi-Fi APs. The code will cover hiding a process, renaming a process, blocking kill command on certain processes, network stack based RAT and much more. The code will be released under GPL v2.


### [Wiretapping Tool to Sniff Packets Directly from LAN Cables](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Wiretapping tool to sniff packets directly from LAN cables


### [ZigDiggity: ZigBee Pentest Toolkit](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Introducing ZigDiggity, an entire suite of new ZigBee penetration testing tools to be released by Francis Brown and Matthew Gleason exclusively at Black Hat USA – Arsenal 2018. We'll be publicly releasing a FREE set of ZigBee hacking tools designed specifically for use by security professionals. We will showcase the best-of-breed in both hacking hardware and software (ZigDiggity) that you'll need to build a complete ZigBee penetration toolkit. Each of the key concepts/tools will be accompanied with live hacking demonstrations that will be both exciting as well as educational, including:

ZigBee – disabling home security system door/window alarms via ZigBee DoS attacks
Scaling this same home ZigBee attack to an entire neighborhood by equipping Bishop Fox's DangerDrone with the ZigBee Hacking gear and new ZigDiggity toolset.

We'll also be giving away a fully functional Danger Drone to one lucky audience member, fully equipped and loaded with ZigDiggity hacking capabilities – guaranteed to leave your friends feeling peanut butter and jealous!


### ["HACKER MODE" FOR AMAZON ALEXA(TM)](#)  
![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category-Red--Teaming--/--Embedded](https://img.shields.io/badge/Category-Red--Teaming--/--Embedded-gray)  
Have you ever been stuck at a command line, not quite remembering the syntax for a NetCat relay? Ever wish that buddy that has a photographic memory for man-pages was with you? Hacker Mode makes Amazon's Alexa(TM) be that epic hacker buddy for you!

The Hacker Mode skill designed for Alexa assists hackers and developers with:

HTML, Hex, URL, ASCII encodings
NetCat, NMap, and Metasploit command line interfaces
Well-known TCP and UDP ports, HTTP headers, HTTP response codes and HTTP verbs

Simply ask Alexa to enter "Hacker Mode" and then ask a question like: "How can I send a file with NetCat?" The app provides both voice feedback and Alexa App feedback to ensure you get the syntax just right.


---

## 🧩 Contributing

Contributions are welcome! Please:

- Add tools under the right category

- Use Markdown formatting like shown above

- Include at least: name, description, GitHub/project link, and relevant badges

- Optional: Create a `tools/tool-name.json` file with structured metadata

> See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines

---

## 📄 License

[MIT](LICENSE)

---

> Inspired by [Awesome Lists](https://awesome.re) and powered by the Black Hat Arsenal community.