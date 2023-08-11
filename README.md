# C2Live: Tracking C2 Malicious IPs Over Time

![C2Live Logo](logo.png)

C2Live is an open-source project aimed at providing a comprehensive and interactive platform for tracking Command and Control (C2) malicious IP addresses over time. This project focuses on categorizing and visualizing these IPs based on the framework they are associated with and the country they originate from. The goal is to help security professionals, researchers, and organizations gain insights into the evolving landscape of cyber threats.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Command and Control (C2) servers play a critical role in many cyberattacks, allowing malicious actors to control compromised systems remotely. Tracking these C2 IPs is essential for detecting and mitigating cyber threats effectively. C2Live aims to provide a user-friendly interface for visualizing the distribution of these IPs based on various parameters, helping users understand attack patterns and trends.

## Features

- **Interactive Map:** C2Live offers an interactive map that allows users to visualize the geographic distribution of malicious C2 IPs over time.
- **Framework Tracking:** The project categorizes C2 IPs based on the specific malware or attack framework they are associated with, making it easier to identify related threats.
- **Temporal Analysis:** Users can track the changes in C2 IPs over time, enabling the identification of emerging threats and trends.
- **Country Analysis:** C2Live provides insights into the countries from which these malicious IPs originate, aiding in understanding global threat landscapes.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/installing/) package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/C2Live.git
