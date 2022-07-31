# simple-crawler

## Description
This repository is intended for a practical technical test in order to measure code standards, development skills, writing level, abstractions and other technical requirements of software development like code pattern, read language documentation and libraries, and use the git versioning system. 

The project proposes a challenge of mining data in some web pages using the Python language and some of its libraries. The project proposes the development of a crawler that navigates in two different pages, [being this web page from Vultr](https://www.vultr.com/products/bare-metal/#pricing) one and [this one from Hostgator](https://www.hostgator.com/vps-hosting) and from there extract some data, like:
- CPU / VCPU
- MEMORY
- STORAGE / SSD DISK
- BANDWIDTH / TRANSFER
- PRICE [ $/mo ]

## Index
   * [Description](#Description)
   * [Prerequisites](#Prerequisites)
   * [Setup](#Setup)
   * [Execution](#Execution)
        * [Example](#Example)
   * [Version](#Version)
   * [Authors](#Authors)
   * [License](#License)


## Prerequisites

### The following tools are necessary to properly execute the code in this project

1. Python 3 correctly installed on host [see here](https://www.python.org/) for more details about.
2. Any code editor, visual studio code sugested [see here](https://code.visualstudio.com/).

## Setup

### This section explains the necessary steps to execute de projet and test it locally to verify all the ouput data and test other requirements

1. Clone the repository
    - To clone the repository run the code `git clone https://github.com/IanAlves21/simple-crawler.git`.
2. On the clone repository enter the folder by running `cd path/to/the/folder`.
3. Inside the project folder run `pip install -r requirements.txt`.
4. If no errors, then the project is ready to run and test.

## Execution

### To execute the project it is necessary to import the created classes and use the methods created such ass `print`, `save_json` and `save_csv`. The code bellow exemplifies this process in a python file.

~~~python
from src.crawler.hostgatorCrawler import HostgatorCrawler
from src.crawler.VultrCrawler import VultrCrawler

h = HostgatorCrawler()

h.print()
h.save_csv()
h.save_json()

v = VultrCrawler()

v.print()
v.save_csv()
v.save_json()
~~~

### Files generated from the execution above
![image](https://user-images.githubusercontent.com/31904421/182031940-76336965-bcf0-4865-8aec-7b8c211a82c5.png)

### Example of the execution the code above
![image](https://user-images.githubusercontent.com/31904421/182031886-e0e738d3-8c42-405e-a787-ba401e029340.png)

## Version

It was used [GitHub](https://github.com/) for version control. For available versions, look at [tags in this repository](https://github.com/IanAlves21/simple-crawler/tags). 

## Authors

* **Ian Gustavo Alves Pessoa Silva**
    * *Main developer* - developed all features
    * GitHub Profile [here](https://github.com/IanAlves21/).
    * LinkedIn Profile [here](https://www.linkedin.com/in/ian-gustavo-alves-pessoa-silva-8bb328150/) 


## License

This project is under license - see file [LICENSE](https://github.com/IanAlves21/simple-crawler/blob/main/LICENSE) for more details.