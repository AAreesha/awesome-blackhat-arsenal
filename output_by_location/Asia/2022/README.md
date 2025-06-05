# Asia 2022
---
## 🧠 Tools by Category
### Red Teaming / AppSec

<details><summary><strong>[AISY: A Framework for Deep Learning-Based Side-Channel Analysis](https://github.com/AISyLab/AISY_Framework)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Stjepan Picek](https://img.shields.io/badge/Stjepan%20Picek-informational)

                Profiling side-channel attacks (SCA) allow evaluators to verify the worst-case security scenario of their products. Nowadays, deep learning has become the state-of-the-art method for profiling SCA as deep neural networks show the ability to learn side-channel leakages from protected implementations. While deep learning is a powerful technique for security evaluations, it offers numerous possibilities for neural network configurations and optimization techniques. Selecting the best setup for each evaluated product is far from trivial and requires expertise in SCA and deep learning fields. To improve SCA methods, and at the same time to be able to investigate the resistance of the product to more complex attack scenarios, researchers continuously propose new techniques.
Unfortunately, several obstacles are making the acceptance of such techniques a challenge. Security evaluators from the industry face difficulties following up on new promising methods. What is more, certification bodies also must be aware of new SCA techniques to issue the certifications. Indeed, one of the main issues is the lack of publicly available, easy-to-use frameworks that allow powerful and reliable side-channel analysis. Moreover, due to the absence of the uniformed evaluation/implementation method, the reproducibility of the outcomes is not easy to ensure.

We propose AISY as a tool to allow state-of-the-art deep learning-based SCA. AISY is a python-based open-source framework, and it provides state-of-the-art functionalities for profiling SCA with easy usage, extensibility, reproducibility, integrated database, and user interface. We envision a system where the user can efficiently run the attacks with few lines of code and based on state-of-the-art but also extend those functionalities to support new developments. AISY supports the complete development cycle for deep learning-based SCA: from dataset preparation to the automated development of new models and their assessment concerning the side-channel metrics.

                </details>
                
<details><summary><strong>[Kinstrument: Binary-Only Instrumentation Framework for Linux Kernel Based on Breakpoint](https://github.com/hac425xxx/hac425xxx)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Red Teaming / AppSec](https://img.shields.io/badge/Category:%20Red%20Teaming%20/%20AppSec-red) ![Sili Luo](https://img.shields.io/badge/Sili%20Luo-informational)

                For regular Linux kernels, we can use qemu or vmware, and then use gdb to debug the kernel, but for some special embedded devices, such as Android phones, it is difficult to debug and instrument the kernel. In order to debug the kernel, it often needs to recompile the kernel and use additional hardware.

The characteristics of kinstrument are as follows:

1. The kernel only needs to support the insertion of the ko module, the kernel does not need to be recompiled, and no additional hardware is required.
2. Support instrumentation basic blocks, and get basic block coverage of kernel code
3. Use the breakpoint mechanism to hook and debug arbitrary instructions.


Kinstrument can be used for kernel debugging and Fuzz.

                </details>
                

### Blue Team & Detection

<details><summary><strong>[Hayabusa](https://github.com/YamatoSecurity)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Blue Team & Detection](https://img.shields.io/badge/Category:%20Blue%20Team%20&%20Detection-cyan) ![Zach Mathis](https://img.shields.io/badge/Zach%20Mathis-informational)

                Hayabusa is a sigma-based threat hunting and fast forensics timeline generator for Windows event logs written in rust by Yamato Security. Rules can either be written sigma or built-in hayabusa rules that let the analyst extract out only the important fields for Windows DFIR investigations.

                </details>
                

### Web/AppSec

<details><summary><strong>[NtHiM (Now, the Host is Mine!): Super Fast Sub-Domain Takeover Detection](https://github.com/TheBinitGhimire/NtHiM)</strong></summary>

                ![BH-ARSENAL](https://img.shields.io/badge/BH-ARSENAL-blue) ![Category: Web/AppSec](https://img.shields.io/badge/Category:%20Web/AppSec-blue) ![Binit Ghimire](https://img.shields.io/badge/Binit%20Ghimire-informational)

                NtHiM, which stands for "Now, the Host is Mine!" is a Rust-based systems project, which enables security enthusiasts to discover subdomain takeover vulnerabilities in hostnames (domains and subdomains) from different organizations.


In this session, I will be discussing about the following things, apart from an introduction of myself as the project maintainer and your presenter for this session.

Project Overview
Brief Introduction (what this project actually is)
Initiation Story (how I decided to start working on this project)
Brief Logic Explanation (understanding the project workflow with a simple pseudocode)
Project Features (getting to know about all of the things built into the project)
User-level Video Documentation (Demonstration; including guides for the end-users of this project)
Developer-level Video Documentation (Demonstration; including guides on how you can get started with extending or contributing to this project)

                </details>
                
