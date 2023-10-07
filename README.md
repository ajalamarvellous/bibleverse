Bibleverse

==============================
<!-- ABOUT THE PROJECT -->
## About The Project

## Idea:

One morning, I was feeling somehow, not great actually and I wanted to remember on particular bible verse that was speaking to how I was feeling, but I couldn't remember exactly the verse, so I thought, how about a tool to help me find Bible verses that are speaking to your circumstance?

## Solution:

Bibleverse is a commandline and web tool that helps you find the bible verses that speak the most to your circumstance
<div align="center">
    <img width="815" alt="Screenshot 2023-10-06 at 22 19 39" src="https://github.com/ajalamarvellous/bibleverse/assets/31284870/876484a2-77f4-4bef-be3c-398888cc3e52">
    <img width="1350" alt="Screenshot 2023-10-06 at 22 41 27" src="https://github.com/ajalamarvellous/bibleverse/assets/31284870/77014a88-d520-448c-95d3-f03f78860bd5">
</div>


### Built With

* [PyPDF2](https://pypi.org/project/PyPDF2/)
* [Gensim](https://pypi.org/project/gensim/)
* [Streamlit](https://streamlit.io)

## Folder structure
------------
```text
    ├── LICENSE            <- The Project Licence for the project.
    ├── CONDUCT.md         <- Code of Conduct for contributions.
    ├── README.md          <- The top-level README about the project.
    ├── requirements.txt   <- The requirements file for reproducing the project 
    │                        
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    
    |   ├── base.py        <- main preprocessing file 
    |   ├── process.py     <- Preprocessing pdf file to convert to formats usable 
    |   ├── cli.py         <- script to run the project on the commandline
    │   └── web.py         <- script to run the project on the web
    │        
    ├── assets       
    │   └─ Scripture_for_Every_Moment.pdf   <- file to load the data from
    |     
    └── test    <- test suite for the project
         └─ test_process.py  <- 
```

<!-- GETTING STARTED -->
## Getting Started

To get started and set up the project in your local environment, please download the packages listed in the requirements

### Installation

1. Create a virtual environment
    ```sh
    python -m venv .venv
    ```
2. Activate the virtual environment
    ```sh
    source .venv/bin/activate
    ```
3. Clone the repo
   ```sh
   git clone https://github.com/Ajalamarvellous/bibleverse.git
   ```
4. Install the necessary packages
   ```sh
   pip install requirements
   ```

   And you are ready to rumble


<!-- USAGE EXAMPLES -->
## Usage

To try out the software, you can use the commandline or through the web.

To use the commandline
```sh
python src/cli.py
```

To use the web service
```sh
streamlit run src/web.py
```
Voila, there you go, you have it running on your device

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

Please check the `CONTRIBUTING.md` on important information to contribute to this project


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



<!-- CONTRIBUTING -->
## Contributing

- Ajala, Marvellous - [@madeofajala](https://twitter.com/madeofajala)- ajalaoluwamayowa00@gmail.com

Project Link: [https://github.com/ajalamarvellous/bibleverse](https://github.com/ajalamarvellous/bibleverse)

