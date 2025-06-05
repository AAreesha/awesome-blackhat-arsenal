# USA 2019
---
## 🧠 Tools by Category
### Red Teaming

<details><summary><strong>[AADInternals: PowerShell Module for Administering Azure AD and Office 365](https://github.com/Gerenios/AADInternals)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Nestori Syynimaa](https://img.shields.io/badge/Nestori%20Syynimaa-informational)

                AADInternals is a PowerShell module for administering Azure AD and Office 365. It is a result of hours of reverse-engineering and debugging of Microsoft tools related to Azure AD, such as PowerShell modules, directory synchronisation, and admin portals.

AADInternals contains tools for retrieving detailed information about Azure AD/Office 365 tenant not available otherwise, tools for manipulating Azure AD objects (e.g., users and passwords), and tools for creating backdoors to Azure AD/Office 365. The backdoor tools are based on the discovery and research of a vulnerability in Azure AD identity federation.

                </details>
                
<details><summary><strong>[Apfell: Multi-Platform Command and Control](https://github.com/its-a-feature/Mythic)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Cody Thomas](https://img.shields.io/badge/Cody%20Thomas-informational)

                Apfell is a collaborative, command and control platform designed to facilitate a plug-n-play architecture. It uses a web-based front-end so that it can be accessed from any OS and a Python/Docker based back-end. Apfell focuses on quality of life improvements for operators, especially while operating across macOS and *nix operating systems, such as searchable tasks, per-task comments, artifact tracking, MITRE ATT&CK mappings/exports, multiple concurrent c2 profiles, command versioning, and much more. It features a JavaScript for Automation (JXA) agent that runs in memory on macOS devices, but offers agents across a variety of platforms and services.

                </details>
                
<details><summary><strong>[AVET: AntiVirus Evasion Tool](https://github.com/govolution/avetosx)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Daniel Sauder](https://img.shields.io/badge/Daniel%20Sauder-informational)

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

                </details>
                
<details><summary><strong>[barq: The AWS Post-Exploitation Tool](https://github.com/Voulnet/barq)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Mohammed Aldoub](https://img.shields.io/badge/Mohammed%20Aldoub-informational)

                barq is a post-exploitation framework that allows you to easily perform attacks on a running AWS infrastructure. It allows you to attack running EC2 instances without having the original instance SSH keypairs. It also allows you to perform enumeration and extraction of stored Secrets and Parameters in AWS.

                </details>
                
<details><summary><strong>[Break out the Box (BOtB): Container Analysis, Exploitation and CICD Tool](https://github.com/brompwnie/botb)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Chris Le Roy](https://img.shields.io/badge/Chris%20Le%20Roy-informational)

                BOtB is the first tool aimed at hackers and developers to automate Container exploitation. BOtB is a tool that can be used to analyze and identify vulnerabilities for Containers such as LXC and Docker. Not only does BOtB provide the user with a detailed analysis of identified vulnerabilities of the container, BOtB provides an autopwn feature which allows for the user to automagically exploit the vulnerabilities identified and break out onto the host. BOtB is able to identify multiple container vulnerabilities and contains a vast collection of exploits to break out of the container. BOtB is also developer friendly and has a Continuous Integration Continuous Development (CICD) mode which when enabled, BOtB will attempt to autopwn identified vulnerabilities but instead of dropping to host shells, it will return exit codes greater than 0 which is used by CICD technologies to indicate failed tests. When used in an Agile SDLC process implementing DevSecOps principles, this can assist developers with identifying Container issues prior to production deployments. BOtB is written in Golang and is distributed as a binary for multiple platforms.

                </details>
                
<details><summary><strong>[CALDERA: Automating Adversary Emulation](https://github.com/0x4D31/awesome-threat-detection)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![David Hunt](https://img.shields.io/badge/David%20Hunt-informational)

                Adversary emulation is great, but it can be time consuming – so why not automate it? CALDERA automates the adversary emulation process, allowing users to run fully automated adversary emulation exercises, aligning its operations with MITRE ATT&CK. Blue and red teamers alike can use CALDERA for training, to test analytics and defensive tools, and just generally to stress test their networks and systems.


CALDERA was first released in late 2017 featuring its end-to-end “adversary mode” capability, where operators could use CALDERA to run fully end-to-end tests emulating the full adversary lifecycle. This mode allowed CALDERA to run intelligently and autonomously, leveraging a planning system to dynamically compose operations.


Since this first release, the MITRE team has continued to expand CALDERA’s capabilities, releasing a new “chain mode” in 2019. This new mode allows users much more control over CALDERA, letting them orchestrate and automate atomic unit tests as opposed to end-to-end operations. With more fine-grained control over CALDERA, users can better control their operations to accommodate more use cases, such as testing and refining analytics.


This demo will highlight both of CALDERA’s modes, providing demos and guides on how to use CALDERA including how to extend it with new plugins and adding additional tests. CALDERA is open source and can be downloaded off of the MITRE GitHub repository.

                </details>
                
<details><summary><strong>[Commando VM 2.0: Security Distribution for Penetration Testers and Red Teamers](https://github.com/mandiant/commando-vm)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Jacob Barteaux](https://img.shields.io/badge/Jacob%20Barteaux-informational) ![Blaine Stancill](https://img.shields.io/badge/Blaine%20Stancill-informational) ![Nhan Huynh](https://img.shields.io/badge/Nhan%20Huynh-informational)

                Commando VM is an open-source Windows-based security distribution designed for Penetration Testers and Red Teamers. It is an add-on from FireEye's very successful Reverse Engineering distribution: FLARE VM. Much like Kali Linux, Commando VM is designed with an arsenal of open-source offensive tools that will help operators achieve assessment objectives.

Being built on Windows, Commando VM comes with all the native support for accessing Active Directory environments. Additionally, Commando VM includes Web Application assessment tools, scripting languages (such as Python and Go), Information Gathering tools (such as Nmap, WireShark, and PowerView), Exploitation Tools (such as PowerSploit, GhostPack and Mimikatz), Persistence tools, Lateral Movement tools, Evasion tools, Post-Exploitation tools (such as FireEye's SessionGopher), Remote Access tools, Command-Line tools, and all the might of FLARE VM's reversing tools.

Commando VM 1.0 was greeted with tremendous enthusiasm and praise when it debuted at Black Hat Asia in Singapore this year; afterwards, it generated lots of media buzz. Less than two weeks after release our GitHub repository had over 2000 followers and over 400 forks. For Black Hat USA, we are debuting Commando VM 2.0, with full support for Kali on the Windows Subsystem for Linux, as well as giving users the ability to customize what tools get installed on their system.

                </details>
                
<details><summary><strong>[Dolos Cloak: Your NAC Can't See This](https://github.com/fkasler/dolos_cloak)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Forrest Kasler](https://img.shields.io/badge/Forrest%20Kasler-informational)

                Dolos Cloak is a new tool designed to give penetration testers and red team members the ability to easily bypass 802.1x network access controls. The tool performs an advanced man-in-the-middle attack against nearly any authorized network device, automatically configures a NAT to blend in, and pass legitimate traffic unaltered. Simply plug a Dolos Cloak device in between a network jack and an available workstation, IP phone, printer, or other device and walk away. Dolos Cloak can be configured to call home using TPC/UDP reverse shells, SSH, VPN, Empire, or other custom methods to maintain a stealthy foothold on the network. The creation of Dolos Cloak was inspired by sysadmins that thought they could rely solely on 802.1x to keep attackers off their networks.

                </details>
                
<details><summary><strong>[Fudge: A Collaborative C2 Framework for Purple Teaming](https://github.com/IvanLazarevsky/AIML_1sem/blob/master/nltk_feature_names4_wm.json)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Kris Anderson](https://img.shields.io/badge/Kris%20Anderson-informational)

                Fudge is a Python3/Flask web-based C2 framework and Powershell implant designed to facilitate purple teaming activities, post-campaign review and timelining.

Fudges' inception is based on 3 main areas:

Creating a suitable way for blue teamers to review the chronological activities a red team engagement, allowing them to assess if key alerts were missed.
Finding ways to incrementally increase detection rates, allowing defenders to identify the intrusion. This provides a gauge of skill & target areas for upskilling if the intrusion is not identified.
Providing a way for junior testers to experience red teaming without increasing risk to the campaign OpSec/client network.
Purple teaming was born out of the need for tighter integration between offensive and defensive teams. If the red team is successful in compromise, their ability to export the campaign timeline and logging can prove invaluable insight to the blue team. Allowing defenders to review network and host logs as they follow a campaign timeline, allows for blind spots to be identified and tooling adjusted and tuned.

Fudges' implant also supports varying levels and types of obfuscation to allow for varying levels of noise to be made during the engagement to help a SoC benchmark their detection skills.

Lastly, Fudge is designed around team usage, which allows for a senior red teamer to allow another user to have read or read/write access to the campaign. These access controls allow a junior member to view the campaign and see the kind of commands, and techniques used in a post-exploitation environment.

Fudge can be found on Github at: https://github.com/Ziconius/Fudge

                </details>
                
<details><summary><strong>[Kube-Hunter: Pentest Platform for Kubernetes Environments](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Containers.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Michael Cherny](https://img.shields.io/badge/Michael%20Cherny-informational)

                Kubernetes is today's most popular container orchestrator. But it's also a complex distributed system, with defaults tuned for usability rather than for security. More so, configuring Kubernetes correctly is not trivial. Failing to configure Kubernetes in a secure way exposes the applications running on it to imminent risk, regardless of how securely those application are built.

We recognized the need to assess the level of security of a Kubernetes cluster deployment, and built kube-hunter to be an extensible pentesting and risk assessment platform for Kubernetes environments. We contributed quite a few discovery and hunt techniques from the get-go, and will add more over time. Kube-hunter is also designed to be easily extended by the community. This is the current list of tests:
Passive Tests (tests not making any change to the cluster):

Generates ip addresses to scan, based on cluster/scan type
Scans known Kubernetes ports to determine open endpoints for discovery
Checks for an open API Server
Checks for open Kubelet ports
Checks for an open Proxy service
Checks for email addresses in kubernetes ssl certificates
Hunts for a dashboard behind the proxy
Hunts open Dashboards, gets the type of nodes in the cluster
Reads specific endpoints on open ports in the readonly Kubelet server
Hunting Azure cluster deployments using specific known configurations
Hunting etcd, checks for remote availability of etcd, its version, and read access to the DB
Hunting API server using the service account token obtained from a compromised pod
Vulnerabilities hunter:
○ CVE-2018-1002105
○ CVE-2019-1002100

Active Tests (may perform state-changing actions on the cluster):

Retrieves logs from a random container
Hunts Proxy when exposed, extracts the version
Hunts when proxy is exposed, extracts the build date of kubernetes
Executes uname inside of a random container
Gets the Azure subscription file on the host by executing inside a container
Hunting etcd, checks for remote write access to etcd- will attempt to add a new key to the etcd DB
Accessing the api server might grant an attacker full control over the cluster

                </details>
                
<details><summary><strong>[Lauschgerät: Gets in the Way of your Victim's Traffic and Out of Yours](https://github.com/SySS-Research/Lauschgeraet)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Adrian Vollmer](https://img.shields.io/badge/Adrian%20Vollmer-informational)

                Lauschgerät gets in the way of your victim and out of yours. This python tool acts as a convenient man-in-the-middle tool to sniff traffic, terminate TLS encryption, host malicious services and bypass 802.1X - provided you have physical access to the victim machine, or at least its network cable.

There are three ways to run it: Either on its own dedicated device like a Raspberry Pi or Banana Pi, in a virtual machine with two physical USB-NICs attached, or on your regular pentest system in its own network namespace. It will look like a completely transparent piece of wire to both victim systems you are getting in the middle of, even if they are using 802.1X because it is implementing the ideas presented in a talk by Alva Lease 'Skip' Duckwall IV.

The Lauschgerät operates with three interfaces: Two interfaces going to the victim client and the victim switch respectively, and one management interface which you can connect to and initiate the redirection of traffic, inject your own traffic, start and stop malicious services, and so forth. It comes with a few services included, such as a service that terminates TLS encryption (which will of course cause a certificate warning on the victim's end) or a service that performs the classic "SSL strip" attack. And more to come!

An optional wireless interfaces can either be used as another management interface or for intercepting traffic of wireless devices. The management can be done via SSH or via a web application, making sure you can hit the ground running.

                </details>
                
<details><summary><strong>[Mr.SIP: SIP-Based Audit & Attack Tool](https://github.com/meliht)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Ismail Melih Tas](https://img.shields.io/badge/Ismail%20Melih%20Tas-informational)

                Mr.SIP is a simple console based SIP-based Audit and Attack Tool. Originally it was developed to be used in academic work to help developing novel SIP-based DDoS attacks and then the idea has been converted into a fully functional SIP-based penetration testing tool. So far, it has been used more than 5 journal papers. Mr.SIP can also be used as SIP client simulator and SIP traffic generator.

The initial academic journal paper which Mr.SIP is used is titled "Novel SIP-based DDoS Attacks and Effective Defense Strategies" published in Computers & Security 63 (2016) 29-44 by Elsevier, Science Direct http://sciencedirect.com/science/article/pii/S0167404816300980.

In the current state, Mr.SIP comprises 7 sub-modules named as SIP-NES (network scanner), SIP-ENUM (enumerator), SIP-DAS (DoS attack simulator), SIP-ASP (attack scenario player), SIP-EVA (eavesdropper), SIP-SIM (signaling manipulator) and SIP-CRACK (cracker). Since it provides a modular structure to developers, more modules will continue to be added by the authors and it is open to be contributed by the open-source developer community.

SIP-NES is a network scanner. It needs the IP range or IP subnet information as input. It sends SIP OPTIONS message to each IP addresses in the subnet/range and according to the responses, it provides the output of the potential SIP clients and servers on that subnet.

SIP-ENUM is a enumerator. It needs the output of SIP-NES and also pre-defined SIP usernames. It generates SIP REGISTER messages and sends them to all SIP components and try to find the valid SIP users on the target network. You can write the output in a file.

SIP-DAS is a DoS/DDoS attack simulator. It comprises four components: powerful spoofed IP address generator, SIP message generator, message sender and response parser. It needs the outputs of SIP-NES and SIP-ENUM along with some pre-defined files.

IP spoofing generator has 3 different options for spoofed IP address generation, i.e., manual, random and by selecting spoofed IP address from subnet. IP addresses could be specified manually or generated randomly. Furthermore, in order to bypass URPF filtering, which is used to block IP addresses that do not belong to the subnet from passing onto the Internet, we designed a spoofed IP address generation module. Spoofed IP generation module calculated the subnet used and randomly generated spoofed IP addresses that appeared to come from within the subnet.
SIP-DAS basically generates legitimate SIP INVITE message and sends it to the target SIP component via TCP or UDP. In the current state, it doesn't support instrumentation which helps you to understand the impact of the attack by using Mr.SIP, but we will support it very soon. In the current state, we can see the impact of the attack by checking the CPU and memory usage of the victim SIP server.

SIP is a text-based protocol such as HTTP but more complex than HTTP. For example, when we talk about SIP INVITE message, there are some specific headers and parameters need to be vendor specific and unique for each call. SIP Message Generator allows you to bypass security perimeters bu generating all these headers and parameters as it should be, so basic it is harder to be detected by anomaly detection engines that these messages are generated automatically. You can generate SIP methods such as INVITE message, REGISTER message, etc. You can specify the message count, the destination port, you can use predefined toUser list, fromUser list, userAgent list etc.

In order to bypass automatic message generation detection (anomaly detection) systems, random "INVITE" messages are generated that contained no patterns within the messages. Each generated "INVITE" message is grammatically compatible with SIP RFCs and acceptable to all of the SIP components.

"INVITE" message production mechanism specifies the target user(s) in the "To" header of the message. This attack can be executed against a single user or against legitimate SIP users on the target SIP server as an intermediary step before the DoS attack. The legitimate SIP users are enumerated and written to a file. Next, they are placed randomly in the "To" header of the generated "INVITE" messages. "Via, "User-Agent, "From," and "Contact" headers within an "INVITE" message were syntactically generated using randomly selected information from the valid user agent and IP address lists. The tag parameter in the "From" header, the branch and source-port parameters in the "Via" header, and the values in the "Call-ID" header are syntactically and randomly generated using the valid user agent list. In addition, the source IP addresses in the "Contact" and "Via" headers are also generated using IP spoofing.

UDP is used widely in SIP systems as a transport protocol, so attacks on the target server are implemented by sending the generated attack messages in the network using UDP. Also, TCP can be used optionally. The message sender of SIP-DAS allows the optional selection of how many SIP messages could be sent during one second. The number of SIP messages sent in one second depended on the resources (CPU and RAM) of the attacker machine.

SIP-ASP is Attack Scenario Player. It is working like a sub-function of SIP-DAS. It has a powerful parser and allows you to create stateful SIP attack call flows. In our academic studies, we have developed new attack vectors by using our SIP-DAS and SIP-ASP such as re-transmission based DDoS attacks and reflection based DRDoS attacks.

SIP-EVA is an eavesdropper. It sniffs the target network and can grasp the SIP messages. It allows you to extract call specific information such as who is calling, who is called, the duration of the call, the unique call-ID value and you can even download the media content of the call.

SIP-SIM is a signaling manipulator. It is working like an Intercepting SIP Proxy. It uses the same sniffer mechanism with SIP-EVA but it allows you to catch the messages between clients and server and you can replicate the messages and manipulate some headers and/or parameters as you want and send it to the victim server. By using SIP-SIM you can do Caller-ID spoofing attacks. SIP-SIM support both LAN-based and WAN-based Caller-ID spoofing attacks. But in order to make WAN-based Caller-ID spoofing attack, you need to have proper service provider account.

SIP-CRACK is a password cracker. Again, it uses the same sniffing mechanism and it allows you to catch the SIP REGISTER messages, extract the authentication data such as hash values. You can do brute-force based cracking, or you can choose a dictionary or rainbow table cracking. So SIP is a time-critical protocol and cracking should be an offline attack.

                </details>
                
<details><summary><strong>[PivotSuite: Hack The Hidden Network - A Network Pivoting Toolkit](https://github.com/RedTeamOperations/PivotSuite)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Manish Gupta](https://img.shields.io/badge/Manish%20Gupta-informational)

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

                </details>
                
<details><summary><strong>[PowerShell-RAT](https://github.com/Viralmaniar/Powershell-RAT/actions)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Viral Maniar](https://img.shields.io/badge/Viral%20Maniar-informational)

                PowerShell-RAT is a stealthy tool which exfiltrates sensitive information from the Windows environment through screenshots and keystrokes. The exfiltrated information is sent to a malicious user over a HTTPS protocol in the form of email attachments. The RAT can be invoked with a single key press using 'Hail Mary' option. Gmail is used to receive files from the backdoored machine. As Gmail is considered one of the highly trusted domains, this would allow an attacker to avoid network detection by NextGen Firewalls.

During a Red Team engagement, this tool can be executed on any Windows machine which backdoors the user machine using a number of task schedulers which will run the PowerShell scripts. Once backdoored, malicious user receives screenshots of the user activities via email every 5 minutes. After the email is received, screenshots are deleted from the machine to clean up the disk space, hence, avoiding the detection.

On successful authentication on a Windows machine, backdoor triggers the keystroke module on the user machine. It saves every key press via keyboard in the "log.txt" file on the user machine and sends it to the malicious user every hour as an email attachment. Setup requires a dedicated throw away Gmail account with modification to PowerShell script credential variables and a malicious user needs to enable "Allow less secure apps" under the security settings of the Gmail account to receive screenshots and key logs from the backdoored machine.

Target system can be identified using attachments naming convention which is Computer name followed by the timestamp. The backdoor Python file can be converted into an executable using Pyinstaller. During demo, I would also walk through a number of defence mechanisms to detect stealthy backdoors using publicly available tools such as Sysinternals from Microsoft.

                </details>
                
<details><summary><strong>[Router Exploit Shovel: Automated Application Generation for Stack Overflow Types on Wireless Routers](https://gist.github.com/Lysak/a0ca30a3e6732d39199b27c170a8cd28)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Qinghao Tang](https://img.shields.io/badge/Qinghao%20Tang-informational) ![Yuan Zhuang](https://img.shields.io/badge/Yuan%20Zhuang-informational)

                Router exploits shovel is an automated application generation tool for stack overflow types on wireless routers. The tool implements the key functions of exploits, it can adapt to the length of the data padding on the stack, generate the ROP chain, generate the encoded shellcode, and finally assemble them into a complete attack code. The user only needs to attach the attack code to the overflow location of the POC to complete the Exploit of the remote code execution. The tool also incorporates live recovery, leaving no trace of attack after the Exploit attack is completed.

                </details>
                
<details><summary><strong>[Scapy: Python-Based Interactive Packet Manipulation Program + Library](https://github.com/secdev/scapy)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Guillaume Valadon](https://img.shields.io/badge/Guillaume%20Valadon-informational)

                Scapy (https://github.com/secdev/scapy) is a renowned packet manipulation tool written in Python that supports a wide number of protocols on many different platforms (Linux, macOS, *BSD, and Windows). Initially developed by Philippe Biondi since 2003, it is now maintained by Guillaume Valadon, Pierre Lalet and Gabriel Potter. While the existence of this tool is well-known, its grip is much less, to the community's detriment. This presentation aims at filling this gap using practical and detailed examples.

                </details>
                
<details><summary><strong>[SILENTTRINITY (v0.2.0): Async Post-Exploitation Agent Powered by Python, C# & .NET's DLR](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/RT.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Marcello Salvati](https://img.shields.io/badge/Marcello%20Salvati-informational)

                SILENTTRINITY is an asynchronous post-exploitation agent powered by Python, IronPython, C# and .NET's DLR (Dynamic Language Runtime), it attempts to weaponize and demonstrate the flexibility that BYOI (Bring Your Own Interpreter) payloads have over traditional C# implants. What are BYOI payloads? Turns out, by harnessing the sheer craziness of the .NET framework, you can embed entire interpreters inside of .NET languages allowing you to natively execute scripts written in third-party languages (like Python) on windows! Not only does this allow you to dynamically access all of the .NET API from a scripting language of your choosing, but it also allows you to still remain completely in memory and has a number of advantages over traditional C# payloads! Essentially, BYOI payloads allow you to have all the "power" of PowerShell, without going through PowerShell in anyway! Additionally, you can nest multiple interpreters within each other to perform what I've coined "engine inception"! If you're interested in bleeding-edge and out of the ordinary C#/.NET offensive trade-craft, this is the demo for you!

                </details>
                
<details><summary><strong>[The Air-Gap Malware of X-Sploit](https://github.com/Trustworthy-AI-Group/Adversarial_Examples_Papers)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Jie Fu](https://img.shields.io/badge/Jie%20Fu-informational) ![Yongtao Wang](https://img.shields.io/badge/Yongtao%20Wang-informational) ![Jinglun Li](https://img.shields.io/badge/Jinglun%20Li-informational)

                X-Sploit is a Linux-based Red-Teaming-Toolkit for IT security experts and geeks. In this presentation, we will introduce a physical penetration tip, the Air-gap malware in X-Sploit Toolkit. The victim device's hardware adapter could be controlled and used for backdoor data transmission without interfering with the target's existing connection status and communication.


Advantage:
Cross-platform support (Windows, Mac OS, Linux)
Bypass Firewall/IDS/IPS
No signature, more difficult to detect
Used in isolate network environment attack
Does not affect the victim's existing connection status and communication

                </details>
                
<details><summary><strong>[WIG: Wi-Fi Information Gathering](https://github.com/6e726d)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Andres Blanco](https://img.shields.io/badge/Andres%20Blanco-informational)

                WIG (Wi-Fi Information Gathering) is a free and open source (GPLv3) utility for IEEE 802.11 device fingerprinting. WIG uses Wi-Fi network interfaces that supports monitor mode to obtain information on nearby devices with Wi-Fi support. The tool supports vendors proprietary protocols such as Apple AirDrop/AirPlay, Cisco Client eXtensions, Wi-Fi Protected Setup (WPS) and Wi-Fi Direct. Using these protocols the tool is able to find and fingerprint potential Wi-Fi targets that other tools are not able to find. The tool output it's useful on the threat modeling phase during wi-fi penetration testing or to find potential targets during a network assessment.

                </details>
                
<details><summary><strong>[WMImplant: An Offensive Use Case of WMI](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/RT.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Chris Truncer](https://img.shields.io/badge/Chris%20Truncer-informational)

                When looking forward to the latest defenses that are being seen in environments all over the world today, we're consistently seeing EDR, "Next-Gen AV", and application whitelisting. Of the available defenses, application whitelisting seemed like the most interesting challenge to undertake. We wanted to build something that would work against one of the best application whitelisting solutions from a detection/prevention perspective, Windows Defender Application Control (WDAC), previously known as Device Guard.

WDAC aims to lock down Windows workstations via multiple methods, one example is digital signature based rule enforcement when determining if an application is allowed to execute. Another, is that WDAC automatically enforces PowerShell into Constrained Language Mode (CLM), a severely restricted version of PowerShell. So how can you operate in a restricted WDAC environment?

WMImplant is one possible answer. Why not leverage a service that is built in to Windows and enabled by default since the days of Windows Server 2000? Windows Management Instrumentation (WMI) enables us to execute commands on systems, remotely and locally. WIth the enforcement of PowerShell Constrained Langauge Mode (CLM), our PowerShell based code had to adhere to the restrictions of the language mode. WMImplant is fully PowerShell CLM compliant and is designed to provide a Meterpreter-esque menu for users to easily perform post-exploitation tasks against the targeted system.

Come learn how a CLM compliant code-base designed to operate exclusively over WMI can allow you to survive and thrive in a heavily restricted application whitelisting environment.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[ACT: Semi-Automated Cyber Threat Intelligence](https://gist.github.com/georgepar/3d5cda48c50c6ee57f56aaea9b99603d)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Martin Eian](https://img.shields.io/badge/Martin%20Eian-informational)

                ACT is an open-source threat intelligence platform that has been built from the ground up to address the real-world needs of security analysts, incident responders and threat researchers across all industries. The platform is the product of a 3-year collaborative research project between the private sector, security agencies, CERTs and universities.


ACT enables advanced threat enrichment, threat analysis, visualisation, process automation, lossless information sharing and powerful graph analysis. Its modular design and APIs facilitate implementing new workers for enrichment, analysis, information sharing, and countermeasures.


Included in the platform is Scio, a component that ingests human-readable reports, like threat advisories and blog posts, and uses natural language processing and pattern matching to extract structured threat information to import to the platform. Our Github repositories also include support for information import and data enrichment from MISP, MITRE ATT&CK, VirusTotal, PassiveDNS, ShadowServer and Splunk, with more on the way.


So why build yet another threat intelligence platform?
In 2014 we set out to find a platform on the market to meet the needs of our SOC and threat intelligence team. Our requirements were not particularly unique: we needed a platform that would help us to collect and organise our knowledge of threats, facilitate analysis and sharing, and make it easy to retrieve that knowledge when needed. We spent too much time on manual processes, copy-pasting information between different systems. Much of our knowledge was in an unstructured form, like threat reports, that made it difficult and time consuming to figure out if we had relevant knowledge that could help us decide how to handle security alerts and security incidents.


Sound familiar? After evaluating the existing platforms, we concluded they could not easily be adapted to meet our requirements. In speaking with our partners, customers and the security community, we saw we were not alone and decided to research and develop a new platform: ACT.


This session will focus on threat analysis using the GUI to demonstrate how ACT can help SOC analysts, incident responders and threat analysts/hunters/researchers.

Source code: https://github.com/mnemonic-no/act

                </details>
                
<details><summary><strong>[BLACKPHENIX: Malware Analysis + Automation Framework](https://github.com/fortinet/ips-bph-framework)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Chris Navarrete](https://img.shields.io/badge/Chris%20Navarrete-informational)

                Various approaches have been developed through the years for malware analysis and vary from static, dynamic, behavioral, network, memory, and automated. Each analyst has developed his/her own strategy when analyzing malware. However, the accuracy of the results relies densely on their knowledge of system internals, analytical skills, and even reverse engineering. Therefore, novice analysts generate a strict dependency on experienced people to ensure the proper delivery of threat reports.

Even experienced analysts and reverse engineers could miss critical details, such as unexplored code paths, a specific or new self-defense mechanism, a challenging obfuscation algorithm difficult to decipher quickly, or hidden data that was not revealed in early stages. All of this is due to time constraints or a potential lack of information tracking throughout the analysis process.

BLACKPHENIX performs an Intelligent Automation and Analysis by combining all the known malware analysis approaches, automating the time-consuming stages and counter-attacking malware behavioral patterns. The objective: generate precise IOCs by revealing the real malware purpose and exposing its hidden data and related functionalities that are used to exfiltrate or compromise the user's information.

This framework focuses on consolidating, correlating, and cross-referencing the data collected between analysis stages by the execution of Python scripts and helper modules, providing full synchronization between the debugger, disassembler, and supporting components. The automation modules allow interaction with external tools and libraries that can be used to scale the framework functionality by developing plug-ins on top of it, allowing people of any skill level adapt it to their needs and producing actionable threat information in the shape of technical threat reports, IPS/AV signatures or the discovery of new malware attacks, variants or families.

The presentation will include a live demo of the system processing real different categories of malware taken from the wild.

                </details>
                
<details><summary><strong>[Cloud Security Suite: One-Stop Tool for AWS/GCP/Azure Security Audit](https://github.com/jayeshchauhan)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Jayesh Chauhan](https://img.shields.io/badge/Jayesh%20Chauhan-informational)

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

                </details>
                
<details><summary><strong>[CyBot: Open-Source Threat Intelligence Chat Bot (Platform Enhanced)](https://github.com/ali-ce/datasets/blob/master/Artificial-Intelligence/ChatterbotsDB.csv)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Tony Lee](https://img.shields.io/badge/Tony%20Lee-informational)

                Threat intelligence chat bots are useful friends. They perform research for you and can even be note takers or central aggregators of information. However, it seems like most organizations want to design their own bot in isolation and keep it internal. To counter this trend, our goal was to create a repeatable process using a completely free open source framework, an inexpensive Raspberry Pi (or even virtual machine), and host a community-driven plugin framework to open up the world of threat intel chat bots to everyone from the average home user to the largest security operations center.

We were thrilled to debut the end result of our research (a chat bot that we affectionately call CyBot) at Black Hat Arsenal Vegas 2017. To build on that momentum we also brought CyBot to Black Hat Europe and Asia to gather more great feedback and ideas from an enthusiastic international crowd. This year's Black Hat Vegas will allow us to share new features that stemmed from Black Hat feedback as well as enhancements provided by a platform upgrade.

Best of all, if you know even a little bit of Python, you can help our global collaboration efforts by writing plugins and sharing them with the community. If you want to build your own CyBot, the instructions in this project will let you do so with about an hour of invested time and anywhere from $0-$35 in expenses. Come make your own threat intelligence chat bot today!

                </details>
                
<details><summary><strong>[EventList](https://github.com/miriamxyra)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Miriam Wiesner](https://img.shields.io/badge/Miriam%20Wiesner-informational)

                EventList: What the log?! So many events, so little time...
Detecting adversaries is not always easy - especially when it comes to correlating Windows Event Logs to real-world attack patterns and techniques. EventList helps to match Windows Event Log IDs with the MITRE ATT&CK framework (and vice-versa) and offers methods to simplify the detection in corporate environments worldwide.

Use this tool to:

Import either MSFT Baselines or custom GPOs
Find out immediately which Events are being generated and what MITRE ATT&CK techniques are being covered by the selected Baseline/GPO
Choose MITRE ATT&CK techniques and generate GPOs to generate the events needed for detection
Generate Agent Forwarder Configs to only cover the events needed for the detection (avoid being "Log spammed")
Generate Queries to detect the chosen MITRE ATT&CK techniques, regardless of the SIEM solution used

                </details>
                
<details><summary><strong>[IOC Explorer: Correlate IOC in Automatic Way](https://github.com/lion-gu/ioc-explorer)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Lion Gu](https://img.shields.io/badge/Lion%20Gu-informational)

                IOC correlation is usually a manual or semi-automatic work. It takes a lot of time to search multiple data sources and process different IOC types. IOC Explorer aims to introduce an automatic way to search data across major OSINT sources, like VirusTotal. Moreover, recursive searching feature will explore more possible IOCs based on previous IOCs, then build IOC relations automatically.

Source Code: https://github.com/lion-gu/ioc-explorer

                </details>
                
<details><summary><strong>[LMYN: Let's Map Your Network](https://github.com/varchashva/LetsMapYourNetwork)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Pramod Rana](https://img.shields.io/badge/Pramod%20Rana-informational)

                It is of utmost importance for any security engineer and network administrator to understand their network before securing and managing it, and it becomes a daunting task to have a 'true' understanding of a widespread network. In a mid to large-size organisation's network, having a network architecture diagram doesn't provide a complete understanding, and manual verification is a nightmare. Hence, in order to secure and manage entire network, it is important to have a complete picture of all the systems connected to your network.

BOTTOM LINE - YOU CAN'T SECURE WHAT YOU ARE NOT AWARE OF.

LetsMapYourNetwork (LMYN) aims to provide an easy-to-use interface to visualise any network in graphical-form with zero manual error at any point-of-time, where a node represents a system and relationship between nodes represents the connection.

Key Features

Project management
Bulk load of existing CMDB
Ability to perform on-demand network activities
Cloud (AWS) support
Enumeration
Ability to analyse 'interesting' network only
Continuous monitoring
Segregation of backend activities and UI
Docker support

                </details>
                
<details><summary><strong>[Malboxes](https://github.com/GoSecure/malboxes/releases)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Olivier Bilodeau](https://img.shields.io/badge/Olivier%20Bilodeau-informational) ![Maxime Carbonneau](https://img.shields.io/badge/Maxime%20Carbonneau-informational)

                Malboxes is a tool to streamline and simplify the creation and management of virtual machines used for malware analysis.

Building analysis machines is a tedious task. One must have all the proper tools installed on a VM such as a specific version of vulnerable software (ie: Flash), Sysinternal tools, debuggers (Windbg), network traffic analyzers (Wireshark), man-in-the-middle tools (Fiddler). One must also avoid leaking his precious proprietary software licenses (IDA). At the moment, this menial job is not automated and is repeated by every analyst.

Malboxes leverages the DevOps principle of infrastructure as code to enable researchers to automatically create fully operational and reusable analysis machines. The tool uses Vagrant and Packer to do an initial out-of-band bootstrapping. Afterward, chocolatey is used to install further tools benefiting from the chocolatey package repository.

Attendees will learn a simple tool for safe malware analysis practice that is easy to grasp, enabling them to start doing analysis faster. Seasoned malware researchers will also gain from this demo by seeing how the DevOps approach can be applied to simplify and accelerate their labs' malware reverse-engineering capacity or reduce its management overhead.

                </details>
                
<details><summary><strong>[SilkETW: Collecting Actionable ETW Data](https://github.com/FuzzySecurity/BH-Arsenal-2019)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Ruben Boonen](https://img.shields.io/badge/Ruben%20Boonen-informational)

                Event Tracing for Windows (ETW) provides researchers with a rich data set which can be leveraged both for defensive as well as offensive purposes. ETW collectors can alert the user to malicious behavior such as user-land APC injection from the Kernel, or equally, allow an attacker to spy on keyboard and mouse activity. The scope for ETW research is large but the information security community has been slow to adopt it. The two primary problems with ETW are: the complexities involved in event collection, and the volume of data that is generated.

SilkETW is a flexible C# ETW wrapper which attempts to mitigate the aforementioned issues by providing a straightforward interface for data collection, various filtering mechanics, and an output format that can be easily processed. ETW output can be written locally to disk, to the Windows event log or shipped off (using POST requests) to 3rd party infrastructure such as Elasticsearch.

This project was originally implemented by the FireEye Advanced Practices (AP) team to aid in the rapid analysis of novel attacker trade-craft, and to feed that analysis back into the detection engineering process.

                </details>
                
<details><summary><strong>[Splunk Threat Hunting Application](https://github.com/olafhartong/ThreatHunting)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Olaf Hartong](https://img.shields.io/badge/Olaf%20Hartong-informational)

                This is a Splunk application containing several dashboards and over 120 reports that will facilitate initial hunting indicators to investigate. One of the reasons this app was created is because the endpoint is an often used entry way into a network. There are quite some Endpoint Detection & Remediation (EDR) solutions out there and most of them are quite good; however, they can be costly and not everyone is able to afford that (yet).

The goal was to create an alternative approach to the detection aspect, using the MITRE ATT&CK framework and work with the existing environment. It allows you to leverage your existing data platform, in this case Splunk.

                </details>
                
<details><summary><strong>[SysmonX: An Augmented and Community-Driven Drop-In Replacement of Sysmon](https://github.com/marcosd4h/sysmonx)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Marcos Oviedo](https://img.shields.io/badge/Marcos%20Oviedo-informational) ![Joel Spurlock](https://img.shields.io/badge/Joel%20Spurlock-informational)

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

                </details>
                
<details><summary><strong>[Trash Taxi: Taking Out the Garbage in Your Infrastructure](https://github.com/jiayiwangjw/pythonstudy/blob/master/001_Essential%20notes002.py)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Patrick Cable](https://img.shields.io/badge/Patrick%20Cable-informational)

                Auditors dream of a world in which they can guarantee that few possess unrestricted administrator access. Yet, developers and operations staff often need to debug complex events - that only occur with load - in production. How can we balance the need to grant occasional superuser access with the incentive to ensure changes make their way back into configuration management, while reducing the risk of configuration drift? We built Trash Taxi to help us understand why people use "sudo -i," and also clean up hosts that have had arbitrary commands run on them by "taking out the trash" as in: terminating them.

                </details>
                
<details><summary><strong>[VECTR: Purple Teams Simulation Platform](https://github.com/Brian-MacMonigle/typing-speed-website/blob/master/WordFilter.py)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Chris Salerno](https://img.shields.io/badge/Chris%20Salerno-informational) ![Phil Wainwright](https://img.shields.io/badge/Phil%20Wainwright-informational)

                VECTR is a free tool and platform designed to facilitate your red and blue security teams through comprehensive purple team threat simulations. Document your attacks, develop metrics, gauge the effectiveness of your defensive tools, and improve your detection capabilities through historical performance tracking. We'll demo how to operationalize your purple teams and show measurable progress of your program with live test cases and simulations.

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[Alexa HackerMode 2.0: Voice Auto Pwn Using Kali Linux and Alexa Skill Combo](https://github.com/xssninja/HackerMode2.0)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![David Cross](https://img.shields.io/badge/David%20Cross-informational) ![Cate Jennison](https://img.shields.io/badge/Cate%20Jennison-informational) ![James Blackburn](https://img.shields.io/badge/James%20Blackburn-informational)

                HackerMode 2.0 code-named: "Death Star" is an Alexa driven auto-sploit tool designed for the cloud. Not only will it help with syntax and encodings, but it will go full hacker mode and exploit systems automatically for you.

"Alexa, ask HackerMode to hack IP address 192.168.1.135" will instruct Alexa to begin and manage the process of port scanning, fingerprinting, exploit selection, and smart brute forcing exploits through Metasploit 4 or 5.

Alexa will entertain you with mood music or various other activities while it roots and dumps users and passwords from your target. If the exploit is taking a while you can check in on the progress by asking "How's the hack going?"

                </details>
                
<details><summary><strong>[Medaudit: Auditing Medical Devices and Healthcare Infrastructure](https://github.com/anirudhduggal/medaudit)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Anirudh Duggal](https://img.shields.io/badge/Anirudh%20Duggal-informational)

                Medaudit is a healthcare/ medical device auditing tool that would help anyone auditing a healthcare networks and medical devices. At the time of writing, there are no tools - commercial or free - that can help security pentest healthcare infrastructure. This tool aims to close that gap and help security analysts use their web app skill set to analyze medical devices. The tool support HL7 protocol right now and will have support for FHIR and DICOM in near future.

The tool does the following things:

Create a visual map of HL7 traffic flow on a network (Passive analysis), extract HL7 traffic on the network.
Scan and verify for open HL7 ports on a host
Perform DOS attacks against HL7 streams on HL7 reciever
Send HL7 messages (malformed attacks)
Fuzzer
Malicious HL7 Server

The tool also acts a proxy using web API so you can reuse web application tests on medical devices.

                </details>
                
<details><summary><strong>[ShodanSeeker: Command-Line Tool Using Shodan API](https://github.com/laincode)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Laura Garcia](https://img.shields.io/badge/Laura%20Garcia-informational)

                The large number of assets published on the Internet - some of which organizations are not even aware of their existence - increase the probability of services being exposed that could put them at risk. As a first step towards resolving this problem, we introduce ShodanSeeker.

Taking advantage of Shodan's crawlers, ShodanSeeker analyzes historical records on-the-fly to discover differences between previously performed scans in order to identify new published services.

Enhancing the capabilities of Shodan's real-time stream of data, our fully customizable solution monitors and generates notification messages once a new risk service is discovered.

Presentation slides: https://drive.google.com/open?id=1Fi5XJ5-1QyXSawHKXVm_emF3NUR2Nx7X

                </details>
                

### Miscellaneous / Lab Tools

<details><summary><strong>[ARSENAL LAB - JTAGulator: Assisted Discovery of On-Chip Debug Interfaces](https://github.com/RakhithJK/Cyber-Security_Collection/blob/master/Readme_en.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Miscellaneous / Lab Tools](https://img.shields.io/badge/Category:%20Miscellaneous%20/%20Lab%20Tools-gray) ![Joe Grand](https://img.shields.io/badge/Joe%20Grand-informational)

                For over five years, the JTAGulator has been the de facto open source tool for identifying interfaces commonly used for hardware hacking, such as JTAG and UART, from a target product's test points, vias, component pads, or connectors. The tool bridges the gap between gaining physical access to circuitry and exploiting it, and can save a significant amount of effort compared to traditional reverse engineering processes. For the first time at Black Hat Arsenal, attendees will have the opportunity to play with the JTAGulator and a variety of real-world embedded devices in an informal, hands-on environment.

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[Azucar: Multi-Threaded Plugin-Based Tool to Help Assess the Security of Azure Cloud Environment Subscription](https://github.com/nccgroup/azucar/blob/master/Azucar.ps1)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Juan Garrido](https://img.shields.io/badge/Juan%20Garrido-informational)

                Azucar is a multi-threaded plugin-based tool to help assess the security of Azure Cloud environment subscription. By leveraging the Azure API, Azucar automatically gathers a variety of configuration data and analyses all data relating to a particular subscription in order to determine security risks.

                </details>
                
<details><summary><strong>[cwe_checker: Hunting Binary Code Vulnerabilities Across CPU Architectures](https://gist.github.com/DaffyDuke/06c022992b3e9e3de76e819c95c55e0b)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Nils-Edvin Enkelmann](https://img.shields.io/badge/Nils-Edvin%20Enkelmann-informational) ![Thomas Barabosch](https://img.shields.io/badge/Thomas%20Barabosch-informational)

                cwe_checker is an open source suite of tools to detect common bug classes like Use After Free (CWE-416) or Null Pointer Dereference (CWE-476). These bug classes are formally known as Common Weakness Enumerations (CWEs). Its main goal is to quickly point analysts to vulnerable code paths in binaries (e.g. firmware) without access to the source code.

cwe_checker is built on top of the Binary Analysis Platform (BAP). By using an intermediate representation for the binary code it can analyze ELF binaries of different CPU architectures, including x86/64, ARM, MIPS, and PPC. It has a modular and extensible architecture implementing static and dynamic analysis techniques. So far cwe_checker implements checks for more than 15 CWE classes including CWE-190 (Integer Overflow), CWE-415 (Double Free), and CWE- 676 (Use of Potentially Dangerous Function).

In addition, cwe_checker has been adopted as a core plugin for the Firmware Analysis & Comparison Tool (FACT). This enables analysts to hunt for vulnerabilities in large firmware data sets. Furthermore, the results of cwe_checker are exportable and there is an IDA Pro plugin that highlights any findings in the binary.

                </details>
                
<details><summary><strong>[Scout Suite: A Multi-Cloud Security Auditing Tool](https://github.com/nccgroup/ScoutSuite/wiki)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Xavier Garceau-Aranda](https://img.shields.io/badge/Xavier%20Garceau-Aranda-informational)

                Scout Suite (https://github.com/nccgroup/ScoutSuite) is an open source multi-cloud security-auditing tool, which enables security posture assessment of cloud environments. Using the APIs exposed by cloud providers, Scout Suite gathers configuration data for manual inspection and highlights risk areas. Rather than going through dozens of pages on the web consoles, Scout Suite presents a clear view of the attack surface automatically.

The following cloud providers are currently supported:

Amazon Web Services
Microsoft Azure
Google Cloud Platform

During the presentation, we will run Scout Suite against a number of cloud environments preconfigured with typical flaws. We will display how Scout Suite can be used to identify and help with remediation of security misconfigurations.

We will also release support for a number of new cloud providers (Oracle Cloud Infrastructure, Alibaba Cloud & IBM Cloud), and demonstrate how Scout Suite's cloud-agnostic architecture allows for great extensibility.

Presentation Slides: https://github.com/nccgroup/ScoutSuite/files/3502099/BH.Arsenal.2019.Scout.Suite.pdf

                </details>
                
<details><summary><strong>[SimpleRisk GRC](https://github.com/aparsons/simplerisk)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Josh Sokol](https://img.shields.io/badge/Josh%20Sokol-informational)

                As security professionals, almost every action we take comes down to making a risk-based decision. Web application vulnerabilities, malware infections, physical vulnerabilities, and much more all boils down to some combination of the likelihood of an event happening and the impact it will have. Risk management is a relatively simple concept to grasp, but the place where many practitioners fall down is in the tool set. The lucky security professionals work for companies who can afford expensive GRC tools to aide in managing risk. The unlucky majority out there usually end up spending countless hours managing risk, via spreadsheets. It's cumbersome, time consuming, and just plain sucks. After starting a Risk Management program from scratch at a $1B/year company, Josh Sokol ran into these same barriers and where budget wouldn't let him go down the GRC route, he finally decided to do something about it. SimpleRisk is a simple and free tool to perform risk management activities. Based entirely on open source technologies and sporting a Mozilla Public License 2.0, a SimpleRisk instance can be stood up in minutes and instantly provides the security professional with the ability to submit risks, plan mitigations, facilitate management reviews, prioritize for project planning, and track regular reviews. It is highly configurable and includes dynamic reporting and the ability to tweak risk formulas on the fly. It is under active development with new features being added all the time. SimpleRisk is Enterprise Risk Management simplified.

                </details>
                
<details><summary><strong>[TaintedLove: Dynamic Security Analysis Tool for Ruby](https://github.com/Shopify/tainted_love/blob/master/tainted_love.gemspec)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Benoit Côté-Jodoin](https://img.shields.io/badge/Benoit%20Côté-Jodoin-informational)

                TaintedLove is a dynamic security analysis tool for Ruby. It leverages Ruby's object tainting and monkey patching features to identify potentially vulnerable code paths at runtime. TaintedLove is library agnostic and provides a simple framework to extend the detection of unsafe method usage and user input tracking.

                </details>
                

### OSINT

<details><summary><strong>[Dradis Framework: Combine the Output of 20 Scanners and Automate Your Reporting](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Docs_and_Reports.md?plain=1)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

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

                </details>
                
<details><summary><strong>[PasteHunter: Scanning Pastebin with Yara Rules](https://github.com/InQuest/awesome-yara)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Kevin Breen](https://img.shields.io/badge/Kevin%20Breen-informational)

                From a security analytics and Threat Intelligence perspective, Pastebin is a treasure trove of information. All content that is uploaded to Pastebin and not explicitly set to private (which requires an account) is listed and can be viewed by anyone.

Hackers and script kiddies are quick to push their warez on to the site for the world to see and developers/network engineers are prone to accidentally leaking internal configurations and credentials. Anyway, how can we the lowly security analyst sift through all this data and use it to our advantage? We can scrape Pastebin and check all the data uploaded to see if any of it is of interest to us. There are some tools that can monitors paste sites with a set of regular expressions but I wanted more control and flexibility.

Having used Yara extensively in Malware analysis and Threathunting I saw it as a powerful method for quickly scanning large amounts of data and identifying the contents.

Over the last two years of development Pastehunter has grown to include modular inputs that can read from any data source and process the data in to a searchable indexed data set that also has the ability to send notifications with minutes of data matching your rules going public.

Inputs include Pastebin, Github Gists and all StackExchange posted questions. Ouptuts include Elastic Search and SMS / WhatsApp / Slack amongst others.

                </details>
                
<details><summary><strong>[TALR: Automating the Sharing and Ingestion of SIEM Rules](https://github.com/SecurityRiskAdvisors/TALR)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: OSINT](https://img.shields.io/badge/Category:%20OSINT-lightgrey) ![Nick Ascoli](https://img.shields.io/badge/Nick%20Ascoli-informational) ![Kevin Foster](https://img.shields.io/badge/Kevin%20Foster-informational)

                Keeping up with the evolving landscape of attacker techniques can feel like an uphill battle. Many organizations use a SIEM to perform log correlation and analysis and can attest that keeping rules current is a challenge. To combat the burden of keeping pace with the offensive community, this presentation will detail a new initiative to develop, share, and assess the latest and greatest in alerting logic—the Threat Alert Logic Repository (TALR). TALR is a repository of curated SIEM rules, designed for quick and easy ingestion in to the SIEM tool of your choice. The TALR repository is a publicly available TAXII server intended to keep SIEM engineers and analysts up-to-date on the latest and greatest detection logic. The TALR agent will provide a means to submit new rules to the repository, and to download updates for the latest detection rules (using our repository, or any TAXII server hosting TALR formatted SIEM content).

Attendees will gain a comprehensive overview of TALR and understand how to incorporate it into their environments as a way to remain on the cutting edge of alerting logic, and as a means of enacting more contextualized and informed response.

                </details>
                

### Web/AppSec or Red Teaming

<details><summary><strong>[Electronegativity: Identify Misconfigurations and Security Anti-Patterns in Electron Applications](https://github.com/phosphore)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Lorenzo Stella](https://img.shields.io/badge/Lorenzo%20Stella-informational)

                Electronegativity is a tool to identify misconfigurations and security anti-patterns in Electron-based applications (electronjs.org).

This is the first and only tool capable of detecting potential weaknesses and implementation bugs when developing applications using Electron, as recommended in the official security guidelines of the Electron project. Software developers and security auditors can use this tool to create secure desktop applications using web technologies.

After being first introduced at Black Hat US 2017 (Electronegativity - A Study of Electron Security) and featured in Black Hat Asia 2019 (Preloading Insecurity In Your Electron), the tool will be showcased for the first time ever at the Black Hat USA 2019 Arsenal where we will demonstrate its potential by scanning well-known applications.

Come see live demonstrations of Electronegativity hunting Electron applications for vulnerabilities and walk away with an open-source (Apache 2.0) static analysis engine to help secure your Electron applications!

                </details>
                

### Web/AppSec

<details><summary><strong>[Ghost in the Browser: Backdooring with Shadow Workers](https://gist.github.com/pmarreck/28b3049a1a70b8b4f2eaff4466d0c76a)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Emmanuel Law](https://img.shields.io/badge/Emmanuel%20Law-informational) ![Claudio Contin](https://img.shields.io/badge/Claudio%20Contin-informational)

                Service Workers are all the rage for progressive web apps nowadays. This talk will take a look at Service Workers from a different perspective. We will be focusing on our tool called "Shadow Workers" that serves as an exploitation toolkit to weaponize Service Workers

We'll explore some of the tools features including the ability to implant a pseudo backdoor in the browser and ghost through a victim's browser session to sniff, manipulate, and even proxy data silently.

We'll demo the various persistence mechanisms our tool provides to keep service workers alive and demo how MITM can be done at the browser layer. We'll also release a compendium tool to provide various mitigation mechanisms against such attacks.

                </details>
                
<details><summary><strong>[JSShell: An Interactive XSS Management & Browser Debugging Tool](https://github.com/Den1al/JSShell)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Daniel Abeles](https://img.shields.io/badge/Daniel%20Abeles-informational)

                JSShell is an interactive multi-user web based javascript shell that enables the user to debug esoteric browsers and manage XSS (cross site scripting) campaigns. It was originally created during research to have the ability to debug remote esoteric browsers that did not have a simple debugging console. This tool can be also used to easily attach to a XSS (Cross Site Scripting) payload to achieve browser remote code execution (similar to the BeeF framework) and manage the vulnerability.

Version 2.0 is created entirely from scratch, introducing new exciting features, stability and maintainability.

                </details>
                
<details><summary><strong>[ReDTunnel: Explore Internal Networks via DNS Rebinding Tunnel](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Network_Attacks.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Tomer Zait](https://img.shields.io/badge/Tomer%20Zait-informational) ![Nimrod Levy](https://img.shields.io/badge/Nimrod%20Levy-informational)

                Did you wonder how you could browse target's internal network without deploying anything on the victim machine? Sounds like magic, right? Imagine that you could have a one-click setup that will provide you a magic tunnel from the outside world. That's when we came up with the "ReD Tunnel" idea. The design goal was to use tools that exist on the victim's device, like the browser, rather than rely on 0days to stay below the radar of the most advanced AV. To create this new capability, we decided to combine two concepts: JavaScript reconnaissance techniques and the DNS rebinding attack. Open your browser, wait until the victim visits your website and start browsing the internal websites in their network. Now, when red-teaming you could really "be a guest, but feel at home".

                </details>
                

### Social Engineering / General

<details><summary><strong>[King Phisher: A Phishing Campaign Toolkit](https://github.com/rsmusllp/king-phisher)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Social Engineering / General](https://img.shields.io/badge/Category:%20Social%20Engineering%20/%20General-pink) ![Spencer McIntyre](https://img.shields.io/badge/Spencer%20McIntyre-informational)

                King Phisher is a phishing toolkit created to meet the highly customized and flexible needs that offensively-focused security testers require. It boasts a wide range of features to facilitate it's use both on offensive, breaching-centric engagements as well as for user awareness training.

This arsenal demonstration will show the newer features that have been added to King Phisher in recent years. Viewers will see the latest campaign improvements including from the template selection process to gathering MFA tokens, validating submitted credentials and the Let's Encrypt integration. By integrating with Let's Encrypt through certbot, users are able to quickly and easily issue certificates for, and enable HTTPS for their phishing sites. Finally, viewers will see a demonstration of the newest plugins for campaign data management, the usage of various alerting services and finally SPAM evasion.

Source code: https://github.com/securestate/king-phisher

                </details>
                
<details><summary><strong>[Social Attacker: Automated Phishing on Social Media Platforms](https://github.com/Greenwolf/social_attacker)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Social Engineering / General](https://img.shields.io/badge/Category:%20Social%20Engineering%20/%20General-pink) ![Jacob Wilkin](https://img.shields.io/badge/Jacob%20Wilkin-informational)

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

                </details>
                
<details><summary><strong>[SPF: SpeedPhishing Framework](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/phishing/spf.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Social Engineering / General](https://img.shields.io/badge/Category:%20Social%20Engineering%20/%20General-pink) ![Adam Compton](https://img.shields.io/badge/Adam%20Compton-informational)

                SpeedPhishing Framework (SPF) is a small collection of tools which can assist penetration testers in quickly/automatically deploying phishing exercises in minimal time.

Among the various capabilities included with SPF is the ability to automate the phishing process of OSINT and target selection, deployment of one or more phishing websites, the crafting and sending of phishing emails to the targets, recording the results, and generating a basic report.

SPF also includes more advanced capabilities such as dynamically building new web phishing templates, automatically validating captured credentials against target mail servers and the pillaging of sensitive information, and SPF can assist in the phishing of multifactor authentication portals.

                </details>
                

### Reverse Engineering

<details><summary><strong>[The Go Reverse Engineering Tool Kit](https://gist.github.com/0xdevalias/4e430914124c3fd2c51cb7ac2801acba)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Joakim Kennedy](https://img.shields.io/badge/Joakim%20Kennedy-informational)

                The Go Reverse Engineering Tool Kit (go-re.tk) is a new open source toolset for analyzing Go binaries. The tool is designed to extract as much metadata as possible from stripped binaries to aid both reverse engineering and malware analysis. Gore can, for example, detect the compiler version used, extract type information and recover function information, including source code line numbers for functions and source tree structure.

The core library is written in Go, but the tool kit includes C-bindings and a library implementation in Python. When using the C-bindings or the Python library, it is possible to write plugins for other analysis tools such as IDA Pro and Ghidra. The toolset also includes "redress", a command line tool to "re-dress" stripped Go binaries. It can both be used standalone to print out extracted information from the binary or as a radare2 plugin to reconstruct stripped symbols and type information.

The goal with the tool kit is to lower the bar to enter for anyone that wants to analyze programs written in Go.

Source Code: https://github.com/goretk

                </details>
                
<details><summary><strong>[YARASAFE: Automatic Binary Function Similarity Checks with Yara](https://github.com/lucamassarelli/yarasafe)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Reverse Engineering](https://img.shields.io/badge/Category:%20Reverse%20Engineering-orange) ![Luca Massarelli](https://img.shields.io/badge/Luca%20Massarelli-informational)

                YARASAFE is a new Yara module that automates the generation of rules containing binary similarity checks. Given a binary function, YARASAFE computes automatically its signature and includes it into a rule that will match any similar function.

This module rely on SAFE, a tool developed to create embedding vectors to represent binary functions. SAFE generates similarity-preserving embeddings: given two similar functions, their SAFE embeddings will be similar.

To create the embedding of a desired function YARASAFE includes an IDA Pro plugin: it sufficient to select the function in IDA and run the plugin to obtain its embedding.

YARASAFE can be used to create automatically yara rules for different purposes:

- Malware hunting
- Library function recognition
- Vulnerable function detection

                </details>
                
