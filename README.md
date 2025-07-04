<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Ollama Chat</h3>

  <p align="center">
    A custom wrapper utility for a local deployment of the open-source Ollama 3:8b LLM
    <br />
    <br />
    <a href="https://github.com/acm-udayton/acm-ollama-chat/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/acm-udayton/acm-ollama-chat/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Ollama Chat Screen Shot][product-screenshot]]([product-screenshot])

This project provides the source code for a CLI to interact with a local Ollama LLM installed on the University of Dayton ACM chapter's server. Currently we are running llama3:8b as our LLM of choice, providing a balance between function and efficiency.

All users on the server have access to the CLI tool, and active development in the form of issues, forks, and commits by any club member is welcome! 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Docker][Docker]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Set up an instance of the Ollama within a Docker container.
   ```sh
   docker pull ollama/ollama
   docker run -d -v ollama:root/.ollama -p 11434:11434 --name ollama ollama/ollama
   docker exec -it ollama ollama pull llama3:8b

   # Optionally, set a restart policy for ollama to restart unless stopped by a user.
   docker update --restart unless-stopped ollama
   ```

### Installation 

### Fresh install (not needed on ACM server)

1. Clone the repo (on Debian filesystem)
   ```sh
   mkdir -p /opt/ollama-chat
   cd /opt/
   git clone https://github.com/acm-udayton/acm-ollama-chat/repo_name.git .
   ```
2. Install Python packages in a virtual environment
   ```sh
   sudo python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Restrict file permissions
   ```sh
   sudo chown -R <your_username>:<your_username> /opt/ollama-chat/
   ```
4. Make the script executable as a command
   ```sh
   chmod +x /opt/ollama-chat/ollama_chat.sh
   sudo ln -s /opt/ollama-chat/ollama_chat.sh /usr/local/bin/ollama-chat
   ```

### Update an existing installation (should be owner of the initial install)

1. Update the source code version from the repo
   ```sh
   git checkout <branch-name>
   ```
2. Update and install Python packages your virtual environment
   ```sh
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Restrict file permissions
   ```sh
   sudo chown -R <your-username>:<your-username> /opt/ollama-chat/
   ```
4. Make the script executable as a command
   ```sh
   chmod +x /opt/ollama-chat/ollama_chat.sh
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To start a conversation via Ollama Chat, log into your account on the University of Dayton ACM server and run the command `ollama-chat`.

When you're done, use 'exit' or 'quit' to end the Ollama Chat instance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- Be the first to request a new feature!

See the [open issues](https://github.com/acm-udayton/acm-ollama-chat/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/acm-udayton/acm-ollama-chat/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=acm-udayton/acm-ollama-chat" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Questions? Contact [Joseph Lefkovitz][contact-link], Vice President - ACM at University of Dayton

Project Link: [https://github.com/acm-udayton/acm-ollama-chat](https://github.com/acm-udayton/acm-ollama-chat)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/acm-udayton/acm-ollama-chat.svg?style=for-the-badge
[contributors-url]: https://github.com/acm-udayton/acm-ollama-chat/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/acm-udayton/acm-ollama-chat.svg?style=for-the-badge
[forks-url]: https://github.com/acm-udayton/acm-ollama-chat/network/members
[stars-shield]: https://img.shields.io/github/stars/acm-udayton/acm-ollama-chat.svg?style=for-the-badge
[stars-url]: https://github.com/acm-udayton/acm-ollama-chat/stargazers
[issues-shield]: https://img.shields.io/github/issues/acm-udayton/acm-ollama-chat.svg?style=for-the-badge
[issues-url]: https://github.com/acm-udayton/acm-ollama-chat/issues
[license-shield]: https://img.shields.io/github/license/acm-udayton/acm-ollama-chat.svg?style=for-the-badge
[license-url]: https://github.com/acm-udayton/acm-ollama-chat/blob/main/LICENSE
[product-screenshot]: images/docs-project-screenshot.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org
[Docker]: https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white&style=for-the-badge
[Docker-url]: https://www.docker.com
[Contact-link]: https://github.com/lefkovitzj