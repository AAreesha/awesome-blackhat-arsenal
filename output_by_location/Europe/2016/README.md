# Europe 2016
---
## 🧠 Tools by Category
### Red Teaming

<details><summary><strong>[APT2 - Automated Penetration Testing Toolkit](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/vulnerability_assessment/apt2.md)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Adam Compton](https://img.shields.io/badge/Adam%20Compton-informational) ![Austin Lane](https://img.shields.io/badge/Austin%20Lane-informational)

                Nearly every penetration test begins the same way; run a NMAP scan, review the results, choose interesting services to enumerate and attack, and perform post-exploitation activities. What was once a fairly time consuming manual process, is now automated! Automated Penetration Testing Toolkit (APT2) is an extendable modular framework designed to automate common tasks performed during penetration testing. APT2 can chain data gathered from different modules together to build dynamic attack paths. Starting with a NMAP scan of the target environment, discovered ports and services become triggers for the various modules which in turn can fire additional triggers. Have FTP, Telnet, or SSH? APT2 will attempt common authentication. Have SMB? APT2 determines what OS and looks for shares and other information. Modules include everything from enumeration, scanning, brute forcing, and even integration with Metasploit. Come check out how APT2 will save you time on every engagement.

                </details>
                
<details><summary><strong>[PowerMemory](https://github.com/giMini/PowerMemory/blob/master/PowerMemory.ps1)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Pierre-Alexandre Braeken](https://img.shields.io/badge/Pierre-Alexandre%20Braeken-informational)

                PowerMemory is a PowerShell post-exploitation tool. It uses Microsoft binaries and therefore is able to execute on a machine, even after the Device Guard Policies have been set. In the same way, it will bypass antivirus detection. PowerMemory can retrieve credentials information and manipulate memory. It can execute shellcode and modify process in memory (in userland and kernel land as a rootkit). PowerMemory will access everywhere in user-land and kernel-land by using the trusted Microsoft debugger aka cdb.exe which is digitally signed.We will cover the following subjects:User-land proof-of-concept: attacking the digest Security Support Provider byte per byte with PowerShell and Microsoft debugger to retrieve passwords from memoryKernel-land proof-of-concept: Direct Kernel Object Manipulation with PowerShell and Microsoft debugger o Hiding/Un-hiding a process o Protecting a process o Injecting all privileges in a process with SYSTEM identity o Pass-The-Token attackUser-land proof-of-concept: Injecting and executing a shellcode in a remote process with PowerShell and a Microsoft debuggerIf we have time, we will hack the minesweeper too :-)

                </details>
                
<details><summary><strong>[WarBerryPi](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/red_team/warberrypi.md)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Yiannis Ioannides](https://img.shields.io/badge/Yiannis%20Ioannides-informational)

                What if the only requirements for taking down a corporate network are 60 minutes and $35? Traditional hacking techniques and corporate espionage have evolved. Advanced attacks nowadays include a combination of social engineering, physical security penetration and logical security hacking. It is our job as security professionals to think outside the box and think about the different ways that hackers might use to infiltrate corporate networks.The WarBerry is a customized RaspBerryPi hacking dropbox which is used in Red Teaming engagements with the sole purpose of performing reconnaissance and mapping of an internal network and providing access to the remote hacking team while remaining covert and bypassing security mechanisms. The outcome of these red teaming exercises is the demonstration that if a low cost microcomputer loaded with python code can bypass security access controls and enumerate and gather such a significant amount of information about the infrastructure network which is located at, then what dedicated hackers with a large capital can do is beyond conception. The talk will be comprised of slides and a demonstration of the WarBerry's capabilities in a virtual network.

                </details>
                

### Web/AppSec

<details><summary><strong>[DeepViolet TLS/SSL Scanner](https://github.com/spoofzu/DeepViolet/blob/master/src/main/java/com/mps/deepviolet/api/CipherSuiteUtil.java)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Milton Smith](https://img.shields.io/badge/Milton%20Smith-informational)

                DeepViolet TLS/SSL scanner is an information gathering tool for secure web servers. Written in Java, DeepViolet is be run from the command line, as a desktop application, or included as an API in other programs. Use DeepViolet to enumerate web server cipher suites, display X.509 certificate metadata, examine X.509 certificate trust chains, and more. DeepViolet is an open source project written to help educate the technical community around TLS/SSL and strengthen our knowledge of security protocols while we improve security of our web applications. DeepViolet project is always looking for volunteers.

                </details>
                
<details><summary><strong>[From XSS to RCE 2.5](https://github.com/Varbaek/xsser)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Hans-Michael Varbaek](https://img.shields.io/badge/Hans-Michael%20Varbaek-informational)

                This presentation demonstrates how an attacker can utilise XSS to execute arbitrary code on the web server when an administrative user inadvertently triggers a hidden XSS payload. Custom tools and payloads integrated with Metasploit's Meterpreter in a highly automated approach will be demonstrated live, including post-exploitation scenarios and interesting data that can be obtained from compromised web applications. This version includes cool notifications and new attack vectors!

                </details>
                
<details><summary><strong>[OWASP CSRFGuard](https://github.com/aramrami/OWASP-CSRFGuard)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Azzeddine RAMRAMI](https://img.shields.io/badge/Azzeddine%20RAMRAMI-informational)

                OWASP CSRFGuard implements a variant of the synchronizer token pattern to mitigate the risk of CSRF attacks. In order to implement this pattern, CSRFGuard must offer the capability to place the CSRF prevention token within the HTML produced by the protected web application. CSRFGuard 3 provides developers more fine grain control over the injection of the token. Developers can inject the token in their HTML using either dynamic JavaScript DOM manipulation or a JSP tag library. CSRFGuard no longer intercepts and modifies the HttpServletResponse object as was done in previous releases. The currently available token injection strategies are designed to make the integration of CSRFGuard more feasible and scalable within current enterprise web applications. Developers are encouraged to make use of both the JavaScript DOM Manipulation and the JSP tag library strategies for a complete token injection strategy.CSRFGuard WikiPage: https://www.owasp.org/index.php/Category:OWASP_CSRFGuard_Project

                </details>
                
<details><summary><strong>[WSSAT - Web Service Security Assessment Tool](https://github.com/toolswatch/blackhat-arsenal-tools/blob/master/webapp_security/wssat.md)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Mehmet Yalcin YOLALAN](https://img.shields.io/badge/Mehmet%20Yalcin%20YOLALAN-informational) ![Salih TALAY](https://img.shields.io/badge/Salih%20TALAY-informational)

                WSSAT is an open source web service security scanning tool which provides a dynamic environment to add, update or delete vulnerabilities by just editing its configuration files. This tool accepts WSDL address list as input file and performs both static and dynamic tests against the security vulnerabilities. It also makes information disclosure controls.Objectives of WSSAT are to allow organizations:Perform their web services security analysis at onceSee overall security assessment with reportsHarden their web servicesWSSAT's main capabilities include:Dynamic Testing:Insecure Communication; SSL Not Used Unauthenticated Service Method; Error Based SQL Injection; Cross Site Scripting; XML Bomb; External Entity Attack - XXE XPATH Injection; Verbose SOAP Fault MessageStatic Analysis:Weak XML Schema: Unbounded Occurrences; Weak XML Schema: Undefined Namespace; Weak WS-SecurityPolicy: Insecure Transport; Weak WS-SecurityPolicy: Insufficient Supporting Token Protection; Weak WS-SecurityPolicy: Tokens Not ProtectedInformation Leakage: Server or development platform oriented information disclosureWSSAT's main modules are:ParserVulnerabilities LoaderAnalyzer/AttackerLoggerReport GeneratorThe main difference of WSSAT is to create a dynamic vulnerability management environment instead of embedding the vulnerabilities into the code. More information can be found here: https://github.com/YalcinYolalan/WSSAT

                </details>
                

### Red Teaming / AppSec

<details><summary><strong>[Dradis: Collaboration and Reporting for InfoSec Teams](https://github.com/rmusser01/Infosec_Reference/blob/master/Draft/Docs_and_Reports.md?plain=1)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Daniel Martin](https://img.shields.io/badge/Daniel%20Martin-informational)

                Dradis is an extensible, cross-platform, open source collaboration framework for InfoSec teams. It can import from over 19 popular tools, including Nessus, Qualys, and Burp. Started in 2007, the Dradis Framework project has been growing ever since (15,000 commits in the last 12 months). Dradis is the best tool to consolidate the output of different scanners, add your manual findings and evidence and have all the engagement information in one place.Come to see the latest Dradis release in action. It's loaded with updates including new tool, connectors (Metasploit, Brakeman, ...), full REST API coverage, testing methodologies and lots of interface improvements (issue tagging, UX improvements and much more). Come and find out why Dradis is being downloaded over 300 times every week. Come and check it out before we run out of stickers!

                </details>
                

### Red Teaming / Embedded

<details><summary><strong>[Firmware Analysis Toolkit (FAT)](https://github.com/adi0x90/attifyos)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Aditya Gupta](https://img.shields.io/badge/Aditya%20Gupta-informational)

                There exists a number of tools in today's security industry which offers static and dynamic analysis of software binaries and mobile applications. However, there is no such toolkit, which helps an embedded or IoT security researcher to analyse firmwares in an in-depth level. FAT or Firmware Analysis Toolkit is a scriptable toolkit suite is a part of Attify's internal pentesting suite which has helped us reduce a significant number of man hours put into firmware analysis in our IoT and smart devices pentest engagements. It comes with an easy to use API which can then be used in additional analysis, as well as for research purposes. It is a toolkit suite which performs static and dynamic analysis of firmwares, also enabling the user to emulate the firmware and having a live firmware device as if a real physical device was sitting on the network. This has been done by taking advantage of Qemu emulation and static vulnerability identification techniques. Below are some of the capabilities of the toolkit : Full emulation of the firmware along with networking Dynamic traffic analysis Static vulnerability identification Integration with tools such as nmap and metasploit for additional assessment and exploitationBy Black Hat EU, there might be more features added to the list which I will later on send once they are in a more concrete stage. FAT has been made possible because of the following open source tools listed below, which FAT leverages at various stages:Binwalk Firmware Modification KitFirmadyneMITMProxyNmapMetasploitSnmpwalkRadare2

                </details>
                
<details><summary><strong>[HEATHEN Internet of Things Pentesting Framework](https://github.com/chihebchebbi/Internet-Of-Things-Pentesting-Framework)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Red Teaming / Embedded](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20Embedded-purple) ![Chiheb Chebbi](https://img.shields.io/badge/Chiheb%20Chebbi-informational)

                Oxford defines the Internet of Things as: "A proposed development of the Internet in which everyday objects have network connectivity, allowing them to send and receive data."Heathen IoT of Things Penetration Testing Framework developed as a research project, which automatically help developers and manufacturers build more secure products in the Internet of Things space based on the Open Web Application Security Project (OWASP) by providing a set of features in every fundamental era:Insecure Web InterfaceInsufficient Authentication/AuthorizationInsecure Network ServicesLack of Transport EncryptionPrivacy ConcernsInsecure Cloud InterfaceInsecure Mobile InterfaceInsufficient Security ConfigurabilityInsecure Software/FirmwarePoor Physical Security

                </details>
                

### Mobile Security

<details><summary><strong>[Nmap on Android](https://github.com/kost/NetworkMapper)</strong></summary>

                ![BH-EU-16](https://img.shields.io/badge/BH-EU-16-blue) ![Category: Mobile Security](https://img.shields.io/badge/Category:%20Mobile%20Security-yellow) ![Vlatko Kosturjak](https://img.shields.io/badge/Vlatko%20Kosturjak-informational)

                Network Mapper is Android frontend for well known Nmap scanner. Frontend will help you to download, install and run Nmap on Android-based phone. It is also a collection of tools to build all known Android architectures: arm, mips and x86 in 32/64 bit architectures.Shiny new 2.0 release will be presented with easy interface and mobile specific scans.

                </details>
                
