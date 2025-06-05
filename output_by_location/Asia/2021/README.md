# Asia 2021
---
## 🧠 Tools by Category
### Red Teaming / AppSec

<details><summary><strong>[Adversarial Threat Detector](https://github.com/gyoisamurai/Adversarial-Threat-Detector)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Isao Takaesu](https://img.shields.io/badge/Isao%20Takaesu-informational)

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

                </details>
                

### Red Teaming

<details><summary><strong>[CANalyse: A Vehicle Network Analysis and Attack Tool](https://github.com/KartheekLade/CANalyse)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Kartheek Lade](https://img.shields.io/badge/Kartheek%20Lade-informational)

                CANalyse is a software tool built to analyze the log files to find out unique data sets automatically and able to connect to simple attacker interfaces such as Telegram. Basically, while using this tool you can provide your bot-ID and be able to use the tool over the internet through telegram. It is made to be installed inside a raspberry-PI and able to exploit the vehicle through a telegram bot by recording and analyzing the data logs, it is like a hardware implant planted inside a car which acts as a bridge between the Telegram bot and the Vehicle's network.

                </details>
                
<details><summary><strong>[Empire: Post-Exploitation Framework](https://github.com/txuswashere/Pentesting-Windows/blob/main/README.md)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Anthony Rose](https://img.shields.io/badge/Anthony%20Rose-informational) ![Jake Krasnov](https://img.shields.io/badge/Jake%20Krasnov-informational)

                Empire is a Command and Control (C2) framework powered by Python 3 that supports Windows, Linux, and macOS exploitation. It leverages many widely used offensive security tools through PowerShell, Python 3, and C# agents. At the same time, it offers cryptologically-secure communications and flexible modular architecture that links Advanced Persistent Threats (APTs) Tactics, Techniques, and Procedures (TTPs) through the MITRE ATT&CK database.

Empire has evolved significantly since its introduction in 2015 and has become one of the most widely used open-source C2 platforms. Through this time, Empire has advanced from a single user experience to allowing multiple user operations through an API with Empire acting as a teamserver. Currently, 2 different applications are available to connect to the Empire teamserver: Empire Command Line Interface (CLI) and Starkiller.

The Empire CLI is built from the ground up as a replacement to the embedded legacy CLI and gives users a familiar feel of the legacy CLI, but is portable and connects through the Empire API. While Starkiller is a cross-platform UI available in Linux, Windows, and macOS powered by ElectronJS.

The framework's flexibility to easily incorporate new modules allows for a single solution for red team operations with the aim for Empire to provide an easy-to-use platform for emulating APTs. Customization is essential to any successful red team operation, which has driven the expansion of user plugins. These plugins allow any custom program to run side-by-side with the Empire teamserver. In addition, the commonality between other C2 platforms allows profiles and modules to be easily dropped in without the need for additional development. These features allow both red and blue teams to easily emulate and defend against the APT attack vectors.

                </details>
                
<details><summary><strong>[OWFuzz: WiFi Protocol Fuzzing Tool Based on OpenWiFi](https://github.com/alipay/Owfuzz/blob/main/README.md?plain=1)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Hongjian Cao](https://img.shields.io/badge/Hongjian%20Cao-informational)

                Generally, when using WiFi Fuzzing Tool to test the security of WiFi protocol, you need a WiFi USB dongle that supports monitor mode and set the WiFi USB dongle to monitor mode to listen and inject arbitrary WiFi frames. However, many WiFi USB dongles fail to meet our expectations. For example, some are not stable enough in monitor mode and often get stuck, which leads to the interruption of the fuzzing process. And some, we don't have complete control over some frame fields.

OWFuzz is a WiFi protocol testing tool using OpenWiFi. OpenWiFi is an open-source WiFi protocol stack based on SDR that is fully compatible with Linux mac80211. It's driver takes advantage of the Linux kernel's supports (mac80211, cfg80211) for WiFi high MAC, so it can provide an interface to the application layer like a common WiFi USB dongle. In The hardware part, CSMA/CA protocol and other functions of WiFi low MAC layer are implemented on FPGA. It supports monitoring and injection of arbitrary WiFi frames，The application layer software can also directly communicate with the OpenWiFi driver/FPGA/RF underlying functions through nl80211, which provides users with great autonomous and controllable ability. OWFuzz is the first to use OpenWiFi platform (Xilinx ZC706 dev board + FMCOMMS3) to implements a WiFi protocol fuzzing test framework, which supports the fuzzing test of all WiFi frames and the interactivity testing of WiFi protocols.

This research introduces a comprehensive overview of the OWFuzz. We will introduce its architecture, implementation (arbitrary frame and protocol interactivity fuzzing test), and how it works. And finally we will have a video demonstration.

                </details>
                
<details><summary><strong>[Red Kube](https://github.com/KaplanOpenSource/israeli-opensource-companies)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming](https://img.shields.io/badge/Category:%20Red%20Teaming-red) ![Or Azarzar](https://img.shields.io/badge/Or%20Azarzar-informational)

                Red Kube is a red team cheat sheet based on kubectl commands to Asses the Kubernetes Cluster Security Posture.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[Identify iOS Malicious Code Based on MachO File Structure](https://gist.github.com/LucaMell/bb7fa6c7ff58f5869b793e7ba85a187d?short_path=897e916)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Shijie Cao](https://img.shields.io/badge/Shijie%20Cao-informational)

                iOS Malicious Bit Hunter is a malicious plug-in detection engine for iOS applications. It can analyze the head of the macho file of the injected dylib dynamic library based on runtime, and can perform behavior analysis through interface input characteristics to determine the behavior of the dynamic library feature. The program does not rely on the jailbreak environment and can be used on the AppStore.

                </details>
                

### Web/AppSec or Red Teaming

<details><summary><strong>[KICS](https://github.com/bashis/The-Federation-WWE-Roster-Viewer/blob/master/Resources%20(READ%20README!)/wrestlers/wrestlergen/last.txt)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec or Red Teaming](https://img.shields.io/badge/Category:%20Web/AppSec%20or%20Red%20Teaming-blue) ![Erez Yalon](https://img.shields.io/badge/Erez%20Yalon-informational) ![Ori Bendet](https://img.shields.io/badge/Ori%20Bendet-informational)

                KICS is an open-source solution for static code analysis of Infrastructure as Code. It finds security vulnerabilities, compliance issues, and infrastructure misconfigurations in the following Infrastructure as Code solutions: Terraform, Kubernetes, Docker, AWS CloudFormation, Ansible. And more to come. Over 1000 rules are already available.

                </details>
                

### Social Engineering / General

<details><summary><strong>[SniperPhish: The Web-Email Spear Phishing Toolkit](https://github.com/GemGeorge/SniperPhish)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Social Engineering / General](https://img.shields.io/badge/Category:%20Social%20Engineering%20/%20General-pink) ![Gem George](https://img.shields.io/badge/Gem%20George-informational)

                Spear Phishing campaigns are commonly used to test employees' awareness in a company/organization. This exercise involves mostly the combination of phishing emails and websites. An effective campaign requires sophisticated methods starting from designing a phishing website to executing payload at the target in an undetectable manner. A platform is required to send emails to targeted users and tracking campaign progress. This basically involves the use of a mail server (to send email) and a web server (to host phishing website). To collect campaign data, these two domains need to be considered. Precisely, the campaign required to track email delivery status and the data submitted in the phishing website.

Usually, the data from these two domains can be collected easily, but it is more challenging and time-consuming when these data are to be consolidated and address questions such as which victim in the mail submitted data through the website. SniperPhish comes in handy here so that the data is tracked centrally, and displays the consolidated data in its dashboard.

SniperPhish is an advanced Web-Email spear-phishing toolkit developed in PHP to conduct professional phishing assessments. The abstract idea behind this toolkit is to simulate, combine, and centrally track all campaigns that involve email and phishing websites. SniperPhish supports tracking data from web site containing n number of pages. The data submitted in the phishing website containing multiple pages are tracked sequentially with email campaigns. The advanced customization in the report generation module helps to customize column fields and export in multiple outputs. In addition to the core campaign module, SniperPhish also provides additional functionalities such as hosting phishing websites, payload generation, encryption options, and options to convert payloads to FUD using different methods (eg: conversion to reflective DLL/PE).

                </details>
                

### Web/AppSec

<details><summary><strong>[Threagile: The Open-Source Agile Threat Modeling Toolkit](https://github.com/cschneider4711)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Christian Schneider](https://img.shields.io/badge/Christian%20Schneider-informational)

                The open-source tool Threagile enables agile teams to create a threat model directly from within the IDE using a declarative approach: Given information about the data assets, technical assets, communication links, and trust boundaries as input in a simple to maintain YAML file, it executes a set of over 40 built-in risk rules, which can be extended with custom risk rules, against the processed model. The resulting artifacts are graphical diagrams, Excel, and PDF reports about the identified risks, their rating, and the mitigation steps as well as risk tracking state. DevSecOps pipelines can be enriched with Threagile as well to process the JSON output.

                </details>
                
